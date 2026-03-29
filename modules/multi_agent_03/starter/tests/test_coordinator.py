"""Tests for Module 03 Starter — Multi-Agent Research Coordinator.

CCA-F Exam Domains: D1 (~27%), D2 (~18%), D5 (~15%)

These tests validate the orchestrator-worker pattern — specifically that
the coordinator scopes context correctly and manages all communication.
"""

import inspect
import json
from typing import Any

import pytest

from modules.multi_agent_03.starter.coordinator import (
    COORDINATOR_TOOLS,
    ResearchFinding,
    ResearchTask,
    SynthesizedReport,
    delegate_to_researcher,
    synthesize_findings,
)


class TestContextScoping:
    """Subagents must receive SCOPED context, not full conversation history."""

    def test_delegate_tool_requires_scoped_context(self) -> None:
        """The delegate_to_researcher tool schema must require a 'context' field
        that is explicitly described as scoped/focused, not full history.

        Key exam concept: Workers get ONLY task-relevant context.
        Passing full conversation history wastes tokens and can confuse the worker.
        """
        delegate_tool = next(
            t for t in COORDINATOR_TOOLS if t["name"] == "delegate_to_researcher"
        )
        context_prop = delegate_tool["input_schema"]["properties"]["context"]

        # Context description should emphasize scoping
        description = context_prop["description"].lower()
        assert any(
            phrase in description
            for phrase in ["scoped", "not include full", "only", "not full conversation"]
        ), (
            "The context field description must emphasize that context is SCOPED "
            "to the subtopic — not full conversation history. "
            "Workers should never receive the entire conversation."
        )

    def test_research_task_does_not_include_full_history(self) -> None:
        """ResearchTask dataclass must NOT have a field for full conversation history.

        The task should contain: subtopic, context (scoped), output_format.
        It should NOT contain: messages, conversation_history, full_context, etc.
        """
        task_fields = {f.name for f in ResearchTask.__dataclass_fields__.values()}

        history_fields = {
            "messages",
            "conversation_history",
            "full_context",
            "chat_history",
            "all_messages",
            "parent_context",
        }

        overlap = task_fields & history_fields
        assert len(overlap) == 0, (
            f"ResearchTask contains history-like fields: {overlap}. "
            "Workers must receive SCOPED context only — not full conversation history."
        )

    def test_delegate_function_signature_has_scoped_params(self) -> None:
        """delegate_to_researcher must accept subtopic, context, and output_format.

        It must NOT accept a 'messages' or 'conversation' parameter.
        """
        sig = inspect.signature(delegate_to_researcher)
        param_names = set(sig.parameters.keys())

        # Must have scoped parameters
        assert "subtopic" in param_names, "Missing 'subtopic' parameter"
        assert "context" in param_names, "Missing 'context' parameter"
        assert "output_format" in param_names, "Missing 'output_format' parameter"

        # Must NOT have full-history parameters
        history_params = {"messages", "conversation", "history", "full_context"}
        overlap = param_names & history_params
        assert len(overlap) == 0, (
            f"delegate_to_researcher accepts history-like params: {overlap}. "
            "Workers must receive scoped context, not full conversation history."
        )


class TestCoordinatorManagesAllCommunication:
    """The coordinator must be the single point of communication between agents."""

    def test_synthesize_requires_worker_attribution(self) -> None:
        """synthesize_findings input must include worker_id for attribution.

        Key exam concept: When findings conflict, the coordinator annotates
        both sides with source attribution. This requires knowing which
        worker produced each finding.
        """
        synthesize_tool = next(
            t for t in COORDINATOR_TOOLS if t["name"] == "synthesize_findings"
        )
        findings_schema = synthesize_tool["input_schema"]["properties"]["findings"]
        item_props = findings_schema["items"]["properties"]

        assert "worker_id" in item_props, (
            "synthesize_findings schema must include 'worker_id' in each finding. "
            "This enables source attribution when findings conflict."
        )

    def test_synthesized_report_has_conflicts_field(self) -> None:
        """SynthesizedReport must have a conflicts field for disagreements.

        Key exam concept: Conflicting findings must be annotated with both
        perspectives and source attribution — never silently resolved.
        """
        report_fields = {f.name for f in SynthesizedReport.__dataclass_fields__.values()}

        assert "conflicts" in report_fields, (
            "SynthesizedReport must have a 'conflicts' field. "
            "When workers disagree, both perspectives must be preserved with attribution."
        )

    def test_coordinator_tools_are_under_limit(self) -> None:
        """Coordinator should have a focused set of tools (AP8 check).

        Key exam concept (AP8): 18+ tools degrades selection reliability.
        Even the coordinator should have a focused tool set.
        """
        assert len(COORDINATOR_TOOLS) <= 5, (
            f"Coordinator has {len(COORDINATOR_TOOLS)} tools. "
            "AP8: Keep tools under 5 per agent for reliable selection. "
            "The coordinator needs: delegate, synthesize, and maybe 1-2 utility tools."
        )


class TestToolDefinitionQuality:
    """Tool definitions must encode business rules in descriptions."""

    def test_delegate_description_warns_about_context_scope(self) -> None:
        """The delegate tool description should warn against passing full history.

        Key exam concept (D2): Tool descriptions encode business rules and
        constraints. The description should make it clear that context must be scoped.
        """
        delegate_tool = next(
            t for t in COORDINATOR_TOOLS if t["name"] == "delegate_to_researcher"
        )
        description = delegate_tool["description"].lower()

        assert any(
            phrase in description
            for phrase in ["not the full", "only", "scoped", "not full conversation"]
        ), (
            "delegate_to_researcher description must warn against passing full "
            "conversation history. Tool descriptions should encode constraints."
        )

    def test_synthesize_description_mentions_conflicts(self) -> None:
        """The synthesize tool description must mention conflict handling.

        Silently picking one finding over another is the wrong approach.
        """
        synthesize_tool = next(
            t for t in COORDINATOR_TOOLS if t["name"] == "synthesize_findings"
        )
        description = synthesize_tool["description"].lower()

        assert "conflict" in description, (
            "synthesize_findings description must mention conflict handling. "
            "Conflicting findings must be annotated, not silently resolved."
        )
