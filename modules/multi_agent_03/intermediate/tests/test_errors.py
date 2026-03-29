"""Tests for Module 03 Intermediate — Structured Error Propagation.

CCA-F Exam Domains: D1 (~27%), D2 (~18%)

These tests validate that subagent errors are ALWAYS structured and NEVER silent.
The core anti-patterns being tested: AP6 (generic errors) and AP7 (silent suppression).
"""

from typing import Any

import pytest

from modules.multi_agent_03.intermediate.error_propagation import (
    ErrorCategory,
    SubagentResult,
)


class TestSubagentResultSuccess:
    """Successful results must contain structured data."""

    def test_ok_result_has_success_true(self) -> None:
        """SubagentResult.ok() must set success=True."""
        try:
            result = SubagentResult.ok({"claims": ["test claim"], "sources": ["test.com"]})
        except NotImplementedError:
            pytest.skip("SubagentResult.ok() not yet implemented")

        assert result.success is True, "ok() result must have success=True"

    def test_ok_result_has_data(self) -> None:
        """SubagentResult.ok() must include the data dict."""
        try:
            data = {"claims": ["test claim"], "sources": ["test.com"]}
            result = SubagentResult.ok(data)
        except NotImplementedError:
            pytest.skip("SubagentResult.ok() not yet implemented")

        assert result.data == data, "ok() result must contain the provided data"

    def test_ok_result_has_no_error(self) -> None:
        """Successful results must NOT have error information."""
        try:
            result = SubagentResult.ok({"claims": []})
        except NotImplementedError:
            pytest.skip("SubagentResult.ok() not yet implemented")

        assert result.error is None, "Successful results must not have error field set"


class TestSubagentResultFailure:
    """Failures must return STRUCTURED errors, never empty dicts."""

    def test_failure_returns_structured_error_not_empty_dict(self) -> None:
        """AP7: Failures must NEVER return {} or [].

        This is the single most important error handling test.
        An empty dict on failure is indistinguishable from a success with no data.
        """
        try:
            result = SubagentResult.failure(
                category=ErrorCategory.TRANSIENT,
                message="API timeout after 30s",
                attempted="Fetch pricing data from Bloomberg API",
                alternatives=["Try Reuters API"],
            )
        except NotImplementedError:
            pytest.skip("SubagentResult.failure() not yet implemented")

        assert result.success is False, "failure() must have success=False"
        assert result.error is not None, (
            "AP7: failure() must include error dict — never return None/empty on failure"
        )
        assert result.error != {}, (
            "AP7: failure() error must not be empty dict — include category, message, etc."
        )

    def test_failure_error_has_required_fields(self) -> None:
        """AP6: Error dict must include category, message, isRetryable, attempted.

        Generic errors like {"error": "something went wrong"} are anti-pattern AP6.
        Every error must have enough context for the coordinator to act on it.
        """
        try:
            result = SubagentResult.failure(
                category=ErrorCategory.NOT_FOUND,
                message="No data found for ticker XYZABC",
                attempted="Look up stock price for XYZABC",
                alternatives=["Check if ticker symbol is correct"],
            )
        except NotImplementedError:
            pytest.skip("SubagentResult.failure() not yet implemented")

        error = result.error
        required_fields = ["category", "message", "isRetryable", "attempted"]

        for field_name in required_fields:
            assert field_name in error, (
                f"AP6: Error missing required field '{field_name}'. "
                "Errors must include: category, message, isRetryable, attempted, alternatives."
            )

    def test_transient_errors_are_retryable(self) -> None:
        """TRANSIENT errors should be auto-detected as retryable."""
        try:
            result = SubagentResult.failure(
                category=ErrorCategory.TRANSIENT,
                message="Rate limited — 429 response",
                attempted="Fetch market data",
            )
        except NotImplementedError:
            pytest.skip("SubagentResult.failure() not yet implemented")

        assert result.error["isRetryable"] is True, (
            "TRANSIENT errors must be retryable — the coordinator should retry after delay."
        )

    def test_validation_errors_are_not_retryable(self) -> None:
        """VALIDATION errors should NOT be retryable with same input."""
        try:
            result = SubagentResult.failure(
                category=ErrorCategory.VALIDATION,
                message="Invalid date format: '2024-13-45'",
                attempted="Parse date range for query",
            )
        except NotImplementedError:
            pytest.skip("SubagentResult.failure() not yet implemented")

        assert result.error["isRetryable"] is False, (
            "VALIDATION errors must NOT be retryable — the input needs to change first."
        )

    def test_permission_errors_are_not_retryable(self) -> None:
        """PERMISSION errors should NOT be retryable."""
        try:
            result = SubagentResult.failure(
                category=ErrorCategory.PERMISSION,
                message="API key does not have access to premium data",
                attempted="Fetch premium market analytics",
            )
        except NotImplementedError:
            pytest.skip("SubagentResult.failure() not yet implemented")

        assert result.error["isRetryable"] is False, (
            "PERMISSION errors must NOT be retryable — escalate to user."
        )

    def test_failure_can_include_partial_results(self) -> None:
        """Partial results must be preserved even on failure.

        Key concept: A worker that found 3/5 sources before timing out
        still has valuable data. Don't throw it away.
        """
        partial = [
            {"claim": "Revenue grew 15%", "source": "SEC filing"},
            {"claim": "Market cap is $50B", "source": "Yahoo Finance"},
        ]

        try:
            result = SubagentResult.failure(
                category=ErrorCategory.TRANSIENT,
                message="Timeout after finding 2 of 5 sources",
                attempted="Research company financials",
                partial_results=partial,
            )
        except NotImplementedError:
            pytest.skip("SubagentResult.failure() not yet implemented")

        assert len(result.partial_results) == 2, (
            "Partial results must be preserved on failure — don't discard useful data."
        )

    def test_failure_includes_alternatives(self) -> None:
        """Failure errors should suggest alternative approaches when possible."""
        try:
            result = SubagentResult.failure(
                category=ErrorCategory.NOT_FOUND,
                message="Company 'Acme Corp' not found in Bloomberg",
                attempted="Look up Acme Corp financials in Bloomberg",
                alternatives=["Try Reuters", "Search by ticker symbol instead of name"],
            )
        except NotImplementedError:
            pytest.skip("SubagentResult.failure() not yet implemented")

        assert "alternatives" in result.error, (
            "Error should include 'alternatives' — suggest fallback approaches."
        )
        assert len(result.error["alternatives"]) > 0, (
            "Alternatives list should not be empty when alternatives are provided."
        )


class TestErrorCategoryEnum:
    """ErrorCategory must cover the standard failure modes."""

    def test_all_categories_exist(self) -> None:
        """The four standard error categories must be defined."""
        expected = {"TRANSIENT", "VALIDATION", "NOT_FOUND", "PERMISSION"}

        actual = {member.name for member in ErrorCategory}

        assert expected.issubset(actual), (
            f"Missing error categories: {expected - actual}. "
            "Must have: TRANSIENT (retryable), VALIDATION, NOT_FOUND, PERMISSION."
        )
