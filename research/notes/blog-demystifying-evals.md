---
title: Demystifying evals for AI agents
speaker: Anthropic Engineering
source: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
themes:
  - evals
  - orchestration
  - enforcement-reliability
  - claude-code-workflows
  - tool-design-mcp
---

## Core claims

1. Manual testing breaks down at scale; evals are the primary mechanism to separate real regressions from noise before deploy.
2. Grader design is critical: code-based graders are fast/objective but brittle; model-based graders are flexible but non-deterministic and need human calibration.
3. Capability evals measure potential (start low, set improvement targets); regression evals ensure stability (stay near 100%, detect breaks).
4. Different agent archetypes require different eval strategies: coding agents need test execution + static analysis; conversational agents need user simulation + outcome checks; research agents need groundedness + coverage checks; computer-use agents must check backend state, not just UI state.
5. Non-determinism demands two metrics: pass@k (probability of ≥1 success in k trials, rises with k) and pass^k (probability all k trials succeed, falls with k).
6. "0% pass rate across many trials usually means broken task/grader, not incapable model" — a critical debugging insight.
7. Evals become the shared language between product and research teams for what to optimize.
8. Grade outcomes, not exact paths; agents find valid alternate routes.
9. Eval suites require dedicated long-term ownership + domain-expert contributions.
10. No single method catches everything; layer evals with production monitoring, A/B testing, user feedback, manual review, and periodic human calibration.

## Patterns & frameworks

- **pass@k vs pass^k**: pass@k rises with k; pass^k falls. Example: 75% single-trial success → ~42% all-3-trials success (0.75³).
- **LLM-as-judge**: rubric scoring, pairwise comparison, reference-based grading, multi-judge consensus for open-ended output; needs calibration against humans.
- **Balanced problem sets**: test both trigger-cases and non-trigger-cases (e.g., Claude.ai web search: "should search" + "shouldn't search" evals).
- **Isolated harness**: clean environment per trial; shared state across trials causes correlated failures or unfair advantages.
- **Roadmap 0–8**: start early (20-50 tasks from real failures) → convert manual checks → write unambiguous tasks + reference solutions → balanced problem sets → robust harness → thoughtful grader design → read transcripts → watch saturation → maintain long-term.
- **Swiss Cheese defense**: combine automated evals (pre-launch/CI) + production monitoring (post-launch, reactive) + A/B tests (slow, needs traffic) + user feedback (sparse, self-selected) + manual review (intuition, slow) + human studies (calibration, expensive).

## Numbers & specifics

- **Claude Code**: evals started narrow (concision, file editing), expanded to behaviors like over-engineering.
- **Descript**: moved from manual grading to LLM grading + periodic human calibration; separate quality-benchmark and regression suites.
- **Bolt**: built eval system in ~3 months combining static analysis, browser-agent testing, LLM judges.
- **SWE-Bench Verified**: jumped from ~40% to 80%+ within one year.
- **Opus 4.5 CORE-Bench**: scored 42% due to rigid numeric grading (rejecting "96.12" vs. long decimal); reached 95% after fixes.
- **METR τ-Bench**: penalized Claude for correctly following instructions because grader's threshold logic was backwards.
- **Qodo**: initially undervalued Opus 4.5 because one-shot evals didn't capture gains on longer agentic tasks.
- **Start with**: 20-50 tasks from real failures beats waiting to build hundreds.

## Quotes

1. "0% pass rate across many trials usually means broken task/grader, not incapable model."
2. "Grade the outcome, not the exact path."
3. "Evals become the shared language between product and research teams for what to optimize."
4. "No single method catches everything."
5. "The only way to know if a grader is fair or a failure is a genuine agent mistake is to read the transcripts."

## Applied AI relevance

- **Reliability vs. capability**: Understand pass@k vs pass^k distinction. Customer-facing agents need pass^k (consistent every time); research tasks can accept pass@k (one good answer). Mismatched metrics hide instability.
- **Infrastructure maturity**: Evals are not optional for agentic systems. Start with 20-50 real failures; convert existing bugs into tests; grow deliberately. Teams without evals debug reactively.
- **Grader design discipline**: Prefer deterministic, outcome-focused graders. Reserve LLM graders for genuinely subjective quality (rubric scoring), and always calibrate against human judgment. Transcripts are the gold standard for debugging unfair/broken graders.
- **Saturation planning**: As evals saturate (capability floor rises), small score changes compress real gains. Plan transitions from capability evals into regression suites. Monitor for exploitable/gameable grading logic.
