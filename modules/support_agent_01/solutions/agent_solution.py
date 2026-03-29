"""Customer Support Agent — SOLUTION (Starter Tier).

CCA-F Exam Domain: D1 Agentic Architecture (~27%)

This is the complete reference implementation of the agentic loop.
Every pattern here is exam-correct. Comments explain WHY each choice matters.

Key exam patterns demonstrated:
- stop_reason-based loop control (NOT text parsing — AP1)
- max_iterations as safety net only (NOT primary control — AP2)
- tool_result blocks with matching tool_use_id
- Structured error responses with isError/isRetryable (AP6, AP7)
- Customer verification before order/refund operations
"""

from __future__ import annotations


import json
from typing import Any

import anthropic

# ---------------------------------------------------------------------------
# Tool Definitions — identical to starter/agent.py
# These are redefined here so the solution is self-contained.
# In production you would import from a shared module.
# ---------------------------------------------------------------------------

TOOLS: list[dict[str, Any]] = [
    {
        "name": "get_customer",
        "description": (
            "Look up a customer by ID (CUST-xxx) or email. "
            "MUST be called before any order lookup or refund to verify customer identity. "
            "Returns customer profile with kyc_verified flag."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Customer ID (CUST-xxx) or email address",
                },
            },
            "required": ["customer_id"],
        },
    },
    {
        "name": "lookup_order",
        "description": (
            "Look up an order by ID (ORD-xxxx). Returns order details including "
            "status, total, items, and refund eligibility. "
            "Requires prior customer verification via get_customer."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "Order ID in format ORD-xxxx",
                },
            },
            "required": ["order_id"],
        },
    },
    {
        "name": "process_refund",
        "description": (
            "Process a refund for an order. Validates amount <= order total and amount > 0. "
            "Returns requires_approval: true if amount > $500. "
            "Requires prior customer verification via get_customer."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "Order ID to refund",
                },
                "amount": {
                    "type": "number",
                    "description": "Refund amount in USD",
                },
                "reason": {
                    "type": "string",
                    "description": "Reason for the refund",
                },
            },
            "required": ["order_id", "amount", "reason"],
        },
    },
    {
        "name": "escalate_to_human",
        "description": (
            "Escalate to a human agent. "
            "Valid reasons ONLY: customer_request, policy_gap, capability_limit. "
            "NEVER escalate based on sentiment or confidence scores."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "case_summary": {
                    "type": "string",
                    "description": "Summary of the case for the human agent",
                },
                "customer_id": {
                    "type": "string",
                    "description": "Customer ID",
                },
                "reason": {
                    "type": "string",
                    "enum": ["customer_request", "policy_gap", "capability_limit"],
                    "description": "Escalation reason — must be one of the 3 valid triggers",
                },
                "priority": {
                    "type": "string",
                    "enum": ["low", "normal", "high", "urgent"],
                    "description": "Case priority level",
                    "default": "normal",
                },
            },
            "required": ["case_summary", "customer_id", "reason"],
        },
    },
]

# ---------------------------------------------------------------------------
# Mock Data — simulates fintech-mock MCP server responses.
# In production, these would be real MCP tool calls.
# ---------------------------------------------------------------------------

_MOCK_CUSTOMERS: dict[str, dict[str, Any]] = {
    "CUST-001": {
        "customer_id": "CUST-001",
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "account_id": "ACC-001",
        "status": "active",
        "kyc_verified": True,
        "created_at": "2024-01-15T10:00:00Z",
    },
    "CUST-002": {
        "customer_id": "CUST-002",
        "name": "Bob Smith",
        "email": "bob@example.com",
        "account_id": "ACC-002",
        "status": "active",
        "kyc_verified": True,
        "created_at": "2024-03-20T14:30:00Z",
    },
    "CUST-003": {
        "customer_id": "CUST-003",
        "name": "Charlie Brown",
        "email": "charlie@example.com",
        "account_id": "ACC-003",
        "status": "suspended",
        "kyc_verified": False,
        "created_at": "2024-06-01T09:00:00Z",
    },
}

