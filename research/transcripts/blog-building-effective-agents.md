---
title: "Building Effective AI Agents"
speaker: "Erik S. and Barry Zhang (Anthropic Engineering)"
source_url: "https://www.anthropic.com/engineering/building-effective-agents"
retrieved: 2026-07-16
method: webfetch
publication_date: "2024-12-19"
note: >
  This is a condensed, paraphrased set of study notes rather than a verbatim
  reproduction of the original article, in line with copyright limits on
  reproducing full third-party text. Structure and key points are captured;
  wording is not a direct copy. For the exact original text and any code
  samples, refer to the source URL above.
---

# Building Effective AI Agents

**Author/Team:** Erik S. and Barry Zhang
**Published:** December 19, 2024

## Section Headings (in order)

1. Building effective agents
2. What are agents?
3. When (and when not) to use agents
4. When and how to use frameworks
5. Building blocks, workflows, and agents
   - Building block: The augmented LLM
   - Workflow: Prompt chaining
   - Workflow: Routing
   - Workflow: Parallelization
   - Workflow: Orchestrator-workers
   - Workflow: Evaluator-optimizer
   - Agents
6. Combining and customizing these patterns
7. Summary
8. Appendix 1: Agents in practice
   - A. Customer support
   - B. Coding agents
9. Appendix 2: Prompt engineering your tools

## Notes by section

**Opening — Building effective agents**
Anthropic studied teams implementing LLM agents across sectors. Finding: the most effective implementations use simple, composable patterns rather than heavyweight frameworks or specialized tooling.

**What are agents?**
Two system types distinguished. *Workflows* run LLMs and tools through predefined, orchestrated code paths. *Agents* are systems where the LLM itself directs its own process and tool use, retaining control over how it accomplishes a task. "Agent" is used loosely across the industry — from fully autonomous long-running systems to more constrained implementations.

**When (and when not) to use agents**
Start with the simplest solution; add complexity only when it earns its keep. Agentic systems trade latency and cost for capability. Workflows fit predictable, well-scoped tasks; agents fit tasks needing flexibility and model-driven judgment at scale. Many use cases are served well enough by a single optimized LLM call plus retrieval/few-shot examples.

**When and how to use frameworks**
Frameworks mentioned: Claude Agent SDK, AWS's Strands Agents SDK, Rivet (visual workflow builder), Vellum (GUI workflow builder). They simplify standard plumbing (calling LLMs, parsing tool calls) but add abstraction layers that can obscure what's actually happening, complicating debugging. Recommendation: start with direct API calls since many patterns need only a few lines of code; if you do use a framework, understand what it does under the hood.

**Building block: The augmented LLM**
An LLM enhanced with retrieval, tools, and memory. Modern models can generate their own search queries, pick tools, and decide what to retain. Emphasis on tailoring the interface to your use case and keeping it easy to inspect. Model Context Protocol (MCP) is cited as one way to integrate with a growing ecosystem of third-party tools.

**Workflow: Prompt chaining**
Break a task into ordered LLM steps where each step's output feeds the next; add programmatic checks between steps. Trades latency for higher accuracy on each sub-step. Example uses: draft-then-translate marketing copy, or outline-then-write-full-document with a validation gate in between.

**Workflow: Routing**
Classify the input, then send it to a specialized downstream path — enabling separate optimization per category instead of one prompt trying to do everything. Examples: routing support tickets (general/refunds/technical) to different flows, or routing easy queries to a cheaper/faster model (e.g., Haiku) and hard ones to a stronger model (e.g., Sonnet).

**Workflow: Parallelization**
Two variants: *sectioning* (split into independent parallel subtasks) and *voting* (run the same task multiple times for diverse takes). Used for speed or for higher-confidence results via multiple perspectives — e.g., one model path answering while another screens for policy violations, or evaluating code/content from several angles simultaneously.

**Workflow: Orchestrator-workers**
A central LLM breaks a complex task into subtasks on the fly and dispatches them to worker LLMs, then combines the results. Differs from static parallelization because the subtask breakdown is decided per input, not fixed in advance. Good fit for tasks like multi-file code edits where the specific changes needed can't be predicted ahead of time.

**Workflow: Evaluator-optimizer**
One LLM generates, another critiques/scores, and the loop repeats. Works best when there's a clear evaluation rubric and iteration genuinely improves the result. Example uses: literary translation needing nuance, or research tasks needing multiple passes with an evaluator deciding when to stop.

**Agents**
Agents kick off from a user instruction/conversation, clarify the task, then work autonomously — pulling in the human again only when needed. Key features: getting "ground truth" from the environment (tool results, execution outcomes) at each step, and checkpoints for human oversight or when stuck. Despite sounding sophisticated, an agent is typically just an LLM using tools in a loop based on environmental feedback. Success hinges on well-designed tools and documentation. Best suited to open-ended problems where the number/shape of steps can't be hardcoded — but autonomy raises cost and compounding-error risk, so extensive sandbox testing and guardrails are recommended. Anthropic cites its SWE-bench solver and computer-use reference implementation as examples.

**Combining and customizing these patterns**
These are patterns to remix, not rules to follow rigidly. Measure performance, iterate, and only add complexity where it demonstrably helps.

**Summary**
Favor the simplest workable design. Recommended path: start with simple prompts, optimize with real evaluation, and only move to multi-step agentic complexity when simpler approaches fall short. Three guiding principles: keep designs simple, favor transparency (make the agent's planning visible), and invest carefully in the agent-computer interface (docs + testing).

**Appendix 1: Agents in practice**
- *Customer support*: combines a familiar chat interface with tool access for open-ended resolution — pulling customer data/order history/knowledge base, and taking actions like issuing refunds. Resolution is a natural, measurable success metric; some companies price only for successful resolutions.
- *Coding agents*: strong fit because code output can be automatically tested, agents can iterate on test feedback, the problem space is well-structured, and quality is objectively measurable. Anthropic's own implementation resolves real GitHub issues from PR descriptions alone, though human review is still needed for broader alignment checks.

**Appendix 2: Prompt engineering your tools**
Tool specs deserve as much prompt-engineering care as the rest of the prompt. The same action can be specified in very different formats (e.g., diffs vs. full-file rewrites; markdown vs. JSON output) with very different cognitive cost to the model — e.g., writing a diff requires knowing line counts in advance; JSON requires escaping quotes/newlines. Guidance: give the model room to "think" before committing to a format it can paint itself into a corner with, prefer formats that resemble natural text the model has seen a lot of, and cut unnecessary formatting overhead. Treat tool parameter names/descriptions like documentation for a new engineer, test extensively (e.g., via the Workbench), and build in error-prevention (poka-yoke). Anthropic reports investing more effort tuning tools than the overall prompt during SWE-bench work — e.g., requiring absolute file paths instead of relative ones eliminated a class of model mistakes caused by working-directory confusion.
