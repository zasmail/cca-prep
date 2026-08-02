---
title: "Demystifying evals for AI agents"
speaker: Anthropic Engineering
source: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
retrieved: 2026-07-16
method: webfetch
note: >
  Copyright limits prevent saving a full verbatim transcript or a lightly-reworded
  paraphrase of this article. Below is a condensed, independently-written study-note
  summary (substantially shorter than, and restructured from, the source) capturing
  the facts and terminology relevant to CCA-F prep. Refer to the source URL for the
  original text.
---

# Demystifying evals for AI agents — study notes

## Core terminology
- **Task**: one test with defined inputs + success criteria.
- **Trial**: one attempt at a task (run multiple trials because models are non-deterministic).
- **Grader**: scoring logic; a task can have multiple graders/assertions.
- **Transcript/trace/trajectory**: the full record of a trial (messages, tool calls, reasoning).
- **Outcome**: the final state of the world after the trial (e.g., did the DB actually get updated).
- **Evaluation harness**: infra that runs tasks end-to-end (instructions, tools, concurrency, grading, aggregation).
- **Agent harness/scaffold**: the system that turns a model into an agent (e.g., Claude Code, Agent SDK).
- **Evaluation suite**: a set of tasks measuring one broad capability.

## Why build evals
- Manual testing/user feedback works early but breaks down at scale — teams without evals debug reactively (wait for complaints → reproduce → fix → hope nothing else broke).
- Evals let teams: separate real regressions from noise, test changes against many scenarios pre-deploy, quantify improvement, and adopt new model releases in days instead of weeks.
- Case studies cited: Claude Code (evals started narrow — concision, file editing — then expanded to behaviors like over-engineering); Descript (moved from manual grading to LLM grading + periodic human calibration, running separate quality-benchmark and regression suites); Bolt (built an eval system in ~3 months combining static analysis, browser-agent testing, LLM judges).
- Evals become the shared "language" between product and research teams for what to optimize.

## Grader types
- **Code-based**: exact/regex/fuzzy match, static analysis (lint/type-check/security scan), outcome checks, tool-call verification, transcript metrics (turns, tokens). Fast, cheap, objective, but brittle to valid variation.
- **Model-based (LLM-as-judge)**: rubric scoring, natural-language assertions, pairwise comparison, reference-based grading, multi-judge consensus. Flexible/scalable for open-ended output, but non-deterministic, costlier, needs calibration against humans.
- **Human graders**: SME review, crowdsourcing, spot checks, A/B tests, inter-annotator agreement. Gold standard, used to calibrate model graders; slow and expensive.
- Scoring can be weighted (combined score must clear a threshold), binary (all graders must pass), or hybrid.

## Capability vs. regression evals
- **Capability evals**: "what can the agent do well?" — start at low pass rates, give a concrete improvement target.
- **Regression evals**: "does it still do what it used to?" — should stay near 100%; a drop signals a break.
- Saturated capability evals graduate into the regression suite.

## Evaluating by agent type
- **Coding agents**: rely on well-specified tasks, stable environments, real test execution. Benchmarks: SWE-bench Verified (real GitHub issues, grade by whether the test suite now passes without breaking others — jumped from ~40% to 80%+ in a year); Terminal-Bench (end-to-end tasks like building a Linux kernel). Grading layers: pass/fail tests + code-quality rubric + static analysis (ruff/mypy/bandit) + state checks + tool-call verification; also track turns, tool-call count, tokens, latency (TTFT, tokens/sec, TTLT).
- **Conversational agents** (support/sales/coaching): need end-state outcome checks + rubrics for interaction quality; multi-turn user simulation usually needs a second LLM playing the "user." Benchmarks: τ-Bench / τ2-Bench (simulated multi-turn retail/airline scenarios).
- **Research agents**: quality is contextual (what counts as "comprehensive" varies by task type); benchmark: BrowseComp (hard-to-solve, easy-to-verify web lookup). Best combo: groundedness checks (claims supported by sources), coverage checks (must-include facts), source-quality checks (primary vs. top-ranked-but-shallow sources); exact match for objectively-answerable facts.
- **Computer-use agents**: interact via screenshots/clicks/keyboard on real GUIs; must check actual backend state, not just apparent success. Benchmarks: WebArena (browser tasks, URL/page-state + backend checks), OSWorld (full OS control, checks file system/app config/DB state/UI properties). Tradeoff: DOM-based interaction = fast but token-heavy; screenshot-based = slower but token-efficient (cited example: Claude for Chrome learning to use DOM for Wikipedia text vs. screenshots for shopping).

