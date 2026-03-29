"""Tests for Module 01 Intermediate — Hook Enforcement.

These tests validate that hooks provide PROGRAMMATIC enforcement,
not just prompt-based guidance. This is the #1 tested concept on the CCA-F exam.
"""

import json

import pytest

from modules.support_agent_01.intermediate.agent_with_hooks import (
    AgentState,
    post_tool_use_hook,
    pre_tool_use_hook,
)


class TestPreToolUseHook:
    """AP3: Critical business rules must be enforced programmatically, not via prompts."""

    def test_hook_denies_refund_without_customer_verification(self) -> None:
        """process_refund MUST be denied if no customer has been verified.

        Anti-pattern #3: This rule cannot be left to the system prompt.
        The hook GUARANTEES enforcement regardless of what the model tries.
        """
        state = AgentState()  # No verified customers

        result = pre_tool_use_hook(
            "process_refund",
            {"order_id": "ORD-1001", "amount": 100.0, "reason": "defective"},
            state,
        )

        assert result is not None, "Hook must return a denial dict when customer not verified"
        assert result.get("denied") is True, "Denial must have denied=True"
        assert "reason" in result, "Denial must include a reason"

    def test_hook_denies_order_lookup_without_customer_verification(self) -> None:
        """lookup_order MUST also be denied without prior customer verification."""
        state = AgentState()

        result = pre_tool_use_hook(
            "lookup_order",
            {"order_id": "ORD-1001"},
            state,
        )

        assert result is not None, "Hook must deny lookup_order without verification"
        assert result.get("denied") is True

    def test_hook_allows_refund_after_customer_verification(self) -> None:
        """Once a customer is verified, process_refund should be allowed."""
        state = AgentState()
        state.verified_customers.add("CUST-001")

        result = pre_tool_use_hook(
            "process_refund",
            {"order_id": "ORD-1001", "amount": 100.0, "reason": "defective"},
            state,
        )

        assert result is None, "Hook must return None (allow) when customer is verified"

    def test_hook_denies_invalid_escalation_reason(self) -> None:
        """Escalation with invalid reason must be denied programmatically.

        Anti-patterns #4, #5: Sentiment and confidence are NOT valid triggers.
        The hook prevents these from ever reaching the tool.
        """
        state = AgentState()

        # Sentiment-based — INVALID (AP5)
        result = pre_tool_use_hook(
            "escalate_to_human",
            {
                "case_summary": "Customer is angry",
                "customer_id": "CUST-001",
                "reason": "customer_sentiment",
            },
            state,
        )

        assert result is not None, "Hook must deny invalid escalation reasons"
        assert result.get("denied") is True


class TestPostToolUseHook:
    """Hooks track state and flag compliance concerns."""

    def test_post_hook_tracks_verified_customers(self) -> None:
        """After successful get_customer, the customer ID must be added
        to state.verified_customers. This enables the PreToolUse check."""
        state = AgentState()

        customer_result = json.dumps({
            "customer": {"customer_id": "CUST-001", "name": "Alice"},
            "verified": True,
        })

        post_tool_use_hook("get_customer", {"customer_id": "CUST-001"}, customer_result, state)

        assert "CUST-001" in state.verified_customers, (
            "PostToolUse hook must add customer to verified_customers set "
            "after successful get_customer call."
        )

    def test_post_hook_flags_high_value_refund(self) -> None:
        """Refunds >$500 must generate a compliance warning.

        The warning is a FLAG, not a BLOCK — the refund proceeds but is logged.
        """
        state = AgentState()

        refund_result = json.dumps({
            "refund_id": "REF-1001",
            "amount": 899.00,
            "requires_approval": True,
        })

        post_tool_use_hook(
            "process_refund",
            {"order_id": "ORD-1002", "amount": 899.00, "reason": "wrong item"},
            refund_result,
            state,
        )

        assert len(state.compliance_warnings) > 0, (
            "PostToolUse hook must flag high-value refunds (>$500) "
            "with a compliance warning."
        )

    def test_post_hook_logs_all_tool_calls(self) -> None:
        """Every tool call must be logged to state.tool_call_log."""
        state = AgentState()

        post_tool_use_hook(
            "get_customer",
            {"customer_id": "CUST-001"},
            json.dumps({"customer": {"customer_id": "CUST-001"}}),
            state,
        )

        assert len(state.tool_call_log) == 1, "Each tool call must be logged"
        assert state.tool_call_log[0]["tool"] == "get_customer"

    def test_post_hook_returns_result_unmodified(self) -> None:
        """PostToolUse hooks observe but do NOT modify the tool result."""
        state = AgentState()
        original = json.dumps({"customer": {"customer_id": "CUST-001"}})

        returned = post_tool_use_hook(
            "get_customer",
            {"customer_id": "CUST-001"},
            original,
            state,
        )

        assert returned == original, "PostToolUse hook must return the result unmodified"
