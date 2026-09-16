---
type: concept
name: Fact supersession — silence, don't delete; detect (updating) vs dispose (forgetting)
status: living
last_ingested: 2026-06-12
sources: [../source/josselyn-tonegawa-2020-engrams.md, ../source/hardt-nader-nadel-2013-active-forgetting.md]
epistemic_tags: [asserted, speculated]
tags: [caddy, fact-tier, supersession, silent-engrams, active-forgetting, updating-stage, failure-mode]
---

## Definition

`[ASSERTED]` **Supersession** is the failure mode where a fact that *was* true changes ("I'm vegetarian" → "I'm pescatarian now"), and the stale fact, left in the verbatim store, is later retrieved and asserted as current. It is the signature hazard of the [fact (verbatim) tier](./verbatim-vs-latent-tiers.md): the very property that makes the tier good at facts — **immutability** (verbatim traces don't drift) — makes it helpless against change. The [schema tier](./verbatim-vs-latent-tiers.md) gets supersession for free (EMA drift slides toward recent statistics); the fact tier does not.

This page exists because supersession is load-bearing across the failure analysis ([caddy](./caddy.md)), the forgetting machinery ([H34](../hypothesis/H34-forgetting-scores.md)), the silencing primitive ([silent-engrams](./silent-engrams.md)), and the active-stages taxonomy ([active-stages-framework](./active-stages-framework.md)) — and because it carries an open research problem (the detector) with its own lifecycle.

## Claim 1: silence, don't delete

`[ASSERTED]` The disposal of a superseded fact should be **silencing**, not deletion. This applies the [silent-engram](./silent-engrams.md) primitive — the three-way *available / silent / absent* distinction — to supersession directly. When "I'm vegetarian" is superseded, it should move to **silent** (trace intact, retrieval handle removed), not to **absent** (destroyed).

Why silencing beats deletion here:

- **Non-destructive.** "They were strictly vegetarian until three weeks ago" is itself a fact that may matter; deletion throws away the history.
- **Reversible.** Supersession in the wild is often temporary or contextual ("vegetarian during Lent"). A silenced trace reactivates if the user reverts; a deleted one cannot.
- **Maps to compaction.** Silencing is exactly what an [LSM-tree compaction pass](./verbatim-vs-latent-tiers.md) does — move the losing version to a cold tier with its retrieval key removed. A silent engram is a tombstone-that-isn't-quite-a-tombstone.

`[ASSERTED]` This is why the synchronous "supersede/delete action" improvised in the 2026-06-08 Web-Claude transcript is the wrong shape: it is a binary destroy-and-replace reached for *because the transcript lacked the compaction frame*. With active forgetting as the compaction policy, supersession is just what compaction does.

## Claim 2: detection (updating) and disposal (forgetting) are different stages

`[ASSERTED]` Active forgetting is the **disposal** half only. It answers "this fact has decayed in usefulness — silence it." It does **not** answer "this *new* fact contradicts an *old* one, so fire the silencing now." That trigger is **detection**, and in the [active-stages-framework](./active-stages-framework.md) it belongs to the **updating** stage, not forgetting. The clean decomposition:

> **surprise-gated supersession detection (updating) → silencing (forgetting)**

`[ASSERTED]` The detection trigger is already present in the architecture: the contradiction produces a large representation-space **surprise spike** (the predictor expected continuity, got a reversal), which is exactly the signal that cleanly segments the supersession event. The signal to act is present; the *action* and the *decision to act* are the parts that need building.

## The open problem: the detector must distinguish three look-alike cases

`[SPECULATED]` The hard, unsolved part is that the detector must tell apart three situations that look similar at the surface:

1. **Supersession** — "vegetarian" → "pescatarian now": old is now **false**, silence it.
2. **Refinement** — "vegetarian" → "vegetarian, but eats fish on holidays": both **true**, the second narrows the first; do *not* silence.
3. **Genuine multi-value fact** — "vegetarian on weekdays, fish on weekends": both **true** and coordinate; keep both, linked.

Collapse these and you get one of two failures: fail to silence stale facts (the original supersession bug) or wrongly silence true ones (a worse, quieter bug). No current system — and neither the Web-Claude transcript nor active-forgetting-as-stated — cracks this. It is the live research question this page names.

## Sightings in the RL-memory cluster (2026-06-12, all four papers full-read verified)

`[ASSERTED]` The detector's three-case confusion is not hypothetical — it is the *motivating failure* of the RL-memory training literature:

- **[Memory-R1](../source/yan-2025-memory-r1.md)** (Fig. 1, App. A.1): a vanilla manager reads "adopted another dog named Scout" as contradicting "adopted Buddy" and issues DELETE+ADD — **refinement (case 2) misread as supersession (case 1)**, producing exactly the "wrongly silence true facts" failure this page names as the worse, quieter bug. Their RL-trained manager learns the consolidating UPDATE instead. Independent confirmation that the reconciling action must exist *and* be selected correctly.
- **[Memory-R2](../source/yan-2026-memory-r2.md)** (Fig. 7 prompt): DELETE fires only when a fact is "explicitly prove[d] false or invalid (*not merely outdated*)"; a monotonicity rule retains outdated-but-true state and **defers conflict resolution to read time**, where a hard-coded recency-default reader resolves it. A prompt-engineered approximation of silence-don't-delete — with the disposal stage missing entirely.
- **[AgeMem](../source/yu-2026-agemem.md)** (case study B.1): preference change handled by UPDATE that writes provenance *into the content string* ("updated from 60 minutes"), later requiring a DELETE+ADD hygiene pass to purge the stale reference. A curated trace, but it exhibits the full supersession-hygiene loop — and the provenance-in-content anti-pattern that makes cleanup necessary.
- **[Mem-α](../source/wang-2025-mem-alpha.md)** (§3.4): explicitly **excludes conflict resolution from training** "due to the lack of realistic evaluation benchmarks." The training side of the field is dodging supersession for want of exactly the benchmark axis MASQ builds ([multi-party-attribution-gap](./multi-party-attribution-gap.md)).

Net: the cluster confirms the failure mode is live in deployed-style systems, that current fixes are prompt rules rather than learned detectors, and that nobody trains or scores the three-case distinction.

**Fifth training-side sighting (2026-06-12, full-read verified).** [Mem-T](../source/yue-2026-mem-t.md) reproduces both established patterns in one system: its DeleteItemTool fires only when an item is "explicitly negated or wrong" (R2's monotonicity rule as prompt scaffolding), and its UpdateItemTool instructs "must save the original time information of previously items in the document" — the provenance-in-content anti-pattern from AgeMem's case study, now appearing as *designed-in* policy rather than emergent behavior. Its case study also re-exhibits the untrained refinement-misread-as-supersession failure (baseline overwrites unrelated entries via UPDATE), fixed by training. The schema's validity windows `[t_start, t_end]` are the cleaner half — provenance as metadata, not content.

**Benchmark-side sighting + a fourth case (2026-06-12, full-read verified).** [STALE](../source/chao-2026-stale.md) builds an evaluation around exactly the implicit half of this page (later observation invalidates earlier memory without surface negation) and finds the failure pervasive: updated evidence retrieved but not *adjudicated* — only 3.3% of co-retrieved stale entries judged as needing update; "visibility does not imply authority" (their Table 3). Their CUPMem prototype is an **engineered write-side version of the detector this page names open**: per-slot {KEEP, STALE, REPLACE, UNKNOWN} adjudication at write time, jumping 8.7%→68% on the same backbone. Two takeaways: (1) write-side adjudication, not retrieval, is empirically the lever — consistent with this page's compaction-time-disposal framing; (2) their **UNKNOWN_CURRENT** state is a **fourth case our taxonomy lacks**: *old value invalid, replacement not yet established* (in multi-party form: "decision reopened but not re-decided"). Single-user and schema-dependent (hand-built life-domain ontology), so the detector problem in our schema-free team-decision setting remains open — but the four-case taxonomy should be considered when the fact-tier detector is prototyped, and the reopened-not-redecided case is logged as a MASQ extension candidate (`masq-paper/FUTURE.md`).

## Two prerequisites inherited from the forgetting theory

`[ASSERTED]` Supersession does not get solved "for free" by adopting active forgetting; it inherits two prerequisites:

- **Pattern separation.** Supersession *is* a collision case — "I'm vegetarian" and "I'm pescatarian" sit almost on top of each other in key space (both "user dietary constraint, food domain"). Per [pattern-separation](./pattern-separation.md), graded silencing has no meaningful referent unless near-duplicate keys can be told apart well enough to recognise "same slot, new value." This is the [H34](../hypothesis/H34-forgetting-scores.md) prerequisite biting again.
- **The competition signal is the supersession signal.** [H34](../hypothesis/H34-forgetting-scores.md)'s third scoring dimension — *competition suppression* — is precisely the evidence that two facts contend for the same retrieval slot, i.e. the disposal-side trigger. We already have a learned-policy mechanism for the disposal half; what is missing is the detector that decides *which* of the three cases above obtains.

## Timing: defense in depth

`[SPECULATED]` If silencing runs only at offline compaction, a just-superseded fact stays live and retrievable *within* a session — so the failure can still fire before the next compaction. Therefore two mechanisms, not one:

- **Synchronous staleness-on-read.** The retrieval policy needs **staleness/recency as an observable input** so it can skip a not-yet-compacted stale fact (a policy cannot learn a distinction its state vector can't see — see [caddy § Rock-3 design lemmas](./caddy.md)).
- **Asynchronous silencing-at-compaction.** The durable disposal happens in the background pass.

This is the partial vindication of the transcript's two instincts (a supersede action; staleness-awareness): both are right *as parts*, wrong as a single synchronous fix.

## Why this matters

- It converts the success-case-looks-complete illusion into two concrete design requirements (a detector in the updating stage; silencing as compaction-time disposal).
- It connects three previously-separate wiki threads — [silent-engrams](./silent-engrams.md), [H34 forgetting](../hypothesis/H34-forgetting-scores.md), and the [active-stages](./active-stages-framework.md) updating/forgetting split — into one mechanism for the fact tier.
- The detector problem is a clean, falsifiable open question worth promoting to a hypothesis once the fact tier is being prototyped.

## Scope limits

- This page is about *facts that change*. The static format/read mechanics are [verbatim-vs-latent-tiers](./verbatim-vs-latent-tiers.md).
- It does not specify the detector — distinguishing supersede/refine/multi-value is named here as open, not solved.
- Schema-tier change (drift) is out of scope by construction; schemas handle change via EMA, no special machinery.

## Related

- [silent-engrams](./silent-engrams.md) — the available/silent/absent primitive this applies to supersession
- [verbatim-vs-latent-tiers](./verbatim-vs-latent-tiers.md) — the fact tier and its LSM-compaction frame
- [H34-forgetting-scores](../hypothesis/H34-forgetting-scores.md) — competition-suppression dimension = the disposal-side supersession signal
- [active-stages-framework](./active-stages-framework.md) — detection is *updating*, silencing is *forgetting*
- [pattern-separation](./pattern-separation.md) — prerequisite: colliding keys must be separable
- [caddy § Rock 3](./caddy.md) — the design lemmas (observable state, action space) that govern the detector and silencer
- [Memory-R2](../source/yan-2026-memory-r2.md) — the training-side mirror (memory makes RL comparisons unfair); **full-read verified 2026-06-12**, with [Memory-R1](../source/yan-2025-memory-r1.md), [Mem-α](../source/wang-2025-mem-alpha.md), [AgeMem](../source/yu-2026-agemem.md) (see Sightings section)
- [STALE](../source/chao-2026-stale.md) — benchmark-side sighting; CUPMem = engineered write-side detector; source of the fourth (UNKNOWN_CURRENT) case
- [Mem-T](../source/yue-2026-mem-t.md) — fifth training-side sighting; monotone-DELETE rule + provenance-in-content as designed-in policy; **full-read verified 2026-06-12**

## Source archive

Synthesized 2026-06-10 from the 2026-06-08 Web-Claude transcript (`web-claude-chat.txt`, supersession failure-trace) reconciled against [silent-engrams](./silent-engrams.md), [H34](../hypothesis/H34-forgetting-scores.md), and the [Hardt/Nader/Nadel active-forgetting](../source/hardt-nader-nadel-2013-active-forgetting.md) framing.