_MOCK_ORDERS: dict[str, dict[str, Any]] = {
    "ORD-1001": {
        "order_id": "ORD-1001",
        "customer_id": "CUST-001",
        "total": 249.99,
        "status": "delivered",
        "items": [
            {"name": "Wireless Headphones", "quantity": 1, "price": 199.99},
            {"name": "USB-C Cable", "quantity": 2, "price": 25.00},
        ],
        "created_at": "2024-11-10T08:00:00Z",
        "refund_eligible": True,
    },
    "ORD-1002": {
        "order_id": "ORD-1002",
        "customer_id": "CUST-002",
        "total": 899.00,
        "status": "delivered",
        "items": [
            {"name": "Ergonomic Office Chair", "quantity": 1, "price": 899.00},
        ],
        "created_at": "2024-10-05T12:00:00Z",
        "refund_eligible": True,
    },
    "ORD-1003": {
        "order_id": "ORD-1003",
        "customer_id": "CUST-001",
        "total": 59.99,
        "status": "shipped",
        "items": [
            {"name": "Phone Case", "quantity": 1, "price": 29.99},
            {"name": "Screen Protector", "quantity": 1, "price": 30.00},
        ],
        "created_at": "2024-12-01T16:00:00Z",
        "refund_eligible": False,
    },
}


def execute_tool(tool_name: str, tool_input: dict[str, Any]) -> str:
    """Execute a tool call by dispatching to simulated fintech-mock responses.

    Exam-correct patterns:
    - ALWAYS returns a JSON string (never empty, never None) — avoids AP7
    - Error responses include isError + isRetryable fields — avoids AP6
    - Structured error with human-readable message for the model to relay

    Args:
        tool_name: Name of the tool to execute.
        tool_input: Input parameters for the tool.

    Returns:
        JSON string with the tool result or structured error.
    """
    # WHY: We dispatch by tool name, not by parsing model text. Each tool
    # handler returns structured data the model can reason about.
    try:
        if tool_name == "get_customer":
            return _handle_get_customer(tool_input)
        elif tool_name == "lookup_order":
            return _handle_lookup_order(tool_input)
        elif tool_name == "process_refund":
            return _handle_process_refund(tool_input)
        elif tool_name == "escalate_to_human":
            return _handle_escalate(tool_input)
        else:
            # WHY: Unknown tools get a structured error, not a silent failure.
            # The model sees isError=True and knows not to retry (isRetryable=False).
            return json.dumps({
                "error": f"Unknown tool: {tool_name}",
                "isError": True,
                "isRetryable": False,
            })
    except Exception as exc:
        # WHY: Catch-all ensures we NEVER return None or raise to the loop.
        # AP7 says: never silently suppress errors. We surface them structured.
        return json.dumps({
            "error": str(exc),
            "isError": True,
            "isRetryable": True,
        })


def _handle_get_customer(tool_input: dict[str, Any]) -> str:
    """Simulate get_customer tool from fintech-mock MCP server."""
    customer_id = tool_input.get("customer_id", "")

    # Support lookup by email as well as by ID
    customer: dict[str, Any] | None = _MOCK_CUSTOMERS.get(customer_id)
    if customer is None:
        # Try email lookup
        for cust in _MOCK_CUSTOMERS.values():
            if cust["email"] == customer_id:
                customer = cust
                break

    if customer is None:
        return json.dumps({
            "error": f"Customer not found: {customer_id}",
            "isError": True,
            "isRetryable": False,
        })

    return json.dumps({"customer": customer, "verified": True})


def _handle_lookup_order(tool_input: dict[str, Any]) -> str:
    """Simulate lookup_order tool from fintech-mock MCP server."""
    order_id = tool_input.get("order_id", "")
    order = _MOCK_ORDERS.get(order_id)

    if order is None:
        return json.dumps({
            "error": f"Order not found: {order_id}",
            "isError": True,
            "isRetryable": False,
        })

    return json.dumps({"order": order})


