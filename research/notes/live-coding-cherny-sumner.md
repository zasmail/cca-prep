---
title: Live Coding Session - Robo Bun at CwC 2026
speaker: Boris Cherny, Jarred Sumner
source: https://www.youtube.com/watch?v=DlTCu_pNDHE
retrieved: 2026-07-16
themes:
  - claude-code-workflows
  - enforcement-reliability
  - tool-design-mcp
  - orchestration
  - context-engineering
  - evals
---

## Core claims

1. **CLAUDE.md is programmatic enforcement**, not guidance—every repeated pattern must be documented or agents will hallucinate.
2. **Verification loops (CI, tests, code review) are the gating mechanism** for autonomous agent execution at scale.
3. **Hill climbing with metrics** (target + measurement + iteration) is uniquely effective on Opus 4.7 and the only reliable way to close autonomous loops.
4. **Multi-agent complementarity matters more than individual capability**—Code Rabbit catches style, Claude Code catches subtle edge cases.
5. **Bottlenecks shift progressively**: code-writing → testing/CI → verification → planning/taste, automating each layer reveals the next.
6. **Auto mode (permission skipping) is foundational** for parallel agent scaling; human approval gates break autonomous operation.
7. **Signal-to-noise ratio on AI code review is ~90%** (10% false positives), making it usable without full manual review for simple cases.
8. **External metrics (performance benchmarks, test pass rates) are more reliable than model confidence** for deciding when to merge or stop iterating.

## Patterns & frameworks

| Pattern | Explanation |
|---------|-------------|
| **Adversarial code review** | Two agents (Code Rabbit + Claude Code) review each other's changes in a loop, marking comments resolved when fixed. |
| **Hill climbing** | Give model a metric (performance target, test coverage, bug count) + verification mechanism; it iterates autonomously until goal reached. |
| **Self-verification loop** | Agent writes code → runs CI → monitors logs → reads errors → iterates; no human in the loop between stages. |
| **Issue → Reproduce → Auto-PR** | Automate issue triage by having agent attempt reproduction first; only send human-reviewable PRs upstream. |
| **Progressive bottleneck automation** | Identify slowest step in development loop; automate it completely; repeat with newly exposed bottleneck. |

## Numbers & specifics

- **Robo Bun now larger contributor than Jarred** by commit volume to Bun repo (despite merging only ~50% of its PRs).
- **~10% false-positive rate** on Claude Code reviews vs. "had to ignore most output" from prior tools.
- **30+ comment exchanges** in single multi-agent code review thread.
- **Hundreds of agents running in parallel** every night; each agent handles independent issue reproductions.
- **3–4 PRs generated in ~25 minute live demo window** from issue queue.
- **20-minute monitoring interval** for autonomous PR validation (tunable, currently longer than optimal).
- **Opus 4.7 first model** capable of reliable autonomous loops; prior models required scaffolding/token overprovisioning.
- **3 months ago** this pipeline was not feasible; now running daily.
- **No-flicker mode**: virtualized scrolling + rendering, constant memory usage, enables 30+ minute auto-mode sessions without degradation.

## Quotes

1. *"every time that you find yourself repeating something it should probably go in CLAUDE.md because the question now is like how do you make it maintainable to have lots of Claudes running all the time"* — Emphasizes CLAUDE.md as enforcer, not suggestion.

2. *"Robun is now a bigger contributor to Bun than I am…with merging not all of its PRs"* — Shows scale of autonomous contribution despite selective human filtering.

3. *"you can just make it iterate and keep going and keep going until it hits that metric…Opus 47 is uniquely good at this"* — Hill climbing as core pattern, model-dependent.

4. *"the bottleneck now is actually like CI and making sure that the code…making sure all the test stuff works"* — Bottleneck has shifted from capability to verification.

5. *"in auto mode I can let cloud runs for hours and hours at a time…before this it just didn't work cuz it always got stuck at some kind of permission request"* — Permission gating as blocker for scale.

## Applied AI relevance

- **CLAUDE.md ≠ prompt guidance**: Enforce critical constraints (build steps, test placement, error-message ordering) in config, not prose. Prose can be ignored; CLAUDE.md is law.
- **Verification first, not confidence-based**: Never escalate or halt based on model uncertainty. Use external metrics (CI pass/fail, test coverage, performance delta) as ground truth for stopping/merging decisions.
- **Opus 4.7 enables closed loops**: Earlier models lack reliable self-correction within a session; hill climbing requires this. Don't attempt autonomous refining on older models without heavy scaffolding.
- **Complementary agent design wins**: One agent finds style issues, another finds logic bugs. Pair agents with non-overlapping strengths rather than stacking identical capabilities.
- **Auto mode is a prerequisite for scale**: Hundred-agent parallelization breaks under permission prompts. Design UX to minimize human decision gates in hot paths; gate only irreversible actions.
