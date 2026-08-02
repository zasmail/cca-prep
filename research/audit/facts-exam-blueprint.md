# CCA-F Exam Blueprint — Official Ground Truth Fact Sheet

Audit date: 2026-07-16
Scope: Verify repo's claims about the Claude Certified Architect – Foundations (CCA-F) exam blueprint against ONLY official Anthropic-controlled properties.

**Headline finding: an official exam guide exists and is retrievable.** It is linked from `anthropic.skilljar.com` (an explicitly allowed source domain), which 302-redirects to `anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification`; that page links a PDF hosted on Anthropic's Skilljar/Everpath content CDN (`everpath-course-content.s3-accelerate.amazonaws.com`), titled **"Claude Certified Architect – Foundations Exam Guide," Version 1.0, Effective July 2026**. This is treated as the authoritative primary source below. Note the domain nuance flagged in confidence notes: the PDF itself sits on a redirect-target subdomain (`anthropic-partners.skilljar.com`) and a CDN host, not literally on the whitelisted `anthropic.skilljar.com` string — but it is one hop from that domain via an official 302 redirect with no third party in the chain, so it is treated as confirmed/official, not third-party.

Local copies saved for reference (not for redistribution — exam guide is confidential per its own NDA clause):
- `/Users/zasmail/dev/scratchpad/claude_architect/cca-prep/research/audit/exam-guide.pdf`
- `/Users/zasmail/dev/scratchpad/claude_architect/cca-prep/research/audit/terms.pdf`
- `/Users/zasmail/dev/scratchpad/claude_architect/cca-prep/research/audit/exam-policy.pdf`

---

## 1. Domain list and weights

| Claim | Repo says | Official source says | Match? |
|---|---|---|---|
| Domain 1 name/weight | "D1 Agentic Architecture ~27%" | **"Agentic Architecture & Orchestration" — 27%** | Match (repo shortens the name, weight exact) |
| Domain 2 name/weight | "D2 Tool Design ~18%" | **"Tool Design & MCP Integration" — 18%** | Match |
| Domain 3 name/weight | "D3 Claude Code Configuration ~20%" | **"Claude Code Configuration & Workflows" — 20%** | Match |
| Domain 4 name/weight | "D4 Prompt Engineering ~20%" | **"Prompt Engineering & Structured Output" — 20%** | Match |
| Domain 5 name/weight | "D5 Context Management ~15%" | **"Context Management & Reliability" — 15%** | Match |
| Total | implied 100% | 100% (stated explicitly in guide) | Match |

**Source:** Claude Certified Architect – Foundations Exam Guide, Section 4 "Exam Content Outline (Blueprint)" (PDF, linked via `anthropic.skilljar.com` → `anthropic-partners.skilljar.com`).
**Quote:** "The exam blueprint defines the content domains measured and the approximate weight of each domain on the exam... The percentages indicate the approximate proportion of scored items drawn from each domain." Table: "1 | Agentic Architecture & Orchestration | 27% / 2 | Tool Design & MCP Integration | 18% / 3 | Claude Code Configuration & Workflows | 20% / 4 | Prompt Engineering & Structured Output | 20% / 5 | Context Management & Reliability | 15% / Total 100%"
**Confidence:** Confirmed (fetched and read the PDF directly).

**Nuance:** Repo's domain names are abbreviated ("D1 Agentic Architecture" vs official "Agentic Architecture & Orchestration"; "D2 Tool Design" vs official "Tool Design & MCP Integration"). Names are not verbatim but weights and substance match exactly. Not a material discrepancy, but repo's CLAUDE.md doesn't use the exact official domain titles.

---

## 2. Exam format

| Claim | Repo says | Official source says | Match? |
|---|---|---|---|
| Question count | "60 MCQ" | **60 items** total | Match on count |
| Item type | "MCQ" (implies pure multiple-choice) | **"Multiple-choice and multiple-response items; each item states how many responses to select"** | Partial mismatch — some items require selecting multiple correct responses, not pure single-answer MCQ |
| Structure | not mentioned | **4 scenarios presented per exam, drawn at random from a bank of 6 total scenarios**, each scenario anchors several questions | New detail, not a contradiction |
| Time limit | "120 min" | **120 minutes** | Match |
| Passing score | "720/1000" | **Scaled score of 720 on a scale of 100–1,000** | Match |
| Proctored | "proctored" | **"Proctored: online proctored and/or test center, per program policy"** | Match |
| Delivery vendor | not mentioned | **Pearson VUE** (registration, scheduling, exam delivery) | New detail |
| Exam fee | not mentioned in domain table (mentioned elsewhere in repo?) | **$125 USD** | New detail, confirmed |
| Credential validity | not mentioned | **12 months from date awarded**; free non-proctored renewal assessment; full retake at full fee if lapsed | New detail |
| Result reporting | not mentioned | Pass/fail with scaled score (100–1,000) plus percent-correct by domain; domain percentages are informational only, not used for pass/fail | New detail |
| Retake policy | not mentioned | Wait 14 days after 1st fail, 30 days after 2nd, 90 days after 3rd; max 4 attempts per rolling 12-month period | New detail |
| Exam code | Repo/community commonly call it "CCA-F" | **Official exam code printed on the guide cover is "CCAR-F,"** not "CCA-F" | **Discrepancy** — the certification's plain-English name is "Claude Certified Architect – Foundations," commonly abbreviated informally as CCA-F (including by Anthropic's own marketing/URL slugs), but the guide's own "Exam code" field reads CCAR-F |

