# A3 — Ship Your Own MCP Server

**Concept: "21 endpoints, 3 tools. The discipline is curation, not coverage."** Wrap Autobound's own Signal API as a FastMCP stdio server — but design the tools *backward from `/scout`'s workflow*, not forward from the API surface. (Count for yourself: the `ENDPOINTS` array in `explorer.html` has 21 objects across 7 `group:` values. The exact number isn't the point — the ratio is.)

> **House rule for this assignment (non-negotiable):** You type every line. Claude Code is a reviewer and explainer only — ask it *why*, never paste *what*. Every done-criterion below is built so copy-paste can't satisfy it: you either explain a decision in writing or a fresh session picks your tool from your description. If you paste the server in, the 5/5 validation is meaningless and you'll know it.

---

**Where this sits in the arc (A1 → A3, and who calls this server).** A1 scored ICP fit *inside* a hand-typed loop — `icp.md` + a static account body, forced through `submit_icp_score`. A3 doesn't re-teach scoring; it productizes the data access under it. Your `score_icp_fit` tool is that same judgment turned into a reusable contract — so in DESIGN.md, note how it differs from A1's in-loop scorer (A1 read a static markdown body; this pulls live signals from `companies/enrich`). And keep the caller in mind: a tool has no value alone — it is invoked *by loops*. `/scout` (Milestone 4) is your first caller; A1's overnight-scorer pattern and A5's orchestrator are the production ones. Write the descriptions for a non-deterministic agent reader, not a human.

## Why this matters

- **Interview:** This is your own company's API as a tools-as-contracts case study. "I wrapped 21 endpoints into 3 tools and can defend every cut" is a stronger story than any generic MCP demo — and you'll have measured token numbers to back it.
- **Exam — D2 (Tool Design, ~18%):** Directly hits the core D2 design principle — never wrap an API 1:1; design tools backward from the workflow (un-numbered in the anti-pattern list, but the root of `wiki/tool-design-and-mcp.md`) — and anti-pattern #6 (structured error fields). (Careful with numbering under pressure: anti-pattern #1 is *parsing natural language for loop termination*, a D1 trap — not a tool-design rule.) It also lets you *demonstrate* the correct reading of anti-pattern #8: the anti-pattern is **treating "5 tools max" as a hard cap** — "≤5" was a useful pre-Nov-2025 heuristic, now superseded by Tool Search Tool + Programmatic Tool Calling. You cut 21 endpoints to 3 because that's what `/scout`'s workflow needs, *not* to hit a magic number; be ready to say exactly that. The "smart-but-lazy 12-year-old" description test is exam-canonical.
- **Exam — D5 (Context Management, ~15%):** A tool that dumps a raw enrich envelope vs. one that distills + truncates under a token budget is the whole context-economy argument, made concrete and measured.

---

## Prerequisites (~40 min)

1. `wiki/tool-design-and-mcp.md` — the whole page (~15 min). Non-negotiable: the "backward from workflow" thread and the tool-count framing — specifically *why* the old ≤5 hard cap is a superseded heuristic (anti-pattern #8), not a law, and why curation-to-workflow is the real discipline.
2. `wiki/context-engineering.md` — "Numbers & rules of thumb" + take #1 (~10 min). You need the token-budget framing for Milestone 5.
3. Skim two reference files (~15 min), don't study them:
   - `shared/mcp-servers/fintech-mock/server.py` — the FastMCP *scaffold* you'll copy: `@mcp.tool()` async funcs returning `json.dumps`, the `_error(...)` helper, docstrings-as-descriptions (note the prerequisite-gate language "MUST be called before..."). **Caveat — it models the scaffold, not the hard part of M2:** every fintech-mock tool is a pure in-memory dict lookup with *zero* outbound HTTP (grep it — no `httpx`/`requests`/`urllib`). Your tools make a real authenticated call to `signals.autobound.ai`, parse a nested JSON envelope, and map HTTP failures (timeout / 4xx / 5xx) into the error contract. Copy the shape from here; you'll write the network + error-mapping layer yourself (see M2).
   - `~/dev/Autobound/autobound-explorer/explorer.html` — the `ENDPOINTS` array (line 156). This is your raw material: 21 endpoints across 7 groups (`grep -oE "id: '[a-z-]+'" explorer.html | wc -l` → 21; `grep -oE "group: '[^']+'" explorer.html | sort -u` → 7), base `https://signals.autobound.ai/v1`, auth header `X-API-KEY`.

---

## The build (~4–5 hrs)

> **Time honesty.** The five milestone estimates sum to ~250 min (~4.2 hrs) of *clean* work. Two frictions this spec can't estimate for you eat the rest of the band: (a) the first live-API debugging pass against `companies/enrich`'s actual field shapes — not documented in this spec, you reverse-engineer them from `explorer.html` or a live call — and (b) spinning up and validating a genuinely context-clean fresh session for Milestone 5. Budget **60–90 min** of slack for those two combined (a first live reverse-engineering pass rarely fits in 20 minutes, and the 5/5 test is *expected* to force at least one description fix + a brand-new fresh session) — which puts the realistic total at the top of, or slightly past, the brief's 3–5 focused-hour band. This is the one assignment the brief deliberately scopes across three days (A3 = "Days 5–7"), so if the fresh-session validation slips, split it across two sittings — but keep each sitting inside the focused-hours ceiling rather than letting one marathon run over. If you're hand-typing every line with no copy-paste (you are — see the house rule), plan for the top of the range, not the bottom.

**Grounding reality — read before you start.** There is *no* existing signal infrastructure to wire into. `.mcp.json` does not exist anywhere in `sales-machine`. `.claude/skills/scout/` exists but is **empty** — no `SKILL.md`. "685 signals" is marketing copy from `CLAUDE.md`; the live API self-reports **~32–33 signal types** (`/signals/types` says 32 canonical slugs, `/stats` says 33). Use "32–33 signal types" as your technical unit and never cite "685" as an API fact. You are building from zero. That's the point.

Repo target: `~/dev/Autobound/sales-machine`. Server lives at `mcp/signal-server/server.py`.

### Milestone 1 — The curation decision (DESIGN.md) · ~45 min
The design doc is a first-class deliverable, authored **before** any server code. This milestone is a real design decision, not a defense of a given answer — so **derive your own cut first, then check it against the reference below.**

**Step 1 — derive (do this before reading the table).** Open the 21 endpoints in `explorer.html` and work *backward from `/scout`'s workflow*: for a domain, `/scout` needs to (a) decide if the company is worth pursuing, (b) see the few signals that matter, (c) find the one angle to open with. Write, in DESIGN.md, the **3 agent-shaped tools you'd cut** — name each, list which endpoint(s) it composes, and say in one line why it's shaped like a workflow step and not like an endpoint. Commit to your three before you scroll.

**Step 2 — reconcile.** Now compare against the recommended distillation. Where you differ, either defend your choice in writing *or* adopt the reference and note why it's better. Don't silently overwrite your reasoning — the diff *is* the learning.

Recommended distillation (a reference to check yourself against, not a spec to copy — adjust if you can defend it):

| Tool | Composes which endpoints | Why it's agent-shaped |
|---|---|---|
| `get_top_signals(domain, focus, max_signals=5)` | `POST /companies/enrich` (sole source for a domain-only tool) | Ranks + truncates raw envelopes to `{headline, type, date, evidence_url}` under a token budget |
| `score_icp_fit(domain)` | `POST /companies/enrich` + `GET /signals/types` | Returns a fit score + rationale against `playbook/icp.md` dimensions — one number the agent can branch on |
| `find_warm_angle(domain, persona)` | `GET /buyer-intent/topics` + `GET /buyer-intent/companies/{domain}/timeline` + enrich | Surfaces the single best outreach hook for a persona |

> **Why not `contacts/enrich` as a fallback for `get_top_signals`?** It doesn't type-check against a domain-only tool: `contacts/enrich` takes a `contact_email` body param (explorer.html:220–222), not a domain — there's no email to pass, and no bridging step is in scope. The real API doc recommends the *opposite* direction ("fall back to company enrich on the employer domain", explorer.html:219). So `companies/enrich` is the source, full stop; contact-level enrichment is a different tool with a different input, deliberately not built here.

DESIGN.md must also record the **deliberate exclusions** and why: `monitoring/add` (10cr/record write, all-or-nothing — not a read tool), `buyer-intent/contacts/export` (the endpoint id is `intent-export`; async 202, 50cr+ upfront, poll loop — wrong shape for an interactive agent), `contacts/enrich` (needs a `contact_email`, not a domain — wrong input shape for a domain-keyed workflow), content-gen v3.6 (separate host, enterprise-only, CORS-blocked, not signal data — out of scope). Note the **credit model**: these calls cost real money (2cr/signal on enrich, 1cr/contact on intent); zero-result calls are free; design so a tool never fans out an unbounded paid search.

**Deliverable:** `mcp/signal-server/DESIGN.md` — your derived cut + reconciliation note, the final 3-tool table, the exclusion list, the credit note.
**Explain-back (write it in DESIGN.md):** *"An engineer says 'just expose all 21 endpoints, the model can figure it out.' Give the two-sentence rebuttal you'd say out loud, citing what specifically degrades."*

### Milestone 2 — The server, error contract, token budget · ~75 min
Build `server.py`: `FastMCP("autobound-signals")`, three `@mcp.tool()` async funcs, `mcp.run(transport="stdio")` in `__main__`. Auth: read `os.environ["AUTOBOUND_API_KEY"]`, send header `X-API-KEY: <key>` (NOT Bearer — confirmed at explorer.html:465). Copy the `_error(...)` helper. Unlike fintech-mock, your tools actually leave the process: use **`httpx`** for the live call (its `AsyncClient` is the natural fit for async tool funcs). You do **not** add a dependency for it — `httpx` ships transitively with `mcp[cli]` (confirmed: `mcp[cli]>=1.0.0` pulls `httpx` into the env), so `import httpx` just works. Budget real time for the first live call: you'll reverse-engineer `companies/enrich`'s response shape (it's not documented here) and decide how timeouts and 4xx/5xx map onto your error fields — that's the novel work, not the FastMCP boilerplate.

Two decisions you must make and write down, not guess:
- **Error field name.** Anti-pattern #6 (exam form) wants `errorCategory`; fintech-mock ships `code`. Pick one, use it consistently, and justify in a one-line comment. (Recommendation: `errorCategory` to match the exam, but own the call.) You already built this contract once — `lint-draft.py` in A2 emits `isError`/`errorCategory`/`isRetryable` for a *hook*; here you emit the same shape for an *MCP tool*. Same anti-pattern #6 fix, different surface: keep the field names identical across both so A4's eval harness can consume either without a shim.
- **Token budget per response.** Each tool caps its output (e.g. `max_signals=5`, truncate evidence text). When you truncate, the response must *say so* and steer — `"note": "5 of 23 signals shown; narrow with focus=..."` — never cut silently (anti-pattern #7). **Deliberate swap from the brief:** the brief lists "pagination" as the response-control mechanism; this spec substitutes **truncation-with-steering-note** on purpose. Pagination hands the agent a cursor and invites it to loop and re-fetch — burning the enrich credits the spec warns about — whereas a hard budget plus a steering note gives the agent one economical response and a *narrowing* lever (`focus=`) instead of a *paging* lever. If you'd rather implement real pagination, that's a defensible variant — just document why in DESIGN.md.

`pyproject.toml`: one *declared* runtime dep — `mcp[cli]>=1.0.0` — plus `requires-python>=3.12`. You get `httpx` for free through it (transitive), so you don't declare it separately and the "one dep" story holds; just `import httpx` in `server.py`. (The fintech-mock `pyproject.toml` also lists a standalone `fastmcp>=0.1.0`, but its `server.py` imports `from mcp.server.fastmcp import FastMCP` — the FastMCP that ships *inside* the `mcp` package, not the separate PyPI `fastmcp`. That extra dep is dead weight; don't copy it. Import FastMCP from `mcp.server.fastmcp`.)

**Deliverable:** `server.py` that starts under stdio and returns a structured error on a bad domain.
**Explain-back:** *"Show the exact JSON your `get_top_signals` returns when the API yields 23 signals but your budget is 5. Point to the field that keeps the agent from thinking it saw everything."*

### Milestone 3 — Descriptions as onboarding docs + `.mcp.json` · ~45 min
Rewrite each tool's docstring as documentation for a new engineer: what it's for, when to reach for it vs. the other two, what each param means, what comes back. Bake in prerequisite/steering language the way fintech-mock does. These descriptions are the *only* thing the Milestone 5 fresh session gets — treat them as the product.

Then **create** `sales-machine/.mcp.json` from scratch (it does not exist) wiring the stdio server:
```json
{ "mcpServers": { "autobound-signals": {
  "command": "uv", "args": ["--directory", "mcp/signal-server", "run", "server.py"],
  "env": { "AUTOBOUND_API_KEY": "${AUTOBOUND_API_KEY}" } } } }
```

**Deliverable:** three onboarding-grade docstrings + `.mcp.json`.
**Explain-back:** *"Paste your three tool descriptions. For each, name the one word/phrase that disambiguates it from the other two so the model never confuses them."*

### Milestone 4 — Author the `/scout` skill · ~40 min
`.claude/skills/scout/` is an empty stub. Write its `SKILL.md` (pattern-match the existing `daily-brief`, `coach`, `post-call` skills that already have one). `/scout <domain>` should: call `score_icp_fit`, and if the fit clears a bar, call `get_top_signals` + `find_warm_angle`, then hand back a scouting brief. The skill uses the tools — it does not re-implement API calls.

**Deliverable:** `.claude/skills/scout/SKILL.md`.
**Explain-back:** *"Why does `/scout` gate `get_top_signals` behind `score_icp_fit` instead of always calling both? Frame it in credit + token terms."*

### Milestone 5 — The smart-but-lazy test + measure the win · ~45 min
Two verifications:
1. **5/5 tool selection.** In a *fresh* Claude session (clean context — this is the whole point), give only the three tool descriptions and 5 realistic `/scout`-style prompts. The model must pick the right tool 5/5 from descriptions alone. Any miss = the description is wrong; fix the description, not the prompt. Save the transcript.
2. **Token economy, measured.** Compare context cost of your distilled `get_top_signals` response vs. dumping the raw `/companies/enrich` envelope for the same domain. Record both token counts and the ratio. **Measurement method (pick one and state it in VALIDATION.md so the number is comparable):** if you already have an Anthropic Console API key, `client.messages.count_tokens` is the source of truth — it counts exactly what a real request bills. If you don't (Claude Code subscription access doesn't include one), **do not burn setup time acquiring one for this** — `chars/4` or `tiktoken` applied identically to both rows is a perfectly citable approximation, labeled as such (the *ratio* is robust to the method; the absolute counts aren't). Don't mix methods across the two rows, and don't quote a ratio without naming how you got it. Keep the smoke test on **free** endpoints (`/account`, `/signals/types`, `/buyer-intent/companies/{domain}/timeline`) to avoid burning credits during iteration.

**Deliverable:** `mcp/signal-server/VALIDATION.md` — the 5/5 transcript + a two-row token table (raw vs. distilled) with the ratio and a one-line note stating the counting method used.
**Explain-back:** *"State your measured token ratio in one sentence you'd say in an interview. Then: what did a wrong tool-pick teach you about which description, and what exact word did you change?"*

---

## Done criteria (copy-paste-proof)

Each row names how to check it. Six are terminal commands; two (marked **manual**) are judgment calls you self-grade against a stated bar — that's inherent to "written in your own words" and "a human picked the right tool," not a gap.

**Machine-checkable (run from `sales-machine/`):**

- [ ] Server boots under stdio: `uv --directory mcp/signal-server run server.py` starts without error (Ctrl-C to exit; a clean stdio handshake with no traceback = pass).
- [ ] Exactly **3** tools: `grep -c "@mcp.tool" mcp/signal-server/server.py` → `3`. Not 4, not 21.
- [ ] `.mcp.json` exists and wires the server: `test -f .mcp.json && grep -q autobound-signals .mcp.json && echo OK`.
- [ ] Skill exists and invokes tools by name: `grep -Eq 'get_top_signals|score_icp_fit|find_warm_angle' .claude/skills/scout/SKILL.md && echo OK`.
- [ ] **Bad domain returns a structured error** — drive the stdio server through a real client call (stdio has no curl equivalent, so use the provided harness):
  ```bash
  # scripts/probe.py — a ~15-line client that opens the stdio server and calls one tool.
  # Use the MCP Python SDK's stdio_client + ClientSession (see the SDK quickstart);
  # call get_top_signals(domain="not-a-real-domain-xyz.invalid") and print the result.
  uv run python scripts/probe.py | python -c "import sys,json; d=json.load(sys.stdin); assert d['isError'] and 'isRetryable' in d and ('errorCategory' in d or 'code' in d); print('OK')"
  ```
  Writing `probe.py` yourself is part of the exercise — it's also your Milestone-5 measurement harness. Pass = the assert prints `OK`. **Heads-up — the bogus domain may not error:** this API's documented pattern for unknown domains is a graceful empty 200 (`explorer.html:254`: the timeline endpoint returns "an empty timeline, not a 404", and zero-result calls are free), and nothing documents `companies/enrich` behaving differently. If `not-a-real-domain-xyz.invalid` comes back as a benign empty result, that's the API working as designed — your tool should surface it as a truthful empty (anti-pattern #7: never dress an empty up as success *or* as an error). To exercise the *error* path deterministically, trigger a failure you control instead: run the probe with `AUTOBOUND_API_KEY` unset (auth failure → your 401 mapping) or point the client at a wrong port (timeout mapping). Either satisfies this criterion; note which you used.
- [ ] **Truncation announces itself** — same harness against a domain with many signals: the JSON contains a `note`/steering field naming the shown-vs-total count (`... | python -c "import sys,json; assert 'note' in json.load(sys.stdin); print('OK')"`).

**Manual (self-graded against a stated bar):**

- [ ] DESIGN.md, VALIDATION.md, and all four explain-back answers are written in your own words. **Bar:** each explain-back cites a *specific* endpoint, field, credit cost, or token number — not a generic principle. (These are the copy-paste-proof core — a pasted server can't produce a reasoned exclusion list or a token ratio you measured.)
- [ ] VALIDATION.md shows **5/5** fresh-session tool selection (saved transcript, 5 prompts, right tool each time) and a raw-vs-distilled token table with the counting method named. **Bar:** any miss is fixed by editing the *description*, and the fix is recorded.

---

## Stretch (optional)

- **Namespacing / progressive-disclosure spike:** add a 4th (then a 5th) read tool and measure whether selection reliability drops. The point is *not* to confirm a magic number — "≤5" is a superseded pre-Nov-2025 heuristic (anti-pattern #8), and Tool Search + Programmatic Tool Calling exist precisely to scale past it. The point is empirical: find the workflow-specific point where adding a tool stops paying for its context, and document that delta. That's the architecture-choice framing the exam rewards.
- **Cassette the paid calls:** record one real `/companies/enrich` response to a fixture and let the server replay it offline, so the eval loop costs zero credits. Note what this buys you vs. hitting live.

---

## Interview takes to earn

Add these to `assignments/interview-takes.md` once the explain-backs are written:

1. **"I never wrap an API 1:1 — I design tools backward from the workflow."** I turned 21 Autobound endpoints into 3 agent-shaped tools and can name exactly what each exclusion (async export, write-side monitoring, enterprise content-gen) would have cost the model in tokens and credits.
2. **"A tool is a contract with a non-deterministic reader, so descriptions are the product."** A fresh session picked my tool 5/5 from the docstrings alone — and the one miss I fixed was a description bug, not a prompt bug.
3. **"Context economy is measurable, and I measured mine."** My distilled `get_top_signals` costs [X]× fewer tokens than dumping the raw enrich envelope — with a truncation note that keeps the agent from thinking it saw everything.
