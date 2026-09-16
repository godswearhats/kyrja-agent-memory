---
type: source
name: "Howard & Kahana 2002 — A Distributed Representation of Temporal Context"
status: timeless
last_ingested: 2026-05-14
sources: []
tags: [cog-sci, temporal-context, episodic-memory, retrieval-cue, asymmetric-recall, distributed-memory-model, modern-cog-sci, load-bearing]
---

## Citation

Howard, M. W., & Kahana, M. J. (2002). *A distributed representation of temporal context.* Journal of Mathematical Psychology, 46, 269–299. DOI: 10.1006/jmps.2001.1388. Received 12 July 1999; revised 14 March 2001.

## Location

- PDF: [library/papers/howard-kahana-2002-tcm.pdf](../../../research/library/papers/howard-kahana-2002-tcm.pdf)
- DOI: 10.1006/jmps.2001.1388
- Raw data archive (per the paper, p.18 footnote 8): http://fechner.ccs.brandeis.edu/Experiments/archive.html

## Why this paper is load-bearing for Kyrja

TCM names a memory primitive that no current LLM-agent memory system implements: **a slowly-drifting context vector, distinct from item content, that is updated by what gets retrieved**. The retrieval cue is content-driven *but not* identical to content — it accumulates trajectory information that lets two memories studied near each other in time be cued by each other even when their content is unrelated. This is the architectural difference between "retrieve by similarity to query" and "retrieve by similarity to where I am in time/task." TCM is the cleanest 2002-vintage formalization of that primitive; it anchors mechanism-gap-matrix row M13 and is the cog-sci foundation for [H41](../hypothesis/H41-temporal-context-retrieval.md).

## Key claims (with our restatements)

### Thesis (abstract, verbatim, p.1)

> "Rather than being driven by random fluctuations, this formulation, the *temporal context model* (TCM), uses retrieval of prior contextual states to drive contextual drift. In TCM, retrieved context is an inherently asymmetric retrieval cue."

**Our restatement:** `[ASSERTED]` TCM's load-bearing departure from prior random-fluctuation context models (Estes 1955; Mensink & Raaijmakers 1989; Murdock 1997) is that **context drift is content-driven, not noise-driven**. Items retrieve context; retrieved context updates the context state; the updated context becomes the cue for the next retrieval. The architecture closes a feedback loop at the *context* level.

### The five-component model (§5.4 Conclusions, p.21)

`[ASSERTED]` TCM consists of:

1. **F-space** — semantic memory; item representations `f_i` (assumed orthonormal in this paper).
2. **T-space** — context states `t_i`.
3. **M^TF matrix** (context-to-item, eq 1, p.6) — `M^TF = Σ f_i t_i'`, simple Hebbian outer products. Connects context cue to item activations.
4. **M^FT matrix** (item-to-context, eq 12, p.14) — uses item-specific unlearning (projection-operator decay parallel to f_i) to keep the retrieved context vector bounded when an item is repeated.
5. **Evolution equation** (eq 6, p.10) — `t_i = ρ_i t_{i-1} + β t_i^IN`, where `t_i^IN = M^FT f_i` (eq 5, p.9) and `ρ_i` is set quadratically (eq 7) to keep ||t||=1.

### Asymmetric retrieval falls out of the preexperimental/newly-learned split (§3.1, eq 8, Fig 6, p.12)

`[ASSERTED]` When an item recurs, the retrieved context input is decomposed into two components:

```
t_r^IN = A_i · t_i^IN + B_i · t_i
```

- `t_i^IN` is the **preexperimental context** — the context state from the item's prior history. It only resembles contextual states that *followed* item i (forward asymmetry).
- `t_i` is the **newly-learned context** — the context state when item i was just encoded in this list. It is similar to states both *before* and *after* item i (symmetric).

Their mixture produces forward-asymmetric retrieval *without a dedicated asymmetry parameter*. Fig 6 (p.12) plots the two components vs lag: newly-learned context is symmetric around 0; preexperimental context is non-zero only for forward lags. This is the load-bearing figure for the asymmetry mechanism.

**Our restatement:** `[ASSERTED]` The two-tier split maps naturally onto LLM-agent memory: **preexperimental ≈ user-lifetime semantic context for an item; newly-learned ≈ session-local episodic context for the item**. Translation candidate, not in the paper.

### Retrieval is softmax-over-activations (eq 14, p.16)

`[MEASURED]` Recall probability:

```
P(f_i | f^IN) = exp(2 a_i / τ) / Σ_j exp(2 a_j / τ)
```

where `a_i = f^IN · f_i` is the activation of item `f_i` under context cue, and τ is a temperature parameter.

**Construct-validity check:** This is mathematically identical to modern transformer attention `softmax(QK'/√d)V`. TCM's eq 14 is `softmax(2(f^IN · f_i)/τ)`. Same primitive, separated by ~15 years.

**Our restatement:** `[ASSERTED]` The architectural through-line from TCM to transformer attention is real. The novel content of TCM relative to attention is *not* the retrieval rule — it is the **evolution equation for the cue** (eq 6) and the **item-specific unlearning rule for the cue-generating matrix** (eq 12). Both are absent from vanilla attention.

