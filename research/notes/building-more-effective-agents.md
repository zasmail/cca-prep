---
title: Building More Effective AI Agents
speaker: Erik Schluntz (w/ Alex Albert)
source: https://www.youtube.com/watch?v=uhJJgc-0iTQ
themes:
  - orchestration
  - tool-design-mcp
  - context-engineering
  - claude-code-workflows
  - evals
  - model-fundamentals
---

## Core Claims

1. Claude's agent capability stems from explicit RL training on open-ended multi-step tasks across coding, search, and planning domains during model development.

2. Coding is the fundamental agent skill; mastery here transfers to all other domains via spillover effect (search, scheduling, reasoning).

3. Writing code to generate artifacts is more effective than direct generation, especially for repetitive/large-scale outputs (e.g., SVG diagrams with nested patterns).

4. Agent loops now dramatically outperform single-shot workflows because Claude can respond to feedback and iteratively correct its own work.

5. "Workflows of agents" (chaining closed-loop agents together) replaces the earlier pattern of chaining single prompts; each step verifies success before transition.

6. Multi-agent systems with parallelization differ fundamentally from workflows of agents—multiple Claudes work simultaneously, not sequentially.

7. Sub-agents are exposed as tools that Claude can call with prompts; research shows Claude initially gives incomplete delegation instructions but improves with training.

8. Tool and MCP design must follow UI-first principles (unified presentation) rather than API-first (one tool per endpoint); the model is a *user* of these tools.

9. Simplicity is foundational—start with single-shot prompts, move to agent loops, add multi-agent only when parallelization or context isolation genuinely helps.

10. Verification and self-testing (agents observing their own work via execution feedback) is the frontier unlocking agent adoption in non-verifiable domains.

## Patterns & Frameworks

- **Agentic escalation**: Single-shot → Agent loop → Workflows of agents → Multi-agent orchestration
- **Sub-agent delegation**: Offload heavy/parallel work to specialized agents; protects main context from token overhead
- **Parallelization for MapReduce tasks**: Split independent subtasks among agents; fan-in results (e.g., deep research product)
- **Tool bucketing**: For 100+ tools, distribute into buckets (~20 per agent); main agent orchestrates which bucket
- **UI-first tool design**: Present all related data in one tool call (Slack example: unified view vs. three separate endpoints)
- **Test-time compute via multi-agent**: Multiple agents working the same problem → better final answer (analogous to ensemble reasoning)

## Numbers & Specifics

- RL training applied to: coding, search, planning, and other agent-like domains
- Deep research product: orchestrator agent spawns multiple sub-agents running searches in parallel
- Sub-agent context isolation: offload "tens of thousands of tokens" of work to preserve main context
- Tool distribution rule: ~20 tools per agent (from 100–200 tool problem)
- Slack example: 3 separate endpoints (load conversation, user ID→name, channel ID→name) vs. 1 unified tool
- Matrix reference: Neo learning kung fu = injecting skills directly into Claude

## Quotes

> "Once you have an amazing coding agent, a coding agent can do any other kind of work."

> "Each one of those steps in the workflow is actually a closed loop where... it runs, Claude sees the output and then it can keep iterating and repeat until it knows that it got the right value and then it transitions to the next step."

> "Claude makes a lot of the same mistakes that first time managers make of where it will give incomplete or sort of unclear instructions."

> "Tools should be one-to-one with your UI, not your API. Because ultimately the model is a user of these things."

> "Start simple and make sure you only add complexities you need... even though you can build a big workflow of agents, you should still start sort of from the simplest possible thing."

## Applied AI Relevance

- **MCP & tool design**: Structure tools around agent interaction patterns, not backend APIs; bundle related data to reduce tool-call sequences and improve decision quality.
- **Observability through simplicity**: Start with single-shot, add agentic loops when iteration is needed, introduce multi-agent only when parallelization/context isolation pays off. Complexity compounds debugging difficulty.
- **Sub-agent as scaling pattern**: Use sub-agents to parallelize independent work, protect context budgets, and shard large tool vocabularies—critical for enterprise automation.
- **Closing the verification loop**: The frontier for production reliability is self-testing (agents running their own output, observing feedback, catching bugs)—this unlocks verifiable use cases beyond software engineering.
