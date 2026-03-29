"""Tests for Module 03 Advanced — Claude Code Native Subagents.

CCA-F Exam Domains: D1 (~27%), D5 Context Management (~15%)

These tests validate that agent files are properly configured and that
the coordinator never passes full conversation history to subagents.
"""

from __future__ import annotations


import re
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

AGENTS_DIR = Path(__file__).resolve().parent.parent / "agents"


class TestAgentFileConfiguration:
    """Agent files must have valid frontmatter with model, tools, and maxTurns."""

    def _get_agent_files(self) -> list[Path]:
        """Get all .md files in the agents directory."""
        files = list(AGENTS_DIR.glob("*.md"))
        assert len(files) > 0, "No agent files found in agents/ directory"
        return files

    def _parse_frontmatter(self, filepath: Path) -> dict[str, str]:
        """Parse YAML frontmatter from an agent file."""
        content = filepath.read_text()

        assert content.startswith("---"), (
            f"Agent file {filepath.name} must start with YAML frontmatter (---)."
        )

        parts = content.split("---", 2)
        assert len(parts) >= 3, (
            f"Agent file {filepath.name} has malformed frontmatter."
        )

        frontmatter = {}
        for line in parts[1].strip().split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                frontmatter[key.strip()] = value.strip()

        return frontmatter

    def test_agents_have_model_specified(self) -> None:
        """Every agent file must specify which model to use.

        Key exam concept: Use the right model for the task.
        Research lead → sonnet (balanced). Fact checker → haiku (fast, cheap).
        """
        for agent_file in self._get_agent_files():
            fm = self._parse_frontmatter(agent_file)

            assert "model" in fm, (
                f"Agent {agent_file.name} must specify 'model' in frontmatter."
            )

            valid_models = ["opus", "sonnet", "haiku"]
            assert fm["model"] in valid_models, (
                f"Agent {agent_file.name} has invalid model '{fm['model']}'. "
                f"Must be one of: {valid_models}"
            )

    def test_agents_have_tools_specified(self) -> None:
        """Every agent must declare its tools (principle of least privilege)."""
        for agent_file in self._get_agent_files():
            fm = self._parse_frontmatter(agent_file)

            assert "tools" in fm, (
                f"Agent {agent_file.name} must specify 'tools' in frontmatter."
            )

    def test_agents_have_max_turns(self) -> None:
        """Every agent must have maxTurns as a safety net.

        Key exam concept: maxTurns is the agent's safety net — it prevents
        runaway token spend. It should NOT be the primary termination condition
        (that's stop_reason), but it must exist.
        """
        for agent_file in self._get_agent_files():
            fm = self._parse_frontmatter(agent_file)

            assert "maxTurns" in fm, (
                f"Agent {agent_file.name} must specify 'maxTurns' in frontmatter. "
                "This is a safety net to prevent runaway token spend."
            )

            max_turns = int(fm["maxTurns"])
            assert max_turns > 0, "maxTurns must be positive"
            assert max_turns <= 50, (
                f"Agent {agent_file.name} has maxTurns={max_turns}. "
                "Keep maxTurns reasonable — high values risk runaway costs."
            )

    def test_agent_tools_under_limit(self) -> None:
        """Each agent should have 5 or fewer tools (AP8).

        Key exam concept (AP8): 18+ tools degrades selection reliability.
        Keep each agent focused with a small, task-appropriate tool set.
        """
        for agent_file in self._get_agent_files():
            fm = self._parse_frontmatter(agent_file)

            if "tools" in fm:
                tools = [t.strip() for t in fm["tools"].split(",")]

                assert len(tools) <= 5, (
                    f"Agent {agent_file.name} has {len(tools)} tools. "
                    "AP8: Keep tools under 5 per agent for reliable selection."
                )


class TestContextIsolation:
    """Coordinator must never pass full conversation to subagents."""

    def test_agent_instructions_state_scoped_context(self) -> None:
        """Agent files should explicitly state they receive scoped context.

        Key exam concept: Subagents should NOT see the full conversation.
        The agent's instructions should make this clear to the model.
        """
        for agent_file in self._get_agent_files():
            content = agent_file.read_text().lower()

            scoping_indicators = [
                "scoped",
                "not full conversation",
                "not full history",
                "only your subtopic",
                "specific subtopic",
                "not see the full",
            ]

            has_scoping = any(phrase in content for phrase in scoping_indicators)

            assert has_scoping, (
                f"Agent {agent_file.name} should explicitly state that it receives "
                "scoped context, not full conversation history. "
                "This reinforces the context isolation pattern."
            )

    def test_agent_instructions_prevent_cross_agent_communication(self) -> None:
        """Agent files should state they don't communicate with other agents.

        Key exam concept: In the orchestrator-worker pattern, workers NEVER
        talk to each other. All communication goes through the coordinator.
        """
        for agent_file in self._get_agent_files():
            content = agent_file.read_text().lower()

            isolation_indicators = [
                "do not communicate",
                "not communicate with other",
                "do not see",
                "not see other",
                "no knowledge of other",
                "don't communicate",
            ]

            has_isolation = any(phrase in content for phrase in isolation_indicators)

            assert has_isolation, (
                f"Agent {agent_file.name} should state that it does not communicate "
                "with other agents. The coordinator manages all inter-agent communication."
            )

    def test_fact_checker_uses_cheaper_model(self) -> None:
        """Fact checker should use haiku — it's a structured verification task.

        Key exam concept: Match model capability to task complexity.
        Fact-checking is structured (check claim against sources) — it doesn't
        need the reasoning depth of sonnet/opus. Haiku is faster and cheaper.
        """
        fact_checker = AGENTS_DIR / "fact-checker.md"

        if not fact_checker.exists():
            pytest.skip("fact-checker.md not found")

        fm = self._parse_frontmatter(fact_checker)

        assert fm.get("model") == "haiku", (
            "Fact checker should use 'haiku' model. "
            "Verification is a structured task — use the cheapest model that can do it well."
        )

    def test_research_lead_has_more_turns_than_fact_checker(self) -> None:
        """Research lead needs more turns (deeper exploration) than fact checker.

        Research involves searching, reading, cross-referencing — more steps.
        Fact checking is bounded — 1-3 searches per claim.
        """
        research_lead = AGENTS_DIR / "research-lead.md"
        fact_checker = AGENTS_DIR / "fact-checker.md"

        if not research_lead.exists() or not fact_checker.exists():
            pytest.skip("Agent files not found")

        rl_fm = self._parse_frontmatter(research_lead)
        fc_fm = self._parse_frontmatter(fact_checker)

        rl_turns = int(rl_fm.get("maxTurns", "0"))
        fc_turns = int(fc_fm.get("maxTurns", "0"))

        assert rl_turns > fc_turns, (
            f"Research lead maxTurns ({rl_turns}) should be > fact checker ({fc_turns}). "
            "Research requires more exploration steps than bounded verification."
        )
