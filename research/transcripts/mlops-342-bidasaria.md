---
title: "Building Claude Code: Origin, Story, Product Iterations, & What's Next"
speaker: Siddharth Bidasaria (Member of Technical Staff, Anthropic) — interviewed by Demetrios Brinkmann (MLOps Community)
source_url: https://home.mlops.community/public/videos/building-claude-code-origin-story-product-iterations-and-whats-next
episode: MLOps Community Podcast #342
retrieved: 2026-07-16
method: websearch+webfetch
status: ok (partial — reconstructed from the official show page; not confirmed as literal word-for-word transcript)
---

# Limitation notice

The official MLOps Community show page for this episode presents timestamped transcript-style
content, which is reproduced/paraphrased below with direct quotes kept in quotation marks exactly
as rendered on the page. Two other listed mirrors (Metacast, which advertised a transcript)
returned HTTP 403 and could not be fetched to cross-check completeness. Treat quoted lines as
verbatim excerpts from the source page and unquoted narration between them as paraphrase/summary
bridging the gaps, not a certified full transcript.

## Episode metadata
- **Title:** Building Claude Code: Origin, Story, Product Iterations, & What's Next
- **Episode:** MLOps Community Podcast #342
- **Guest:** Siddharth Bidasaria, Member of Technical Staff @ Anthropic
- **Host:** Demetrios Brinkmann, Chief Happiness Engineer @ MLOps Community
- **Also on:** [Spotify](https://open.spotify.com/episode/4FUtoXvGjuDvZvCm1JwHdt), Apple Podcasts

## Content (reconstructed, timestamped where available on source page)

**[00:00:34] Genesis of Claude Code.** Bidasaria describes the origin as coming out of
Anthropic's Labs team, which prototypes new products. A colleague, Boris (Cherny), built a
prototype that accessed Claude from a terminal and added two key tools: Spotify control and file
read/write capability. Bidasaria: "The moment he added that, he shared it with us. I was like,
holy shit." ... "It was just like, instantly I was like, there's something here. It feels really
ergonomic." The team released it internally at Anthropic; within two weeks it had 300 active
daily users at a 600-person company. Strong internal attachment led to launching an external
Early Access Program, which then grew organically via social media.

**[00:05:46–00:07:30] Why file tools changed everything.** Prior products required
synchronization/setup — copying files, building Docker images, sharing repos. Bidasaria: "It's
just. What matters is that you have the files locally." ... "You can just spin up Claude, ask it
to read a bunch of files, ask it to explore kind of how a human would. It just felt really
magical. It just felt really low friction."

**[00:07:45] Favorite feature: the to-do list.** Bidasaria: "I think my favorite feature that I
added would probably be honestly, like, the to do list." ... "It feels satisfying, you know,
like, best feeling ever. Like, it's just doing all this stuff for me. I'm just watching." The
to-do list helps the model stay on track for longer-horizon tasks — instead of stalling after
~30 files, it first creates a to-do list, batching e.g. 100 files into batches of 10 and checking
them off.

**[00:09:58] Model jumps.** Bidasaria: "Oh, a hundred percent, 100%, I think. I think 3, like, 35
was pretty good. And. But 37 is kind of like where things really started to come together." —
describing a step change in the complexity of tasks the model could handle between model
versions (referred to informally as "35" and "37").

**[00:14:48] Team philosophy: deleting code.** "One of the core, like, philosophies of our team
is we absolutely love deleting code and, like, taking and just deleting features." The team
calls this "unhobbling the model" — letting it work naturally instead of steering it with
narrow, hand-built tools. Example: rather than many filesystem-specific tools, they gave the
model a general BASH tool, since "we can just literally just give it the BASH tool and it, like,
will know it can just do all of these things just through the abstraction of a BASH command."

**[00:17:57] Hooks.** Hooks let users inject code into Claude Code's lifecycle — e.g. a
pre-tool-call hook is "a piece of code that the harness runs before each tool call," usable for
things like logging every tool call via a bash script or other code that receives parameters
about which tool is being called.

**[00:26:13–00:30:18] Verification.** Bidasaria splits the verification problem into two parts:
"Model behavior. Like does the model know that to check its work regularly and can it elicit
that behavior? And the second is, do you have the tools or have you given the models the tools
to effectively check its own work?" For web development, MCP servers like Puppeteer let the model
take screenshots and iterate on them. Harder cases remain, e.g. verifying animations. On
practical advice: "The one thing that I will for sure do is make sure that I have a unit testing
framework that is able to test as large of a surface area as possible of my code" — unit tests as
the shortest path to reliable verification.

**[00:33:38] Power users.** The most surprising case: one user running "a fleet of 10 to 12
clods for one problem," using the filesystem for instances to communicate and assigning each
instance a persona (backend engineer, frontend engineer, etc.) — this reportedly inspired the
sub-agents feature. Also: "I've seen people with like 100 MCP servers installed or something like
that, and I was like, what do you even do with 100 MCP servers? But hey, it works for them."

**[00:36:18–00:39:35] Sub-agents' future.** Currently sub-agents act as tools within a main
thread. Bidasaria muses about more complex topologies: "What if you just had like, you know, a
master, master model where you had like multiple sub agents kind of all doing their own thing,"
communicating peer-to-peer — raising open questions like message-bus vs. point-to-point
communication and timing of message injection. He's cautious: "it is unclear to me right now
whether some of these more complex agent or sub agent topologies lead to better results... I'm
hesitant in kind of adding that complexity" absent evidence a given topology works well.

**[00:39:55] What excites him most.** Beyond power users, "what's more exciting is like there's
this whole other spectrum of users who are just like, just about, you know, just getting their
feet wet with this."

**[00:42:29–00:44:02] Permissions and sensitive data across sub-agents.** "Observability is
really hard for complex subagent topologies. And because of that, as a result of that, how you
do permission management and how you do that kind of becomes complex too." Currently, any
sub-agent hitting a tool it lacks permission for bubbles up and asks the user — which Bidasaria
flags as not scalable: it "works because... the sub agent implementation we have is quite
simple," but wouldn't scale to more complex agent topologies.

**[00:47:07] Dynamic permissions.** As models get smarter, Bidasaria expects more reliance on the
model itself (the "Eye of Sauron agent") to understand user intent and grant dynamic permissions
rather than hardcoded rules.

**[00:47:20] Research ties.** The Claude Code team stays closely connected to Anthropic's
research org — a two-way flywheel where "what you learn from user behavior and what you learn
from product usage kind of like feeds back into research and what the research priorities are
going forward."

**[00:49:32] Investment in coding.** "I think Anthropic has leaned into coding for a few model
releases. Now that's not to say that there's not other stuff happening, but there's definitely is
kind of a focus on coding just because models are really good at... coding."

## Key takeaways (per source page)
- Claude Code emerged from Labs-team experimentation (Boris Cherny's terminal prototype).
- File tools + local file access were the breakthrough that made it feel "magical" and low
  friction.
- The to-do list feature was central to sustaining long-horizon task completion.
- Model capability step-changes occurred between named model versions ("35" to "37").
- Team philosophy favors deleting bespoke tools/code in favor of general abstractions (e.g. BASH)
  — "unhobbling the model."
- Verification is unsolved in general; unit tests are the pragmatic default; screenshot-based
  MCP tools (e.g. Puppeteer) help for web UI.
- Power-user behavior (fleets of parallel Claude instances with assigned personas) directly
  inspired the sub-agents feature.
- Permission management doesn't yet scale to complex multi-agent topologies; the team is waiting
  for stronger evidence before adding that complexity.

## What's missing
The Metacast mirror (which advertised a transcript) returned HTTP 403 and could not be
cross-checked. Any dialogue outside the timestamped segments captured on the official show page
was not recoverable from public text sources at time of retrieval.
