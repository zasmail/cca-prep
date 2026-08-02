# API Mechanics Fact Sheet — Ground Truth Audit

Retrieved: 2026-07-16. All sources fetched live via WebFetch/WebSearch against official Anthropic properties. Docs at `docs.claude.com` now 301/302-redirect to `platform.claude.com`; that domain is treated as the same official property (it is the current home of the same documentation set, still under the `claude.com` domain named in the source rules). `code.claude.com` used for Agent SDK. Note: the live docs describe a model lineup (Opus 4.8, Sonnet 5, Claude Fable 5, Claude Mythos 5) that is newer than what's in the project's CLAUDE.md (which references Sonnet/Opus/Haiku 4.5/4.6) — flagged inline where it matters for the audit.

---

## 1. `stop_reason` enum

| Claim | Source URL | Quote | Confidence |
|---|---|---|---|
| `end_turn` — model reached a natural stopping point | https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons | "`end_turn`" — "Claude finished its response naturally." | confirmed |
| `max_tokens` — hit the requested/model max_tokens limit | https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons | "`max_tokens`" — "The response reached your `max_tokens` limit." | confirmed |
| `stop_sequence` — hit a custom stop sequence | https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons | "`stop_sequence`" — "Claude emitted one of your `stop_sequences`." | confirmed |
| `tool_use` — model invoked one or more tools | https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons | "`tool_use`" — "Claude invoked one or more tools." (also stated on tool-use overview: "the response carries a `tool_use` block") | confirmed |
| `pause_turn` — a long-running/server-tool turn was paused; resend as-is to continue | https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons ; https://platform.claude.com/docs/en/api/messages | "`pause_turn`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue." (api/messages fetch) / handling-stop-reasons: "A server-tool loop reached its iteration limit." | confirmed |
| `refusal` — model declined to respond (streaming classifier intervention) | https://platform.claude.com/docs/en/api/messages ; https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons | api/messages: "`refusal`: when streaming classifiers intervene to handle potential policy violations." handling-stop-reasons: "Claude declined to respond." | confirmed |
| `model_context_window_exceeded` — response filled the model's context window | https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons | "`model_context_window_exceeded`" — "The response filled the model's context window." | confirmed |
| In non-streaming mode `stop_reason` is always non-null; in streaming it's null in `message_start`, non-null otherwise | https://platform.claude.com/docs/en/api/messages | "In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise." | confirmed |

**Audit note:** CLAUDE.md's reference card lists only 5 values (`end_turn`, `max_tokens`, `stop_sequence`, `tool_use`, `model_context_window_exceeded`) and omits `pause_turn` and `refusal`, both of which are currently documented. This is a gap worth flagging to the user — current docs show **7** stop_reason values, not 5.

---

## 2. `tool_choice` options and extended-thinking compatibility

| Claim | Source URL | Quote | Confidence |
|---|---|---|---|
| `auto` — Claude decides whether to call any provided tool; default when tools are provided | https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools | "`auto` allows Claude to decide whether to call any provided tools or not. This is the default value when `tools` are provided." | confirmed |
| `any` — Claude must use one of the provided tools, not a particular one | https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools | "`any` tells Claude that it must use one of the provided tools, but doesn't force a particular tool." | confirmed |
| `tool` — forces Claude to always use a specific named tool | https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools | "`tool` forces Claude to always use a particular tool." | confirmed |
| `none` — prevents any tool use; default when no tools are provided | https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools | "`none` prevents Claude from using any tools. This is the default value when no `tools` are provided." | confirmed |
| With extended thinking + tool use, `any` and `tool` are NOT supported and error; only `auto` and `none` are compatible | https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools | "When using extended thinking with tool use, `tool_choice: {\"type\": \"any\"}` and `tool_choice: {\"type\": \"tool\", \"name\": \"...\"}` are not supported and will result in an error. Only `tool_choice: {\"type\": \"auto\"}` (the default) and `tool_choice: {\"type\": \"none\"}` are compatible with extended thinking." | confirmed |
| Changing `tool_choice` invalidates cached message blocks (tools/system prompt stay cached) | https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools | "When using prompt caching, changes to the `tool_choice` parameter will invalidate cached message blocks. Tool definitions and system prompts remain cached, but message content must be reprocessed." | confirmed |
| When `tool_choice` is `any`/`tool`, API prefills the assistant turn so no natural-language text precedes the tool call | https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools | "Note that when you have `tool_choice` as `any` or `tool`, the API prefills the assistant message to force a tool to be used. This means that the models will not emit a natural language response or explanation before `tool_use` content blocks..." | confirmed |
| A separate model ("Claude Mythos Preview") does not support forced tool use at all (400 error on `any`/`tool`) | https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools | "[Claude Mythos Preview] does not support forced tool use. Requests with `tool_choice: {\"type\": \"any\"}` or `tool_choice: {\"type\": \"tool\", \"name\": \"...\"}` return a 400 error on this model." | confirmed |