**Source:** Same Exam Guide PDF, Section 3 "Exam Details at a Glance" and Sections 10–15.
**Quote (cover):** "Claude Certified Architect – Foundations — Exam Guide. Version 1.0 · Effective July 2026 · Exam code: CCAR-F · This guide is subject to change without notice."
**Quote (format):** "Item format | Multiple-choice and multiple-response items; each item states how many responses to select" / "Exam structure | 4 scenarios drawn from a bank of 6" / "Time limit | 120 minutes" / "Delivery | Proctored: online proctored and/or test center, per program policy" / "Passing score | Scaled score of 720 on a scale of 100–1,000" / "Exam fee | $125 USD" / "Validity period | 12 months from the date the credential is awarded"
**Confidence:** Confirmed (fetched and read directly).

---

## 3. Prerequisites

**Claim:** Repo's CLAUDE.md does not list formal prerequisites in the domain table.
**Official source:** No formal/enforced prerequisite exists. The guide instead describes an "ideal candidate" profile and recommends practical experience.
**Quote:** "The ideal candidate for this certification is a solution architect who designs and implements production applications with Claude... The candidate typically has 6+ months of practical experience building with Claude APIs, Agent SDK, Claude Code, and MCP, understanding both the capabilities and limitations of large language models in production environments."
**Source:** Exam Guide, Section 2 "Intended Audience."
**Confidence:** Confirmed. No prerequisite exam, course, or credential is required to register — "6+ months experience" is a recommendation, not a gate enforced at registration.

**Access gating (separate from content prerequisites):** Registration flows through "the Anthropic Partner Academy," and the certification's own landing page URL slug is literally `.../claude-certified-architect-foundations-access-request`, implying an access-request/gating step tied to Claude Partner Network membership.
**Confidence:** Inferred (URL naming and "Partner Academy" framing strongly imply partner-gated access, but no official page states in plain language "unaffiliated individuals cannot register" — that specific phrasing was only seen in third-party summaries, not verified verbatim on an official page).

---

## 4. Cost

**Claim:** Repo doesn't specify a cost.
**Official source:** **$125 USD per attempt.** Fee applies per attempt (does not carry over across retakes); "The exam fee applies to each attempt."
**Source:** Exam Guide, Section 3 and Section 12 ("Retake policy").
**Confidence:** Confirmed.

**Unverifiable sub-claim:** Several third-party sites claim the early-access/beta price was $99, later raised to $125. No official Anthropic page confirms a $99 price point — the exam guide's own Document Control table only shows draft versions (0.1 Feb 2026, 0.2 June 2026, 1.0 July 2026) with no pricing history. **Recorded as unverifiable.**

---

## 5. Objectives per domain

**Confirmed in full.** The guide's Section 6 "Detailed Objectives by Domain" lists every domain's task statements (e.g., Domain 1 has Task Statements 1.1–1.7; Domain 2 has 2.1–2.5; Domain 3 has 3.1–3.6; Domain 4 has 4.1–4.6; Domain 5 has 5.1–5.6), each with "Knowledge of" and "Skills in" bullet lists. This content substantively matches the spirit of the repo's own module breakdown (agentic loops/stop_reason, hooks vs prompts, MCP tool design, CLAUDE.md hierarchy, prompt engineering/structured output, context management, escalation triggers), including near-verbatim anti-pattern language the repo also states (e.g., "avoiding anti-patterns such as parsing natural language signals to determine loop termination, setting arbitrary iteration caps as the primary stopping mechanism" and sentiment-based/self-reported-confidence escalation being explicitly called out as invalid).
**Source:** Exam Guide, Section 6, all sub-sections; also Section 17 "Appendix" (In-Scope / Out-of-Scope topics), which explicitly excludes: fine-tuning/training custom models, API auth/billing/account management, specific programming language/framework implementation details, MCP server deployment/infrastructure, Claude's internal architecture/training/model weights, Constitutional AI/RLHF/safety training methodology, embeddings/vector DBs, computer use, vision, streaming API internals, rate limiting/quotas/pricing calculations, OAuth/key rotation, cloud-provider-specific configs, model benchmarking, prompt-caching implementation internals, and tokenization/token-counting algorithms.
**Confidence:** Confirmed.

