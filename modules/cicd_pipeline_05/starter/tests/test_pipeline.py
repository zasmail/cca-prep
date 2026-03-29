"""Tests for Module 05 Starter — Code Review Pipeline.

These tests validate the pipeline script structure, JSON schema,
and correct flag usage for non-interactive Claude Code execution.
"""

import json
from pathlib import Path

import pytest


class TestPipelineScript:
    """The review pipeline script must use correct claude -p flags."""

    def _read_script(self) -> str:
        """Read the pipeline script content."""
        script_path = Path(__file__).parent.parent / "review_pipeline.sh"
        return script_path.read_text()

    def test_script_exists_and_is_bash(self) -> None:
        """The script must exist with a proper bash shebang."""
        script_path = Path(__file__).parent.parent / "review_pipeline.sh"

        assert script_path.exists(), "review_pipeline.sh must exist"

        content = script_path.read_text()
        assert content.startswith("#!/usr/bin/env bash"), (
            "Script must have #!/usr/bin/env bash shebang"
        )

    def test_uses_non_interactive_flag(self) -> None:
        """Pipeline MUST use `claude -p` for non-interactive execution.

        Without -p, claude runs interactively and blocks the CI/CD pipeline.
        This is the #1 tested concept for CI/CD integration.
        """
        content = self._read_script()

        assert "claude -p" in content or 'claude -p' in content, (
            "Pipeline must use 'claude -p' for non-interactive mode. "
            "Interactive mode blocks CI/CD pipelines."
        )

    def test_uses_json_output_format(self) -> None:
        """Pipeline must use --output-format json for machine-readable output."""
        content = self._read_script()

        assert "--output-format json" in content, (
            "Pipeline must use '--output-format json' for machine-readable output."
        )

    def test_uses_json_schema(self) -> None:
        """Pipeline must use --json-schema to enforce output structure."""
        content = self._read_script()

        assert "--json-schema" in content, (
            "Pipeline must use '--json-schema' to enforce structured output. "
            "Without it, output format is unpredictable."
        )

    def test_has_max_turns_limit(self) -> None:
        """Pipeline must set --max-turns to prevent runaway tool loops."""
        content = self._read_script()

        assert "--max-turns" in content, (
            "Pipeline must set '--max-turns' to limit tool call rounds. "
            "Without it, the pipeline could run indefinitely."
        )

    def test_has_budget_limit(self) -> None:
        """Pipeline must set --max-budget-usd to cap API spend."""
        content = self._read_script()

        assert "--max-budget-usd" in content, (
            "Pipeline must set '--max-budget-usd' to cap spend per invocation. "
            "Without it, a single run could consume unlimited API budget."
        )

    def test_restricts_tools_to_read_only(self) -> None:
        """Review pipeline must restrict tools to read-only operations.

        A code review should NEVER have Write, Edit, or Bash tools.
        --allowedTools enforces least-privilege access.
        """
        content = self._read_script()

        assert "--allowedTools" in content, (
            "Pipeline must use '--allowedTools' to restrict tool access. "
            "Review sessions should only have Read, Grep, Glob."
        )

        # Verify read-only tools are specified
        assert '"Read"' in content or "'Read'" in content, (
            "Read tool must be in --allowedTools"
        )
        assert '"Grep"' in content or "'Grep'" in content, (
            "Grep tool must be in --allowedTools"
        )
        assert '"Glob"' in content or "'Glob'" in content, (
            "Glob tool must be in --allowedTools"
        )


class TestReviewSchema:
    """The JSON schema must define the correct review output structure."""

    def _extract_schema(self) -> dict:
        """Extract the REVIEW_SCHEMA from the script."""
        script_path = Path(__file__).parent.parent / "review_pipeline.sh"
        content = script_path.read_text()

        # Find the JSON schema block between single quotes after REVIEW_SCHEMA=
        import re
        match = re.search(r"REVIEW_SCHEMA='(\{.*?\})'", content, re.DOTALL)
        if not match:
            pytest.skip("Could not extract REVIEW_SCHEMA from script")

        return json.loads(match.group(1))

    def test_schema_requires_summary(self) -> None:
        """Schema must require a summary field."""
        schema = self._extract_schema()

        assert "summary" in schema.get("properties", {}), "Schema must have 'summary' field"
        assert "summary" in schema.get("required", []), "summary must be required"

    def test_schema_requires_issues_array(self) -> None:
        """Schema must require an issues array with structured items."""
        schema = self._extract_schema()

        assert "issues" in schema.get("properties", {}), "Schema must have 'issues' field"

        issues_schema = schema["properties"]["issues"]
        assert issues_schema["type"] == "array", "issues must be an array"

        item_schema = issues_schema.get("items", {})
        required_fields = {"file", "line", "severity", "description", "suggestion"}
        actual_fields = set(item_schema.get("properties", {}).keys())
        assert required_fields.issubset(actual_fields), (
            f"Issue items missing fields: {required_fields - actual_fields}"
        )

    def test_schema_has_severity_enum(self) -> None:
        """Issue severity must be constrained to critical/warning/info."""
        schema = self._extract_schema()

        severity = (
            schema["properties"]["issues"]["items"]["properties"]["severity"]
        )
        assert "enum" in severity, "severity must have an enum constraint"
        assert set(severity["enum"]) == {"critical", "warning", "info"}, (
            "severity enum must be: critical, warning, info"
        )

    def test_schema_requires_approved_boolean(self) -> None:
        """Schema must require an approved boolean field."""
        schema = self._extract_schema()

        assert "approved" in schema.get("properties", {}), "Schema must have 'approved' field"
        assert schema["properties"]["approved"]["type"] == "boolean", (
            "approved must be a boolean"
        )
        assert "approved" in schema.get("required", []), "approved must be required"
