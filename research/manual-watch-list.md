# Manual Watch List

*Content that still could NOT be transcript-harvested — auth-gated, login-gated, paywalled, or blocked by YouTube IP bans. Ranked by watch priority for Anthropic Applied AI interview prep + CCA-F. Watch these on a residential connection / logged-in account.*

**Why manual:** the harvest environment's cloud IP is blocked by YouTube for automated transcript extraction (youtube-transcript-api 403 / HTTP 429 / SABR streaming protection / yt-dlp page-reload errors), and Goldcast webinars + course platforms are behind auth with no transcript API.

> **Drip-pass note (2026-07-16 evening):** a slow residential-IP pass (`research/drip_harvest.py`, 1 video / 15 min, resume-safe) recovered **10 more**: earlier tonight `how-we-build-effective-agents`, `karpathy-vibe-to-agentic`, `karpathy-software-is-changing`, `agents-run-for-hours`, `reinvent-long-horizon-agents`, `no-priors-karpathy-loopy-era`, `cowork-gtm-workshop-workos`; this pass `cwc-2025-keynote` (13k words), `prompting-for-agents` (6.2k), `vibe-coding-in-prod` (5.9k) — all in `research/transcripts/`. Then YouTube rate-limited the IP (2× IpBlocked), so the pass was stopped. **Still pending (rerun `python3 research/drip_harvest.py` after a day's cooldown):** `cwc-2026-tokyo-keynote`, `cwc-2026-london-keynote`, `karpathy-how-i-use-llms`, `karpathy-deep-dive-llms`, `karpathy-state-of-gpt`. Permanently gone: `beyond-basics-claude-code` (subtitles disabled) and likely `cwc-2026-sf-keynote` (same). The Tier rankings below predate these recoveries — items 2, 6, and 11 are now recovered.
>
> **Older delta-pass note (2026-07-16, cloud IP):** that run added **0 new sources**. This list has been pruned to the items that remain genuinely blocked; entries that already have notes in `research/notes/` (e.g. the Dwarkesh–Karpathy episode, live-coding-cherny-sumner, behind-craft-* interviews, training-data-cherny) have been removed. The 27 items below are the still-failed set. Note that much of the *payload* of the blocked Karpathy talks is already captured in the recap notes that back [karpathy-mental-models.md](../wiki/karpathy-mental-models.md) (sequoia-recap, animals-vs-ghosts, llm-wiki, x-posts) — re-watch the source talks only for nuance and exact quotes.

---

## Tier 0 — Watch first (highest interview leverage)

1. **Code with Claude 2026: Opening Keynote (SF)** — `cwc-2026-sf-keynote` — *YouTube `wjvESxKgqaQ`, subtitles disabled.* Latest official product/vision framing; freshest canon on agents + Cowork.
2. **Code with Claude Opening Keynote (2025)** — `cwc-2025-keynote` — *YouTube `EvtPBaaykdo`, IP-blocked.* The foundational keynote much of the corpus references.
3. **How we build effective agents** (Anthropic) — `how-we-build-effective-agents` — *YouTube `D7_ipDqhtwk`, IP-blocked.* Video companion to the most-cited blog post; verify the five-patterns framing in the authors' own words. Blog payload already in [blog-building-effective-agents](notes/blog-building-effective-agents.md); extends [orchestration-patterns.md](../wiki/orchestration-patterns.md).

## Tier 1 — High value

4. **Karpathy — "From Vibe Coding to Agentic Engineering"** (Sequoia AI Ascent 2026) — `karpathy-vibe-to-agentic` — *YouTube `96jN2OCOfLs`, IP-blocked.* Sharpens the vibe-vs-agentic distinction central to [karpathy-mental-models.md](../wiki/karpathy-mental-models.md); recap already mined in [karpathy-sequoia-recap](notes/karpathy-sequoia-recap.md).
5. **Karpathy — "Software Is Changing (Again)"** (YC AI Startup School 2025) — `karpathy-software-is-changing` — *YouTube `LCEmiRjPEtQ`, IP-blocked.* The Software 3.0 / LLM-as-OS-kernel source talk; payload captured in [karpathy-x-posts](notes/karpathy-x-posts.md).
6. **Prompting for Agents** (Anthropic) — `prompting-for-agents` — *YouTube `XSZP9GhhuAc`, IP-blocked.* Agent-era prompt engineering; extends [prompting-101](notes/prompting-101.md) and [context-engineering.md](../wiki/context-engineering.md).
7. **Code with Claude 2026: Tokyo Keynote** — `cwc-2026-tokyo-keynote` — *YouTube `N4efO8viXXo`, HTTP 429.* Regional keynote; likely overlaps SF but may add detail.
8. **Code with Claude 2026: London Keynote** — `cwc-2026-london-keynote` — *YouTube `6amLO7I9xdg`, HTTP 429.* Same as above.
9. **No Priors — Ben Mann** — `no-priors-ben-mann` — *YouTube, IP-blocked (429).* Anthropic co-founder on safety + product direction; useful for "strong opinions" framing.
10. **Beyond the Basics with Claude Code** — `beyond-basics-claude-code` — *YouTube `tuY2ChJIx48`, IP-blocked.* Deepens [claude-code-workflows.md](../wiki/claude-code-workflows.md) (parallel sessions, headless/CI, hooks).
11. **Vibe Coding in Production** — `vibe-coding-in-prod` — *YouTube `fHWFF_pnqDk`, IP-blocked.* Production-grade agentic engineering discipline; complements [enforcement-reliability.md](../wiki/enforcement-reliability.md).

## Tier 2 — Worth it if time allows

12. **Karpathy — "How I Use LLMs"** — `karpathy-how-i-use-llms` — *YouTube `EWvNQjAaOHw`, IP-blocked.* Mental-model reinforcement; load-bearing ideas already in the wiki.
13. **Karpathy — "Deep Dive into LLMs like ChatGPT"** — `karpathy-deep-dive-llms` — *YouTube `7xTGNNLPyMI`, IP-blocked.* Fundamentals deep-dive; wiki captures the payload.
14. **No Priors — Karpathy "loopy era"** — `no-priors-karpathy-loopy-era` — *IP-blocked.* Re-watch only for nuance beyond the Dwarkesh episode (already noted).
15. **Cowork GTM Workshop (WorkOS)** — `cowork-gtm-workshop-workos` — *YouTube, IP-blocked.* Partner GTM workshop; adjacent to [gtm-applications.md](../wiki/gtm-applications.md).
16. **Spotify × Anthropic — agentic dev** — `spotify-anthropic-agentic-dev` — *YouTube, IP-blocked.* Enterprise adoption case study.
17. **Agents Run for Hours** — `agents-run-for-hours` — *IP-blocked.* Long-horizon reliability; overlaps checkpointing content in [orchestration-patterns.md](../wiki/orchestration-patterns.md).
18. **re:Invent — Long-Horizon Agents** — `reinvent-long-horizon-agents` — *IP-blocked.* Same theme as above.
19. **SPC — Rahul Patil** — `spc-rahul-patil` — *IP-blocked.* Fireside; lower direct interview leverage.

## Tier 3 — Cloud/platform (nice-to-have, role-dependent)

20. **Building with Claude on Google Cloud** — `claude-on-google-cloud` — *IP-blocked.* Platform-specific; relevant only if the role touches GCP.
21. **Building AI agents with Claude in Vertex AI** — `vertex-ai-agents-webinar` — *IP-blocked.* Same as above.

## Explicitly skipped / low-value (foundational teaching series — not interview-load-bearing)

The mental-model payload of these is already in [karpathy-mental-models.md](../wiki/karpathy-mental-models.md); watch only for teaching depth on fundamentals.

22. **Karpathy — "Intro to LLMs"** — `karpathy-intro-to-llms` — *IP-blocked.*
23. **Karpathy — "State of GPT" (2023)** — `karpathy-state-of-gpt` — *YouTube `bZQun8Y4L2A`, manual en-US captions only.*
24. **Karpathy — "CS25: Transformers"** — `karpathy-cs25-transformers` — *IP-blocked.*
25. **Karpathy — "Let's Build GPT"** — `karpathy-lets-build-gpt` — *IP-blocked.*
26. **Karpathy — "Let's Build the Tokenizer"** — `karpathy-tokenizer` — *IP-blocked.*
27. **Karpathy — Berkeley Hackathon keynote** — `karpathy-berkeley-hackathon` — *IP-blocked.*

---

### Harvest-failure appendix (for a future re-run)

- **Root cause:** environment cloud IP permanently blocked by YouTube (403 / 429 / SABR). Retry from a residential IP or with authenticated `yt-dlp` cookies.
- **YouTube IDs to retry:** `wjvESxKgqaQ`, `EvtPBaaykdo`, `D7_ipDqhtwk` (how-we-build-effective-agents), `96jN2OCOfLs` (karpathy-vibe-to-agentic), `LCEmiRjPEtQ` (karpathy-software-is-changing), `XSZP9GhhuAc` (prompting-for-agents), `N4efO8viXXo` (Tokyo), `6amLO7I9xdg` (London), `tuY2ChJIx48` (beyond-basics-claude-code), `fHWFF_pnqDk` (vibe-coding-in-prod), `EWvNQjAaOHw` (how-i-use-llms), `7xTGNNLPyMI` (deep-dive-llms), `bZQun8Y4L2A` (state-of-gpt), plus no-priors (Ben Mann, Karpathy loopy-era), spc-rahul-patil, cowork-gtm-workshop-workos, spotify-anthropic-agentic-dev, agents-run-for-hours, reinvent-long-horizon-agents, claude-on-google-cloud, vertex-ai-agents-webinar, and karpathy intro-to-llms / CS25 / lets-build-gpt / tokenizer / berkeley-hackathon.
