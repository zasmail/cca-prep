# Fact Sheet: Claude Model Lineup & Economics — Audit

**Compiled:** 2026-07-16
**Source rule:** Only official Anthropic properties (anthropic.com, claude.com, docs.claude.com/platform.claude.com, code.claude.com, console.anthropic.com, anthropic.skilljar.com). All facts below were fetched live via WebFetch on 2026-07-16 unless noted. `docs.claude.com` and `docs.anthropic.com` both 302-redirect to `platform.claude.com` — treated as the same official source (Anthropic-controlled redirect, not a third party).

**Note on methodology:** This audit was requested inside a session that had a third-party/cached "claude-api" skill loaded into context, containing extensive claims about the same models. That skill's cached content is **not** an official source and was **not** used as evidence here — every fact below was independently re-fetched from the live docs. Where the skill's cached claims happened to match, that's coincidental corroboration, not the basis for the fact.

---

## Current Model Lineup (Active)

| Claim | Model ID | Context Window | Max Output | Source | Confidence |
|---|---|---|---|---|---|
| Claude Fable 5 — API ID | `claude-fable-5` | 1M tokens | 128K tokens | platform.claude.com/docs/en/about-claude/models/overview | confirmed |
| Claude Opus 4.8 — API ID | `claude-opus-4-8` | 1M tokens | 128K tokens | platform.claude.com/docs/en/about-claude/models/overview | confirmed |
| Claude Sonnet 5 — API ID | `claude-sonnet-5` | 1M tokens | 128K tokens | platform.claude.com/docs/en/about-claude/models/overview | confirmed |
| Claude Haiku 4.5 — API ID | `claude-haiku-4-5-20251001` (alias `claude-haiku-4-5`) | 200K tokens | 64K tokens | platform.claude.com/docs/en/about-claude/models/overview | confirmed |
| Claude Mythos 5 — API ID (Project Glasswing only, limited availability) | `claude-mythos-5` | 1M tokens | 128K tokens | platform.claude.com/docs/en/about-claude/models/overview | confirmed |

Quote: "Claude Fable 5 ... claude-fable-5 ... Claude Opus 4.8 ... claude-opus-4-8 ... Claude Sonnet 5 ... claude-sonnet-5 ... Claude Haiku 4.5 ... claude-haiku-4-5-20251001" (models overview comparison table).

Quote (Fable 5 / Mythos 5 specs): "Context window and output: a 1M token context window by default, and up to 128k output tokens per request. Pricing: $10 USD per million input tokens and $50 USD per million output tokens." — platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 — confirmed

## Legacy / Still-Active Models

| Claim | Model ID | Context | Max Output | Source | Confidence |
|---|---|---|---|---|---|
| Claude Opus 4.7 — dateless ID, still active | `claude-opus-4-7` | 1M | 128K | platform.claude.com models overview ("Legacy models" accordion) | confirmed |
| Claude Opus 4.6 — dateless ID, still active | `claude-opus-4-6` | 1M | 128K | same | confirmed |
| Claude Sonnet 4.6 — dateless ID, still active | `claude-sonnet-4-6` | 1M | 128K | same | confirmed |
| Claude Sonnet 4.5 — dated ID, still active | `claude-sonnet-4-5-20250929` (alias `claude-sonnet-4-5`) | 200K | 64K | same | confirmed |
| Claude Opus 4.5 — dated ID, still active | `claude-opus-4-5-20251101` (alias `claude-opus-4-5`) | 200K | 64K | same | confirmed |
| Claude Opus 4.1 — dated ID, **deprecated** | `claude-opus-4-1-20250805` (alias `claude-opus-4-1`) | 200K | 32K | same | confirmed |

Quote: "Claude Opus 4.1 (`claude-opus-4-1-20250805`) is deprecated and will be retired on August 5, 2026. Migrate to Claude Opus 4.8 before the retirement date." — platform.claude.com/docs/en/about-claude/models/overview — confirmed

---

## Pricing Per MTok (Standard API)

Source for all rows: platform.claude.com/docs/en/about-claude/pricing (Model pricing table) — confirmed, fetched live.