### Empirical fits — mixed quantitative quality (§4, Fig 7-8, pp.17-20)

`[MEASURED]` TCM was fit to free-recall data from Howard & Kahana (1999), Experiment 1 (immediate) and Experiment 2 (delayed and continuous-distractor conditions, 12-item lists, 1-1.2s/item, 16s arithmetic distractor).

**Best-fit parameters:** β = 0.402, τ = 0.247, d (effective distractor length) = 7.24. γ was fixed at 1.

**End-of-list recency fit (Fig 7):**

| Condition | χ²(8) | Most-deviant point |
|---|---|---|
| Immediate | 26.9 | First serial position contributed 8.4 of 26.9 |
| Delayed | 57.7 | First serial position contributed 18.3 |
| Continuous-distractor | 37.3 | n.s. |

**Lag-recency CRP fit (Fig 8):**

| Condition + direction | χ²(5) |
|---|---|
| Delayed, forward | **103** (very poor) |
| Continuous-distractor, forward | 5.46 (very good) |

**Construct-validity check:** The χ² values measure deviation from the data points on the fitted curves. The 5% critical value for χ²(8) is ~15.5 and for χ²(5) is ~11.1. Most TCM fits **exceed** these thresholds, meaning a strict goodness-of-fit test *rejects* the model on its own data. The authors are explicit (p.20): *"Although the fits were not numerically spectacular, they were acceptable given the simplicity of the model."*

**Our restatement:** `[ASSERTED]` TCM captures the *qualitative* pattern (recency + contiguity + asymmetry across time scales) with parameter parsimony; it does **not** quantitatively fit the data well. Cite TCM as a *principled* architectural account, not a high-fidelity model. Misciting it as "TCM works" would overclaim.

### What TCM is NOT (§5.3, pp.25-27)

`[ASSERTED]` The authors explicitly disclaim TCM as a full free-recall model. TCM does not include:

- **Primacy** (no mechanism — the most-deviant points in all three condition fits are first serial position).
- **Output-position effects on the CRP** in immediate recall (the CRP shape changes with output position in immediate but not delayed/continuous-distractor).
- **Repetition avoidance** during recall.
- **Semantic similarity** between items.

TCM is "a model that prescribes a set of rules for how a distributed episodic representation should change from moment to moment" (p.25, verbatim). It is the contextual-drift-and-retrieval mechanism, not a complete memory system.

### Distinction from clock/positional models (§5.2.2, pp.23-25)

`[ASSERTED]` The critical empirical signature distinguishing TCM from clock-context models is **context effects driven by item-level perturbations**. Specifically:

- Falkenberg (1972) — repeating a specific distractor task between study and test *improves* memory for items presented before that distractor.
- TCM predicts this because items drive context drift, so repeating a distractor reinstates an earlier context state.
- Clock-context models (which assume context drift is independent of items presented) cannot.

**Our restatement:** `[ASSERTED]` The Falkenberg signature is the falsifiability anchor for [H41](../hypothesis/H41-temporal-context-retrieval.md) in an agent-memory setting: if reintroducing a specific task between sessions does NOT improve retrieval of items studied before that task, the TCM-style content-driven context mechanism doesn't apply.

## Important caveats

- **Orthonormality assumption.** The mathematical derivations throughout assume `f_i` are orthonormal in F. This is `[CONTESTED]` for LLM embeddings, which are anisotropic and cluster around a common mean — see [reference_embedding_anisotropy] in project memory. The math may need re-derivation under non-orthonormal item representations before any LLM-agent implementation.
- **M^TF reset at list onset.** Per §5.1 (p.21, component 3), M^TF is "reset at the beginning of each list" in this paper's applications. The episodic vs semantic boundary is defined by this reset. For an LLM-agent operating across sessions, the equivalent reset rule is not specified by TCM and must be designed.
- **Single domain — verbal free recall.** TCM is fit to free recall of randomly assembled word lists (Toronto Noun Pool, 12 items, fast presentation). Generalization to non-list memory (autobiographical, task-state, code) is unverified. `[SPECULATED]` extrapolation.
- **Two free parameters (β, τ) plus γ and d.** Parameter parsimony is one of TCM's stated virtues, but four parameters total when including γ (fixed at 1 here) and d (effective distractor length). All four interact with fit quality.
- **The "preexperimental context" abstraction.** TCM treats every item's first appearance in the experiment as if it carries pre-experimental associative history. For an LLM-agent system, the equivalent of "preexperimental context" must be operationalized — pretrained-knowledge associations? Prior-session context state? Unspecified.
- **No mechanism for asymmetric encoding of *new* items.** TCM's asymmetry depends on item repetition; the first encoding of a novel item has no preexperimental context contribution. For an LLM-agent system this matters because most memories are novel within their session.
- **Fits are weak.** The numerical χ² values exceed standard goodness-of-fit thresholds. The model captures qualitative structure, not quantitative behavior.

## Mechanism gap question — does any current agent-memory system implement TCM-style temporal context?

`[ASSERTED]` Answer: **No.**

