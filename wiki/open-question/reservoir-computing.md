---
type: open-question
name: Reservoir computing — should the caddy adopt a preconfigured-substrate + learned-readout architecture?
status: OPEN
last_ingested: 2026-05-17
sources: [../source/lukosevicius-jaeger-2009-rc-review.md, ../source/maass-2002-lsm.md, ../source/pathak-2018-chaotic-prediction.md, ../source/pascanu-jaeger-2011-wm.md, ../source/sussillo-abbott-2009-force.md, ../source/gu-goel-re-2022-s4.md, ../source/gu-dao-2023-mamba.md, ../source/yamazaki-tanaka-2007-cerebellum-lsm.md, ../source/buzsaki-2015-spw-r.md]
epistemic_tags: [asserted, measured, contested, speculated]
tags: [reservoir-computing, echo-state-networks, liquid-state-machines, preconfigured-vocabulary, caddy, m14, sketch-a-dead, ssm-bridge, biology-divergence]
---

> **Epistemic status (2026-05-17):** This page has been **anchored against 5 verbatim reads** ([lukosevicius-jaeger-2009-rc-review](../source/lukosevicius-jaeger-2009-rc-review.md), [maass-2002-lsm](../source/maass-2002-lsm.md), [pathak-2018-chaotic-prediction](../source/pathak-2018-chaotic-prediction.md), [pascanu-jaeger-2011-wm](../source/pascanu-jaeger-2011-wm.md), [sussillo-abbott-2009-force](../source/sussillo-abbott-2009-force.md)) and 3 abstract-only reads ([gu-goel-re-2022-s4](../source/gu-goel-re-2022-s4.md), [gu-dao-2023-mamba](../source/gu-dao-2023-mamba.md), [yamazaki-tanaka-2007-cerebellum-lsm](../source/yamazaki-tanaka-2007-cerebellum-lsm.md)). The core findings are summarised in the new **"Literature-review findings (2026-05-17)"** section below. The original exploration-starter sections are preserved with epistemic-tag updates and strikethroughs on resolved sub-questions. The doc remains an OPEN question because the caddy-decision implication ("biology-divergence vs. convergence story") is not yet resolvable from the literature — it depends on whether biology's "fixed substrate" commitment carries information the engineering descendants have abandoned for tractability reasons or for fundamental ones.

## Literature-review findings (2026-05-17)

`[ASSERTED]` Five load-bearing findings from the 8-paper read pass:

### Finding 1 — The "fixed substrate" commitment has been progressively abandoned by RC's engineering descendants

Both papers from inside the RC community that addressed memory or autonomous-generation tasks **extended the textbook architecture**:

- [Pascanu & Jaeger 2011](../source/pascanu-jaeger-2011-wm.md) added WM-units with **trainable feedback weights into the reservoir** for a bracket-nesting working-memory task. The architecture is no longer "fixed reservoir + linear readout".
- [Sussillo & Abbott 2009 FORCE](../source/sussillo-abbott-2009-force.md) showed textbook ESN **empirically fails** on autonomous pattern generation (~50% trial instability post-training). FORCE adds online RLS training with controlled feedback; the 1C variant trains *inner reservoir synapses* directly.

The modern SSM lineage that descends from RC's mathematical framework completed the abandonment:

- [S4 (Gu/Goel/Ré 2022)](../source/gu-goel-re-2022-s4.md) uses *structured + trained* A matrices (HiPPO-initialised, then gradient-optimised).
- [Mamba (Gu/Dao 2023)](../source/gu-dao-2023-mamba.md) makes the A matrix **input-dependent** (selectivity) — content-aware dynamics, the explicit opposite of RC's content-independent substrate commitment.

The arc: random fixed → structured fixed → structured trained → structured trained input-conditioned. Each step abandoned more of pure-RC's commitments and got better results on standard benchmarks.

### Finding 2 — The biological RC precedent (cerebellum) is FEEDFORWARD, not recurrent

The 50-year-mature biological-computational hypothesis cited in this doc's original "Why it matters" section is structurally different from the recurrent-RC ESN/LSM canonical model.

[Yamazaki & Tanaka 2007](../source/yamazaki-tanaka-2007-cerebellum-lsm.md) abstract: *"The model's granular layer generates a finite but very long sequence of active neuron populations **without recurrence**."* The cerebellar "reservoir" is closer to a deep random projection layer with sequential structure than to a chaotic dynamical system.

Two consequences for the M14 → RC analogy:
1. If biology's working RC is feedforward, the analogy to Buzsáki's *recurrent* hippocampus (CA3 in particular) is weaker than this doc originally assumed.
2. A feedforward-substrate caddy is a different architectural sketch — possibly closer to "frozen random projection + trained readout", which is structurally identical to LoRA-on-frozen-base. See [lora](../concept/lora.md) and [catastrophic-interference](../concept/catastrophic-interference.md).