| Model | Base Input | 5m Cache Write | 1h Cache Write | Cache Read | Output |
|---|---|---|---|---|---|
| Claude Fable 5 | $10/MTok | $12.50/MTok | $20/MTok | $1/MTok | $50/MTok |
| Claude Mythos 5 | $10/MTok | $12.50/MTok | $20/MTok | $1/MTok | $50/MTok |
| Claude Opus 4.8 | $5/MTok | $6.25/MTok | $10/MTok | $0.50/MTok | $25/MTok |
| Claude Opus 4.7 | $5/MTok | $6.25/MTok | $10/MTok | $0.50/MTok | $25/MTok |
| Claude Opus 4.6 | $5/MTok | $6.25/MTok | $10/MTok | $0.50/MTok | $25/MTok |
| Claude Opus 4.5 | $5/MTok | $6.25/MTok | $10/MTok | $0.50/MTok | $25/MTok |
| Claude Opus 4.1 (deprecated) | $15/MTok | $18.75/MTok | $30/MTok | $1.50/MTok | $75/MTok |
| Claude Opus 4 (retired, except Google Cloud) | $15/MTok | $18.75/MTok | $30/MTok | $1.50/MTok | $75/MTok |
| Claude Sonnet 5 (through Aug 31, 2026 — introductory) | $2/MTok | $2.50/MTok | $4/MTok | $0.20/MTok | $10/MTok |
| Claude Sonnet 5 (from Sep 1, 2026 — standard) | $3/MTok | $3.75/MTok | $6/MTok | $0.30/MTok | $15/MTok |
| Claude Sonnet 4.6 | $3/MTok | $3.75/MTok | $6/MTok | $0.30/MTok | $15/MTok |
| Claude Sonnet 4.5 | $3/MTok | $3.75/MTok | $6/MTok | $0.30/MTok | $15/MTok |
| Claude Haiku 4.5 | $1/MTok | $1.25/MTok | $2/MTok | $0.10/MTok | $5/MTok |
| Claude Haiku 3.5 (retired, except Bedrock/Google Cloud) | $0.80/MTok | $1/MTok | $1.60/MTok | $0.08/MTok | $4/MTok |

Quote: "Introductory pricing of $2/$10 per million input/output tokens is in effect through August 31, 2026, after which the standard pricing of $3/$15 per million input/output tokens will take effect." — platform.claude.com/docs/en/about-claude/pricing — confirmed

## Long-Context Pricing

Quote: "Claude Fable 5, Claude Mythos 5, Claude Mythos Preview, Claude Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 5, and Sonnet 4.6 include the full 1M token context window at standard pricing. (A 900k-token request is billed at the same per-token rate as a 9k-token request.) Prompt caching and batch processing discounts apply at standard rates across the full context window." — platform.claude.com/docs/en/about-claude/pricing — confirmed

**Note:** the historical "2x input / 1.5x output above 200K tokens" long-context surcharge (present on older Sonnet 3.x/4.x generations per some third-party summaries) does **not** appear anywhere in the current official pricing page for any currently-active model — the current docs state standard-rate billing across the full 1M window for all current 1M-context models. Treat any claim of a long-context multiplier on current models as outdated/incorrect unless a specific official source is found.

## Data Residency / Inference Geography Multiplier

Quote: "For Claude Opus 4.6, Claude Sonnet 4.6, and later models, using `inference_geo: "us"` applies a 1.1x pricing multiplier. `inference_geo: "global"` (default) uses standard pricing." — platform.claude.com/docs/en/about-claude/pricing — confirmed

## Prompt Caching Multipliers (all current models)

Quote (table): "5-minute cache write | 1.25x base input price | Cache valid for 5 minutes" / "1-hour cache write | 2x base input price | Cache valid for 1 hour" / "Cache read (hit) | 0.1x base input price | Same duration as the preceding write" — platform.claude.com/docs/en/about-claude/pricing — confirmed

## Batch API

Quote: "A Message Batch is limited to either 100,000 Message requests or 256 MB in size, whichever is reached first." — platform.claude.com/docs/en/build-with-claude/batch-processing — confirmed

