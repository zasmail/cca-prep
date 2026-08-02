# CCA-F Exam Prep — Hands-On Learning System

A build-by-doing prep system for the **Claude Certified Architect — Foundations (CCA-F)** exam.[^1] Six hands-on modules, one per exam scenario, themed around fintech (payments, accounts, KYC, fraud).

**Exam:** 60 multiple-choice and multiple-response items (some questions require selecting more than one correct answer), 120 min, 720/1000 to pass, proctored, no Claude allowed.

[^1]: Official exam code on the guide cover is **CCAR-F**; "CCA-F" is the common short name used here and in Anthropic's own URL slugs.

## Prerequisites

- Python 3.10+ (3.12+ recommended)
- [uv](https://docs.astral.sh/uv/) package manager
- An [Anthropic API key](https://console.anthropic.com/settings/keys)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI

## Quick Start

```bash
# 1. Clone and enter the repo
git clone https://github.com/zasmail/cca-prep.git
cd cca-prep

# 2. Set your API key
export ANTHROPIC_API_KEY=sk-ant-api03-your-key-here

# 3. Install dependencies
uv sync

# 4. Open in Claude Code
claude

# 5. Start Module 01 (highest exam value — 27% of the exam)
/project:start-module 1
```

## Domain Weights

| Domain | Weight | Modules |
|--------|--------|---------|
| D1 Agentic Architecture | ~27% | 01, 03 |
| D2 Tool Design | ~18% | 03, 04 |
| D3 Claude Code Configuration | ~20% | 02, 05 |
| D4 Prompt Engineering | ~20% | 05, 06 |
| D5 Context Management | ~15% | 02, 03, 06 |

**D1 + D3 = 47% of the exam.** Modules 01 and 02 cover these — start there.

## Exam Logistics

- **Structure:** 4 scenarios drawn at random from a bank of 6 per sitting; each scenario anchors several of the 60 items.
- **Retakes:** wait 14 days after a 1st fail, 30 after a 2nd, 90 after a 3rd — max 4 attempts per rolling 12-month period.
- **Validity:** credential is valid for 12 months from the date awarded; renew with a free, non-proctored assessment before it lapses (a lapsed credential requires a full retake at full fee).
- **Out of scope** (won't appear on the exam — don't over-study these): fine-tuning/training custom models, API auth/billing/account management, Claude's internal architecture or model weights, computer use, vision, streaming API internals, tokenization/token-counting algorithms, and prompt-caching *implementation* internals (the caching behavior/pricing rules above are fair game — the underlying mechanics are not).

## Modules

| # | Module | Domains | What You Build |
|---|--------|---------|---------------|
| 01 | Customer Support Agent | D1 | Agentic loop, stop_reason, hooks, escalation |
| 02 | Claude Code Configuration | D3, D5 | CLAUDE.md hierarchy, rules, slash commands, skills |
| 03 | Multi-Agent Research | D1, D2, D5 | Orchestrator-workers, error propagation, subagents |
| 04 | Developer Productivity | D2, D3 | Tool selection, codebase exploration, MCP integration |
| 05 | CI/CD Pipeline | D3, D4 | Non-interactive mode, session isolation, batch API |
| 06 | Structured Extraction | D4, D5 | Forced tool_use, validation-retry, citations two-pass |

Each module has 3 tiers: **starter** (core pattern) → **intermediate** (production concerns) → **advanced** (system design).

## Slash Commands

| Command | What It Does |
|---------|-------------|
| `/project:start-module <1-6>` | Launch a module — shows objectives, scaffolds exercises |
| `/project:check-work` | Run tests, audit anti-patterns, score progress |
| `/project:quiz-me <topic>` | 5 exam-style MCQs with explanations |
| `/project:next-challenge` | Auto-advance to the next tier or module |

## Agents

| Agent | Purpose |
|-------|---------|
| `exam-coach` | Socratic exam coaching — asks before telling |
| `eval-judge` | Evaluates implementations against exam rubric |
| `code-reviewer` | Audits code against all 10 anti-patterns |

## The #1 Exam Concept

**Programmatic enforcement vs prompt-based guidance.**

When a behavior MUST be GUARANTEED, the answer is ALWAYS programmatic (hooks, prerequisite gates, schema validation). Prompts can be ignored. Hooks cannot. This distinction underlies the two highest-weighted domains — D1 + D3 = 47% of the exam by weight (no official source quantifies how often it shows up question-by-question, but weight is the real signal).

## Project Structure

```
cca-prep/
├── CLAUDE.md              # Master reference — technical reference card, anti-patterns
├── .mcp.json              # Fintech mock MCP server connection
├── shared/
│   ├── schemas/           # Reusable JSON schemas (customer, order)
│   ├── mcp-servers/
│   │   └── fintech-mock/  # In-memory fintech MCP server (7 tools)
│   └── eval/              # Evaluation framework (runner, LLM judge, metrics)
├── modules/
│   ├── support_agent_01/
│   ├── claude_code_config_02/
│   ├── multi_agent_03/
│   ├── dev_productivity_04/
│   ├── cicd_pipeline_05/
│   └── extraction_06/
└── .claude/
    ├── commands/          # Slash commands
    ├── agents/            # Custom agents
    └── rules/             # Path-scoped rules
```

## Running Tests

```bash
uv run pytest                           # All tests
uv run pytest modules/support_agent_01/ # Module 01 only
uv run ruff check .                     # Lint
uv run mypy .                           # Type check
```

## License

MIT
