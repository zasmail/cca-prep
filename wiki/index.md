# Study Wiki — Index & Reading Map

*A synthesis wiki for Anthropic Applied AI interview prep + the CCA-F exam, built from ~46 talk transcripts and blog notes in [`../research/transcripts/`](../research/transcripts/) and [`../research/notes/`](../research/notes/).*

## The corpus in one paragraph

These eleven pages distill roughly four dozen sources — Anthropic engineering blog posts (Building Effective Agents, Context Engineering, Writing Tools, Code Execution with MCP, Demystifying Evals, Multi-Agent Research, Agent Skills), builder interviews (Boris Cherny across YC / Lenny's / Pragmatic Engineer / MAD Podcast / Latent Space, Cat Wu, Sid Bidasaria, Eleanor Dorfman, David Soria Parra on MCP origins), conference talks (Code w/ Claude, AIEWF MCP track, Prompting 101), and the Karpathy/Dwarkesh/Sholto-Trenton mental-model canon. The throughline: the industry has crossed an agentic inflection (Karpathy dates the coding break to ~Dec 2025; 70–90% of Anthropic's own code is now Claude-written), and the durable engineering discipline has moved *up the stack* — from writing code to designing the context, tools, evals, and programmatic guardrails that let non-deterministic agents run reliably with a human out of the hot loop. Everything here is one of five recurring problems: **context is scarce**, **tools are contracts with a non-deterministic reader**, **guarantees go in code not prompts**, **evals grade outcomes not paths**, and **knowledge should compound not re-derive.**

## The eleven pages

