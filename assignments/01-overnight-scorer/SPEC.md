# A1 — The Overnight Scorer

**Concept: "My pipeline gets scored while I sleep — and I can explain every line of the loop."** A raw-API Python script (no Claude Code harness, no MCP) that reads `wiki/accounts/*.md` + `playbook/icp.md`, runs a hand-typed agentic loop to score each account for ICP fit, forces the final score through a structured tool, writes it back to frontmatter, then re-runs the whole job through the Batch API to feel the economics.

**Meta-rule (non-negotiable):** You type every line. Claude Code is a reviewer and explainer only — ask it *why*, never paste from it. The done-criteria below are built so copy-paste can't satisfy them: they require written explain-backs and deliberate-choice notes in your own words.

**Substrate:** `~/dev/Autobound/sales-machine` (real repo). Deliverables land there, not in a toy.

---

## Why this matters

- **Interview payoff (D1, ~27% of exam):** Loop termination by *contract*, not vibes. You'll be able to say "I wrote correct, contract-derived handling for `refusal` and `pause_turn` — and I can tell you exactly when each fires, why my client-tool-only loop never trips them on the happy path, and what breaks if you drop the branch" and "I chose Batch for the overnight run because 50% off on a no-SLA job is free money." These are experience claims — the honest kind: what you *built and understand*, not a claim you watched a safety refusal fire on a benign B2B prompt.
- **Exam anti-patterns you'll internalize by building against them:** #1 (parsing natural language for loop termination), #2 (arbitrary iteration caps as the *primary* stop), and the forced-`tool_choice` structured-output pattern.
- **The Travis-Bryant overnight-scoring pattern at personal scale** — a cron/event-triggered agent that refreshes context and does bounded work unattended. "Loops are the future" (Cherny); this is your first one, typed by hand.

---

## Prerequisites (≤45 min total)

> **Path convention for this spec:** every repo path is written relative to the substrate root `~/dev/Autobound/`, so `sales-machine/...` is the prefix throughout. Note there are **two** unrelated `wiki/` trees on this machine — `cca-prep/wiki/` (orchestration notes, no `accounts/`) and `sales-machine/wiki/` (the account bodies you score). When a path says `sales-machine/wiki/accounts/…`, it is the latter; do not go looking under `cca-prep/wiki/`.

- `cca-prep/wiki/orchestration-patterns.md` → "Always-on / scheduled (the loop)" + "Numbers & rules of thumb" (10 min).
- CCA-F reference card (`cca-prep/CLAUDE.md`): the **stop_reason** table, **tool_choice** table, **Batch API** block, and anti-patterns #1/#2 (10 min).
- Skim the real inputs you'll score against (15 min): `sales-machine/playbook/icp.md` (the 7-attribute weighted rubric + disqualifier gate + band thresholds — you are *applying* this, not inventing it) and two account bodies (`sales-machine/wiki/accounts/orum.md`, `sales-machine/wiki/accounts/qualified.md`) so you know the shape of the text Claude will read.
- Anthropic Messages API + Batch API docs — just the request/response shapes for `stop_reason`, `tool_choice`, and `/v1/messages/batches` (10 min).

---

## The build (4 milestones, ~4.25 hr focused work)

> **Time budget, honestly.** The per-milestone minutes below are *focused-typing* estimates and assume the happy path. They sum to ~4.25 hr of build + ≤45 min of prereqs — which is the **top** of the brief's 3–5 hr band with zero slack. This assignment is scoped across **Days 1–2** precisely so a real API error, a schema typo, or a frontmatter round-trip bug has somewhere to go without blowing the ceiling. If M2 or M3 runs long, bank the milestone at its last green checkpoint and resume next session — do **not** rush the explain-backs to hit a clock. Expect debugging; it is not overrun, it is the work.

