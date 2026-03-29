# CCA-F Exam Prep — Hands-On Learning System

## Project Context
This is a hands-on prep system for the **Claude Certified Architect — Foundations (CCA-F)** exam.
Every module teaches by DOING — skeleton code with TODOs, not documentation to read.
Theme: fintech (payments, accounts, KYC, fraud) to match real API demo work.

## Domain Weights
| Domain | Weight | Modules |
|--------|--------|---------|
| D1 Agentic Architecture | ~27% | 01, 03 |
| D2 Tool Design | ~18% | 03, 04 |
| D3 Claude Code Configuration | ~20% | 02, 05 |
| D4 Prompt Engineering | ~20% | 05, 06 |
| D5 Context Management | ~15% | 02, 03, 06 |

**Key exam fact:** D1 + D3 = 47% of the exam — front-load these domains.

## #1 Tested Concept
**Programmatic enforcement vs prompt-based guidance.**
When a behavior MUST be GUARANTEED, the answer is ALWAYS programmatic (hooks, prerequisite gates, schema validation).
Prompts can be ignored. Hooks cannot.

## Build Commands
```bash
uv run pytest                                          # Run all tests
ruff check .                                           # Lint
mypy .                                                 # Type check
uv --directory shared/mcp-servers/fintech-mock run server.py  # Start MCP server
```

## Architecture
```
cca-prep/
├── CLAUDE.md              # This file — master reference
├── .mcp.json              # MCP server connections
├── pyproject.toml         # Dependencies
├── progress.json          # Module/tier completion tracking
├── shared/
│   ├── schemas/           # Reusable JSON schemas
│   │   ├── customer.json
│   │   └── order.json
│   ├── mcp-servers/
│   │   └── fintech-mock/  # Fintech MCP server (accounts, orders, KYC, fraud)
│   └── eval/              # Evaluation framework (runner, judge, metrics)
├── modules/
│   ├── support_agent_01/      # D1: Agentic loop, stop_reason, hooks
│   ├── claude_code_config_02/ # D3: CLAUDE.md, rules, slash commands, skills
│   ├── multi_agent_03/        # D1, D2, D5: Coordination, error propagation
│   ├── dev_productivity_04/   # D2, D3: Tool selection, codebase exploration
│   ├── cicd_pipeline_05/      # D3, D4: Non-interactive, session isolation, batch
│   └── extraction_06/         # D4, D5: Forced tool_use, validation-retry, citations
└── .claude/
    ├── commands/          # Slash commands (start-module, check-work, quiz-me, next-challenge)
    ├── agents/            # Custom agents (eval-judge, exam-coach, code-reviewer)
    └── rules/             # Rules (python-style, testing)
```

## Coding Conventions
- Python 3.10+ (3.12+ recommended)
- Type hints on ALL functions
- ruff formatting
- AAA test pattern (Arrange-Act-Assert)
- NEVER hardcode API keys — use environment variables

## The 5 Orchestration Patterns
From Anthropic's "Building Effective Agents":

1. **Prompt Chaining** — Sequential steps, each step's output feeds the next. Gate on quality between steps.
2. **Routing** — Classify input, dispatch to specialized handler. Use tool_choice for forced classification.
3. **Parallelization** — Fan-out independent subtasks, fan-in results. Reduces latency.
4. **Orchestrator-Workers** — Central coordinator delegates to specialized subagents. Coordinator manages ALL inter-agent communication.
5. **Evaluator-Optimizer** — Generate → evaluate → refine loop. Separate sessions for gen vs eval.

## Escalation Triggers

### 3 Valid Triggers (exam-tested)
1. `customer_request` — Customer explicitly asks for a human
2. `policy_gap` — No policy covers this situation
3. `capability_limit` — AI cannot perform the required action

### 2 INVALID Triggers (exam traps)
1. **Sentiment-based triggers** — "Customer sounds angry" is NOT a valid reason
2. **Self-reported confidence scores** — "I'm only 60% confident" is NOT a valid reason

