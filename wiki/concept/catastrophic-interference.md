---
type: concept
name: Catastrophic interference — overwriting of prior learning under unconstrained gradient updates, and the architectural solutions to it
status: timeless
last_ingested: 2026-05-17
sources: [../source/mcclelland-mcnaughton-oreilly-1995-cls.md, ../source/buzsaki-2015-spw-r.md, ../source/lukosevicius-jaeger-2009-rc-review.md, ../source/maass-2002-lsm.md, ../source/pathak-2018-chaotic-prediction.md, ../source/pascanu-jaeger-2011-wm.md, ../source/sussillo-abbott-2009-force.md, ../source/hu-2021-lora.md]
epistemic_tags: [asserted, speculated]
tags: [catastrophic-interference, continual-learning, m11, m14, frozen-substrate, reservoir-computing, lora, architectural-primitive]
---

## Definition

`[ASSERTED]` **Catastrophic interference** (also: *catastrophic forgetting*) is the phenomenon where a neural network trained on task A then trained on task B has its weights shifted to fit B, losing the representations that supported A — often dramatically (~90% of A forgotten after a few epochs of B training). The original demonstration is McCloskey & Cohen 1989; the term has been canonical in continual-learning research since.

The structural cause: gradient descent over shared weights, with no mechanism preserving prior task representations. It is **not a bug** — it is a direct consequence of the optimisation objective. Standard neural network training has no intrinsic preference for preserving old behaviour while learning new.

This concept page exists because:
1. Catastrophic interference is referenced across 11+ Kyrja wiki pages, often invoked without anchor.
2. The matrix walk (M11, M14, M15) produced a clean taxonomy of architectural solutions; that taxonomy deserves a single canonical reference.
3. Future Kyrja design decisions about caddy / consolidation-channel / LoRA-interface choices depend on understanding which solution-shape each design adopts.

## The four-and-a-half known solution shapes

`[ASSERTED]` Catastrophic interference is a *write-time architectural choice*, not a fundamental property of learning systems. Several distinct architectural commitments avoid it:

| Solution | What's fixed | What's plastic | Interference avoided by |
|---|---|---|---|
| Standard NN training | Architecture only | All weights | Nothing — interference happens |
| **M11 / interleaved replay** | Architecture + fast store transient | Slow weights | Replaying old data alongside new during consolidation |
| **M14 / preconfigured vocabulary** | Substrate structure | Content-to-position bindings | Substrate never changes; experience selects from repertoire |
| **Reservoir computing** | Reservoir + connectivity | Readout layer only | Substrate never changes; only readout learns |
| **Frozen LLM + LoRA / adapters** | Base model | Low-rank delta per task | Base model untouched; switching adapters preserves base |

The half: **elastic weight consolidation (EWC, Kirkpatrick 2017)** and similar regularisation-based methods penalise updates to weights important for previous tasks. Distinct from the five above because nothing is structurally fixed; the system uses a *loss-function modification* rather than an architectural commitment. Effective on benchmarks but less load-bearing for the Kyrja-relevant agent-memory case. [pending source page]

## The biological story (M11 vs M14)

`[ASSERTED]` McClelland, McNaughton & O'Reilly 1995 — the [complementary-learning-systems](./complementary-learning-systems.md) framework — proposed the **dual-system + interleaved-replay** solution. The hippocampus accepts new memories one-shot; the neocortex learns gradually; during consolidation, replay interleaves new patterns with old ones so the slow system doesn't get scrambled.

[Buzsáki 2015](../source/buzsaki-2015-spw-r.md) proposed an alternative: **preconfigured vocabulary**. The hippocampus is not a tabula rasa — it has a pre-existing combinatorial repertoire of sequences. New experience *binds content to existing sequence positions*; it doesn't write new sequences. Interference is reduced because the substrate's structure never changes. (Verbatim p1152: *"In a preconfigured network with self-generated multitudes of sequences, interference is much less of a problem since most sequences are constructed from preexisting neural word sequences in an already balanced system."*)

These solutions are **not competing.** They operate at different levels and likely co-occur in biology:

- M11 is about the **slow store** (neocortex) not getting scrambled during gradual learning over decades.
- M14 is about the **fast store** (hippocampus) not having to generate new sequences for every experience.

A complete architecture probably needs both — fixed-substrate-with-learned-bindings for the fast store, and interleaved-replay-during-consolidation for transfer to a slower learned system.

## The software story (LoRA stumbled into M14)

`[SPECULATED]` The mainstream LLM toolchain has stumbled into M14-shape solutions without ever invoking the biological framing:

- **Frozen pretrained model + [LoRA](./lora.md)**: the base model is the preconfigured vocabulary; the LoRA delta is the binding policy. Fine-tuning on a new task via LoRA preserves base capability (catastrophe avoided), where full fine-tuning would degrade it (catastrophe occurs). [Hu et al. § 7.3](../source/hu-2021-lora.md) sharpens the mechanism: ΔW operates on the *subordinate* singular directions of W, leaving the dominant pre-training directions intact — preservation is structural, not merely empirical.
- **Adapter-based PEFT**: same shape, slightly different parameterisation.
- **Prompt tuning / prefix tuning**: even more extreme M14-shape — base model entirely fixed, only soft-prompt tokens learn.

The **catastrophic-interference resistance of these methods is direct empirical evidence that the M14 architectural principle works.** Substrate-fixed-only-bindings-update is a real, deployed, production-tested commitment.

[Reservoir computing](../open-question/reservoir-computing.md) is the same architectural principle taken further: the substrate is fixed *and random*, with bindings carried by a typically-linear readout (anchored: [lukosevicius-jaeger-2009-rc-review](../source/lukosevicius-jaeger-2009-rc-review.md), [maass-2002-lsm](../source/maass-2002-lsm.md)). The substrate carries the rich dynamics; the readout interprets them.

**`[ASSERTED]` Caveat from the 2026-05-17 literature review:** pure linear readouts are empirically insufficient for non-trivial tasks. [Pathak 2018](../source/pathak-2018-chaotic-prediction.md) required a quadratic term (P_2·r²) for KS-PDE prediction. [Pascanu & Jaeger 2011](../source/pascanu-jaeger-2011-wm.md) extended ESN with WM-units that have trainable feedback into the reservoir (no longer "readout only"). [Sussillo & Abbott 2009 FORCE](../source/sussillo-abbott-2009-force.md) demonstrated readout-only training (echo-state clamping) *fails* on autonomous pattern generation in ~50% of trials. The "even the bindings are linear" framing characterises *textbook RC* but does not survive contact with hard tasks — both Pascanu/Jaeger and Sussillo/Abbott (RC insiders) extended the architecture. See [reservoir-computing § Sketch A](../open-question/reservoir-computing.md) for the empirical-deadness verdict.

## The interference-vs-decay distinction (M17 nuance)

`[ASSERTED]` [Hardt, Nader & Nadel 2013](../source/hardt-nader-nadel-2013-active-forgetting.md) partition forgetting into two mechanisms:

- **Interference-driven forgetting** — dominates in densely-overlapping representations (early sensory cortex). Happens during active processing.
- **Decay-driven forgetting** — dominates in pattern-separated areas (hippocampus). Happens off-line.

This refines the standard catastrophic-interference picture. Pure interference happens in shared representations; pattern separation defeats it but introduces decay as the alternative loss mechanism. For Kyrja:

- Bolt-on systems with vector-DB storage have *no interference* — each memory is its own row, no shared representation. They have *decay only* (capacity-driven eviction).
- Substrate systems (Hope, EvoSC) operate on shared representations and inherit interference.
- The caddy's choice of substrate-shape determines which failure mode it will face.

**The prerequisite framing (post M17 walk, 2026-05-17):** decay-dominant forgetting only becomes possible once [pattern-separation](./pattern-separation.md) is in place. Without orthogonal coding, similar memories collide and interference is the failure mode that determines what's forgotten — no salience signal can rewrite that. Pattern separation has to come first; then per-memory decay rates become a meaningful policy variable. See [pattern-separation § Why pattern separation is a prerequisite for graded decay](./pattern-separation.md) for the full development and DB analogy.

