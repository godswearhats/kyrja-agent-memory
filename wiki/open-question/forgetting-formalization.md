---
type: open-question
name: Theoretical formalization of optimal forgetting
status: OPEN
last_ingested: 2026-05-17
sources: []
epistemic_tags: [asserted]
tags: [forgetting, consolidation, theory-gap]
---

## The question

**What should an agent memory system forget, when, and how?**

Utility-based deletion (forget what stops getting retrieved) is promising — SimpleMem reports ~10% gains — but the field lacks a theoretical framework for *optimal* forgetting in the context of agent workflows. There's no equivalent to the catastrophic-forgetting / continual-learning literature for retrieval-based memory; the closest analog (cognitive-science forgetting models like MOOM) covers only one operational mechanism.

This is the **theory-shape** question. The operational hypotheses ([H34-forgetting-scores](../hypothesis/H34-forgetting-scores.md), [H36-consolidation-ordering](../hypothesis/H36-consolidation-ordering.md)) test specific implementations; this question asks what those implementations are *approximations of*.

## Why it matters

- **The field is operating on intuition.** MOOM's 9:1 access-to-recency ratio is empirical, not derived. SimpleMem's utility-deletion is heuristic, not principled. Without a framework, every system invents its own forgetting policy and they don't compose.
- **Tradeoffs are not characterized.** Forgetting trades off (a) storage cost, (b) retrieval-noise reduction, (c) information loss, (d) provenance fidelity. The right operating point in this 4-d space is workload-dependent; no theory tells us where to start.
- **Compliance forces a partial answer.** [f12-retention-wiring](./f12-retention-wiring.md) requires *mandatory* forgetting under retention floors (HIPAA, SOX, EU AI Act). A theoretical framework needs to accommodate the dual case where some forgetting is policy-driven and some is utility-driven.

## What evidence would resolve it

- **A formal framework** that defines (a) what makes a memory valuable, (b) how to estimate that value from observable signals (retrieval frequency, downstream task success, time decay), (c) what the cost of erroneous forgetting is, and (d) how those quantities trade off into a deletion policy.
- **Cross-system unification.** MOOM, SimpleMem, LightMem, A-MEM, and GAM all implement different forgetting mechanisms. A framework that recovers each as a special case under specific parameter choices would validate the framework.
- **Workload-conditional validation.** Coding workloads (where the *latest* fix-pattern is usually correct) likely want different forgetting than enterprise-knowledge workloads (where older facts may be more stable). The theory needs to bear out this conditioning.

> **Pattern-separation prerequisite (added 2026-05-17 M17 walk):** any formal framework for optimal forgetting must condition on the memory representation's pattern-separation property. Without pattern separation (orthogonal / sparse / LSH-separated keys), similar memories collide and *interference* is the dominant loss mechanism — and no per-memory utility score can be applied because there's no per-memory address that's stable under writes. The MOOM-style scoring and SimpleMem's utility-deletion both implicitly assume pattern-separated memories; that assumption is a separately-designed architectural property, not a given. See [pattern-separation](../concept/pattern-separation.md) for the prerequisite framing and [Hardt, Nader & Nadel 2013](../source/hardt-nader-nadel-2013-active-forgetting.md) for the cog-sci anchor that surfaced the distinction.

> **M17 anchor (added 2026-05-17):** the active-forgetting framing from [Hardt, Nader & Nadel 2013](../source/hardt-nader-nadel-2013-active-forgetting.md) provides cog-sci grounding this open question was missing. Their partition of forgetting into two mechanisms (interference vs decay) is a more principled starting point than treating forgetting as a single phenomenon. The "encode promiscuously, forget intelligently" architectural inversion is the load-bearing reframe — a theory of optimal forgetting that holds it equal in stature to admission control is consistent with current AI practice; one that holds it as *the* place intelligence lives is consistent with biology. The two are not the same theory.

## Related

- [H34-forgetting-scores](../hypothesis/H34-forgetting-scores.md) — MOOM-style operational implementation
- [H36-consolidation-ordering](../hypothesis/H36-consolidation-ordering.md) — depends on forgetting being formalized first
- [admission-control](../concept/admission-control.md) — the dual problem: admission decides what *enters*; forgetting decides what *leaves*. Theory should cover both.
- [pattern-separation](../concept/pattern-separation.md) — architectural prerequisite for graded decay; any formal forgetting framework must condition on this property
- [hardt-nader-nadel-2013-active-forgetting](../source/hardt-nader-nadel-2013-active-forgetting.md) — primary source for the interference-vs-decay partition; cog-sci anchor
- [matrix row M17](../concept/mechanism-gap-matrix.md) — active forgetting as the matrix's first inverse mechanism
- [catastrophic-interference](../concept/catastrophic-interference.md) — the failure mode the interference half describes
- [f12-retention-wiring](./f12-retention-wiring.md) — compliance-side forcing function
- [LightMem source](../source/lightmem-2510.md) — three-stage Atkinson-Shiffrin consolidation, closest published theory
- Deep-dive §11 Q20 origin: agentic-memory-scaling-deep-dive.md
