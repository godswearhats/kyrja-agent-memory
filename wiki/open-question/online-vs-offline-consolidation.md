---
type: open-question
name: Online vs offline consolidation for Kyrja's consolidation channel
status: OPEN
last_ingested: 2026-05-14
sources: [../source/behrouz-2026-nested-learning.md, ../source/xu-2026-agentic-memo.md, ../source/yu-2026-evosc.md, ../source/behrouz-2024-titans.md, ../source/yang-et-al-2024-selection-of-experience.md, ../source/mcclelland-mcnaughton-oreilly-1995-cls.md, ../source/josselyn-tonegawa-2020-engrams.md]
epistemic_tags: [speculated]
tags: [consolidation, consolidation-channel, cls, online-vs-offline, design-fork, wedge-relevant]
---

## The question

Biological [Complementary Learning Systems](../concept/complementary-learning-systems.md) ([McClelland 1995](../source/mcclelland-mcnaughton-oreilly-1995-cls.md)) implement *two* consolidation processes (Frey & Morris 1997; [Yang et al. 2024](../source/yang-et-al-2024-selection-of-experience.md)): **(1)** *online / synaptic* — fast, gradient-coupled, happens during encoding; and **(2)** *offline / systems* — slow, replay-driven, happens during sharp-wave ripples (SWRs) or sleep, with **active selection** of which traces to replay.

The agentic-memory substrate literature has split along this fork:

- **[Behrouz et al. 2026 (Nested Learning / Hope)](../source/behrouz-2026-nested-learning.md)** explicitly addresses stage 1 only. Verbatim §1.1: *"in this work, we focus on the first stage: memory consolidation as an online process."* Hope's consolidation is gradient-coupled to inference; no separate replay phase, no curated trace selection.
- **[Xu et al. 2026](../source/xu-2026-agentic-memo.md)** cites Skill-SD (Wang 2026) as the closest implemented mechanism — distillation of trajectories into student weights — which is *offline* in shape (batched, scheduled) but does not implement biological-style selective replay.
- **[EvoSC](../source/yu-2026-evosc.md)** is online distillation (per-task soft-prompt update from many-shot teacher) but at frozen-base / depth-2.
- **Biological replay** (Yang et al. 2024, Foster & Wilson 2006) is *offline + selective*: SWR-mediated reactivation, prioritised by surprise / reward / novelty.

**The question Kyrja must answer for Phase 3:** which consolidation regime does the personal-assistant wedge use — online gradient-coupled (Hope shape), offline batched distillation (Skill-SD shape), or biological-style selective replay (no existing implementation, closest to Yang 2024)?

This is a load-bearing design fork, not a tuning knob. The three regimes have categorically different operational profiles (latency, compute budget, selectivity, reversibility) and demand different infrastructure.

## Why it matters

- **If online gradient-coupled (Hope shape):** Consolidation happens during inference; no separate batch job. Plugs into the [active-stages framework](../concept/active-stages-framework.md) curation stage by making the update rule itself learnable. Compute cost is per-token, latency-sensitive. Falls within the substrate-depth ladder rung 2-3 (transient) or rung 4 with persistence wiring. Curation reduces to *implicit weighting in the forward pass* — there is no separate "what to write" decision.
- **If offline batched distillation (Skill-SD shape):** Consolidation runs as a scheduled background job on logged trajectories. Decouples inference latency from consolidation cost. Maps onto the [active-stages framework](../concept/active-stages-framework.md)'s temporal-credit-assignment story cleanly (delayed reward, batch reconciliation). Falls at substrate-depth ladder rung 5 (full FT) or rung 4 (targeted edit). Demands a curation policy because the batch job must decide what to consolidate.
- **If selective-replay (biological shape):** Consolidation happens during "rest periods" (idle compute, end-of-session, scheduled maintenance) with *active selection* of which traces to replay — driven by surprise, reward, or recency. Closest match to McClelland 1995 CLS. **No existing system implements this in the substrate-memory literature.** Engineering surface is largest; differentiator potential is also largest.

**Decisions this question gates:**

- [H36-consolidation-ordering](../hypothesis/H36-consolidation-ordering.md) — the forget-first-vs-consolidate-first question presupposes a consolidation regime. Different regimes order differently.
- [active-stages-framework](../concept/active-stages-framework.md) per-stage training-signal taxonomy — RLVR-with-delayed-reward fits offline; per-token weighted update fits online; selective-replay needs a separate signal architecture.
- Phase 3 architecture sketch — substrate-depth choice and frequency choice are entangled with the online/offline choice.
- Storage requirements — offline / selective-replay need a *durable trajectory log*; online does not.

