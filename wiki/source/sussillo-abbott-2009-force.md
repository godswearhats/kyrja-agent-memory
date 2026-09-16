---
type: source
name: "Sussillo & Abbott 2009 — Generating Coherent Patterns of Activity from Chaotic Neural Networks"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [reservoir-computing, force-learning, p1, autonomous-generation, chaos-control, rls, edge-of-rc, caddy-load-bearing]
---

## Citation

Sussillo, D. & Abbott, L. F. (2009). *Generating Coherent Patterns of Activity from Chaotic Neural Networks.* Neuron 63(4), 544–557. DOI: 10.1016/j.neuron.2009.07.018.

## Location

- Publisher: <https://www.sciencedirect.com/science/article/pii/S0896627309005479>
- PMC open access: <https://pmc.ncbi.nlm.nih.gov/articles/PMC2756108/>
- Code (ModelDB): <https://modeldb.science/127967>

## Key claims (with our restatements)

### FORCE algorithm: keep error small throughout training, not just at convergence

**Paper (§Methods, Eqs. 4–5):** First-Order Reduced and Controlled Error (FORCE) uses a recursive least-squares (RLS) update rule with adaptive per-neuron learning rates, modulating updates by the inverse correlation structure of network activities (matrix P). *"Errors are always small, even from the beginning of the training process"* — the goal is not significant error reduction but reducing the amount of modification needed.

**Our restatement:** `[ASSERTED]` — FORCE is an *online* algorithm that abandons the textbook RC commitment to offline linear regression. The novelty is the joint solution to two problems: (a) chaos suppression during readout training, (b) feedback-loop stability.

### Echo-state clamping (textbook RC) fails on autonomous pattern generation

**Paper (Fig. 4):** Direct empirical demonstration. When training feedback is clamped to the target (the standard ESN approach), networks become **unstable** in roughly 50% of trials post-training. FORCE feedback (using actual error) converges reliably. A mixing parameter γ shows networks remain stable only at γ < 0.15 (γ=0 = pure FORCE; γ=1 = pure echo-state clamping).

**Our restatement:** `[MEASURED]` — **textbook RC's "train only the readout offline" commitment empirically fails for autonomous pattern generation**. Construct-validity note: this is specifically for autonomous-output tasks (no input drives the generation post-training); input-driven prediction tasks may still work with textbook ESN. The failure mode is task-class-specific, not universal.

### Architectural variants: 1A in-RC, 1B feedback-network, 1C inner-reservoir-trained

**Paper (Fig. 1A/B/C):** Three architectures explored. (1A) Only readout weights w trained; reservoir random fixed — still RC, but with online training. (1B) Feedback network synapses J_FG trained too — semi-RC. (1C) **Inner reservoir synapses J_GG trained directly** — abandons the fixed-reservoir commitment.

**Our restatement:** `[ASSERTED]` — second example from inside the RC community (alongside [pascanu-jaeger-2011-wm](./pascanu-jaeger-2011-wm.md)) where solving hard tasks required *training parts of what RC's textbook says should be fixed*. Architectures 1A–1B remain RC-territory; 1C is a hybrid that retains chaotic-initialisation philosophy but explicitly trains reservoir weights.

### Tasks solved: motor capture, 4-bit memory, autonomous switching

**Paper (Figs. 7, 8):** A 5000-neuron FORCE network generates human running *and* walking from motion-capture data (95 joint angles, switching via input). 4-bit memory with crosstalk rejection. Five-pattern autonomous switching. *"For any given target function ... there is an upper limit for g [chaos parameter] beyond which chaos cannot be suppressed by FORCE learning."*

**Our restatement:** `[MEASURED]` — concrete tasks FORCE solves that pure ESN cannot. Construct-validity note: motor-pattern generation is a *continuous-dynamics* task; the 4-bit memory is a *small symbolic* task. Neither approximates caddy-scale episodic recall, but both demonstrate the architectural extension is empirically necessary.

### Chaos is helpful, not just tolerable

**Paper (Fig. 5):** Chaotic networks (g > 1) train **faster**, **more accurately**, and with **smaller weight magnitudes** than damped networks (g < 1). FORCE actively suppresses the chaos during training; the resulting fixed point is *near* the chaotic regime, not damped into it.

**Our restatement:** `[ASSERTED]` — empirical case for operating *near* the edge of chaos, with active suppression during learning. Conceptually aligned with [pathak-2018-chaotic-prediction](./pathak-2018-chaotic-prediction.md)'s tuning (ρ=0.6, close to but below the unit-spectral-radius boundary). The Mamba-era reframe: chaos is a feature when controlled, a bug when not.

### Biological prediction: plasticity in multiple areas, coupled by a common error signal

**Paper (Discussion):** *"Plasticity in multiple areas (at least two, in these examples) coupled by a common error signal is a basic prediction of the model."* The error signal is hypothesised to be computed by an internal model (cerebellum candidate). Pre-movement variability drop replicates Churchland et al. 2006 observations.

**Our restatement:** `[ASSERTED]` — relevant to caddy commitment 5 (auxiliary objective): if a caddy adopts FORCE-shape training, the auxiliary objective must compute an error signal jointly across the substrate and the readout. This is a non-trivial system-design constraint not addressed in the open-question doc.

## Important caveats

- FORCE requires plasticity that acts *faster* than typical long-term potentiation timescales. *"A challenge raised by this work to uncover how such rapid plasticity can be realized biologically."* The mechanism is biologically motivated but not biologically grounded.
- The RLS update is computationally non-trivial: matrix P updates scale as O(N²) per timestep. Scaling to very large reservoirs has not been demonstrated.
- Architecture 1C explicitly violates the "fixed substrate" commitment. Calling FORCE "reservoir computing" is a matter of definition; the architecturally faithful subset is 1A only.
- The motor-capture and 4-bit memory tasks are far smaller than caddy-relevant memory tasks. Scaling argument is not made.

## Relevance to Kyrja

Cited from:
- [open-question/reservoir-computing](../open-question/reservoir-computing.md) — **primary evidence for Sketch A failure** on autonomous generation; co-anchor for "RC needs extension for hard tasks" with [pascanu-jaeger-2011-wm](./pascanu-jaeger-2011-wm.md).
- [concept/catastrophic-interference](../concept/catastrophic-interference.md) — supplementary anchor for "Reservoir computing" row.

## Audit history

- 2026-05-17 — read by Nils via structured extraction from PMC HTML version (full article). Equations and figure references cross-checked.

## Archive location

PMC open-access HTML: <https://pmc.ncbi.nlm.nih.gov/articles/PMC2756108/>. ModelDB code: <https://modeldb.science/127967>. PDF not downloaded; PMC HTML is the canonical open-access form.
