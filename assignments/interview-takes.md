# Interview Takes

Positions I can now argue **from experience, not reading**. One `##` section per assignment; each "take to earn" starts unchecked. Check a box **only** when you've built the thing and can defend the claim unaided — then add a dated entry from the template below in your own words. A take you can't demo or explain out loud isn't earned yet, no matter what the repo shows.

## Entry template (copy one per take as you earn it)

```
### YYYY-MM-DD — "<the claim>"
- **What I built:** <the artifact / demo, one line>
- **The claim I can now defend:** <in my own words, not the spec's>
- **The number or demo I'd cite in the room:** <a real figure, transcript, or moment>
- **The follow-up I'd get and my answer:** <the interviewer's likely probe>
```

---

## A1 — The Overnight Scorer

- [ ] **"Loop termination is a contract, not a vibe."** I terminate on `stop_reason` with a handled branch for every value — and I'm precise about which I exercised (`tool_use`/`end_turn`, `max_tokens` when I undersized the budget) versus which I coded correct-by-construction (`pause_turn` needs a server-tool turn; `refusal` needs the safety classifier). `max_iterations` is a safety net I log, never my control flow.
- [ ] **"Structured output is a guarantee, prompts are a request."** I force the final score through a `tool_choice: tool` schema so the shape is guaranteed — and I know that buys determinism at the cost of extended thinking on that call.
- [ ] **"Batch economics from experience."** I ran the same 9-account job sync and batched and can quote my real numbers: 50% off, 24h no-SLA window, free money for an overnight scorer — and I know which Batch limitations would have disqualified it if my job had needed streaming or cache hints.

## A2 — Make the Rules Real

- [ ] **"I moved my own rules from prompt to code, and I can show you the hook winning a prompt-injection."** Guarantee vs. preference argued from a system I built — CLAUDE.md rule 1 and 2 went from advisory prose to a PreToolUse gate that blocks the write and denies the send.
- [ ] **"PostToolUse can't block — and knowing which event can is the whole game."** I caught a spec that said 'PostToolUse blocks failures,' proved it can only report after the fact, and moved the guarantee to PreToolUse where deny actually means deny.
- [ ] **"The linter has two contracts on purpose: an exit code the hook obeys and a JSON error object humans and evals read."** Exit-code gating vs. structured `isError`/`errorCategory`/`isRetryable` payloads are different jobs; conflating them is anti-pattern #6.

## A3 — Ship Your Own MCP Server

- [ ] **"I never wrap an API 1:1 — I design tools backward from the workflow."** I turned 21 Autobound endpoints into 3 agent-shaped tools and can name exactly what each exclusion (async export, write-side monitoring, enterprise content-gen) would have cost the model in tokens and credits.
- [ ] **"A tool is a contract with a non-deterministic reader, so descriptions are the product."** A fresh session picked my tool 5/5 from the docstrings alone — and the one miss I fixed was a description bug, not a prompt bug.
- [ ] **"Context economy is measurable, and I measured mine."** My distilled `get_top_signals` costs [X]× fewer tokens than dumping the raw enrich envelope — with a truncation note that keeps the agent from thinking it saw everything.

## A4 — The Harness

- [ ] **"I grade outcomes, not paths — and for cold outreach I had to define what the outcome even is."** I judge voice-match, SMYKM personalization, and structure as the gradeable end-state, because reply-rate is too sparse and laggy to grade a single draft on.
- [ ] **"My judges are calibrated against my own accept/reject decisions to ≥80% per dimension."** I tuned rubric wording (never the labels) by reading disagreement transcripts — and kept an 'Unknown' hatch because a judge forced to guess is as useless as a self-reported confidence score.
- [ ] **"I chose pass^k for a customer-facing agent, deliberately, and reported per-dimension."** 75% single-trial is ~42% over three consecutive drafts — a lone aggregate number (AP #10) would have hidden exactly the instability that matters, so I picked the metric to the product and swapped models on evidence.

## A5 — The Machine

- [ ] **"I paid the multi-agent tax and can tell you when it's worth it."** I ran orchestrator-workers over my own pipeline, read the ledger, and can point to the one stage whose loose-coupling justified the ~15x overhead — and say plainly which stages a single agent would've done cheaper.
- [ ] **"My orchestrator decides about errors; it doesn't swallow them."** Workers return `isError`/`errorCategory`/`isRetryable`; the coordinator retries transient, skips-and-logs hard content failures, and aborts on a SAFETY breach — a skipped account is always a visible line, never an empty-list 'success' (anti-pattern #7).
- [ ] **"Kill it mid-run and it resumes without repeating work."** File-based checkpointing after every worker, a token budget as the primary stop (iteration cap only a safety net), and a clean budget-halt that loses nothing — long-horizon reliability as engineering, not prompting.

---

## Earned entries

_Add dated entries here (or under each take) as you check boxes off. Newest first._