def _handle_process_refund(tool_input: dict[str, Any]) -> str:
    """Simulate process_refund tool from fintech-mock MCP server."""
    order_id = tool_input.get("order_id", "")
    amount = tool_input.get("amount", 0)
    reason = tool_input.get("reason", "")

    order = _MOCK_ORDERS.get(order_id)
    if order is None:
        return json.dumps({
            "error": f"Order not found: {order_id}",
            "isError": True,
            "isRetryable": False,
        })

    if not order.get("refund_eligible", False):
        return json.dumps({
            "error": f"Order {order_id} is not eligible for refund (status: {order['status']})",
            "isError": True,
            "isRetryable": False,
        })

    if amount <= 0:
        return json.dumps({
            "error": "Refund amount must be greater than 0",
            "isError": True,
            "isRetryable": False,
        })

    if amount > order["total"]:
        return json.dumps({
            "error": f"Refund amount ${amount} exceeds order total ${order['total']}",
            "isError": True,
            "isRetryable": False,
        })

    # WHY: Refunds over $500 require manager approval. The tool returns
    # requires_approval=True so the model can inform the customer.
    requires_approval = amount > 500
    refund_id = f"REF-{order_id.split('-')[1]}"

    return json.dumps({
        "refund_id": refund_id,
        "order_id": order_id,
        "amount": amount,
        "reason": reason,
        "status": "pending_approval" if requires_approval else "processed",
        "requires_approval": requires_approval,
    })


def _handle_escalate(tool_input: dict[str, Any]) -> str:
    """Simulate escalate_to_human tool."""
    valid_reasons = {"customer_request", "policy_gap", "capability_limit"}
    reason = tool_input.get("reason", "")

    # WHY: Even though the schema has an enum, we validate server-side too.
    # Defense in depth — the schema constrains the model, the handler validates.
    if reason not in valid_reasons:
        return json.dumps({
            "error": f"Invalid escalation reason: '{reason}'. Valid: {sorted(valid_reasons)}",
            "isError": True,
            "isRetryable": False,
        })

    return json.dumps({
        "escalation_id": "ESC-5001",
        "status": "created",
        "assigned_to": "support-team-queue",
        "priority": tool_input.get("priority", "normal"),
        "case_summary": tool_input.get("case_summary", ""),
        "customer_id": tool_input.get("customer_id", ""),
        "reason": reason,
    })


# ---------------------------------------------------------------------------
# System Prompt — encodes business rules the model should follow.
# NOTE: Prompts provide guidance but are NOT guaranteed enforcement.
# For guaranteed enforcement, use hooks (see intermediate tier).
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are a customer support agent for FinTech Corp. You help customers with \
account inquiries, order lookups, and refund processing.

CRITICAL RULES:
1. ALWAYS verify the customer first using get_customer before any order lookup \
or refund operation. Never skip this step.
2. When processing refunds, check that the order is refund-eligible before proceeding.
3. For escalations, only use the 3 valid reasons: customer_request, policy_gap, \
capability_limit. NEVER escalate based on customer sentiment or your confidence level.
4. Always provide clear, helpful responses. If a tool returns an error, explain \
the issue to the customer in plain language.
5. If a refund requires manager approval (>$500), inform the customer that their \
refund is pending approval and provide the refund ID for tracking.

