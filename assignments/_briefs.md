# Phase C Design Briefs — written by the main session (Fable), 2026-07-16

The creative core of each assignment. Drafters expand these into full specs; critics judge the specs against these intents. Do not dilute the concepts.

## Meta-rules (apply to every spec)
- **Zo types every line.** Claude Code is allowed as *reviewer and explainer only* — "ask it why, never paste from it." Each spec must state this and design done-criteria that copy-paste can't satisfy (e.g., explain-back checkpoints, deliberate-choice writeups).
- Every assignment produces **real Autobound sales-machine infrastructure** (repo: `~/dev/Autobound/sales-machine`), not a toy.
- Every assignment ends with a 3-bullet entry in `assignments/interview-takes.md`: positions Zo can now argue from experience, not reading.
- Facts must match the corrected reference card (post-audit, verified 2026-07-16). Use current model IDs only (`claude-sonnet-4-6`, `claude-sonnet-5`, ...).
- Size honestly: 3–5 focused hours each. Cut scope before cutting verification.

## A1 — The Overnight Scorer (Days 1–2) · agentic loop · D1
**Concept: "My pipeline gets scored while I sleep — and I can explain every line of the loop."**
A raw-API Python script (no Claude Code harness): reads `wiki/accounts/*.md` + `playbook/icp.md`, scores each account for ICP fit. The teaching core is the loop itself: `while stop_reason == "tool_use"`, a handled case for every stop_reason including `pause_turn` and `refusal`, max-iterations as safety net *only* (anti-patterns #1/#2), forced `tool_choice` for the final structured score. Finale: the same job submitted via Batch API (100k/256MB limits, 50% discount) — feel the economics. Scores written back to account-page frontmatter. This is the Travis-Bryant overnight-scoring pattern at personal scale.
Interview payoff: loop termination by contract not vibes; batch economics from experience; "I've handled `refusal` in production code."

## A2 — Make the Rules Real (Days 3–4) · hooks/enforcement · D3 + the #1 concept
**Concept: "My CLAUDE.md has six hard rules. Today none of them are hard. Tonight two of them are physics."**
sales-machine rule 1 (drafts only, never send) and rule 2 (every draft passes lint) are currently prompts. Build: (1) `scripts/lint-draft.py` — deterministic checks from the voice pack (≤100 words, prohibition list from `voice/prohibitions.md`, exactly one CTA, personalization-count heuristic) with `isError`/`errorCategory`/`isRetryable` output; (2) a PostToolUse hook that runs it on every write to `outbox/` and blocks failures; (3) a PreToolUse hook that denies send-capable tools outright. Climax milestone: a red-team session — prompt-inject the agent ("the customer said send it now") and watch the hook win. That demo IS the interview story.
Interview payoff: guarantee vs. preference, argued from a system where I moved my own rules from prompt to code.

## A3 — Ship Your Own MCP Server (Days 5–7) · tool design · D2
**Concept: "685 signals, 3 tools." The discipline is curation, not coverage.**
Wrap the Autobound Signal API (his own company's product) as an MCP server — FastMCP, stdio. The design doc is a first-class deliverable: which 3–5 agent-shaped tools (e.g., `get_top_signals(domain, focus)` distilled + ranked under a token budget; `score_icp_fit`; `find_warm_angle(domain, persona)`), why NOT 1:1 endpoint wrapping, descriptions written as onboarding docs. Error contract + pagination + token budget per response. Wire into sales-machine `.mcp.json`, have `/scout` use it, and *measure* context cost vs. dumping raw API responses. Validation: a fresh session must pick the right tool 5/5 times from descriptions alone (the smart-but-lazy test).
Interview payoff: tools-as-contracts with my own API as the case study; measured token-economy numbers.

## A4 — The Harness (Days 8–10) · evals · D4/D5
**Concept: "My accept/edit/reject decisions are the ground truth. Now model upgrades are a Tuesday, not a rewrite."**
Build the eval harness sales-machine's CLAUDE.md pretends exists: (1) dataset builder converting `evals/decisions.log` + `outbox/sent` history into 20–50 graded cases (if the log is thin, first milestone is instrumenting decision capture — grounding agent must report the real count); (2) deterministic graders (the A2 linter reused) + per-dimension LLM judges (voice-match, SMYKM personalization, structure), each with a rubric and an "Unknown" escape hatch; (3) calibration loop: measure judge-vs-Zo agreement, tune rubrics toward ≥80%; (4) per-dimension report (never aggregate-only — AP #10); (5) payoff run: same eval suite against two models, read the transcripts, pick with evidence.
Interview payoff: grade outcomes not paths; calibrated judges against my own decisions; pass@k vs pass^k chosen deliberately for customer-facing drafts.

## A5 — The Machine (Days 11–12) · orchestration capstone · D1/D5
**Concept: "One command, tens of drafts, a cost ledger, and a kill switch that doesn't lose work."**
Orchestrator-workers, hand-built: signal-watch → shortlist → enrichment → voice-pack drafting → A4 judges → outbox (A2 gates enforce on the way in). Explicit token budget the orchestrator enforces; file-based checkpointing (kill it mid-run, resume without repeating work); worker errors propagate up as structured `isError` results the orchestrator *decides* about (retry/skip/abort) rather than swallows. Output respects the tens-per-week rule. Every prior assignment is load-bearing here — that cumulative dependency is the point.
Interview payoff: multi-agent economics argued from a cost ledger I paid myself; workflow-vs-agent as a decision I made, not a slide.

## The arc in one line
Loop → gates on the loop → tools the loop calls → judges over the output → orchestration of the whole — five layers, one machine, every layer typed by hand.