## Why this matters

`[ASSERTED]` Catastrophic interference is *the* obstacle between current AI systems and an agent-with-persistent-memory. Every design decision about consolidation, admission, persistence, and forgetting interacts with it.

The taxonomy above lets each Kyrja design conversation specify *which* solution-shape it is adopting. Conversations that don't specify the shape end up vague about whether they are committing to M11, M14, both, or neither.

Specifically:

- **Memory-for-the-model (substrate path)** must adopt an explicit solution, because substrate IS shared-weight learning. Default is M11 (interleaved replay during consolidation) or LoRA-shape (frozen base + adapter).
- **Memory-for-the-agent (bolt-on path)** mostly avoids interference architecturally — memories are stored independently — but inherits decay-driven forgetting and admission-control problems instead.
- **Caddy architectures** can adopt either or both. The [caddy concept](./caddy.md) is currently neutral on which shape; this concept page makes the choice explicit.

## Scope limits

`[ASSERTED]`

- **This concept covers the architectural problem, not the optimisation question.** Why gradient descent has this property — second-order curvature, loss-landscape geometry, mode connectivity — is interesting but lives in the broader ML-theory literature. Not in scope here.
- **EWC and similar regularisation methods are mentioned but not deeply covered.** They are valuable in continual-learning benchmarks but less load-bearing for the agent-memory architectural question.
- **Memory consolidation and catastrophic interference are tightly related but distinct concepts.** Consolidation is the operator; interference is the failure mode the operator addresses. See [consolidation-channel](./consolidation-channel.md) for the operator-side framing.
- **The biological version may not perfectly match the artificial version.** Biological forgetting has its own mechanisms (M17 active forgetting, metaplasticity) that don't map cleanly to gradient-descent dynamics.

## Related

`[ASSERTED]`

- [[mechanism-gap-matrix]] M11, M14, M17 rows
- [[complementary-learning-systems]] — McClelland's framework; M11 solution
- [[mcclelland-mcnaughton-oreilly-1995-cls]] — primary source for M11
- [[buzsaki-2015-spw-r]] — primary source for M14
- [[hardt-nader-nadel-2013-active-forgetting]] — interference/decay partition
- [[lora]] — the M14-shape solution the LLM world stumbled into
- [[reservoir-computing]] — the M14 principle taken to its limit
- [[consolidation-channel]] — the operator-side framing
- [[caddy]] — the caddy concept; this page makes the choice of interference-solution-shape explicit
- [[memory-caddy]] — the live design question
- [[substrate-as-memory]] — the substrate-path framing; must adopt one of these solutions
- [[H39-silent-state-primitives]] — silent engrams as M14-related architectural primitive
- [[pattern-separation]] — architectural prerequisite for decay-dominant forgetting; the inverse / partner concept (this page defines the failure mode, pattern-separation defines the prerequisite that prevents it)
- [[H34-forgetting-scores]] — graded forgetting hypothesis; depends on pattern-separation being in place
- [[H43-soft-composition-emergent-construction]] — interacts with interference: soft composition over densely-overlapping keys may compose blurry averages, soft composition over pattern-separated keys composes cleaner basis vectors

## Source archive

`[ASSERTED]` Catastrophic interference was first described by McCloskey & Cohen 1989, *Catastrophic interference in connectionist networks: The sequential learning problem*. Psychology of Learning and Motivation 24, 109-165. No `source/*` page yet — [pending] for future ingest.

The M11 solution was formalised in [McClelland, McNaughton & O'Reilly 1995](../source/mcclelland-mcnaughton-oreilly-1995-cls.md). The M14 solution was articulated in [Buzsáki 2015](../source/buzsaki-2015-spw-r.md). The decay-vs-interference partition is in [Hardt, Nader & Nadel 2013](../source/hardt-nader-nadel-2013-active-forgetting.md). EWC is Kirkpatrick et al. 2017, *Overcoming catastrophic forgetting in neural networks*, PNAS — [pending source page].