## Non-determinism metrics
- **pass@k**: probability the agent succeeds at least once in k attempts — rises with k. Matters when any one success suffices (e.g., coding, pass@1 typically).
- **pass^k**: probability *all* k trials succeed — falls with k. Matters for customer-facing agents needing consistent behavior every time. Example: 75% single-trial success rate → all-3-succeed probability ≈ 42% (0.75³).
- At k=1 the two metrics are identical; they diverge sharply as k grows (pass@k → ~100%, pass^k → ~0% by k=10 in the article's illustrative graph).

## Roadmap to build good evals (Step 0–8)
0. **Start early** — 20-50 tasks from real failures beats waiting to build hundreds.
1. **Start from what you already test manually** — convert existing manual checks and real bug-tracker/support issues into test cases.
2. **Write unambiguous tasks with reference solutions** — an independent expert should get the same answer; a frontier model scoring 0% across many trials (0% pass@100) usually means a broken task, not agent incapability; always build one known-good reference solution.
3. **Build balanced problem sets** — test both where a behavior should and shouldn't trigger (example: Claude.ai web search evals had to cover both "should search" and "shouldn't search" cases to avoid over/under-triggering).
4. **Build a robust, isolated harness** — clean environment per trial; shared state across trials causes correlated failures or unfair advantages (e.g., an agent peeking at leftover git history from a prior trial).
5. **Design graders thoughtfully** — prefer deterministic graders, use LLM graders when needed, use humans for validation; grade the outcome, not the exact path (agents find valid alternate routes); give partial credit for multi-step tasks; calibrate LLM graders against human judgment and give them an "Unknown" escape hatch; watch for exploitable/gameable grading. Cited failure case: Opus 4.5 scored only 42% on CORE-Bench due to rigid numeric grading (rejecting "96.12" vs. expected long decimal) and unreproducible tasks — after fixes, score reached 95%. METR found τ-Bench penalized Claude for correctly following instructions because the grader's threshold logic was backwards.
6. **Read the transcripts** — the only way to know if a grader is fair or a failure is a genuine agent mistake.
7. **Watch for capability-eval saturation** — e.g., SWE-Bench Verified went from ~30% to 80%+ within the year; near-saturated evals compress real gains into small score changes (Qodo initially undervalued Opus 4.5 because one-shot evals didn't capture gains on longer agentic tasks).
8. **Keep suites healthy long-term** — dedicated evals-infra owners + domain experts/product teams contributing tasks (even via PRs from non-engineers using Claude Code) keeps suites alive and relevant.

## How evals fit with other methods (the "Swiss Cheese" framing)
No single method catches everything — combine:
- **Automated evals**: fast, reproducible, no user impact, but need upfront + ongoing investment and can create false confidence if unrepresentative.
- **Production monitoring**: real usage/ground truth but reactive (users hit it first) and noisy.
- **A/B testing**: measures real outcomes but slow (needs traffic/days-weeks) and low-signal on *why*.
- **User feedback**: real signal but sparse, self-selected, rarely explains the failure.
- **Manual transcript review**: builds intuition, catches subtle issues, but slow/inconsistent/not scalable.
- **Systematic human studies**: gold-standard, used to calibrate LLM graders, but expensive and slow.
Mapped to lifecycle: automated evals pre-launch/CI, monitoring + A/B post-launch, feedback/review ongoing, human studies for calibration.

## Frameworks (appendix)
Harbor (containerized envs, standardized task/grader format, ships Terminal-Bench 2.0), Braintrust (offline eval + production observability + autoevals library), LangSmith (tracing/eval tied to LangChain), Langfuse (self-hosted open-source alternative), Arize (Phoenix open-source / AX SaaS). Framework choice matters less than the quality of the test cases and graders you put into it.

## Exam-relevant takeaways
- Key formulas: pass@k rises with k, pass^k falls with k; know which applies to which agent type.
- "0% pass rate across many trials usually means broken task/grader, not incapable model" is a classic gotcha.
- This directly reinforces the CLAUDE.md's #1 tested concept adjacent idea: evals need programmatic/deterministic grading where possible, human/LLM grading calibrated and reserved for genuinely subjective quality.
