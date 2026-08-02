---
title: MCP — Origins and Requests For Startups
speaker: Theo Chu (Product Manager, Anthropic MCP)
source: https://www.youtube.com/watch?v=x-8pBqWiTzk
conference: AIEWF 2025
retrieved: 2026-07-16
themes:
  - context-engineering
  - tool-design-mcp
  - orchestration
  - claude-code-workflows
  - gtm-applications
  - enforcement-reliability
---

## Core Claims

1. **Context window bottleneck.** Engineers constantly copy-paste context from external systems (Slack, Sentry, error logs) manually into the conversation window.

2. **Model agency solves scaling.** The core insight: give models the ability to autonomously reach into the external world and pull context/actions themselves.

3. **Standardized open protocol is mandatory.** Closed ecosystems require partnerships/BD to scale; standardized protocols unlock ecosystem growth.

4. **Tool calling + reasoning models made the timing right.** Reasoning models and improved tool-calling reliability made autonomous agent behavior viable.

5. **Adoption comes through builder agency.** Ecosystem adoption happened only after tool developers (Cursor, VS Code) let engineers build MCPs for their own workflows.

6. **Server-heavy ecosystem design.** MCP is architected assuming many more servers than clients; complexity is pushed to clients to keep servers simple.

7. **Three-user design principle.** MCP servers must account for three distinct users: end users, client developers, AND the model itself.

8. **Skepticism defeated by experience.** Early questions ("Why not just tool calling?" "Why open source?") only dissolved when builders shipped their own MCPs.

9. **Higher-quality means prompt-aware design.** Wrapping 1:1 API endpoints is wrong; good MCPs design tools around actual user workflows and model prompts.

10. **Vertical expansion is the scalability play.** Initial dev-tools focus is limiting; opportunity is in sales, finance, legal, education, etc.

## Patterns & Frameworks

- **Three-User MCP Design** — Account for end user, client developer, and model as co-equal design constraints; shape tool schemas around what the model needs to reason effectively.
- **Ecosystem-First Scaling** — Favor server simplicity over client simplicity; complexity burden serves builder velocity and network effects.
- **Use-Case-Driven Tool Schema** — Design tools backward from: (1) end-user prompts, (2) model reasoning needs, (3) then API endpoints.
- **Community-Driven Spec Evolution** — OAuth fixes, transport layer changes driven by community contribution; standards harden through real-world usage feedback.
- **Adoption via Self-Interest** — Builders adopt when they can automate their own workflows; ecosystem grows from internal adoption outward.

## Numbers & Specifics

- **Launch timeline:** Concept (mid-2024) → Internal hack week (November 2024) → Open source release (November 2024) → Tool adoption (Cursor, VS Code, SourceGraph) → Industry adoption (Google, Microsoft, OpenAI).
- **Roadmap weighting:** 80% on building more/higher-quality servers, 10% on server tooling, 10% on other opportunities.
- **Transport evolution:** SSE → Streamable HTTP (enables bidirectional agent-to-agent communication).
- **Key protocol additions:** Remote MCPs, OAuth spec corrections, elicitation (server-initiated user questions), registry API (for model-driven discovery).
- **Design constraint:** Optimize for server simplicity even when it increases client complexity.

## Quotes

> "Claude or any LLM could just kind of climb out of its box, reach out into the real world and bring that context and those actions to the model." (line 65–67)

> "Model agency was the biggest thing that was stopping LLMs from actually reaching the next stage of usefulness and intelligence." (line 91–93)

> "What's MCP? or even worse, what's MPC?" (line 127–129) — on initial market skepticism.

> "You want to think about what are the use cases that your end users are going to have... ultimately what are the tools that you then need to expose to the model to enable the model to respond correctly." (line 358–364)

> "Servers are going to be the vast majority of the ecosystem. There will of course be a lot of clients as well, but the order of magnitude of servers is going to outweigh the order of magnitude of clients." (line 377–382)

## Applied AI Relevance

- **Model agency is architectural.** Treat autonomous tool selection as a first-class design constraint, not a bonus feature. This changes how you structure agent loops, error handling, and context flow.
- **Three-user principle generalizes.** When designing tools/APIs for models, always audit for the model as a user: What does the model need to reason? What schema reduces hallucination? What tool boundaries prevent cascade failures?
- **Standards win through builder adoption, not features.** Anthropic's bet is that MCPs become standard because engineers can build for their own pain first; platform features follow adoption, not vice versa.
- **Security and observability are now critical constraints.** Server-heavy architecture means security, auditing, observability, and deployment tooling must be first-class concerns, not afterthoughts.

---
**Word count:** 560 | **Effort level:** Medium depth (suitable for exam study + GTM context)
