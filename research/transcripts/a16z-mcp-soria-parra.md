---
title: "MCP Co-Creator on the Next Wave of LLM Innovation"
speaker: David Soria Parra (Anthropic, MCP co-creator), interviewed by Yoko Li (a16z)
source_url: https://a16z.com/podcast/mcp-co-creator-on-the-next-wave-of-llm-innovation/
podcast: AI + a16z
published: 2025-05-02
retrieved: 2026-07-16
method: webfetch (direct HTML fetch + extraction; summarized, not verbatim, per copyright policy)
---

# MCP Co-Creator on the Next Wave of LLM Innovation

> Note: the source page hosts a full interview transcript. Per copyright policy this file is a
> detailed, substantially-shortened summary in my own words rather than a verbatim reproduction.
> The original is public at the source URL above.

## What MCP is
Soria Parra frames MCP as a boring-on-purpose open protocol: it defines how a developer's
integration code and an AI application talk to each other, so that anyone — not just the
original app's team — can extend an AI application with the workflows they personally care
about. His stated ambition is for MCP to become something like the current API ecosystem, but
for LLM interactions. Yoko Li's analogy: before common API schemas, every SaaS integration
(Salesforce vs. HubSpot) needed its own bespoke client code; MCP aims to do the equivalent for
how agents discover and use context/tools.

## Origin story
Soria Parra joined Anthropic around April 2024 doing internal developer-tooling work. Two
frustrations converged:
- He couldn't personally build a bespoke workflow integration for every team internally — people
  needed to be able to build their own.
- He was toggling between Claude Desktop (great artifact visualization, but no way to reach
  outside the chat box to local files or external systems) and the Zed code editor (full file
  access, but none of Claude Desktop's visualization). Copy-pasting between the two was the
  breaking point.

That's the classic M-clients × N-providers integration problem, and his answer was "build a
protocol for it." He brought the idea to Justin Spahr-Summers, who co-created MCP with him:
Spahr-Summers built the first version into Claude Desktop while Soria Parra built it into Zed,
in parallel, refining the primitives through rapid prototyping arguments along the way. They
open-sourced MCP in November 2024.

The first real prototype was a Puppeteer/browser-control server — chosen because watching Claude
drive a browser live is a strong demo of "there's a lot of possibility here." The first
genuinely useful internal servers were mundane (GitHub, Postgres).

## Creative ecosystem examples discussed
Blender (natural-language-driven 3D modeling), an Ableton integration for programming
synthesizer patches, a JetBrains IDE-control server, a well-known reverse-engineering YouTuber
using Claude+MCP for binary analysis, someone hooking Claude Desktop to their Amazon account to
buy Christmas gifts via browser automation, and — from Yoko Li's own side projects — an MCP
server that flashes Philips Hue lights in Morse code to signal when a long-running coding agent
finishes a task, and a Raspberry-Pi camera project that narrates/yells at her cats, which she's
converting into an MCP client so it can chain into an ElevenLabs MCP server for voice.

## Underused protocol primitives
Both speakers agree tool calling is overwhelmingly what people build, and flag three other
primitives as underused:
- **Sampling** — lets an MCP server ask the client (not its own bundled SDK/API key) to run a
  completion against whatever model the user currently has configured. This keeps servers
  model-agnostic and lets them do rich things (summarization, their own mini agent loops) while
  the client retains control over inference. Adoption is limited mainly because most clients
  don't support it yet.
- **Resources** — blob/file-like data a server exposes; unlike tools (model-driven) or prompts
  (user-driven), resources are described as "application-driven" — the client app decides whether
  to inject a resource directly or run retrieval/RAG over it first.
- **Prompts** — user-driven templates a person explicitly pulls into context (as opposed to a
  tool the model decides to call); can be static or dynamically backed by an API call (example
  given: pulling a stack trace from Sentry into a prompt template).

They also discuss chaining: because an MCP server can itself act as an MCP client to other
downstream servers, you can build indefinitely deep (though practically shallow) graphs of
composed servers — effectively assembling multi-tool agent systems out of independently built
pieces.

## Transport and architecture notes
MCP is deliberately transport-independent. It started with stdio (well-suited to local lifecycle
management) using JSON-RPC, heavily inspired by the Language Server Protocol, and is evolving
toward HTTP-based remote transports so servers can run off-device.

## Authorization
Current spec work prioritizes authorization (can this client access this resource?) over
authentication/identity (who is this?), built on OAuth, developed jointly with security/identity
experts from Microsoft, Okta, and AWS. Soria Parra expects authorization support to unlock a wave
of remote, account-bound professional MCP servers (his example: a PayPal MCP server you log into
directly) while local, hacker-style servers remain part of the ecosystem.

## Governance and contributing
MCP runs as a traditional merit-based open-source project — write patches, fix bugs, triage
issues, and earn commit trust over time (the Pydantic team's help on the Python SDK is cited as
an example). Spec-level changes require a much higher bar — a detailed RFC, ideally with backing
from a company or community group. Soria Parra says the project is still feeling out a more
formal governance model as bigger companies get involved.

## Modality, agents, and trust boundaries
A tangent on generative modalities (Yoko Li's ASCII-art/Tamagotchi experiments) leads into a
direct question: how do you define an "agent"? Yoko Li's definition is simple — a multi-step LLM
reasoning chain. Soria Parra's is close but framed around agency: the moment a system reacts to
the outcome of its own prior step, it has agency. He's not confident MCP alone needs new
abstractions for agents yet, and thinks the more useful lens for where protocol boundaries matter
is **trust boundaries** rather than task complexity — e.g., a travel-booking agent that needs
bank access is a natural place for a protocol seam, versus tasks that can just stay inside one
framework. Both agree the field is too early to have settled opinions on the "right" abstraction.

## Where to help
Soria Parra points contributors toward the SDK repos (Python, TypeScript, and community-driven
C#/Java/Kotlin SDKs), issue triage, PRs, and documentation as the highest-leverage entry points,
reserving spec PRs for people willing to write a fully worked RFC.

---
*Word count of this summary: ~950 words (source interview transcript is substantially longer).*
