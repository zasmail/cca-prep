# CCA-F Repo Framework Audit — 2026-07-16

Inputs: five verified fact sheets in `research/audit/facts-*.md` (exam-blueprint, api-mechanics, models-pricing, claude-code-config, beyond-exam-delta), the 30-item findings set, and spot-checks of the live repo. Ground truth = official Anthropic properties only (the exam guide PDF, `platform.claude.com`, `code.claude.com`, `anthropic.com/news`).

---

## Verdict on the D1–D5 framework

**Structure: CONFIRMED. Pedagogy: substantially confirmed in spirit. Reference-card facts: riddled with errors.** These are three different trust levels and the repo conflates them.

**What is confirmed cold** (fetched from the official *Claude Certified Architect – Foundations Exam Guide*, v1.0, effective July 2026):

- **Domain names and weights** — all five match exactly: D1 Agentic Architecture & Orchestration 27%, D2 Tool Design & MCP Integration 18%, D3 Claude Code Configuration & Workflows 20%, D4 Prompt Engineering & Structured Output 20%, D5 Context Management & Reliability 15%. The repo abbreviates the official titles but the weights and substance are exact. **"D1 + D3 = 47%" is correct.**
- **Exam logistics** — 60 items, 120 minutes, 720/1000 scaled passing score, proctored. All confirmed.
- **The six scenarios** map almost one-to-one onto the repo's six modules — the module set was clearly built to mirror the official scenario bank. This is a genuine strength.
- **The "#1 tested concept" (programmatic enforcement vs. prompt guidance) and the escalation/anti-pattern framing are directionally right.** The guide's own objectives (§5) use near-verbatim language the repo also uses: "parsing natural language signals to determine loop termination," "setting arbitrary iteration caps as the primary stopping mechanism," and sentiment-based / self-reported-confidence escalation being explicitly called out as invalid. So the pedagogy is anchored in real blueprint objectives, not invented.

**What could NOT be verified — and what that means:**

