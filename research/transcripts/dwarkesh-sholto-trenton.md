---
title: "Sholto Douglas & Trenton Bricken — How to Build & Understand GPT-7's Mind"
speaker: Sholto Douglas (Google DeepMind) & Trenton Bricken (Anthropic), interviewed by Dwarkesh Patel
source_url: https://www.dwarkesh.com/p/sholto-douglas-trenton-bricken
retrieved: 2026-07-16
method: webfetch
publish_date: uncertain — sources disagree (dates seen: 2024-03-28 and 2025-08-28); the requested target was "March 2025"; this is the only/original Douglas+Bricken episode found (the follow-up "How Does Claude 4 Think?" at /p/sholto-trenton-2 is a separate, later episode not covered here)
content_type: summary (see note)
---

> **Note on this file:** This episode's full transcript is copyrighted
> content published by the Dwarkesh Podcast. Per copyright policy, this
> file is a detailed original-language summary organized by topic, not a
> verbatim reproduction of the transcript. For exact wording, read the
> source at the URL above. The original runs roughly 3h12m across ten
> sections.
>
> **Publish-date caveat:** search results returned conflicting dates for
> this URL (March 2024 vs. August 2025); neither matches the "March 2025"
> requested in the task. This appears to be the correct episode by guest
> names and title ("GPT-7's Mind"), but the exact date could not be
> confirmed — verify directly at the source URL before citing a date.

## Episode structure (per the source page)
1. Long contexts
2. Intelligence is just associations
3. Intelligence explosion & great researchers
4. Superposition & secret communication
5. Agents & true reasoning
6. How Sholto & Trenton got into AI research
7. Are feature spaces the wrong way to think about intelligence?
8. Will interp actually work on superhuman models
9. Sholto's technical challenge for the audience
10. Rapid fire

## Summary

### Long contexts
Sholto argues million-token context windows are underrated: loading an
entire codebase solves the "onboarding problem" instantly, and perplexity
improves with longer context in ways comparable to scaling up model size,
without the architecture growing. As evidence models "already know things
you don't," he cites models learning an obscure human language from
in-context examples alone (not in training data). Mechanistically,
in-context learning is likened to gradient descent implemented through
attention — n transformer layers act like n steps of an optimization
process — and the residual stream functions like RAM, read from and
written to as needed, giving models an effective working memory beyond
human limits. Trenton flags a safety wrinkle: if a forward pass is doing
something like on-the-fly fine-tuning via in-context learning, an
adversarial prompt effectively creates a new, untested model each time,
regardless of prior safety training.

