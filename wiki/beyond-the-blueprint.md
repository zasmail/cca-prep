# Beyond the Blueprint

*Current best practice beyond the July-2026 CCA-F blueprint. This is the **fast-moving page** — verified as of **2026-07-16** against official Anthropic sources only (anthropic.com, platform.claude.com, code.claude.com, claude.com). Everything here postdates or extends the exam guide's apparent scope; whether the blueprint itself has since caught up to any of it is unconfirmed. Re-verify before leaning on a specific number in an interview — this lineup moves in weeks, not quarters.*

## The thread

The exam blueprint freezes a snapshot; the field didn't stop moving under it. Nine developments since late 2025 change how a working Applied AI engineer should actually build, even where the certification framing hasn't updated: tool-count ceilings became an architecture choice instead of a hard cap, MCP servers are now code APIs instead of chat turns, a new model tier sits above Opus with its own refusal semantics, the SDK/Managed-Agents split formalizes "prototype vs. production," and governance of MCP itself left Anthropic's building. None of this invalidates the D1–D5 framework — it extends it. Each item below tags which domain it sharpens, so you can decide whether to mention it as "one more thing I'd add" in an interview answer.

---

## 1. Tool Search Tool + Programmatic Tool Calling

**What it is:** Two features from Anthropic's Nov 24, 2025 "Advanced Tool Use" release. **Tool Search Tool** keeps tool definitions out of context until Claude actually requests them — scales tool vocabularies into the thousands without bloating every turn. **Programmatic Tool Calling** has Claude write code in a sandbox that calls multiple tools, processes their outputs, and decides what actually enters context — collapsing N round-trips into one.

