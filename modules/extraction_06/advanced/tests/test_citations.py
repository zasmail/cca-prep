"""Tests for Module 06 Advanced — Two-Pass Citations Extraction.

These tests validate the two-pass separation pattern:
Pass 1 (tool_use for structure) and Pass 2 (citations for attribution).
"""

import inspect

import pytest


class TestTwoPassSeparation:
    """Citations and tool_use MUST be in separate passes."""

    def test_pass_1_exists_for_extraction(self) -> None:
        """Pass 1 function must exist for tool_use extraction."""
        from modules.extraction_06.advanced.citations_extraction import pass_1_extract

        sig = inspect.signature(pass_1_extract)
        assert "document_text" in sig.parameters

    def test_pass_2_exists_for_verification(self) -> None:
        """Pass 2 function must exist for citations verification."""
        from modules.extraction_06.advanced.citations_extraction import (
            pass_2_verify_with_citations,
        )

        sig = inspect.signature(pass_2_verify_with_citations)
        assert "document_text" in sig.parameters
        assert "extraction" in sig.parameters

    def test_pass_2_does_not_use_tool_choice(self) -> None:
        """Pass 2 MUST NOT use tool_choice — citations are incompatible with tool_use.

        This is a DIRECT exam question. Citations and tool_use cannot be in
        the same API call.
        """
        from modules.extraction_06.advanced.citations_extraction import (
            pass_2_verify_with_citations,
        )

        source = inspect.getsource(pass_2_verify_with_citations)

        # Pass 2 should mention citations but NOT tool_choice
        assert "citation" in source.lower(), (
            "Pass 2 must reference the citations API"
        )
        # The function should document that tool_choice is NOT used
        assert "NOT" in source or "CANNOT" in source or "INCOMPATIBLE" in source, (
            "Pass 2 must document that tool_use is incompatible with citations"
        )

    def test_pass_2_source_mentions_citations_enabled(self) -> None:
        """Pass 2 must enable citations on the document source."""
        from modules.extraction_06.advanced.citations_extraction import (
            pass_2_verify_with_citations,
        )

        source = inspect.getsource(pass_2_verify_with_citations)

        assert "citations" in source and "enabled" in source, (
            "Pass 2 must include citations={'enabled': True} on document sources"
        )


class TestTwoPassPipeline:
    """two_pass_extract_and_verify must orchestrate both passes."""

    def test_pipeline_function_exists(self) -> None:
        """The pipeline function must exist and accept document_text."""
        from modules.extraction_06.advanced.citations_extraction import (
            two_pass_extract_and_verify,
        )

        sig = inspect.signature(two_pass_extract_and_verify)
        assert "document_text" in sig.parameters

    def test_pipeline_calls_both_passes(self) -> None:
        """Pipeline must reference both pass_1 and pass_2 functions."""
        from modules.extraction_06.advanced.citations_extraction import (
            two_pass_extract_and_verify,
        )

        source = inspect.getsource(two_pass_extract_and_verify)

        assert "pass_1" in source or "Pass 1" in source, (
            "Pipeline must call or reference Pass 1 (extraction)"
        )
        assert "pass_2" in source or "Pass 2" in source, (
            "Pipeline must call or reference Pass 2 (verification)"
        )

    def test_pipeline_documents_return_structure(self) -> None:
        """Pipeline return type must include extraction, verification, and confidence."""
        from modules.extraction_06.advanced.citations_extraction import (
            two_pass_extract_and_verify,
        )

        source = inspect.getsource(two_pass_extract_and_verify)

        assert "extraction" in source, "Return must include 'extraction' field"
        assert "verification" in source, "Return must include 'verification' field"
        assert "unverified" in source.lower(), "Return must track unverified fields"


class TestIncompatibilityDocumentation:
    """Code must clearly document the citations + tool_use incompatibility."""

    def test_module_documents_incompatibility(self) -> None:
        """Module docstring must explain why citations and tool_use are incompatible."""
        from modules.extraction_06.advanced import citations_extraction

        source = inspect.getsource(citations_extraction)

        assert "INCOMPATIBLE" in source or "incompatible" in source, (
            "Module must document that citations and tool_use are incompatible"
        )

    def test_demonstrate_incompatibility_function(self) -> None:
        """demonstrate_incompatibility must explain the restriction clearly."""
        from modules.extraction_06.advanced.citations_extraction import (
            demonstrate_incompatibility,
        )

        explanation = demonstrate_incompatibility()

        assert "incompatible" in explanation.lower(), (
            "Must state that citations and tool_use are incompatible"
        )
        assert "two" in explanation.lower() or "separate" in explanation.lower(), (
            "Must explain the two-pass solution"
        )
        assert "cited_text" in explanation, (
            "Must mention that cited_text is not counted as output tokens"
        )
        assert "15%" in explanation, (
            "Must mention ~15% better recall with citations"
        )

    def test_also_incompatible_with_structured_outputs(self) -> None:
        """Must document that citations are also incompatible with Structured Outputs."""
        from modules.extraction_06.advanced.citations_extraction import (
            demonstrate_incompatibility,
        )

        explanation = demonstrate_incompatibility()

        assert "Structured Outputs" in explanation or "JSON mode" in explanation, (
            "Must document that citations are also incompatible with Structured Outputs"
        )

    def test_citations_scope_rule(self) -> None:
        """Must document that citations must be enabled on ALL or NONE documents."""
        from modules.extraction_06.advanced.citations_extraction import (
            demonstrate_incompatibility,
        )

        explanation = demonstrate_incompatibility()

        assert "ALL" in explanation and "NONE" in explanation, (
            "Must document that citations must be enabled on ALL or NONE documents"
        )
