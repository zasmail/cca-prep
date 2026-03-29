"""Tests for Module 02 Starter — CLAUDE.md and Rule File Configuration.

CCA-F Exam Domain: D3 Claude Code Configuration (~20%)

These tests validate that configuration files follow exam-correct patterns.
Each test checks a specific structural requirement for CLAUDE.md and rule files.
"""

import re
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

MODULE_DIR = Path(__file__).resolve().parent.parent
STARTER_DIR = MODULE_DIR / "starter"
RULES_DIR = STARTER_DIR / "rules"
CLAUDE_MD = STARTER_DIR / "fintech_dashboard_claude.md"


class TestClaudeMdSections:
    """CLAUDE.md must have all required sections for effective project context."""

    REQUIRED_SECTIONS = [
        "Project Context",
        "Build Commands",
        "Architecture",
        "Coding Conventions",
        "API Patterns",
        "Security Rules",
    ]

    def test_claude_md_exists(self) -> None:
        """CLAUDE.md must exist — it's the primary project configuration file."""
        assert CLAUDE_MD.exists(), (
            f"CLAUDE.md not found at {CLAUDE_MD}. "
            "This is the most important configuration file in Claude Code."
        )

    def test_claude_md_has_required_sections(self) -> None:
        """CLAUDE.md must contain all standard sections for a complete project config.

        Key exam concept: CLAUDE.md should include project context, build commands,
        architecture, conventions, and security rules at minimum.
        """
        content = CLAUDE_MD.read_text()

        for section in self.REQUIRED_SECTIONS:
            assert f"## {section}" in content, (
                f"Missing required section '## {section}' in CLAUDE.md. "
                "A complete CLAUDE.md needs: project context, build commands, "
                "architecture, coding conventions, and security rules."
            )

    def test_claude_md_has_no_unfilled_todos(self) -> None:
        """All TODO sections should be filled in by the student.

        This test will FAIL until the exercise is completed — that's intentional.
        """
        content = CLAUDE_MD.read_text()

        todo_count = content.count("<!-- TODO:")

        assert todo_count == 0, (
            f"Found {todo_count} unfilled TODO section(s) in CLAUDE.md. "
            "Complete all TODO sections to finish this exercise."
        )

    def test_claude_md_has_import_references(self) -> None:
        """CLAUDE.md should use @import to pull in rule files and schemas.

        Key exam concept: @import resolves relative paths and brings external
        files into the CLAUDE.md context. This is how you compose configuration.
        """
        content = CLAUDE_MD.read_text()

        assert "@" in content and ("rules/" in content or "schemas/" in content), (
            "CLAUDE.md should contain @import references to rule files or schemas. "
            "Example: @.claude/rules/api-routes.md"
        )


class TestRuleFiles:
    """Rule files must have paths: frontmatter to scope enforcement."""

    def test_rule_files_exist(self) -> None:
        """At least one rule file must exist in the rules/ directory."""
        rule_files = list(RULES_DIR.glob("*.md"))

        assert len(rule_files) > 0, (
            "No rule files found in rules/ directory. "
            "Rule files provide path-scoped configuration for Claude Code."
        )

    def test_rule_files_have_paths_frontmatter(self) -> None:
        """Every rule file MUST have a paths: directive in YAML frontmatter.

        Key exam concept: The paths: directive scopes when the rule is loaded.
        Without it, the rule would apply to ALL files (wasteful context usage).

        Format:
        ---
        paths: src/app/api/**/*.ts
        ---
        """
        rule_files = list(RULES_DIR.glob("*.md"))

        for rule_file in rule_files:
            content = rule_file.read_text()

            # Check for YAML frontmatter
            assert content.startswith("---"), (
                f"Rule file {rule_file.name} must start with YAML frontmatter (---). "
                "Frontmatter is required for the paths: directive."
            )

            # Extract frontmatter
            parts = content.split("---", 2)
            assert len(parts) >= 3, (
                f"Rule file {rule_file.name} has malformed frontmatter. "
                "Must be: ---\\npaths: <glob>\\n---"
            )

            frontmatter = parts[1]
            assert "paths:" in frontmatter, (
                f"Rule file {rule_file.name} is missing 'paths:' in frontmatter. "
                "Every rule file must specify which file paths it applies to."
            )

    def test_paths_values_are_valid_globs(self) -> None:
        """paths: values must be valid glob patterns.

        Valid examples: src/**/*.ts, tests/**/*.py, *.md
        Invalid examples: plain filenames without glob syntax (unless intentional)
        """
        rule_files = list(RULES_DIR.glob("*.md"))

        for rule_file in rule_files:
            content = rule_file.read_text()
            parts = content.split("---", 2)

            if len(parts) < 3:
                continue

            frontmatter = parts[1]
            paths_match = re.search(r"paths:\s*(.+)", frontmatter)

            if paths_match:
                paths_value = paths_match.group(1).strip()

                # Should contain at least one glob character or file extension
                has_glob = any(c in paths_value for c in ["*", "?", "["])
                has_extension = "." in paths_value

                assert has_glob or has_extension, (
                    f"Rule file {rule_file.name} has paths: '{paths_value}' which "
                    "doesn't look like a valid glob pattern. "
                    "Expected patterns like: src/**/*.ts, tests/**/*.py"
                )
