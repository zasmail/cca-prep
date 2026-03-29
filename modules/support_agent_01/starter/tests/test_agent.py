"""Tests for Module 01 Starter — Customer Support Agent (Raw Messages API).

These tests validate EXAM-CORRECT patterns, not just "does it run."
Each test name describes the specific CCA-F pattern being validated.

Tests use mocked API responses to validate BEHAVIOR, not source code inspection.
"""

from __future__ import annotations

import json
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest


def _make_text_block(text: str) -> SimpleNamespace:
    """Create a mock TextBlock."""
    return SimpleNamespace(type="text", text=text)


def _make_tool_use_block(
    tool_id: str, name: str, input_data: dict
) -> SimpleNamespace:
    """Create a mock ToolUseBlock."""
    return SimpleNamespace(type="tool_use", id=tool_id, name=name, input=input_data)


def _make_response(
    stop_reason: str, content: list
) -> SimpleNamespace:
    """Create a mock Messages API response."""
    return SimpleNamespace(stop_reason=stop_reason, content=content)


class TestLoopTermination:
    """AP1: Loop MUST use stop_reason, not text parsing."""

    def test_loop_uses_stop_reason_not_text_parsing(self) -> None:
        """The agentic loop must continue when stop_reason == 'tool_use'
        and terminate when stop_reason == 'end_turn'.

        Anti-pattern #1: Parsing natural language for loop termination.
        """
        from modules.support_agent_01.starter.agent import run_support_agent

        # Arrange: Mock a 2-turn conversation
        # Turn 1: model calls get_customer (stop_reason = "tool_use")
        # Turn 2: model responds with text (stop_reason = "end_turn")
        turn1 = _make_response("tool_use", [
            _make_tool_use_block("tu_001", "get_customer", {"customer_id": "CUST-001"}),
        ])
        turn2 = _make_response("end_turn", [
            _make_text_block("Hello Alice, how can I help you today?"),
        ])

        mock_client = MagicMock()
        mock_client.messages.create.side_effect = [turn1, turn2]

        with patch("modules.support_agent_01.starter.agent.anthropic") as mock_anthropic, \
             patch("modules.support_agent_01.starter.agent.execute_tool") as mock_exec:
            mock_anthropic.Anthropic.return_value = mock_client
            mock_exec.return_value = json.dumps({
                "customer": {"customer_id": "CUST-001", "name": "Alice Johnson"},
                "verified": True,
            })

            # Act
            result = run_support_agent("I need help with my account")

        # Assert: The loop made exactly 2 API calls (tool_use → end_turn)
        assert mock_client.messages.create.call_count == 2, (
            "Agent should call API twice: once getting tool_use, once getting end_turn. "
            "If it called more or fewer, the loop isn't using stop_reason correctly."
        )
        assert "Alice" in result, (
            "Agent should return the final text response from the end_turn message."
        )

    def test_loop_handles_multiple_tool_calls(self) -> None:
        """Agent should process ALL tool_use blocks in a single response
        before making the next API call.
        """
        from modules.support_agent_01.starter.agent import run_support_agent

        # Arrange: Turn 1 has TWO tool calls, Turn 2 is end_turn
        turn1 = _make_response("tool_use", [
            _make_tool_use_block("tu_001", "get_customer", {"customer_id": "CUST-001"}),
            _make_tool_use_block("tu_002", "lookup_order", {"order_id": "ORD-1001"}),
        ])
        turn2 = _make_response("end_turn", [
            _make_text_block("Your order ORD-1001 has been delivered."),
        ])

        mock_client = MagicMock()
        mock_client.messages.create.side_effect = [turn1, turn2]

        with patch("modules.support_agent_01.starter.agent.anthropic") as mock_anthropic, \
             patch("modules.support_agent_01.starter.agent.execute_tool") as mock_exec:
            mock_anthropic.Anthropic.return_value = mock_client
            mock_exec.return_value = json.dumps({"status": "ok"})

            # Act
            run_support_agent("Check my order")

        # Assert: execute_tool called twice (once per tool_use block)
        assert mock_exec.call_count == 2, (
            "Both tool_use blocks in a single response must be executed. "
            "The agent should process ALL blocks, not just the first one."
        )