Quote: "most batches completing within 1 hour. You can access batch results when all messages have completed or after 24 hours, whichever comes first. Batches expire if processing does not complete within 24 hours." — same source — confirmed

Quote: "Batch results are available for 29 days after creation." — same source — confirmed

Quote: "All usage is charged at 50% of the standard API prices." — same source — confirmed

**Discrepancy flag:** Anthropic's docs list "Multi-turn conversations" explicitly among supported batch request types ("What can be batched" section), and streaming (`stream: true`) is the only listed unsupported parameter alongside `speed`, thread params, cache hints, `max_tokens: 0`, and a research-preview flag. A commonly repeated claim that batch has "no multi-turn tool calling" support is **not supported by the current docs** — multi-turn conversations and tool use (including server tools) are explicitly listed as supported. Flagging this as a correction to any prior assumption of "10,000 requests per batch" (current limit is 100,000 requests or 256MB) and "no multi-turn" (current docs say multi-turn is supported; only streaming is unsupported).

---

## Extended Thinking / Adaptive Thinking — Per-Model Behavior

Source: platform.claude.com/docs/en/build-with-claude/adaptive-thinking — confirmed, fetched live.

| Model | Adaptive thinking | Manual `budget_tokens` | Notes |
|---|---|---|---|
| Claude Fable 5 / Mythos 5 | Always on; cannot disable | Rejected (400) | "adaptive thinking is always on; `thinking: {type: "disabled"}` is not supported" |
| Claude Opus 4.8 | Only supported mode; off unless `thinking: {type: "adaptive"}` explicitly set | Rejected (400) | "Thinking is off unless you explicitly set `thinking: {type: "adaptive"}`" |
| Claude Opus 4.7 | Only supported mode; off by default, same as 4.8 | Rejected (400) | same pattern as 4.8 |
| Claude Opus 4.6 | Off unless explicitly set to adaptive | Still accepted but **deprecated** | "manual `{type: "enabled", budget_tokens: N}` is still accepted but deprecated" |
| Claude Sonnet 5 | **On by default**; must pass `{type: "disabled"}` to turn off | Rejected (400) | "adaptive thinking is on by default; pass `thinking: {type: "disabled"}` to turn it off" |
| Claude Sonnet 4.6 | Off unless explicitly set to adaptive | Still accepted but deprecated | same pattern as Opus 4.6 |
| Older (Sonnet 4.5, Opus 4.5, Haiku 4.5) | Not supported | Required (only thinking mode) | "Older models, such as Claude Sonnet 4.5 and Claude Opus 4.5, do not support adaptive thinking and require `thinking.type: "enabled"` with `budget_tokens`" |

Quote: "`thinking.type: "enabled"` and `budget_tokens` are deprecated on Opus 4.6 and Sonnet 4.6 and will be removed in a future model release." — confirmed

### Effort levels and thinking depth

Quote (table): "`max` | Claude always thinks with no constraints on thinking depth. Available on all models that support adaptive thinking." / "`xhigh` | Claude always thinks deeply with extended exploration. Available on Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, Claude Opus 4.7, and Claude Sonnet 5." / "`high` (default) ..." / "`medium` ..." / "`low` ..." — platform.claude.com/docs/en/build-with-claude/adaptive-thinking — confirmed

### thinking.display default (silent behavior change)

Quote: "`"omitted"` (the default) ... This is a silent change from Claude Opus 4.6, where the default was `"summarized"`." (applies to Fable 5, Mythos 5, Sonnet 5, Opus 4.8, Opus 4.7, Mythos Preview) — confirmed

### Effort parameter defaults per model

Quote: "On Claude Opus 4.8, the `effort` parameter defaults to `high` on all surfaces, including the Claude API, Claude Code, and claude.ai. On Claude Sonnet 5, it defaults to `high` on the Claude API and Claude Code." — platform.claude.com/docs/en/about-claude/models/overview — confirmed

---

## Deprecation Status — Full Table

Source: platform.claude.com/docs/en/about-claude/model-deprecations — confirmed, fetched live. Table quoted verbatim:

