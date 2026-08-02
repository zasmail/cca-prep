# Applied AI Interview Prep

*Role-specific synthesis for Anthropic Applied AI / forward-deployed engineer interviews, drawn from the whole corpus. Pair with [top-20-things-to-internalize.md](top-20-things-to-internalize.md) for facts and [index.md](index.md) for the map.*

---

## What an Applied AI engineer at Anthropic actually does

The clearest picture comes from the GTM and product-engineering talks. The role is **forward-deployed synthesis engineering**: you sit between a customer's (or an internal team's) existing systems and Claude, and you build the layer that makes non-deterministic agents reliable enough to deploy. Concretely, the work looks like:

- **Integrate against the system of record, don't replace it.** Eleanor Dorfman rebuilt Anthropic's sales org keeping the whole stack (Salesforce, Clay, Gong, Ironclad, Slack, Lean Data) and using Claude as "the connective tissue that makes the tools we've already bought talk to one another" ([gtm-applications.md](gtm-applications.md)). Your deliverable is the synthesis/orchestration layer, not a new app.
- **Ship connectors + skills as one atomic unit.** The "sales plug-in" bundles six MCP connectors with five encoded skills (morning brief, call prep, follow-up, competitive intel, create-asset) and hands it to every new rep on day one. You test the *integration*, not tools in isolation ([gtm-applications.md](gtm-applications.md)).
- **Design the human gate to match blast radius.** Claude drafts; a human clicks send on anything that leaves the building (the outbox pattern); internal, self-verifiable actions go full-auto. The send-gate is *programmatic*, not a prompt asking the model to be careful ([gtm-applications.md](gtm-applications.md), [enforcement-reliability.md](enforcement-reliability.md)).
- **Author skills from observed eval gaps, not imagination.** Run the agent on real production tasks, find where it fails, write a skill to fill that exact gap, watch how Claude uses it, refine the naming/description, repeat ([skills-and-progressive-disclosure.md](skills-and-progressive-disclosure.md)).
- **Ground agents in the customer's reality first.** In product engineering, Claude reads the design doc (`EXCEL_RENDERER_DESIGN.md`) and explores the codebase before implementing, and validates against *live* product state via Playwright MCP — cutting onboarding from weeks to hours ([claude-in-product-engineering](../research/notes/claude-in-product-engineering.md)).
- **Build the eval harness that lets you migrate models in days.** Start with 20–50 real failures, layer automated evals in CI with production monitoring, and give the suite a long-term owner ([evals.md](evals.md)).

The recurring cultural claim: adoption is an **interface-design problem**. Non-technical operators became "GTM architects" only when the entry point collapsed to three fields (name, role, context doc) — map the workflow first, then simplify the interface; don't expose config knobs ([gtm-applications.md](gtm-applications.md)).

## The vocabulary they use (speak it fluently)

- **Context engineering** — "optimizing which tokens occupy the limited context window during inference"; distinct from prompt engineering because it's *iterative, every turn*.
- **Context rot** — gradual accuracy decay as the window fills (n² attention).
- **Progressive disclosure** — three-tier loading: metadata → body → bundled files.
- **Just-in-time retrieval** — fetch via tools/references at runtime rather than pre-loading blobs; **hybrid** is usually the sweet spot.
- **Compaction / autocompact** — model self-summarizing prior turns near the window limit; "crude but effective."
- **Unhobbling** — deleting bespoke tools in favor of general abstractions (BASH, file I/O) as models improve.
- **Poka-yoke** — error-prevention by design (absolute file paths eliminate a class of bugs).
- **pass@k vs pass^k** — ≥1 success in k vs. succeeds *every* time; research vs. customer-facing.
- **Nines of reliability** — long-horizon failure from multiplicative step-chaining.
- **Grade the outcome, not the path** — score end-state, not trajectory.
- **LLM-as-judge with per-dimension rubric** + calibration against humans + an "Unknown" escape hatch.
- **Orchestrator-workers** — coordinator owns *all* inter-agent communication.
- **Evaluator-optimizer** — generate/critique loop in *separate sessions*.
- **Workflow vs. agent** — predefined code paths vs. model-directed process.
- **Tool-as-contract** / **descriptions as onboarding docs** / the "smart-but-lazy 12-year-old" description test.
- **Code Mode / code execution over tool calls** — MCP servers as a typed code API; filter before the model sees results.
- **Sampling** — server requests completions from the *client's* model (MCP's most powerful, least-used primitive).
- **Skills vs. agents** — "code is all we need"; skill = organized folder; **Day 30 >> Day 1**.
- **Software 3.0 / LLM-as-OS-kernel / animals-vs-ghosts / autonomy slider / jagged intelligence** — Karpathy framing.
- **Cognitive core + external memory** — small reasoning core, facts offloaded to retrieval.
- **Diffusion vs. capability** — two independent steep exponentials on different clocks; ~6-month enterprise adoption lag is friction, not a capability ceiling (Dario).
- **Internal-first / dogfooding** — build and use it alongside model development; "get tacit knowledge into written form" so Claude can use it. Process/workflow restructuring — not model access — is the durable moat.
- **Context editing + memory** — clear stale tool results, store context externally; +39% on internal evals (a capability lever, not hygiene).
- **Dreaming / memory reconsolidation** — scheduled off-task pruning of contradictory memories; shipped overnight on Claude.ai, background on managed agents.
- **Character as enforcement** — for unsupervised judgment no rule anticipates, the model's values *are* the reliability mechanism; evaluated as a hybrid quantitative + transcript-reading eval.
- **Self-recovery / outcome optimization** — the agent detects its own divergence and iterates to a specified outcome/metric rather than a prescribed output structure.
- **The loop** — cron/event-triggered recurring agent that refreshes context and works unattended; "loops are the future" (Cherny).

