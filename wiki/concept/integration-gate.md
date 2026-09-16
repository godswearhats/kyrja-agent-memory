---
type: concept
name: The integration gate — Kerros's validity test, as a scaling separation
status: living
last_ingested: 2026-05-30
program: kerros
sources: [../source/xu-2026-agentic-memo.md, ../source/zhang-2026-compression-spectrum.md, ../source/nader-schafe-ledoux-2000-reconsolidation.md, ../source/mcclelland-mcnaughton-oreilly-1995-cls.md]
epistemic_tags: [asserted, speculated]
tags: [kerros, validity-gate, boltability, methodology, capability-map]
---

> **Program: [Kerros](./kerros.md).** This page holds the formal treatment of the boltability gate that [kerros.md](./kerros.md) refers to. The charter says *what* Kerros is; this page says *how a Kerros result is validated* and *what survives the test*.

## Definition

The **integration gate** is the validity test for a Kerros result: a result counts only if it beats a bolt-on **control** via integration the bolt-on structurally cannot match. The bolt-on (memory-for-the-agent: text retrieved into a frozen model's context) is not a competitor to out-engineer — it is the control.

This page records the 2026-05-26 refinement: the gate is **not binary** ("can a bolt-on do X?") but a **scaling separation** ("does the bolt-on's imitation cost diverge with problem complexity?").

## The refinement: binary → scaling separation

`[ASSERTED]` (Nils/AJ, 2026-05-26.) Asking "can a bolt-on do X?" is the wrong question, and it is the trap the old [tier-3-4 wedge](../decision/tier-3-4-as-wedge.md) framing fell into. A bolt-on with arbitrary software and offline LLM calls can *imitate* almost anything — summarise (fake consolidation), generate-and-store scenarios (fake construction), read-modify-write a record (fake reconsolidation). Asked "can it?", the answer is almost always "yes, weakly," and the gate fails to discriminate.

The right question:

> **Does the bolt-on's imitation cost stay bounded, or diverge with problem complexity?**

Integration counts only when simulating it through the prompt costs something that *diverges*. The formal instance is [Xu, Dai & Zhang 2026, Theorem 1](../source/xu-2026-agentic-memo.md): in-context (retrieval) composition pays `Ω(k²)` sample complexity while parametric composition pays `O(d)` — a separation `Ω(k²/d)` that is *"independent of context window size."* Not "the bolt-on can't compose," but "the bolt-on composes at a cost that blows up."

This gives the gate a ruler: **separation strength = how fast the bolt-on's imitation cost grows.** Construct-validity note: the divergence half rests on Xu's **Assumption 1** (`ᾱ < 1` — a frozen LLM given K demos caps below full accuracy on held-out pairs), which is *empirical, not proven*. If pretraining already covers the rule, `ᾱ → 1` and the separation vanishes. Establishing `ᾱ < 1` is mandatory, not assumable — it is the generalised [BoW-at-chance gate](../open-question/tier-3-structural-vs-semantic.md).

## The second refinement: existence is not enough — the efficiency gate

`[ASSERTED]` (AJ catch, 2026-05-28.) The scaling separation above tests **existence**: can weights *represent* a composition the frozen bolt-on can't? But [Xu Thm 1](../source/xu-2026-agentic-memo.md) is a **sample-complexity** separation (in-context retrieval `Ω(k²)` vs parametric `O(d)`) — it shows the parametric solution is *compact* and that retrieval scales badly, but it says nothing about the **training/acquisition cost** of reaching that solution, nor whether a real model can write it *incrementally and few-shot*. Passing it proves "possible in principle," not "is a memory function." A *memory* function is defined by cost: it must absorb new knowledge **cheaply, locally, incrementally** — and cheap-incremental-vs-retrain is precisely the line between **memory** and **training**. So the gate has two faces, and the spec was implicitly testing only the first:

- **Gate 1 — existence.** The separation exists: the bolt-on's imitation cost diverges while the integrated arm holds. (The scaling separation above.)
- **Gate 2 — efficiency.** The integrated arm's *write* is cheap enough to be memory, not a retrain. A model already competent at the task must absorb a *new* symbol via a cheap, local, few-shot weight write and still generalise.

Both are necessary; Gate 1 alone is half a result. The gate as specced could *pass* (bolt-on diverges, weights hold) and Kerros still be impractical if integration needs training-scale compute — in which case the inert bolt-on is the right product. This is the make-or-break viability question, tracked as [incremental-integration-cost](../open-question/incremental-integration-cost.md).

`[MEASURED]` First Gate-2 evidence ([scaling-and-memory-gates](../experiment/2026-05-26-factored-operator-beachhead/scaling-and-memory-gates.md), 2026-05-28): the *cheapest* write — freeze the transformer, train only a new symbol's embedding row — **fails to generalise** (few-shot at chance, perfect retention). **Construct-validity:** the train-loss column is decisive — loss→0 with held-out at chance shows the failure is *generalisation*, not insufficient data. Diagnosis: underdetermined in parameter space (data was sufficient; the 896-d row has too many free directions, no low-rank prior). Not yet decisive — the escalation ladder (low-rank-constrained write → LoRA → full-FT-continued) is unrun, and the underdetermination diagnosis predicts a low-rank write *should* recover few-shot generalisation. That prediction is the pending decider.

`[ASSERTED]` **Sharpening (2026-05-30): Gate 1's read was *bought with a training write*, so Gate 2 is not optional.** The Gate-1 separation was demonstrated by *full fine-tuning* the integrated arm — i.e. the read advantage was purchased with a training-cost write. So Gate 1 proves the **prize exists** (a class of problems where thinks-with beats thinks-about) but, on its own, is **inert as a memory mechanism**: the advantage is reachable only through a write we don't yet know how to make cheap. Read and write don't separate cleanly — the read only matters if the knowledge can be *written*. This reframes the write (Gate 2 / [incremental-integration-cost](../open-question/incremental-integration-cost.md)) from "half the bet" to **the whole bet**; Gate 1 is the motivation, not a standalone result. (Strategy session, Nils/AJ — exploratory; see also the [wedge-sizing](../open-question/thinks-with-wedge-sizing.md) scoping thread.)

## The capability map: applying the gate to the mechanism-gap matrix

`[ASSERTED]` Re-grading the [mechanism-gap-matrix](./mechanism-gap-matrix.md) (M01–M17) by the scaling-separation gate — *does the capability require information to live in weights/activations, or can it be staged as text through a frozen pass?* — collapses the 17 mechanisms onto a single axis. The pivot is the [memory-consumer-axis](./memory-consumer-axis.md): integration ↔ memory-for-the-model; persistence ↔ memory-for-the-agent.

| Bucket | Mechanisms | Bolt-on imitation cost | → |
|---|---|---|---|
| **Integration (Kerros)** — compositional / constructive generalization | M12, M14, M16 | **Diverges** (combinatorial / Xu `k²/d`) | strongest, *provable* |
| **Integration (Kerros)** — consolidation into the slow store (schema-fit) | M03, M05, M07 | grows (text-replay scales with the knowledge base) | medium–strong |
| **Persistence (product)** | M01, M04, M08, M09, M13, M15, M17 | bounded (storage/selection/decay a software loop does fine) | boltable |
| **Inverted cost (a constraint, not a capability)** | M11 (interference) | bolt-on *wins* — inert records never collide; integration *risks* collision | flag |
| **Excluded** | M10 (reconsolidation) | — | see Exclusions |

`[ASSERTED]` **The map collapses to one bet.** Through the gate, the Kerros bucket is not a list — it is a single capability, **non-frozen weights**, with two faces:
- **Read-side = composition** — apply consolidated rules to inputs never seen (Xu-provable separation).
- **Write-side = consolidation** — extract rules from inert episodes into θ (the [consolidation-channel](./consolidation-channel.md)).

This supersedes the wedge-anchored [research-backlog stack-rank](../decision/research-backlog-stack-rank.md): its seven items were ranked against "moves us toward tier 3-4 retrieval via the caddy," a product-wedge goal. Re-derived through the gate, they reduce to one Kerros target plus a pile of product/persistence and one cost.

**Construct-validity flag (recorded honestly):** the wide pass *converged* on the [consolidation-channel](./consolidation-channel.md) we already had. Two readings — (a) *robust*: four independent roads (product-wedge, cog-sci, consumer-axis, the formal gate) reached the same target; (b) *predetermined*: the gate ("beat the bolt-on via something in weights/activations") nearly *defines* the answer as weights-plasticity, so the pass may not have had room to diverge. AJ's call (2026-05-26): convergence is evidence, not echo — but the tightness of the gate is the thing to keep attacking. The pass's defensible value is **narrowing** (one bet, not seven), **exclusion** (below), and isolating the **one provable test** (composition).

## Exclusions

### M10 — reconsolidation / per-memory malleability: out of scope

`[ASSERTED]` (AJ decision, 2026-05-26: *"M10 stays dead — a feature for biology, a bug for software."*) [Reconsolidation](../source/nader-schafe-ledoux-2000-reconsolidation.md) (retrieval makes a stored memory labile and rewrites it) reads like a Kerros capability but is **undesirable**, not merely unproven:

- **Drift / confabulation.** Memories that mutate on use lose the reliability that inert records have.
- **Security.** It *worsens* the [evil² problem](../source/xu-2026-agentic-memo.md): if retrieval can rewrite good memories, an attacker doesn't just add poison, they edit your truth. `P(compromise) → 1` gets a second amplifier.
- **Inspectability.** Per-memory mutability is the opposite of the auditability the bolt-on rightly prizes (see [Zhang 2026 §2.3](../source/zhang-2026-compression-spectrum.md)).

The desirable "malleability" AJ named (*"our memory is malleable, yours is not — let's fix that"*) is **non-frozen weights**, not mutable episodes. Crucially, this distinguishes two operations the wiki sometimes blurs:

> **Consolidation** (extract structure into θ — Kerros) ≠ **reconsolidation** (rewrite the episode on retrieval — excluded).

This refuses the refinement the [Nader source page](../source/nader-schafe-ledoux-2000-reconsolidation.md) suggested (folding retrieval-triggered rewrite *into* the consolidation channel). Episodes stay inert and inspectable; θ is where plasticity lives. The biological lability is very likely a *constraint* (a synapse can't be stable and writable at once) AI doesn't share — AI has copy-on-write. Borrow the capability (interference-safe integration), drop the policy (lability-on-retrieval). Consistent with the prior [R5 read-as-write decline](./mechanism-gap-matrix.md) per inspiration-not-blueprint.

## The cost ledger — integration is not free

`[ASSERTED]/[SPECULATED]` Three costs the gate makes visible, all paid for by the same architectural move (collapsing the inert store into computation):

1. **Interference (M11).** The inert store avoids collision by construction; weights risk it. CLS pays this down with pattern separation + slow interleaved consolidation.
2. **Inspectability / editability** (the [Zhang 2026](../source/zhang-2026-compression-spectrum.md) steelman). You can audit and delete a text rule; you can't easily excise a fact from weights.
3. **Write-side separation is unproven.** Composition (read-side) has a theorem; the claim that integration captures *updates the frozen pass can't author* (write-side) has only the analogy. `[SPECULATED]`, not `[ASSERTED]`.

**Resolution: co-existence, disciplined by minimum plasticity.** Keep an inert, inspectable scaffold store (the bolt-on's strength) *and* a plastic weight store (Kerros). Consolidate to weights **only** the validated, cross-domain structure that has earned it — [Zhang 2026's](../source/zhang-2026-compression-spectrum.md) own "promote only when evidence warrants" principle, carried one rung past their scope boundary. This is CLS, it is the gate, it keeps M10 dead, and it bounds the inspectability cost to the most-general knowledge.

## How to use it — the experiment shape

`[SPECULATED]` The gate, run honestly, dictates the beachhead experiment (design direction, spec not yet locked):

1. **Pick a composition rule with real structure** (small `d`, large `k²` — so the gap is big).
2. **Establish `ᾱ < 1`** — empirically show the frozen base model can't do it in-context, however many demos. (The generalised BoW-at-chance check; skipping it builds another contaminated [arc test](../open-question/tier-3-structural-vs-semantic.md).)
3. **Beat the control:** integrated path learns from ~`O(d)` while the bolt-on control (the same content as the best L3 text rule, source experience held constant) stays stuck.

This is the boundary-crossing version of [Zhang 2026's](../source/zhang-2026-compression-spectrum.md) testable prediction (i) (L2 skills vs L1 retrieval, source held constant) — theirs minus the gate-crossing is ours.

**Locked + Phase-1-validated (2026-05-26).** This design is now the [factored-operator beachhead spec](../experiment/2026-05-26-factored-operator-beachhead/spec.md) (pre-registration locked). The composition rule is a rank-`m` factored operator (adjusted-cosine of hidden per-symbol vectors), which decouples "cheap to learn" (small `m`) from "can't be written down" (large `k`). [Phase 1](../experiment/2026-05-26-factored-operator-beachhead/phase1-results.md) (idealised stand-ins, no LLM) confirmed the task expresses the separation and that the `ᾱ<1`/order-blind floor sits at chance once the embeddings are centred+normalised.

## Related

- [kerros.md](./kerros.md) — the program charter that refers to this gate.
- [mechanism-gap-matrix](./mechanism-gap-matrix.md) — the 17 mechanisms this page re-grades; see its 2026-05-26 re-grade section.
- [memory-consumer-axis](./memory-consumer-axis.md) — the model/agent pivot the sort runs on.
- [consolidation-channel](./consolidation-channel.md) — the write-side face of the one Kerros bet; where the Gate-2 write cost is paid.
- [incremental-integration-cost](../open-question/incremental-integration-cost.md) — Gate 2 made durable: is the write cheap enough to be memory, or training in disguise?
- [scaling-and-memory-gates](../experiment/2026-05-26-factored-operator-beachhead/scaling-and-memory-gates.md) — the run that tests both gates; Gate 1 cleared at k=64/128, Gate 2 first result negative.
- [tier-3-structural-vs-semantic](../open-question/tier-3-structural-vs-semantic.md) — the BoW-at-chance gate; the special case of the `ᾱ < 1` check.
- [research-backlog-stack-rank](../decision/research-backlog-stack-rank.md) — the wedge-anchored ranking this re-derivation supersedes.
- [Xu, Dai & Zhang 2026](../source/xu-2026-agentic-memo.md) — Theorem 1, the formal separation.
- [Zhang et al. 2026 — Experience Compression Spectrum](../source/zhang-2026-compression-spectrum.md) — the bolt-on foil; the steelman and the minimum-plasticity principle.

## Source archive

Refinement + capability-map produced in the 2026-05-26 Nils/AJ Kerros wide-pass session (continuation of the 2026-05-25 program split). Walked the mechanism-gap-matrix through the gate; walked Xu Theorem 1 from first principles; walked M10 and resolved its exclusion; ran the literature survey (ParamMem, Skill-SD, Experience Compression Spectrum). No new experiment run — this is analysis + survey synthesis.
