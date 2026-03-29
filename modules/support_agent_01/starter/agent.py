"""Customer Support Agent — Starter Tier (Raw Messages API).

CCA-F Exam Domain: D1 Agentic Architecture (~27%)

This exercise teaches the MOST IMPORTANT exam pattern: the agentic loop.
You will implement a customer support agent using the raw Anthropic Messages API.

Key concepts tested:
- Loop MUST terminate on stop_reason, NOT by parsing response text
- Tool results MUST include tool_use_id matching the tool_use block
- max_iterations is a SAFETY NET, not primary loop control
- Customer verification MUST happen before any order/refund operations
"""

from __future__ import annotations


import json
from typing import Any

import anthropic

# ---------------------------------------------------------------------------
# Tool Definitions — these get passed to the API in the `tools` parameter.
# Note: tool descriptions ENCODE business rules (exam-tested concept).
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


def execute_tool(tool_name: str, tool_input: dict[str, Any]) -> str:
    """Execute a tool call by dispatching to the MCP server or local handler.

    TODO: Implement this function.
    - Connect to the fintech-mock MCP server OR simulate tool responses
    - Return a JSON string with the tool result
    - On error, return structured error: {"error": "msg", "code": "X", "isError": true, "isRetryable": false}
    - NEVER return empty string or None on failure (anti-pattern #7)
    """
    # TODO: Implement tool dispatch
    raise NotImplementedError("Implement execute_tool — dispatch to fintech-mock MCP server")


def run_support_agent(
    user_message: str,
    *,
    max_iterations: int = 25,
    model: str = "claude-sonnet-4-6-20250514",
) -> str:
    """Run the customer support agent loop.

    This is the core agentic loop — the #1 exam pattern.

    TODO: Implement the agentic loop following these steps:

    1. Initialize the Anthropic client and messages list
    2. Create the system prompt (include business rules for the support context)
    3. Enter the loop:
       a. Call client.messages.create() with model, system, tools, and messages
       b. Check response.stop_reason:
          - "end_turn" → extract final text response and return it
          - "tool_use" → process tool calls (step 4)
          - Other → handle appropriately
       c. CRITICAL: The loop condition MUST be based on stop_reason == "tool_use"
          Do NOT parse response text to decide whether to continue.
          Do NOT use iteration count as PRIMARY termination (it's a safety net only).

    4. Processing tool calls:
       a. FIRST: Append the full assistant response to messages
          (messages.append({"role": "assistant", "content": response.content}))
       b. THEN: For each tool_use block in response.content:
          - Extract tool name and input
          - Call execute_tool(name, input)
          - Build a tool_result content block:
            {"type": "tool_result", "tool_use_id": block.id, "content": result}
       c. Append ALL tool results in a single user message:
          messages.append({"role": "user", "content": [tool_result_blocks]})

    5. Safety net: if max_iterations reached, return a message indicating
       the agent hit its safety limit (this should rarely happen in practice)

    Args:
        user_message: The customer's support request.
        max_iterations: Safety net limit (NOT primary loop control).
        model: Claude model to use.

    Returns:
        The agent's final text response to the customer.
    """
    # TODO: Implement the agentic loop
    raise NotImplementedError("Implement run_support_agent — the core agentic loop")
