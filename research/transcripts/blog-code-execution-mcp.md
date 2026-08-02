---
title: "Code Execution with MCP: Building More Efficient Agents"
speaker: "Adam Jones and Conor Kelly (Anthropic Engineering)"
source_url: "https://www.anthropic.com/engineering/code-execution-with-mcp"
retrieved: 2026-07-16
method: webfetch
publication_date: "2025-11-04"
note: >
  Condensed, paraphrased study notes rather than a verbatim reproduction of
  the original article, in line with copyright limits on reproducing full
  third-party text. Structure and key points are captured; wording is not a
  direct copy. Refer to the source URL for exact original text and code
  samples.
---

# Code Execution with MCP: Building More Efficient Agents

**Author/Team:** Adam Jones and Conor Kelly (acknowledgments: Jeremy Fox, Jerome Swannack, Stuart Ritchie, Molly Vorwerck, Matt Samuels, Maggie Vo)
**Published:** November 4, 2025

## Section Headings (in order)

1. Introduction
2. Excessive token consumption from tools makes agents less efficient
3. Code execution with MCP improves context efficiency
4. Benefits of code execution with MCP
5. Summary

## Notes by section

**Introduction**
MCP (Model Context Protocol) is an open standard, launched November 2024, letting agents connect to external systems/tools; it now has broad adoption (thousands of community servers, SDKs across major languages). Problem: as agents connect to more tools, loading every tool definition upfront and routing all intermediate results through the context window gets inefficient. The article covers using code execution to work with MCP servers more efficiently.

**Excessive token consumption from tools makes agents less efficient**
Two core problems:
- *Tool definition overload*: loading all tool schemas upfront (examples given: Google Drive, Salesforce) can cost hundreds of thousands of tokens before the agent even starts, hurting latency and cost when connected to many tools.
- *Intermediate results consume tokens*: chained tool calls push every intermediate result through the model's context. Example: downloading a meeting transcript from Google Drive and attaching it to a Salesforce record forces the full transcript through context twice — potentially tens of thousands of extra tokens for a long meeting. Very large documents can blow past context limits entirely, breaking the workflow.

**Code execution with MCP improves context efficiency**
Instead of exposing tools as direct function calls, represent MCP servers as a code API — each tool becomes a typed file/interface in a virtual file tree that the agent writes code against, discovering tools by browsing rather than having every definition preloaded. The Drive-to-Salesforce example becomes a small piece of code that loads the transcript once and passes it directly to Salesforce without the model ever re-processing the intermediate content — in the article's numbers, this cuts token use from roughly 150,000 down to about 2,000 (~98.7% reduction). Cloudflare published a similar approach independently under the name "Code Mode," reinforcing that models handle external systems better via code than via raw sequential tool calls.

**Benefits of code execution with MCP**
- *Progressive disclosure*: models are good at exploring file systems, so tools can be loaded on demand rather than all at once; a `search_tools`-style function can return varying levels of detail (name only, name+description, full schema) to conserve context.
- *Context-efficient tool results*: code can filter/transform data before it ever reaches the model — e.g., reducing a 10,000-row spreadsheet down to just the rows that matter before returning a summary. Works for aggregation, joins across data sources, and field extraction.
- *More powerful control flow*: loops, conditionals, and error handling become normal code instead of a long chain of individual tool calls — e.g., polling or monitoring a deployment without needing to bounce back and forth between tool calls and sleeps at the agent-loop level, reducing latency since the code environment (not the model) drives the logic.
- *Privacy-preserving operations*: intermediate results stay inside the execution environment by default; the model only sees what's explicitly logged or returned. For sensitive data, the harness can tokenize PII before it ever reaches the model, letting data (e.g., customer contact info) move from a spreadsheet to a CRM without passing through the model directly.
- *State persistence and skills*: filesystem access lets agents checkpoint progress across steps, and persist working code as reusable functions in a "skills" directory — building up higher-level capabilities over time. Ties into Anthropic's broader "Skills" concept (folders combining instructions, scripts, and resources the model can reference).
- *Implementation trade-offs*: this approach requires a secured sandbox, resource limits, and monitoring — real infrastructure overhead and security considerations that plain tool-calling avoids, so the efficiency gains need to be weighed against that cost.

**Summary**
MCP provides the connective protocol for agents to reach many tools/systems, but naive tool-definition loading and unfiltered intermediate results limit efficiency at scale. These are largely familiar software-engineering problems with familiar solutions; applying code execution patterns to agent-MCP interactions brings standard programming constructs (filtering, control flow, modularity) to bear, and the authors invite the community to share further findings.