| API model name | Current state | Deprecated | Tentative retirement date |
|---|---|---|---|
| claude-fable-5 | Active | N/A | Not sooner than June 9, 2027 |
| claude-opus-4-8 | Active | N/A | Not sooner than May 28, 2027 |
| claude-opus-4-7 | Active | N/A | Not sooner than April 16, 2027 |
| claude-opus-4-6 | Active | N/A | Not sooner than February 5, 2027 |
| claude-opus-4-5-20251101 | Active | N/A | Not sooner than November 24, 2026 |
| claude-opus-4-1-20250805 | Deprecated | June 5, 2026 | August 5, 2026 |
| claude-opus-4-20250514 | Retired | April 14, 2026 | June 15, 2026 |
| claude-sonnet-5 | Active | N/A | Not sooner than June 30, 2027 |
| claude-sonnet-4-6 | Active | N/A | Not sooner than February 17, 2027 |
| claude-sonnet-4-5-20250929 | Active | N/A | Not sooner than September 29, 2026 |
| claude-sonnet-4-20250514 | Retired | April 14, 2026 | June 15, 2026 |
| claude-3-7-sonnet-20250219 | Retired | October 28, 2025 | February 19, 2026 |
| claude-haiku-4-5-20251001 | Active | N/A | Not sooner than October 15, 2026 |
| claude-3-5-haiku-20241022 | Retired | December 19, 2025 | February 19, 2026 |
| claude-3-haiku-20240307 | Retired | February 19, 2026 | April 20, 2026 |

Also: Claude Mythos Preview (`claude-mythos-preview`) — "will be retired on July 21, 2026." Confidence: confirmed.

**Key finding — Opus 4.5/4.6/4.7 deprecation status:** As of this audit, **none of Opus 4.5, 4.6, 4.7, or 4.8 are deprecated** — all are listed "Active" with tentative (not-sooner-than) retirement dates in 2026–2027. Only **Opus 4.1** (`claude-opus-4-1-20250805`) is deprecated, with a firm retirement date of August 5, 2026. **Sonnet 4.6 and Sonnet 4.5 are Active, not deprecated.** (Only Sonnet 4 (`claude-sonnet-4-20250514`, no ".6") is retired.)

---

## Whether `claude-sonnet-4-6-20250514` Ever Existed as a Valid Model ID

**Finding: No — this string does not correspond to any real, documented model ID at any point.** Confidence: confirmed, via cross-reference of two official pages.

Reasoning, cited to official sources:
1. Per platform.claude.com/docs/en/about-claude/models/model-ids-and-versions: "Starting with the Claude 4.6 generation, model IDs use a dateless format: `claude-{name}-{major}[-{minor}]`. For example: `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-opus-4-6`, `claude-opus-4-7`, and `claude-opus-4-8`." — the 4.6 generation, by design, **never** takes a dated suffix. A dated variant like `-20250514` would contradict the documented naming scheme for 4.6+.
2. The date `20250514` is documented elsewhere as the release-date suffix of a **different, older model**: `claude-sonnet-4-20250514` (Claude Sonnet 4, not 4.6) — per the model-deprecations page: "claude-sonnet-4-20250514 | Retired | April 14, 2026 | June 15, 2026." That model was retired June 15, 2026, and was never called Sonnet "4.6."
3. Quote: "A common misconception is that dateless model IDs such as `claude-sonnet-4-6` behave as evergreen pointers ... For the 4.6 generation and later, the dateless ID is the canonical model ID for that release. It maps to a single, fixed model snapshot." This directly confirms Sonnet 4.6 has no dated form.

Conclusion: `claude-sonnet-4-6-20250514` conflates the real dateless ID `claude-sonnet-4-6` with the release date of the unrelated, retired `claude-sonnet-4-20250514`. It is a fabricated/invalid ID.

---

## Claude 5 Family (Sonnet 5, Fable 5, Mythos 5) — Facts

All confirmed via platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 and platform.claude.com/docs/en/about-claude/models/overview, fetched live, unless noted otherwise (Sonnet 5 announcement fetched via WebFetch of anthropic.com/news/claude-sonnet-5).

