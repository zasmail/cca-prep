---
title: "How we built our multi-agent research system"
speaker: Anthropic Engineering
source: https://www.anthropic.com/engineering/multi-agent-research-system
retrieved: 2026-07-16
method: webfetch
note: >
  Copyright limits prevent saving a full verbatim transcript or a lightly-reworded
  paraphrase of this article. Below is a condensed, independently-written study-note
  summary (substantially shorter than, and restructured from, the source) capturing
  the facts and terminology relevant to CCA-F prep. Refer to the source URL for the
  original text.
---

# Multi-agent research system — study notes

## Architecture
- **Orchestrator-workers pattern**: a LeadResearcher agent plans strategy, spawns parallel Subagents for different facets of a query, synthesizes their findings, and can spawn more subagents or refine strategy if gaps remain.
- A **CitationAgent** runs at the end to attach source citations to claims before returning the final answer to the user.
- LeadResearcher persists its plan to memory because context windows (200K tokens) get truncated on long-running tasks.
- Differs from static RAG: this is dynamic, multi-step search that adapts based on intermediate findings rather than one-shot retrieval of similar chunks.

## Why multi-agent beats single-agent (for research)
- Internal eval: Claude Opus 4 (orchestrator) + Claude Sonnet 4 (subagents) beat a single Opus 4 agent by **90.2%** on Anthropic's internal research eval.
- Three factors explained ~95% of variance in BrowseComp eval performance: **token usage alone ~80%**, plus number of tool calls and model choice.
- Parallel subagents with independent context windows let the system explore more surface area and compress findings before final synthesis.

## Cost tradeoff
- Multi-agent research uses roughly **15x the tokens** of a normal chat interaction, and **~4x** a single-agent setup.
- Only worth it when task value justifies the token cost. Not a good fit for tasks needing tight shared context/high interdependency (e.g., much of coding work), where agent coordination is less mature.

## Prompt engineering principles that mattered
1. **Model the agent's "mind"** — simulate the agent step by step with real prompts/tools to see actual failure modes (over-searching, verbose queries, wrong tool choice) rather than guessing.
2. **Explicit task decomposation for subagents** — vague delegation ("research X") caused duplicate work or gaps; subagents need clear objective, output format, tool/source guidance, and clear task boundaries.
3. **Scale effort to query complexity** — explicit rules in the prompt: simple fact lookups = 1 agent, 3-10 tool calls; comparisons = 2-4 subagents, 10-15 calls each; broad research = 10+ subagents with divided responsibilities.
4. **Tool design/selection matters as much as the tool itself** — bad or ambiguous MCP tool descriptions route agents wrong; heuristics: check available tools first, match tool to intent, prefer specialized tools over generic ones.
5. **Claude can improve its own tool descriptions** — letting Claude test flawed tool descriptions and rewrite them cut task completion time by **~40%** for subsequent runs.
6. **Broad-then-narrow search strategy** — start with short, broad queries, then narrow, rather than long overly-specific queries that return nothing.
7. **Use extended thinking as a visible scratchpad** — lead agent uses it for planning/tool selection/subagent counts; subagents use "interleaved thinking" after tool results to evaluate quality/gaps and refine next query.
8. **Parallel tool calls** — lead agent spins up 3-5 subagents concurrently (not sequentially); subagents fire 3+ tool calls in parallel. Cut research time by **up to 90%** on complex queries.
- Overall approach favors flexible heuristics over rigid rules, mirroring how expert human researchers work.

## Evaluation approach
- Multi-agent systems don't have one "correct" execution path, so evals must judge outcome + reasonableness of process, not exact step sequences.
- Start small: ~20 representative test queries early on; big early prompt changes can visibly move success rates (e.g., 30% → 80%), so small samples are enough to detect signal.
- **LLM-as-judge** graded against a rubric: factual accuracy, citation accuracy, completeness, source quality (primary vs. secondary sources), tool-call efficiency. A single LLM call with a unified rubric producing a 0–1 score + pass/fail was most reliable/human-aligned.
- **Human evaluation still needed** to catch things automation misses — e.g., testers found early agents over-favored SEO-heavy sites over authoritative-but-lower-ranked sources (scholarly PDFs, forums); fixed via explicit source-quality heuristics in the prompt.
- Multi-agent behavior is emergent — small lead-agent prompt tweaks can unpredictably change subagent behavior, so good prompts function as collaborative frameworks (labor division, conflict resolution, work budgets), not rigid instructions.

## Production/engineering reliability
- Agents are long-running and stateful; errors compound — a small failure early can send the whole trajectory off course. Solution: resumable agents that continue from saved state after a failure rather than restarting from scratch; the model is told about tool failures and often adapts gracefully on its own.
- Debugging is harder because behavior is non-deterministic across runs with identical prompts — solved via full production tracing of decision patterns and interaction structures (without inspecting private conversation content) to find root causes.
- Deployment: agents are highly stateful over long-running sessions, so updates use **"rainbow deployments"** — gradually shifting traffic from old to new versions rather than an instant cutover, to avoid disrupting in-flight agents.
- Current limitation: subagents run **synchronously** — the lead agent waits for each to finish before continuing, which is simple but limits steering/coordination and stalls the whole system on one slow subagent. Async execution would add more parallelism but adds complexity around result ordering, state consistency, and error propagation.

## Appendix highlights
- For agents that mutate state across turns, evaluate **end state** achieved rather than exact turn-by-turn path (agents may find valid alternate routes).
- For very long conversations, agents summarize completed work and store key info externally (memory) before continuing, and can launch fresh-context subagents as they approach context limits.
- Subagents can write outputs directly to a shared filesystem/artifact store and return lightweight references to the lead agent instead of passing large outputs through conversation history — saves tokens and avoids information loss on hand-off.

## Usage breakdown (Clio analysis of Research feature usage)
Top use-case categories: software/technical development (10%), professional/technical content creation (8%), business/growth strategy (8%), academic/educational research support (7%), fact-checking on entities/orgs/locations (5%).

## Exam-relevant takeaways
- Concrete numbers worth memorizing: **90.2%** improvement multi-agent vs. single-agent; **~15x** token cost vs. chat, **~4x** vs. single agent; **80%** of variance from token usage; **up to 90%** time reduction from parallel tool calls; **~40%** faster completion after agent-authored tool description fixes.
- This is the canonical example of the **Orchestrator-Workers** pattern from "Building Effective Agents" — coordinator manages all inter-agent communication, workers don't talk to each other directly.
