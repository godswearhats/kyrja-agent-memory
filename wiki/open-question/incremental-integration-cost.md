---
type: open-question
name: "Is integrating new knowledge into weights cheap enough to be memory, or is it training in disguise?"
status: OPEN
last_ingested: 2026-05-30
program: kerros
sources: [../experiment/2026-05-26-factored-operator-beachhead/scaling-and-memory-gates.md, ../concept/integration-gate.md, ../concept/consolidation-channel.md, ../source/xu-2026-agentic-memo.md]
epistemic_tags: [measured, speculated]
tags: [kerros, memory-vs-training, incremental-write, consolidation, efficiency-gate, viability]
---

## The question

The [integration gate](../concept/integration-gate.md) — instantiated as the [Xu Thm 1](../source/xu-2026-agentic-memo.md) fan-open — tests whether weights can *represent* a composition a frozen bolt-on cannot. Xu Thm 1 is a **sample-complexity** separation (in-context `Ω(k²)` vs parametric `O(d)`): it shows the parametric solution is compact and retrieval scales badly, but it does **not** address the **training/acquisition cost** of reaching that solution, nor whether a real model can write it incrementally and few-shot. But a *memory* function is defined by exactly that cost: it must absorb new knowledge **cheaply, locally, incrementally** — not by retraining the model. So the make-or-break viability question for Kerros-as-memory:

> Can a model already competent at a task integrate a *new* piece of knowledge via a cheap, local, few-shot weight write and still generalise — or does integration fundamentally require retraining-scale compute, in which case "weight-integration memory" is just **training in disguise** and the inert bolt-on is the right product?

This is the question AJ surfaced (2026-05-28): *"if the only way to learn something new is to spend huge amounts of training time chasing a loss function, then it's not really a memory function."* It is **distinct** from the consolidation-channel's "[which substrate-depth rung is cost-effective](../concept/consolidation-channel.md)" design question — this asks whether *any* cheap rung suffices at all, i.e. whether the approach qualifies as memory.

## 2026-05-30 update — toy decider PARKED; the question widens to a trade-off

`[SPECULATED]` (Nils/AJ strategy session, 2026-05-30. **Exploratory — not a committed direction;** AJ flagged not to overindex.) On reflection the projected-low-rank decider below has **low discriminating power**: we *built in* rank `m=4`, so a positive ("knee at r=4") is semi-rigged and a negative just says "escalate" — and the deeper reframe is that *weights* may be the wrong substrate to test cheap writes on at all. **Decider PARKED (reversible** — recover it if we later want to cleanly separate write-parametrisation from operator non-invertibility).

The question generalises. The two ways to give a model new knowledge map onto a possible **fundamental trade-off**:

- **Cheap, real-time writes already exist** — append a `(key, value)` to a non-parametric store ([kNN-LM](../source/khandelwal-2020-knn-lm.md), RETRO, Memorizing Transformer). One forward pass, no training.
- **But that is exactly the substrate [Xu Thm 1](../source/xu-2026-agentic-memo.md) says is *bad at composition*** (`Ω(k²)`). Good composition comes from the *parametric* substrate — which needs the slow, training-cost write.

So the sharpened open question:

> **Is there a write that is cheap/real-time AND lands in a substrate that keeps the compositional read advantage — or do cheap-write and compositional-read fundamentally pull against each other?**

If the trade-off is **fundamental** → real-time compositional memory is intractable (a clean negative for Kerros-as-memory; the bolt-on is correct). If **breakable** → that mechanism is the entire prize. Candidate real-time-parametric-write substrates worth surveying *before* any experiment: test-time training / [Titans](../source/behrouz-2024-titans.md)-style neural memory, fast weights, per-memory adapters (MEGa). Whether any preserves the fan-open is, as far as mapped, **unmeasured** — that is the crux.

**Load-bearing check before leaning on this:** confirm Xu's `Ω(k²)` bound bites *activation-blending* retrieval ([kNN-LM](../source/khandelwal-2020-knn-lm.md), which retrieves into the output distribution), not only *in-context/prompt* memory (the bolt-on control it was derived against). If activation-blended retrieval escapes the bound, cheap-write-plus-decent-composition may partly coexist already and the problem is less fundamental.