## Likely interview themes

1. **"Design an agent for X — walk me through it."** Expect a customer-facing or internal-workflow prompt. Anchor on: (a) is it a workflow or an agent; (b) what's the verification signal; (c) where does the human gate sit (blast radius); (d) tool/context budget; (e) how you'd eval it. Climb the complexity ladder — start with the simplest thing that could work.
2. **Guarantee vs. preference.** They will hand you a "must never happen" requirement (never refund >$X, never send without approval). Correct answer is always programmatic — hook/schema/gate — never "I'll word the prompt carefully."
3. **Reliability of long-horizon runs.** Nines-of-reliability math, verification gates between steps, resumable checkpoints, why a better final prompt doesn't fix a compounding chain.
4. **Evals.** How you'd measure success without a golden path; pass@k vs pass^k for *this* product; per-type/per-field over aggregate; what a 0% score tells you; why you read transcripts.
5. **Context/token economics.** Context rot, when to reach for subagents (~15x cost) vs. NOTES.md vs. compaction; code execution to cut 150k→2k tokens.
6. **Tool/MCP design.** Why never wrap an API 1:1; ≤5 tools in context; namespacing; actionable errors; MCP as standardization.
7. **Adoption / forward-deployed judgment.** How you'd get a non-technical team to actually use this (collapse the interface); connectors+skills as a unit; ROI framing over cost-cutting. Know the **diffusion story**: enterprise adoption lags raw capability ~6 months on institutional friction (legal, procurement, security) while individual devs move faster — so land **individual-first** (make one operator "exponentially more powerful"), then scale to multi-team, and don't mistake adoption friction for a capability ceiling ([gtm-applications.md](gtm-applications.md), [dwarkesh-dario](../research/notes/dwarkesh-dario.md), [behind-craft-jess-yan](../research/notes/behind-craft-jess-yan.md)).
8. **Model-agnostic framing.** They may probe whether you over-engineer for today's model — know the "scaffolding decays / unhobbling" tension and take a defensible position.

## Strong opinions worth holding

Interviews reward a *position* plus the reconciling variable, not fence-sitting:

- **"If it must be guaranteed, it goes in code. Full stop."** The most defensible hill; it's the #1 tested idea and the cleanest signal of maturity.
- **"Autonomy is earned through verifiability."** Removing the human is safe exactly where the agent can check itself — and that's a *design target*, not a given. This lets you reconcile the auto-mode-vs-human-gate contradiction gracefully.
- **"Most agent projects should be workflows."** Reaching for multi-agent first is an anti-pattern; its ~15x cost is only repaid on decomposable, loosely-coupled work.
- **"Grade outcomes, not paths — and read the transcripts."** Signals you've actually run evals, not just read about them.
- **"Build skills, not agents — the scaffolding is universal now."** A forward-looking take, but hold the caveat: skills earn their durability by encoding *domain/procedural* knowledge the model won't pretrain on.
- **"Adoption is an interface problem."** Shows you think about deployment, not just model behavior — the essence of forward-deployed work.
- **Anti-anthropomorphism (Karpathy's ghosts).** Reason about behavior empirically via evals, not about what the model "wants." Keeps you credible on both capability hype and safety.

## Questions to ask interviewers that signal depth

- "Where does the Applied AI team draw the line on how much scaffolding to build vs. waiting for the next model? Cherny frames scaffolding as buying only 10–20% and decaying — how do you decide what's load-bearing *now*?"
- "For customer deployments, how do you decide the blast-radius boundary — which actions go full-auto vs. keep a human send-gate?"
- "When a customer's task isn't cleanly verifiable, how do you construct a proxy reward signal so an agent can still self-check?"
- "How do you handle eval ownership over time so the suite doesn't rot — is there a dedicated owner, and how do graders avoid overfitting to the previous model's output style?"
- "Where are you seeing the connectors-vs-skills boundary settle in practice — is MCP the durable primitive or the connectivity layer beneath skills-as-expertise?"
- "For long-horizon customer agents, what's the current state of resumable checkpointing and observability — is it still mostly filesystem-and-hooks, or is there a scaling permission/topology story yet?"
- "How much of a typical engagement is prompt/context work vs. plumbing/integration vs. eval-building? Where do most deployments actually get stuck?"

## 60-second self-intro spine (adapt to your background)

"The shift I care about is that the durable engineering discipline moved up the stack — from writing code to designing the context, tools, evals, and *programmatic* guardrails that make non-deterministic agents reliable. My default questions on any agent problem are: is this a workflow or an agent, what's the verification signal, and where does the human gate sit relative to blast radius. I think the highest-leverage Applied AI work is connective-tissue integration — owning the synthesis layer over a customer's existing stack — and getting the interface simple enough that non-technical operators actually adopt it."