### M1 — Close the substrate gaps + decide the write contract (~30 min)
The repo isn't ready for this job; fix that first, deliberately.
- **Gap 1 — no key.** `sales-machine/.env.example` and `.env` contain only `AUTOBOUND_API_KEY` and `CRUNCHBASE_USER_KEY`. This job needs `ANTHROPIC_API_KEY`. Add `ANTHROPIC_API_KEY=` to `.env.example` (committed, blank) and confirm your real key is available to the shell. Do **not** hardcode it — read from env.
- **Gap 2 — no score field.** No account frontmatter has any score key (grepped: zero hits). You are adding a new convention. Define and document three keys: `icp_score` (float, 0–100), `icp_tier` (`tier-1`/`tier-2`/`nurture`/`out`, matching `icp.md` bands), `icp_scored_at` (ISO date). Follow the one Python convention in the repo (`scripts/build-index.py`: stdlib, plain functions, no classes, docstring banner) — the only new third-party dep is `anthropic`.
- **Gap 3 — no packaging convention.** `sales-machine` has no `requirements.txt`, no `pyproject.toml`, no venv; both existing scripts (`build-index.py`, `lint-draft.py`) are pure-stdlib by design, and the system `python3` is 3.9.6. `anthropic` is your first third-party dep here, so you must make one deliberate isolation choice — don't `pip install` into system Python. Simplest zero-config path (uv is already on this machine): run the script with `uv run --with anthropic scripts/score-icp.py`, which pulls a modern Python + the SDK into an ephemeral env and leaves the repo's stdlib-only convention untouched. If you'd rather make it durable, create a `.venv` and add a one-line `requirements.txt` (`anthropic`) — but then say *why* in the docstring, because you're introducing a packaging convention the repo didn't have. Either way this is a decision to name, not a step to skip; budget a few minutes for it inside M1.
- **Deliverable:** `.env.example` updated; the isolation choice made (an `uv run` invocation you can reproduce, or a committed `requirements.txt`); a 4-line comment block at the top of your new `scripts/score-icp.py` naming the three frontmatter keys and their types.
- **Explain-back (write it in the docstring):** Why write the score to frontmatter *in Python after the loop returns*, rather than giving Claude a file-edit tool and asking it to update the page itself? (Hint: guarantee vs. preference — what must be deterministic here?)

### M2 — The loop, every stop_reason handled (~90 min)
The teaching core. Score **one** account (start with `orum.md`) end-to-end.
- Build a raw Messages API agentic loop: `while stop_reason == "tool_use":` execute the requested tool, append the `tool_result` (matching `tool_use_id`), re-call. Give the model exactly one read tool if it needs one (e.g. `get_icp_rubric` returning `icp.md`) — or just prepend both files to the prompt and let the loop exist for the *final scoring tool* in M3. Either is fine; the loop must be real.
- Handle **every** `stop_reason` with an explicit branch: `tool_use` (act), `end_turn` (done), `pause_turn` (resend the request as-is to continue — do not treat as terminal), `refusal` (stop, log, mark account `needs_review` — it's an HTTP 200, not an exception), `max_tokens` and `model_context_window_exceeded` (stop, log, don't silently truncate). No `else: break` that swallows unknowns.
- **Which branches you'll actually exercise vs. code defensively — be honest about this.** In *this* build the model has only client-side tools (one read tool, or none) and no server tools (`web_search`/`code_execution`/computer use), so `pause_turn` is structurally unreachable — it fires on long-running *server-tool* turns, which this job never issues. And `refusal` fires from the safety classifier on genuinely problematic content; benign B2B ICP-scoring prompts are extremely unlikely to trip it. You will most likely only ever *observe* `tool_use`, `end_turn`, and (if you undersize the budget) `max_tokens`. That is exactly why the other branches matter: you write them **from the API contract**, correct-by-construction, so the loop is total over the stop_reason enum rather than lucky. Do not pretend you watched `pause_turn` fire — claim what's true: you coded the branch the spec guarantees is correct, and you can say *when* it would fire and *why* falling through would be wrong.
- `max_iterations` exists as a **safety net only** — hitting it is an error path you log, never your normal termination. Normal termination is `end_turn`/the final tool. (Anti-patterns #1 and #2.)
- **Deliverable:** `score-icp.py` scores one account and prints the raw score object; a `STOP_REASONS.md` table you wrote — one row per stop_reason, "what my code does / why," with a column marking each as **observed in this run** or **coded defensively (contract-derived)** so the table stays honest about what you exercised.
- **Explain-back:** For `pause_turn` and `refusal` specifically — from the API contract, *when* does each fire, why is neither reachable-on-the-happy-path in a client-tool-only job like this one, and what would break if you let each fall through to a default `break` (e.g., `pause_turn` → you'd drop a turn the API expects you to resume; `refusal` → you'd treat an HTTP-200 safety stop as a normal finish and write a garbage score)? Why is `max_iterations` *not* your loop's termination logic?

### M3 — Force the structured score (~60 min)
- Define a `submit_icp_score` tool whose input schema is the score object: `score` (number), `tier` (enum), `per_attribute` (the 7 `icp.md` attributes each with points), `disqualifier_hit` (bool + reason), `rationale` (string). Set `tool_choice` to `{"type": "tool", "name": "submit_icp_score"}` so the model *must* emit it — you parse structured JSON, never prose.
- Note in a comment: forced `tool_choice` (`any`/`tool`) is **incompatible with extended thinking** — so this final call runs without thinking, by design.
- Apply the `icp.md` disqualifier gate: if `disqualifier_hit`, score floors to 0 → `out`, regardless of points. Map bands: 80–100 `tier-1`, 60–79 `tier-2`, 40–59 `nurture`, <40 `out`.
- Write the result back to that account's frontmatter (the three M1 keys), preserving all existing keys and body.
- **Deliverable:** `orum.md` frontmatter now carries `icp_score`/`icp_tier`/`icp_scored_at`; the script's write function is idempotent (re-running overwrites cleanly, doesn't duplicate keys).
- **Explain-back:** Why forced `tool_choice: tool` instead of asking for JSON in the prompt and parsing the text? What does the schema *guarantee* that a prompt can only *request*? Sanity-check: is Orum's written score near the rubric's worked example (82.5 → tier-1)? If not, why?