class TestToolResultFormat:
    """Tool results must include tool_use_id matching the tool_use block."""

    def test_tool_results_include_tool_use_id(self) -> None:
        """Each tool_result content block must have a tool_use_id field that
        matches the id from the corresponding tool_use block.
        """
        from modules.support_agent_01.starter.agent import run_support_agent

        # Arrange
        turn1 = _make_response("tool_use", [
            _make_tool_use_block("tu_abc123", "get_customer", {"customer_id": "CUST-001"}),
        ])
        turn2 = _make_response("end_turn", [
            _make_text_block("Done."),
        ])

        mock_client = MagicMock()
        mock_client.messages.create.side_effect = [turn1, turn2]

        with patch("modules.support_agent_01.starter.agent.anthropic") as mock_anthropic, \
             patch("modules.support_agent_01.starter.agent.execute_tool") as mock_exec:
            mock_anthropic.Anthropic.return_value = mock_client
            mock_exec.return_value = json.dumps({"customer": {"customer_id": "CUST-001"}})

            # Act
            run_support_agent("Help me")

        # Assert: The second API call should include tool_result with matching tool_use_id
        second_call_args = mock_client.messages.create.call_args_list[1]
        messages = second_call_args.kwargs.get("messages") or second_call_args[1].get("messages", [])

        # Find the user message with tool_result blocks
        tool_result_msgs = [
            m for m in messages
            if m.get("role") == "user"
            and isinstance(m.get("content"), list)
            and any(
                (c.get("type") == "tool_result" if isinstance(c, dict) else False)
                for c in m["content"]
            )
        ]
        assert len(tool_result_msgs) > 0, (
            "Must send tool_result content blocks back to the API in a user message."
        )

        # Check the tool_use_id matches
        tool_results = [
            c for c in tool_result_msgs[-1]["content"]
            if isinstance(c, dict) and c.get("type") == "tool_result"
        ]
        assert any(tr.get("tool_use_id") == "tu_abc123" for tr in tool_results), (
            "tool_result must include tool_use_id matching the tool_use block's id ('tu_abc123'). "
            "Without this, the API cannot correlate results to requests."
        )


class TestErrorHandling:
    """AP6, AP7: Errors must be structured, never silently suppressed."""

    def test_agent_handles_tool_errors_gracefully(self) -> None:
        """When a tool call fails, execute_tool must:
        1. Return a structured error (not empty/None) — AP7
        2. Include isError field — AP6

        Anti-pattern #7: Never silently suppress errors.
        Anti-pattern #6: Never return generic error messages.
        """
        from modules.support_agent_01.starter.agent import execute_tool

        # Act: call with a nonexistent customer
        try:
            result = execute_tool("get_customer", {"customer_id": "NONEXISTENT"})
        except NotImplementedError:
            pytest.skip("execute_tool not yet implemented")

        # Assert: must return JSON with structured error fields
        assert result is not None, "execute_tool must never return None (AP7)"
        assert result != "", "execute_tool must never return empty string (AP7)"
        assert result != "{}", "execute_tool must never return empty object (AP7)"

        parsed = json.loads(result)
        assert "isError" in parsed or "error" in parsed, (
            "Error responses must include 'isError' or 'error' field. "
            "Anti-pattern #6: Generic errors without isError/errorCategory/isRetryable."
        )


class TestBusinessRules:
    """Verify customer before refund — encoded in tool descriptions."""

    def test_verification_before_refund(self) -> None:
        """get_customer MUST be called before process_refund.

        This is enforced via:
        1. Tool descriptions (prompt-level guidance)
        2. Hooks (programmatic enforcement — intermediate tier)

        The tool descriptions should make the dependency clear.
        """
        from modules.support_agent_01.starter.agent import TOOLS

        # Arrange
        get_customer = next(t for t in TOOLS if t["name"] == "get_customer")
        process_refund = next(t for t in TOOLS if t["name"] == "process_refund")

        # Assert: descriptions encode the business rule
        assert "before" in get_customer["description"].lower() or \
               "must" in get_customer["description"].lower(), (
            "get_customer description should encode the business rule that it "
            "MUST be called before order lookups or refunds."
        )

        assert "customer" in process_refund["description"].lower() or \
               "verification" in process_refund["description"].lower() or \
               "requires" in process_refund["description"].lower(), (
            "process_refund description should reference the customer verification requirement."
        )


class TestEscalation:
    """Escalation must use valid triggers only."""

    def test_escalation_on_explicit_request(self) -> None:
        """The escalate_to_human tool must restrict reason to the 3 valid triggers:
        customer_request, policy_gap, capability_limit.

        Anti-pattern #4: Self-reported confidence is NOT a valid trigger.
        Anti-pattern #5: Sentiment analysis is NOT a valid trigger.
        """
        from modules.support_agent_01.starter.agent import TOOLS

        # Arrange
        escalate = next(t for t in TOOLS if t["name"] == "escalate_to_human")
        reason_schema = escalate["input_schema"]["properties"]["reason"]

        # Assert: must have enum constraint
        assert "enum" in reason_schema, (
            "Escalation reason must be constrained to an enum of valid triggers. "
            "Without enum, the model could use invalid triggers like sentiment or confidence."
        )

        valid_reasons = set(reason_schema["enum"])
        expected = {"customer_request", "policy_gap", "capability_limit"}
        assert valid_reasons == expected, (
            f"Escalation reasons must be exactly {expected}, got {valid_reasons}. "
            "Only these 3 triggers are valid on the CCA-F exam."
        )

        # Must NOT include invalid triggers
        for invalid in ["sentiment", "confidence", "angry", "frustrated"]:
            assert invalid not in str(reason_schema).lower(), (
                f"Found invalid escalation trigger '{invalid}' in schema. "
                "Anti-patterns #4/#5: Sentiment and confidence are NEVER valid triggers."
            )
