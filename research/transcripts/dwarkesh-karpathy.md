---
title: "Andrej Karpathy — AGI is still a decade away"
speaker: Andrej Karpathy (interviewed by Dwarkesh Patel)
source_url: https://www.dwarkesh.com/p/andrej-karpathy
retrieved: 2026-07-16
method: webfetch
publish_date: 2025-10-17
content_type: summary (see note)
---

> **Note on this file:** This episode's full transcript is copyrighted content
> published by the Dwarkesh Podcast. Per copyright policy, this file is a
> detailed original-language summary organized by topic, not a verbatim
> reproduction of the transcript. For the exact wording, read the source at
> the URL above. The original runs roughly 2 hours / tens of thousands of
> words across nine sections.

## Episode structure (per the source page)
1. AGI is still a decade away
2. LLM cognitive deficits
3. RL is terrible
4. How do humans learn?
5. AGI will blend into 2% GDP growth
6. ASI
7. Evolution of intelligence & culture
8. Why self-driving took so long
9. Future of education

## Summary

### Timeline
Karpathy pegs roughly a decade before AI agents become genuinely reliable
workplace participants — he distinguishes the hype of a "year of agents"
from the more realistic "decade of agents." His estimate is drawn from 15
years of watching the field's predictions play out, not a fixed formula.

### Three eras of deep learning
1. **Task-specific nets** (post-AlexNet, ~2012): one model, one task.
2. **Premature agents** (2013–2015): RL on Atari and the OpenAI "Universe"
   project to control keyboard/mouse — which Karpathy now views as having
   jumped the gun, since models lacked good representations and reward
   signals were too sparse.
3. **LLMs / representation learning**: pretraining on internet text builds
   representations first, and today's agents sit on top of that
   foundation.

### Pretraining as "a crappy form of evolution"
Evolution compresses learning algorithms into a small genome so organisms
can learn efficiently in their lifetime; pretraining analogously compresses
internet text into network weights so the model can do useful things
downstream. He argues pretraining conflates two things it shouldn't:
memorized facts and general algorithmic/reasoning ability — and that this
conflation actively hurts generalization.

### In-context learning as working memory
Karpathy treats in-context learning as the model's most impressive
capability — something like gradient descent implemented via attention.
Anything baked into the weights is "hazy recollection" (a huge corpus
compressed into a comparatively tiny parameter count); anything in the
context window is directly accessible, which is why giving a model the
actual text beats relying on what it "remembers."

### Where LLMs are cognitively missing pieces
No hippocampus-equivalent (no persistent episodic memory across sessions),
no sleep-like consolidation/distillation step, limited sparse-attention
mechanisms (he flags DeepSeek v3.2 as a hint of convergent evolution
toward this), no amygdala-like affective machinery, and a tendency to
collapse to stereotyped outputs (e.g., ask for a joke and you get one of
about three canned answers).

### Model collapse
Training on model-generated data causes diversity to mysteriously collapse
even when individual outputs look fine — a major constraint on synthetic
data strategies. Humans avoid full collapse via novel experience and
social contact; Karpathy speculates dreaming may serve an
entropy-injection function that keeps human cognition from over-fitting.

### RL critique — "reinforcement learning is terrible"
The core complaint is credit assignment: out of many rollouts on a hard
problem, maybe one succeeds, and RL upweights *every* token in that one
successful trajectory uniformly — including wrong turns that happened to
precede the right answer. He calls this "sucking supervision through a
straw": a whole trajectory's worth of signal gets compressed into one
scalar reward, then broadcast back across every token. He'd prefer
process-level supervision but notes it's practically broken because LLM
judges are trivially gameable — models find adversarial, meaningless token
sequences that fool the judge into a perfect score, and this keeps
recurring because the space of adversarial examples is effectively
infinite.

### How humans actually learn
Karpathy argues humans mostly don't use RL for cognitive (as opposed to
motor) skills. Reading a book isn't ingesting knowledge directly — it
prompts internal synthetic-data generation and reconciliation with what
you already believe, which current LLMs don't do; they just predict next
tokens over the stretched-out text.

### Cognitive core vs. memory
He proposes deliberately separating a small "cognitive core" (reasoning
strategies, algorithms) from bulk factual memory, which would live in an
external lookup system instead of the weights. A much smaller model
(he floats "billion-parameter" scale) stripped of memorized trivia, paired
with retrieval, might match today's far larger models on reasoning tasks.
Dwarkesh pushes back that empirical scaling-down trends (two orders of
magnitude in two years) suggest cores could get even smaller; Karpathy
agrees in spirit but insists some baseline knowledge is required — "you
can't think if you're looking things up constantly."

### Why coding is the natural first application
Text-native, huge training corpus, and existing tooling (diffs, version
control, IDEs) make code a great fit for current models, unlike something
spatial like slides. Building his "nanochat" project, Karpathy found
coding models imposed unwanted conventions, over-engineered defensively,
suggested deprecated APIs, and added boilerplate — autocomplete was more
useful to him than full agentic "vibe coding," except when working in an
unfamiliar paradigm (e.g., a Rust tokenizer), where agents helped more.
The upshot: don't expect these models to autonomously drive novel research
architecture — a prerequisite some people assume for a fast intelligence
explosion.

### Where agents stand today
Impressive and useful daily, but nowhere near replacement-level: no
cross-session state/continual learning, insufficient multimodality, and
unreliable computer use. He expects an "autonomy slider" — AI doing an
increasing share of volume while humans supervise small teams of agents —
rather than a sudden flip, citing radiology (not displaced despite great
vision models, because the job is messier than pure image classification)
versus call centers (much more automatable: repetitive, digital, bounded).

### AGI and GDP
He keeps the classic definition — any economically valuable task at human
level or better — and argues even restricting to knowledge work implies
trillions of dollars of value. But he expects this to show up as
continuation of the ~2% annual growth trend seen for roughly 250 years,
not a visible discontinuity — pointing out you can't find the iPhone's
2008 launch in aggregate GDP data either, because real technology
diffusion is slow and staggered even when the tech itself is
transformative.

### Superintelligence and control
Karpathy expects ASI to look like continued automation rather than a
sudden qualitative break, but describes the resulting world as "foreign" —
many fast-thinking entities running on compute. His main worry isn't one
runaway superintelligence but a gradual, diffuse loss of human
understanding/control as many autonomous agents, delegated to on behalf of
different people and companies, interact and compete — some going rogue,
others policing them — producing system-level outcomes nobody
specifically intended or can fully steer, even if individual humans retain
nominal authority over their own agent.

### Education
The transcript's ninth section (future of education) is referenced by the
episode's own outline but the fetched excerpt cuts off before it's
substantively covered; consult the source URL for that portion.
