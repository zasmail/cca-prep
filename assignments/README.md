# Phase C — The Sales-Machine Assignments

> **The hand-typing rule (non-negotiable, applies to every assignment).** You type every line. Claude Code is a **reviewer and explainer only** — ask it *why*, never paste *what*. Every assignment's done-criteria are built so copy-paste can't satisfy them: written explain-backs, deliberate-choice notes, and live demos you run. If the only thing you can say about a line is "Claude wrote it," it fails.

## The arc, in one paragraph

Five assignments build **one machine**, each layer typed by hand on top of the last. **A1** hand-writes a raw-API agentic **loop** that scores your pipeline overnight — termination by `stop_reason` contract, not vibes. **A2** wraps that loop in **enforcement**: hooks that gate every write and deny every send, moving your CLAUDE.md rules from prompt to physics (the #1 tested concept). **A3** builds the **tools the loop calls** — your own Signal API curated from 21 endpoints down to 3 agent-shaped MCP tools, descriptions written as the product. **A4** builds the **judges over the output** — deterministic graders (reusing A2's linter) plus calibrated per-dimension LLM judges, so a model swap becomes evidence instead of faith. **A5** is the **orchestration of the whole**: an orchestrator-workers pipeline that composes every prior layer — A1's loop, A2's gates, A3's tools, A4's judges — with a token budget, disk checkpointing, structured error triage, and a cost ledger you paid yourself. Loop → gates on the loop → tools the loop calls → judges over the output → orchestration of the whole. Five layers, one machine, every layer load-bearing for the next.

## The five assignments

| # | Assignment | Days | Layer | Real deliverable (in `~/dev/Autobound/sales-machine`) | Exam domain |
|---|---|---|---|---|---|
| A1 | The Overnight Scorer | 1–2 | The loop | `scripts/score-icp.py`, 9 accounts scored in frontmatter, Batch API run + `BATCH_NOTES.md` | **D1** Agentic Architecture (~27%) |
| A2 | Make the Rules Real | 3–4 | Gates on the loop | `scripts/lint-draft.py` + PreToolUse lint hook + send-deny in `.claude/settings.json` | **D3** Claude Code Config (~20%) + the #1 concept |
| A3 | Ship Your Own MCP Server | 5–7 | Tools the loop calls | `mcp/signal-server/` (3-tool FastMCP server) + `.mcp.json` + `/scout` skill | **D2** Tool Design (~18%) |
| A4 | The Harness | 8–10 | Judges over the output | `evals/` — `capture.py`, deterministic + LLM graders, `calibrate.py`, `report.py` | **D4** Prompt Eng (~20%) / **D5** Context (~15%) |
| A5 | The Machine | 11–12 | Orchestration of the whole | `scripts/run-machine.workflow.js` orchestrator + checkpointing + `ledger.md` | **D1** / **D5** (capstone) |

Every layer references the one before it. A2's hooks gate A1's loop outputs; A3's server is called by loops like A1's and A5's; A4's judges reuse A2's linter and grade the outputs A1/A3 produce; A5 composes all four. Where a later assignment needs an earlier artifact that isn't built yet, its spec declares an explicit **degraded-mode stand-in** — you run against what's actually there, never a fake.

## The 14-day calendar

**Daily loop (every build day):** 15-min `/quiz-me` drill on the day's domain → the build block for the current milestone → one dated entry in `interview-takes.md` (check off a take only when you can defend it unaided).

| Day | Focus | Milestone target | Extras |
|---|---|---|---|
| 1 | A1 — The loop | Prereqs + M1 (substrate gaps, write contract) + start M2 | `/quiz-me agentic-loops` |
| 2 | A1 — The loop | M2 (every `stop_reason`) → M3 (forced `tool_choice`) → M4 (Batch API) | `/quiz-me batch-api`; log A1 takes |
| 3 | A2 — Gates | Prereqs + M1 (reconcile rules) + M2 (`lint-draft.py`, dual contract) | `/quiz-me hooks` |
| 4 | A2 — Gates | M3 (PreToolUse gate) + M4 (deny send surface) + **M5 red-team** | Log A2 takes → **🎤 Mock design interview #1** |
| 5 | A3 — Tools | Prereqs + M1 (DESIGN.md, the curation cut) + start M2 (server) | `/quiz-me mcp` |
| 6 | A3 — Tools | M2 (error contract, token budget) + M3 (descriptions + `.mcp.json`) | `/quiz-me tools` |
| 7 | A3 — Tools | M4 (`/scout` skill) + M5 (5/5 fresh-session test, token measure) | Log A3 takes |
| 8 | A4 — Judges | Prereqs + M1 (`capture.py`, seed ≥20 cases) | `/quiz-me extraction` |
| 9 | A4 — Judges | M2 (refactor A2 linter → grader) + M3 (per-dimension judges) | `/quiz-me context-management` |
| 10 | A4 — Judges | M4 (calibrate to ≥80%) + M5 (per-dimension report + two-model run) | Log A4 takes |
| 11 | A5 — Machine | Prereqs + M1 (DEPENDENCIES.md + skeleton + ledger) + M2 (gate-then-fanout) | `/quiz-me caching` |
| 12 | A5 — Machine | M3 (budget + checkpointing) + M4 (error triage + outbox gate) + M5 (ledger, live demo) | Log A5 takes |
| 13 | Buffer + polish | Overflow from any slipped milestone; reread all explain-backs | **🎤 Mock design interview #2** |
| 14 | Buffer + polish | Final sweep: done-criteria greps, `interview-takes.md` complete, `git diff` review | `/quiz-me model-selection` |

**Mock design interviews** land at the two natural inflection points: **~Day 4** (after A2 — you can now argue guarantee-vs-preference from a hook you built) and **~Day 13** (after A5 — you can argue multi-agent economics from a ledger you paid). Treat each as a rehearsal for the real thing, not a checkpoint.

**If you slip:** milestones bank at their last green checkpoint. Push overflow into Days 13–14 rather than rushing an explain-back to hit a clock. Never cut the explain-backs or the live demos — those are the copy-paste-proof core.

## Files

- `01-overnight-scorer/SPEC.md` … `05-orchestrated-machine/SPEC.md` — the five assignment specs.
- `_briefs.md` — the original design briefs (the creative core each spec expands).
- `interview-takes.md` — the running log of positions you can argue from experience; every assignment ends by earning three.
