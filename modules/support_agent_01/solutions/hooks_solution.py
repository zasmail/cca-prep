"""Customer Support Agent with Hooks — SOLUTION (Intermediate Tier).

CCA-F Exam Domain: D1 Agentic Architecture (~27%)

This is the complete reference implementation of hook-based enforcement.
The #1 tested concept: programmatic enforcement vs prompt-based guidance.

Key exam patterns demonstrated:
- PreToolUse hooks DENY unauthorized calls BEFORE execution (AP3)
- PostToolUse hooks TRACK state and FLAG compliance concerns
- Hooks are PROGRAMMATIC — the model cannot bypass them
- This is the key distinction: prompts can be ignored, hooks cannot
- State tracking enables multi-step business rules (verify then allow)
"""

from __future__ import annotations


import json
from dataclasses import dataclass, field
from typing import Any

import anthropic

# ---------------------------------------------------------------------------
# Reuse tool definitions and mock data from the agent solution.
# We use a relative import so the solutions package is self-contained
# regardless of how the parent directories are named or aliased.
# ---------------------------------------------------------------------------

from .agent_solution import (
    SYSTEM_PROMPT,
    TOOLS,
    execute_tool,
)


# ---------------------------------------------------------------------------
# Hook State — tracks verified customers and compliance flags.
# WHY dataclass: Provides typed, structured state (not raw dicts).
# The exam tests that you understand structured state management.
# ---------------------------------------------------------------------------

@dataclass
class AgentState:
    """Mutable state tracked across the agent's tool calls.

    This state is used by hooks to enforce business rules programmatically.
    Each field serves a specific enforcement or compliance purpose.
    """

    # WHY set: O(1) lookup for "has this customer been verified?"
    # PreToolUse checks this before allowing order/refund operations.
    verified_customers: set[str] = field(default_factory=set)

    # WHY list: Compliance warnings accumulate over the conversation.
    # These are FLAGS (logged for audit) not BLOCKS (they don't stop operations).
    compliance_warnings: list[str] = field(default_factory=list)

    # WHY list of dicts: Full audit trail of every tool call.
    # Exam tests that you log calls for observability, not just for enforcement.
    tool_call_log: list[dict[str, Any]] = field(default_factory=list)


# ---------------------------------------------------------------------------
# PreToolUse Hook — DENY unauthorized tool calls BEFORE they execute
#
# WHY this matters for the exam:
# Anti-pattern #3 says "prompt-based enforcement for critical business rules."
# The system prompt says "verify customer first" — but the model COULD ignore it.
# This hook makes it IMPOSSIBLE to call process_refund or lookup_order without
# prior verification. That is the difference between guidance and enforcement.
# ---------------------------------------------------------------------------

# WHY constant: Avoids magic strings scattered across the hook. If the valid
# reasons change, we update one place. Matches the enum in the tool schema.
_VALID_ESCALATION_REASONS = {"customer_request", "policy_gap", "capability_limit"}


def pre_tool_use_hook(
    tool_name: str,
    tool_input: dict[str, Any],
    state: AgentState,
) -> dict[str, Any] | None:
    """PreToolUse hook: enforce business rules before tool execution.

    Returns None to allow the call, or a denial dict to block it.
    The denial dict is returned to the model as a tool_result so it
    understands WHY the call was blocked and can adjust its behavior.

    Exam-correct patterns:
    - Checks verified_customers BEFORE allowing order/refund ops
    - Validates escalation reasons against the 3 valid triggers
    - Returns structured denial the model can reason about

    Args:
        tool_name: Name of the tool being called.
        tool_input: Input parameters for the tool.
        state: Current agent state with verification tracking.

    Returns:
        None to allow the call, or dict with denied=True and reason.
    """
    # Rule 1: process_refund and lookup_order require prior customer verification.
    # WHY: This is PROGRAMMATIC enforcement of the "verify first" business rule.
    # Even if the prompt says "verify first," the model might skip it.
    # This hook makes skipping IMPOSSIBLE — the call is denied before execution.
    if tool_name in ("process_refund", "lookup_order"):
        if not state.verified_customers:
            return {
                "denied": True,
                "reason": (
                    "Customer must be verified before order/refund operations. "
                    "Call get_customer first to verify the customer's identity."
                ),
            }

    # Rule 2: escalate_to_human must use one of the 3 valid triggers.
    # WHY: Anti-patterns #4 and #5 say sentiment and confidence are NOT valid.
    # The schema enum constrains the model, but this hook is defense-in-depth.
    # If the model somehow sends an invalid reason (e.g., via prompt injection),
    # this hook blocks it before it reaches the escalation system.
    if tool_name == "escalate_to_human":
        reason = tool_input.get("reason", "")
        if reason not in _VALID_ESCALATION_REASONS:
            return {
                "denied": True,
                "reason": (
                    f"Invalid escalation reason: '{reason}'. "
                    f"Valid reasons are: {sorted(_VALID_ESCALATION_REASONS)}. "
                    "Do NOT escalate based on customer sentiment or confidence scores."
                ),
            }

    # All checks passed — return None to allow the tool call.
    # WHY None specifically: the caller checks `if result is not None` to detect
    # denials. Returning an empty dict would be truthy and ambiguous.
    return None