- **Claude Fable 5** (`claude-fable-5`): "Anthropic's most capable widely released model, built for the most demanding reasoning and long-horizon agentic work." 1M token context window, 128K max output, $10/$50 per MTok. Confirmed.
- **Claude Mythos 5** (`claude-mythos-5`): "Shares the same capabilities and is available only in limited release through Project Glasswing." Same specs/pricing as Fable 5. Successor to the invitation-only Claude Mythos Preview (`claude-mythos-preview`, retiring July 21, 2026). Key difference from Fable 5: "Claude Mythos 5 does not include these [safety] classifiers" that Fable 5 has. Confirmed.
- **Availability date:** "Claude Fable 5 and Claude Mythos 5 both become available on June 9, 2026." Confirmed.
- **Access restoration note:** The live page carries a tip: "Access to Claude Fable 5 and Claude Mythos 5 has been restored. See our statement for more information" (linking anthropic.com/news/redeploying-fable-5) — indicating Fable 5 access was paused and later restored at some point after its June 9, 2026 launch. Confirmed (quote present on page) but the underlying incident details are **unverifiable** from this page alone (would require fetching anthropic.com/news/redeploying-fable-5, not done in this audit).
- **Data retention:** "Claude Fable 5 and Claude Mythos 5 carry 30-day data retention and are not available under zero data retention: both are designated Covered Models." Confirmed.
- **Refusals:** "Claude Fable 5 includes safety classifiers that can decline certain requests... Claude Mythos 5 does not include these classifiers." A decline returns `stop_reason: "refusal"` as an HTTP 200, not an error. Confirmed.
- **Fallback / billing:** Server-side `fallbacks` parameter (beta), client-side SDK middleware, or manual "fallback credit" retry are the three documented ways to retry a refusal on another model; "You are not billed for a request that is refused before any output is generated." Confirmed.
- **Adaptive thinking always on:** "Adaptive thinking is the only thinking mode on Claude Fable 5 and Claude Mythos 5. It applies whenever the `thinking` parameter is unset. `thinking: {"type": "disabled"}` is not supported." Confirmed.
- **Raw chain-of-thought never exposed:** "The raw chain of thought is never returned on Claude Fable 5 and Claude Mythos 5." `display: "summarized"` gives a readable summary; `"omitted"` (default) gives an empty `thinking` field. Confirmed.
- **Tokenizer:** Fable 5 (and Mythos 5) use the tokenizer introduced with Opus 4.7 — "compared to models before Claude Opus 4.7, the same text produces roughly 30% more tokens." Confirmed (models overview tooltip + pricing page note).
- **Claude Sonnet 5** (`claude-sonnet-5`): "The best combination of speed and intelligence" per the models overview; per the anthropic.com/news/claude-sonnet-5 announcement, "built to be the most agentic Sonnet model yet. It can make plans, use tools like browsers and terminals, and run autonomously," with gains in "reasoning, tool use, coding, and knowledge work," and it "autonomously checks its own output without explicitly being asked." Confirmed (announcement page, fetched live). Announcement date reported by the fetch as "Jun 30, 2026" — confidence: inferred (taken from a WebFetch summary of the announcement page rather than a directly quoted, dated byline I independently re-verified character-for-character; treat the exact day as likely-correct but not independently cross-checked against a second source).
- **Sonnet 5 pricing:** $2/$10 per MTok introductory (through Aug 31, 2026), $3/$15 standard thereafter. Confirmed (pricing page).
- **Sonnet 5 context/output:** 1M token context window, 128K max output tokens — confirmed via models overview comparison table (same row as Fable 5/Opus 4.8).
- **Sonnet 5 adaptive thinking:** On by default (must explicitly disable) — confirmed, adaptive-thinking page.
- **Sonnet 5 effort levels:** Full `low`/`medium`/`high`/`xhigh`/`max` range supported, `xhigh` newly available on Sonnet 5 (previously Opus-only) — confirmed, adaptive-thinking page.

---

## Context Windows — Additional Confirmed Facts

Source: platform.claude.com/docs/en/build-with-claude/context-windows — confirmed, fetched live.

Quote: "Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 5, and Claude Sonnet 4.6 have a 1M-token context window on the Claude API, Amazon Bedrock, Google Cloud, and Microsoft Foundry. Claude Mythos Preview also has a 1M-token context window." — confirmed

