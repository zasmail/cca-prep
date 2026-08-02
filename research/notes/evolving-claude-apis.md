---
title: Evolving Claude APIs for Agents
speaker: Katelyn Lesse
source: https://www.youtube.com/watch?v=aqW68Is_Kj4
themes:
  - model-fundamentals
  - tool-design-mcp
  - context-engineering
  - memory
  - skills
  - claude-code-workflows
  - orchestration
  - evals
---

## Core Claims

1. Platform success hinges on three pillars: harnessing capabilities, managing context, and providing computing infrastructure.
2. Extended thinking performance scales with reasoning budget—developers control whether Claude thinks long or responds quickly.
3. Tool use reliability is achieved through standardized JSON schema definition and Claude's learned ability to select and call tools.
4. MCP enables agents to access external systems (GitHub, Century) without bloating the context window.
5. Memory tools allow Claude to store context outside the window and retrieve it intelligently.
6. Context editing (clearing old tool results) combined with memory yields 39% performance improvement on internal benchmarks.
7. Code execution in secure sandboxes removes friction between code-writing and code-running capabilities.
8. Skills (folders of scripts, instructions, resources) grant agents domain expertise to apply MCP tools intelligently.
9. Larger context windows are only effective when paired with editing tools and Claude's learned understanding of remaining space.
10. The future of agentic systems is autonomous model operation within sandboxed environments with proper infrastructure.

## Patterns & Frameworks

- **Three-pillar platform design:** Capabilities → Context Management → Compute Infrastructure
- **Capability exposure pattern:** Train model → Expose via customizable API features (thinking budget, tool_choice, code execution)
- **Context stratification:** In-window (current) vs. stored (memory) vs. cleared (editing)
- **MCP + Skills composition:** MCP provides tool/context access; Skills provide domain expertise to use them effectively
- **Reasoning budget as performance lever:** Think longer for complex problems, quick answers for simple requests
- **Container orchestration at scale:** Secure sandboxing, session persistence for web/mobile Claude Code

## Numbers & Specifics

- **39% performance bump** from combining memory + context editing on internal evals
- **1 million token context window** available on some Claude models
- **MCP adoption:** Introduced ~1 year ago, community-wide standardization achieved
- **Claude Code tool density:** "Many, many, many tools" called constantly; hundreds of files read/written per session
- Tool results often "really large," consuming significant window space unnecessarily
- **Design system expertise:** Codebase-specific patterns stored as queryable skills

## Quotes

> "Claude has access to writing code. And if Claude has access to running that same code, it can accomplish anything."

> "Getting the right context at the right time in the window is one of the most important things that you can do to maximize performance."

> "Skills are basically just folders of scripts, instructions, and resources that Claude has access to and can decide to run within its sandbox environment."

> "We're going to keep leaning into agent infrastructure... orchestration, secure environments, and sandboxing."

> "Tool results from past calls are not necessarily super relevant to help claude get good responses later on in a session."

## Applied AI Relevance

- **Context editing is a force multiplier:** 39% performance gain proves it's not optimization theater—prioritize implementing context cleanup strategies.
- **MCP and Skills are complementary, not competing:** Combine MCP for external tool/context access with Skills for domain expertise application; don't choose one.
- **Autonomous sandboxed execution is the frontier:** Invest in reliable orchestration, session persistence, and secure container management—these are differentiators.
- **Train model capabilities; expose via API primitives:** Training (extended thinking, tool use, context awareness) only drives value when developers have API levers to control when/how it activates.