**[claude-code-workflows.md](claude-code-workflows.md)** — How Anthropic engineers actually work: Explore→Plan→Implement→Commit, plan-mode-first (~80% of Cherny's sessions), parallel sessions, self-verifying hill-climb loops, and fresh-context review. The human's job moved from writing code to closing verification loops.

**[context-engineering.md](context-engineering.md)** — Context as a finite resource with diminishing returns; context rot (n² attention) as the physical basis; compaction vs. NOTES.md vs. subagent isolation vs. just-in-time retrieval, plus prompt-caching economics. Token budget is the primary design constraint, not an afterthought.

**[enforcement-reliability.md](enforcement-reliability.md)** — The single most-tested idea: anything that must be *guaranteed* cannot live in a prompt — hooks, schema, gates, and stop_reason are deterministic; CLAUDE.md is advisory. Reliability compounds multiplicatively, and autonomy is *earned* through self-verifiability.

**[evals.md](evals.md)** — Evals as the infrastructure that separates regressions from noise: grade the outcome not the path, pass@k vs pass^k, code graders vs LLM-judge, start with 20–50 real failures, per-type/per-field metrics, read the transcripts. What lets you migrate models in days.

**[orchestration-patterns.md](orchestration-patterns.md)** — The five patterns (chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer), workflow-vs-agent, the complexity ladder, and why multi-agent's ~15x token cost is only repaid on decomposable, loosely-coupled work. Most "agents" should not be agents.

**[tool-design-and-mcp.md](tool-design-and-mcp.md)** — A tool is a contract, not an endpoint; never wrap an API 1:1; token economy as a constraint; code execution over sequential tool calls (150k→2k tokens); MCP as boring, load-bearing standardization (LSP for AI). Tool descriptions are among the highest-leverage things to tune.

**[skills-and-progressive-disclosure.md](skills-and-progressive-disclosure.md)** — Skills as organized folders (SKILL.md + scripts) loaded via three-tier progressive disclosure; descriptions as routers not docs; scripts beat prose for procedural steps; "build skills, not agents." The compounding, distributable layer of expertise on top of MCP connectivity.

**[memory-and-compounding.md](memory-and-compounding.md)** — LLMs have no episodic memory or consolidation, so memory is a write-back-and-retrieval problem; the compounding-vs-re-retrieval distinction (Karpathy's LLM-wiki vs classic RAG); three-layer architecture (immutable sources / mutable synthesis / schema); skills as procedural memory (Day 30 >> Day 1).

**[gtm-applications.md](gtm-applications.md)** — Applied AI in go-to-market: Claude as connective tissue between existing tools (not rip-and-replace); connectors+skills shipped as one "plug-in"; the outbox/human-send-gate pattern; matching gate strictness to blast radius. The clearest picture of what a forward-deployed/Applied AI engineer builds.

**[karpathy-mental-models.md](karpathy-mental-models.md)** — The metaphor canon: LLM-as-OS-kernel, Software 3.0 (context window as control surface), jagged intelligence gated by *verifiability not specifiability*, animals-vs-ghosts anti-anthropomorphism, the autonomy slider, and "decade of agents." The frame that explains why eval design is the scarce skill.

**[beyond-the-blueprint.md](beyond-the-blueprint.md)** — Current best practice beyond the July-2026 CCA-F blueprint: Tool Search/Programmatic Tool Calling, code-execution-with-MCP, `refusal` stop_reason, the Fable 5/Mythos 5/Sonnet 5 lineup, Agent SDK vs. Managed Agents, Routines, Skills-as-open-standard/Plugins, context engineering's official origin, and MCP's move to the Agentic AI Foundation. **This is the fast-moving page — verified as of 2026-07-16; re-check dates and numbers before citing them, this lineup shifts in weeks not quarters.**

## Contradictions worth knowing

Genuine cross-page tensions the sources do not fully reconcile — hold both sides and know the reconciling variable:

- **Human gate vs. auto-mode: is removing the human safer or riskier?** [enforcement-reliability.md](enforcement-reliability.md) insists on human checkpoints for high-stakes/regulated work and frames Bidasaria's "stop babysitting" as valid only where the agent self-verifies. [gtm-applications.md](gtm-applications.md) records Cherny arguing auto mode is *more* secure than human-in-the-loop because approval prompts cause fatigue (~1% prompt-injection success), while Dorfman holds a hard line that every customer-facing draft gets a human click. Reconciling variable: **blast radius / verifiability** — full-auto for internal, self-checkable actions; a gate for anything irreversible or customer-facing. But they genuinely weight the same tradeoff differently.

- **Compaction: "crude but effective" or lossy?** [context-engineering.md](context-engineering.md) and [memory-and-compounding.md](memory-and-compounding.md) carry both positions: the Claude Code team reports autocompact *outperformed* the elaborate memory systems they built, while the context-engineering blog treats single-session compaction as lossy and prefers structured NOTES.md for long-horizon build work. Reconciling variable: **task shape** (conversation vs. multi-hour build) — but the underlying bet on how much memory machinery is worth genuinely differs.

- **Sub-agents: durable pattern or context-window crutch?** [orchestration-patterns.md](orchestration-patterns.md) treats orchestrator-workers as a first-class pattern (90.2% lift on research evals). [tool-design-and-mcp.md](tool-design-and-mcp.md) and [enforcement-reliability.md](enforcement-reliability.md) record Cal Rueb calling sub-agents "a short-term workaround for today's limited context windows," and Cherny's "scaffolding buys only 10–20% and decays." One camp designs agent topologies; the other bets the model will subsume them.

- **How much scaffolding is load-bearing?** [claude-code-workflows.md](claude-code-workflows.md) has Cherny predicting plan mode is ~1 month from obsolescence (scaffolding decays), yet the same page's live-coding evidence shows autonomous loops became possible *only because of* concrete scaffolding (CI hooks, monitoring, auto-mode). [skills-and-progressive-disclosure.md](skills-and-progressive-disclosure.md) sharpens it: if scaffolding erodes, do skills erode too? (The skills camp says no — skills encode *domain* knowledge the model won't pretrain on.) Unsettled.

- **Big/curated context and where knowledge should live.** [context-engineering.md](context-engineering.md): keep ground truth external, pull just-in-time (in-context beats hazy weights). [memory-and-compounding.md](memory-and-compounding.md): Karpathy wants a small *cognitive core* with facts offloaded — "you can't think if you're looking things up constantly." Both agree model and memory should be *separated*; they disagree on how much must live inside the model.

- **Code graders vs. LLM-judge — brittleness cuts both ways.** Internal to [evals.md](evals.md) but load-bearing everywhere: "prefer deterministic code graders" collides with the same page's case studies (CORE-Bench 42%→95% after a grader fix) where rigid graders penalized correct answers. The hedge — read transcripts, calibrate, give partial credit — is not a clean rule.

## Suggested reading order (interview prep)

Front-load the two highest-leverage, most-tested domains, then breadth, then framing:

1. **[enforcement-reliability.md](enforcement-reliability.md)** — the #1 tested concept (guarantee vs. preference) and the mental spine for every other page.
2. **[context-engineering.md](context-engineering.md)** — the scarce resource that shapes tools, retrieval, orchestration, and CLAUDE.md.
3. **[tool-design-and-mcp.md](tool-design-and-mcp.md)** — tools-as-contracts and the token economy; pairs directly with #2.
4. **[evals.md](evals.md)** — how self-verification gets measured; the skill Karpathy calls scarce.
5. **[orchestration-patterns.md](orchestration-patterns.md)** — the five patterns and the workflow-vs-agent decision.
6. **[skills-and-progressive-disclosure.md](skills-and-progressive-disclosure.md)** — the packaging primitive and "build skills, not agents."
7. **[memory-and-compounding.md](memory-and-compounding.md)** — compounding vs. re-retrieval; ties skills + context together.
8. **[claude-code-workflows.md](claude-code-workflows.md)** — how it all shows up in a working day; great for "how do you actually work" questions.
9. **[gtm-applications.md](gtm-applications.md)** — read right before the interview; this is the concrete Applied AI job.
10. **[karpathy-mental-models.md](karpathy-mental-models.md)** — the framing layer; skim last to have vivid metaphors on tap.

Then read **[top-20-things-to-internalize.md](top-20-things-to-internalize.md)** as the night-before drill and **[applied-ai-interview-prep.md](applied-ai-interview-prep.md)** for role-specific synthesis.
