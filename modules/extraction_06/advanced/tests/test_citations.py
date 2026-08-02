"""Tests for Module 06 Advanced — Citations + Structured Extraction.

These tests validate the two-pass pattern (Pass 1: citations, free text;
Pass 2: forced tool_use, structure) AND the corrected compatibility facts:
citations + tool_use coexist fine; citations + Structured Outputs
(`output_config.format`) do not.
"""

import inspect
import re

import pytest


class TestTwoPassOrdering:
    """Citations (free text) must come before structuring (forced tool_use)."""

    def test_pass_1_exists_for_citation_extraction(self) -> None:
        """Pass 1 function must exist for citations-enabled extraction."""
        from modules.extraction_06.advanced.citations_extraction import (
            pass_1_extract_with_citations,
        )

        sig = inspect.signature(pass_1_extract_with_citations)
        assert "document_text" in sig.parameters

    def test_pass_1_does_not_force_tool_choice(self) -> None:
        """Pass 1 must NOT force tool_choice — citations need free text output.

        Forced tool_choice prefills the assistant turn with a tool_use-only
        block, leaving no text for citation markers to attach to. This is a
        mechanical constraint, not an API-enforced incompatibility.
        """
        from modules.extraction_06.advanced.citations_extraction import (
            pass_1_extract_with_citations,
        )

        source = inspect.getsource(pass_1_extract_with_citations)

        assert "citation" in source.lower(), "Pass 1 must reference the citations API"
        assert '"type": "tool"' not in source, (
            "Pass 1 must not force tool_choice to a specific tool — citations "
            "need a free-text turn to attach to"
        )

    def test_pass_1_enables_citations_on_document(self) -> None:
        """Pass 1 must enable citations on the document source."""
        from modules.extraction_06.advanced.citations_extraction import (
            pass_1_extract_with_citations,
        )

        source = inspect.getsource(pass_1_extract_with_citations)

        assert "citations" in source and "enabled" in source, (
            "Pass 1 must include citations={'enabled': True} on the document source"
        )

    def test_pass_2_exists_for_structuring(self) -> None:
        """Pass 2 function must exist and accept the cited extraction."""
        from modules.extraction_06.advanced.citations_extraction import pass_2_structure

        sig = inspect.signature(pass_2_structure)
        assert "cited_extraction" in sig.parameters

    def test_pass_2_uses_forced_tool_choice(self) -> None:
        """Pass 2 must force tool_choice to guarantee schema-valid structure."""
        from modules.extraction_06.advanced.citations_extraction import pass_2_structure

        source = inspect.getsource(pass_2_structure)

        assert "tool_choice" in source, "Pass 2 must force tool_choice for guaranteed structure"


class TestTwoPassPipeline:
    """two_pass_extract_and_structure must orchestrate both passes in order."""

    def test_pipeline_function_exists(self) -> None:
        """The pipeline function must exist and accept document_text."""
        from modules.extraction_06.advanced.citations_extraction import (
            two_pass_extract_and_structure,
        )

        sig = inspect.signature(two_pass_extract_and_structure)
        assert "document_text" in sig.parameters

    def test_pipeline_calls_both_passes(self) -> None:
        """Pipeline must reference both pass_1 and pass_2 functions."""
        from modules.extraction_06.advanced.citations_extraction import (
            two_pass_extract_and_structure,
        )

        source = inspect.getsource(two_pass_extract_and_structure)

        assert "pass_1" in source or "Pass 1" in source, (
            "Pipeline must call or reference Pass 1 (citation extraction)"
        )
        assert "pass_2" in source or "Pass 2" in source, (
            "Pipeline must call or reference Pass 2 (structuring)"
        )

    def test_pipeline_documents_return_structure(self) -> None:
        """Pipeline return type must include structured data and citations."""
        from modules.extraction_06.advanced.citations_extraction import (
            two_pass_extract_and_structure,
        )

        source = inspect.getsource(two_pass_extract_and_structure)

        assert "structured" in source, "Return must include 'structured' field"
        assert "citations" in source, "Return must include 'citations' field"
        assert "unverified" in source.lower(), "Return must track unverified fields"


class TestCompatibilityDocumentation:
    """Code must document the REAL compatibility rules, not the inverted claim."""

    def test_module_documents_tool_use_compatibility(self) -> None:
        """Module docstring must state that citations and tool_use are compatible."""
        from modules.extraction_06.advanced import citations_extraction

        source = inspect.getsource(citations_extraction)

        assert re.search(r"citations.{0,40}tool_use.{0,40}compatible", source, re.IGNORECASE) or (
            "COMPATIBLE" in source
        ), "Module must document that citations and tool_use are compatible"

    def test_module_documents_structured_outputs_incompatibility(self) -> None:
        """Module docstring must state citations + Structured Outputs is the real conflict."""
        from modules.extraction_06.advanced import citations_extraction

        source = inspect.getsource(citations_extraction)

        assert "Structured Outputs" in source, (
            "Module must document that citations are incompatible with Structured Outputs"
        )
        assert "output_config.format" in source, (
            "Module must name the actual incompatible parameter (output_config.format)"
        )

    def test_demonstrate_citations_compatibility_function(self) -> None:
        """demonstrate_citations_compatibility must explain the corrected rules."""
        from modules.extraction_06.advanced.citations_extraction import (
            demonstrate_citations_compatibility,
        )

        explanation = demonstrate_citations_compatibility()

        assert "compatible" in explanation.lower(), (
            "Must state that citations and tool_use are compatible"
        )
        assert "Structured Outputs" in explanation, (
            "Must state that Structured Outputs is the real incompatibility"
        )
        assert "cited_text" in explanation, (
            "Must mention that cited_text is not counted as output tokens"
        )

    def test_no_unsourced_recall_percentage(self) -> None:
        """Must NOT assert a specific recall percentage — no official figure exists.

        Anthropic's docs only say citations are "significantly more likely" to
        cite relevant quotes than prompt-only approaches. Any specific percentage
        (e.g. "~15%") is unsourced and should not be hardcoded as fact.
        """
        from modules.extraction_06.advanced.citations_extraction import (
            demonstrate_citations_compatibility,
        )

        explanation = demonstrate_citations_compatibility()

        assert not re.search(r"\d+%", explanation), (
            "Must not state a specific recall percentage — no official figure exists"
        )
        assert "significantly more likely" in explanation.lower(), (
            "Should use the official qualitative phrasing instead of a percentage"
        )

    def test_citations_scope_rule(self) -> None:
        """Must document that citations must be enabled on ALL or NONE documents."""
        from modules.extraction_06.advanced.citations_extraction import (
            demonstrate_citations_compatibility,
        )

        explanation = demonstrate_citations_compatibility()

        assert "ALL" in explanation and "NONE" in explanation, (
            "Must document that citations must be enabled on ALL or NONE documents"
        )
