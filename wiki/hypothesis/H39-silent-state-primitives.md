---
type: hypothesis
name: H39 — Silent-state primitives in agent memory yield measurable utility over delete-or-keep
status: PROPOSED
last_ingested: 2026-05-14
sources: [../source/josselyn-tonegawa-2020-engrams.md, ../concept/silent-engrams.md, ../concept/mechanism-gap-matrix.md]
epistemic_tags: [speculated]
tags: [silent-engrams, ai-translation, memory-eviction, three-state-memory, cog-sci-derived]
---

## Claim

**Agent memory systems that implement explicit silent-state primitives** — i.e., a three-state design (available / silent / absent) where silent items are preserved in storage but excluded from natural-cue retrieval, reactivatable only by direct operator-mediated invocation — **outperform two-state systems (delete-or-keep) on workloads with cross-session continuity requirements and bounded retrieval budgets.**

The biological precedent is the silent-engram phenomenon ([Josselyn & Tonegawa 2020](../source/josselyn-tonegawa-2020-engrams.md), [silent-engrams concept](../concept/silent-engrams.md)). Translation to AI is `[SPECULATED]` until empirically tested.

## What would falsify it

A controlled benchmark comparison where:

- **System A** implements two-state memory: items are either in the active retrieval index (available) or evicted (absent). Eviction policy: any reasonable baseline (LRU, age, importance score).
- **System B** implements three-state memory: items can be available, silent (preserved in cold storage, not in active index, reactivatable via explicit reference), or absent. Demotion policy: any reasonable baseline matched to System A's eviction policy.
- **Workload**: cross-session agent tasks with bounded retrieval budgets, including some queries that would benefit from reactivating previously demoted info (e.g., "remember when we talked about X" where X was demoted but later relevant).

H39 is **REJECTED** if:
- Under matched compute and retrieval budgets, System B shows no significant utility difference from System A across multiple workloads, OR
- System B shows utility difference only on workloads engineered to favor it (i.e., the difference doesn't generalize to plausible real-world agent tasks), OR
- The silent-state reactivation operator is so rarely invoked that the storage cost outweighs the retrieval benefit.

H39 is **SUPPORTED** (not proven) if:
- Significant utility difference on multiple natural workloads, with reactivation invoked frequently enough to amortize storage cost, AND
- Difference replicates across different demotion policies (so the win comes from the *three-state architecture*, not from a clever policy that could be applied to System A).

H39 is **partially supported** if the win appears for specific workloads (e.g., long-running personal assistant) but not others (e.g., short-session tool-use agents). The scope of the win then becomes the result.

## Evidence for

`[ASSERTED]` Biological precedent — [silent engrams](../concept/silent-engrams.md) demonstrate that storage and retrievability are dissociable at the substrate level. Multiple labs, multiple paradigms, converging evidence ([Josselyn & Tonegawa 2020](../source/josselyn-tonegawa-2020-engrams.md) review).

`[ASSERTED]` Conceptual gap in current AI memory ([mechanism-gap-matrix](../concept/mechanism-gap-matrix.md) row M06): no current agent-memory system (Mem0, Letta, Zep, Cognee, LightMem, Hope, EvoSC, Skill-SD) implements three-state memory. The eviction-vs-keep binary is universal.

`[SPECULATED]` Mechanistic plausibility: at least four AI architectures naturally support silent-state implementations — disabled LoRA adapters, embedding-removed-content-preserved stores, hash-only cold archives, attention-masked-knowledge configurations. None is exotic.

`[SPECULATED]` The Kitamura et al. 2017 evidence on systems-consolidation-via-silencing (cited in Josselyn 2020) suggests that **migration between memory substrates passes through silent states** in biology. This implies silent states are not just a passive storage tier but an active mechanism for memory reorganization — an analog AI feature would be useful for cross-substrate memory transfer (e.g., demoting vector-store items as they consolidate into adapter weights).

## Evidence against

`[SPECULATED]` (No empirical evidence against yet — the hypothesis is novel.)

Anticipated objections:

- **"Silent state is just LRU under a different name."** Distinction: LRU is policy (when to evict); silent-state is architecture (three-state vs two-state). LRU determines *what* to demote; silent-state determines *what 'demote' means*. Composable but distinct.
- **"Cold storage exists in production already."** Distinction: existing cold-tier systems require explicit migration steps and are typically read-cold (high latency to retrieve). Silent-state primitives are first-class architecturally — reactivation is a normal operator, not an ops procedure.
- **"The biological analogy is too far."** Acknowledged risk. The hypothesis is `[SPECULATED]` precisely because cog-sci → AI translations have a poor track record at the mechanism level. The falsifier is designed to test the *AI claim* empirically, independent of the biological analogy.

## Open sub-questions

- **What is the operational definition of "silent" in an AI system?** Multiple candidates: embedding removed, retrieval index entry removed, attention masked, adapter disabled, hash-only archived. Each tests differently. Sub-question candidate for promotion to an open-question page.
- **What's the right demotion policy?** Independent of three-state architecture. The hypothesis tests *architecture*, not *policy*. Future work could decompose.
- **What's the right reactivation operator?** Direct ID-based lookup, schema-fit-based reactivation (linking to [H40](./H40-schema-fit-modulated-consolidation.md)), agent-triggered explicit recall? Multiple plausible operators.
- **Does silent-state interact with consolidation?** The Kitamura evidence suggests yes; an AI test might benefit from running silent-state and consolidation experiments jointly rather than independently.
- **What's the right benchmark?** Existing agent-memory benchmarks don't have demotion/reactivation-friendly workloads. May need a new benchmark — sub-question for the team.
- **Latency budget for reactivation?** A silent-state architecture is only viable if reactivation is fast enough for inline use. Storage tier choices (RAM-cold vs SSD-cold vs object-storage-cold) bound this.

## Origin

`[ASSERTED]` Surfaced 2026-05-14 during the cog-sci primary-source sweep ([log](../log.md)), specifically the verbatim read of [Josselyn & Tonegawa 2020](../source/josselyn-tonegawa-2020-engrams.md). The silent-engram concept was flagged in `MORNING.md` as the most novel concept from the sweep. AJ approved promotion to a hypothesis on 2026-05-15.

## Related

- [silent-engrams concept](../concept/silent-engrams.md) — the biological grounding.
- [mechanism-gap-matrix](../concept/mechanism-gap-matrix.md) — M06 is the row this hypothesis derives from.
- [Josselyn & Tonegawa 2020 source](../source/josselyn-tonegawa-2020-engrams.md) — primary source.
- [H34 — forgetting-scores](./H34-forgetting-scores.md) — sibling hypothesis on what to evict; H39 modifies the action space (evict vs silence vs keep), H34 modifies the policy (which items get what action).
- [consolidation-channel](../concept/consolidation-channel.md) — silent-state transitions may be the substrate of cross-tier consolidation.
- [active-stages-framework](../concept/active-stages-framework.md) — silencing is a biologically-precedented mechanism for the "controlled forgetting" active stage; distinct from age-based eviction.
- [H40 — schema-fit-modulated consolidation](./H40-schema-fit-modulated-consolidation.md) — sibling hypothesis from the same sweep; could combine (silent-state demotion triggered by low schema-fit at retrieval time).
