---
title: Remote MCPs - What We Learned from Shipping
speaker: John Welsh
source: https://www.youtube.com/watch?v=0NHCyq8bBcM
themes: [tool-design-mcp, orchestration, context-engineering, enforcement-reliability, claude-code-workflows]
---

## Core Claims

1. Tool calling became reliable only in mid-2024, triggering a chaos phase of custom endpoints that duplicated context-provisioning logic across teams.
2. Every custom endpoint eventually converges to MCP's shape (get_tools, get_resources, resource elicitation) regardless of whether teams explicitly adopt it.
3. Standardizing internally on MCP as a transport-agnostic protocol is a "boring" non-differentiator that returns enormous engineering velocity.
4. The JSON RPC message spec (not the HTTP/OAuth transport layer) is MCP's core value; transport is pluggable and can be websockets, gRPC, Unix sockets, or even IMAP.
5. A centralized MCP gateway ("pit of success") makes authentication, rate limiting, audit, and credential management the path of least resistance.
6. Credential portability through the gateway enables batch jobs and internal services to inherit user context without token passing or re-authentication.
7. Standardized message formats unlock organization-wide security policies: prompt injection filtering, malicious server bans, content classification, and audit—all at one choke point.

## Patterns & Frameworks

- **Pit of success** — Make the right thing the easiest thing; everyone naturally falls into correct behavior.
- **Transport abstraction** — MCP works identically over websockets, gRPC, Unix sockets, or any read/write stream.
- **Gateway pattern** — Single entry point for all context provisioning; centralizes auth, rate limits, observability, and policy.
- **URL-based routing** — Gateway routes to internal or external MCP servers transparently; clients don't care about location.
- **Unified auth model** — OAuth handled once at gateway; consumers get portable credentials and avoid token management.
- **Standardization-layer positioning** — Solve shared infrastructure problems once (at gateway); let teams focus on business problems.

## Numbers & Specifics

- Speaker: 20 years building large-scale systems.
- Timeline: Models became reliable at tool calling mid-last year (mid-2024).
- Internal infrastructure: Supports multiple products with different billing models, token limits, usage tracking.
- Endpoints: api.anthropic.com and cloud.ai as distinct OAuth redirect targets.
- Transport options tested: Websockets, gRPC, Unix sockets, IMAP (enterprise-grade email).
- Scope: Anthropic runs internal agents (PR review bots, Slack management, LLM-backed services).

## Quotes

> "It's not a competitive advantage to be really good at making Google Drive talk to your app. It's just a thing that you need to do. It's not your differentiator."

> "Being boring on stuff like this is good."

> "MCP is really just JSON streams and how you pipe those streams around your infrastructure is a small implementation detail. That's a couple lines of code."

> "You really want to make the right way to do a thing the easiest way to do a thing and then everyone just falls into doing the right thing naturally."

> "The really nice thing about this is that because it's MCP, all of your messages are in a standardized format. So it's really easy to hook into that stream."

## Applied AI Relevance

- **Gateway as scaling pattern** — Anthropic's internal MCP gateway solves transport, auth, and policy at org scale; template for enterprise AI integrations.
- **Protocol over transport** — MCP's JSON RPC spec is the asset; how you pipe streams (websockets, gRPC, Unix sockets) is implementation detail—focus architectural decisions on message semantics, not pipes.
- **Credential model for AI workflows** — Portable user context through gateway enables batch jobs, multi-agent sessions, and service-to-service calls without re-auth or token passing—critical for non-interactive agents.
- **Standardized security enforcement** — Centralizing MCP messages at gateway enables uniform prompt injection filtering, resource access policies, and audit across all LLM-backed services—enforcement beats prompting.
