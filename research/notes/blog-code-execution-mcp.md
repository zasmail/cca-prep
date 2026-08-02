---
title: Code Execution with MCP—Building More Efficient Agents
speaker: Adam Jones, Conor Kelly (Anthropic Engineering)
source: https://www.anthropic.com/engineering/code-execution-with-mcp
themes: [tool-design-mcp, context-engineering, orchestration, enforcement-reliability, claude-code-workflows]
---

## Core Claims

1. **Upfront tool-definition loading wastes hundreds of thousands of tokens** before agents begin work, especially with large APIs (Google Drive, Salesforce).
2. **Unfiltered intermediate results force every step's output through the model's context**, doubling token cost when data moves between systems.
3. **Code execution APIs replace sequential tool calls**, letting MCP servers behave as typed interfaces in a virtual filesystem.
4. **Progressive disclosure loads tools on demand** via search/browse rather than preloading every schema.
5. **Data filtering/transformation can happen before the model sees it**, reducing context bloat and preserving privacy.
6. **Loops and conditionals in code eliminate repeated agent-loop bounces**, cutting latency compared to chained tool calls.
7. **Filesystem persistence enables checkpoint-and-skill patterns**, letting agents build reusable capabilities across steps.
8. **Privacy-by-architecture (sandboxed execution) beats privacy-by-prompt** — sensitive data never leaves the code environment.
9. **Cloudflare independently validated this pattern** as "Code Mode," confirming models handle external systems better via code than sequential calls.
10. **Infrastructure trade-offs are real** — sandbox, resource limits, and monitoring add operational overhead that must justify efficiency gains.

## Patterns & Frameworks

- **Code Mode** — Represent external tools as code APIs instead of function calls (Cloudflare independent validation)
- **Progressive Disclosure** — Load tool definitions on demand via search rather than upfront; return varying detail levels (name → name+description → full schema)
- **Context-Efficient Filtering** — Transform/aggregate data in the code environment before returning to model (10,000-row spreadsheet → summary)
- **State Persistence via Filesystem** — Checkpoint progress across steps; persist reusable functions as "skills"
- **Privacy-Preserving Data Pipelines** — Route sensitive data directly between systems; tokenize PII before model ingestion

## Numbers & Specifics

- **150,000 tokens → 2,000 tokens** (98.7% reduction) for Drive-to-Salesforce workflow
- **MCP launch:** November 2024
- **Community adoption:** Thousands of servers, SDKs across major languages
- **Example:** 10,000-row spreadsheet reduction to relevant rows before return
- **Tool definitions:** Google Drive, Salesforce used as complexity examples

## Quotes

- "Loading all tool definitions upfront...can cost hundreds of thousands of tokens before the agent even starts"
- "The Drive-to-Salesforce example becomes a small piece of code that loads the transcript once"
- "Code can filter/transform data before it ever reaches the model"
- "Intermediate results stay inside the execution environment by default"
- "These are largely familiar software-engineering problems with familiar solutions"

## Applied AI Relevance

- **Scale requires code execution, not sequential tool calling** — agents with many MCP servers need context-efficient patterns or token costs explode
- **MCP + code APIs enable on-demand tool loading** — progressive disclosure lets agents explore available tools without up-front schema bloat
- **Privacy and cost align through architecture** — sandboxed code environments filter sensitive data before model ingestion, matching compliance and efficiency needs
- **Reusable skills compound across sessions** — filesystem checkpoints and persisted functions let agents build institutional knowledge, enabling higher-level workflows over time

---

**Examined:** 2026-07-16 | **Length:** ~450 words
