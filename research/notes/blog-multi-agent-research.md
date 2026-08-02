---
title: "How we built our multi-agent research system"
speaker: Anthropic Engineering
source: https://www.anthropic.com/engineering/multi-agent-research-system
themes:
  - orchestration
  - tool-design-mcp
  - context-engineering
  - evals
  - enforcement-reliability
---

# Multi-Agent Research System — Distilled Notes

## Core Claims

1. Orchestrator-Workers pattern (LeadResearcher + parallel Subagents) beats single-agent by **90.2%** on research evaluation.
2. Token usage alone explains ~80% of performance variance; model choice and tool-call count account for remaining ~15%.
3. Multi-agent research costs ~15x normal chat interaction, ~4x single-agent setup; only justified for high-value tasks.
4. Parallel subagents with independent context windows explore more task surface and compress findings more effectively than sequential single-agent work.
5. Explicit task decomposition for subagents (objective, output format, tool guidance, boundaries) prevents duplicate work and gaps better than vague delegation.
6. Tool quality (description clarity, fit to intent) routes agent behavior more reliably than the tool's underlying capability.
7. Extended thinking used as a visible scratchpad (lead agent: planning/tool selection; subagents: post-result evaluation) improves coherence and debugging.
8. LLM-as-judge with unified rubric (factual accuracy, citation accuracy, completeness, source quality, efficiency) is most reliable for multi-agent evaluation.
9. Production multi-agent systems are long-running and stateful; errors compound early and cascade; resumable checkpoints are essential.
10. Small prompt tweaks produce emergent, unpredictable shifts in subagent behavior—prompts must be collaborative frameworks (labor division, conflict resolution, budgets), not rigid instructions.
11. Broad-then-narrow search (short queries → narrow refinement) outperforms overly-specific long queries that return nothing.

## Patterns & Frameworks

- **Orchestrator-Workers** — LeadResearcher plans strategy, spawns parallel Subagents, synthesizes findings, iterates if gaps remain. Coordinator manages ALL inter-agent communication.
- **CitationAgent** runs at end to attach sources before final return.
- **Extended thinking (visible scratchpad)** — lead agent for planning; subagents for interleaved thinking after tool results to evaluate gaps and refine queries.
- **Broad-then-narrow strategy** — start with short, general queries; progressively narrow based on findings rather than guessing specificity upfront.
- **Rainbow deployments** — gradual traffic shift from old to new agent versions to avoid disrupting long-running sessions.
- **Resumable agents** — save state at checkpoints; agents continue from failure rather than restart, often adapting gracefully to tool failures.
- **LLM-as-judge rubric** — unified 0–1 score + pass/fail on outcome + process reasonableness, not exact step sequences.
- **Source-quality heuristics** — human testers found agents over-favored SEO-heavy sites; fixed with explicit preference for primary sources (scholarly PDFs, authoritative forums).

## Numbers & Specifics

- **90.2%** improvement (Opus 4 orchestrator + Sonnet 4 subagents vs. single Opus 4)
- **~80%** of variance from token usage; **~15%** from tool-call count and model choice
- **~15x** tokens vs. normal chat; **~4x** vs. single-agent setup
- **Up to 90%** time reduction via parallel tool calls (3–5 subagents concurrently, 3+ calls per subagent in parallel)
- **~40%** faster task completion after Claude rewrote flawed tool descriptions
- **~20 representative queries** sufficient to detect signal early; **30%→80%** success rate swing from prompt changes
- LeadResearcher persists plan to memory at context window truncation (200K token ceiling)
- Current limitation: subagents run synchronously (lead agent waits); async execution would improve parallelism but add complexity

## Quotes

1. "Model the agent's mind—simulate the agent step by step with real prompts/tools to see actual failure modes rather than guessing."
2. "Tool design/selection matters as much as the tool itself—bad MCP tool descriptions route agents wrong."
3. "Multi-agent behavior is emergent—small lead-agent prompt tweaks can unpredictably change subagent behavior."
4. "A small failure early can send the whole trajectory off course—errors compound in long-running stateful systems."
5. "Agents may find valid alternate routes—evaluate end state achieved, not exact turn-by-turn path."

## Applied AI Relevance

- **Tool design is a first-class performance lever** — MCP tool descriptions directly influence agent routing and task success; engineer these explicitly with clarity and specificity.
- **Recognize task structure before pattern choice** — Orchestrator-Workers excels at decomposable research/discovery; poor fit for tightly-coupled reasoning or coding where high interdependency demands shared context.
- **Extended thinking (visible + interleaved) improves production reliability** — enables human tracing of decision logic, early gap detection in subagents, and coherent synthesis without "black box" behavior.
- **Production costs are high** — resumable checkpoints, tracing, gradual deployments, and separate tool-validation agents are mandatory for long-running systems; cost/benefit favors high-value research use-cases over low-value routine tasks.
