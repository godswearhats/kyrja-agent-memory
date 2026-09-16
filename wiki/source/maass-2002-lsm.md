---
type: source
name: "Maass, Natschläger & Markram 2002 — Real-Time Computing Without Stable States: A New Framework for Neural Computation Based on Perturbations"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [reservoir-computing, liquid-state-machines, foundational, p0, spiking-networks, universal-approximation, cortex-microcircuit]
---

## Citation

Maass, W., Natschläger, T. & Markram, H. (2002). *Real-Time Computing Without Stable States: A New Framework for Neural Computation Based on Perturbations.* Neural Computation 14(11), 2531–2560. DOI: 10.1162/089976602760407955.

## Location

- Publisher (paywalled): <https://direct.mit.edu/neco/article-abstract/14/11/2531/6650/Real-Time-Computing-Without-Stable-States-A-New>
- Maass group preprint: <https://igi-web.tugraz.at/PDF/130.pdf>
- Local archive: [library/papers/maass-2002-lsm.pdf](../../../research/library/papers/maass-2002-lsm.pdf)

## Key claims (with our restatements)

### LSM definition: liquid filter + memoryless readout

**Paper (§3):** A Liquid State Machine M consists of (a) a liquid filter L^M mapping input function u(·) to internal liquid state x^M(t) = (L^M u)(t), and (b) a memoryless readout map f^M producing y(t) = f^M(x^M(t)). The liquid is implemented as a recurrent circuit of integrate-and-fire neurons with biological time constants (~30ms membrane). The readout is a separate population of I&F neurons trained via a perceptron-like local learning rule.

**Our restatement:** `[ASSERTED]` — LSM differs from ESN primarily in (a) spiking vs rate-coded units, (b) continuous vs discrete time, (c) biological-plausibility commitment. The architectural shape (fixed substrate + trained readout) is identical.

### The framing is explicitly anti-attractor

**Paper (§1):** *"80% of the synapses within a functional neocortical column [are] multiple recurrent loops"* — defies attractor-based and Turing-machine-based models. *"Stable internal states are not required for giving a stable output, since transient internal states can be transformed by readout neurons into stable target outputs due to the high dimensionality of the dynamical system."*

**Our restatement:** `[ASSERTED]` — information lives in the *trajectory*, not the state. Direct relevance to M14 / Buzsáki preconfigured-vocabulary framing: both bet that the structure-and-trajectory pattern carries the computation, not the resting state. See [reservoir-computing](../open-question/reservoir-computing.md) "Off-line vs on-line angle".

### Separation Property (SP) and Approximation Property (AP)

**Paper (§2):** Two macroscopic properties together are sufficient for powerful real-time computing on perturbations. SP: different input streams must produce well-separated liquid trajectories (property of the liquid). AP: readouts must be able to distinguish and transform liquid states into target outputs (property of the readout). SP depends on liquid complexity; AP depends on readout adaptability.

**Our restatement:** `[ASSERTED]` — this factorisation matches the caddy commitment-split: commitment 1 (separately-addressable model state) ≈ a liquid that satisfies SP for the caddy's input space; commitment 5 (auxiliary objective beyond consumer task loss) ≈ a readout-training procedure that achieves AP for the caddy's target. See [caddy](../concept/caddy.md).

### Universal approximation theorem for fading-memory filters

**Paper (§4, Theorem 1 in Appendix A):** *"A mathematical theorem guarantees that LSMs have this universal computational power regardless of specific structure or implementation, provided that two abstract properties are met: the class of basis filters from which the liquid filters L^M are composed satisfies the pointwise separation property, and the class of functions from which the readout maps f^M are drawn satisfies the approximation property."* Universality holds for *any time-invariant filter with fading memory* on time-varying inputs.

**Our restatement:** `[ASSERTED]` — strong theoretical result, but bounded. Universality is for **fading-memory** filters, not arbitrary computations. Hard memory (recall specific past events months later — what an agent-memory caddy needs) falls *outside* the universality result. Important construct-validity caveat against any "LSMs are provably sufficient for memory" inference. See [reservoir-computing](../open-question/reservoir-computing.md) sub-question 5.

### Multiple readouts can share one liquid (parallel multitasking)

**Paper (§3, §5):** *"Multiple readout modules can be trained to perform different tasks on the same state trajectories of a recurrent neural circuit, thereby enabling parallel real-time computing."*

**Our restatement:** `[ASSERTED]` — interesting architectural property for caddy design. A single substrate could serve multiple downstream consumers via separate readouts, each trained for its own task, without interference between consumers. Relevant to caddy "memory-consumer-axis" question — same substrate, multiple consumer-axis cells served.

### Biological motivation is cortical microcircuits

**Paper (§1, §5):** The model is motivated by neocortical column observations — the recurrent loops, heterogeneity of neuron types, diversity of time constants, "loops within loops" structure. *"Neural microcircuits ... appear to be ideal liquids for computing on perturbations because of the large diversity of their elements."*

**Our restatement:** `[ASSERTED]` — the canonical biological precedent is **cortex** (and cerebellum via [yamazaki-tanaka-2007-cerebellum-lsm](./yamazaki-tanaka-2007-cerebellum-lsm.md)). Hippocampus is NOT in the original LSM biological-precedent set. Buzsáki's preconfigured-vocabulary framing for hippocampus would be an extension beyond what Maass et al. claimed.

## Important caveats

- The universal-approximation theorem applies to *time-invariant fading-memory filters*. It does not cover (a) long-term episodic recall, (b) goal-directed sequence generation, (c) catastrophic-interference avoidance — all of which a caddy needs.
- The paper precedes the engineering-vs-biology divergence. Subsequent work (Pascanu/Jaeger 2011, Sussillo/Abbott 2009, S4, Mamba) has shown that pure LSM-style readout-only training is insufficient for many tasks Maass et al. implied would be tractable.
- Spiking-vs-rate-coded is the most visible difference from ESN, but the architectural shape and limitations are nearly identical in practice.

## Relevance to Kyrja

Cited from:
- [open-question/reservoir-computing](../open-question/reservoir-computing.md) — anchor for LSM definition, separation/approximation properties, universal-approximation theorem (with fading-memory caveat), parallel-readouts property.
- [concept/catastrophic-interference](../concept/catastrophic-interference.md) — co-anchor (with [lukosevicius-jaeger-2009-rc-review](./lukosevicius-jaeger-2009-rc-review.md)) for the "Reservoir computing" row.

## Audit history

- 2026-05-17 — verbatim read of pages 1–10 by Nils (side-quest window) via Maass-group preprint PDF. Section/equation references checked against PDF page numbers (Neural Computation 14, 2531–2540 covers §1–§6 intro material).

## Archive location

Local PDF: [library/papers/maass-2002-lsm.pdf](../../../research/library/papers/maass-2002-lsm.pdf). Canonical preprint: <https://igi-web.tugraz.at/PDF/130.pdf>. Publisher: <https://direct.mit.edu/neco/article-abstract/14/11/2531/6650/>.
