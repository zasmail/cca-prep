"""Tests for Module 06 Intermediate — Validation-Retry Loop.

These tests validate that the retry pattern uses SPECIFIC error feedback
(not generic "try again") and follows the correct message structure.
"""

import inspect

import pytest


class TestValidationRules:
    """validate_extraction must catch semantic errors with specific messages."""

    def test_catches_line_item_amount_mismatch(self) -> None:
        """Should detect when line item amount != quantity * unit_price."""
        from modules.extraction_06.intermediate.validation_retry import validate_extraction

        try:
            extraction = {
                "vendor_name": "Test Corp",
                "invoice_number": "INV-001",
                "date": "2026-01-15",
                "line_items": [
                    {"description": "Widget", "quantity": 2, "unit_price": 50, "amount": 150},
                ],
                "subtotal": 150,
                "tax": None,
                "total": 150,
                "currency": "USD",
                "confidence_notes": None,
            }

            errors = validate_extraction(extraction)

            assert len(errors) > 0, "Should catch amount mismatch (2 * $50 != $150)"
            # Error must be SPECIFIC with actual values
            error_text = " ".join(errors).lower()
            assert "150" in error_text or "100" in error_text, (
                "Error must include actual values, not just 'amount mismatch'"
            )
        except NotImplementedError:
            pytest.skip("validate_extraction not yet implemented")

    def test_catches_subtotal_mismatch(self) -> None:
        """Should detect when subtotal != sum of line items."""
        from modules.extraction_06.intermediate.validation_retry import validate_extraction

        try:
            extraction = {
                "vendor_name": "Test Corp",
                "invoice_number": "INV-001",
                "date": "2026-01-15",
                "line_items": [
                    {"description": "Widget", "quantity": 1, "unit_price": 100, "amount": 100},
                    {"description": "Service", "quantity": 1, "unit_price": 30, "amount": 30},
                ],
                "subtotal": 150,  # Wrong: should be 130
                "tax": None,
                "total": 150,
                "currency": "USD",
                "confidence_notes": None,
            }

            errors = validate_extraction(extraction)

            assert len(errors) > 0, "Should catch subtotal mismatch ($150 != $130)"
        except NotImplementedError:
            pytest.skip("validate_extraction not yet implemented")

    def test_passes_valid_extraction(self) -> None:
        """Should return empty list for a valid extraction."""
        from modules.extraction_06.intermediate.validation_retry import validate_extraction

        try:
            extraction = {
                "vendor_name": "Test Corp",
                "invoice_number": "INV-001",
                "date": "2026-01-15",
                "line_items": [
                    {"description": "Widget", "quantity": 2, "unit_price": 50, "amount": 100},
                ],
                "subtotal": 100,
                "tax": None,
                "total": 100,
                "currency": "USD",
                "confidence_notes": None,
            }

            errors = validate_extraction(extraction)

            assert len(errors) == 0, f"Valid extraction should pass. Got errors: {errors}"
        except NotImplementedError:
            pytest.skip("validate_extraction not yet implemented")


class TestErrorFeedbackSpecificity:
    """AP6: Error feedback must be SPECIFIC, never generic."""

    def test_feedback_includes_actual_values(self) -> None:
        """Error feedback must include actual values for the model to correct."""
        from modules.extraction_06.intermediate.validation_retry import format_error_feedback

        try:
            errors = [
                "subtotal is $150 but line items sum to $130 (Widget: $100, Service: $30)",
                "date '01/15/2026' is not ISO 8601 format (expected YYYY-MM-DD)",
            ]

            feedback = format_error_feedback(errors)

            assert "$150" in feedback or "150" in feedback, (
                "Feedback must include actual values from the errors"
            )
            assert "ISO 8601" in feedback or "YYYY-MM-DD" in feedback, (
                "Feedback must include format expectations"
            )
        except NotImplementedError:
            pytest.skip("format_error_feedback not yet implemented")

    def test_feedback_is_not_generic(self) -> None:
        """Error feedback must NOT be generic 'try again' messages (AP6)."""
        from modules.extraction_06.intermediate.validation_retry import format_error_feedback

        try:
            errors = ["subtotal is $150 but line items sum to $130"]

            feedback = format_error_feedback(errors)

            # Check for generic patterns that violate AP6
            generic_patterns = [
                "try again",
                "please retry",
                "there are errors",
                "something went wrong",
            ]
            feedback_lower = feedback.lower()
            for pattern in generic_patterns:
                if pattern in feedback_lower:
                    # Only flag if the feedback ONLY contains generic text
                    # It's OK to say "please re-extract" IF specific errors are also included
                    assert "150" in feedback or "130" in feedback, (
                        f"Found generic pattern '{pattern}' without specific values. "
                        "AP6: Error messages must include actual values."
                    )
        except NotImplementedError:
            pytest.skip("format_error_feedback not yet implemented")


class TestRetryPattern:
    """extract_with_validation must use correct retry message structure."""

    def test_function_accepts_max_retries(self) -> None:
        """Must accept max_retries parameter for safety net."""
        from modules.extraction_06.intermediate.validation_retry import extract_with_validation

        sig = inspect.signature(extract_with_validation)

        assert "max_retries" in sig.parameters, (
            "extract_with_validation must accept max_retries parameter"
        )

    def test_source_uses_is_error_flag(self) -> None:
        """Retry must use is_error=True in tool_result to signal extraction errors.

        The is_error flag tells the model its previous extraction was wrong.
        Without it, the model treats the tool_result as normal feedback.
        """
        from modules.extraction_06.intermediate.validation_retry import extract_with_validation

        source = inspect.getsource(extract_with_validation)

        assert "is_error" in source, (
            "extract_with_validation must use 'is_error' in tool_result. "
            "This flag signals to the model that its extraction had errors."
        )

    def test_source_uses_tool_result(self) -> None:
        """Retry must append a tool_result message (not a new user message)."""
        from modules.extraction_06.intermediate.validation_retry import extract_with_validation

        source = inspect.getsource(extract_with_validation)

        assert "tool_result" in source, (
            "Retry must use 'tool_result' type in the user message. "
            "This is the correct way to send error feedback in a tool_use conversation."
        )

    def test_source_references_same_conversation(self) -> None:
        """Retry must happen in the SAME conversation, not a new one.

        Starting a new conversation loses the context of what went wrong.
        Appending to the existing messages list preserves context.
        """
        from modules.extraction_06.intermediate.validation_retry import extract_with_validation

        source = inspect.getsource(extract_with_validation)

        assert "append" in source or "messages" in source, (
            "Retry must append to existing messages (same conversation). "
            "Starting a new conversation loses error context."
        )


class TestPerFieldAccuracy:
    """AP10: Must track per-field accuracy, not just aggregate."""

    def test_function_returns_per_field_metrics(self) -> None:
        """Must return accuracy for individual fields, not just overall."""
        from modules.extraction_06.intermediate.validation_retry import track_per_field_accuracy

        try:
            extractions = [
                {"vendor_name": "A Corp", "total": 100},
                {"vendor_name": "B Corp", "total": 200},
            ]
            ground_truth = [
                {"vendor_name": "A Corp", "total": 100},
                {"vendor_name": "B Corp", "total": 250},
            ]

            metrics = track_per_field_accuracy(extractions, ground_truth)

            assert "vendor_name" in metrics, "Must include per-field accuracy for vendor_name"
            assert "total" in metrics, "Must include per-field accuracy for total"
            assert isinstance(metrics["vendor_name"], float), "Accuracy must be a float"
        except NotImplementedError:
            pytest.skip("track_per_field_accuracy not yet implemented")
