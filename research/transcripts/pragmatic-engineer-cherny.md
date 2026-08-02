---
title: "Building Claude Code with Boris Cherny"
speaker: "Boris Cherny (Head of Claude Code, Anthropic), interviewed by Gergely Orosz"
source: https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny
retrieved: 2026-07-16
method: webfetch
status: ok
note: >
  Anthropic's copyright policy limits verbatim reproduction of third-party
  copyrighted text. This file is a substantive, structured SUMMARY of the
  publicly visible newsletter/podcast page (not a verbatim transcript copy).
  No paywall was detected on the page itself, but the full spoken transcript
  (audio/video) was not reproduced verbatim here — only key points, direct
  short quotes, and structure are captured.
---

# Building Claude Code with Boris Cherny

**Publication:** The Pragmatic Engineer (Substack), published March 4, 2026
**Host:** Gergely Orosz
**Guest:** Boris Cherny — Head of Claude Code at Anthropic; previously a Principal Engineer at Meta for five years; author of *Programming TypeScript*.

## Background

Boris joined Anthropic to lead development of Claude Code after his time at Meta, where he had previously worked on internal tooling and automated code-review lint rules.

## Key Discussion Points (paraphrased)

1. **Personal productivity at scale** — Boris describes shipping roughly 20–30 pull requests a day by running around five parallel Claude Code instances at once.

2. **Codebase quality compounds** — Clean, consistently-migrated codebases produce measurable double-digit productivity gains when paired with AI coding agents; partially-migrated codebases confuse both humans and models alike.

3. **Search over RAG** — Claude Code's codebase search relies on simple, model-driven glob/grep operations rather than a retrieval-augmented-generation (RAG) pipeline with embeddings.

4. **Automation precedent from Meta** — Boris had previously noticed repetitive human code-review feedback and turned it into automated lint rules — a pattern he brought forward into how Claude Code approaches review automation.

5. **Flat organizational structure** — Anthropic uses a single, uniform "Member of Technical Staff" title across the org, intentionally blurring the lines between product, design, and infrastructure responsibilities.

6. **Claude Cowork build speed** — Built in roughly ten days; the team prioritized safety guardrails (classifiers, protections against destructive file operations) given the target audience includes non-technical users.

7. **Prototypes over PRDs** — On the Claude Code team, working prototypes have effectively replaced traditional written Product Requirement Documents as the main artifact for aligning on what to build.

8. **Context-switching as the new engineering skill** — The interview frames modern high-leverage engineering as being about managing several parallel agent workstreams rather than sustained, single-threaded deep work.

9. **Infrastructure leverage** — Fixing foundational/platform-level issues is repeatedly described as higher-leverage than shipping surface-level features.

10. **Printing-press analogy** — Boris draws a historical parallel: the printing press displaced scribes, but many scribes went on to become authors; he suggests software engineers may see an analogous expansion of what they're able to build and reach, rather than simple displacement.

## Available Resources (per source page)
- Video available on YouTube, Spotify, and Apple Podcasts
- Timestamped chapters spanning roughly 11:15 to 1:35:24
- Related Pragmatic Engineer "deepdive" posts linked from the page
- Reference list of speakers' social handles and resources mentioned in conversation

## Limitation
This is a condensed, paraphrased summary of the publicly available page content, not a full verbatim transcript. For the complete spoken conversation, consult the linked audio/video directly.