---

## 6. Exam scenarios (new detail not in repo's CLAUDE.md)

Six scenarios exist in the bank; 4 are drawn per sitting: (1) Customer Support Resolution Agent, (2) Code Generation with Claude Code, (3) Multi-Agent Research System, (4) Developer Productivity with Claude, (5) Claude Code for Continuous Integration, (6) Structured Data Extraction. Each scenario is mapped to specific "primary domains."
**Source:** Exam Guide, Section 5 "Exam Scenarios."
**Confidence:** Confirmed. Notably, this maps closely to the repo's own module theming (support agent, CI/CD pipeline, multi-agent, dev productivity, extraction) — the repo's fintech-flavored module set looks deliberately built to mirror these six official scenarios.

---

## 7. What other Anthropic certifications exist

| Claim | Finding |
|---|---|
| Is CCA-F Anthropic's only current technical certification? | **Yes, as of the source article's publish date.** Quote: "Claude Certified Architect, Foundations, available today for partners" is described as introducing "the first Claude technical certification." |
| Are more certifications planned? | **Yes — named audiences, not named certs.** Quote: "Later this year, we'll introduce additional certifications for sellers, architects, and developers." No specific names, codes, or dates given for these future certifications on any official page found. |
| Broader claim of "10,000+ consultants certified" | A separate, later Anthropic news post states: "more than 10,000 consultants have earned a Claude certification—a credential, held by an individual, that signals they've been trained to build and deploy Claude in production," earned via "Anthropic Partner Academy exams," with the only named exam linked being the CCA-F access-request page. The article does not explicitly confirm whether all 10,000 earned CCA-F specifically or a broader/earlier partner-training credential. |
| Compliance certifications (unrelated to the exam) | Anthropic separately holds **ISO 27001:2022, ISO/IEC 42001:2023, SOC 2 Type I & II, and HIPAA-ready configuration (BAA available)** — these are *company* compliance certifications, not individual technical credentials, and are unrelated to CCA-F. |

**Sources:**
- https://www.anthropic.com/news/claude-partner-network — published **March 12, 2026**. Quote: "We're committing an initial $100 million to this network for 2026" / "Claude Certified Architect, Foundations, available today for partners" / "This is a technical exam for solution architects building production applications" / "Later this year, we'll introduce additional certifications for sellers, architects, and developers."
- https://www.anthropic.com/news/services-track-partner-hub — published **June 3, 2026**. Quote: "more than 10,000 consultants have earned a Claude certification—a credential, held by an individual, that signals they've been trained to build and deploy Claude in production."
- https://support.claude.com/en/articles/10015870-what-certifications-has-anthropic-obtained — compliance certs list (ISO 27001:2022, ISO/IEC 42001:2023, SOC 2 Type I & II, HIPAA-ready/BAA).

**Confidence:** Confirmed for all quotes above (fetched and read directly).

---

## 8. Launch date and investment figure

