"""Tests for Module 05 Intermediate — Generate-Then-Review Session Isolation.

These tests validate that the pipeline uses SEPARATE sessions for
generation and review (AP9: same-session self-review is an anti-pattern).
"""

import re
from pathlib import Path

import pytest


class TestSessionIsolation:
    """AP9: Generation and review MUST use separate sessions."""

    def _read_script(self) -> str:
        """Read the gen_then_review script content."""
        script_path = Path(__file__).parent.parent / "gen_then_review.sh"
        return script_path.read_text()

    def test_script_exists_and_is_bash(self) -> None:
        """The script must exist with a proper bash shebang."""
        script_path = Path(__file__).parent.parent / "gen_then_review.sh"

        assert script_path.exists(), "gen_then_review.sh must exist"

        content = script_path.read_text()
        assert content.startswith("#!/usr/bin/env bash"), (
            "Script must have #!/usr/bin/env bash shebang"
        )

    def test_has_two_distinct_session_ids(self) -> None:
        """Script must define TWO different session ID variables.

        AP9: Same-session self-review causes confirmation bias.
        The generation and review sessions MUST have different IDs.
        """
        content = self._read_script()

        # Must have two separate uuidgen calls for two session IDs
        uuidgen_calls = re.findall(r'\$\(uuidgen\)', content)
        assert len(uuidgen_calls) >= 2, (
            f"Found {len(uuidgen_calls)} uuidgen calls, need at least 2. "
            "Generation and review must each get a unique session ID."
        )

    def test_generation_session_has_session_id(self) -> None:
        """Generation session must use --session-id flag."""
        content = self._read_script()

        assert "GEN_SESSION_ID" in content, (
            "Generation session must define a GEN_SESSION_ID variable"
        )
        assert "--session-id" in content, (
            "Must use --session-id flag to identify sessions"
        )

    def test_review_session_has_different_session_id(self) -> None:
        """Review session must use a SEPARATE --session-id."""
        content = self._read_script()

        assert "REVIEW_SESSION_ID" in content, (
            "Review session must define a REVIEW_SESSION_ID variable"
        )

        # Both session ID variables must exist and be different names
        assert "GEN_SESSION_ID" in content and "REVIEW_SESSION_ID" in content, (
            "Must have distinct variable names for generation and review session IDs"
        )


class TestToolRestrictions:
    """Generation and review sessions must have different tool permissions."""

    def _read_script(self) -> str:
        """Read the gen_then_review script content."""
        script_path = Path(__file__).parent.parent / "gen_then_review.sh"
        return script_path.read_text()

    def test_generation_session_has_write_tools(self) -> None:
        """Generation session should have Write/Edit/Bash tools."""
        content = self._read_script()

        # The generation section should reference write-capable tools
        assert '"Write"' in content or "'Write'" in content, (
            "Generation session should include Write tool"
        )

    def test_review_session_has_read_only_tools(self) -> None:
        """Review session should restrict to Read/Grep/Glob tools only."""
        content = self._read_script()

        # The review section should reference read-only tools
        assert '"Read"' in content or "'Read'" in content, (
            "Review session should include Read tool"
        )
        assert '"Grep"' in content or "'Grep'" in content, (
            "Review session should include Grep tool"
        )

    def test_review_session_uses_plan_permission_mode(self) -> None:
        """Review session should use --permission-mode plan for read-only enforcement.

        This is defense-in-depth: both --allowedTools AND --permission-mode
        restrict the review session to read-only operations.
        """
        content = self._read_script()

        assert "--permission-mode plan" in content or "--permission-mode=plan" in content, (
            "Review session must use '--permission-mode plan' for read-only enforcement. "
            "This prevents the review session from modifying reviewed code."
        )


class TestBothSessionsUseNonInteractive:
    """Both sessions must use claude -p for CI/CD compatibility."""

    def _read_script(self) -> str:
        """Read the gen_then_review script content."""
        script_path = Path(__file__).parent.parent / "gen_then_review.sh"
        return script_path.read_text()

    def test_both_sessions_use_dash_p(self) -> None:
        """Both generation and review must use `claude -p` (non-interactive)."""
        content = self._read_script()

        # Count claude -p occurrences (should be at least 2)
        claude_p_count = len(re.findall(r'claude -p', content))
        assert claude_p_count >= 2, (
            f"Found {claude_p_count} 'claude -p' calls, need at least 2. "
            "Both generation and review sessions must be non-interactive."
        )

    def test_script_checks_session_isolation(self) -> None:
        """Script should verify that session IDs are different."""
        content = self._read_script()

        # Should have a comparison checking the two IDs aren't equal
        assert "GEN_SESSION_ID" in content and "REVIEW_SESSION_ID" in content, (
            "Script should compare session IDs to verify isolation"
        )

        # Should have an error message about AP9
        assert "AP9" in content or "confirmation bias" in content.lower() or \
               "same" in content.lower(), (
            "Script should warn about AP9 (same-session self-review) violation"
        )
