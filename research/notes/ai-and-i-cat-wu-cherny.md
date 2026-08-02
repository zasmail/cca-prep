---
title: How to Use Claude Code Like the People Who Built It
speaker: Cat Wu, Boris Cherny
source: https://www.youtube.com/watch?v=IDSAMqip6ms
themes:
  - claude-code-workflows
  - tool-design-mcp
  - orchestration
  - enforcement-reliability
  - skills
---

## Core Claims

1. **Terminal-as-paradigm shift**: Removing the text editor and making bash the primary interface was not intentional but emerged from prototyping—Claude Code has access to everything an engineer does at the terminal, with nothing in between.

2. **Bash over custom tools**: Despite having custom tools, bash remains superior because Claude models are already excellent at bash, reducing tool proliferation from dozens to ~12, lower cognitive load, and easier deployment.

3. **Dual-use tool design**: Elegant design for humans translates well to models—tools designed to make sense to engineers naturally make sense to Claude, eliminating the need for separate model-optimized APIs.

4. **Latent demand drives product**: Build hackable, open-ended systems, observe how users abuse them for unintended use cases, then productize that demand (Facebook Dating from 60% opposite-gender profile views; Marketplace from 40% sell posts).

5. **Scaffolding gets subsumed by models**: Features built to support current model limitations (e.g., plan mode) will eventually become unnecessary as models improve—the boundary of what needs explicit scaffolding shifts outward with each generation.

6. **Hook-based determinism over prompts**: Critical behaviors must be enforced programmatically via hooks and prereqs, not prompt guidance—hooks can block; prompts can be ignored.

7. **Ant-fooding as signal engine**: Internal dogfooding at 70-80% adoption among Anthropic technical staff provides rapid feedback (one post every 5 minutes on internal channels) and drives product decisions.

8. **Multi-agent uncorrelated context windows**: Spawning separate sub-agents with independent context (e.g., "me vs. auditor" negotiating expenses) produces better results than single-agent solutions due to non-overlapping attention.

9. **Compounding engineering pattern**: Each feature should make the next feature easier to build by codifying learnings into prompts, slash commands, and hooks—productivity per engineer increased ~70% despite 2x headcount at Anthropic.

10. **Demo culture over docs**: Shifting from documentation to 15-second demos as the primary currency of communication—what's hard to explain in prose becomes obvious when shown.

## Patterns & Frameworks

**Latent demand** — Build systems hackable enough that users discover uses you didn't anticipate, then productize the demand you observe.

**Compounding engineering** — Each feature codifies learnings into rules/prompts/hooks so the next engineer gets "on-ramp" context automatically, accelerating subsequent feature velocity.

**Uncorrelated context windows** — Dispatch independent sub-agents without shared context (e.g., opponent negotiation) to avoid confirmation bias and improve solution quality.

**Scaffolding regression** — Temporary features (plan mode, extra prompt tokens) that support current model limits will be subsumed into base model capability; build for premium experience, expect deprecation in 3 months.

**Progressive disclosure** — Hide complexity until relevant; show tips contextually; let users drill into raw transcript (Ctrl+O) only when needed; model teaches usage via demonstrations.

**Shift-tab interaction pattern** — Single keybinding for toggling autonomy level (plan mode, auto-accept, extended thinking) creates consistent mental model across features.

## Numbers & Specifics

- ~12 tools currently in Claude Code (down from dozens); add/remove ~weekly
- 70-80% of Anthropic technical staff use Claude Code daily
- Internal feedback channel: ~1 post every 5 minutes on usage/issues
- Anthropic doubled in size since January 2026; productivity per engineer increased ~70%
- Metric: PRs as primary measure (plus latent feature-attempt signals)
- Autonomy duration: Current model ~30 hours continuous task execution; next model expected ~days
- System prompt reduction: Deleted ~2,000 tokens from system prompt for Sonnet 4.5 vs. Opus 4.1 (model capability absorbed scaffolding)
- Haiku 4.5 preferred for cost efficiency; north star remains Sonnet 4.5 (premium positioning)
- Plan mode: 2-3x success rate improvement when aligned first vs. one-shot
- Vector embedding: Internal shift from embeddings (maintenance burden, security surface) to agentic search (cleaner deployment)

## Quotes

1. "Everything you can do, Claude Code can do. There's nothing in between." — Boris Cherny on terminal-as-everything design

2. "If you can solve your own problem, it's much more likely you're solving the problem for others." — Boris Cherny citing YC wisdom on dogfooding

3. "The model just wants to use tools. We gave it bash and it just started using bash." — Boris Cherny on first revelation of agentic bash

4. "Latent demand: build a product hackable enough that people abuse it for other use cases, then you build for that because you know there's demand." — Boris Cherny on product philosophy

5. "We hope that we will get rid of it in three months." — Cat Wu on intentional deprecation strategy for scaffolding features

## Applied AI Relevance

- **Programmatic enforcement over prompts**: When designing agent systems for production, implement critical behaviors as hooks/prerequisites/schema validation, not narrative instruction—prompts fail under pressure; code doesn't.

- **Agentic search + bash > embeddings**: For codebase reasoning in multi-turn agents, prefer models with tool access (bash + file read) over pre-computed vector indices; easier to maintain, deploy, and reason about security boundaries.

- **Dual-use tool semantics**: When building tool sets for human + model consumption, optimize for human UX first; well-designed human APIs almost always work for models due to clarity and consistency.

- **Sub-agent independence as quality lever**: For sensitive reasoning tasks (conflict resolution, auditing, negotiation), dispatch separate agents without context sharing to avoid echo-chamber confirmation bias—uncorrelated windows often outperform centralized reasoning.
