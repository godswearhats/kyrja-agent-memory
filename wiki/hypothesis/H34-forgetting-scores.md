---
type: hypothesis
name: H-FORGETTING-SCORES — MOOM-style 3-dim forgetting scores work
status: PROPOSED
last_ingested: 2026-06-10
sources: [../source/moom-paper-2509.md]
epistemic_tags: [asserted]
tags: [consolidation, forgetting, manage-layer]
---

> **Cross-link to dual (added 2026-05-17):** [H42 — learned salience function](H42-learned-salience-function.md) is the **dual** of this hypothesis. Forgetting-as-learned-policy and salience-as-learned-policy likely share architecture — the same model with opposite-sign outputs, or two heads on a shared backbone. See [salience-signal open question](../open-question/salience-signal.md) for the upstream framing. Together they decompose the consolidation decision into "what to keep" + "what to drop" as paired learned policies.

> **M17 architectural reweighting (added 2026-05-17):** The [Hardt, Nader & Nadel 2013](../source/hardt-nader-nadel-2013-active-forgetting.md) walk repositioned this hypothesis from "one good tool in the toolkit" to "*the* place intelligence may belong in agent-memory architecture." Biology's "encode promiscuously, forget intelligently" inverts current AI practice (smart admission + weak forgetting). The MOOM-style scoring this hypothesis tests is one concrete implementation of the inverted-architecture bet. See [matrix row M17](../concept/mechanism-gap-matrix.md) and the [admission-control § M17 tension](../concept/admission-control.md) note.

> **Competition-suppression = the supersession signal (added 2026-06-10):** The third scoring dimension (competition suppression) is precisely the evidence that two facts contend for the *same* retrieval slot — i.e. the disposal-side trigger for [fact-supersession](../concept/fact-supersession.md). This already gives a learned-policy mechanism for the *disposal* half of supersession (silence the loser). What it does **not** supply is the *detector* that decides whether the contention is genuine supersession (silence) vs refinement vs a coordinate multi-value fact (keep both) — that is an *updating*-stage problem, not a forgetting one. See [fact-supersession § detection vs disposal](../concept/fact-supersession.md).

> **Pattern-separation prerequisite (added 2026-05-17):** This hypothesis has an architectural precondition. Without pattern-separated memory representations (orthogonal / sparse / LSH-separated keys), similar memories collide and interference dominates as the forgetting mechanism — and no per-memory decay rate has a meaningful referent. The MOOM-style scoring assumes each memory is independently addressable; that assumption requires [pattern-separation](../concept/pattern-separation.md) as a separately-designed property. Verifying pattern separation is a prerequisite for measuring this hypothesis cleanly.

## Claim

Scoring memories on three dimensions — temporal decay, retrieval reinforcement, and competition suppression — using injection-competition logs as the signal source, produces a useful ranking for deciding which memories to demote. The MOOM-published 9:1 access-to-recency ratio (β=0.9, α=0.1) is a reasonable starting calibration.

## What would falsify it

- Running the MOOM formula on production data shows it demotes memories that turn out to be frequently needed (over-aggressive forgetting).
- The competition signal is too noisy — small differences in rank don't predict quality differences.
- A simpler approach (pure recency decay, or human curation, or no forgetting at all) produces equivalent or better downstream retrieval quality.

## Evidence for

- **MOOM paper** (arxiv 2509.11860, see [MOOM source](../source/moom-paper-2509.md)) — published the formula and demonstrated it on their benchmark. `[ASSERTED]`. Competition-inhibition mechanism is cognitive-science-inspired.
- **Architectural elegance.** Competition logs are a byproduct of normal retrieval+injection; no extra data collection needed.
- **Cognitive-science grounding.** Forgetting in human memory is driven by competition/interference, not just time. The mechanism mirrors empirical psychology.

## Evidence against

- MOOM was tested on a single-agent chatbot benchmark, not enterprise multi-agent or coding workloads.
- The 9:1 access-vs-recency ratio may not hold for coding workloads where temporal-relevance patterns differ (e.g. a recent bug fix may matter more than a frequently-accessed-but-stale config note).
- Formula hasn't been run on our data; the ranking quality is unknown for our memory types.

## Open sub-questions

- What does "useful ranking" mean operationally? Candidate metric: demoted memories are rarely-requested-after-demotion (precision-of-forgetting).
- How does forgetting interact with [H36-consolidation-ordering](./H36-consolidation-ordering.md)? The ordering question depends on this scoring being meaningful in the first place.
- Does forgetting-as-demotion (memory moved to cold tier) match the MOOM model, or does demotion need to be a different operation than the published forget-from-store one?

## Related

- [admission-control](../concept/admission-control.md) — the upstream sibling: admission decides what *enters*; forgetting decides what *stays*
- [H36-consolidation-ordering](./H36-consolidation-ordering.md) — depends on this scoring working
- [pattern-separation](../concept/pattern-separation.md) — architectural prerequisite for graded decay; per-memory decay rates have no meaningful referent if memories are constantly clobbering each other at shared addresses
- [hardt-nader-nadel-2013-active-forgetting](../source/hardt-nader-nadel-2013-active-forgetting.md) — cog-sci anchor; "encode promiscuously, forget intelligently" architectural framing
- [matrix row M17](../concept/mechanism-gap-matrix.md) — active forgetting; this hypothesis is the operational AI-side translation
- [catastrophic-interference § interference-vs-decay distinction](../concept/catastrophic-interference.md) — the M17 partition refines what kind of forgetting this hypothesis is implementing (decay, not interference)
- [tool-chain-wedge-as-adoption-path](../decision/tool-chain-wedge-as-adoption-path.md) — wedge defers TTL/forgetting; this hypothesis is the v2+ formalization
- Shelved predecessor: H19 in _archive