### Finding 3 — Pathak 2018 KS-prediction result, quantified

`[MEASURED]` [Pathak et al. 2018](../source/pathak-2018-chaotic-prediction.md): **8 Lyapunov times of prediction** on Kuramoto-Sivashinsky chaotic PDE, scale-invariant via parallel-reservoir spatial decomposition (linear in spatial extent L; demonstrated up to L=1600 with Kaplan-Yorke dimension D_KY=338, total 25.6M neurons across 512 parallel reservoirs of 5000 each).

Construct-validity note: "8 Lyapunov times" measures *prediction horizon on a known dynamical system*, not memory capacity or sequence storage. The metric does not transfer directly to caddy memory-task evaluation.

Notable empirical details:
- Pure linear readout **did not work** — required P_2·r² quadratic term to break a parity symmetry. Direct evidence against the strong form of "RC bindings are purely linear" — important refinement for [catastrophic-interference](../concept/catastrophic-interference.md).
- Spectral radius ρ=0.6, not the textbook ρ=0.9. Edge-of-chaos is task-dependent in practice.

### Finding 4 — Memory capacity is provably linear in N

`[ASSERTED]` From [Lukoševičius & Jaeger 2009](../source/lukosevicius-jaeger-2009-rc-review.md): Jaeger's memory capacity measure C ≈ Nλ/(1−λ) under stated assumptions.

A 10⁶-neuron pure reservoir at ρ=0.9 holds ~10⁷ time-step-equivalents of input history. This is a hard upper bound; capacity does not grow combinatorially. Important caveat against treating RC as a high-capacity substrate.

Open caddy-relevant question: does the M14 preconfigured-vocabulary framing want *small fixed repertoire + large compositional combinatorics* (which a linear-capacity substrate could support if the readout does the combinatorics) or *large stored library* (which a linear-capacity substrate cannot)?

### Finding 5 — Spectral-radius < 1 condition for ESP is folklore

`[ASSERTED]` Both [Lukoševičius & Jaeger 2009](../source/lukosevicius-jaeger-2009-rc-review.md) and [Pascanu & Jaeger 2011](../source/pascanu-jaeger-2011-wm.md) **explicitly call out** that ρ < 1 is *neither necessary nor sufficient* for the echo-state property. The "folklore belief" was corrected by Buehner & Young 2006 with refined algebraic conditions.

Any wiki claim that uses "spectral radius < 1" as load-bearing should be re-anchored. The empirical sweet spot ρ ≈ 0.9 is engineering practice, not theory.

### Caddy-decision implication — Sketch A is empirically dead at scale; Sketches B and C remain alive

**Sketch A (pure RC as caddy substrate)** is structurally identical to the textbook ESN/LSM commitment that *the RC community's own follow-up work* extended away from. Both [Pascanu/Jaeger 2011](../source/pascanu-jaeger-2011-wm.md) and [Sussillo/Abbott 2009](../source/sussillo-abbott-2009-force.md) demonstrate that pure ESN fails on tasks the caddy would need to handle (working memory at scale; autonomous generation). The 50-year-mature engineering wisdom is: this commitment doesn't survive contact with hard tasks.

**Sketch B (reservoir-as-pre-training)** is the convergence-story sketch. S4 is essentially this: structured initialisation (HiPPO) + gradient training. The engineering field has voted with its feet for Sketch B; the question is whether the additional "shape pre-training around dynamics" commitment beats what S4 already does.

**Sketch C (reservoir + writable buffer)** is the biology-divergence sketch. The M14 SPW-R off-line consolidation regime maps naturally here — the reservoir provides the trajectory space; the writable buffer accumulates (trajectory, content) pairs; off-line consolidation replays. Sketch C is structurally distinct from both Sketch A and Sketch B, and from S4/Mamba. It remains the architecturally most-interesting sketch for the caddy decision.

**Honest residual uncertainty:** the engineering-vs-biology divergence is not resolvable from the literature alone. Either (a) biology kept the fixed-substrate commitment because biology is doing something ML hasn't figured out, or (b) "fixed substrate" purity was always a stepping-stone, and the right caddy lives somewhere in the Pascanu/Jaeger or Mamba zone. The caddy designed under (a) looks very different from the caddy designed under (b).

---

## The question

