---
type: concept
name: Discrete-unit memory architecture — the family of memory systems that operate on identifiable units with separate stores and explicit consolidation events
status: living
last_ingested: 2026-05-19
sources: [../source/josselyn-tonegawa-2020-engrams.md, ../source/mcclelland-mcnaughton-oreilly-1995-cls.md, ../source/yang-et-al-2024-selection-of-experience.md, ../source/tse-et-al-2007-schemas.md]
epistemic_tags: [asserted, speculated]
tags: [architecture-family, path-decision, memory-architecture, patents-as-precedent, consumer-axis, aj-originated]
---

## Definition

`[ASSERTED]` The **discrete-unit memory architecture** is the family of memory systems characterised by three structural properties:

1. **Discrete identifiable units of memory.** Each memory event has an addressable identity — a tag, a key, a snapshot ID, an engram tag. Memories are countable and trackable, not aggregated into a single continuous state.
2. **Separate addressable store.** Memory persistence lives in a substrate that is queryable independent of the inference/processing pipeline. Hippocampus vs cortex; vector DB vs LLM weights; a memory model's internal store vs a primary LLM.
3. **Consolidation operation with an explicit success/failure signal.** A discrete event marks "this memory has been integrated into the slow store." Biologically, cortical retrieval-pathway maturation. Engineering-wise, an acknowledgement / persistence-success signal.

The family is defined by membership in this three-property set, not by a specific path or implementation. Both [bolt-on memory](./substrate-as-memory.md) and the [caddy](../open-question/memory-caddy.md) are members. So is biological memory (M01-M13 of the [mechanism-gap-matrix](./mechanism-gap-matrix.md)). So are the eBay distributed-stream patents `WO 2018/191879 A1` and `US 10,691,485 B2` (AJ co-inventor, 2017-2018). Continuous-update substrate flavors — Hope-shape online gradient-coupled consolidation — are not members.

## Why this concept exists