- **The escalation-trigger taxonomy (3 valid / 2 invalid) and the "5 orchestration patterns" as *named, enumerated* concepts** were not found verbatim on any official page (facts-claude-code-config Unverifiable list). The *ideas* match the guide's objectives; the specific enumeration is Anthropic-Academy/prep framing, not quotable product doc. Trust the concepts, don't represent the exact list as "official."
- **Frequency claims are invented.** README's "this distinction appears in nearly half the exam questions" and the implication that MCQ = single-answer are not supported. The guide says items are **"multiple-choice AND multiple-response"** — some questions require selecting more than one answer. No official source quantifies how often any concept appears; the only real number is domain weight (D1+D3=47%), which is about weight, not question-content overlap.
- **The official exam code is "CCAR-F," not "CCA-F"** (guide cover). "CCA-F" is fine as the common name (Anthropic's own URL slugs use it) but it is not the formal code.

**Bottom line:** the *skeleton* of the framework (domains, weights, scenarios, the enforcement thesis) is trustworthy and well-built. The *reference card and module fact-claims bolted onto it* are where the rot is — a fabricated model ID in runnable code, a module built on a factual inversion (citations), and a cluster of stale/unverifiable numbers. A learner who trusts the framing is fine; a learner who memorizes the reference card will walk in with several wrong "facts."

---

## Corrections ranked by blast radius

| Rank | File(s) | What's wrong / stale | Correction | Source |
|---|---|---|---|---|
| 1 | 11 runnable `.py` files: `support_agent_01/{starter/agent.py:144, intermediate/agent_with_hooks.py:130, advanced/production_agent.py:119, solutions/agent_solution.py:392, solutions/hooks_solution.py:244}`, `multi_agent_03/starter/coordinator.py:234`, `cicd_pipeline_05/advanced/batch_review.py:98`, `extraction_06/{starter/extractor.py:131,199, intermediate/validation_retry.py:114, advanced/citations_extraction.py:58,88,170}`, `shared/eval/judge.py:46,120` | **Fabricated model ID `claude-sonnet-4-6-20250514`** used as the default model everywhere. This ID never existed — the 4.6 generation uses dateless IDs only (`claude-sonnet-4-6`); the `20250514` suffix belongs to the retired `claude-sonnet-4-20250514` (Sonnet 4). Every module's runnable code will 404 / error on an invalid model. | Replace with `claude-sonnet-4-6` (dateless) or, to match the current lineup, `claude-sonnet-5`. Fix the hardcoded pricing-lookup key in `judge.py:120` too. | facts-models-pricing §"Whether claude-sonnet-4-6-20250514 ever existed" (lines 148–157) |
| 2 | `extraction_06/advanced/citations_extraction.py:6,15,121,232`, its module CLAUDE.md, README:54, `test_citations.py:32-51,106-118,136-138` | **Module's central thesis is factually inverted.** It teaches "Citations API is INCOMPATIBLE with tool_use, you MUST use two passes," with a `demonstrate_incompatibility()` function and tests that *enforce* the claim. Official docs: citations are incompatible with **Structured Outputs** (`output_config.format`), NOT with `tool_use`. The entire two-pass rationale rests on conflating two different features. | Rewrite the module around the real incompatibility (Citations + Structured Outputs → 400 error). Citations + tool_use can coexist. Delete/repurpose the incompatibility demo and its asserting tests. | facts-api-mechanics §5 (400 error on `output_config.format` + citations) |
| 3 | `CLAUDE.md:114`, `cicd_pipeline_05/advanced/batch_review.py:14,124,155`, `test_batch.py`, `wiki/top-20-things-to-internalize.md:52` | **Batch API "max 10,000 requests" is wrong** and test-enforced in code. | Current official limit is **100,000 requests OR 256 MB, whichever comes first**. Update the reference card, the module constant, the test assertion, and the wiki flashcard. | facts-api-mechanics §3; facts-models-pricing "Batch API" |
| 4 | `CLAUDE.md:117`, `cicd_pipeline_05/advanced/batch_review.py:12,125,153`, `test_batch.py:148-158`, `wiki/top-20-things-to-internalize.md:52` | **"No multi-turn tool calling" in Batch is wrong** and enforced by `test_code_documents_no_multi_turn`. | Multi-turn conversations AND tool use (incl. server tools) ARE supported in Batch. Only `stream:true`, thread/`store` continuation params, cache hints, `max_tokens:0`, and Fast mode are unsupported. Drop the claim; fix the test. | facts-api-mechanics §3 |
| 5 | `claude_code_config_02/README.md:12` | **"Directory-level CLAUDE.md overrides project-level"** — wrong mental model in a D3 (20%) teaching module. | CLAUDE.md files are **concatenated**, not overridden. Directory-level content loads *after* project-level (more recency/attention), but nothing is discarded. | facts-claude-code-config #4 |
| 6 | `CLAUDE.md:130-137` | **CLAUDE.md hierarchy diagram is incomplete and mis-structured** (D3 core topic). Omits the top tier (org **Managed policy** CLAUDE.md, loads first, cannot be excluded) and **Local** scope (`CLAUDE.local.md`). Also presents `@imports` and `.claude/rules/*.md` as sequential hierarchy nodes — they are separate mechanisms. | Real load order (broadest→narrowest): **Managed policy → User → Project → Local**. `@imports` resolve relative to the importing file (max depth 4); rules without `paths` frontmatter load at the *same* priority as `.claude/CLAUDE.md`, not "after directory." | facts-claude-code-config #1–5, #14–15, #20 |
| 7 | `.claude/agents/{code-reviewer.md, eval-judge.md, exam-coach.md}` (line 1 each) | **All three subagent files omit the required `name` and `description` frontmatter fields** — invalid/incomplete per the documented subagent schema. Without `name`, hooks/Task tool have no identifier; without `description`, no auto-delegation signal. | Add `name:` and `description:` to each. (`model: sonnet` in exam-coach is current and fine.) | facts-claude-code-config #49–50; sub-agents-clean.txt L252-253 |
| 8 | `CLAUDE.md:144` (Context Windows table) | **"Sonnet 4.6 \| 64K tokens" max output is wrong.** | Sonnet 4.6 max output is **128K**, not 64K. Only Sonnet 4.5 / Opus 4.5 (200K-context tier) and Haiku 4.5 are 64K-capped. | facts-models-pricing "Legacy/Still-Active Models" |
| 9 | `CLAUDE.md:109`, `wiki/context-engineering.md:40`, `wiki/top-20-things-to-internalize.md:51` | **"Minimum 1024 tokens to cache" stated as a flat universal rule.** Wrong for two models named in this same repo's pricing table. | Model-dependent: Sonnet 5/Opus 4.8 = 1,024; Fable 5/Mythos 5 = 512; **Opus 4.6 & Haiku 4.5 = 4,096**; Haiku 3.5 = 2,048. Caveat it. | facts-api-mechanics §4 |
| 10 | `CLAUDE.md:95` (stop_reason table) | **Only 5 stop_reason values listed; current docs list 7.** Stale. | Add `pause_turn` (long-running/server-tool turn paused; resend as-is) and `refusal` (model declined; returned as HTTP 200, notable for Fable 5 safety classifiers). | facts-api-mechanics §1 |
| 11 | `CLAUDE.md:165`, `dev_productivity_04/starter/tool_selection.py:15,139,147`, its module CLAUDE.md:21, `multi_agent_03/CLAUDE.md:24`, `mcp_integration.py:14,232`, `test_tools.py:212,221` | **Anti-pattern #8 "more than 5 tools / 18+ degrades ~40%"** — the `~40%` figure is unverifiable AND the whole hard-cap framing is stale. | No official source states ~40%. Anthropic's Nov 2025 "Advanced Tool Use" (Tool Search Tool, Programmatic Tool Calling) reframes tool-count ceilings as an architecture choice, not a hard cap. Keep as a heuristic but caveat; drop the invented percentage. Note: not confirmed whether the exam blueprint still tests the old heuristic. | facts-beyond-exam-delta §3 #13 |
| 12 | `CLAUDE.md:128`, `extraction_06/advanced/citations_extraction.py:15,121,232`, README:54, `test_citations.py:136-138` | **"~15% better recall when enabled"** — no official source states any percentage. Test-enforced as a required substring. | Official page only says citations are "significantly more likely to cite the most relevant quotes." Drop the number or label as unsourced. Remove the test assertion. | facts-api-mechanics §5 (Unverifiable #1) |
| 13 | `CLAUDE.md:147` | **"Long context pricing (Sonnet 4/4.5): >200K = 2x/1.5x"** — no current official source, and internally incoherent (Sonnet 4.5 has only a 200K window, so a >200K rule can't apply). | Remove or mark legacy/unverified. Current docs: all 1M-context models bill at standard rates across the full window, no multiplier, no beta header. | facts-models-pricing "Long-Context Pricing" |
| 14 | `README.md:5`, `.claude/commands/quiz-me.md` (and CLAUDE.md quiz framing) | **"60 MCQ" implies single-answer.** | Format is **multiple-choice AND multiple-response**; some items require selecting several correct answers (stated per item). Update `/quiz-me` to generate multi-select items too. Count/time/score are correct. | facts-exam-blueprint §2 |
| 15 | `README.md:80` | **"appears in nearly half the exam questions"** — unverifiable frequency claim. | No official source. Soften to "underlies the highest-weighted domains (D1+D3=47% by weight)." | facts-exam-blueprint (no such fraction exists) |
| 16 | `wiki/orchestration-patterns.md:43` | **"Context window 200K default, 1M beta"** — stale. | For all current 1M-context models, 1M is the *default* (no beta header, standard pricing). | facts-models-pricing "Context Windows — Additional Confirmed Facts" |
| 17 | `README.md:5` + `CLAUDE.md` (name usage) | **"CCA-F" is the informal name, not the official code.** ok-notable, not wrong. | Official code on the guide cover is **CCAR-F**. Add a footnote if precision matters. | facts-exam-blueprint §2 |
| 18 | `CLAUDE.md:149-154` (Model Pricing table) | **Reference model set is stale** — the individual numbers (Opus 4.6 $5/$25, Sonnet 4.6 $3/$15, Haiku 4.5 $1/$5) are *correct*, but the table omits the current flagships. ok-notable. | Add current lineup: Fable 5/Mythos 5 $10/$50, Sonnet 5 $2/$10 intro → $3/$15, Opus 4.8 $5/$25. Sonnet 5 is the current default Free/Pro model. | facts-models-pricing "Pricing Per MTok"; facts-beyond-exam-delta §4 |
| 19 | `.claude/commands/*.md` (all four) | **Legacy command format** vs. current `.claude/skills/<name>/SKILL.md`. Not broken. ok-notable. | Legacy `.claude/commands/` still works identically. If the repo wants to model current D3 best practice, migrate to SKILL.md (gains supporting files, `disable-model-invocation`, etc.). No `description` field is fine (only "recommended"). | facts-claude-code-config #37, #38, #39, #84 |

---

## Two-track map (spine for the study-guide redo)

### Track 1 — In the exam (verified blueprint topics → repo coverage)

| Blueprint topic (official, confirmed) | Weight | Repo coverage | Health |
|---|---|---|---|
| D1 Agentic Architecture & Orchestration — agentic loop, `stop_reason`-driven termination, hooks vs. prompts, escalation triggers, orchestration patterns | 27% | `support_agent_01`, `multi_agent_03`; CLAUDE.md enforcement thesis | Strong pedagogy; fix stop_reason table (add `pause_turn`/`refusal`), fabricated model ID |
| D2 Tool Design & MCP Integration — tool schemas, error fields (`isError`/`errorCategory`/`isRetryable`), tool selection, MCP | 18% | `multi_agent_03`, `dev_productivity_04`; fintech-mock MCP server | Solid; reframe the "5 tools / ~40%" anti-pattern as heuristic-not-cap |
| D3 Claude Code Config & Workflows — CLAUDE.md hierarchy, rules, skills/commands, settings, headless mode | 20% | `claude_code_config_02`, `cicd_pipeline_05` | Highest-error zone: hierarchy diagram wrong, "override" mental-model error, agent files invalid, legacy command format |
| D4 Prompt Engineering & Structured Output — forced `tool_use`, `tool_choice`, structured outputs, validation-retry, citations | 20% | `cicd_pipeline_05`, `extraction_06` | Citations module built on an inverted fact — must-fix |
| D5 Context Management & Reliability — context windows, prompt caching, compaction, batch | 15% | `claude_code_config_02`, `multi_agent_03`, `extraction_06` | Cache-minimum and batch-limit facts wrong |
| Exam logistics — 60 items (MC + multi-response), 120 min, 720/1000, 4-of-6 scenarios, Pearson VUE, $125, 12-mo validity | — | README, CLAUDE.md | Fix "MCQ" framing; add multi-response, scenario-bank, retake facts |

Confirmed but *not yet in the repo* and worth adding to the study guide: the **4-of-6 scenario draw**, retake waiting periods (14/30/90 days, max 4/yr), 12-month credential validity + free renewal, and the explicit **out-of-scope list** (fine-tuning, billing, model internals, computer use, vision, streaming internals, tokenization, prompt-caching *implementation* internals) — knowing what's excluded prevents over-studying.

### Track 2 — Beyond the exam, new & relevant (from facts-beyond-exam-delta)

What an Applied AI engineer should know that the July-2026 exam framing likely misses. Each is a candidate "current best practice" callout box.

| Topic | Why it matters | Source |
|---|---|---|
| **Tool Search Tool + Programmatic Tool Calling** (Nov 24, 2025) | Directly obsoletes anti-pattern #8's hard tool cap. Tool Search keeps tool defs out of context until requested (scales to thousands of tools); Programmatic Tool Calling has Claude write code to orchestrate N tools in one round-trip. Highest-value D2 update. | anthropic.com/engineering/advanced-tool-use; facts-beyond-exam §3 #13 |
| **Code execution with MCP** (Nov 4, 2025) | The token-efficiency argument behind Programmatic Tool Calling: 150,000 → 2,000 tokens (98.7%) by presenting MCP servers as code APIs. Core D5 context-engineering technique. | anthropic.com/engineering/code-execution-with-mcp; §6 #24 |
| **`refusal` stop_reason + Fable 5 safety classifiers** | New `stop_reason: "refusal"` returned as HTTP 200 (not an error); needs fallback handling (`fallbacks` param / SDK middleware). Changes how you write robust agent loops. | facts-beyond-exam §4 #16; facts-api-mechanics §1 |
| **Fable 5 / Mythos 5 tier above Opus** + **Sonnet 5 as new default** | The whole reference-card model lineup is a generation behind. Fable 5 ($10/$50), Sonnet 5 (default Free/Pro since Jun 30 2026). Adaptive thinking is the *only* mode; `effort` param replaces manual `budget_tokens`. | facts-beyond-exam §4; facts-models-pricing |
| **Agent SDK (renamed from Claude Code SDK) vs. Claude Managed Agents** | Architectural line the repo never draws: SDK = agent loop in *your* process; Managed Agents = hosted REST API (Anthropic runs harness+sandbox). Prototype on SDK → productionize on Managed Agents. | facts-api-mechanics §7; facts-beyond-exam §2 |
| **Claude Code Routines + Managed Agents scheduling/Vaults** | Scheduled/event-triggered cloud automation — the operational surface beyond interactive Claude Code. | facts-beyond-exam §1 #4–6 |
| **Agent Skills open standard + Plugins** | `.claude/skills/<name>/SKILL.md` with progressive disclosure is now the recommended format; the repo's `.claude/commands/` is legacy. Plugins bundle skills+agents+hooks+MCP. Direct D3 currency gap. | facts-beyond-exam §5; facts-claude-code-config #37–48 |
| **Context engineering as its own discipline** (Sept 29, 2025) | Anthropic formally distinguishes *context engineering* from *prompt engineering* — the intellectual backbone of D5. | anthropic.com/engineering/effective-context-engineering-for-ai-agents; §6 #23 |
| **MCP donated to the Agentic AI Foundation** (Dec 9, 2025) | Governance moved to a Linux Foundation fund; upcoming spec (RC 2026-07-28) goes stateless at transport, adds MCP Apps. Context for "who owns MCP now." (Spec source is non-Anthropic — treat as context, not ground truth.) | facts-beyond-exam §3 #11–12 |

---

## Proposed changes (awaiting approval — no edits made)

### (a) Must-fix — wrong facts / broken code

1. **Replace `claude-sonnet-4-6-20250514` → `claude-sonnet-4-6`** across all 11 code files + the `judge.py:120` pricing key. *(support_agent_01 ×5, multi_agent_03 coordinator, cicd batch_review, extraction_06 ×3 files, shared/eval/judge.py)* — fixes runnable code.
2. **Rewrite the citations module** (`extraction_06/advanced/citations_extraction.py`, its CLAUDE.md, README:54, `test_citations.py`) around Citations-vs-**Structured-Outputs** incompatibility; remove the false tool_use claim, the `demonstrate_incompatibility()` demo, and the asserting tests.
3. **Fix Batch limits** (CLAUDE.md:114, batch_review.py:14/124/155, test_batch.py, wiki/top-20:52): 10,000 → **100,000 or 256 MB**.
4. **Fix Batch multi-turn claim** (CLAUDE.md:117, batch_review.py:12/125/153, test_batch.py:148-158, wiki/top-20:52): multi-turn + tool use ARE supported; only streaming/thread-params unsupported.
5. **Fix CLAUDE.md hierarchy diagram** (CLAUDE.md:130-137): add Managed policy + Local; separate `@imports`/`.claude/rules` from the scope chain.
6. **Fix "directory overrides project"** (claude_code_config_02/README.md:12): concatenation, not override.
7. **Fix Sonnet 4.6 max output** (CLAUDE.md:144): 64K → **128K**.
8. **Add `name` + `description` frontmatter** to all three `.claude/agents/*.md` files.

### (b) Should-update — stale

9. **stop_reason table** (CLAUDE.md:95): add `pause_turn`, `refusal`.
10. **Prompt-cache minimum** (CLAUDE.md:109, wiki/context-engineering.md:40, wiki/top-20:51): flag as model-dependent (512–4,096).
11. **Model pricing/lineup table** (CLAUDE.md:149-154): add Fable 5/Mythos 5/Sonnet 5/Opus 4.8 rows.
12. **Context-window "1M beta"** (wiki/orchestration-patterns.md:43): 1M is now default.
13. **Consider migrating** `.claude/commands/*.md` → `.claude/skills/<name>/SKILL.md` (optional; models current D3 practice).

### (c) Reframe — unverifiable claims to label or replace

14. **Anti-pattern #8** (CLAUDE.md:165 + module 04/03 + tests): drop invented `~40%`; reframe "5 tools" as heuristic superseded by Tool Search / Programmatic Tool Calling.
15. **Citations "~15% better recall"** (CLAUDE.md:128, module 06, README:54, test): remove number or label unsourced; delete the test substring assertion.
16. **Long-context multiplier** (CLAUDE.md:147): remove / mark legacy-unverified.
17. **"60 MCQ"** (README:5, /quiz-me): "60 multiple-choice and multiple-response items"; teach multi-select.
18. **"nearly half the exam questions"** (README:80): soften to domain-weight framing.
19. **"CCA-F" vs "CCAR-F"** (README:5): add a one-line footnote.

### (d) Additions — beyond-exam track

20. Add a **"Current best practice (beyond the July-2026 blueprint)"** appendix to CLAUDE.md / the wiki index covering the Track-2 items: Tool Search + Programmatic Tool Calling, `refusal`/fallbacks, current model lineup, Agent SDK vs. Managed Agents, Skills-over-commands, context engineering as a discipline, MCP governance move.
21. Add confirmed-but-missing **exam logistics** to README/study guide: 4-of-6 scenarios, retake windows, 12-mo validity, the out-of-scope list.

---

## Confidence notes

- **Exam blueprint (domains, weights, format, scenarios, logistics): high confidence.** The auditor fetched the actual exam guide PDF via an official Skilljar redirect chain. Weights and format are quoted verbatim.
- **The escalation-trigger taxonomy and the "5 orchestration patterns" enumeration: thin.** The *concepts* are confirmed present in the guide's objectives (parsing-NL-for-termination, arbitrary-caps, sentiment/confidence escalation all appear near-verbatim), but the specific 3-valid/2-invalid list and the pattern names were not found quoted on any official page. Treat the framing as sound pedagogy anchored in real objectives, not as officially enumerated lists. Do not claim the exam "tests these exact five patterns" as fact.
- **The "~15% recall," "~40% tool degradation," and "nearly half the questions" numbers: no official source exists.** These are the clearest cases of prep-lore hardening into "facts" — two of them are enforced by tests, which is the worst place for an unverifiable number to live.
- **Model/pricing facts: high confidence but time-sensitive.** All fetched live 2026-07-16 from `platform.claude.com`. The lineup moves fast (Fable 5/Sonnet 5 landed June 2026); any pricing table needs a "verified as of" date.
- **MCP spec RC (2026-07-28) details: explicitly below the ground-truth bar** — only source is `modelcontextprotocol.io`, now under the independent Agentic AI Foundation, not an Anthropic domain. Use as context only.
- **One conflict of note:** the exam guide is dated July 2026, but several Track-2 facts (Fable 5, Tool Search, Managed Agents) predate it and are absent from the blueprint's apparent scope. Whether the blueprint has been updated to include them is itself unverified (facts-beyond-exam Unverifiable list). So "beyond the exam" is a genuine hedge — some of it may quietly be *in* the current exam and the repo can't confirm either way.