- **$100 million** committed to the Claude Partner Network for 2026 (this funds partner enablement broadly, not the exam specifically — the guide doesn't say the $100M funds the certification program itself).
  **Source:** anthropic.com/news/claude-partner-network. **Confidence:** Confirmed.
- **March 12, 2026** — publish date of the article announcing the partner network investment and that CCA-F is "available today for partners." This is the best available official evidence of a launch date; the exam guide itself is versioned separately (v0.1 Feb 2026 draft, v0.2 June 2026, v1.0 July 2026) and does not itself state a "launch" date, only guide-revision dates.
  **Confidence:** Confirmed for the article's publish date; inferred that this corresponds to the actual certification launch (the article phrasing "available today" strongly implies same-day launch, but no separate official "certification launched on X date" announcement was found).

---

## Full fact list with source/quote/confidence (flat table)

| # | Claim | Source URL | Quote | Confidence |
|---|---|---|---|---|
| 1 | Certification full name is "Claude Certified Architect – Foundations" | anthropic-partners.skilljar.com exam guide PDF | "Claude Certified Architect – Foundations Exam Guide" | Confirmed |
| 2 | Official exam code is CCAR-F, not CCA-F | Exam Guide cover page | "Exam code: CCAR-F" | Confirmed |
| 3 | Exam guide version 1.0, effective July 2026 | Exam Guide cover / §18 Document Control | "Version 1.0 · Effective July 2026" | Confirmed |
| 4 | 5 domains, weights 27/18/20/20/15 = 100% | Exam Guide §4 | table quoted above | Confirmed |
| 5 | 60 items, multiple-choice AND multiple-response | Exam Guide §3 | "Multiple-choice and multiple-response items; each item states how many responses to select" | Confirmed |
| 6 | 4 of 6 scenarios drawn per exam | Exam Guide §3, §5 | "4 scenarios drawn from a bank of 6" | Confirmed |
| 7 | 120-minute time limit | Exam Guide §3 | "Time limit \| 120 minutes" | Confirmed |
| 8 | Passing score 720 on 100–1,000 scale | Exam Guide §3, §10 | "Scaled score of 720 on a scale of 100–1,000" | Confirmed |
| 9 | Proctored (online and/or test center) via Pearson VUE | Exam Guide §3, §11 | "Proctored: online proctored and/or test center, per program policy" | Confirmed |
| 10 | Exam fee $125 USD | Exam Guide §3 | "Exam fee \| $125 USD" | Confirmed |
| 11 | Credential valid 12 months; free renewal assessment | Exam Guide §15 | "valid for 12 months from the date it is awarded... complete a free, non-proctored assessment" | Confirmed |
| 12 | Retake waits: 14/30/90 days; max 4 attempts/12 months | Exam Guide §12 | "Waiting periods increase with each failed attempt: 14 days after the first, 30 days after the second, and 90 days after the third... up to four times within a rolling twelve-month period" | Confirmed |
| 13 | No formal prerequisite; recommend 6+ months experience | Exam Guide §2 | "The candidate typically has 6+ months of practical experience..." | Confirmed |
| 14 | Registration is via Anthropic Partner Academy + Pearson VUE | Exam Guide §11 | "Registration and scheduling are handled through the Anthropic Partner Academy and Pearson VUE" | Confirmed |
| 15 | CCA-F is Anthropic's first Claude technical certification, available for partners | anthropic.com/news/claude-partner-network | "Claude Certified Architect, Foundations, available today for partners" | Confirmed |
| 16 | $100M committed to Claude Partner Network for 2026 | anthropic.com/news/claude-partner-network | "We're committing an initial $100 million to this network for 2026" | Confirmed |
| 17 | Article (best proxy for launch) published March 12, 2026 | anthropic.com/news/claude-partner-network | dateline "Mar 12, 2026" | Confirmed |
| 18 | More certifications ("sellers, architects, developers") planned later in 2026; none named yet | anthropic.com/news/claude-partner-network | "Later this year, we'll introduce additional certifications for sellers, architects, and developers" | Confirmed |
| 19 | 10,000+ consultants have earned "a Claude certification" via Partner Academy exams | anthropic.com/news/services-track-partner-hub (June 3, 2026) | "more than 10,000 consultants have earned a Claude certification" | Confirmed (quote); not confirmed which specific exam(s) count toward this figure |
| 20 | Anthropic's compliance certs (unrelated to CCA-F): ISO 27001:2022, ISO/IEC 42001:2023, SOC 2 Type I/II, HIPAA-ready | support.claude.com/en/articles/10015870 | "ISO 27001:2022... ISO/IEC 42001:2023... SOC 2 Type I & Type II" | Confirmed |
| 21 | Exam covers Claude Code, Claude Agent SDK, Claude API, and MCP | Exam Guide §1 | "tests foundational knowledge across Claude Code, the Claude Agent SDK, the Claude API, and Model Context Protocol (MCP)" | Confirmed |
| 22 | Explicit out-of-scope topics (fine-tuning, billing, model internals, computer use, vision, streaming, rate limits, cloud configs, benchmarking, tokenization, etc.) | Exam Guide §17 Appendix | "The following related topics will not appear on the exam: ... Fine-tuning Claude models... API authentication, billing, or account management..." | Confirmed |

---

## Unverifiable

- **$99 early-access price** for the exam (claimed by multiple third-party prep sites as the pre-June-2026 price before it rose to $125). No official Anthropic page or the exam guide's own version history states a $99 price. Recorded as unverifiable per source rules.
- **Exact certification launch date as a discrete, officially-labeled "launch."** The March 12, 2026 article is the strongest official evidence ("available today for partners") but Anthropic has not published a page that explicitly says "the CCA-F certification launched on March 12, 2026" in those words.
- **Whether the certification is strictly and exclusively closed to non-partner individuals** ("you cannot register as an unaffiliated individual"). Strongly implied by the "Anthropic Partner Academy" registration flow and the `access-request` URL slug, but no official page states this restriction in plain, quotable language.
- **Whether the $100 million partner-network investment specifically funds the certification program** (vs. partner enablement broadly, e.g., co-marketing, technical support, services track). The official article ties the $100M to the network generally, not to the exam.
- **Exact count of how many of the "10,000+ consultants"** hold CCA-F specifically vs. some earlier/broader Anthropic Partner Academy credential — the article does not disambiguate.
- **A dedicated `claude.com/resources/certifications` overview page** — this URL 404s; no working official aggregator page listing "all Anthropic certifications" was found. The only two working official entry points found are the Skilljar course page (for CCA-F itself) and the two news articles (context/announcements).
