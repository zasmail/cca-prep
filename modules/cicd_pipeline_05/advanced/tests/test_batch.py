"""Tests for Module 05 Advanced — Batch Review.

These tests validate the Batch API request structure,
constraints awareness, and correct tool_choice usage.
"""

import pytest


class TestBatchRequestStructure:
    """Batch requests must follow the Anthropic Batch API format."""

    def test_review_tool_has_correct_schema(self) -> None:
        """The review tool must define a valid input_schema for structured output."""
        from modules.cicd_pipeline_05.advanced.batch_review import REVIEW_TOOL

        assert REVIEW_TOOL["name"] == "submit_review"
        assert "input_schema" in REVIEW_TOOL

        schema = REVIEW_TOOL["input_schema"]
        required_fields = {"file_path", "summary", "issues", "approved"}
        actual_fields = set(schema.get("properties", {}).keys())
        assert required_fields.issubset(actual_fields), (
            f"Review tool schema missing fields: {required_fields - actual_fields}"
        )

    def test_review_tool_issues_have_severity_enum(self) -> None:
        """Issue severity must be constrained to critical/warning/info."""
        from modules.cicd_pipeline_05.advanced.batch_review import REVIEW_TOOL

        issues_schema = REVIEW_TOOL["input_schema"]["properties"]["issues"]
        severity = issues_schema["items"]["properties"]["severity"]
        assert "enum" in severity, "severity must have enum constraint"
        assert set(severity["enum"]) == {"critical", "warning", "info"}

    def test_build_batch_requests_returns_list(self) -> None:
        """build_batch_requests must return a list of request dicts."""
        from modules.cicd_pipeline_05.advanced.batch_review import build_batch_requests

        try:
            # Test with empty list (edge case)
            result = build_batch_requests([])
            assert isinstance(result, list)
            assert len(result) == 0
        except NotImplementedError:
            pytest.skip("build_batch_requests not yet implemented")

    def test_each_request_has_custom_id(self) -> None:
        """Each batch request MUST have a unique custom_id.

        custom_id maps results back to inputs — without it,
        you cannot correlate batch results to original files.
        """
        from modules.cicd_pipeline_05.advanced.batch_review import build_batch_requests

        try:
            # Create a temp file to test with
            import tempfile
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write("def hello(): pass\n")
                temp_path = f.name

            requests = build_batch_requests([temp_path])

            for req in requests:
                assert "custom_id" in req, (
                    "Each batch request must have 'custom_id' for result correlation"
                )
        except NotImplementedError:
            pytest.skip("build_batch_requests not yet implemented")

    def test_each_request_uses_tool_choice(self) -> None:
        """Each request must use tool_choice to force structured output.

        tool_choice={"type": "tool", "name": "submit_review"} ensures
        the model always returns structured review data.
        """
        from modules.cicd_pipeline_05.advanced.batch_review import build_batch_requests

        try:
            import tempfile
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write("def hello(): pass\n")
                temp_path = f.name

            requests = build_batch_requests([temp_path])

            for req in requests:
                params = req.get("params", {})
                tool_choice = params.get("tool_choice", {})
                assert tool_choice.get("type") == "tool", (
                    "tool_choice must be type='tool' for forced extraction"
                )
                assert tool_choice.get("name") == "submit_review", (
                    "tool_choice must name 'submit_review' for structured output"
                )
        except NotImplementedError:
            pytest.skip("build_batch_requests not yet implemented")


class TestBatchConstraintsAwareness:
    """Code must demonstrate awareness of Batch API constraints."""

    def test_code_documents_50_percent_discount(self) -> None:
        """Code must document the 50% cost reduction."""
        import inspect
        from modules.cicd_pipeline_05.advanced import batch_review

        source = inspect.getsource(batch_review)

        assert "50%" in source, (
            "Code must document that Batch API is 50% cheaper than real-time"
        )

    def test_code_documents_24_hour_window(self) -> None:
        """Code must document the 24-hour processing window."""
        import inspect
        from modules.cicd_pipeline_05.advanced import batch_review

        source = inspect.getsource(batch_review)

        assert "24" in source and "hour" in source.lower(), (
            "Code must document the 24-hour processing window"
        )

    def test_code_documents_no_sla(self) -> None:
        """Code must document that there is no SLA on batch completion."""
        import inspect
        from modules.cicd_pipeline_05.advanced import batch_review

        source = inspect.getsource(batch_review)

        assert "no sla" in source.lower() or "NO SLA" in source, (
            "Code must document that Batch API has no SLA"
        )

    def test_code_documents_no_streaming(self) -> None:
        """Code must document that batch does not support streaming."""
        import inspect
        from modules.cicd_pipeline_05.advanced import batch_review

        source = inspect.getsource(batch_review)

        assert "no streaming" in source.lower() or "No streaming" in source, (
            "Code must document that Batch API does not support streaming"
        )

    def test_code_documents_multi_turn_is_supported(self) -> None:
        """Code must correctly document that Batch DOES support multi-turn
        conversations and tool use — the real restriction is narrower
        (no streaming, no thread/store continuation, no cache hints,
        no max_tokens:0, no Fast mode).
        """
        import inspect
        from modules.cicd_pipeline_05.advanced import batch_review

        source = inspect.getsource(batch_review)

        assert "multi-turn" in source.lower(), (
            "Code must mention multi-turn support/behavior in Batch"
        )
        assert "are supported" in source.lower() or "ARE supported" in source, (
            "Code must document that multi-turn conversations and tool use "
            "ARE supported in Batch (not a blanket 'no multi-turn' claim)"
        )

    def test_code_documents_max_requests_per_batch(self) -> None:
        """Code must document the correct Batch API request/size ceiling:
        100,000 requests OR 256 MB, whichever is reached first.
        """
        import inspect
        from modules.cicd_pipeline_05.advanced import batch_review

        source = inspect.getsource(batch_review)

        assert "100,000" in source or "100000" in source, (
            "Code must document the 100,000 requests per batch limit"
        )
        assert "256 MB" in source or "256MB" in source, (
            "Code must document the 256 MB batch size limit"
        )
        assert "10,000" not in source and "10000" not in source, (
            "Code must not still reference the stale 10,000-request limit"
        )

    def test_code_documents_jsonl_29_days(self) -> None:
        """Code must document .jsonl format and 29-day availability."""
        import inspect
        from modules.cicd_pipeline_05.advanced import batch_review

        source = inspect.getsource(batch_review)

        assert ".jsonl" in source, "Code must document .jsonl result format"
        assert "29" in source, "Code must document 29-day result availability"