**Connected scoping thread:** even if tractable, the [wedge-sizing question](./thinks-with-wedge-sizing.md) asks whether the problems needing it are a big enough slice to matter.

## Why it matters

- **If cheap incremental write generalises:** Kerros has a real wedge over the bolt-on product — memory the *model* thinks with, written at memory cost, not training cost. The write-side ([consolidation-channel](../concept/consolidation-channel.md)) bet is alive, and the architectural finding (e.g. "memory = low-rank writes into a learned read-subspace") becomes a design target.
- **If only retraining-scale write generalises:** weight-integration ≈ training; for an *agent memory product* the bolt-on (inert, inspectable, cheap-to-write) is correct, and Kerros's contribution narrows to the existence claim (interesting, but not a memory mechanism). A clean, informative negative for the program.
- **Gates:** whether to keep building the integrated arm at all vs. ceding the memory-write role to retrieval; which rung of the [substrate-depth ladder](../concept/consolidation-channel.md) is even viable; how to read the [fan-open result](../experiment/2026-05-26-factored-operator-beachhead/scaling-and-memory-gates.md) (existence without cheap acquisition is half a result).

## What evidence would resolve it

`[MEASURED]` First evidence in, 2026-05-28 ([scaling-and-memory-gates § Gate 2](../experiment/2026-05-26-factored-operator-beachhead/scaling-and-memory-gates.md)): the **cheapest write fails**. Freezing a competent k=128 model and training only the new symbols' 896-d embedding rows reached at best 0.347 (few-shot at chance), with perfect retention. **Construct-validity:** the train-loss column is decisive — loss→0.003 with held-out at chance shows the write fit perfectly yet generalised at chance, so the failure is *generalisation*, not data; retention held *exactly* 0.500, confirming the freeze. Diagnosis: **underdetermined in parameter space** — data was information-sufficient (6 > m+1 constraints) but ~892 free embedding directions let it interpolate train without recovering the true vector.

**The decider `[PARKED 2026-05-30 — see update above]`:** a **projected low-rank write** — project the new rows onto the top-`r` PCA subspace of the frozen base embeddings (a "write head" learned once from the model, reused per symbol), `r`-sweep at fixed `N_new=64`.

**Adequate signal:** new held-out **rising as `r` → ~4** = cheap few-shot memory works *with the right write mechanism* → answer is "yes, it's memory (given a learned low-rank write subspace)." **Flat at chance across all `r`** → the operator isn't cheaply invertible → escalate (LoRA, then full-FT-continued); if those need retraining-scale, the answer is "training in disguise." The predicted outcomes differ by enough magnitude (≥0.40 vs ~0.20) that the single `r`-sweep is discriminating.

## Sub-questions

- Is the failure the **write parametrisation** (full-dim SGD, no prior) or a genuine **non-invertibility** of the frozen operator? (The low-rank decider separates these.)
- Does a learned low-rank **write subspace** generalise across *which* new symbol — i.e. is it a reusable "memory module," or must it be refit per write?
- How does write cost scale with `k` and with the *number* of new facts written before interference appears? (Retention was exact here only because the base was frozen.)
- Does the same cheap-write result hold on a **larger, already-competent base** (where the new fact is a small delta), or is the 0.5B-from-near-scratch regime pessimistic?

## Related

- [integration-gate](../concept/integration-gate.md) — Gate 1 (existence) vs Gate 2 (efficiency); this question is Gate 2 made durable.
- [consolidation-channel](../concept/consolidation-channel.md) — the write-side mechanism whose cost this question prices; the substrate-depth ladder is the menu of write rungs.
- [scaling-and-memory-gates](../experiment/2026-05-26-factored-operator-beachhead/scaling-and-memory-gates.md) — the experiment producing the evidence; the low-rank decider is the next run.
- [Xu, Dai & Zhang 2026](../source/xu-2026-agentic-memo.md) — Thm 1 establishes representability (Gate 1); this question is the acquisition cost the theorem does not address.