## What evidence would resolve it

The question is too design-laden to be settled by a single benchmark — it is a fork that demands committed architectural exploration. Three feasible paths:

1. **Build minimal online-only consolidation in the MTP** (lowest cost). Wire a Titans-style surprise-driven gradient update into the personal-assistant loop. Measure whether the resulting cross-session continuity is "good enough" for the wedge. If yes, the question collapses for now; if no, escalate.
2. **Build minimal offline-only consolidation** (medium cost). Distil end-of-session trajectories into a small LoRA delta via a Skill-SD-style pipeline. Measure same-session and across-session retention. Compare to online baseline.
3. **Build selective-replay consolidation** (highest cost, largest differentiator). Requires a surprise-/reward-/novelty-based prioritisation policy plus a replay scheduler. No existing implementation to learn from; build cost is months, not weeks.

**Adequate signal:** A single concrete user trajectory of ≥10 sessions where the online and offline regimes produce *qualitatively different* outcomes (one remembers the consolidated abstraction, the other doesn't) is enough to commit. Quantitative gap need not be large — what matters is whether the *shape* of behaviour differs.

## Sub-questions

- **Trigger.** What triggers offline consolidation in regime 2 or 3 — end of session, idle compute, capacity threshold, scheduled cron, or surprise accumulation?
- **Selectivity policy for regime 3.** What surrogate for SWR-style prioritisation does Kyrja use? Surprise (Titans-style gradient norm)? Reward (downstream task success)? Recency × frequency? Combinations?
- **Reversibility.** Can offline / selective-replay updates be rolled back if they produce harmful weights? Online updates that don't persist are trivially reversible; persistent updates need a story.
- **Multi-tenant interaction.** If the user has multiple devices / agents, who runs consolidation, and when does the consolidated weight propagate?
- **Empirical resolution mechanism for the Yang 2024 SWR claim itself.** The neuroscientific evidence for selective-replay being the *correct* model is itself contested in 2025-2026 literature (engram studies, distributed-circuit framing — see [Behrouz et al. 2026 §1.1](../source/behrouz-2026-nested-learning.md) refs to Christophel 2017, Kitamura 2017, Roy 2022). Kyrja should not over-anchor on Yang 2024 without acknowledging the active debate.

## Related

- [consolidation-channel](../concept/consolidation-channel.md) — the operator this question is *about*
- [active-stages-framework](../concept/active-stages-framework.md) — temporal-credit-assignment story differs across regimes
- [mechanism-gap-matrix](../concept/mechanism-gap-matrix.md) — the three regimes correspond to rows M03 (consolidation operator) and M04 (selective replay); selectivity is the gap most decisively unfilled across all three
- [H40 — schema-fit-modulated consolidation](../hypothesis/H40-schema-fit-modulated-consolidation.md) — rate modulation is orthogonal to the online/offline axis but interacts with regime choice (high-fit info may favor online; low-fit may favor offline with more evidence)
- [substrate-as-memory](../concept/substrate-as-memory.md) — paradigm-level frame
- [H36-consolidation-ordering](../hypothesis/H36-consolidation-ordering.md) — sibling design question (forget-first vs consolidate-first); presupposes a consolidation regime
- [rl-target-encoding-vs-consolidation](./rl-target-encoding-vs-consolidation.md) — sibling question on RL budget allocation; the regime choice shapes where the RL spend lands
- [Behrouz et al. 2026](../source/behrouz-2026-nested-learning.md) — names the stage-1-only restriction explicitly
- [Xu et al. 2026](../source/xu-2026-agentic-memo.md) — names the consolidation channel, cites Skill-SD (offline) and Titans (online) as the two existing mechanism families
- [EvoSC](../source/yu-2026-evosc.md) — online distillation, depth-2

## Origin

Surfaced 2026-05-14 during the verbatim read of [Behrouz et al. 2026 Nested Learning](../source/behrouz-2026-nested-learning.md). The paper's §1.1 explicit demarcation of stage-1-only consolidation forced an articulation of the offline branch as a separate design path. Pre-2026-05-14 the consolidation-channel page treated "online vs offline" as a single dimension among many (trigger / representation / depth); the Hope read elevated it to a load-bearing fork that determines the rest of the design.
