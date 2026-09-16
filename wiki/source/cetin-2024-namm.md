---
type: source
name: "Cetin et al. 2024 — An Evolved Universal Transformer Memory (Sakana AI NAMM)"
status: timeless
last_ingested: 2026-05-16
sources: []
tags: [sakana-ai, namm, kv-cache-pruning, evolutionary-search, sidecar-shape, working-memory-policy, not-a-caddy]
---

## Citation

Cetin, E. et al. (2024). *An Evolved Universal Transformer Memory.* arXiv:2410.13166. Sakana AI. Published December 10 2024.

## Location

- arXiv: https://arxiv.org/abs/2410.13166
- Code: https://github.com/SakanaAI/evo-memory
- Sakana blog: https://sakana.ai/namm/
- Local archive: [`cetin-2024-namm.pdf`](../../../research/library/papers/cetin-2024-namm.pdf) (35 pages)

## Key claims (with our restatements)

### Architecture — learned KV-cache retention policy

**Paper:** Neural Attention Memory Models (NAMM) are neural network classifiers that take attention matrices (converted to spectrograms via short-time Fourier transform, then exponential-moving-average compressed) and output binary remember/forget decisions per token in the LLM's attention KV cache. Trained via evolutionary search (no gradients) to maximise downstream LM performance under cache-size budget.

**Our restatement:** `[ASSERTED]` NAMM is a **trained policy that operates on the LLM's own working memory** (attention KV cache), not a separate memory module beside the LLM. The "sidecar" shape Sakana emphasises refers to the classifier being separately trainable and transferable across base models — not to the classifier holding any persistent memory state itself.

### Universal — transfers across pretrained transformers

**Paper:** A single NAMM trained on one base transformer can be applied across all the model's layers and transferred to other transformers (vision, RL, language) without retraining. Demonstrated across Llama, Vision Transformer, and RL transformer baselines.

**Our restatement:** `[ASSERTED]` This is the most important commercial-shape finding: **a separately-trained policy that operates on a frozen LLM's working memory generalises across base models.** Partial proof-of-concept for the frozen-consumer property a [caddy](../concept/caddy.md) would want. **Important: this is the working-memory level (KV cache pruning), not the long-term-memory level.** A caddy operates at a different timescale and on different data structures.

### Benchmark and baselines

**Paper:** Evaluates on LongBench, InfiniteBench, ChouBun (36 tasks combined). Baselines are H₂O and L₂ (other KV-cache compression methods). Claims "superior results across language and coding tasks while requiring less memory."

**Our restatement:** `[ASSERTED]` paper-reported. **Construct-validity:** these benchmarks measure within-context efficiency under cache pressure. They do NOT measure cross-session memory persistence, selective consolidation, schema-based recall, or any other Norman-rubric property. NAMM's benchmark suite confirms it solves a different problem than caddy memory addresses.

### Bio-cognitive framing

**Paper:** References "human memory selectively retains and prunes" as motivation. No neurobiological citations (no hippocampus, CLS, schema, etc.) — purely motivational analogy.

**Our restatement:** `[ASSERTED]` Cog-sci grounding is decoration only. NAMM is engineering-first work that uses biology as marketing flavour. Scores 0 on CG1 (explicit cog-sci grounding) of our prior survey rubric.

## Important caveats

- **NAMM is NOT a memory module.** It is a *policy* that decides what to drop from the LLM's attention cache. The "memory" it manages is the LLM's own working memory, not a separate store.
- **Within-context only, no cross-session persistence.** The classifier is stateless; KV-cache decisions don't carry across context-window resets.
- **Evolutionary training is non-trivial to scale.** No gradients means hyperparameter-heavy and compute-intensive. Productisation has not happened — the paper has been public for 17 months as of 2026-05-16 with no Sakana product launch.
- **Norman-rubric score: ~1/5.** Partial credit on selective encoding (the classifier *does* selectively retain tokens) but at the wrong timescale and wrong data type. Fails event segmentation, temporal contiguity, competition at retrieval, dynamic updating in any meaningful sense.
- **Sakana's broader memory research line.** NAMM is one of several Sakana memory-adjacent papers; CTM (Continuous Thought Machine, separate paper at pub.sakana.ai/ctm) has more cog-sci grounding (STDP, oscillations) but is vision-focused and not a memory module either. Sakana ships research, not memory products as of 2026-05-16.

## Relevance to Kyrja

- **Enabling evidence, not competitive threat.** NAMM proves a *trained policy that operates on a frozen LLM's working memory and transfers across base models* is feasible and ships. That's a partial proof-of-concept for the frozen-consumer property a caddy would want — but at the working-memory level, not the long-term-memory level. Useful citation for the VC pitch.
- **Sakana the company has the team and funding to build a caddy if they decide to.** $135M Series B at $2.65B valuation (November 2025). David Ha + Llion Jones founders. They have the biology curiosity, the evolutionary-methods expertise, and the partial proof-of-concept. **17 months of NAMM existence without a caddy-shaped product launch is itself a signal** that they have not prioritised that direction — but Sakana stays on the watch list.
- **Architectural contrast:** NAMM is *sidecar in the engineering sense* (separately-trained, transferable) but **not sidecar in the memory-architecture sense** (no persistent state, operates on the consumer's own working memory). The two senses of "sidecar" matter — Kyrja means the latter; Sakana demonstrates the former. Worth distinguishing carefully in pitch language.

## Audit history

- 2026-05-16 — WebFetch of sakana.ai/namm + Semantic Scholar abstract + arXiv abstract. Local PDF downloaded but not verbatim-read at the methods-section level. Architecture summary above is from blog + abstract, not from §3 methods detail. Verbatim re-read queued if NAMM becomes load-bearing in any future claim.

## Archive location

arXiv:2410.13166. Local PDF: [`cetin-2024-namm.pdf`](../../../research/library/papers/cetin-2024-namm.pdf) (35 pages). Code: https://github.com/SakanaAI/evo-memory. Blog: https://sakana.ai/namm/.
