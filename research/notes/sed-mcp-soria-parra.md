---
title: Anthropic and the Model Context Protocol
speaker: David Soria Parra (Anthropic, MCP co-creator)
source: Software Engineering Daily, Episode 1836 (May 2025)
source_url: https://softwareengineeringdaily.com/2025/05/13/anthropic-and-the-model-context-protocol-with-david-soria-parra/
themes: [tool-design-mcp, context-engineering, orchestration, model-fundamentals, claude-code-workflows]
---

## Core claims

1. MCP solves the M×N integration problem between AI clients and context providers by establishing a shared protocol, analogous to how LSP solved IDE-language integrations.
2. MCP is JSON-RPC based with three primitives — tools, resources, and prompts — enabling both local and remote stateful servers despite "server" terminology.
3. Servers are typically stateful local programs running on the user's machine, not network-remote services; the term refers to serving context upward.
4. Sampling (requesting completions from the client's configured model) is a severely underused feature that enables composable, model-independent agent chains.
5. Authorization for cloud-hosted servers and stateless horizontal scaling are the two most critical near-term roadmap items.
6. MCP's long-term value depends on ecosystem neutrality — competitors must trust it equally, requiring evolution toward formal governance (foundation-like models).
7. Tools alone are not sufficient for agents; higher-level abstractions likely necessary but still unresolved in the protocol design.

## Patterns & frameworks

**LSP-inspired design** — MCP directly models LSP's JSON-RPC invoke/response/error pattern and initialization handshake, solving one-to-many AI integration parallel to IDE-language integration.

**Capability exchange** — Client and server negotiate capabilities during initialization, crediting both LSP and Mercurial's push/pull protocol design.

**Sampling as composition** — Servers can request completions from the client's model rather than embedding their own, enabling chains of MCP clients/servers that form agent-logic graphs.

**Merit-based governance** — Similar to PHP and Mercurial communities: SDK maintainers (Pydantic, Microsoft, Spring, JetBrains) contribute as equals; formal models being explored as scale grows.

## Numbers & specifics

- **LSP adoption threshold**: ~2015, solved N×M IDE-language problem before MCP applied same logic to AI clients/providers
- **SDK languages**: Python, TypeScript, C#, Java, Kotlin, Go (expected)
- **SDK maintainers**: Pydantic (Python), Microsoft (C#), Spring team (Java), JetBrains (Kotlin)
- **Parallel ship**: Justin Spahr-Summers (Claude Desktop), David Soria Parra (Zed), same-sprint bottom-up project
- **Oculus integration effort**: Merged traditional gaming toolchain (Perforce for binaries, Windows-based stateful CI) into Facebook's Linux-first ephemeral CI
- **Facebook's stack rationale**: Monorepo + language choice load-bearing at scale; cheaper to dedicate teams optimizing existing stack (Mercurial, Buck, PHP) than migrate company-wide

## Quotes

- *"tools are likely necessary for agents but I'm not convinced they're sufficient"* — on open boundaries in agent architecture
- *"the term is about serving context upward to the client, not about network location"* — clarifying what "server" means in MCP
- *"most clients currently only implement tool calling"* — on why sampling (a powerful feature) remains underexplored
- *"MCP's value depends on staying an ecosystem competitors can all trust equally"* — on governance necessity for protocol survival
- *"find a bug in a big open-source project, fix it, move it forward"* — his learning philosophy from age 14 onward

## Applied AI relevance

- **Protocol design transfers**: Anthropic engineers building integrations should study MCP's LSP-inspired patterns (JSON-RPC, capability exchange, initialization handshakes) when designing shared protocols across tools/agents.
- **Sampling unlocked**: The model-independent completion feature is a powerful but underused composable primitive for building agent chains without vendor lock-in; worth exploring systematically in multi-agent orchestration work.
- **Governance as technical debt**: MCP's neutral-ecosystem requirement shows how protocol adoption scales only when trust is enforced at the governance level, not just in spec prose — apply this when designing CCA certification or shared model access frameworks.
- **Abstraction gaps**: If tools are necessary but insufficient for agents, the critical missing work is identifying and standardizing higher-level orchestration primitives (routing, parallelization, evaluator-optimizer patterns) at the protocol level.
