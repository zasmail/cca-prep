---
title: "Agent Ready Episode 8: Anthropic, Cloudflare, and Arcade — Evolving Architectures for AI Agents"
speakers: Max Gerber (Stytch, moderator), Lizzie Siegle (Cloudflare), Cal Rueb (Anthropic), Nate Barbettini (Arcade)
source_url: https://stytch.com/blog/agent-ready-ep8-anthropic-cloudflare-arcade-agent-architecture/
published: 2025-09-24
retrieved: 2026-07-16
method: webfetch (direct HTML fetch + extraction; summarized, not verbatim, per copyright policy)
---

# Agent Ready Episode 8: Evolving Architectures for AI Agents

> Note: the source page hosts a full panel transcript. Per copyright policy this file is a
> detailed, substantially shortened summary in my own words rather than a verbatim reproduction.
> The original is public at the source URL above.

Panel: Max Gerber (Stytch software engineer, moderator), Lizzie Siegle (Cloudflare developer
advocate, AI demos/AutoRAG/Vectorize/MCP deployment platform), Cal Rueb (Anthropic Applied AI
team; notes he wrote much of the Claude Code system prompt), Nate Barbettini (Arcade founding
engineer, focused on letting agents take real authenticated actions via tools).

## Defining "agent" and where they work today
Cal Rueb frames Anthropic's internal definition (citing a colleague's "Building Effective Agents"
post): give a model tools, an open-ended task, and let it call tools in a loop until it decides
it's done — as opposed to a rigid multi-step "workflow" that chains fixed prompts together.
Workflows are brittle on edge cases and recover from errors poorly; agents largely fix both
issues once the underlying model is trained to operate well in that loop.

Two domains cited as having real product-market fit today: coding assistants (developers can
watch the agent work step by step and correct course immediately — strong human-in-the-loop
fit) and deep-research products (a search tool plus a sub-agent tool, run in a big loop, that
comes back with a synthesized report). Customer support is raised as a counterexample — full
end-to-end agent autonomy is harder there because the end user typically has no visibility into
what's happening behind the scenes, so many teams still find a scripted workflow more reliable.

## Tool design principles (the panel's most repeated theme)
- Keep tool descriptions simple and action-oriented, not a 1:1 wrap of a REST API's resource
  model. Models want a "share file" action, not a sequence of GET/lookup/POST calls against a
  resource graph — directly wrapping existing REST endpoints tends to perform poorly even for
  strong reasoning models, burning tokens re-deriving how to compose calls each time.
- Validate inputs; keep outputs predictable.
- One tool, one goal — avoid cramming multiple steps into a single tool.
- Clean up raw API responses (strip irrelevant fields, rename cryptic keys) before returning them
  as tool results — described as "context engineering" on the output side, not just the input
  side.
- Don't hand a model too many endpoints/tools at once; constrain the option set. The panel's
  framing: models are smart but "lazy" — give them exactly what's needed for the task rather than
  a large menu to reason over.
- A useful design heuristic offered near the end: could a smart-but-lazy 12-year-old figure out
  how to use this tool from its description alone? If yes, a frontier model probably can too.

## MCP's role and gaps
The panel broadly agrees MCP's real value is standardization — one server implementation working
across many client apps (Claude, Cursor, ChatGPT, Windsurf) — rather than the protocol itself
being conceptually novel (function/tool calling already existed). Gaps called out:
- No built-in way for a server to signal context-window/payload-size limits back to the client;
  a server can return an arbitrarily large result that simply blows the context window, with no
  negotiation mechanism today.
- Authorization/security is still nascent, especially third-party and enterprise-grade auth
  profiles (stricter controls needed for regulated industries).
- Multi-tenancy is hard in practice — Lizzie Siegle's example is a personal tennis-court-booking
  MCP server authenticated to her own Stytch-backed credentials; extending it to other users would
  require handling their credentials too, which isn't solved cleanly yet.
- No trusted registry yet for vetting servers, which the panel expects to matter more as the
  ecosystem grows (both Microsoft and Anthropic are described as working on something in this
  space).

## Security: tool poisoning and context poisoning
The group distinguishes "context poisoning" (an attacker crafts a GitHub issue/PR that tricks an
agent with legitimate, granted access into taking a harmful action) from "tool poisoning"
(malicious instructions hidden inside an MCP server's tool description — invisible to the human
user, but read and potentially followed by the model). A proposed spec fix using signed hashes of
tool descriptions is discussed and picked apart live (the server can publish a hash of its own
compromised description, so hashing alone doesn't establish trust). The panel converges on an
app-store-style trusted-registry model as the more durable direction, while acknowledging that
approval-gated ecosystems (citing slow iOS/Android app review experiences) can reduce openness
and accessibility for smaller/indie developers. Cal Rueb notes Anthropic is also considering
model-level mitigations, like flagging user-supplied tools as lower-trust in context, while
stressing that model-level defenses alone won't fully close prompt-injection-style risks.

## Sub-agents
Anthropic uses sub-agents in two products: Claude Code (delegating research/search-heavy work to
a sub-agent that reports back a summary, protecting the main agent's context window) and Deep
Research (fanning out multiple search sub-agents that each investigate a sub-topic and report
back for a compiled report). Cal Rueb is otherwise skeptical of over-applying the multi-agent
pattern — models aren't yet good at delegation generally, and it can be overengineering outside
those two proven cases. Nate Barbettini goes further, framing sub-agents as likely a short-term
workaround for today's limited context windows rather than a durable long-term architecture,
drawing an analogy to old multi-threaded engineering patterns that became less necessary once
hardware capacity grew.

## Closing takeaways
- Build things you'd actually use yourself, even if nobody sees them.
- Invest specifically in tool description/input/output design — it materially changes whether the
  model picks the right tool and does the right thing.
- Keep using new tools yourself; the field's dominant discourse shifts fast (RAG a year prior,
  agents now).
- Today's frontier models are, per the panel, the slowest and least capable they will ever be —
  worth building for where the trajectory is heading, not just where things stand today.

## Audience Q&A
One audience question raised MCP monetization — since agent-mediated interactions bypass
traditional ad-supported browsing, is there a tipping/microtransaction model coming? Cal Rueb's
personal guess favors mundane per-publisher subscription/OAuth arrangements over crypto-style
microtransactions; Nate Barbettini suggests classic SEO will fade but be replaced by a new
discipline of getting a company's information favorably represented in models' training data. A
second question on sub-agent design tradeoffs echoes the sub-agents discussion above (how many,
how much context to give them) as still very much unsettled.

---
*Word count of this summary: ~900 words (source panel transcript is substantially longer).*
