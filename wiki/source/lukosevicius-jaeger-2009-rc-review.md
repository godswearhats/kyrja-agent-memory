---
type: source
name: "Lukoševičius & Jaeger 2009 — Reservoir computing approaches to recurrent neural network training"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [reservoir-computing, echo-state-networks, liquid-state-machines, foundational, p0, review, edge-of-chaos, memory-capacity]
---

## Citation

Lukoševičius, M. & Jaeger, H. (2009). *Reservoir computing approaches to recurrent neural network training.* Computer Science Review 3(3), 127–149. DOI: 10.1016/j.cosrev.2009.03.005.

## Location

- Canonical PDF: <https://www.ai.rug.nl/minds/uploads/2261_LukoseviciusJaeger09.pdf>
- Publisher (paywalled): <https://www.sciencedirect.com/science/article/abs/pii/S1574013709000173>
- Local archive: [library/papers/lukosevicius-jaeger-2009-rc-review.pdf](../../../research/library/papers/lukosevicius-jaeger-2009-rc-review.pdf)

## Key claims (with our restatements)

### Reservoir computing = fixed random recurrent substrate + trained readout

**Paper (§3.1–3.2):** ESNs and LSMs both commit to a fixed, randomly-initialised reservoir; only the readout weights are trained, typically via linear regression. ESN uses discrete-time tanh units; LSM uses continuous-time integrate-and-fire spiking neurons.

**Our restatement:** `[ASSERTED]` — this is the canonical RC commitment as the field defined it through 2009. Both Sketch A in [reservoir-computing](../open-question/reservoir-computing.md) and the [catastrophic-interference](../concept/catastrophic-interference.md) "reservoir computing" row in the four-and-a-half table refer to this commitment as their baseline.

### Echo state property — the spectral-radius condition is folklore

**Paper (§3.1):** The echo state property (ESP) ensures the reservoir state asymptotically forgets its initial conditions. *"The ESP is usually ensured when the spectral radius of the reservoir weight matrix W is set to a value below unity, but we emphasize that this is neither a necessary nor a sufficient criterium (Jaeger, 2007), in spite of a folklore belief in the field that it is both."*

**Our restatement:** `[ASSERTED]` — important schema-correction for any wiki claim that uses "spectral radius < 1" as load-bearing. The empirical sweet spot ρ ≈ 0.9 is engineering practice, not theory. Buehner & Young 2006 gave refined algebraic conditions.

### Memory capacity is linear in reservoir size

**Paper (§8 context):** Jaeger's memory capacity measure: C ≈ Nλ/(1−λ) under stated assumptions. Capacity is bounded by reservoir dimension N and modulated by spectral radius λ.

**Our restatement:** `[ASSERTED]` — sets a hard upper bound on what a pure-RC substrate can hold. A 10⁶-neuron reservoir at ρ=0.9 holds ~10⁷ time-step-equivalents of input history. Relevant capacity-ceiling argument for Sketch A in [reservoir-computing](../open-question/reservoir-computing.md) and any caddy substrate sized via RC principles.

### Training: closed-form Tikhonov-regularised linear regression

**Paper (§8.1.1):** W_out = T M^T (M M^T + βI)^(−1), with β > 0 the regularisation strength. Closed-form, single-pass, no iteration.

**Our restatement:** `[ASSERTED]` — the practical advantage that motivates RC. Training cost is O(N²·T + N³) for one matrix solve, with no gradient steps.

### Edge-of-chaos is empirically real but theoretically unproven

**Paper (§3 / §9 Discussion):** Optimal performance clusters around ρ ∈ [0.8, 0.95]. The "computation at the edge of chaos" claim has empirical support but remains an open theoretical question. Cited but not resolved.

**Our restatement:** `[CONTESTED]` — the field uses edge-of-chaos as a tuning heuristic without a load-bearing theory under it. Pathak 2018 used ρ=0.6 successfully on chaotic-PDE prediction; Pascanu & Jaeger 2011 used ρ=0.5 for working memory. Task-dependent in practice.

### Biological connection: cerebellum-as-LSM, cortex-as-microcircuit (cited, not original)

**Paper (§3.2):** LSM design was inspired by cerebellar architecture (random Purkinje connections + structured readout) and by cortical microcircuit observations. Whether cortex *uses* reservoir-computing principles is "unknown but plausible."

**Our restatement:** `[ASSERTED]` — the biological precedent is cerebellum (modelled as a reservoir since Marr 1969 / Albus 1971; formalised in [yamazaki-tanaka-2007-cerebellum-lsm](./yamazaki-tanaka-2007-cerebellum-lsm.md)). Cortex is hypothesised; hippocampus is *not* in the standard RC biological-precedent set. Important caveat against the M14 [buzsaki-2015-spw-r](./buzsaki-2015-spw-r.md) → RC analogy in [reservoir-computing](../open-question/reservoir-computing.md): the cerebellar template is feedforward, not recurrent.

### Open problem: RC for sequence generation

**Paper (§9):** *"RC strongest on prediction where fading memory is natural. True sequence generation (without teacher forcing) underdeveloped; open challenge."*

**Our restatement:** `[ASSERTED]` — directly relevant to the M14 joint-replay / sequence-stitching question. RC's strength is prediction over short-fading-memory windows; sequence-generation is acknowledged as an open frontier. Subsequently addressed (incompletely) by Sussillo & Abbott 2009 FORCE and Pascanu & Jaeger 2011.

## Important caveats

- The review is dated; it predates S4 (2022), Mamba (2023), and the modern SSM lineage that descends from RC's mathematical framework. The genealogy section (§3.6 "Other exotic types") doesn't include those.
- "Memory capacity" in the paper means *fading-memory-window* capacity, not the long-term-storage capacity a caddy substrate would need. Construct-validity caveat against treating C ≈ Nλ/(1−λ) as a caddy storage bound directly.
- The review is by RC partisans (both authors are RC founders). Independent assessments of where RC sits in the broader ML landscape are sparser.

## Relevance to Kyrja

Cited from:
- [open-question/reservoir-computing](../open-question/reservoir-computing.md) — primary anchor for ESN/LSM definitions, ESP-folklore caveat, memory-capacity bound, edge-of-chaos contested status, sequence-generation open problem.
- [concept/catastrophic-interference](../concept/catastrophic-interference.md) — anchor for the "Reservoir computing" row in the four-and-a-half solution table.

## Audit history

- 2026-05-17 — verbatim read by Nils (side-quest window) via canonical MINDS PDF. WebFetch extraction with structured prompt; cross-validated section numbers and key claim wordings against the PDF outline. Full extraction archived in session transcript.

## Archive location

Local PDF: [library/papers/lukosevicius-jaeger-2009-rc-review.pdf](../../../research/library/papers/lukosevicius-jaeger-2009-rc-review.pdf). Canonical source: <https://www.ai.rug.nl/minds/uploads/2261_LukoseviciusJaeger09.pdf>.
