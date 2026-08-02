---
title: "Prompting 101 | Code w/ Claude"
speaker: "Hannah Moran & Christian Ryan, Code w/ Claude 2025"
source: "https://www.youtube.com/watch?v=ysPbXH0LpIE"
themes:
  - context-engineering
  - model-fundamentals
  - enforcement-reliability
  - prompt-engineering
  - gtm-applications
---

## Core Claims

1. Prompt engineering is an iterative, empirical science—test cases and feedback loops drive improvement, not trial-and-error guessing.
2. Structure matters more than verbosity: task description → dynamic content → detailed instructions → examples → reinforcement works reliably.
3. System prompts should contain static, reusable context (form specs, background docs) that never changes between queries.
4. Delimiters (XML tags, markdown) help Claude organize information and refer back to specific sections throughout its reasoning.
5. Few-shot examples and conversation history enrich context; real failure cases + human-validated solutions are most powerful.
6. Preventing hallucinations requires explicit factual grounding rules ("answer only if very confident," cite sources in output).
7. Output formatting (XML tags, JSON pre-fill) lets you parse and integrate results into production databases without separate extraction.
8. Step-by-step task ordering mirrors human reasoning and improves accuracy for complex multimodal analysis.
9. Pre-filled responses (opening with `<output_format>` tag) steer Claude's serialization without relying on post-hoc parsing.
10. Extended thinking transcripts surface implicit reasoning steps; analyzing them reveals missing prompt structure to encode.

## Patterns & Frameworks

- **Prompt structure template**: Task/role → Content (images/data) → Detailed instructions (step order) → Examples (few-shot) → Reinforcement (guidelines + output format)
- **Confidence thresholds**: Embed "answer only if very confident" in system prompt to prevent false claims; require citations for factual assertions
- **Content ordering heuristic**: Process simpler/known data first (form checkboxes) before ambiguous data (sketch), matching human intuition
- **Semantic tagging**: Use XML (`<form_analysis>`, `<sketch_analysis>`) to let Claude organize and re-reference sections
- **Prompt caching candidate**: Reusable static context (form structure, field definitions) maps to cache breakpoint, reducing 90% of repeated token costs
- **Few-shot encoding**: Encode difficult real-world examples with human-validated verdicts; use base64 images + expected reasoning format
- **Pre-filling pattern**: Begin output with format marker (e.g., `<final_verdict>`) to enforce JSON/XML structure without parsing logic
- **Extended thinking debugging**: Enable thinking tags, analyze transcripts to find reasoning gaps, encode missing steps back into system prompt

## Numbers & Specifics

- Swedish car accident insurance scenario; 17 checkboxes in claim form
- Two-column vehicle layout (Vehicle A, Vehicle B) on accident report
- 10-point prompt structure framework (slides reference)
- Four iterative versions (v1 → v4) shown in live console demos
- Temperature 0 (deterministic) with large max_tokens budget (no artificial capping)
- Claude 3.7 and Claude 4 both support extended thinking
- Form specs = static content → system prompt candidate for reuse across 1000s of queries

## Quotes

> "Prompt engineering is the practice of writing clear instructions for the model, giving the model the context that it needs to complete the task, and thinking through how we want to arrange that information to get the best result."

> "Prompt engineering is a very iterative empirical science... you iteratively build upon your prompt to make sure it's actually tackling the problem you're intending to solve."

> "Claude really loves structure, loves organization. That's why we recommend following kind of a standard structure in your prompts."

> "The order in which Claude analyzes this information is very important... If we have the form and can read the form first and understand that we're talking about a car accident... then we know a little bit more about how to understand what might be in the drawing."

> "Extended thinking is something we want to highlight because you can use extended thinking as a crutch for your prompt engineering... it's not only more token efficient but it's a good way of understanding how these intelligent models go about the data that we provide them."

## Applied AI Relevance

- **Prompt caching ROI**: Static context (domain specs, form definitions) should move to system prompts as primary caching target—10% of base cost on cache hits saves ~$40–$400/million tokens depending on volume.
- **Factual grounding is programmatic**: Halluciniation prevention requires explicit output constraints + citation rules, not suggestion-based guidance; use XML tags to force structured reasoning.
- **Few-shot is bottleneck relief**: Encode real edge cases (tricky accident drawings, ambiguous form markings) with human-validated solutions; collect failure cases from production to update prompts.
- **Extended thinking transparency**: Analyze thinking transcripts to surface implicit reasoning steps Claude is taking; encode those steps back into prompt structure (step ordering, confidence gates) to make reasoning reproducible and debuggable.

---
**Word count**: 578 | **Themes**: context-engineering, model-fundamentals, enforcement-reliability