## Technical Reference Card

### stop_reason Values
| Value | Meaning |
|-------|---------|
| `end_turn` | Model finished naturally |
| `max_tokens` | Hit max_tokens limit |
| `stop_sequence` | Hit a custom stop sequence |
| `tool_use` | Model wants to call a tool |
| `model_context_window_exceeded` | Context window full |

### tool_choice Options
| Value | Behavior |
|-------|----------|
| `auto` | Default. Model decides whether to use tools |
| `none` | Model will not use any tools |
| `any` | Model MUST use a tool (any tool). **INCOMPATIBLE with extended thinking** |
| `tool` | Model MUST use a specific named tool. **INCOMPATIBLE with extended thinking** |

### Prompt Caching
- Cache hit = **10% of base cost**
- 5-min TTL = 1.25x write cost
- 1-hour TTL = 2x write cost
- Minimum **1024 tokens** to cache
- Up to **4 cache breakpoints**
- Prefix order: **tools -> system -> messages**

### Batch API
- Max **10,000 requests** per batch
- **50% discount** on token costs
- **24-hour** processing window
- **No SLA**, no streaming, no multi-turn tool calling
- Results as **.jsonl** available for **29 days**

### Extended Thinking
- **Adaptive** — recommended for Claude 4.6
- **Manual budget_tokens** — deprecated on Claude 4.6

### Citations
- `cited_text` is **NOT counted** as output tokens
- **Incompatible** with Structured Outputs (JSON mode)
- Enable on **ALL or NONE** documents
- ~**15% better recall** when enabled

### CLAUDE.md Hierarchy
```
user (~/.claude/CLAUDE.md)
  → project (repo root CLAUDE.md)
    → directory (subdirectory CLAUDE.md)
      → @import references
        → .claude/rules/*.md
```
Only **project-level and below** are shared via VCS.

### Context Windows
| Model | Input | Max Output |
|-------|-------|------------|
| Opus 4.6 | 1M tokens | 128K tokens |
| Sonnet 4.6 | 1M tokens | 64K tokens |
| Haiku 4.5 | 200K tokens | 64K tokens |

Long context pricing (Sonnet 4/4.5): >200K input = 2x input cost, 1.5x output cost.

### Model Pricing (per million tokens)
| Model | Input | Output |
|-------|-------|--------|
| Opus 4.6 | $5 | $25 |
| Sonnet 4.6 | $3 | $15 |
| Haiku 4.5 | $1 | $5 |

## 10 Exam Anti-Patterns

1. **Parsing natural language for loop termination** instead of checking `stop_reason`
2. **Arbitrary iteration caps** as primary stopping mechanism (safety net is OK, primary control is NOT)
3. **Prompt-based enforcement** for critical business rules (use hooks/code instead)
4. **Self-reported confidence scores** for escalation decisions
5. **Sentiment-based escalation triggers** ("customer sounds angry")
6. **Generic error messages** without `isError`, `errorCategory`, `isRetryable` fields
7. **Silently suppressing errors** or returning empty results as success
8. **More than 5 tools per agent** (18+ tools degrades selection reliability)
9. **Same-session self-review** (use separate sessions to avoid confirmation bias)
10. **Aggregate accuracy metrics only** — must track per-document-type AND per-field metrics

## Imported Schemas
@shared/schemas/customer.json
@shared/schemas/order.json

## Reference Materials

Companion study materials live in Notion at:
**https://www.notion.so/3302367dc5ff8015bd89e00af01a69c3**

This Notion workspace contains:
- **Study Guide** — Day-by-day reading plan, Anthropic Academy course sequence, 600+ practice question sources with URLs, technical reference card
- **Official Sample Test** — 12 official exam questions with full explanations, anti-pattern tags per question, self-scoring rubric
- **Project Spec** — Complete reference implementations for every module if you get stuck

When `/quiz-me` or the `exam-coach` agent can't answer something, check the Notion study guide.
