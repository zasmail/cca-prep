---
title: "Engineering at AI Speed: Lessons from the First Agentically Accelerated Software Project"
speaker: "Adam Wolff (Engineer, Claude Code team, Anthropic)"
source: https://www.infoq.com/presentations/engineering-ai/
retrieved: 2026-07-16
method: webfetch
status: ok
note: >
  Anthropic's copyright policy limits verbatim reproduction of third-party
  copyrighted text. This file is a substantive, structured SUMMARY of the
  InfoQ presentation page content (talk abstract + key points + short direct
  quotes), not a verbatim line-by-line transcript copy, even though InfoQ's
  page reportedly hosts a full transcript with no login required.
---

# Engineering at AI Speed

**Event:** QCon San Francisco 2025
**Speaker:** Adam Wolff, engineer on the Claude Code team at Anthropic
**Talk duration:** 51:21

## Abstract (paraphrased)

Wolff argues that AI coding assistance fundamentally shifts the software development bottleneck away from implementation and toward architectural decision-making. Drawing on three case studies from building Claude Code, he makes the case that rapid experimentation and real user feedback beat extensive upfront planning once the cost of writing code approaches zero.

## Core Thesis

> "the speed of learning becomes the only competitive advantage"

When implementation is nearly free, traditional long design phases give way to fast iteration loops grounded in actual user behavior rather than speculative design docs.

## Three Case Studies from Claude Code Development

1. **Terminal input handling ("Cursor Class")** — The team rebuilt terminal cursor/input handling from scratch despite conventional wisdom warning against it. Unicode-related edge cases surfaced gradually and required ongoing refactoring — an example of complexity that only reveals itself once you start building.

2. **Shell implementation** — An initial design using a single persistent shell process had to be replaced with transient, per-command shells to support parallel execution. Wolff's framing: "you discover the requirements by poking at them" rather than by specifying them fully in advance.

3. **SQLite-backed persistence** — A roughly two-week experiment to add SQLite-based persistence, involving native dependencies, was ultimately abandoned. Presented as a case study in recognizing sunk cost and cutting losses on an approach that wasn't working.

## Closing Insight

> "when the implementation cost goes to zero, the feedback loop becomes everything"

## Limitation
This is a condensed summary and selection of short direct quotes from the talk, not a full verbatim transcript. Per copyright policy, the complete spoken transcript is not reproduced here — consult the InfoQ presentation page directly (https://www.infoq.com/presentations/engineering-ai/) for the full text/video.
