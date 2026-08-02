"""Customer Support Agent — Intermediate Tier (Agent SDK with Hooks).

CCA-F Exam Domain: D1 Agentic Architecture (~27%)

This exercise teaches PROGRAMMATIC ENFORCEMENT — the #1 tested concept.
You will add PreToolUse and PostToolUse hooks to enforce business rules
that CANNOT be left to prompt guidance alone.

Key concepts tested:
- PreToolUse hooks DENY unauthorized tool calls BEFORE execution
- PostToolUse hooks TRACK state changes and FLAG compliance concerns
- Hooks are PROGRAMMATIC — they cannot be bypassed by the model
- This is the key distinction: prompts can be ignored, hooks cannot
"""

from __future__ import annotations


from dataclasses import dataclass, field
from typing import Any


# ---------------------------------------------------------------------------
# Hook State — tracks verified customers and compliance flags
# ---------------------------------------------------------------------------

@dataclass
class AgentState:
    """Mutable state tracked across the agent's tool calls.

    This state is used by hooks to enforce business rules programmatically.
    """

    verified_customers: set[str] = field(default_factory=set)
    compliance_warnings: list[str] = field(default_factory=list)
    tool_call_log: list[dict[str, Any]] = field(default_factory=list)


# ---------------------------------------------------------------------------
# PreToolUse Hook — DENY unauthorized tool calls BEFORE they execute
# ---------------------------------------------------------------------------

def pre_tool_use_hook(
    tool_name: str,
    tool_input: dict[str, Any],
    state: AgentState,
) -> dict[str, Any] | None:
    """PreToolUse hook: enforce business rules before tool execution.

    TODO: Implement these checks:

    1. If tool_name is "process_refund" or "lookup_order":
       - Check if ANY customer has been verified (state.verified_customers is not empty)
       - If NOT verified, return a DENIAL:
         {"denied": True, "reason": "Customer must be verified before order/refund operations"}
       - This is PROGRAMMATIC enforcement — the model cannot bypass this

    2. If tool_name is "escalate_to_human":
       - Validate that tool_input["reason"] is one of the 3 valid triggers
       - If invalid reason, return denial with message explaining valid triggers
       - Key exam point: this PREVENTS anti-patterns #4 and #5 programmatically

    3. If all checks pass, return None (allow the tool call)

    Args:
        tool_name: Name of the tool being called.
        tool_input: Input parameters for the tool.
        state: Current agent state.

    Returns:
        None to allow the call, or dict with {"denied": True, "reason": "..."} to block it.
    """
    # TODO: Implement pre-tool-use checks
    raise NotImplementedError("Implement pre_tool_use_hook — enforce rules BEFORE execution")


# ---------------------------------------------------------------------------
# PostToolUse Hook — TRACK state and FLAG compliance concerns
# ---------------------------------------------------------------------------

def post_tool_use_hook(
    tool_name: str,
    tool_input: dict[str, Any],
    tool_result: str,
    state: AgentState,
) -> str:
    """PostToolUse hook: track state changes and flag compliance concerns.

    TODO: Implement these behaviors:

    1. Log every tool call to state.tool_call_log with:
       {"tool": tool_name, "input": tool_input, "result_preview": tool_result[:200]}

    2. If tool_name is "get_customer":
       - Parse the result JSON
       - If successful (no "error" key), add customer_id to state.verified_customers
       - This enables the PreToolUse hook to allow subsequent order/refund calls

    3. If tool_name is "process_refund":
       - Parse the result JSON
       - If refund amount > $500 (check tool_input["amount"]):
         - Add compliance warning to state.compliance_warnings:
           "HIGH_VALUE_REFUND: ${amount} refund for order {order_id} requires manager approval"
         - This is a FLAG, not a BLOCK — the refund proceeds but is logged

    4. Return the original tool_result (hooks observe, they don't modify results)

    Args:
        tool_name: Name of the tool that was called.
        tool_input: Input parameters that were used.
        tool_result: JSON string result from the tool.
        state: Current agent state (mutate in place).

    Returns:
        The original tool_result string (unmodified).
    """
    # TODO: Implement post-tool-use tracking
    raise NotImplementedError("Implement post_tool_use_hook — track state and flag concerns")


# ---------------------------------------------------------------------------
# Agent Runner with Hook Integration
# ---------------------------------------------------------------------------

def run_agent_with_hooks(
    user_message: str,
    *,
    max_turns: int = 20,
    max_budget_usd: float = 2.0,
    model: str = "claude-sonnet-4-6",
) -> dict[str, Any]:
    """Run the support agent with hook-based enforcement.

    TODO: Implement the agent loop with hooks integrated:

    1. Initialize AgentState
    2. For each turn in the agentic loop:
       a. Call the Messages API (same as starter tier)
       b. Check stop_reason (same as starter tier)
       c. For each tool_use block:
          - FIRST: Call pre_tool_use_hook(). If denied, create a tool_result
            with the denial message (the model sees why the call was blocked)
          - IF ALLOWED: Execute the tool
          - AFTER execution: Call post_tool_use_hook() to track state
          - Build the tool_result content block
       d. Append results and continue loop

    3. Return a dict with:
       {
           "response": final_text,
           "state": {
               "verified_customers": list(state.verified_customers),
               "compliance_warnings": state.compliance_warnings,
               "tool_calls": len(state.tool_call_log),
           }
       }

    Key exam concepts demonstrated:
    - Hooks provide GUARANTEED enforcement (prompt says "must verify" → hook BLOCKS without verification)
    - State tracking enables multi-step business rules (verify → then allow refund)
    - Compliance warnings are logged but don't block operations (flag vs block distinction)

    Args:
        user_message: The customer's request.
        max_turns: Safety net for loop iterations.
        max_budget_usd: Budget limit for API calls.
        model: Claude model to use.

    Returns:
        Dict with response text and state summary.
    """
    # TODO: Implement the agent loop with hooks
    raise NotImplementedError("Implement run_agent_with_hooks — agentic loop + hooks")
