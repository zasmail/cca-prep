"""Tests for Module 02 Advanced — Skills with Context Isolation.

CCA-F Exam Domain: D3 (~20%), D5 Context Management (~15%)

These tests validate skill frontmatter and the critical concept of context isolation.
Skills with context: fork run as isolated subagents — this is the key to AP9 prevention.
"""

from __future__ import annotations


import re
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SKILLS_DIR = Path(__file__).resolve().parent.parent / "skills"


class TestSkillFrontmatter:
    """Skills must have valid YAML frontmatter with required fields."""

    def _get_skill_files(self) -> list[Path]:
        """Get all SKILL.md files in the skills directory tree."""
        files = list(SKILLS_DIR.rglob("SKILL.md"))
        assert len(files) > 0, "No SKILL.md files found in skills/ directory"
        return files

    def _parse_frontmatter(self, filepath: Path) -> dict[str, str]:
        """Parse YAML frontmatter from a skill file."""
        content = filepath.read_text()

        assert content.startswith("---"), (
            f"Skill file {filepath} must start with YAML frontmatter (---). "
            "Frontmatter is required for skills in Claude Code."
        )

        parts = content.split("---", 2)
        assert len(parts) >= 3, (
            f"Skill file {filepath} has malformed frontmatter."
        )

        frontmatter = {}
        for line in parts[1].strip().split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                frontmatter[key.strip()] = value.strip()

        return frontmatter

    def test_skills_have_context_directive(self) -> None:
        """Skills must specify their context mode.

        Key exam concept:
        - context: fork — skill runs in isolated subagent (NEW context window)
        - context: shared — skill runs in the current conversation context

        For security audits, code review, and evaluation tasks,
        context: fork is REQUIRED to prevent AP9 (same-session review bias).
        """
        for skill_file in self._get_skill_files():
            fm = self._parse_frontmatter(skill_file)

            assert "context" in fm, (
                f"Skill {skill_file} is missing 'context:' in frontmatter. "
                "Must specify 'fork' (isolated subagent) or 'shared' (current session)."
            )

            assert fm["context"] in ("fork", "shared"), (
                f"Skill {skill_file} has invalid context value: '{fm['context']}'. "
                "Must be 'fork' or 'shared'."
            )

    def test_audit_skills_use_fork_context(self) -> None:
        """Audit/review skills MUST use context: fork.

        Key exam concept (AP9): Same-session self-review suffers from
        confirmation bias. The reviewer already "knows" what the code is
        supposed to do and is biased toward approving it.

        context: fork creates a new context window where the reviewer
        has NO knowledge of the developer's conversation — it evaluates
        the code objectively.
        """
        for skill_file in self._get_skill_files():
            skill_name = skill_file.parent.name.lower()

            # Skills that involve auditing or reviewing MUST use fork
            audit_keywords = ["audit", "review", "check", "validate", "verify"]
            is_audit_skill = any(kw in skill_name for kw in audit_keywords)

            if is_audit_skill:
                fm = self._parse_frontmatter(skill_file)

                assert fm.get("context") == "fork", (
                    f"Audit skill {skill_file} must use 'context: fork'. "
                    "AP9: Same-session review introduces confirmation bias. "
                    "Fork creates an isolated context for objective evaluation."
                )

    def test_skills_have_tools_directive(self) -> None:
        """Skills must specify their allowed tools.

        Key exam concept: Restricting tools follows the principle of least privilege.
        A security audit skill should only need read tools (Read, Grep, Glob) —
        it should NOT have Write, Edit, or Bash access.
        """
        for skill_file in self._get_skill_files():
            fm = self._parse_frontmatter(skill_file)

            assert "tools" in fm, (
                f"Skill {skill_file} is missing 'tools:' in frontmatter. "
                "Specify the minimum set of tools needed (principle of least privilege)."
            )

    def test_audit_skills_are_read_only(self) -> None:
        """Audit skills should only have read tools — no write capability.

        An audit skill that can modify files defeats the purpose of auditing.
        It should observe and report, not fix.
        """
        for skill_file in self._get_skill_files():
            skill_name = skill_file.parent.name.lower()

            audit_keywords = ["audit", "review", "check"]
            is_audit_skill = any(kw in skill_name for kw in audit_keywords)

            if is_audit_skill:
                fm = self._parse_frontmatter(skill_file)
                tools = fm.get("tools", "")
                write_tools = ["Write", "Edit", "Bash"]

                for tool in write_tools:
                    assert tool not in tools, (
                        f"Audit skill {skill_file} has write tool '{tool}'. "
                        "Audit skills should be READ-ONLY: Read, Grep, Glob. "
                        "They observe and report — they don't modify."
                    )

    def test_skills_have_model_directive(self) -> None:
        """Skills should specify which model to use.

        Key exam concept: Use the right model for the task.
        - opus: Complex reasoning, architecture decisions
        - sonnet: General purpose, good balance of speed/quality
        - haiku: Fast, cheap, simple classification tasks
        """
        for skill_file in self._get_skill_files():
            fm = self._parse_frontmatter(skill_file)

            assert "model" in fm, (
                f"Skill {skill_file} is missing 'model:' in frontmatter. "
                "Specify the appropriate model: opus, sonnet, or haiku."
            )

            valid_models = ["opus", "sonnet", "haiku"]
            assert fm["model"] in valid_models, (
                f"Skill {skill_file} has invalid model: '{fm['model']}'. "
                f"Must be one of: {valid_models}"
            )
