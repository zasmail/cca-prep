# Tool Design & MCP

## The thread

Every builder in this corpus converges on one reframe: **a tool is not an API endpoint — it is a contract with a non-deterministic reader.** Deterministic software returns the same output for the same input; an agent may misread a tool, hallucinate its arguments, or ignore it entirely. So tool specs deserve the same engineering rigor as prompts. Anthropic reports investing *more* effort tuning tools than tuning the overall prompt during SWE-bench work ([blog-building-effective-agents](../research/notes/blog-building-effective-agents.md)), and tool descriptions are named "one of the highest-leverage things you can optimize" ([blog-writing-tools](../research/notes/blog-writing-tools.md)). The anti-pattern everyone names by hand: wrapping an existing REST API 1:1 and exposing every endpoint as a tool — "you're going to get the worst results you can possibly imagine" (David Kramer, Sentry, [aiewf-2025-mcp-track](../research/notes/aiewf-2025-mcp-track.md)). Good tools are designed *backward* from user workflows and model reasoning, not forward from the API surface ([mcp-origins](../research/notes/mcp-origins.md)).

The second thread is **token economy as a first-class constraint.** Agents have real, measurable context limits, unlike near-unlimited machine memory. That reframes fewer-but-focused tools, semantic identifiers over UUIDs, pagination/filtering/truncation with sensible defaults, and — the biggest lever at scale — moving work *out* of the context window entirely via code execution ([blog-code-execution-mcp](../research/notes/blog-code-execution-mcp.md)). See [context-engineering](context-engineering.md) for the demand side of this budget.

The third thread is **MCP as boring, load-bearing standardization.** MCP (open-sourced Nov 2024) solves the M×N integration problem the way LSP solved IDE-language integration — a shared JSON-RPC protocol so every client and every context provider speak once ([a16z-mcp-soria-parra](../research/notes/a16z-mcp-soria-parra.md), [sed-mcp-soria-parra](../research/notes/sed-mcp-soria-parra.md)). "It's not a competitive advantage to be really good at making Google Drive talk to your app... Being boring on stuff like this is good" ([remote-mcps-lessons](../research/notes/remote-mcps-lessons.md)). The value is standardization across clients, not conceptual novelty — function calling already existed ([stytch-agent-ready-ep8](../research/notes/stytch-agent-ready-ep8.md)).

## Patterns

**Tool-as-contract / defensive design** — Design assuming the agent will misread or misuse. Use error-prevention (poka-yoke): requiring absolute file paths instead of relative ones eliminated an entire class of working-directory bugs. When you must *guarantee* a behavior, enforce in code, not prose (see [enforcement-reliability](enforcement-reliability.md)). [blog-building-effective-agents](../research/notes/blog-building-effective-agents.md), [blog-writing-tools](../research/notes/blog-writing-tools.md).

**Descriptions as onboarding docs** — Write parameter names and descriptions like documentation for a new engineer joining your team. Litmus test: "Could a smart-but-lazy 12-year-old figure out this tool from its description alone? If yes, a frontier model probably can too." Use when authoring any tool. [stytch-agent-ready-ep8](../research/notes/stytch-agent-ready-ep8.md), [blog-building-effective-agents](../research/notes/blog-building-effective-agents.md).

**Namespacing** — Group tools under consistent prefixes/suffixes by service or resource so the agent can disambiguate overlapping tools. Prefix vs. suffix choice shows up as *measurable* eval differences. Use when you have many similar tools. [blog-writing-tools](../research/notes/blog-writing-tools.md).

**Actionable errors & token-conscious responses** — Return semantic identifiers (names, readable types) over opaque ones (UUIDs, MIME types). Truncation messages should steer the agent toward a better search, not cut silently. Errors should be actionable, not opaque codes. Exam form: errors need `isError`, `errorCategory`, `isRetryable` fields. [blog-writing-tools](../research/notes/blog-writing-tools.md), CLAUDE.md anti-pattern #6.

