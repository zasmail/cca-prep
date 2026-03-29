"""Tests for Module 04 Intermediate — Codebase Exploration Strategy.

These tests validate that the exploration slash command produces
structured findings following the 4-step incremental discovery pattern.
"""

import pytest


class TestExplorationPatternStructure:
    """The exploration guide must follow the 4-step pattern."""

    def test_exploration_guide_exists(self) -> None:
        """The explore_codebase.md file must exist and be non-empty."""
        from pathlib import Path

        guide_path = Path(__file__).parent.parent / "explore_codebase.md"

        assert guide_path.exists(), "explore_codebase.md must exist"
        content = guide_path.read_text()
        assert len(content) > 100, "explore_codebase.md must have substantial content"

    def test_guide_has_four_steps(self) -> None:
        """The guide must define all 4 steps of incremental discovery."""
        from pathlib import Path

        guide_path = Path(__file__).parent.parent / "explore_codebase.md"
        content = guide_path.read_text().lower()

        assert "step 1" in content, "Must include Step 1: Structure"
        assert "step 2" in content, "Must include Step 2: Threads"
        assert "step 3" in content, "Must include Step 3: Dependencies"
        assert "step 4" in content, "Must include Step 4: Document"

    def test_step1_uses_correct_tools(self) -> None:
        """Step 1 (Structure) must use LS and Glob, not Bash('find')."""
        from pathlib import Path

        guide_path = Path(__file__).parent.parent / "explore_codebase.md"
        content = guide_path.read_text()

        # Step 1 section should reference Glob
        assert "Glob" in content, "Step 1 must use Glob for file discovery"
        # Should reference LS for directory listing
        assert "LS" in content or "ls" in content.lower(), (
            "Step 1 must use LS for directory structure"
        )

    def test_step2_uses_grep_and_read(self) -> None:
        """Step 2 (Threads) must use Grep and Read for targeted exploration."""
        from pathlib import Path

        guide_path = Path(__file__).parent.parent / "explore_codebase.md"
        content = guide_path.read_text()

        assert "Grep" in content, "Step 2 must use Grep for content search"
        assert "Read" in content, "Step 2 must use Read for file contents"

    def test_guide_warns_against_anti_patterns(self) -> None:
        """The guide must explicitly warn against using Bash for dedicated-tool tasks."""
        from pathlib import Path

        guide_path = Path(__file__).parent.parent / "explore_codebase.md"
        content = guide_path.read_text().lower()

        assert "anti-pattern" in content or "anti_pattern" in content, (
            "Guide must explicitly call out anti-patterns to avoid"
        )

    def test_guide_produces_structured_output(self) -> None:
        """Step 4 must define a structured output format for findings."""
        from pathlib import Path

        guide_path = Path(__file__).parent.parent / "explore_codebase.md"
        content = guide_path.read_text().lower()

        # Must define output structure fields
        required_fields = ["architecture", "language", "entry point", "dependencies"]
        for field in required_fields:
            assert field in content, (
                f"Findings output must include '{field}' field. "
                "Structured output ensures findings are reusable."
            )

    def test_guide_is_incremental_not_exhaustive(self) -> None:
        """The guide must emphasize selective reading, not reading everything."""
        from pathlib import Path

        guide_path = Path(__file__).parent.parent / "explore_codebase.md"
        content = guide_path.read_text().lower()

        assert "selective" in content or "not read every" in content or "do not read" in content, (
            "Guide must emphasize incremental/selective exploration, "
            "NOT reading the entire codebase."
        )