| Mechanism component | AI analogue | Implementation status |
|---|---|---|
| Maintained context vector distinct from item content | KV cache / hidden state during a session | ⚠ Implicit, *within session only*, not persisted across sessions |
| Context drift driven by retrieved item content | — | ❌ No agent memory system updates a persistent context vector on retrieval |
| Asymmetric retrieval via preexp/newly-learned split | — | ❌ Forward-recall asymmetry is not modeled in any agent memory system |
| Item-specific unlearning to bound repeated-item context | — | ❌ |
| Softmax retrieval rule over context-cued activations | Transformer attention | ✅ Mathematically identical, but applied to query-content not to maintained context vector |
| Long-term reliable `t_i · t_j` similarity decay (cf STS) | Timestamp-based recency weighting | ⚠ Recency weighting is a scalar boost; not a vector-similarity signal |

The architectural gap: **a persistent, retrieval-updated context vector as a first-class retrieval primitive** is unimplemented. Mem0, Letta, Cognee, Zep, EvoSC, Cartridges, Hope — none of them maintain such a vector across sessions or update it on retrieval.

## What this confirms / refines in the existing wiki

### Confirms

- **[consolidation-channel](../concept/consolidation-channel.md):** the substrate-level paradigm needs distinct *retrieval cue* primitives beyond content similarity. TCM is one such primitive that no current system implements.
- **[active-stages-framework](../concept/active-stages-framework.md):** the framework needs to make space for *retrieval-stage* mechanisms, not just selection/curation/consolidation. TCM is a retrieval-stage primitive.
- **[cross-session-continuity](../open-question/cross-session-continuity.md):** TCM-style context similarity is a candidate addressing-mechanism for the cross-session-continuity gap.

### Refines

- The "no current agent memory uses time-as-vector" framing is now anchored to specific math (eq 6, eq 8, eq 12) and a falsifiability signature (Falkenberg 1972).
- The connection from cog-sci episodic-memory primitives to **transformer attention** via eq 14 is a real architectural through-line. Modern attention inherits TCM's retrieval rule but not TCM's cue-evolution rule.

### Does NOT contradict but worth flagging

- **The McClelland 1995 / engram framework treats memory as items + traces; TCM treats memory as items + a separate context space.** These are *complementary* primitives at different architectural levels. Both can coexist in a hybrid agent-memory architecture.
- **TCM's fits are weak.** The cog-sci community accepted TCM as a foundational framework despite the weak fits because of its parameter parsimony and architectural elegance. This is a different epistemic standard than ML benchmark-driven adoption. Worth keeping in mind when re-citing TCM in Kyrja papers.

## Relevance to Kyrja

- **Anchors M13** in [mechanism-gap-matrix](../concept/mechanism-gap-matrix.md): temporal context as a retrieval primitive.
- **Anchors H41** ([H41-temporal-context-retrieval](../hypothesis/H41-temporal-context-retrieval.md)): a drifting context vector updated by retrieval beats timestamp-only retrieval on cross-session continuity.
- **Concrete AI translation candidate.** The five-component model is implementable: outer-product matrices `O(|F|·|T|)` per update, softmax retrieval, projection-operator decay. Sub-millisecond per step at reasonable dimensions.
- **Mechanism for [cross-session-continuity](../open-question/cross-session-continuity.md).** "What was I doing last week on this project" maps to context-similarity retrieval; forward-recall asymmetry is *exactly what you want* in continuity work (recalling a past meeting preferentially surfaces what came after).
- **Compositional with [silent-engrams](../concept/silent-engrams.md) and [H40](../hypothesis/H40-schema-fit-modulated-consolidation.md).** TCM is read-side; silent-engrams is storage-side; schema-fit consolidation is write-side. All three primitives coexist in a hybrid architecture.

## Predicted follow-up reads

- **Sederberg, Howard, Kahana (2008) — A context-based theory of recency and contiguity in free recall.** Psychological Review 115:893-912. The TCM-A extension addresses semantic similarity in F-space, repetition effects, and primacy. **In library at `sederberg-howard-kahana-2008.pdf`; existing notes at `sederberg-howard-kahana-2008.md`.** Priority bump warranted if we commit to H41.
- **Polyn, Norman, Kahana (2009) — A context maintenance and retrieval model of organizational processes in free recall.** Psychological Review 116:129-156. CMR extends TCM with source context for organizational effects. Not in library; medium priority.
- **Burgess & Hitch (1992, 1999)** — competing positional/oscillator account; cited in §5.2.2. Not in library; low priority unless we need to defend TCM vs clock-context experimentally.
- **Foster & Wilson (2006)** — already named in [yang-et-al-2024-selection-of-experience](./yang-et-al-2024-selection-of-experience.md). Confirms forward-replay mechanism that TCM's content-driven drift maps onto.

## Audit history

- 2026-05-14 — verbatim read (full 31 pages over two passes: pages 1-6 first, pages 7-31 second). Equations 1-14 verified against text. Quantitative χ² values quoted from §4 (pp.18-20). Reading session ~60 min total.

## Archive location

Library: `howard-kahana-2002-tcm.pdf`. Journal of Mathematical Psychology 46, 269-299 (2002).