**Why an Applied AI engineer cares:** This directly obsoletes the "≤5 tools per agent, 18+ degrades selection" framing (anti-pattern #8 in this repo). The fix for a large tool vocabulary is no longer "curate down to 5" — it's "load on demand and let the model orchestrate in code." If you're designing a tool surface for a real product with dozens of integrations, this is the pattern, not a workaround.

**Source:** https://www.anthropic.com/engineering/advanced-tool-use

**Extends:** D2 (Tool Design & MCP Integration) — the single highest-value update to this repo's anti-pattern #8.

---

## 2. Code execution with MCP (150k → 2k tokens)

**What it is:** A Nov 4, 2025 engineering post demonstrating that presenting MCP servers as code APIs (rather than direct tool-call turns) cut a real Drive-to-Salesforce workflow from 150,000 tokens to 2,000 — a 98.7% reduction — by letting Claude write code that calls, filters, and chains MCP tools before anything hits the model's context.

**Why an Applied AI engineer cares:** This is the concrete, measured version of "progressive disclosure" and the token-efficiency argument underneath Programmatic Tool Calling above. If a workflow burns tens of thousands of tokens moving data between two connected systems, this is the fix — not a bigger context window.

**Source:** https://www.anthropic.com/engineering/code-execution-with-mcp

**Extends:** D5 (Context Management & Reliability) — the sharpest concrete number for the "context is the scarce resource" thesis; also reinforces D2.

---

## 3. `refusal` stop_reason + fallbacks

**What it is:** A new `stop_reason: "refusal"` value, returned as a normal HTTP 200 (not an error), emitted when a safety classifier declines a request mid-stream. Ships with Claude Fable 5's input classifiers. Anthropic provides three ways to recover: a server-side `fallbacks` parameter (beta), client-side SDK middleware, or a manual retry — and you are **not billed** for a refused request (no output was generated).

**Why an Applied AI engineer cares:** This repo's stop_reason reference card lists 5 values; current docs list 7 (`pause_turn` also joined). An agent loop that only branches on `end_turn`/`tool_use`/`max_tokens` will silently mishandle a refusal as if it were a normal completion. Any production agent loop built after Fable 5's launch needs an explicit `refusal` branch with a fallback path.

**Source:** https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons ; https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5

**Extends:** D1 (Agentic Architecture) — the agentic-loop / stop_reason-driven termination core, plus D5 reliability (this repo's CLAUDE.md reference card is stale here; see the audit's correction #9).

---

## 4. Fable 5 / Mythos 5 tier, Sonnet 5 default, adaptive-thinking-only, `effort` param

**What it is:** A new model tier above Opus. **Claude Fable 5** (`claude-fable-5`) is the generally-available, safety-classifier-guarded model; **Claude Mythos 5** (`claude-mythos-5`) is the same model with safeguards lifted, restricted to approved customers via Project Glasswing. Both launched June 9, 2026: 1M context, 128K output, $10/$50 per MTok. Separately, **Claude Sonnet 5** (`claude-sonnet-5`) became the default Free/Pro model June 30, 2026 ($2/$10 intro through Aug 31 2026, then $3/$15). On this whole generation, **adaptive thinking is the only mode** — manual `budget_tokens` is rejected outright (Fable 5, Mythos 5, Sonnet 5, Opus 4.7/4.8) or deprecated-but-still-accepted (Opus 4.6, Sonnet 4.6). Thinking depth is now tuned with an **`effort` parameter** (`low`/`medium`/`high`/`xhigh`/`max`) instead of a token budget.

**Why an Applied AI engineer cares:** Model lineups move fast enough to invalidate a reference card within months — this repo's card was a full generation behind until the 2026-07-16 audit (no Fable/Mythos/Sonnet 5 rows, thinking framed around manual `budget_tokens`, and a hardcoded default model ID that never existed — the 4.6 generation only ships dateless IDs). Habit to build: re-verify model IDs and pricing against the live docs before quoting them anywhere, including interviews.

**Source:** https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 ; https://www.anthropic.com/news/claude-sonnet-5 ; https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking

**Extends:** D1 (model selection / agentic capability), D5 (extended thinking is a context-management lever) — and is the root cause of this repo's fabricated-model-ID bug (audit correction #1).

---

## 5. Agent SDK vs. Claude Managed Agents

**What it is:** The Claude Code SDK was renamed the **Agent SDK** to reflect scope beyond coding — it's a library (Python/TypeScript) that runs the agent loop, tools, hooks, subagents, and MCP connections **in your own process**. **Claude Managed Agents** is a separate, newer (April 2026) hosted REST API where **Anthropic runs the agent and the sandbox**; your app sends events and streams results back. The documented path: prototype locally on the Agent SDK, move to Managed Agents for production scale.

**Why an Applied AI engineer cares:** This repo never draws this line at all — it treats "Claude Code" as the only agent-building surface. In practice, "where does the agent loop actually run" is now an architectural decision with two named, opinionated answers, and interviewers may probe whether you know the tradeoff (your infra + full control vs. Anthropic's infra + less ops burden, at the cost of ZDR/HIPAA eligibility — Managed Agents sessions are stateful and don't currently qualify for either).

**Source:** https://code.claude.com/docs/en/agent-sdk/overview ; https://platform.claude.com/docs/en/managed-agents/overview

**Extends:** D1 (Agentic Architecture & Orchestration) — a genuinely new architectural axis this repo's framework doesn't cover.

---

## 6. Routines / scheduling

**What it is:** **Claude Code Routines** (April 2026) are a saved automation — prompt + repo + connectors — that runs on a cron schedule, an API call, or a GitHub event, executing on Anthropic-managed cloud infrastructure rather than your local machine. Managed separately from this is **Managed Agents scheduling** (cron-based recurring runs) and **Vaults** (secure credential storage for Managed Agents), both in public beta since June 9, 2026. Routines are the Claude Code-native, repo-scoped automation surface; Managed Agents scheduling is the general operational surface.

**Why an Applied AI engineer cares:** "Always-on / scheduled agents" already appears in this repo's orchestration-patterns page as a pattern (the "loop"), but it's framed as something you build yourself with cron + a script. Anthropic now ships this as a first-party feature with usage caps (Pro 5/day, Max 15/day, Team/Enterprise 25/day) — worth knowing the product exists before reinventing it.

**Source:** https://claude.com/blog/introducing-routines-in-claude-code ; https://code.claude.com/docs/en/routines ; https://claude.com/blog/whats-new-in-claude-managed-agents

**Extends:** D1 (orchestration patterns — the "always-on/scheduled" pattern) and D3 (Claude Code Configuration & Workflows — a first-party automation primitive).

---

## 7. Agent Skills open standard + Plugins

**What it is:** **Agent Skills** (Oct 16, 2025; published as an open standard Dec 18, 2025) are folders of instructions/scripts/resources an agent discovers and loads via progressive disclosure — name+description always visible, full SKILL.md read on demand, bundled files (including runnable scripts) loaded only as needed. **Claude Code Plugins** (Oct 9, 2025, public beta) package skills, subagents, MCP servers, and hooks into one installable, toggleable unit, distributed through marketplaces including an official one and a public directory with an "Anthropic Verified" designation.

**Why an Applied AI engineer cares:** This repo's `.claude/commands/*.md` slash commands are the **legacy** format. `.claude/skills/<name>/SKILL.md` is the current recommended format — it gains progressive disclosure, `disable-model-invocation`, bundled scripts, and plugin packaging that commands don't have. The legacy format still works identically, so nothing is broken, but modeling current D3 best practice means migrating.

**Source:** https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills ; https://claude.com/blog/claude-code-plugins ; https://claude.com/plugins

**Extends:** D3 (Claude Code Configuration & Workflows) — direct currency gap vs. this repo's `.claude/commands/` convention.

---

## 8. Context engineering as its own discipline

**What it is:** Anthropic's Sept 29, 2025 engineering post formally names and distinguishes **context engineering** from prompt engineering: "the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference" — an iterative, every-turn discipline, not a one-time authoring task like a system prompt.

**Why an Applied AI engineer cares:** This is the intellectual backbone this repo's own `wiki/context-engineering.md` is already built around — it's not new information so much as the canonical citation for why D5 exists as a named domain at all. Worth knowing the term has an official, dated origin rather than being informal industry jargon.

**Source:** https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

**Extends:** D5 (Context Management & Reliability) — names the discipline the whole domain is built on.

---

## 9. MCP donated to the Agentic AI Foundation

**What it is:** Dec 9, 2025 — Anthropic donated MCP governance to a new, independently-run **Agentic AI Foundation**, a Linux Foundation directed fund co-founded with Block and OpenAI and backed by Google, Microsoft, AWS, Cloudflare, and Bloomberg. MCP joins goose (Block) and AGENTS.md (OpenAI) as founding projects; the governance model is unchanged for now. **Caveat:** the specific upcoming spec RC (2026-07-28 — stateless transport, MCP Apps, Tasks demoted to extension) lives only on `modelcontextprotocol.io`, which is no longer an Anthropic-controlled domain post-donation — treat spec-RC details as context, not audited ground truth, per this repo's own sourcing rule.

**Why an Applied AI engineer cares:** "Who owns MCP" is now a legitimate interview question with a real, recent answer — it's not an Anthropic-controlled standard anymore, which matters for anyone betting infrastructure on its long-term direction or stability guarantees.

**Source:** https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation

**Extends:** D2 (Tool Design & MCP Integration) — governance context for "why MCP" that this repo's tool-design module doesn't cover.

---

## Provenance note

Items 1–9 above are Anthropic's own official-source claims, fetched live 2026-07-16 (see `research/audit/facts-beyond-exam-delta.md`, `facts-api-mechanics.md`, and `facts-models-pricing.md` for the full quote-level citations). Whether the July-2026 CCA-F blueprint itself has caught up to any of these is **unconfirmed** — some may quietly already be in scope, some may not be tested for years. Use this page to sound current in an interview, not to guess what's on the exam.