Quote: "Claude Fable 5 and Claude Mythos 5 (claude-fable-5 and claude-mythos-5) have a 1M-token context window, and a single request to these models can generate up to 128k output tokens (`max_tokens`). Other Claude models, including Claude Sonnet 4.5, have a 200k-token context window." — confirmed

Quote: "For every model with a 1M-token context window, 1M is the default: you don't need a beta header, and long-context requests are billed at standard pricing." — confirmed (this directly contradicts any claim of a 1M "beta" gate or a long-context price multiplier for these models)

Quote (extended output on Batch API): "The `output-300k-2026-03-24` beta header raises the `max_tokens` cap to 300,000 for batch requests using Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 5, or Claude Sonnet 4.6." — platform.claude.com/docs/en/build-with-claude/batch-processing — confirmed. Note this is Batch-API-only and beta; the synchronous Messages API cap remains 128K for these models.

---

## Extended Thinking (`budget_tokens`) — Which Models Still Support It

Source: platform.claude.com/docs/en/build-with-claude/extended-thinking (via WebFetch summary) — confirmed for the headline claims; the fetch tool returned a summarized extraction rather than the full raw page text, so exact-quote fidelity here is slightly lower than other rows — confidence noted per row.

- Manual `budget_tokens` currently supported (not deprecated): Claude Opus 4.5, Claude Haiku 4.5, and earlier Claude 4 models. Confidence: inferred (from summarized fetch, cross-checked against the adaptive-thinking page's explicit statement that Opus 4.5 "require[s] `thinking.type: "enabled"` with `budget_tokens`" — that specific cross-check is confirmed).
- Manual `budget_tokens` deprecated but still functional: Claude Opus 4.6, Claude Sonnet 4.6. Confirmed (corroborated verbatim on the adaptive-thinking page).
- Manual `budget_tokens` rejected with 400: Claude Fable 5, Claude Mythos 5, Claude Mythos Preview, Claude Opus 4.8, Claude Opus 4.7, Claude Sonnet 5. Confirmed (corroborated on adaptive-thinking page: "All models except Claude Fable 5, Claude Mythos 5, Claude Sonnet 5, Claude Opus 4.8, and Claude Opus 4.7 (rejected with a 400 error). Deprecated on Opus 4.6 and Sonnet 4.6").

---

## Unverifiable

The following claims from common secondary/AI-generated summaries (including the cached skill content present in this session, which is explicitly excluded as a source per the task's rules) could **not** be independently confirmed against an official Anthropic page within this audit's scope, and should be treated as unverified until checked directly:

1. **"claude-fable-5" access-pause incident details** — the models overview page references a restoration notice and links to `anthropic.com/news/redeploying-fable-5`, but that page was not fetched in this audit, so the reason for/duration of the original access pause is unverifiable here.
2. **Exact byline date "June 30, 2026" for the Claude Sonnet 5 announcement** — obtained via a WebFetch summarization pass rather than a directly quoted, verbatim-matched date string from the raw page; treat as likely correct but not fully cross-verified character-for-character.
3. **Full extended-thinking page content beyond the headline model-support claims** — the WebFetch for `extended-thinking` returned a synthesized summary (not exhaustive raw text), so finer details (e.g., precise minimum `budget_tokens` value, exact wording of every constraint) were not independently re-verified against the raw page in this pass.
4. **Anthropic Skilljar / Academy course content** — not consulted in this audit; no claims from anthropic.skilljar.com are included here.
5. **Console.anthropic.com-specific UI details** (e.g., exact Console menu paths for usage export) — referenced indirectly by the pricing/model-deprecations pages but not independently verified by visiting console.anthropic.com directly.
6. **Whether a long-context (>200K) price multiplier applies to any current model** — current official pricing page states standard pricing across the full 1M window for all current 1M-context models, with no multiplier language found; this is treated as confirmed for current models, but historical/legacy-model long-context multipliers (e.g., on very old Sonnet/Opus dated snapshots below 1M context) were not separately audited and should be treated as unverified in either direction.