# ---------------------------------------------------------------------------
# PostToolUse Hook — TRACK state changes and FLAG compliance concerns
#
# WHY this matters for the exam:
# PostToolUse hooks are OBSERVERS, not GATEKEEPERS. They:
# 1. Update state that PreToolUse hooks depend on (verified_customers)
# 2. Flag compliance concerns for audit (high-value refunds)
# 3. Log all tool calls for observability
# They NEVER modify the tool result — that is the contract.
# ---------------------------------------------------------------------------

def post_tool_use_hook(
    tool_name: str,
    tool_input: dict[str, Any],
    tool_result: str,
    state: AgentState,
) -> str:
    """PostToolUse hook: track state changes and flag compliance concerns.

    This hook OBSERVES but does NOT MODIFY the tool result. It mutates
    the AgentState in place to track verified customers and compliance flags.

    Exam-correct patterns:
    - Logs every call to tool_call_log (observability)
    - Adds verified customers to state (enables PreToolUse checks)
    - Flags high-value refunds (compliance, not blocking)
    - Returns tool_result UNMODIFIED (observer contract)

    Args:
        tool_name: Name of the tool that was called.
        tool_input: Input parameters that were used.
        tool_result: JSON string result from the tool.
        state: Current agent state (mutated in place).

    Returns:
        The original tool_result string, unmodified.
    """
    # Step 1: Log every tool call for audit trail.
    # WHY: Observability is a key exam concept. Every tool invocation should
    # be traceable. We truncate the result preview to avoid bloating the log.
    state.tool_call_log.append({
        "tool": tool_name,
        "input": tool_input,
        "result_preview": tool_result[:200],
    })

    # Step 2: Track verified customers after successful get_customer.
    # WHY: This is the STATE BRIDGE between PostToolUse and PreToolUse.
    # When get_customer succeeds, we add the customer_id to verified_customers.
    # This enables the PreToolUse hook to allow subsequent order/refund calls.
    # Without this state tracking, the PreToolUse hook would block everything.
    if tool_name == "get_customer":
        try:
            parsed = json.loads(tool_result)
            # Only mark as verified if the lookup succeeded (no "error" key).
            # WHY: A failed lookup (customer not found) should NOT count as
            # verification. The PreToolUse hook should continue blocking.
            if "error" not in parsed:
                customer_id = tool_input.get("customer_id", "")
                # Also extract customer_id from the response in case the
                # input was an email and the response has the canonical ID.
                if "customer" in parsed:
                    customer_id = parsed["customer"].get("customer_id", customer_id)
                state.verified_customers.add(customer_id)
        except (json.JSONDecodeError, KeyError):
            # WHY: If we can't parse the result, we don't mark as verified.
            # Fail-safe: deny by default, require explicit verification.
            pass

    # Step 3: Flag high-value refunds for compliance.
    # WHY: This is a FLAG, not a BLOCK. The refund proceeds but is logged
    # so a compliance officer can review it. The exam tests that you understand
    # the difference between flagging (PostToolUse) and blocking (PreToolUse).
    if tool_name == "process_refund":
        amount = tool_input.get("amount", 0)
        if amount > 500:
            order_id = tool_input.get("order_id", "unknown")
            state.compliance_warnings.append(
                f"HIGH_VALUE_REFUND: ${amount} refund for order {order_id} "
                "requires manager approval"
            )

    # Step 4: Return the original result UNMODIFIED.
    # WHY: PostToolUse hooks observe, they don't modify. This is the contract.
    # If you need to transform tool results, that belongs in a different layer
    # (e.g., a result transformer middleware), not in a compliance hook.
    return tool_result


# ---------------------------------------------------------------------------
# Agent Runner with Hook Integration
#
# This combines the agentic loop from the starter tier with the hook
# enforcement from this tier. The key addition: between "model requests
# tool call" and "tool executes," we insert the PreToolUse check.
# After execution, we insert the PostToolUse tracking.
# ---------------------------------------------------------------------------