**Audit note:** matches CLAUDE.md's claim that `any`/`tool` are incompatible with extended thinking — confirmed correct and current.

---

## 3. Batch API

| Claim | Source URL | Quote | Confidence |
|---|---|---|---|
| Discount: all batch usage billed at 50% of standard API prices | https://platform.claude.com/docs/en/build-with-claude/batch-processing | "The Batches API offers significant cost savings. All usage is charged at 50% of the standard API prices." | confirmed |
| Max requests per batch: **100,000** (not 10,000) OR 256 MB, whichever is reached first | https://platform.claude.com/docs/en/build-with-claude/batch-processing | "A Message Batch is limited to either 100,000 Message requests or 256 MB in size, whichever is reached first." | confirmed |
| Processing window: most batches finish within 1 hour; batches expire (results unavailable for unfinished requests) if not done within **24 hours** | https://platform.claude.com/docs/en/build-with-claude/batch-processing | "The system processes each batch as fast as possible, with most batches completing within 1 hour. You can access batch results when all messages have completed or after 24 hours, whichever comes first. Batches expire if processing does not complete within 24 hours." | confirmed |
| Results retention: available for download for **29 days** after creation, batch metadata viewable after that but results are gone | https://platform.claude.com/docs/en/build-with-claude/batch-processing | "Batch results are available for 29 days after creation. After that, you may still view the Batch, but its results will no longer be available for download." | confirmed |
| No SLA stated explicitly, but system note says "processes as fast as possible" — rate limits and demand can slow it | https://platform.claude.com/docs/en/build-with-claude/batch-processing | "Additionally, processing may be slowed down based on current demand and your request volume. In that case, you may see more requests expiring after 24 hours." | confirmed |
| `stream: true` is NOT supported inside a batch (results come back as a single file/jsonl) | https://platform.claude.com/docs/en/build-with-claude/batch-processing | "`stream: true` — Batch results come back as a single file, not a stream." | confirmed |
| Multi-turn conversations ARE supported in batch (contrary to a "no multi-turn" assumption); what's unsupported is stateful/threaded params (`store`/`previous_thread_event_id`) | https://platform.claude.com/docs/en/build-with-claude/batch-processing | Supported list: "Multi-turn conversations" appears under "What can be batched." Unsupported: "`store` / `previous_thread_event_id` (Threads) — Threads are stateful; batch requests are not." | confirmed |
| Results format: `.jsonl`, one JSON object per line, four result types (`succeeded`, `errored`, `canceled`, `expired`) | https://platform.claude.com/docs/en/build-with-claude/batch-processing | "The results are in `.jsonl` format, where each line is a valid JSON object representing the result of a single request in the Message Batch." | confirmed |
| Prompt caching stacks with batch discount; cache hit rates on batch are "best-effort," typically 30–98% | https://platform.claude.com/docs/en/build-with-claude/batch-processing | "Users typically experience cache hit rates ranging from 30% to 98%, depending on their traffic patterns." | confirmed |