**Eval-driven iteration on tools** — Prototype → run realistic multi-step evals against real data → read reasoning traces AND raw transcripts → refine (collaboratively, using an agent to review its own transcripts). Metric patterns diagnose fixes: redundant calls → missing pagination; bad parameters → unclear descriptions. Track accuracy, runtime, token usage, error rate. [blog-writing-tools](../research/notes/blog-writing-tools.md). See [evals](evals.md).

**Code execution with MCP ("Code Mode")** — Represent MCP servers as typed files in a virtual filesystem the agent writes code against, instead of preloading every tool schema. Loops, conditionals, filtering, and joins run in the sandbox; only results the agent explicitly returns hit context. Use at scale (many servers, large intermediate payloads, PII). Cloudflare validated the same pattern independently as "Code Mode." [blog-code-execution-mcp](../research/notes/blog-code-execution-mcp.md).

**Progressive disclosure of tools** — Load tool definitions on demand via a `search_tools`-style call returning graduated detail (name → name+description → full schema) rather than dumping all upfront. Enables 5,000+ tool marketplaces without upfront model knowledge. Overlaps with [skills-and-progressive-disclosure](skills-and-progressive-disclosure.md). [blog-code-execution-mcp](../research/notes/blog-code-execution-mcp.md), [aiewf-2025-mcp-track](../research/notes/aiewf-2025-mcp-track.md).

**Scripts over tools (skills)** — Embedded, self-documenting code in a skill folder beats a static tool description that decays and locks the agent in. "We think code is all we need." Use for reusable procedural knowledge. [dont-build-agents-build-skills](../research/notes/dont-build-agents-build-skills.md).

**MCP gateway / pit of success** — Single internal entry point handling auth, routing (internal/external), rate limiting, audit, and prompt-injection filtering. Make the right way the easiest way so teams adopt it without enforcement. Centralizes org-wide security at one choke point. [remote-mcps-lessons](../research/notes/remote-mcps-lessons.md), [aiewf-2025-mcp-track](../research/notes/aiewf-2025-mcp-track.md).

**Sampling as composition** — A server requests completions from the *client's* configured model instead of bundling its own API key/SDK. Enables model-agnostic, nested agent chains and cost-sharing. MCP's most powerful, least-used primitive. [a16z-mcp-soria-parra](../research/notes/a16z-mcp-soria-parra.md), [sed-mcp-soria-parra](../research/notes/sed-mcp-soria-parra.md).

## Numbers & rules of thumb

- **Tool-count lore, handled carefully:** the talks cite "≤5 tools per agent, 18+ degrades selection" (LangChain research, [aiewf-2025-mcp-track](../research/notes/aiewf-2025-mcp-track.md)) — but per CLAUDE.md anti-pattern #8, treating that as a hard cap **is the anti-pattern**: it was a useful pre-Nov-2025 heuristic, superseded by Tool Search Tool + progressive disclosure. The durable claims are the three selection-killers — too many tools *in context*, tool repetition, mixed domains/instructions — which argue for curation per context window, not a fixed ceiling.
- **150,000 → 2,000 tokens (~98.7% reduction)** on a Drive-to-Salesforce workflow via code execution ([blog-code-execution-mcp](../research/notes/blog-code-execution-mcp.md)).
- Loading all tool schemas upfront can cost **hundreds of thousands of tokens before the agent starts** ([blog-code-execution-mcp](../research/notes/blog-code-execution-mcp.md)).
- Chained tool calls push each intermediate result through context **twice** (e.g., a transcript read then written elsewhere) ([blog-code-execution-mcp](../research/notes/blog-code-execution-mcp.md)).
- Progressive tool disclosure returns **3 detail levels**: name → name+description → full schema ([blog-code-execution-mcp](../research/notes/blog-code-execution-mcp.md)).
- MCP: open-sourced **Nov 2024**; JSON-RPC; **3 primitives** (tools, resources, prompts) + sampling; SDKs in Python, TypeScript, C#, Java, Kotlin, Go ([sed-mcp-soria-parra](../research/notes/sed-mcp-soria-parra.md)).
- Ecosystem is **server-heavy** by design — orders of magnitude more servers than clients; complexity pushed to clients ([mcp-origins](../research/notes/mcp-origins.md)).
- "Smart-but-lazy 12-year-old" description test ([stytch-agent-ready-ep8](../research/notes/stytch-agent-ready-ep8.md)).
- Two proven full-autonomy domains today: **coding assistants + deep research**; customer support stays human-in-loop ([stytch-agent-ready-ep8](../research/notes/stytch-agent-ready-ep8.md)).

