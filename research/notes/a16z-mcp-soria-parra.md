---
title: MCP Co-Creator on the Next Wave of LLM Innovation
speaker: David Soria Parra (Anthropic, MCP co-creator)
source: https://a16z.com/podcast/mcp-co-creator-on-the-next-wave-of-llm-innovation/
published: 2025-05-02
themes:
  - tool-design-mcp
  - context-engineering
  - orchestration
  - gtm-applications
---

# MCP: Protocol Design for Open AI Integration

## Core Claims

1. MCP solves the M×N integration problem for AI applications by defining a standardization layer, analogous to how API schemas unified SaaS integrations.
2. Tool calling is the dominant primitive developers use, but sampling, resources, and prompts are equally powerful but underutilized.
3. MCP servers can chain into other MCP servers, enabling indefinitely deep (though practically shallow) graphs of composed multi-tool agent systems.
4. Authorization (can a client access a resource?) is the critical unlock for professional, remote, account-bound MCP servers; authentication (who is this?) is secondary in current priority.
5. Protocol boundaries should align with trust boundaries (e.g., payment system access) rather than with task complexity.
6. Sampling lets an MCP server remain model-agnostic by delegating inference to the client's configured model, avoiding bundled SDKs/API keys.
7. Resources are "application-driven"—the client layer (not the model) decides whether to inject directly or run retrieval over them.
8. MCP started with stdio + JSON-RPC (LSP-inspired) and is evolving toward HTTP for remote servers while maintaining transport independence.

## Patterns & Frameworks

- **M×N standardization**: Protocol > bespoke integrations (generalized from SaaS API history)
- **Trust boundaries over complexity**: Use protocol seams where security/isolation demands them, not where task logic is complex
- **Primitive layering**: Tool (model-driven), Sampling (model-agnostic inference), Resource (app-driven context), Prompt (user-driven template)
- **Agency definition**: A system has agency when it reacts to the outcome of its own prior step (Soria Parra)
- **Server composition**: Servers as clients to downstream servers enables indefinite depth (practically: shallow hierarchies)

## Numbers & Specifics

- **November 2024**: MCP open-sourced
- **April 2024**: Soria Parra joined Anthropic (internal tooling)
- **Co-creator**: Justin Spahr-Summers (Claude Desktop), Soria Parra (Zed)
- **Authorization partners**: Microsoft, Okta, AWS (security/identity experts)
- **Transport**: JSON-RPC on stdio → HTTP evolution; LSP-inspired
- **First real prototype**: Puppeteer/browser-control (strong demo payload)
- **First useful production servers**: GitHub, Postgres (mundane but genuine wins)

## Quotes

- "Build a protocol for it" (Soria Parra's answer to M×N frustration)
- MCP aims to be "boring-on-purpose" (open protocol design principle)
- "Trust boundaries rather than task complexity" (where protocol seams matter)
- "The moment a system reacts to the outcome of its own prior step, it has agency" (Soria Parra's agent definition)
- "Application-driven" context (resources decision principle: client, not model, owns injection strategy)

## Applied AI Relevance

- **Primitive selection matters**: Choosing the right primitive (tool, sampling, resource, prompt) is key to building reusable, robust integrations; sampling in particular unlocks model-agnostic nested workflows.
- **Sampling for delegation**: When you need a downstream server to run its own reasoning without leaking inference control (API key exposure, cost control), use sampling; it's underutilized because client support is incomplete.
- **Authorization as unlock**: OAuth-based authorization (separate concern from identity) is the bottleneck for production, multi-tenant professional integrations; local/hacker servers work today without it.
- **Compose at protocol seams**: MCP's value emerges when chaining multiple independent systems across trust boundaries (e.g., travel agent needing bank access); for same-team workflows, keep it inline and avoid the serialization cost.

---

*Distilled from a16z AI + podcast, May 2025. Full interview available at source URL.*
