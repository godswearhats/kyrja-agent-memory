---
type: decision
name: Research backlog stack-rank — H44, H40, H42, H41, H43, H39, K6 ordered into a single queue
status: SUPERSEDED
last_ingested: 2026-06-07
sources: [../experiment/2026-05-18-T_A1b-isolation-derisk/README.md]
epistemic_tags: [asserted, speculated]
tags: [research-program, stack-rank, backlog, ordering]
---

> **SUPERSEDED 2026-05-26 by the [integration-gate re-derivation](../concept/integration-gate.md).** This 7-item ranking was anchored to *"moves us toward tier 3-4 retrieval via the caddy"* — a product-wedge goal. Re-graded through the [integration gate](../concept/integration-gate.md), the backlog collapses to a single Kerros bet (**non-frozen weights**: composition read-side, consolidation write-side); the rest are persistence (product), one cost (M11 interference), or excluded (M10). The per-item analysis below is preserved as chronicle; the dequeue order is no longer the live plan. The live target is the composition-separation beachhead in [kerros.md](../concept/kerros.md).

## Decision

`[ASSERTED]` Order the caddy-research-program backlog into a single ordered queue. Per [caddy-as-research-program](./caddy-as-research-program.md), the project runs **one active research thread at a time**; this page sets the dequeue order.

**The queue (2026-05-20):**

| # | Item | Falsifiable form | Type | Status |
|---|---|---|---|---|
| 1 | **T_A1b isolation de-risk** | [H44](../hypothesis/H44-T_A1b-cross-domain-transfer.md) | Load-bearing T4 (representation pathway) | Pre-implementation pre-work |
| 2 | **K2+T_A3 isolation experiment** | [H40](../hypothesis/H40-schema-fit-modulated-consolidation.md) | Load-bearing T4 (consolidation-policy pathway) | Spec preserved in H40, ready to dequeue |
| 3 | **Learned salience function** | [H42](../hypothesis/H42-learned-salience-function.md) | Cross-cutting primitive (C) | PROPOSED; testable on bolt-on shape |
| 4 | **Temporal-context retrieval** | [H41](../hypothesis/H41-temporal-context-retrieval.md) | Read-side primitive (R1 / M13) | PROPOSED; probe 3 of H44 partially covers |
| 5 | **Soft-composition emergent construction** | [H43](../hypothesis/H43-soft-composition-emergent-construction.md) | Output interface (I1 / M16) | PROPOSED; multi-quarter build |
| 6 | **Silent-state primitives** | [H39](../hypothesis/H39-silent-state-primitives.md) | Storage primitive (S2 / M06) | PROPOSED; re-evaluate vs back-burner |
| 7 | **Offline composition** | (K6 — no formalized hypothesis yet) | Speculative T4 | Needs hypothesis formalization first |

Items 1–2 are the **load-bearing pair** that decides the architecture's scientific footing (representations + consolidation policy, on distinct timescales per CLS theory). Items 3–4 are architectural primitives the load-bearing experiments compose with or partially cover. Items 5–7 are downstream of the load-bearing pair.

The queue is robust to H44's outcome: H44 stays #1 either way (we need the result), and H40 is #2 regardless (independent of H44 per H40's Path B testability with a proxy fit signal). After H44 + H40 land, items 3–7 reorder based on what was learned.

## Motivation

Per [caddy-as-research-program](./caddy-as-research-program.md) (2026-05-20), the caddy is a research program. Commercial track owned by Eira. AJ rule: *"we can very definitely only do one thing at a time."* The architecture is treated as a stack-ranked research backlog, not a parallel-work plan.

### Criteria applied (AJ-approved 2026-05-20)

Each item ranked against four criteria, anchored to *moves us toward demonstrating tier 3-4 retrieval via the caddy*:

1. **Scientific leverage** — how foundational toward the goal; how much does it unblock downstream items
2. **Tractability** — feasibility with current resources (single GPU, AJ's time, agent context)
3. **Dependencies** — what blocks this; what does this block
4. **Frontier-pacing risk** — is anyone obviously working on the same question; would a public result subsume ours

### Per-item analysis

**#1 — H44 / T_A1b isolation de-risk.**
- **Scientific leverage**: HIGHEST. T_A1b is the representation-learning bet; representations are more foundational than consolidation policy (which depends on representations to be smart about). H44 directly tests the wedge claim: do JEPA-shape auxiliary-loss-trained reps beat token-averaged baseline on tier-3 (cross-domain analogical) retrieval by ≥10pp.
- **Tractability**: HIGH. Pre-registered protocol exists at [2026-05-18-T_A1b-isolation-derisk](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md). Single GPU (RTX 2080 Ti feasible with encoder isolated). Weeks not months. Encoder + predictor in isolation — no LLM consumer in the loop.
- **Dependencies**: Pre-implementation work known and bounded — V-JEPA (Bardes 2024) + ICAE (Ge 2024) verbatim reads, training-corpus selection (Web-Claude flagged CoderForge / Scale-SWE / Nebius / SWE-ZERO + Project Gutenberg / BookCorpus / WildChat — needs verification), encoder/predictor architecture specs (dim, depth), hyperparameter sweep bounds, structural-pattern pairing list pre-registration. No upstream block.
- **Frontier-pacing**: HIGHEST risk. V-JEPA (Meta) is the public adjacent work; LLM-JEPA (Huang/LeCun/Balestriero 2025) explicitly noted "the lack of JEPA-style LLM is a testimony of the challenge in designing such objectives for language." The field IS moving on JEPA-style losses. If Meta or Anthropic publishes T_A1b-shape result on event-segmented language reps before we do, we lose the priority claim.

**#2 — H40 / K2+T_A3 isolation experiment.**
- **Scientific leverage**: HIGH. K2+T_A3 is the consolidation-policy bet on a distinct timescale (slow / cortical-analog) per [m17-jepa-reconciliation § Resolution](../open-question/m17-jepa-reconciliation.md). The publishable claim — *"schema-fit-modulated consolidation with continuous drift"* — is novel for AI agent memory.
- **Tractability**: MID. Memory-budget-bounded, not compute. Experiment design preserved inside H40 (Version A static-reference + Version B dynamic-reference, matched memory budget, dev/test threshold split). More moving parts than H44 (hot tier + cold tier + schema-fit signal proxy + baseline policies + downstream task probe + ordering-sensitivity probe), but no GPU-bound training.
- **Dependencies**: Independent of H44 per H40's Path B (use any reasonable predictor's prediction error as proxy fit signal; the architecture of K2 is what's tested, not the specific fit signal). Testable in parallel with H44 in principle; sequentially per the one-thread-at-a-time rule.
- **Frontier-pacing**: MID risk. Cog-sci-derived (Tse 2007 schema-mediated consolidation); not heavily explored as agent-memory architecture. Continual-learning has rate-modulation literature (per-task curriculum, meta-learned schedules) but not at agent-memory with explicit schema-fit signal.

**#3 — H42 / Learned salience function.**
- **Scientific leverage**: MID-HIGH. C primitive enables K2, K5, E2, R3 in the architecture per [caddy-architecture § (C) Salience signal](../concept/caddy-architecture.md#c-salience-signal). If solved, K2+T_A3 becomes more tractable (downstream consumers route through C). If rejected (LLM-call wins), the architecture pays an inference-cost tax — but doesn't fall.
- **Tractability**: HIGH. Testable on bolt-on prototype (no caddy required). Sub-100M param distillation of GPT-class importance judgments. Independent of T_A1b architecture.
- **Dependencies**: Independent of T_A1b. C is *structurally* a sub-output of T_A1b's loss per caddy-architecture, so in caddy form C rides T_A1b's training; standalone test (this hypothesis) is cheaper and front-runnable.
- **Frontier-pacing**: MID risk. Schaul 2016 PER and Aljundi 2019 MIR are precedents but in continual-learning RL contexts, not agent-memory. Direct agent-memory salience-function ablations not published by Mem0 / Letta / Zep.
- **Caveat**: H42 is *adjacent* to the tier-3-4 wedge — it's about cost/quality of a primitive, not the wedge capability itself. Strong on tractability and unblock-potential; weaker on direct goal-anchoring than H44/H40.

**#4 — H41 / Temporal-context retrieval.**
- **Scientific leverage**: MID. Tier-3-4 read-side primitive (R1 / M13). The architectural backbone for analogical retrieval on the read side; complements T_A1b's write-side representations.
- **Tractability**: MID. **Partial test already lives inside H44**: probe 3 (trajectory-state decodability) of the T_A1b isolation experiment tests whether the predictor's internal state encodes position-in-pattern decodably. Standalone Falkenberg-signature test requires more infrastructure (cross-session perturbation paradigm, continuity benchmark — neither exists off-the-shelf).
- **Dependencies**: Probe 3 of H44 partially covers it. Standalone test independent of K2.
- **Frontier-pacing**: LOW risk. TCM (Howard & Kahana 2002) is cog-sci-classic; agent-memory translations not done; not a hot ML topic in 2026.

**#5 — H43 / Soft-composition emergent construction.**
- **Scientific leverage**: HIGH for tier 4 (predictive). M16 reframing — the caddy's job is anticipation/construction, not retrieval. Architecturally critical for the strong reading of the wedge claim ("not just better retrieval — constructive memory").
- **Tractability**: LOW. Requires full caddy build (soft-composition AND hard-selection variants, co-trained end-to-end, comparable workloads, composition-score operationalization). Multi-quarter implementation.
- **Dependencies**: Depends on T_A1b (need representations to compose over). Depends on K2+T_A3 (need consolidated memory to compose). Cannot run before items #1–#2.
- **Frontier-pacing**: LOW-MID risk. Memorizing Transformer is partial precedent (soft-composition + co-training works for LM loss). M16 / constructive-memory framing is novel for AI; underlying mechanism (soft attention) is well-explored.

**#6 — H39 / Silent-state primitives.**
- **Scientific leverage**: LOW for tier 3-4 specifically. Silent-state addresses cross-session continuity, not analogical retrieval. S2 (silent state as separate op) was *prototype-dropped* per inspiration-not-blueprint (constraint, not insight). Re-promoting from the deferred state requires evidence that three-state architecture matters in caddy context — which is what H39 would test.
- **Tractability**: MID. Three-state implementation + cross-session benchmark with reactivation queries.
- **Dependencies**: Independent of T_A1b / K2.
- **Frontier-pacing**: LOW risk. Cog-sci novel (Josselyn 2020); AI translation not pursued by incumbents.
- **Note**: H39 may be a candidate for back-burner status rather than active queue. Re-evaluate after H44 + H40 land.

**#7 — K6 / Offline composition.**
- **Scientific leverage**: HIGH for tier 4 long-term (write-side construction via M14 SPW-R analog). But far downstream from current evidence base.
- **Tractability**: VERY LOW. Needs full caddy build + offline consolidation cycle + composition operator. No formalized hypothesis yet (K6 referenced in caddy-architecture but no H-page).
- **Dependencies**: Depends on T_A1b (representations), K2 (consolidation cycle), H43 (composition mechanism — if write-side composition is the same as read-side composition).
- **Frontier-pacing**: LOW risk.
- **Pre-work needed**: Formalize K6 as a falsifiable hypothesis before it can be dequeued.

### Goal-anchoring check

Each item ranked against *moves us toward demonstrating tier 3-4 retrieval via the caddy*:

- **Direct wedge contribution**: H44 (representation pathway to tier 3), H40 (consolidation-policy pathway to tier 3-4 stability), H43 (M16 anticipation/construction reading)
- **Architectural primitive enabling wedge**: H42 (salience signal C), H41 (read-side temporal-context primitive)
- **Architectural enrichment, weaker wedge tie**: H39 (cross-session continuity), K6 (write-side construction)

The top-2 are both direct wedge contributions and structurally distinct (CLS-theory-supported). #3-#4 are primitives the top-2 either consume or partially test. #5 is downstream of the top-2. #6-#7 are architectural enrichment.

### Robustness to H44's outcome

The queue is designed to be robust to H44's outcome (SUPPORTED or REJECTED):

- **If H44 SUPPORTED**: representation pathway has scientific footing. K2+T_A3 (#2) still needed for consolidation-policy pathway. H42 (#3) becomes more interesting (C as sub-output of T_A1b's loss can be tested in caddy form). H43 (#5) becomes load-bearing for tier-4 anticipation claim.
- **If H44 REJECTED**: representation pathway closes. K2+T_A3 (#2) becomes the **only** load-bearing pathway to tier 3-4 — promotes to single-bet status. H42 (#3) still independent. H43 (#5) deferred indefinitely (no representations to compose). The architecture pivots to consolidation-policy-as-wedge.

Either way, items #1 and #2 are the load-bearing pair. The ordering decision (H44 first, H40 second) is set by: (a) H44 is the cheapest representation-pathway test, (b) H44 has highest frontier-pacing pressure, (c) H44's result informs H40's experimental shape (specifically the schema-fit signal choice).

## Commitments

- **#1 is the current active research thread**: T_A1b isolation de-risk. Pre-implementation pre-work begins next session (V-JEPA + ICAE verbatim reads, training-corpus verification, architecture specs).
- **One thread at a time** per AJ. The queue is sequential, not parallel.
- **Re-evaluate the queue after each item lands.** Items #3–#7 may reorder based on what's learned from items #1–#2.
- **#6 (H39) and #7 (K6) are flagged for re-evaluation** before dequeue. H39 may move to back-burner status if cross-session continuity isn't the binding constraint in caddy context. K6 needs hypothesis formalization first.
- **Bolt-on hypotheses (H23–H38) are not in this backlog.** Those belong to Eira's commercial track; see coral for ownership. Items in the wiki under `hypothesis/` from that set are historical research that may or may not continue under Eira's roadmap.

## Reversibility

**Cheap.** This is an ordering decision over an existing research backlog. No implementations or hires are locked. Reversal triggers:

- **A new architectural insight materially changes the goal-anchoring picture** — e.g., a result that shows tier 3 is reachable through a different pathway not currently on the queue.
- **Frontier-pacing changes** — e.g., V-JEPA-on-language gets published, removing H44's priority claim; we accelerate H40 to grab the consolidation-policy publication first.
- **A dependency assumption breaks** — e.g., H40's Path B (proxy fit signal independent of T_A1b) turns out not to work; H40 then *depends* on H44 and the ordering becomes mandatory rather than chosen.
- **AJ's research focus shifts** — affordability or interest drives a different ordering.

The decision is held *until evidence inverts it*, not committed forever. After each item lands, the queue is re-evaluated explicitly.

## Related

- [caddy-as-research-program](./caddy-as-research-program.md) — the framing decision this ordering operationalizes.
- [tier-3-4-as-wedge](./tier-3-4-as-wedge.md) — the goal anchoring the ranking criteria.
- [caddy-architecture](../concept/caddy-architecture.md) — the architectural surface the backlog items map onto.
- [m17-jepa-reconciliation](../open-question/m17-jepa-reconciliation.md) — CLS-theory resolution that supports H44 + H40 as distinct load-bearing bets.
- [H44-T_A1b-cross-domain-transfer](../hypothesis/H44-T_A1b-cross-domain-transfer.md) — #1 in the queue.
- [H40-schema-fit-modulated-consolidation](../hypothesis/H40-schema-fit-modulated-consolidation.md) — #2 in the queue.
- [H42-learned-salience-function](../hypothesis/H42-learned-salience-function.md) — #3 in the queue.
- [H41-temporal-context-retrieval](../hypothesis/H41-temporal-context-retrieval.md) — #4 in the queue.
- [H43-soft-composition-emergent-construction](../hypothesis/H43-soft-composition-emergent-construction.md) — #5 in the queue.
- [H39-silent-state-primitives](../hypothesis/H39-silent-state-primitives.md) — #6 in the queue; flagged for re-evaluation.
- [2026-05-18-T_A1b-isolation-derisk](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md) — the protocol for item #1.

## Source archive

- AJ-Nils 2026-05-20 conversation: framing-shift to research-program (Step 1 refactor landed); Step 2+3 (enumerate + stack-rank) executed same session.
- Backlog enumerated by reading every PROPOSED hypothesis page in `hypothesis/` + the four T4 commitments in [caddy-architecture](../concept/caddy-architecture.md). Bolt-on / commercial-track hypotheses (H23–H38 cluster, minus H39 onwards which are cog-sci-derived) excluded from this backlog per [caddy-as-research-program](./caddy-as-research-program.md) commercial-track decoupling.