def run_agent_with_hooks(
    user_message: str,
    *,
    max_turns: int = 20,
    max_budget_usd: float = 2.0,
    model: str = "claude-sonnet-4-6",
) -> dict[str, Any]:
    """Run the support agent with hook-based enforcement.

    This extends the starter tier's agentic loop with PreToolUse and
    PostToolUse hooks that provide GUARANTEED business rule enforcement.

    The loop structure is identical to the starter tier, with hooks
    inserted at the tool-call boundary:
      model requests tool -> PreToolUse check -> execute (or deny) -> PostToolUse track

    Args:
        user_message: The customer's request.
        max_turns: Safety net for loop iterations (NOT primary control).
        max_budget_usd: Budget limit for API calls (not enforced in this demo).
        model: Claude model to use.

    Returns:
        Dict with response text and state summary including verified
        customers, compliance warnings, and tool call count.
    """
    client = anthropic.Anthropic()
    state = AgentState()

    messages: list[dict[str, Any]] = [
        {"role": "user", "content": user_message},
    ]

    for _turn in range(max_turns):
        response = client.messages.create(
            model=model,
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages,
        )

        # WHY: stop_reason-based loop control, same as starter tier.
        # This is the exam-correct pattern (AP1, AP2).
        if response.stop_reason == "end_turn":
            text_parts: list[str] = []
            for block in response.content:
                if block.type == "text":
                    text_parts.append(block.text)
            final_text = "\n".join(text_parts) if text_parts else ""

            # WHY: Return both the response AND the state summary.
            # The state summary shows what the hooks tracked/enforced,
            # which is the whole point of this tier.
            return {
                "response": final_text,
                "state": {
                    "verified_customers": sorted(state.verified_customers),
                    "compliance_warnings": state.compliance_warnings,
                    "tool_calls": len(state.tool_call_log),
                },
            }

        if response.stop_reason == "tool_use":
            # WHY: Append assistant message FIRST, same as starter tier.
            # The conversation history must include the tool_use blocks
            # so tool_result blocks can reference them by ID.
            messages.append({"role": "assistant", "content": response.content})

            tool_results: list[dict[str, Any]] = []

            for block in response.content:
                if block.type == "tool_use":
                    # --- HOOK INTEGRATION POINT ---

                    # Step A: PreToolUse hook — check BEFORE execution.
                    # WHY: This is where programmatic enforcement happens.
                    # If the hook returns a denial, we skip execute_tool entirely
                    # and return the denial message as the tool_result.
                    # The model sees the denial and adjusts (e.g., calls
                    # get_customer first before retrying the refund).
                    denial = pre_tool_use_hook(block.name, block.input, state)

                    if denial is not None:
                        # WHY: The denial becomes the tool_result content.
                        # The model receives this as if the tool returned an error,
                        # so it can reason about what went wrong and correct course.
                        # We use is_error=True so the model knows this failed.
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": json.dumps({
                                "error": denial["reason"],
                                "denied_by_hook": True,
                                "isError": True,
                                "isRetryable": True,
                            }),
                            "is_error": True,
                        })
                        continue

                    # Step B: Execute the tool (hook allowed it).
                    result = execute_tool(block.name, block.input)

                    # Step C: PostToolUse hook — track AFTER execution.
                    # WHY: The hook updates state (verified_customers) and
                    # flags compliance concerns (high-value refunds).
                    # It returns the result UNMODIFIED — observer contract.
                    result = post_tool_use_hook(block.name, block.input, result, state)

                    # Step D: Build the tool_result content block.
                    # WHY: tool_use_id MUST match block.id for API correlation.
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    })

            # WHY: All tool results in a single user message, same as starter.
            messages.append({"role": "user", "content": tool_results})
            continue

        if response.stop_reason == "max_tokens":
            text_parts = []
            for block in response.content:
                if block.type == "text":
                    text_parts.append(block.text)
            partial = "\n".join(text_parts)
            return {
                "response": f"{partial}\n\n[Response truncated — max_tokens reached]",
                "state": {
                    "verified_customers": sorted(state.verified_customers),
                    "compliance_warnings": state.compliance_warnings,
                    "tool_calls": len(state.tool_call_log),
                },
            }

        # Unexpected stop_reason
        return {
            "response": f"[Unexpected stop_reason: {response.stop_reason}]",
            "state": {
                "verified_customers": sorted(state.verified_customers),
                "compliance_warnings": state.compliance_warnings,
                "tool_calls": len(state.tool_call_log),
            },
        }

    # Safety net exhausted
    return {
        "response": (
            "[Agent safety limit reached] Exceeded maximum turn count "
            f"({max_turns}). This usually indicates a tool-calling loop."
        ),
        "state": {
            "verified_customers": sorted(state.verified_customers),
            "compliance_warnings": state.compliance_warnings,
            "tool_calls": len(state.tool_call_log),
        },
    }


# ---------------------------------------------------------------------------
# Quick manual test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    result = run_agent_with_hooks(
        "Hi, I'm customer CUST-002. I need a refund on order ORD-1002 "
        "because the chair arrived with a broken armrest."
    )
    print("Response:", result["response"])
    print("State:", json.dumps(result["state"], indent=2))
