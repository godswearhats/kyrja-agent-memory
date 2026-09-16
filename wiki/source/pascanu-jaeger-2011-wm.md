---
type: source
name: "Pascanu & Jaeger 2011 — A Neurodynamical Model for Working Memory"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [reservoir-computing, working-memory, p1, esn-extension, wm-units, gamma-attractors, m14-relevant, caddy-load-bearing]
---

## Citation

Pascanu, R. & Jaeger, H. (2011). *A Neurodynamical Model for Working Memory.* Neural Networks 24(2), 199–207. DOI: 10.1016/j.neunet.2010.10.003.

## Location

- Publisher: <https://www.sciencedirect.com/science/article/abs/pii/S0893608010001899>
- MINDS group preprint: <https://www.ai.rug.nl/minds/uploads/2321_PascanuJaeger10.pdf>
- Local archive: [library/papers/pascanu-jaeger-2011-wm.pdf](../../../research/library/papers/pascanu-jaeger-2011-wm.pdf)

## Key claims (with our restatements)

### Textbook ESN is insufficient for true working memory — WM-units extension required

**Paper (§3.1, Eqs. 5–7):** Standard ESN extended with a set of binary-state "WM-units" m(t) with sharp-threshold activation. WM-units have **trainable** input weights W^mem and **trainable feedback** weights W^b into the reservoir. Reservoir update: x(n+1) = f(W^in·u + W·x + W^b·m). The architecture is **no longer "fixed reservoir + linear readout"** — the WM-units feedback path makes them part of the recurrent dynamics, with trainable couplings between m and x.

**Our restatement:** `[ASSERTED]` — **load-bearing for the caddy decision**. The architects of RC themselves found that pure ESN was insufficient for memory tasks that require persistence beyond the fading-memory regime. Their extension *trains feedback weights into the reservoir*, which is outside the textbook RC commitment. Direct evidence against Sketch A (pure RC as caddy substrate) in [reservoir-computing](../open-question/reservoir-computing.md).

### Task: bracket-nesting counter on noisy graphical input

**Paper (§3.2):** Input is a 12-pixel-wide vertical line per timestep — rendered text in salt-and-pepper noise — over 65 ASCII characters plus curly brackets. The network must (a) count the number of opened curly brackets (up to nesting depth 6), and (b) predict the next character. Memory horizon: training data has switching period mean ~17 timesteps; **test data switching period mean ~96.8 timesteps, range up to 691** — far beyond standard ESN fading-memory capacity.

**Our restatement:** `[MEASURED]` — demonstrates that a hand-engineered RC extension *can* handle memory horizons of hundreds of timesteps. Construct-validity note: the task is small-vocabulary symbolic counting, not the rich-content episodic recall a caddy needs. Scale-up to caddy-relevant tasks is not addressed.

### Reservoir uses ρ = 0.5, well below textbook 0.9

**Paper (§3.2 Architecture detail):** Reservoir size 1200 units, sparsity 80%, spectral radius **0.5**, tanh activation. *"These values are a compromise between the requirements of the different subprocesses that go on simultaneously in the network."*

**Our restatement:** `[ASSERTED]` — second empirical confirmation (alongside [pathak-2018-chaotic-prediction](./pathak-2018-chaotic-prediction.md)'s ρ=0.6) that the textbook ρ ≈ 0.9 is task-dependent folklore, not a universal commitment. Memory tasks may want *lower* spectral radius than prediction tasks.

### Echo state property condition is folklore — important caveat

**Paper (§2):** *"The ESP is usually ensured when the spectral radius of the reservoir weight matrix W is set to a value below unity, but we emphasize that this is neither a necessary nor a sufficient criterium (Jaeger, 2007), in spite of a folklore belief in the field that it is both."*

**Our restatement:** `[ASSERTED]` — direct second-source confirmation of the [lukosevicius-jaeger-2009-rc-review](./lukosevicius-jaeger-2009-rc-review.md) caveat, from the same author cluster, two years later. Important to surface in any wiki claim that uses "spectral radius < 1" as load-bearing.

### γ-attractors: formal framework for input-driven attractor states

**Paper (§4):** Introduces a formal definition of "input-induced attractors" (γ-attractors), generalising the standard autonomous-system attractor concept to input-driven systems. Each stored memory item corresponds to a partial attractor that locks one or more reservoir neurons into a specific state while the rest of the dynamics continues to process input.

**Our restatement:** `[ASSERTED]` — useful conceptual framework, though mathematical detail not deeply applicable to caddy design directly. Notable for the **partial-attractor** idea: a memory item doesn't trap the whole network in an attractor, only a subset, leaving the rest available for ongoing processing. Echoes [silent-engrams](../concept/silent-engrams.md) — much of the network state is doing work the readout doesn't see.

### Sussillo & Abbott 2009 cited as the other "RC-extension" reference point

**Paper (§3 final paragraph):** *"A similarly switchable system was recently obtained ... in ESNs by a novel RC training algorithm which may operate simultaneously on the reservoir and the readout, and which has unprecedented stability properties (Sussillo and Abbott, 2009)."*

**Our restatement:** `[ASSERTED]` — anchors the cross-reference between Pascanu/Jaeger 2011 and [sussillo-abbott-2009-force](./sussillo-abbott-2009-force.md) as the two canonical "textbook RC isn't enough; here's the extension" papers from inside the RC community.

## Important caveats

- The bracket-nesting task is *small* (depth 6, 65-character vocabulary). It is not a stress test of caddy-scale memory.
- The WM-units mechanism is hand-engineered for *this* task. Whether a similar extension generalises to caddy-relevant tasks (rich content, multi-modal, open-ended) is unestablished.
- The two-stage training procedure (Stage 1: train W^mem; Stage 2: train W^out) requires per-task instrumentation and teacher-forced targets for the WM-units. This is a non-trivial engineering burden the paper doesn't fully address.

## Relevance to Kyrja

Cited from:
- [open-question/reservoir-computing](../open-question/reservoir-computing.md) — **primary evidence for Sketch A failure**; co-anchor for "ESP is folklore" caveat; load-bearing for the caddy-decision implication.
- [concept/catastrophic-interference](../concept/catastrophic-interference.md) — secondary anchor for the "Reservoir computing" row (RC extensions used for memory tasks).
- [open-question/memory-caddy](../open-question/memory-caddy.md) — direct relevance to caddy commitment 1 (separately-addressable model state) and commitment 5 (auxiliary objective).

## Audit history

- 2026-05-17 — verbatim read of pages 1–9 of preprint by Nils (side-quest window). Equations 5–7 and §3.2 architecture details cross-checked against PDF.

## Archive location

Local PDF: [library/papers/pascanu-jaeger-2011-wm.pdf](../../../research/library/papers/pascanu-jaeger-2011-wm.pdf). Canonical preprint: <https://www.ai.rug.nl/minds/uploads/2321_PascanuJaeger10.pdf>.
