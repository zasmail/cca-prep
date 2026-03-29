"""Tests for Module 02 Intermediate — Slash Command Configuration.

CCA-F Exam Domain: D3 Claude Code Configuration (~20%)

These tests validate that slash commands have correct frontmatter syntax.
Slash commands MUST have proper frontmatter to function in Claude Code.
"""

from __future__ import annotations


import re
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

COMMANDS_DIR = Path(__file__).resolve().parent.parent / "commands"


class TestSlashCommandFrontmatter:
    """Slash commands must have valid YAML frontmatter with required fields."""

    def _get_command_files(self) -> list[Path]:
        """Get all .md files in the commands directory."""
        files = list(COMMANDS_DIR.glob("*.md"))
        assert len(files) > 0, "No command files found in commands/ directory"
        return files

    def _parse_frontmatter(self, filepath: Path) -> dict[str, str]:
        """Parse YAML frontmatter from a markdown file.

        Returns dict of key-value pairs from the frontmatter block.
        """
        content = filepath.read_text()

        assert content.startswith("---"), (
            f"Command file {filepath.name} must start with YAML frontmatter (---). "
            "Frontmatter is required for slash commands in Claude Code."
        )

        parts = content.split("---", 2)
        assert len(parts) >= 3, (
            f"Command file {filepath.name} has malformed frontmatter. "
            "Must be: ---\\nkey: value\\n---"
        )

        frontmatter = {}
        for line in parts[1].strip().split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                frontmatter[key.strip()] = value.strip()

        return frontmatter

    def test_commands_have_argument_hint(self) -> None:
        """Every slash command should have an argument-hint in frontmatter.

        Key exam concept: argument-hint provides the placeholder text shown
        to the user when they invoke the command. The value is accessible
        in the command body via $ARGUMENTS.
        """
        for cmd_file in self._get_command_files():
            fm = self._parse_frontmatter(cmd_file)

            assert "argument-hint" in fm, (
                f"Command {cmd_file.name} is missing 'argument-hint' in frontmatter. "
                "argument-hint provides the placeholder shown when invoking the command."
            )

            hint_value = fm["argument-hint"]
            assert hint_value, (
                f"Command {cmd_file.name} has empty argument-hint. "
                "Provide a descriptive placeholder like '<feature-description>'."
            )

    def test_commands_have_allowed_tools(self) -> None:
        """Slash commands should specify allowed-tools for least privilege.

        Key exam concept: allowed-tools restricts which tools the command
        can invoke. This follows the principle of least privilege and
        prevents AP8 (too many tools degrading selection reliability).
        """
        for cmd_file in self._get_command_files():
            fm = self._parse_frontmatter(cmd_file)

            assert "allowed-tools" in fm, (
                f"Command {cmd_file.name} is missing 'allowed-tools' in frontmatter. "
                "Specify which tools this command needs (principle of least privilege)."
            )

            tools = fm["allowed-tools"]
            assert tools, (
                f"Command {cmd_file.name} has empty allowed-tools. "
                "List the specific tools needed, e.g., 'Read, Write, Edit, Bash'."
            )

    def test_commands_reference_arguments_variable(self) -> None:
        """Commands with argument-hint should reference $ARGUMENTS in the body.

        The $ARGUMENTS variable contains whatever the user typed after the
        command name. If you define argument-hint but never use $ARGUMENTS,
        the user's input is ignored.
        """
        for cmd_file in self._get_command_files():
            content = cmd_file.read_text()
            fm = self._parse_frontmatter(cmd_file)

            if "argument-hint" in fm:
                assert "$ARGUMENTS" in content, (
                    f"Command {cmd_file.name} has argument-hint but never uses $ARGUMENTS. "
                    "The $ARGUMENTS variable contains the user's input after the command name."
                )

    def test_allowed_tools_count_under_limit(self) -> None:
        """Commands should not specify more than 8 tools.

        Key exam concept (AP8): 18+ tools degrades selection reliability.
        Even for commands, keep the tool count reasonable.
        """
        for cmd_file in self._get_command_files():
            fm = self._parse_frontmatter(cmd_file)

            if "allowed-tools" in fm:
                tools = [t.strip() for t in fm["allowed-tools"].split(",")]

                assert len(tools) <= 8, (
                    f"Command {cmd_file.name} specifies {len(tools)} tools. "
                    "AP8: Too many tools degrades selection reliability. "
                    "Keep it under 8 for commands, under 5 for agents."
                )