`[ASSERTED]` Reservoir computing (RC) — Echo State Networks ([Jaeger 2001](https://www.ai.rug.nl/minds/uploads/2261_LukoseviciusJaeger09.pdf "pending verbatim read")) and Liquid State Machines ([Maass 2002](../source/maass-2002-lsm.md)) — commits to **a fixed, randomly-initialised, recurrent substrate plus a separately-trained readout**. The substrate provides rich pre-existing dynamics; experience trains only the cheap linear readout that interprets the substrate's state. This is the canonical RC commitment as defined by the founding papers and the [Lukoševičius & Jaeger 2009 review](../source/lukosevicius-jaeger-2009-rc-review.md).

This is structurally close to two things Kyrja already cares about:

1. **Buzsáki's preconfigured-vocabulary framing of the hippocampus** (M14 — see [mechanism-gap-matrix](../concept/mechanism-gap-matrix.md) and [buzsaki-2015-spw-r](../source/buzsaki-2015-spw-r.md)). Buzsáki proposes the hippocampus generates a large pre-organised repertoire of sequences, and experience *selects* from the repertoire rather than writing new sequences from scratch.
2. **The [caddy](../concept/caddy.md)'s commitment 1 (separately-addressable model state)** and **commitment 5 (auxiliary objective beyond consumer task loss).** A reservoir-flavoured caddy would have a fixed dynamical substrate as commitment 1 and a separate readout-training objective as commitment 5.

The question:

> **Does a reservoir-computing-shaped caddy — fixed substrate + learned readout + content-binding to dynamical trajectories rather than to weights — implement Buzsáki's preconfigured-vocabulary framing in a way that current LLM-era retrieval-augmented architectures (RETRO, Memorizing Transformer, Memory³, MERLIN) do not?**

**Refined (2026-05-17):** The literature-review findings refine this. Pure RC's "fixed substrate" commitment is **empirically dead** for hard tasks; the question becomes whether a *hybrid* caddy (Sketch B or C) inherits Buzsáki's framing in a structurally meaningful way that the SSM lineage does not.

## Why it matters

`[ASSERTED]` Three reasons RC was worth a verbatim read pass:

1. **Direct M14 mechanism candidate.** Buzsáki's preconfigured-vocabulary claim has no specified implementation in current LLM-memory architectures. Reservoir computing is the only architecture I'm aware of where the *substrate's structure is genuinely fixed and pre-existing, and only the readout learns*. **Refined (2026-05-17):** pure RC's fixed-substrate commitment was abandoned by the engineering field; the candidate-implementation argument now applies to hybrid Sketches B and C, not Sketch A.

2. **50-year biological precedent.** The cerebellum has been modelled as a reservoir since Marr 1969 and Albus 1971. Granule cells provide the rich combinatorial state; Purkinje cells are the trained readout. **Refined (2026-05-17):** [Yamazaki & Tanaka 2007](../source/yamazaki-tanaka-2007-cerebellum-lsm.md) shows the granular-layer model is *feedforward*, not chaotic-recurrent. The 50-year precedent is for a *different architectural shape* than the canonical ESN/LSM. The hippocampus-as-reservoir analogy is weaker than this doc originally assumed.

3. **Substrate-antagonism amplifier.** Substrate (Hope-shape) commits to **continuously updating** the model. Reservoir computing commits to **never updating** the substrate. These are directly architecturally opposed. The caddy (commitments 1+5) lives comfortably with either choice; substrate cannot adopt RC without abandoning its defining commitment. Adds another tick to the substrate-antagonism count maintained in the matrix walk.

## What I know (now primary-sourced)

`[ASSERTED]` Reservoir computing in five claims:

1. **Three components:** input layer projects input into reservoir; reservoir is a large recurrent network (~100s-1000s of neurons) with **random, fixed connectivity** never trained after initialisation; readout layer (usually linear regression) maps reservoir state → task output. Only the readout learns. Anchor: [lukosevicius-jaeger-2009-rc-review §3.1–3.2](../source/lukosevicius-jaeger-2009-rc-review.md).

2. **Echo state property:** past inputs progressively fade, recent inputs dominate. Gives bounded memory automatically — no vanishing-gradient problem because no backprop through time. **`[CONTESTED]` correction:** the spectral-radius < 1 condition is *neither necessary nor sufficient* for the ESP — *"in spite of a folklore belief in the field that it is both"* ([lukosevicius-jaeger-2009-rc-review §3.1](../source/lukosevicius-jaeger-2009-rc-review.md), [pascanu-jaeger-2011-wm §2](../source/pascanu-jaeger-2011-wm.md)).

3. **Edge of chaos:** spectral radius near 1 (boundary between damped and chaotic dynamics) gives optimal trajectory richness. **`[CONTESTED]` correction:** empirically real but theoretically unproven; ρ ≈ 0.9 is engineering folklore. Pathak used ρ=0.6 for chaotic-PDE prediction; Pascanu/Jaeger used ρ=0.5 for working memory ([lukosevicius-jaeger-2009-rc-review §9](../source/lukosevicius-jaeger-2009-rc-review.md), [pathak-2018-chaotic-prediction](../source/pathak-2018-chaotic-prediction.md), [pascanu-jaeger-2011-wm](../source/pascanu-jaeger-2011-wm.md)).

4. **Trajectory space is combinatorial:** different inputs trace different trajectories through reservoir state-space; the trajectory space is enormous; the readout picks which subset of state-space corresponds to which output. Anchored as Maass's *Separation Property* ([maass-2002-lsm §2](../source/maass-2002-lsm.md)). **Caveat:** memory capacity is provably linear in N (C ≈ Nλ/(1−λ)), not combinatorial — see Finding 4 above.

5. **Where it works empirically:** dynamical-systems prediction ([pathak-2018-chaotic-prediction](../source/pathak-2018-chaotic-prediction.md) — 8 Lyapunov times on KS chaotic PDE), time-series forecasting, speech recognition (historically). It's never been the dominant approach in mainstream deep learning but it's never gone extinct, and it's the dominant approach in some niches (physical reservoirs in photonics, neuromorphic chips). **Important add:** pure RC fails on (a) autonomous generation ([sussillo-abbott-2009-force](../source/sussillo-abbott-2009-force.md)) and (b) memory tasks requiring persistence beyond fading-memory horizons ([pascanu-jaeger-2011-wm](../source/pascanu-jaeger-2011-wm.md)) — both required RC extensions.

## Where this might land for the caddy

`[ASSERTED]` Three architectural sketches the literature now supports or kills:

### Sketch A: reservoir-as-caddy-substrate (most direct) — `[EMPIRICALLY DEAD]`

- The caddy's internal state is a large fixed reservoir
- Input: experience embeddings (compressed by an encoder, possibly the consumer LLM's encoder)
- Readout: learned linear or shallow-nonlinear projection from reservoir state → retrieval candidates
- Content-binding: experience traces a trajectory through the reservoir; the trajectory is the "stored memory"
- Sequence stitching (M14's joint-replays): trajectories that pass near each other in state-space can be concatenated through shared anchor states
- The reservoir's structure is fixed; only the readout co-trains with the consumer

~~This is the most-faithful sketch. It maps cleanly to RC's standard architecture and to Buzsáki's preconfigured-vocabulary framing.~~

**`[REJECTED]` (2026-05-17):** Pure-RC "fixed substrate + linear readout" was empirically insufficient for the working-memory task ([pascanu-jaeger-2011-wm](../source/pascanu-jaeger-2011-wm.md) — required WM-units with trainable feedback into reservoir) and for autonomous pattern generation ([sussillo-abbott-2009-force](../source/sussillo-abbott-2009-force.md) — required FORCE online training with feedback control; 1C variant trained inner reservoir). Even the cleanest prediction task ([pathak-2018-chaotic-prediction](../source/pathak-2018-chaotic-prediction.md)) required P_2·r² quadratic readout — pure linear failed.

The pattern is consistent: every group that tried to use textbook RC for non-trivial tasks had to extend it. Sketch A is the architectural commitment that the RC field itself voted against.

### Sketch B: reservoir-as-pre-training (less radical) — `[ALIVE; partially instantiated by S4]`

- The caddy has a learned (gradient-trained) internal state, like MERLIN
- But its initial weights come from a *pre-training pass that shapes the reservoir's intrinsic dynamics*, not from random initialisation
- The reservoir-shaped pre-training is the auxiliary objective (MERLIN's MBP replacement)
- After pre-training, the substrate is fine-tuned by the consumer's task loss

This is a hedge — keeps gradient-flow through the substrate but uses RC ideas to shape what gets pre-trained.

**Refined (2026-05-17):** S4 essentially does this — structured initialisation (HiPPO theory) plus gradient training. The engineering field has *converged* on Sketch B as the right shape for sequence-modelling architectures. The open question for caddy: does adding the *RC-specific* pre-training discipline (matching empirical reservoir hyperparameters; targeting specific echo-state properties) beat what S4/Mamba already do, or is the lineage already past the point where Sketch B adds value?

### Sketch C: reservoir + writable buffer (hybrid) — `[ALIVE; architecturally distinct from S4/Mamba]`

- Fixed reservoir provides combinatorial trajectory space
- Separately writable per-memory store (vector DB, kNN) accumulates experience traces as `(reservoir-trajectory, content)` pairs
- Readout indexes into the per-memory store via the current reservoir state
- Off-line consolidation passes (M14's SPW-R analogue) replay stored trajectories through the reservoir to learn new readout patterns

This bridges RC's "fixed substrate" commitment with the discrete-unit-memory-architecture family's "separately addressable store" commitment. Plausibly the most-buildable shape.

**Refined (2026-05-17):** Sketch C is *structurally distinct* from both Sketch A and Sketch B, *and* from the S4/Mamba lineage. It explicitly couples a fixed dynamical substrate with a separately-addressable per-memory store and off-line consolidation. The M14 SPW-R framework (off-line-only consolidation) maps onto Sketch C natively — see [consolidation-channel](../concept/consolidation-channel.md). **This remains the architecturally most interesting sketch for the caddy decision** because it is the one the literature does not address.

## Open sub-questions for the exploration

`[ASSERTED]` These are the questions the parallel-window investigation was meant to answer. Updated 2026-05-17 with literature-review outcomes — resolved questions struck through, unresolved questions sharpened.

1. ~~**Does RC scale?** Modern reservoirs are typically small (~10² to 10⁴ neurons). What happens at LLM-relevant scale (10⁶+)? Are there fundamental obstacles, or just engineering ones?~~ **`[PARTLY RESOLVED]`** — [Pathak 2018](../source/pathak-2018-chaotic-prediction.md) demonstrated scale-invariant prediction up to 25.6M neurons via parallel decomposition, but the trick requires *spatial locality* in the input. Caddy inputs (embeddings, language) have no native spatial coordinate; whether soft-locality (embedding-similarity) enables an analogous decomposition is the remaining open question.

2. ~~**Is the readout-only-trains regime stable at scale?**~~ **`[RESOLVED — NO]`** — [Sussillo & Abbott 2009](../source/sussillo-abbott-2009-force.md) demonstrated readout-only training (echo-state clamping) **fails on autonomous pattern generation** in ~50% of trials. Pure linear readout also failed for Pathak's KS prediction (needed P_2·r²). The pure-readout-only regime is not stable; FORCE-style online training with feedback control is the established workaround.

3. ~~**Can RC be co-trained with a downstream transformer?**~~ **`[RESOLVED — VIA ABANDONMENT]`** — the SSM lineage ([gu-goel-re-2022-s4](../source/gu-goel-re-2022-s4.md), [gu-dao-2023-mamba](../source/gu-dao-2023-mamba.md)) abandoned the fixed-substrate commitment entirely; A is trained and (in Mamba) input-dependent. Co-training with downstream transformers happens naturally as a result. The cost is that "RC" in this regime is just "structured trained recurrent layer", not "fixed random substrate".

4. **What's the empirical sequence-stitching capacity? `[UNRESOLVED, SHARPENED]`** — M14's joint-replay phenomenon is sequence-level recombination through shared anchor states. None of the read papers studied trajectory concatenation as an explicit capability. Sharpened: does Pascanu/Jaeger's γ-attractor framework (input-induced partial attractors) provide a mathematical handle on sequence-concatenation? Or does this require a Sketch-C-style off-line consolidation operator that no RC paper has built?

5. **Is "edge of chaos" the right tuning target for memory rather than prediction? `[SHARPENED]`** — Pathak (ρ=0.6) and Pascanu/Jaeger (ρ=0.5) both used spectral radii *below* the textbook ρ=0.9. Memory may want *lower* spectral radius than prediction. Sharpened with the folklore caveat: spectral radius isn't even the right *handle* on the echo-state property; refined algebraic conditions (Buehner & Young 2006) exist but aren't load-bearing in the papers I read.

6. ~~**What's the relationship to State Space Models (SSMs)?**~~ **`[RESOLVED]`** — SSMs are mathematical descendants of RC's linear-state-space framework (x'(t) = Ax + Bu, y = Cx + Du). The lineage abandoned RC's "random + fixed" commitment in steps: S4 made A structured + trained; Mamba made A input-dependent. Mamba is the modern realisation of "fixed-ish recurrent dynamics + content-aware readout" — but with the dynamics also content-aware.

7. **What's the relationship to Hopfield Networks? `[UNRESOLVED]`** — modern Hopfield (Ramsauer 2020) is in the matrix's candidate-row list. Hopfield is content-addressable memory via pattern completion. RC is rich-dynamics + readout. The Hopfield-attention equivalence shows attention is pattern completion; how does RC relate to that mathematically? Not addressed by any read paper.

8. **What auxiliary objective would the readout train under in a memory caddy? `[SHARPENED]`** — FORCE provides one concrete answer: the readout trains against a target with online RLS, and the error signal jointly stabilises chaos *and* drives learning. This implies caddy commitment 5 must include a target-generating mechanism (an internal model that computes "what should the readout have output?"). [Sussillo & Abbott 2009](../source/sussillo-abbott-2009-force.md) hypothesise cerebellum as the biological target-generator; in caddy terms this is a system-design constraint not addressed in the open-question doc.

9. ~~**Does RC actually work for sequence problems, or is it mostly dynamical-systems prediction?**~~ **`[PARTLY RESOLVED]`** — RC is strongest on *prediction* tasks with short-to-medium fading-memory horizons. *Generation* (without teacher forcing) is acknowledged in [lukosevicius-jaeger-2009-rc-review §9](../source/lukosevicius-jaeger-2009-rc-review.md) as an open challenge; [sussillo-abbott-2009-force](../source/sussillo-abbott-2009-force.md) partially addressed it via FORCE for low-dimensional motor patterns; LLM-era sequence problems (language) remain outside the demonstrated regime.

10. ~~**What kills it?**~~ **`[PARTLY RESOLVED]`** — RC's empirical limits are well-documented: (a) memory horizon is bounded by fading-memory regime (needs extension via Pascanu/Jaeger WM-units or similar); (b) autonomous generation requires FORCE-style training; (c) the textbook commitment to fixed random reservoirs has been progressively traded for structured-trained-input-conditioned A matrices in the SSM lineage with substantial gains. The engineering field's verdict is "the substrate-fixed commitment isn't worth what it costs in capability." Whether this verdict applies to *biological* substrates (cerebellum, hippocampus) is a separate question.

## Suggested reading order for the parallel window (with completion status)

`[ASSERTED]` Reading completion as of 2026-05-17:

**Foundational (P0):**
- Jaeger 2001 — *The "echo state" approach to analysing and training recurrent neural networks*. The original Echo State Networks paper. GMD-Report 148. **Pending verbatim read** — claims covered transitively by [lukosevicius-jaeger-2009-rc-review](../source/lukosevicius-jaeger-2009-rc-review.md).
- ✓ Maass, Natschläger & Markram 2002 — *Real-time computing without stable states*. **Verbatim read** — see [maass-2002-lsm](../source/maass-2002-lsm.md).
- ✓ Lukoševičius & Jaeger 2009 — *Reservoir computing approaches to recurrent neural network training*. **Verbatim read** — see [lukosevicius-jaeger-2009-rc-review](../source/lukosevicius-jaeger-2009-rc-review.md).

**Modern landmark (P0):**
- ✓ Pathak, Hunt, Girvan, Lu & Ott 2018 — *Model-free prediction of large spatiotemporally chaotic systems from data*. **Verbatim read** — see [pathak-2018-chaotic-prediction](../source/pathak-2018-chaotic-prediction.md).
- Tanaka et al. 2019 — *Recent advances in physical reservoir computing: A review*. **Skipped this pass** — relevance is to hardware-RC scaling/energy questions, not caddy-architectural decisions.

**Biological connection (P1):**
- Marr 1969, Albus 1971 — original cerebellum-as-pattern-recognizer papers. **Skipped this pass** — claims covered transitively by [yamazaki-tanaka-2007-cerebellum-lsm](../source/yamazaki-tanaka-2007-cerebellum-lsm.md).
- Buonomano & Maass 2009 — cortex-as-reservoir. **Skipped this pass** — not load-bearing for current decision; revisit if caddy commitment to cortex-shape ever becomes load-bearing.
- ✓ Yamazaki & Tanaka 2007 — *The cerebellum as a liquid state machine*. **Abstract-only read** — see [yamazaki-tanaka-2007-cerebellum-lsm](../source/yamazaki-tanaka-2007-cerebellum-lsm.md). Verbatim read pending if the cerebellum-as-feedforward-LSM claim becomes load-bearing.

**Co-training and modern hybrids (P1):**
- ✓ Pascanu & Jaeger 2011 — *A neurodynamical model for working memory*. **Verbatim read** — see [pascanu-jaeger-2011-wm](../source/pascanu-jaeger-2011-wm.md). **Load-bearing for the Sketch A rejection.**
- Gallicchio & Micheli 2017 — *Deep reservoir computing*. **Skipped this pass** — would inform scaling questions if caddy moves toward deep-RC variants.
- ✓ Sussillo & Abbott 2009 — *Generating coherent patterns of activity from chaotic neural networks*. **Read via PMC HTML extract** — see [sussillo-abbott-2009-force](../source/sussillo-abbott-2009-force.md). **Load-bearing for the Sketch A rejection.**

**SSM / Mamba connection (P2):**
- ✓ Gu, Goel & Ré 2022 — *S4*. **Abstract-only read** — see [gu-goel-re-2022-s4](../source/gu-goel-re-2022-s4.md).
- ✓ Gu & Dao 2023 — *Mamba*. **Source page already existed** at [gu-dao-2023-mamba](../source/gu-dao-2023-mamba.md); cross-link added.

**Anti-cases (P2) — what does NOT work in RC:**
- ✓ Lukoševičius & Jaeger 2009 review covers this in §9 Discussion.
- Verzelli et al. 2019 — *Echo state networks with self-normalization*. **Skipped this pass** — the headline finding (RC has serious tuning-stability issues at scale) is already attested by Pascanu/Jaeger and Sussillo/Abbott; deeper read deferred.

## Bridges back to existing Kyrja material

`[ASSERTED]` Direct cross-links — updated 2026-05-17 with literature-review outcomes:

- [concept/caddy](../concept/caddy.md) — the architectural concept this exploration tests. RC is a candidate for commitment 1 (separately-addressable model state) and commitment 5 (auxiliary objective). **Refined:** pure-RC Sketch A is empirically dead; Sketches B and C remain candidates.
- [concept/mechanism-gap-matrix](../concept/mechanism-gap-matrix.md) M14 row — Buzsáki preconfigured-vocabulary is the biological precedent. **Refined:** the cerebellar-RC precedent is feedforward; the recurrent-RC hippocampus analogy is weaker than initially framed.
- [source/buzsaki-2015-spw-r](../source/buzsaki-2015-spw-r.md) — primary anchor for the preconfigured-vocabulary framing.
- [open-question/memory-caddy](./memory-caddy.md) — the live design question RC might inform.
- [concept/discrete-unit-memory-architecture](../concept/discrete-unit-memory-architecture.md) — the family RC-caddy would join (or possibly challenge — is an RC substrate still "discrete-unit"?). **Refined:** Sketch C is the discrete-unit-compatible variant; pure RC sits outside the family.
- [concept/silent-engrams](../concept/silent-engrams.md) — RC's reservoir state is naturally larger than what the readout exposes; matches M06 silent-engram property. **Anchored** in [pascanu-jaeger-2011-wm](../source/pascanu-jaeger-2011-wm.md) §4 γ-attractor framing.
- [concept/catastrophic-interference](../concept/catastrophic-interference.md) — RC appears as one of the four-and-a-half known solution shapes. **Re-anchored** with the new source pages; "even the bindings are linear" framing softened (Pathak's P_2·r² is empirically non-linear).
- [concept/lora](../concept/lora.md) — LoRA is structurally similar to RC's "frozen substrate + trained low-rank delta" pattern. **Anchored** via the LSM cerebellar precedent which is feedforward (same architectural shape as frozen-base + adapter).

`[ASSERTED]` Threads to pull on (updated):

- **Algorithmic-wedge angle:** confirmed. RC has a "pre-allocated combinatorial structure, content binds at runtime" shape that resembles **consistent hashing** (ring + virtual nodes pre-exist, keys bind at runtime), **locality-sensitive hashing** (random hash functions pre-exist, content gets bucketed at write time), and **Bloom filters** (random hash functions pre-exist, content marks bits). The shape pattern is the same: structure first, content second.
- **MBP-was-dropped angle:** RC says the substrate is *fully fixed*; MERLIN's MBP said the substrate is *trained but with a non-task auxiliary loss*. These are different bets. **Refined (2026-05-17):** the literature evidence is that "fully fixed" doesn't work for hard tasks; MBP-shape (structured initialisation + targeted auxiliary loss) survives. S4's HiPPO + gradient training is essentially MBP at the SSM scale.
- **Off-line vs on-line angle:** RC's substrate runs at inference time during normal forward passes. Buzsáki's SPW-Rs operate during off-line states only. **Refined (2026-05-17):** the answer is "different operational regimes that don't co-exist for the *substrate*". Sketch C resolves this by putting the *consolidation operator* (which replays trajectories through the substrate) off-line, while the substrate itself runs on-line during normal inference. Maps onto [consolidation-channel](../concept/consolidation-channel.md).

## What evidence would resolve this question

`[ASSERTED]` Updated 2026-05-17:

**Evidence to promote (RC informs caddy):**
- ~~Existing RC work at LLM-scale (10⁶+ reservoir neurons) demonstrates the regime is engineering-tractable~~ **Pathak demonstrated this for prediction tasks via parallel decomposition; the trick requires spatial locality. For caddy: need evidence that embedding-similarity-as-soft-locality enables an analogous decomposition.**
- ~~Sequence-concatenation experiments in RC show M14-style joint-replay capability is implementable~~ **No RC paper studied this directly. Open: does Pascanu/Jaeger's γ-attractor framework support trajectory concatenation, or is this a Sketch-C-only capability?**
- ~~A clear gap analysis showing RETRO/Memorizing-Transformer/Memory³ fail to do something RC can do~~ **Reframed:** show that *Sketch C* does something the SSM lineage (S4/Mamba) cannot — specifically off-line consolidation with explicit (trajectory, content) pairs.
- ~~A buildable Sketch C (reservoir + writable buffer) design with concrete training procedure~~ **Still open. Sketch C is the architecturally most interesting candidate but no published work has built it.**

**Evidence to close (RC interesting but not load-bearing):**
- ~~RC's empirical limits make it a dead-end at LLM scale~~ **Pure RC is empirically dead for caddy-relevant tasks; this is *established* for Sketch A but does not close Sketches B and C.**
- ~~The "fixed substrate" property is recoverable from standard transformers by freezing-after-pretraining (no need for true RC)~~ **Frozen-base + LoRA delivers exactly this; see [catastrophic-interference](../concept/catastrophic-interference.md). Sketch B is structurally identical to frozen-base + adapter.**
- ~~Modern SSMs already capture everything RC has plus content-awareness; RC is a subsumed paradigm~~ **`[ASSERTED]` — S4 and Mamba subsume the engineering value of RC. The remaining RC-specific value (if any) is in (a) Sketch C's off-line consolidation regime, (b) biological-fidelity considerations the SSM lineage doesn't address.**
- ~~The cerebellum-as-reservoir analogy doesn't actually transfer to hippocampus (Buzsáki's preconfigured-vocabulary claim is structurally different from cerebellar RC)~~ **`[PARTLY-ASSERTED]` — Yamazaki/Tanaka's cerebellum-as-LSM is feedforward; the hippocampus is densely recurrent. The architectural shapes are different; importing the cerebellar template directly to hippocampus is not justified by the literature.**

## Operational notes for the parallel-window exploration

`[ASSERTED]` The 2026-05-17 ingest replaces this section's prior guidance. The literature-review pass has been completed; the open question is no longer "go read the papers" but "what's the next experimental or design step for Sketch C?"

Suggested next moves (in rough order of leverage):
1. **Pressure-test Sketch C against the Norman rubric** ([norman-rubric](../concept/norman-rubric.md)) — does the reservoir+writable-buffer hybrid actually score better than EM-LLM (2.5/5) on the five evaluable properties? Especially: temporal contiguity and competition at retrieval.
2. **Build a toy Sketch C implementation** — 50-line NumPy reservoir + tiny vector store + naive consolidation operator. Test on a memory-task benchmark. The goal is intuition, not benchmark-beating.
3. **Read the Mamba paper verbatim** to nail down what "content-aware A matrix" buys, and whether Sketch C can adopt selectivity in its reservoir.
4. **Read Hopfield-attention equivalence (Ramsauer 2020) verbatim** to address sub-question 7 — relationship between RC, Hopfield pattern completion, and attention.

## Source archive

`[ASSERTED]` This page was written 2026-05-16 evening during the M14 walk in the main window as an exploration starter. The 2026-05-17 update reflects an 8-paper literature-review pass executed in a side-quest window (Nils/indigo). The original speculation-heavy sections are preserved with epistemic-tag updates and strikethroughs on resolved sub-questions; the new "Literature-review findings (2026-05-17)" section near the top is the post-exploration summary.

Verbatim reads completed:
- [lukosevicius-jaeger-2009-rc-review](../source/lukosevicius-jaeger-2009-rc-review.md) (canonical RC review)
- [maass-2002-lsm](../source/maass-2002-lsm.md) (LSM definition; pages 1–10)
- [pathak-2018-chaotic-prediction](../source/pathak-2018-chaotic-prediction.md) (full PRL, 5 pages)
- [pascanu-jaeger-2011-wm](../source/pascanu-jaeger-2011-wm.md) (preprint pages 1–9)
- [sussillo-abbott-2009-force](../source/sussillo-abbott-2009-force.md) (PMC HTML extract)

Abstract-only reads (with verbatim-read pending):
- [gu-goel-re-2022-s4](../source/gu-goel-re-2022-s4.md)
- [yamazaki-tanaka-2007-cerebellum-lsm](../source/yamazaki-tanaka-2007-cerebellum-lsm.md)

Cross-link only (source already existed):
- [gu-dao-2023-mamba](../source/gu-dao-2023-mamba.md)

## Related

- [[caddy]] — the architectural concept this exploration tests
- [[mechanism-gap-matrix]] M14 row — Buzsáki preconfigured-vocabulary
- [[memory-caddy]] — the live design question
- [[discrete-unit-memory-architecture]] — the family question RC may extend or challenge
- [[silent-engrams]] — M06; RC's reservoir state matches this naturally
- [[consolidation-channel]] — off-line consolidation; RC's "fixed substrate" interacts with this
- [[catastrophic-interference]] — RC as one of the four-and-a-half solution shapes
- [[lora]] — structurally similar "frozen substrate + low-rank delta" pattern
- [[buzsaki-2015-spw-r]] — primary biological source
- [[lukosevicius-jaeger-2009-rc-review]] — canonical RC review (anchor for most claims)
- [[maass-2002-lsm]] — LSM founding paper
- [[pathak-2018-chaotic-prediction]] — modern RC landmark
- [[pascanu-jaeger-2011-wm]] — RC for working memory (load-bearing for Sketch A rejection)
- [[sussillo-abbott-2009-force]] — FORCE algorithm (load-bearing for Sketch A rejection)
- [[gu-goel-re-2022-s4]] — SSM lineage (abstract-only)
- [[gu-dao-2023-mamba]] — Mamba selectivity
- [[yamazaki-tanaka-2007-cerebellum-lsm]] — cerebellum-as-LSM (feedforward biology) (abstract-only)
