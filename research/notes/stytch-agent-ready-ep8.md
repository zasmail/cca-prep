---
title: "Agent Ready Episode 8: Evolving Architectures for AI Agents"
speakers: Cal Rueb (Anthropic), Lizzie Siegle (Cloudflare), Nate Barbettini (Arcade)
source: https://stytch.com/blog/agent-ready-ep8-anthropic-cloudflare-arcade-agent-architecture/
published: 2025-09-24
themes: [tool-design-mcp, orchestration, context-engineering, enforcement-reliability, model-fundamentals]
---

## Core claims

1. Agents (tool-calling loops) recover from errors and edge cases far better than rigid workflows that chain fixed prompts.
2. Only two domains have proven product-market fit for full-autonomy agents today: coding assistants and deep research; customer support remains better as human-in-loop hybrid.
3. Tool descriptions must be action-oriented, not 1:1 REST API mappings—models waste tokens re-deriving call composition when handed raw resource endpoints.
4. Constrained tool options outperform large menus because models are smart but "lazy" and benefit from focused choice.
5. Output-side context engineering (cleaning API responses, stripping irrelevant fields) is as critical as input-side prompt engineering.
6. MCP's value is standardization across clients (Claude, Cursor, ChatGPT, Windsurf), not conceptual novelty; function calling already existed.
7. Context poisoning (malicious GitHub issues) and tool poisoning (malicious server descriptions) are distinct threats requiring different mitigations.
8. Signed-hash verification of tool descriptions fails because compromised servers can publish their own compromised hashes; trusted registries are the durable solution.
9. Sub-agents are temporary workarounds for today's limited context windows, likely unnecessary in higher-capacity models.
10. No negotiation protocol exists for context-window/payload-size limits; servers can blow windows with large results unchecked.

## Patterns & frameworks

- **Agent loop** — Tools + open-ended task + repeat until done (vs. rigid workflow chains).
- **Smart-but-lazy 12-year-old heuristic** — If a competent child couldn't figure out a tool from its description alone, the model probably can't either.
- **Context poisoning** — Attacker crafts legitimate-looking data (GitHub issue/PR) to trick an authorized agent into harmful action.
- **Tool poisoning** — Malicious instructions in MCP server descriptions, invisible to humans but read by models.
- **Approval-gated vs. open ecosystems** — Trade-off between security (slow, gatekeeping) and accessibility (fast, no central authority).
- **Sub-agents as capacity workaround** — Parallel search sub-agents (as in Deep Research) or specialized delegated agents (Claude Code research) to protect main context window; expected to fade with higher capacity.

## Numbers & specifics

- **Two proven agent domains:** coding assistants (real-time human oversight), deep research (search + synthesis loop).
- **Platforms supporting MCP:** Claude, Cursor, ChatGPT, Windsurf.
- **Arcade focus:** Authenticated tool execution (not just read-only API access).
- **Cloudflare stack:** AutoRAG, Vectorize, MCP deployment platform.
- **App-store precedent:** iOS/Android review timelines as cautionary reference for approval-gated ecosystems.

## Quotes

> "Give a model tools, an open-ended task, and let it call tools in a loop until it decides it's done — as opposed to a rigid multi-step workflow."

> "Models are smart but 'lazy' — give them exactly what's needed for the task rather than a large menu to reason over."

> "Could a smart-but-lazy 12-year-old figure out how to use this tool from its description alone? If yes, a frontier model probably can too."

> "Today's frontier models are the slowest and least capable they will ever be — worth building for where the trajectory is heading."

> "Sub-agents are likely a short-term workaround for today's limited context windows rather than a durable long-term architecture."

## Applied AI relevance

- **High-leverage design lever:** Tool description, input validation, and output cleaning materially determine whether models pick the right tool and execute correctly—invest time here.
- **Security requires layering:** Prompt-injection/tool-poisoning risks need both registry-level vetting AND model-level mitigations (e.g., trust-tagging user-supplied tools); neither alone is sufficient.
- **Build for capacity trajectory:** Today's context limits are shaping multi-agent splits and sub-agent patterns; future higher-capacity models may collapse these, so architect for flexibility.
- **Customer support != autonomous agent:** Full end-to-end autonomy lacks visibility to end users; hybrid human-in-loop workflows are more reliable for regulated/high-stakes domains.

---
*~550 words. Themes: tool-design-mcp, orchestration, context-engineering, enforcement-reliability, model-fundamentals.*