**Audit note — IMPORTANT DISCREPANCY:** CLAUDE.md states Batch API max is **10,000 requests per batch**. Current official docs state the limit is **100,000 requests or 256 MB**, whichever comes first. This looks like either a stale figure in the project's reference card or a real historical value that Anthropic has since raised — either way, the *current* official max is 100,000, not 10,000. Also CLAUDE.md doesn't mention "no multi-turn tool calling" as a batch restriction, and current docs actually say multi-turn and tool use (including server tools) ARE supported in batch — the actual unsupported list is narrower (`stream`, `speed`/Fast mode, `store`/thread continuation, `cache_hint`/`context_hint`, `max_tokens: 0`, a `research_preview` beta flag). Recommend correcting CLAUDE.md's "10,000" cap and the "no multi-turn tool calling" claim.

---

## 4. Prompt Caching

| Claim | Source URL | Quote | Confidence |
|---|---|---|---|
| Cache hit cost = 10% (0.1x) of base input token price | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | "Cache hits cost 0.1 times the base input token price (10% of base price)." | confirmed |
| 5-minute TTL cache write = 1.25x base input price | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | "5-minute TTL: 1.25 times the base input token price (25% more than base)" | confirmed |
| 1-hour TTL cache write = 2x base input price | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | "1-hour TTL: 2 times the base input token price (100% more than base)" | confirmed |
| Minimum cacheable tokens varies by model: e.g. Sonnet 5 / Opus 4.8 = 1,024; Claude Fable 5 / Mythos 5 = 512; Opus 4.6/4.5, Haiku 4.5 = 4,096; Haiku 3.5 = 2,048 | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | Table quoted verbatim (see tool output above); e.g. "Claude Opus 4.8 \| 1,024" | confirmed |
| Up to 4 explicit cache breakpoints per request | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | "Up to 4 explicit cache breakpoints are allowed per request." | confirmed |
| Cache prefix order: `tools`, then `system`, then `messages` (hierarchical) | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | "Cache prefixes are created in the following order: `tools`, `system`, then `messages`. This order forms a hierarchy where each level builds upon the previous ones." | confirmed |

**Audit note:** CLAUDE.md's caching numbers (10% hit cost, 1.25x/2x write costs by TTL, 1024-token minimum, 4 breakpoints, tools→system→messages order) all check out against current docs for the **Sonnet-tier minimum** specifically — but CLAUDE.md states "minimum 1024 tokens" as a flat rule, when in fact the minimum is **model-dependent** (512 to 4,096 depending on model). Worth a caveat in the study material.

---

## 5. Citations