`[ASSERTED]` The [mechanism-gap-matrix walkthrough](../open-question/memory-caddy.md#matrix-walkthrough-findings-2026-05-15) of 2026-05-15 produced a cumulative pattern: across M03 → M06, the caddy "resolved frictions" that exist for both bolt-on and substrate paths. AJ's 2026-05-15 (mid-M08) observation reframed that pattern:

> The patent architecture works for bolt-on memory just as well as for caddy memory. It doesn't work for substrate memory. So the cumulative-pattern advantage isn't caddy-specific — it's *discrete-unit-architecture-specific*. Bolt-on and caddy are in the same family. Substrate (in its continuous-update mainstream form) is in a different family.

This reframe matters because:

- The "caddy is special" reading risks attributing a generic architectural advantage to a specific implementation path.
- The "discrete-unit family" reading correctly identifies that the biological mechanism set (M01-M13) is architecturally compatible with **both** bolt-on and caddy, and architecturally incompatible with continuous-update substrate.
- For Kyrja's path-decision, the right question is not "caddy or substrate" but **"discrete-unit family — and within it, which specific implementation route?"**

## Family membership

`[ASSERTED]` Membership decided by whether the architecture admits the three structural properties above. Family-internal differences (cost, deployability, learned vs unlearned policies) matter for product strategy but not for biological-mapping faithfulness.

### Members of the discrete-unit family

| System / path | Discrete units | Separate addressable store | Consolidation event signal |
|---|---|---|---|
| Biological CLS memory | ✓ engram cell ensembles | ✓ hippocampus vs cortex | ✓ retrieval-pathway maturation (M07) |
| Bolt-on memory (Mem0, Cognee, Zep, Letta, Honcho, …) | ✓ stored facts / KG nodes / summaries | ✓ vector DB / KG / structured DB | ⚠ implicit (write-success); rarely explicit acknowledgement |
| Caddy memory model (open question) | ✓ memory unit produced by the model | ✓ memory model's own state | ✓ if designed in (learned consolidation policy with completion signal) |
| **eBay `WO 2018/191879`** (Pounds, Rogers, Liu, Pugach, 2017) | ✓ snapshot ID per message | ✓ aggregating cache → DB row | ✓ persistence of aggregated row |
| **eBay `US 10,691,485`** (Pounds, Rogers, Liu, Pugach, Sridharan, Xu, 2018) | ✓ 64-bit unique ID per message | ✓ memory-mapped transaction log → persistent storage | ✓ explicit acknowledgement-back-to-entry-point |
| Memory Networks (Weston 2014), NTM/DNC (Graves 2014/2016) | ✓ slot-based memory rows | ✓ memory matrix | ⚠ write happens, but no separable consolidation event |
| MERLIN (Wayne 2018) | ✓ row-per-timestep memory matrix | ✓ external memory beside policy | ⚠ no explicit "consolidation succeeded" signal; episode reset is the boundary |
| kNN-LM (Khandelwal 2020), RETRO (Borgeaud 2022), Memorizing Transformer (Wu 2022) | ✓ datastore entries | ✓ frozen datastore | ⚠ no consolidation event — frozen at write time |

### Non-members (continuous-update substrate)

| System | Why it falls outside |
|---|---|
| Hope (Behrouz 2026) — online gradient-coupled consolidation | Continuous gradient updates. No discrete identifiable memory unit; no separately addressable storage independent of the LLM forward pass; no consolidation event signal. |
| EvoSC (Yu 2026) — soft-prompt online distillation | Continuous soft-prompt update at frozen base. Soft prompt is discrete-ish, but at depth-2 only; no consolidation event signalling "this lesson is integrated." |
| Skill-SD (Wang 2026) — offline distillation into student weights | Continuous weight update via distillation; no per-skill discrete identifiability after distillation; consolidation event is the training run, not per-memory. |

### Partial / hybrid cases

`[SPECULATED]` Some substrate-side approaches sit ambiguously:

- **MEMIT / ROME** — discrete weight edits with addressable target locations. Properties 1 and 2 partially satisfied; property 3 (consolidation success signal) is murky.
- **Cartridges (Eyuboglu 2025)** — task-specialised adapters. If treated as discrete pluggable units, property 1 holds; property 2 partially; property 3 depends on training protocol.
- These are the substrate flavors most likely to integrate with discrete-unit thinking. But the mainstream substrate research direction (online gradient-coupled consolidation) is the *least* discrete-unit-compatible.

## How biology lines up with AJ's eBay patents

`[ASSERTED]` Production-proven architectural precedent.

| Biological mechanism | eBay patent component |
|---|---|
| Hippocampal fast store (M01) | Memory-mapped transaction log at entry point (`US 10,691,485`) |
| Cortical slow store (M02) | Persistent storage at end of message-processing stream (`US 10,691,485`) |
| Parallel encoding (M07) | Dual-write to log + processing stream (`US 10,691,485`) |
| Cortical retrieval-pathway maturation (M07) | Acknowledgement-back-to-entry-point (`US 10,691,485`) |
| Replay for unconsolidated traces (M03) | Retransmit on missing acknowledgement (`US 10,691,485`) |
| Temporal coallocation (M08) | Aggregating cache clustering by primary key + time window (`WO 2018/191879`) |
| Consolidation-as-aggregation (M03) | Aggregation function during persistence (`WO 2018/191879`) |
| Rate decoupling (M03 / fast vs slow stores) | Aggregating cache absorbs stream bursts (`WO 2018/191879`) |
| Skip-pattern failure detection | "N later sequence numbers acknowledged, this one wasn't" (`US 10,691,485`) — possibly novel relative to biology |

The patents demonstrate the architectural pattern is **sound at production scale.** They were filed at eBay 2017-2018 to handle real-volume impression and stream-processing traffic. The cog-sci/patent alignment is a coincidence of architectural pressure (the same kind of problem produces the same kind of solution), not a borrowing in either direction. eBay's engineers and biological evolution converged on the same architecture family for the same structural reasons.

## What's missing from the patents (the Kyrja gap)

`[ASSERTED]` The patents implement properties 1-3 with **unlearned policies**:

- The clustering key (`primary key` in `WO 2018/191879`) is an explicit field, not a learned representation.
- The aggregation function (`counting impressions` in the example) is hardcoded.
- The acknowledgement policy (timeout + N-later-acked) is a threshold rule, not a learned decision.

The Kyrja contribution sits in the **policy layer on top** of this architectural family:

1. Learned **clustering** — what counts as "the same memory cluster" when the key isn't an explicit field?
2. Learned **aggregation** — what shape does the consolidated unit take? Generated text, structured KG, learned representation?
3. Learned **consolidation success** — what does "this memory has been integrated" mean when the slow store isn't a DB row?
4. Learned **schema-fit** ([M05](./mechanism-gap-matrix.md)) — modulating the aggregation rate by how well the input slots into existing structure.
5. Learned **selectivity** ([M04](./mechanism-gap-matrix.md)) — which memories deserve consolidation effort.

These are the design problems Kyrja needs to solve. They are *additive* on top of a known-working architectural skeleton, not foundational research from first principles.

## Refinement (M11 walkthrough, 2026-05-15): integration-depth, not capability-binary

`[ASSERTED]` The M11 walkthrough surfaced — and AJ's cross-examination confirmed — that bolt-on and caddy are **not capability-distinct** within the family. The initial "bolt-on cannot do schema induction" reading did not survive: a bolt-on system can in principle implement the cog-sci-derived mechanism set via four learnable sub-systems (learned embedding space, learned field structure / extraction, learned salience / consolidation policy, learned retrieval policy). The real distinguisher is **integration depth**, not a capability break — bolt-on assembles multiple sub-systems with information loss at the handoffs; caddy can train one model end-to-end and let the decomposition emerge.

The detailed honest comparison of the two paths — eighteen cog-sci-derived design ideas walked, six genuinely caddy-only properties identified, one-architectural-commitment-plus-one-bet (T_A1) reduction — lives in [caddy-vs-bolt-on](./caddy-vs-bolt-on.md). The family page records the family-level result: both members are within the family and either can in principle satisfy the [mechanism-gap-matrix](./mechanism-gap-matrix.md).

## Substrate antagonism (matrix-walk validated)

`[ASSERTED]` AJ's 2026-05-15 prediction — substrate would be structurally antagonistic to roughly half of what biology surfaces — was validated by the M01-M17 matrix walk (closed 2026-05-17). The substrate column has 7/13 hard ❌ through M13, with M14 re-graded to ❌ at closeout. The family-level framing's "substrate as thought-tool, not product path" reading is confirmed.

## Implications for the path-decision

`[ASSERTED]` The substrate path's continuous-update mainstream is architecturally mismatched to the biological mechanism set the [mechanism-gap-matrix](./mechanism-gap-matrix.md) catalogues. Substrate (continuous-update flavour) is held as a contrastive thought-tool, not a candidate product path.

The active path-decision is between **bolt-on-with-cog-sci-design-ideas** and **caddy** — within the family, *not* between the family and continuous-update substrate. See [caddy-vs-bolt-on](./caddy-vs-bolt-on.md) for the full comparison and the T_A1-falsification-first recommendation.

## Related

- [[caddy-vs-bolt-on]] — the honest within-family comparison; eighteen design ideas walked, six caddy-only properties identified, T_A1 as the load-bearing bet.
- [[mechanism-gap-matrix]] — the catalogue of biological mechanisms whose translation-fit motivated this concept.
- [[memory-consumer-axis]] — the consumer-axis framing; discrete-unit family is orthogonal to it (a discrete-unit system can be memory-for-the-model or memory-for-the-agent).
- [[substrate-as-memory]] — the substrate path's framing; this concept argues the mainstream substrate flavor is *outside* the family that biology fits.
- [[consolidation-channel]] — Kyrja's primary wedge concept. Lives within the discrete-unit family.
- [[silent-engrams]] — M06 of the matrix. Pattern-completion retrieval is the read-side property of the discrete-unit family.
- [[cognitive-maps-and-conjunctive-coding]] — M11-derivative. Documents the *content* of what discrete-unit family members need to support (conjunctive binding, multiple parallel cognitive maps, salience-as-coordinate). Architectural prior set surfaced from the 2026-05-15 M11 walkthrough.
- [[caddy]] — canonical architectural definition of the within-family alternative to bolt-on. Five commitments, three within-family axes, three caddy-only properties, caddy/golfer analogy.
- [[caddy-architecture]] — detailed architectural specification (six components, 25 operations, tier labels, prototype scoping). Added 2026-05-17.
- [[caddy-interface-doors]] — D/U/Q door framework for caddy/golfer integration. Mechanical specification of read/write/query paths. Added 2026-05-17.
- [open-question / memory-caddy](../open-question/memory-caddy.md) — the live design question; this concept reframes its cumulative-pattern finding.
- [open-question / online-vs-offline-consolidation](../open-question/online-vs-offline-consolidation.md) — design fork for the consolidation operator; the discrete-unit framing constrains the regime choices.
- [[retrieval-granularity]] — within-family design dimension; discrete-unit members can differ in granularity choice (current incumbents all per-turn) independently of substrate-shape.
- [[H43-soft-composition-emergent-construction]] — soft-composition (attention-style output) caddies sit at the boundary of the discrete-unit family; hard-selection members are unambiguously discrete-unit.
- [[pattern-separation]] — architectural prerequisite for graded decay within discrete-unit family members.
- [multi-field-memory-unit](../decision/multi-field-memory-unit.md) — refinement of the "discrete unit" structural property: units are multi-field tuples (`event_rep` + `raw_content` + `trajectory_state`), not single vectors. Refines property 1 without changing family membership.

## Source archive

- AJ-originated reframe, 2026-05-15, mid-M08 discussion in the matrix walkthrough.
- Patent precedent: `WO 2018/191879 A1` (filed 2017-04-19, published 2018-10-25, eBay) and `US 10,691,485 B2` (filed 2018-02-13, granted 2020-06-23, eBay). Local copies: [library/papers/wo-2018191879-consistency-mitigation.pdf](../../../research/library/papers/wo-2018191879-consistency-mitigation.pdf), [library/papers/us-10691485-availability-oriented-durability.pdf](../../../research/library/papers/us-10691485-availability-oriented-durability.pdf).
- The patents are external prior art (not Kyrja work), legitimate citation targets per [[source-vs-experiment-typing]]. They could warrant `source/` pages if cited from multiple places; for now, citation lives inline here.