### M4 — Same job, Batch API, feel the economics (~75 min)
- Submit all 9 real accounts as one Batch API job (`/v1/messages/batches`): 9 requests, each the same forced-scoring call. You are within limits by orders of magnitude (max 100,000 requests **or** 256 MB, whichever first).
- Poll for completion; the window is **24 hours, best-effort, no SLA** (most finish within the hour). Pull results as `.jsonl` (retrievable for 29 days), parse each, write all 9 back to frontmatter.
- Compute the economics: tokens × standard rate for the sync path vs. the **50% batch discount**, from your actual token counts. Note in writing what Batch does **not** support (`stream:true`, thread/`store` continuation, cache hints, `max_tokens:0`, Fast mode) — and confirm nothing your job needs is on that list.
- **Deliverable:** all 9 accounts scored in frontmatter; the batch `.jsonl` saved; a `BATCH_NOTES.md` with your real before/after cost numbers and the "what's unsupported" check.
- **Explain-back:** When is the 24h no-SLA window the *right* trade and when is it disqualifying? For an overnight scorer specifically, why is Batch the correct call and not just cheaper?

---

## Done criteria (copy-paste-proof)

1. `git diff` in `sales-machine` shows: `.env.example` gained `ANTHROPIC_API_KEY=`; `scripts/score-icp.py` exists (stdlib + `anthropic`, no hardcoded key); all **9** real account files gained `icp_score`/`icp_tier`/`icp_scored_at`, existing frontmatter and body intact.
2. `STOP_REASONS.md` exists with a row for **every** value in the reference-card table (`end_turn`, `max_tokens`, `stop_sequence`, `tool_use`, `pause_turn`, `refusal`, `model_context_window_exceeded`) — each with your code's behavior in your words **and** an observed-vs-coded-defensively marker. A grep of your loop confirms an explicit branch for `pause_turn` and `refusal` (not a bare `else`). Note the grep proves the branch *exists and is correct-by-construction*, not that it was *exercised* — `pause_turn`/`refusal` are unreachable on this build's happy path, and the honesty of the table (not the grep) is what carries the claim.
3. The final scoring call uses `tool_choice` of type `tool` (visible in source), and the script parses the tool input as JSON — there is **no** regex/string-parsing of model prose anywhere for the score.
4. `max_iterations` appears only in an error/safety branch — not as the `while` condition and not as the thing that returns a normal result.
5. `BATCH_NOTES.md` contains your *own* cost numbers (not the generic "50%" line alone) and the unsupported-features check, and the batch `.jsonl` is saved.
6. You can, out loud and unaided, walk any line of `score-icp.py` and say why it's there. (If you can only say "Claude wrote it," it fails.) **This is the one criterion no command or artifact can verify — deliberately.** It's a self/oral report, and that's the anti-copy-paste point of the whole assignment: the other five are machine-checkable, this one is the human check that the code is yours. Treat it as pass/fail on your own honesty, not as something the repo can attest.

---

## Stretch (optional)

- **Diff-aware re-scoring:** skip accounts whose body hasn't changed since `icp_scored_at` (compare git mtime / content hash) so the overnight run only re-scores what moved — the real loop pattern.
- **Wire it to a schedule:** a `.workflow`/cron stub or a note on how you'd trigger this nightly and where the run log would go (don't build the whole harness — just make the "overnight" real in one concrete mechanism).

---

## Interview takes to earn

Write these into `assignments/interview-takes.md` when done — as things you *did*, not read:

- **"Loop termination is a contract, not a vibe."** I terminate on `stop_reason`, with a handled branch for every value including `pause_turn` and `refusal` — and I'm precise about which I exercised (`tool_use`/`end_turn`, and `max_tokens` when I undersized the budget) versus which I coded correct-by-construction from the API contract because a client-tool-only job can't reach them (`pause_turn` needs a server-tool turn; `refusal` needs the safety classifier to trip, which benign B2B prompts don't). `max_iterations` is a safety net I log, never my control flow. I built deliberately past the two anti-patterns I *can* provoke — parsing prose to stop, and capping iterations as primary control.
- **"Structured output is a guarantee, prompts are a request."** I force the final score through a `tool_choice: tool` schema so the shape is guaranteed — and I know that buys me determinism at the cost of extended thinking on that call.
- **"Batch economics from experience."** I ran the same 9-account job sync and batched, and I can quote my real numbers: 50% off, 24h no-SLA window, which for an overnight scorer is free money — and I know exactly which Batch limitations would have disqualified it if my job had needed streaming or cache hints.