| Claim | Source URL | Quote | Confidence |
|---|---|---|---|
| `cited_text` does NOT count toward output tokens (and isn't counted toward input tokens when passed back in later turns) | https://platform.claude.com/docs/en/build-with-claude/citations | "The `cited_text` field is provided for convenience and does not count toward output tokens." / "When passed back in subsequent conversation turns, `cited_text` is also not counted toward input tokens." | confirmed |
| Citations are incompatible with structured outputs — combining them returns a 400 error | https://platform.claude.com/docs/en/build-with-claude/citations | "Citations cannot be used together with structured outputs. If you enable citations on any user-provided document ... and also include the `output_config.format` parameter (or the deprecated `output_format` parameter), the API returns a 400 error." | confirmed |
| Citations must be enabled on all documents in a request, or none | https://platform.claude.com/docs/en/build-with-claude/citations | "Set `citations.enabled=true` on each of your documents. Currently, citations must be enabled on all or none of the documents within a request." | confirmed |
| Enabling citations increases input tokens slightly (system prompt + chunking overhead), but is efficient on output tokens | https://platform.claude.com/docs/en/build-with-claude/citations | "Enabling citations incurs a slight increase in input tokens because of system prompt additions and document chunking. However, the citations feature is very efficient with output tokens." | confirmed |
| Anthropic's own evaluations show citations feature is "significantly more likely" to cite the most relevant quotes vs. prompting alone — no specific "~15% better recall" percentage is stated on this page | https://platform.claude.com/docs/en/build-with-claude/citations | "In Anthropic's evaluations, the citations feature is significantly more likely to cite the most relevant quotes from documents than purely prompt-based approaches." | confirmed (no % figure found) |
| Citations work with prompt caching (cache the source documents, not the citation blocks) and with batch processing and token counting | https://platform.claude.com/docs/en/build-with-claude/citations | "Citations work in conjunction with other API features including prompt caching, token counting, and batch processing." | confirmed |
| All active models support citations | https://platform.claude.com/docs/en/build-with-claude/citations | "All active models support citations." | confirmed |

**Audit note — DISCREPANCY:** CLAUDE.md's "~15% better recall when enabled" figure could NOT be verified on the current official citations page — it only says citations are "significantly more likely" to cite relevant quotes, with no percentage given. This number is listed under **Unverifiable** below; it may come from an older Anthropic blog/announcement not currently reachable, or from a third-party source that got folded into the study notes. Everything else in CLAUDE.md's citations section (cited_text token accounting, all-or-none rule, structured-outputs incompatibility) is confirmed accurate.

---

## 6. Structured Outputs

| Claim | Source URL | Quote | Confidence |
|---|---|---|---|
| Structured outputs constrain responses to a JSON schema via `output_config.format`, guaranteeing valid/parseable output | https://platform.claude.com/docs/en/build-with-claude/structured-outputs | "Structured outputs constrain Claude's responses to follow a specific JSON schema, ensuring valid, parseable output for downstream processing." | confirmed |
| Two capabilities: JSON outputs (`output_config.format`) and strict tool use (`strict: true` on tool defs) | https://platform.claude.com/docs/en/build-with-claude/structured-outputs | Summarized from doc structure: "JSON outputs... Get Claude's response in a specific JSON format" and "Strict tool use... Guarantee schema validation on tool names and inputs." | confirmed |
| Guarantees: always valid JSON, type-safe fields, no retries needed for schema violations | https://platform.claude.com/docs/en/build-with-claude/structured-outputs | "Always valid: No more `JSON.parse()` errors. Type safe: Guaranteed field types and required fields. Reliable: No retries needed for schema violations." | confirmed |
| Model availability: GA on a specific list of current models (Fable 5, Mythos 5, Opus 4.8, Mythos Preview, Opus 4.7, Opus 4.6, Sonnet 5, Sonnet 4.6, Sonnet 4.5, Opus 4.5, Haiku 4.5) | https://platform.claude.com/docs/en/build-with-claude/structured-outputs | "Structured outputs are generally available on the Claude API for Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, Claude Mythos Preview, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 5, Claude Sonnet 4.6, Claude Sonnet 4.5, Claude Opus 4.5, and Claude Haiku 4.5." | confirmed |
| Claude may still refuse or hit token limits, producing output that doesn't match the schema despite structured outputs | https://platform.claude.com/docs/en/build-with-claude/structured-outputs | "While structured outputs guarantee schema compliance in most cases, Claude may refuse requests for safety reasons or hit token limits, producing output that doesn't match your schema." | confirmed |
| Changing `output_config.format` invalidates prompt cache for that thread | https://platform.claude.com/docs/en/build-with-claude/structured-outputs | "Changing the `output_config.format` parameter will invalidate any prompt cache for that conversation thread." | confirmed |
| Incompatible with citations (see Citations section above — confirmed from the citations page, cross-referenced) | https://platform.claude.com/docs/en/build-with-claude/citations | (quoted above) | confirmed |

---

## 7. Agent SDK vs. Claude Managed Agents (headline level)

| Claim | Source URL | Quote | Confidence |
|---|---|---|---|
| Agent SDK = a library that runs the agent loop **in your own process**, giving the same tools/agent loop/context management that power Claude Code, for Python and TypeScript | https://code.claude.com/docs/en/agent-sdk/overview | "Build AI agents that autonomously read files, run commands, search the web, edit code, and more. The Agent SDK gives you the same tools, agent loop, and context management that power Claude Code, programmable in Python and TypeScript." | confirmed |
| Agent SDK includes built-in tools (Read, Write, Edit, Bash, Monitor, Glob, Grep, WebSearch, WebFetch, AskUserQuestion) so you don't implement tool execution yourself | https://code.claude.com/docs/en/agent-sdk/overview | "The Agent SDK includes built-in tools for reading files, running commands, and editing code, so your agent can start working immediately without you implementing tool execution." | confirmed |
| Agent SDK supports hooks, subagents, MCP, permissions, and sessions (resumable/forkable) | https://code.claude.com/docs/en/agent-sdk/overview | Section headers/quotes: "Run custom code at key points in the agent lifecycle..." "Spawn specialized agents to handle focused subtasks..." "Connect to external systems via the Model Context Protocol..." | confirmed |
| Managed Agents = a **hosted REST API**: Anthropic runs the agent and the sandbox; your app sends events and streams results back. Agent SDK runs the loop in your own process — opposite of Managed Agents | https://code.claude.com/docs/en/agent-sdk/overview | "[Managed Agents] is a hosted REST API: Anthropic runs the agent and the sandbox, and your application sends events and streams back results. The Agent SDK is a library that runs the agent loop inside your own process." | confirmed |
| Common path: prototype with Agent SDK locally, then move to Managed Agents for production | https://code.claude.com/docs/en/agent-sdk/overview | "A common path is to prototype with the Agent SDK locally, then move to Managed Agents for production." | confirmed |
| Managed Agents = "pre-built, configurable agent harness that runs in managed infrastructure"; best for long-running/async tasks; provides secure sandbox, file/bash/web tools, built-in caching & compaction | https://platform.claude.com/docs/en/managed-agents/overview | "Claude Managed Agents provides the harness and infrastructure for running Claude as an autonomous agent. Instead of building your own agent loop, tool execution, and runtime, you get a fully managed environment where Claude can read files, run commands, browse the web, and run code securely. The harness supports built-in prompt caching, compaction, and other performance optimizations..." | confirmed |
| Managed Agents core concepts: Agent (model/prompt/tools/MCP/skills), Environment (cloud or self-hosted sandbox), Session (running instance), Events (message exchange) | https://platform.claude.com/docs/en/managed-agents/overview | Table quoted verbatim in tool output above. | confirmed |
| Managed Agents is in **beta**; requires `managed-agents-2026-04-01` beta header; NOT currently eligible for Zero Data Retention or HIPAA BAA coverage because sessions are stateful and store data server-side | https://platform.claude.com/docs/en/managed-agents/overview | "Claude Managed Agents is in beta. All Managed Agents endpoints require the `managed-agents-2026-04-01` beta header." / "Because of this, Managed Agents is not currently eligible for Zero Data Retention (ZDR) or HIPAA Business Associate Agreement (BAA) coverage." | confirmed |

**Audit note:** CLAUDE.md's Architecture section doesn't reference the Agent SDK vs. Managed Agents distinction at all — this is current, additive ground truth for the audit rather than a correction to an existing claim.

---

## Unverifiable

The following claims from the project's CLAUDE.md / general exam-prep lore could **not** be confirmed on an official Anthropic domain during this pass. They should be treated as unverified until an official source is found — do not upgrade them to "confirmed" based on third-party prep material.

1. **"Citations give ~15% better recall when enabled."** The official citations page (platform.claude.com/docs/en/build-with-claude/citations) only states citations are "significantly more likely to cite the most relevant quotes" than prompt-based approaches — no percentage figure appears there. Could not locate this stat on any anthropic.com/claude.com property in this pass.
2. **Batch API "10,000 requests per batch" cap.** Current docs say the limit is 100,000 requests (or 256 MB). Either this figure is out of date, or it refers to some other constraint (e.g., a legacy limit, or a per-organization concurrent-batch limit) not found in the current batch-processing page. Flagged as a likely-stale figure rather than a true "unverifiable," but listed here because the specific "10,000 requests" claim itself has no current official source.
3. **"Batch API has no multi-turn tool calling" as a blanket restriction.** Current docs explicitly list "Multi-turn conversations" and tool use (including server tools) as supported in batch; the real restriction is narrower (no `stream`, no `store`/thread continuation params, no `max_tokens: 0`, no Fast mode). The blanket "no multi-turn tool calling" framing is not supported by current docs.
4. **Extended Thinking "manual budget_tokens deprecated on Claude 4.6."** Not directly checked in this pass (out of scope for the specific facts requested); flagging that it was not verified against an official page and should get its own audit pass if it matters.