They push back on the assumption that long-horizon agent failures are a
context problem — the actual bottleneck is reliability ("nines of
reliability"): chaining steps multiplies failure probability, and GPT-4-
class models simply aren't reliable enough yet for robust agents; later
generations need to close that gap. They also cite Rylan Schaeffer's
NeurIPS work arguing many "emergent abilities" are a measurement artifact:
a task needing several correct predictions in a row looks like a sudden
jump once per-step reliability crosses a threshold, even though the
underlying capability was gradually improving. On cost, they note
quadratic attention cost is often dominated by MLP costs in practice, and
inference-time attention (one query against a KV cache) is linear, not
quadratic — part of why long context remains tractable.

### Intelligence as associations
Trenton's central claim: most intelligence is pattern matching via
hierarchical associative memory — chains of association (A→B→C) rather
than discrete symbolic reasoning steps. Associative memory does double
duty as denoising (cleaning up corrupted/partial memories) and retrieval.
The residual stream is described via a "passengers on a boat" image: early
layers extract basic token relationships, middle layers do deeper
recombination, and late layers convert the compressed representation back
into output tokens. Complex deduction (their Sherlock Holmes example) is
framed as extended association and iterative attention/refinement over
context rather than symbolic logic — closer to how humans re-read
evidence and revise hypotheses than to formal inference.

Because the model has far fewer parameters/dimensions than the number of
sparse features present in internet-scale data, it's forced into
"superposition" — packing multiple features into single dimensions, which
is why individual neurons often appear to respond to unrelated concepts.
Larger models can afford less compression (cleaner, more separated
features), which the two connect to why bigger models tend to be more
sample-efficient on the same data.

### Intelligence explosion & great researchers
They describe the field as still meaningfully compute-bound — more
compute means more experiments, and experimental throughput is the
limiting resource, similar to bench science. They're skeptical that better
models alone quickly automate frontier research: interpretability work in
particular needs whole-model context, careful correctness (e.g., properly
accounting for layer-norm effects when attributing behavior to features),
and reasoning current models can't yet reliably do. Scaling trends
themselves are described as imperfect and sometimes non-transferable —
tweaks that help at small scale can hurt at large scale — so researchers
are extrapolating under real uncertainty, and most experiments (the
"graveyard" behind every published result) simply fail.

They locate the real bottleneck in taste/judgment (which of many ideas is
worth testing) and interpretation of ambiguous early results, not in
writing code or generating ideas. Great researchers, in their telling,
iterate very fast at small scale, aren't wedded to one theoretical
framework (RL, optimization, systems), and attack problems directly. They
separate two distinct "intelligence explosion" mechanisms: (1) AI speeding
up engineering/iteration for human researchers (which they find plausible)
versus (2) AI itself becoming the primary source of research ideas via
synthetic data (which they consider much less certain). Sholic estimates
roughly 0.5 elasticity of research progress to compute (10x compute ≈ 5x
faster progress on a program like Gemini), while noting the split between
production and research compute is a strategic choice, not fixed.

They also discuss cost scaling across model generations — rough estimates
of GPT-4-class training around $100M, next generation in the $1-10B range,
the generation after that in the tens of billions (requiring
consortium-level backing), and a further jump toward $1T+ (referencing
Altman's stated funding ambitions) — framing this as a "narrow window"
argument: if superhuman reasoning hasn't emerged by the time costs hit
that ceiling, further brute-force scaling becomes economically
implausible, potentially leaving models at a very capable but
sub-recursive-self-improvement plateau. They're careful to note this still
implies extremely capable, very reliable systems even short of full AGI.

### Superposition & secret communication
Transformers operate in an underparameterized regime relative to the
sparse, high-dimensional feature space of real data, forcing the
superposition described above. Dictionary-learning / sparse-autoencoder
techniques (referencing Anthropic's "Towards Monosemanticity" work) can
project activations into a higher-dimensional, sparser basis that recovers
more interpretable, roughly one-concept-per-dimension features. They frame
knowledge distillation as transferring a fuller probability distribution
("showing work") rather than one-hot answers, which is part of why
distilled small models learn faster than models trained from scratch on
the same hard labels. They speculate — explicitly flagging this as
unverified "headcanon" — that models could in principle encode
information about likely future tokens into the KV cache in ways not
visible to a human reader (a steganography-adjacent concern). More
concretely and better supported, they cite multiple results showing
chain-of-thought reasoning can be unfaithful: it can be deleted or garbled
without changing the final answer, or a model can produce a plausible-
looking rationale while its actual decision was made on different
grounds — compared to confabulation in split-brain patients.

### Agents & true reasoning
Near-term, they expect agent systems built from multiple (possibly
smaller) model instances communicating in natural language, which
preserves human oversight and interpretability versus one opaque
end-to-end system. As context length and adaptive compute improve, they
expect the sharp distinctions between model "sizes/tiers" to blur, with
single models specializing dynamically via context rather than needing
separate fine-tuned variants. They note that end-to-end training on
sparse, delayed rewards (e.g., "did the company make money?") doesn't work
well yet because current reliability is too low to generate any reward
signal often enough to learn from — something they expect to improve as
baseline reliability rises across generations.

They discuss richer inter-agent communication than text — sharing
residual-stream-like dense representations would be far more efficient
than natural language for complex information, analogous to sharing image
embeddings instead of describing an image in words — but flag
interpretability and safety reasons this might be resisted early on;
sharing dictionary-learned (human-interpretable) features is floated as a
middle ground. On multimodality, they reference DeepMind's Demis Hassabis
noting positive transfer between modalities (e.g., video-derived physics
intuition potentially helping coding), while cautioning the size of this
effect is still unclear. They also offer a more speculative claim that
human language itself may have evolved partly to be learnable by children,
i.e., optimized over millennia for transmissibility — which could partly
explain why LLMs trained on language do so well, independent of any
particular architectural choice.

### Background, technical notes, and open questions
Sholto (by their account, relatively new to the field at the time) is
credited by Noam Brown as one of the most important contributors to
Gemini's success, focused on inference optimization and pretraining
guidance. Trenton's neuroscience background feeds into his interpretability
work at Anthropic, including a paper connecting the attention mechanism to
Pentti Kanerva's classical associative-memory algorithm and to cerebellar
circuitry — noting the cerebellum (about 70% of the brain's neurons)
activates during next-token-prediction-like tasks and that cerebellar
damage correlates with autism-spectrum difficulties.

They close by flagging open problems: whether interpretability techniques
will scale to superhuman models is unknown; good evaluations are hard to
construct because internet-scale cultural knowledge contaminates
supposedly-novel test data, and using other LLMs as judges creates its
own reward-hacking incentives; and chain-of-thought's demonstrated
unfaithfulness means current "reasoning traces" shouldn't be trusted at
face value as an explanation of model behavior.
