---
title: "Anthropic and the Model Context Protocol, with David Soria Parra"
speaker: David Soria Parra (Anthropic, MCP co-creator), interviewed by Jordi Mon Companys
source_url: https://softwareengineeringdaily.com/2025/05/13/anthropic-and-the-model-context-protocol-with-david-soria-parra/
transcript_url: https://softwareengineeringdaily.com/wp-content/uploads/2025/04/SED1836-Anthropic.txt
podcast: Software Engineering Daily, Episode 1836
published: 2025-05-13 (episode published; transcript file dated April 2025)
retrieved: 2026-07-16
method: webfetch of episode page; direct fetch of linked transcript .txt file (summarized, not verbatim, per copyright policy)
---

# Anthropic and the Model Context Protocol, with David Soria Parra

> Note: SED publishes a full plain-text transcript at the linked URL above (I confirmed it's
> public and fetched it in full). Per copyright policy this file is a detailed, substantially
> shortened summary in my own words rather than a verbatim reproduction of that transcript.

## Background: how Soria Parra got into software
Self-taught starting around age 14 building small PHP websites (guest books, forums), he got
pulled into the wider PHP community by local mentors and began contributing patches to PHP's C
core in the early 2000s. That "find a bug in a big open-source project, fix it, move it forward"
habit carried him from PHP into version control: he chose to work on Mercurial rather than Git,
partly because Mercurial (written in Python, with an easy extension mechanism) was simpler to
hack on than Git's C core, and partly because he found the Mercurial community more welcoming
than the rougher, Linux-kernel-adjacent Git community of that era.

## Path to Facebook/Meta
He was recruited into Facebook's infrastructure team through the Mercurial community around
2012, when Facebook was choosing Mercurial as its long-term VCS to support its monorepo strategy
(similar to Google's approach). He relocated from Germany to Vancouver and then the Bay Area. He
explains Facebook's unusual stack (custom PHP dialect, Mercurial, Buck) as a rational response to
scale: once a monorepo and a language choice are load-bearing at that size, it's cheaper to build
dedicated teams that optimize the existing stack (source control, build systems, PHP performance)
than to migrate the whole company to a different language or repo structure.

## Oculus integration
After Facebook acquired Oculus in 2015, Soria Parra helped integrate Oculus's traditional
gaming-industry toolchain (Perforce for large binary assets, stateful CI that caches built game
engines, Windows-based development) into Facebook's web-oriented, Linux-first, ephemeral-CI
infrastructure — a large cross-platform integration effort he describes as fascinating but not
always fun.

## MCP origin (same core story as the a16z interview, with LSP detail added)
Joining Anthropic in April 2024 to work on internal developer tooling, he hit the same Claude
Desktop (rich visualization, no external access) vs. Zed (file access, no visualization) wall
described elsewhere, framed again as a classic M×N client/provider integration problem needing a
shared protocol. The added detail here: he had recently been building an internal experimental
LSP (Language Server Protocol) implementation at Anthropic, which is what led him to model MCP
directly on LSP's design — reusing its JSON-RPC-based invoke/response/error pattern and its
initialization/capability-exchange handshake (he also credits some of that handshake thinking to
Mercurial's push/pull protocol). He proposed the idea to Justin Spahr-Summers, who built it into
Claude Desktop while Soria Parra built it into Zed, in parallel, as a two-person bottom-up
project.

## LSP explained
For listeners unfamiliar with LSP: before ~2015, every IDE had to write its own parser/tooling
for every language. Microsoft's Language Server Protocol let one team write a single Python (or
Java, etc.) language server that any LSP-compliant IDE (VS Code, JetBrains, Zed, ...) could plug
into, solving the same N×M problem for IDE-language integrations that MCP now aims to solve for
AI-application-to-context-provider integrations.

## Protocol mechanics
MCP is JSON-RPC based (invoke / response / error), with an initialization sequence where client
and server exchange capabilities. Three server-side primitives: tools (model-invoked), resources
(file/blob-like data an application can choose how to use), and prompts (user-driven templates,
which can be static or dynamically backed by an API call). Despite the name, MCP "servers" are
most commonly local programs running on the user's machine, not remote services — the term is
about serving context upward to the client, not about network location. Servers are full stateful
programs if they need to be (his example: a server that manages a shopping-basket-like state
behind "add to basket" / "list basket" tools).

## Discovery
No built-in discovery mechanism yet — finding a server that does what you want is a manual,
search-the-web process today. A centralized registry is being explored to address this, partly
because indiscriminately downloading and running arbitrary code from the internet is itself a
security concern.

## Reflecting on the ecosystem's growth
Soria Parra says he didn't expect the scale of adoption (unprompted attention from major company
CEOs, adoption discussions at Google/OpenAI) and finds it both exciting and stressful. Governance
is still informal and merit-based, similar to his PHP/Mercurial days — SDK maintainers include the
Pydantic team (Python), Microsoft (C#), the Spring team (Java), and JetBrains (Kotlin), with a Go
SDK expected. He says the project is actively working toward a more formal governance model
(possibilities discussed include something like a foundation) as larger companies get involved,
because MCP's value depends on staying an ecosystem competitors can all trust equally.

## Near-term roadmap, per Soria Parra
Three concrete asks he hears most: (1) authorization for remote/cloud-hosted servers — an initial
spec exists but needs enterprise-grade rework, done in collaboration with identity experts from
Microsoft, AWS, and Okta; (2) better support for horizontally scaling servers in stateless/cloud
deployments, where the spec is mostly right but SDK implementations lag; (3) more streaming
support. Beyond that, he's watching how agent-level abstractions might layer on top of MCP,
without yet having a firm opinion on whether MCP itself needs to grow new primitives for that.

## Sampling, revisited
Same underused-feature pitch as in the a16z interview: sampling lets a server request a
completion from whichever model the client currently has configured rather than embedding its
own model SDK, enabling chains of MCP clients/servers that form graphs of composable,
model-independent agent logic — something he says is barely explored because most clients
currently only implement tool calling.

## Tools vs. agents vs. A2A
Asked directly whether there's a clean boundary between "tools" and "agents," Soria Parra says
that's still unresolved — tools are likely necessary for agents but he's not convinced they're
sufficient. On Google's newly announced A2A protocol (released the same week as this interview),
he doesn't see it as competing with MCP so much as potentially complementary, drawing an analogy
to how OCI containers are foundational to the Kubernetes ecosystem without being the entire
ecosystem themselves.

## Advice for engineers getting started
Install an SDK (Python, TypeScript, C#, Java, Kotlin, and eventually Go are all mentioned) and
build something you personally want first — his own example is a small MCP server that reads his
Steam library to help him and friends pick a game to play together — then go read the spec
properly rather than relying on secondhand Twitter takes. For contributing back: SDK bug fixes,
issue triage, and documentation are the accessible entry points; spec-level pull requests carry a
much higher bar (a well-argued RFC).

---
*Word count of this summary: ~1,050 words (source transcript file is roughly 9,200 words).*
