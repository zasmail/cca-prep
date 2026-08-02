---
title: "Andrej Karpathy — AGI is still a decade away"
speaker: Andrej Karpathy (interviewed by Dwarkesh Patel)
source: https://www.dwarkesh.com/p/andrej-karpathy
themes: [karpathy-mental-models, model-fundamentals, memory, evals, tool-design-mcp, orchestration, context-engineering]
---

## Core claims

1. AGI arrives in roughly a decade, not "year of agents" hype — a realistic timeline drawn from 15 years of field observation, not formula-driven prediction.
2. LLMs suffer five major cognitive gaps: no persistent episodic memory, no sleep-like consolidation, limited sparse attention, no amygdala-like affect machinery, and collapse to stereotyped outputs.
3. Pretraining conflates memorized facts with algorithmic reasoning in weights, actively hurting generalization across both.
4. In-context learning (gradient descent via attention) is the model's single most impressive capability — direct access beats relying on compressed weights.
5. Reinforcement learning as practiced is fundamentally broken: credit assignment broadcasts one scalar reward uniformly across entire trajectories, including wrong turns.
6. Humans learn cognitive skills via internal synthetic-data generation while reading, not by RL; LLMs just predict stretched-out text tokens.
7. A small "cognitive core" (billion-parameter scale) stripped of trivia and paired with external retrieval could match far larger models on reasoning.
8. Model collapse from synthetic data is real and unsolved: diversity mysteriously collapses even when individual outputs appear fine.
9. Coding is the natural first agentic application: text-native, huge corpus, existing tooling (diffs, version control, IDEs).
10. Agents today are impressive but not replacement-level; expect gradual "autonomy slider" rather than sudden flip to autonomy.
11. AGI will appear as continuation of ~2% annual growth for 250 years, not a visible discontinuity — real tech diffusion is slow.
12. ASI risks aren't one runaway superintendent but gradual loss of control as many autonomous agents interact and compete unpredictably.

## Patterns & frameworks

- **Three eras**: (1) task-specific nets (post-AlexNet, 2012), (2) premature agents (2013–2015), (3) LLMs / representation learning.
- **Pretraining as crappy evolution**: compresses internet text into weights so the model can learn efficiently, parallel to how genomes compress learning algorithms.
- **In-context learning as working memory**: direct access to context beats hazy recollection from weights; anything in the window is "directly accessible."
- **Credit assignment failure**: many rollouts, maybe one succeeds, RL upweights every token uniformly — "sucking supervision through a straw."
- **Process-level supervision gameable**: LLM judges easily fooled by adversarial token sequences; space of adversarial examples is effectively infinite.
- **Autonomy slider**: AI doing increasing share of volume while humans supervise small agent teams, not sudden replacement.
- **Cognitive core separation**: split reasoning strategies (small model) from factual memory (external lookup), avoiding constant retrieval overhead.

## Numbers & specifics

- **Decade** = rough timeline to reliable workplace agents (based on 15 years of field observation).
- **2012** = AlexNet, start of task-specific nets era.
- **2013–2015** = premature agents (Atari RL, OpenAI Universe keyboard/mouse control).
- **~2% annual GDP growth** = 250-year trend that will likely continue even with AGI.
- **Billion-parameter scale** = floated size for cognitive core without trivia.
- **Two orders of magnitude reduction** = model scaling drop in two years (per Dwarkesh pushback).
- **Roughly 2 hours / tens of thousands of words** = episode length.

## Quotes

1. "Decade of agents, not year of agents" — the realistic horizon vs. hype.
2. "Pretraining is a crappy form of evolution" — conflates two things it shouldn't.
3. "Hazy recollection" — what weights hold vs. direct context access.
4. "Sucking supervision through a straw" — RL's credit assignment problem in one phrase.
5. "You can't think if you're looking things up constantly" — the baseline knowledge constraint on cognitive cores.

## Applied AI relevance

- **Cognitive gaps → tool and MCP design**: Persistent memory, consolidation, sparse attention, and affect machinery are absent; external tooling must compensate (retrieval, logging, feedback loops).
- **In-context learning is the lever**: Maximizing direct context access over weight-based inference reshapes context-engineering and prompt caching strategies.
- **Credit assignment shapes evals**: Process-level supervision is gameable; must design evaluation systems that reward intermediate reasoning steps, not just outcomes.
- **Retrieval-augmented reasoning over pure scale**: Smaller cognitive cores + external memory aligns with tool-use and orchestration strategies better than scaling model size alone.