You have access to the following tools:
- get_customer: Look up customer by ID or email (always call first)
- lookup_order: Look up order details by order ID
- process_refund: Process a refund for an eligible order
- escalate_to_human: Escalate to a human agent when needed
"""


def run_support_agent(
    user_message: str,
    *,
    max_iterations: int = 25,
    model: str = "claude-sonnet-4-6-20250514",
) -> str:
    """Run the customer support agent loop.

    This implements the core agentic loop — the #1 exam pattern for CCA-F.

    The loop terminates based on stop_reason (exam-correct), NOT by parsing
    the model's text output (anti-pattern #1). max_iterations is a safety net
    only (anti-pattern #2 would be using it as primary control).

    Args:
        user_message: The customer's support request.
        max_iterations: Safety net limit (NOT primary loop control).
        model: Claude model to use.

    Returns:
        The agent's final text response to the customer.
    """
    # WHY: anthropic.Anthropic() reads ANTHROPIC_API_KEY from env automatically.
    # Never hardcode API keys (coding convention).
    client = anthropic.Anthropic()

    # WHY: Messages list is the conversation state. We start with the user's
    # initial message and accumulate assistant responses + tool results.
    messages: list[dict[str, Any]] = [
        {"role": "user", "content": user_message},
    ]

    # WHY: max_iterations is a SAFETY NET, not primary loop control.
    # The loop's real termination condition is stop_reason == "end_turn".
    # If we hit max_iterations, something went wrong (infinite tool loop).
    for _iteration in range(max_iterations):
        # Step 1: Call the Messages API with tools
        response = client.messages.create(
            model=model,
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages,
        )

        # Step 2: Check stop_reason — THIS is the primary loop control.
        # WHY: stop_reason is the ONLY correct way to determine loop behavior.
        # - "end_turn" means the model is done and has a final response
        # - "tool_use" means the model wants to call one or more tools
        # - "max_tokens" means we hit the output limit (handle gracefully)
        # Anti-pattern #1: NEVER parse response text for "I'm done" or similar.

        if response.stop_reason == "end_turn":
            # Extract the final text response from content blocks
            # WHY: Response content is a list of blocks. We find the text block(s)
            # and concatenate them for the final answer.
            text_parts: list[str] = []
            for block in response.content:
                if block.type == "text":
                    text_parts.append(block.text)
            return "\n".join(text_parts) if text_parts else ""

        if response.stop_reason == "tool_use":
            # Step 3a: FIRST append the full assistant response to messages.
            # WHY: The API requires the conversation history to be coherent.
            # The assistant message contains tool_use blocks that the subsequent
            # tool_result blocks must reference by ID. If we skip this append,
            # the API cannot correlate tool results to tool requests.
            messages.append({"role": "assistant", "content": response.content})

            # Step 3b: Process each tool_use block and collect results.
            # WHY: A single response can contain MULTIPLE tool_use blocks
            # (parallel tool calls). We must process all of them and return
            # all results in a SINGLE user message.
            tool_results: list[dict[str, Any]] = []

            for block in response.content:
                if block.type == "tool_use":
                    # Execute the tool and get the result string
                    result = execute_tool(block.name, block.input)

                    # WHY: Each tool_result MUST include tool_use_id matching
                    # the tool_use block's id. Without this, the API cannot
                    # match results to requests and will error.
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    })

            # Step 3c: Append ALL tool results in a single user message.
            # WHY: Multiple tool results go in ONE user message as an array
            # of content blocks, not as separate messages. The API requires
            # role alternation (assistant → user → assistant → ...).
            messages.append({"role": "user", "content": tool_results})

            # Continue the loop — the model will process tool results and
            # either make more tool calls or produce a final response.
            continue

        if response.stop_reason == "max_tokens":
            # WHY: If we hit max_tokens, the model was cut off mid-response.
            # We return what we have rather than silently dropping it.
            text_parts = []
            for block in response.content:
                if block.type == "text":
                    text_parts.append(block.text)
            partial = "\n".join(text_parts)
            return f"{partial}\n\n[Response truncated — max_tokens reached]"

        # Any other stop_reason is unexpected; surface it rather than silently
        # continuing (AP7: never suppress errors).
        return f"[Unexpected stop_reason: {response.stop_reason}]"

    # WHY: This is the safety net. If we get here, we exhausted max_iterations
    # without the model producing an end_turn. This indicates a potential
    # infinite tool-calling loop. AP2: this is a safety net, NOT primary control.
    return (
        "[Agent safety limit reached] The support agent exceeded its maximum "
        f"iteration count ({max_iterations}). This usually indicates a tool-calling "
        "loop. Please try rephrasing your request or contact support."
    )


# ---------------------------------------------------------------------------
# Quick manual test (not used by pytest — just for interactive debugging)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Example: customer asks about an order refund
    result = run_support_agent(
        "Hi, I'm Alice Johnson (CUST-001). I'd like a refund on order ORD-1001 "
        "because the headphones arrived damaged."
    )
    print(result)
