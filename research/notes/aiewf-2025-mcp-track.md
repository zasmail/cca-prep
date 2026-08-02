---
title: AIEWF 2025 MCP Track Distillation
speaker: Theo Chu, John Welsh, Harold Larson, Samuel Colvin, Alex Vulov, Ben Ekl, Jan Churn, et al.
source: https://www.youtube.com/watch?v=z4zXicOAF28
retrieved: 2026-07-16
themes: [tool-design-mcp, orchestration, context-engineering, enforcement-reliability, skills, memory, claude-code-workflows, gtm-applications]
---

## Core Claims

1. **MCP is a pluggable architecture for agents, not an API replacement** — Don't just wrap existing APIs 1:1; design for agent cognition and model reasoning over context.

2. **Tool discovery (dynamic dispatch) is MCP's killer differentiator over OpenAPI** — Only request tools needed in context; prevents context bloat and enables 5,000+ tool marketplaces without upfront LLM knowledge.

3. **Sampling is MCP's least-used but most powerful primitive** — Allows remote MCP servers to call back to the LLM via the client, enabling cost-sharing and avoiding redundant model access overhead.

4. **Observability is a distributed-systems problem now** — Without OpenTelemetry/OTLP integration, you lose visibility across agent→server→agent chains; hotel context propagation through MCP metadata is now standard practice.

5. **Agents need payment identity to autonomously purchase services** — Current agent independence is blocked by lack of agent-to-service identity/billing; centralized marketplace model (e.g., Apify) is nearer-term than new payment systems.

6. **Quality over quantity in tool definition; 3 vectors kill tool selection** — Too many tools confuse models; tool repetition degrades accuracy; mixing domains/instructions raises error rates (LangChain research cited).

7. **MCP standardization is an organization-wide productivity play** — Standardizing on MCP internally (via gateway pattern) eliminates integration chaos, enables code reuse across teams, and shifts cost to shared infrastructure.

## Patterns & Frameworks

| Pattern | Definition |
|---------|-----------|
| **"The pit of success"** | Design the right thing to be the easiest thing; enables org-wide adoption without enforcement |
| **MCP gateway pattern** | Single entry point handling auth, routing (internal/external), rate limiting; returns SDK session to any consumer |
| **Tool as context, not API** | Markdown/XML output formatted for human+LLM reasoning, not machine parsing; progressively enhance via sampling |
| **Tool discovery (dynamic)** | Server tells client available tools based on execution state; solves permission/context-limiting at runtime |
| **Signal loop (Foundry)** | Collect user interactions → fine-tune model → redeploy → observe results; replaces static software factory |
| **Agentic mesh** | Multiple agents interacting over MCP as infrastructure layer; foundation for emergent collective intelligence |
| **SPARD loop** | Scrape → Plan → Analyze (reduce) → Return (deliver) → Detect (evaluate); pattern for AI-intensive applications at scale |

## Numbers & Specifics

- **Pyantic downloads:** 360M/month (~140/second); used in all Python AI SDKs and agent frameworks
- **Apify ecosystem:** 5,000 actors (tools); 1M monthly visitors; creators paid $250K+ in last month; $500K+/month total volume
- **Dragon (healthcare AI):** Off-shelf model → 83% character acceptance rate after synthetic fine-tuning + 650K interaction AB tests
- **Foundry platform:** 70,000 customers; 50,000+ agents built daily
- **MCP servers count:** Registry of registries now exists (masters); Google has DNS-based A2A alternative with .well-known/agents.json
- **OpenTelemetry adoption:** W&B Weave, Logfire, MCP Run now export OTLP-compatible traces; hotel becoming global standard for observability
- **vs.code support:** Full MCP spec support landed in Insiders; Harold confirmed tools, resources, prompts, sampling all now working
- **Token limits:** Some clients/models restrict tool description length (e.g., 350ms fetch latency in distributed trace example)
- **Context window economics:** Payants/Logfire SQL agent inference avoids shipping SQL schema to main agent; keeps overhead minimal

## Quotes

> "MCP is a pluggable architecture for agents. Full stop. That's it. It's pretty simple to reason about." — David Kramer (Sentry)

> "Being boring on stuff like this is good. It's not a competitive advantage to be really good at making Google Drive talk to your app. It's just a thing that you need to do." — John Welsh (Anthropic)

> "You can't just be like, 'I got an API. I'm going to expose all those endpoints as tools.' You're going to get the worst results you can possibly imagine." — David Kramer (Sentry)

> "Quality over quantity. Tools reflect actions, but MCP is really about rich stateful interactions when you use the full spec." — Harold Larson (VS Code)

> "If agents cannot purchase services, how can we expect them to reach higher levels of intelligence?" — Jan Churn (Apify)

## Applied AI Relevance

- **Tool design is not API wrapping.** Construct tools for agent reasoning, not system integration. Test with LLMs early; iterate on descriptions, error messages, markdown formatting for comprehension.
  
- **Observability at scale requires OTLP + context propagation.** Don't build custom tracing; adopt hotel, configure OTLP endpoints, propagate trace IDs through MCP metadata payloads. Audit/security teams require this before production.

- **Dynamic tool discovery is bottleneck removal.** If building multi-tenant or multi-service architecture, move from static tool lists to discovery patterns. Reduces context bloat, enables marketplace scaling, unlocks tool composition.

- **Sampling enables cost-efficient tool agents.** When tool calls need LLM reasoning (SQL generation, validation, retry), use sampling to share parent agent's model; avoid spinning up separate inference per tool.

---

**Key reference:** MCP spec (full) is supported in VS Code Insiders v10+; OpenTelemetry semantic conventions for Gen AI in development; Apify/MCP.run demonstrating production patterns.