## Where speakers disagree

**More tools vs. richer tools.** The dominant view says constrain the menu — models are "smart but lazy," fewer focused tools win ([stytch-agent-ready-ep8](../research/notes/stytch-agent-ready-ep8.md), [blog-writing-tools](../research/notes/blog-writing-tools.md)). But the code-execution and dynamic-discovery camp argues you *can* expose thousands of tools if you gate them behind progressive disclosure so only relevant ones enter context ([blog-code-execution-mcp](../research/notes/blog-code-execution-mcp.md), [aiewf-2025-mcp-track](../research/notes/aiewf-2025-mcp-track.md)). The reconciliation: few tools *in context at once*, many available *on demand* — but they genuinely disagree on whether curation or infrastructure is the primary fix.

**Tools vs. skills as the right abstraction.** Zhang/Murag argue tool descriptions "decay, become ambiguous, and lock agents in," and scripts in skill folders are strictly better ([dont-build-agents-build-skills](../research/notes/dont-build-agents-build-skills.md)). MCP-centric speakers treat well-designed tools as the durable primitive and layer skills alongside ([aiewf-2025-mcp-track](../research/notes/aiewf-2025-mcp-track.md)). Soria Parra splits the difference: "tools are likely necessary for agents but I'm not convinced they're sufficient" ([sed-mcp-soria-parra](../research/notes/sed-mcp-soria-parra.md)).

**Sub-agents: durable pattern or context-window crutch?** Rueb frames sub-agents as "a short-term workaround for today's limited context windows," likely unnecessary as capacity grows ([stytch-agent-ready-ep8](../research/notes/stytch-agent-ready-ep8.md)) — a live tension with orchestrator-worker advocates (see [orchestration-patterns](orchestration-patterns.md)).

**Tool-poisoning defense.** Signed-hash verification of tool descriptions vs. trusted registries: hashing fails because a compromised server publishes its own compromised hash; the durable answer is a vetted registry — but that reintroduces slow app-store-style gatekeeping ([stytch-agent-ready-ep8](../research/notes/stytch-agent-ready-ep8.md)).

## Interview-ready takes

1. **"A tool is a contract with a non-deterministic reader, so I write descriptions like onboarding docs and enforce guarantees in code."** Prose can be ignored; when a rule must hold, it goes in a hook or schema, not the description. Grounded in [blog-writing-tools](../research/notes/blog-writing-tools.md) + the enforcement principle in CLAUDE.md.

2. **"Never wrap an API 1:1 — design tools backward from user workflows."** Raw endpoints force the model to waste tokens re-deriving call composition. Design from (1) end-user prompts, (2) model reasoning needs, then (3) the API. [mcp-origins](../research/notes/mcp-origins.md), [aiewf-2025-mcp-track](../research/notes/aiewf-2025-mcp-track.md).

3. **"At scale, code execution beats sequential tool calls."** Preloading schemas and routing every intermediate result through context is the real cost driver; represent MCP servers as a typed code API and you cut 150K tokens to 2K. Weigh against sandbox/monitoring overhead. [blog-code-execution-mcp](../research/notes/blog-code-execution-mcp.md).

4. **"MCP's value is boring standardization, not novelty."** It's LSP for AI integrations. Standardize internally behind a gateway to centralize auth, rate limiting, and prompt-injection filtering at one choke point. [remote-mcps-lessons](../research/notes/remote-mcps-lessons.md), [a16z-mcp-soria-parra](../research/notes/a16z-mcp-soria-parra.md).

5. **"Tool design is eval-driven, and the agent is your best debugger."** Read reasoning traces and raw transcripts; let redundant calls and bad parameters tell you what's missing. Anthropic tuned tools harder than prompts on SWE-bench. [blog-writing-tools](../research/notes/blog-writing-tools.md), [blog-building-effective-agents](../research/notes/blog-building-effective-agents.md).
