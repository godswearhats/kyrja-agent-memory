---
type: concept
name: Caddy vs bolt-on — honest capability comparison within the discrete-unit family
status: living
last_ingested: 2026-06-12
sources: [../source/dong-2025-norman-episodic.md, ../source/wu-2022-memorizing-transformer.md, ../source/fountas-2024-em-llm.md, ../source/wayne-2018-merlin.md, ../source/borgeaud-2022-retro.md]
epistemic_tags: [asserted, speculated]
tags: [path-decision, caddy, bolt-on, comparison, discrete-unit-family]
---

## Purpose

`[ASSERTED]` This page is the honest within-family comparison between [caddy](./caddy.md) and [bolt-on memory](./substrate-as-memory.md) as candidate implementations of the [discrete-unit memory architecture](./discrete-unit-memory-architecture.md). It walks each cog-sci-derived design idea on its own merits and identifies which capabilities are *genuinely* exclusive to one path versus which are family-level (achievable by both).

The page exists because the [mechanism-gap-matrix](./mechanism-gap-matrix.md) walkthrough (M01–M17, completed 2026-05-17) introduced two methodological biases that make its caddy-vs-bolt-on grading unreliable as a decision input:

1. **Caddy was being designed alongside being graded.** The 2026-05-17 reconciliation pass added M14–M17 findings *into* the caddy architecture before the caddy column was graded. The caddy column therefore reflects what we decided to put in caddy, not an independent test of caddy.
2. **Bolt-on was graded against current incumbents, not a bolt-on that adopts the cog-sci design ideas.** Mem0, Letta, Zep, Cognee — none of these implement event segmentation, schema-fit consolidation, salience-modulated decay, or temporal-context binding. Grading bolt-on at this baseline lets caddy beat a strawman.

The [caddy](./caddy.md) page already concedes the honest version of this distinction (its own line 82): *"the caddy is a refined bolt-on with tighter integration on the surviving axes, not a genuinely separate paradigm."* This page is that concession worked through in detail.

## What we're comparing

`[ASSERTED]` Both paths are members of the [discrete-unit memory architecture family](./discrete-unit-memory-architecture.md). Both could in principle implement the cog-sci-derived mechanism set. The comparison is between two within-family implementations:

- **Caddy-with-cog-sci-design-ideas.** Co-trained sidecar memory module with activation-injection interface, learned consolidation policies, learned representation space, auxiliary world-model loss on memory reps. Specified in detail at [caddy-architecture](./caddy-architecture.md).
- **Bolt-on-with-cog-sci-design-ideas.** External memory store (vector DB, KG, or structured DB) accessed by the consumer LLM via prompt injection, but with learned sub-systems for event segmentation, schema-fit consolidation, salience-modulated decay, temporal-context binding, and pattern-completion retrieval. *Not* what current incumbents ship.

The current-incumbent bolt-ons (Mem0, Letta, etc.) are not what's being compared — they're the strawman the matrix walk implicitly graded.

## The eighteen design ideas

`[ASSERTED]` For each cog-sci-derived design idea, the question is: (a) is each path capable of implementing it, and (b) what is the cost or fidelity difference?

| # | Design idea (cog-sci source) | Bolt-on | Caddy | Notes |
|---|---|---|---|---|
| 1 | **Surprise-based event segmentation** ([M16](./mechanism-gap-matrix.md), Norman N2) | ✓ | ✓ | Bolt-on: small surprise model scores per-token NLL; chunk at peaks. Caddy: same primitive, lives inside E1. No structural advantage either way. |
| 2 | **Promiscuous admission within events** (M17 inversion) | ✓ | ✓ | Bolt-on: write everything to a hot vector store; consolidator runs in background. Caddy: hot tier accepts; K5 demotes. Bolt-on actually *easier* — no co-training required. |
| 3 | **Conjunctive representation** (what×where×when×salience, M11) | ✓ | ✓ | Bolt-on: store `(text, embedding, timestamp, source, salience, schema-tag)` per item. [Zep](../incumbent/zep.md) already does temporal+graph. Caddy: learned encoder bakes the binding into a single vector. Caddy more compact; bolt-on more inspectable. |
| 4 | **Temporal context binding** (TCM, Norman N4) | ✓ | ✓ | Bolt-on: maintain drifting context vector; attach to each write; retrieve with current context vector as part of cue. Novel for current incumbents but engineering-doable. Caddy: same operation, learned. |
| 5 | **Pattern-completion retrieval** (R2, modern Hopfield) | ◐ | ✓ | Bolt-on: ANN + reranker + softmax over candidates *approximates* pattern completion but always returns stored items. Caddy: modern Hopfield over learned keys can return novel compositions in value-space. **Caddy advantage — but only if soft composition is exposed downstream (see #11).** |
| 6 | **Schema-fit consolidation** (K2, Tse 2007) | ✓ | ✓ | Bolt-on: learned scorer + LLM-based summarisation triggers when schema-fit is high. Caddy: K2 trains the consolidator end-to-end. Caddy gets the bet (#13) for free; bolt-on may lose signal at sub-system handoffs (the integration-depth argument from the M11 refinement). |
| 7 | **Salience-modulated decay** (K5, M17) | ✓ | ✓ | Bolt-on: per-item TTL scored by learned salience function; periodic re-score. Caddy: same operation. No structural advantage; [H42](../hypothesis/H42-learned-salience-function.md) is identically falsifiable on both. |
| 8 | **Discrete addressable storage** (S1) | ✓ | ✓ | Family precondition. Both members. No advantage. |
| 9 | **Multi-tier storage with promotion/demotion** | ✓ | ✓ | Bolt-on: hot in-memory cache → vector DB → archived. Caddy: same tiering. No structural advantage. |
| 10 | **Cross-session persistence** | ✓ | ✓ | Trivially solved by both. No advantage. |
| 11 | **Soft composition / emergent construction** ([H43](../hypothesis/H43-soft-composition-emergent-construction.md), M16 strong reading) | ✗ | ✓ | Bolt-on retrieves text and concatenates into the prompt — *hard selection by construction*. To get soft composition you'd have to inject blended vectors into hidden states, which makes you a caddy. **Genuine caddy-only.** |
| 12 | **Activation injection (vs text injection)** | ✗ | ✓ | Bolt-on writes to the prompt; caddy writes to hidden states. Activation injection requires the consumer to be modified. **Genuine caddy-only — and #11 depends on it.** |
| 13 | **Auxiliary world-model loss on memory reps** (T_A1) | ✗ | ✓ | Bolt-on's "memory" is text-or-embedding produced by a frozen embedder; no learned-representation space to train. Caddy has its own representation space. **Genuine caddy-only — and this is the central research bet.** |
| 14 | **End-to-end gradient through memory** | ✗ | ✓ | Bolt-on's vector store is non-differentiable; gradient stops at the embedder. Caddy: gradient flows from task loss through retrieval through storage to encoder. **Genuine caddy-only.** |
| 15 | **Silent state larger than read interface** (M06, C1) | ◐ | ✓ | Bolt-on can store more text than it retrieves, but everything in store is exposable as text. Caddy can hold internal representations that have no surface form — the "silent capacity" the analogy names. Caddy advantage if you care about compression / privacy / pattern-completion. |
| 16 | **Co-trained shorthand** (Q_mem/K_mem alignment) | ✗ | ✓ | Bolt-on can fine-tune an embedder to align with a retriever's expectations, but the consumer LLM's queries aren't part of the loop. Caddy: the LLM's query head is co-trained with the caddy's key space. **Genuine caddy-only.** |
| 17 | **Reconsolidation / read-as-write** (R5) | ✓ | ✓ | Already demoted as a biology constraint, not an insight (see [caddy § R5 demotion](./caddy.md)). Both can re-encode on retrieval. No advantage. |
| 18 | **Offline composition / vicarious search** (K6, M14 SPW-R) | ✓ | ✓ | Both can run background processes that compose new memories from old ones. Bolt-on stores the composition as new text; caddy stores it as new latent. No structural advantage; caddy compresses better. |

## The caddy-only set reduces to one architectural commitment plus one bet

`[ASSERTED]` Of the eighteen design ideas, **six are genuinely caddy-only** (#5, #11, #12, #13, #14, #16). The other twelve are family-level — bolt-on can do them with sufficient learned sub-systems.

The six caddy-only properties are not independent: #11, #12, #14, #16 are all consequences of activation injection plus co-training. #5 (pattern completion in value-space) is meaningful only because of #11 (soft composition). #15 (silent state) is a property of the encoder's representation space.

`[ASSERTED]` The caddy-only set therefore reduces to:

- **One architectural commitment:** activation injection + co-training. The consumer LLM is modified to accept hidden-state injection from the memory module, and the two are co-trained.
- **One research bet (T_A1):** does an auxiliary world-model-style loss on the memory representations add signal beyond LM loss alone, at experiential-memory scale?

`[ASSERTED]` ICAE (Ge et al. 2023, [verbatim read](../source/ge-2024-icae.md)) demonstrates a **same-class-different-shape** version of the auxiliary-loss benefit at LLM scale: dual token-space objective (AE reconstruction + LM continuation) via a frozen decoder, on context-compression scope. ICAE's loss is *not* a representation-space loss on the memory slots — both terms are next-token CE at the decoder output (§2.2.1, §2.2.2), and anti-collapse comes from "frozen decoder must reconstruct text," not the BYOL triad. **Implication:** the auxiliary-loss-helps-at-LLM-scale signal at the family level comes from a different mechanism family than T_A1b inherits from (V-JEPA-style representation-space feature prediction). No same-shape demonstration exists at LLM scale; that gap is T_A1b's load-bearing extrapolation. See [H44 § Loss-family distinction](../hypothesis/H44-T_A1b-cross-domain-transfer.md#loss-family-distinction).

## Bolt-on advantages the matrix walk underweighted

`[ASSERTED]` These are real and have not been adequately accounted for in the caddy-vs-bolt-on framing:

1. **Debuggability and auditability.** Bolt-on memory is text or structured records — you can read what the system "remembers." Caddy memory is learned representations — opaque without a decoder. For an enterprise customer who needs to answer "what does the system know about me," this is a real product-strategy advantage.
2. **Modularity and component swap.** Bolt-on lets you change the vector DB, the embedder, the consumer LLM, the retrieval policy independently. Caddy is locked into co-training: change the consumer, retrain the caddy.
3. **Deployability against frontier LLMs.** Bolt-on works with Claude / GPT-5 / Gemini via API today. Caddy needs an LLM you can co-train against — meaning open-weights, meaning ~3–4 generations behind frontier on capability. This is a *strategic positioning* cost, not just an engineering cost.
4. **Privacy and governance.** Deletion-on-request is genuinely harder when "the memory of user X" is distributed across learned representations. Bolt-on: delete the row, done.
5. **Iteration speed.** A learned bolt-on policy can be retrained quickly on a stored inspectable corpus. Caddy iteration cycle requires co-training, which is expensive and slow.
6. **Training cost.** Caddy requires ~4% of pretraining compute ([Memorizing Transformer §4.5](../source/wu-2022-memorizing-transformer.md)) *plus* the auxiliary-objective work. Bolt-on can be developed in production with no large training run.
7. **Failure-mode profile.** Bolt-on fails by retrieving the wrong stored fact. Caddy can fail by *constructing memories that were never stored* (hallucinated composition from soft attention over blurred keys — H43's downside; see [pattern-separation](./pattern-separation.md) for the architectural prerequisite that mitigates this). The latter is harder to detect, debug, or guard against.
8. **Norman-rubric reachability through engineering.** The M11 refinement showed that bolt-on with four learned sub-systems (embedding, field structure, salience, retrieval) can in principle implement the biological mechanism set. The gap between [Mem0 at 0/5](../incumbent/mem0.md) and a hypothetical bolt-on at 3.5/5 on the [Norman rubric](./norman-rubric.md) is *integration work*, not architecture. **This is the bolt-on competitive-threat argument that has not been adequately accounted for.**

> **2026-06-12 update — the field is building this shape.** The RL-memory cluster (all four full-read verified: [Memory-R1](../source/yan-2025-memory-r1.md), [Memory-R2](../source/yan-2026-memory-r2.md), [Mem-α](../source/wang-2025-mem-alpha.md), [AgeMem](../source/yu-2026-agemem.md)) *is* bolt-on-with-learned-controller in the wild: learned write policies (and in AgeMem, learned STM control) over text stores, trained by RL, beating prompted incumbents — Mem-α's RL-tuned 4B beats gpt-4.1-mini *on the same memory framework* (their Table 3). The "hypothetical bolt-on with learned sub-systems" of argument #8 is no longer hypothetical for the write/consolidation sub-system; it remains unbuilt for segmentation, temporal binding, and pattern-completion retrieval (retrieval is untrained in all four). Caddy-only rows #11–#16 are untouched by the cluster — all four are text-injection systems.

## The honest reduction

`[ASSERTED]` The caddy-vs-bolt-on decision reduces to **one architectural commitment plus one bet**:

- **If T_A1 pays out**, caddy strictly dominates bolt-on on the Norman rubric, and the [post-Norman gap](./norman-rubric.md) becomes a real architectural moat. The caddy-only properties (#11–#14, #16) are activated, and bolt-on's cost-leg advantages (debuggability, modularity, deployability) become tradeoffs the customer accepts for capability.
- **If T_A1 doesn't pay out**, caddy collapses to "Memorizing Transformer plus extra machinery," competing against a frontier-API-bound bolt-on that has lower training cost and better debuggability. The cost-leg advantages of bolt-on become structural problems for caddy.

`[ASSERTED]` This is the *single* falsifiable bet that decides the path. Every other architectural choice is downstream of it.

## The decision criterion

`[ASSERTED]` The right framing is not "caddy or bolt-on" — it is **"how much research risk on T_A1 are we taking before committing to the full caddy build?"**

Three options:

1. **Commit to caddy now.** Maximum upside if T_A1 works; maximum sunk cost if it doesn't. Multi-quarter build before the central assumption is tested.
2. **Pursue bolt-on-with-cog-sci-design-ideas as the primary build.** Lower research risk; the post-Norman gap is still there to fill (no incumbent implements the cog-sci ideas); leaves caddy as a research target. Engineering-heavy; loses the structural moat caddy offers if T_A1 works.
3. **Front-load T_A1 as a small-scale falsification experiment.** Build the smallest thing that tests T_A1 — frozen base + light learned encoder + auxiliary loss on a small-scale memory-augmented LM. If the auxiliary loss adds signal over LM-only at small scale, the representation pathway through the caddy has scientific footing.

`[ASSERTED]` Option 3 is the scientifically disciplined choice. It costs perhaps 4–8 weeks of work versus the multi-quarter caddy build, and it answers the question the representation pathway is predicated on.

> **2026-05-20 framing update.** Per [caddy-as-research-program](../decision/caddy-as-research-program.md), this is no longer a commercial-pivot question. The commercial track is **bolt-on, owned by Eira** (Eira's coral folder) — Option 2 in commercial form is happening on a parallel track, decoupled from this comparison. The caddy is a research program. The comparison below is now **scientific**: which research direction produces the most knowledge per unit budget, and which architectural pattern best demonstrates tier 3-4 retrieval. The "if T_A1b fails, pivot to bolt-on" logic that previously framed this page assumed the caddy was both research bet and product. With caddy as research-only, T_A1b failing is *data* about the representation pathway — not a commercial pivot trigger.

## Recommendation (AJ-ratified 2026-05-17, sharpened 2026-05-18, reframed 2026-05-20 as research-program)

`[ASSERTED]` **Go caddy as a research program. The first deliverable remains the T_A1b falsification experiment at small scale.**

**2026-05-18 sharpening.** T_A1 reformulated as **T_A1b** (JEPA-style predictive loss on event-segmented memory reps, not autoencoder reconstruction). The reformulation is driven by [tier-3-4-as-wedge](../decision/tier-3-4-as-wedge.md): the load-bearing capability is cross-domain analogical retrieval (tier 3 in [memory-retrieval-tiers](./memory-retrieval-tiers.md)), which autoencoder reconstruction does not target. The falsifiable form is [H44](../hypothesis/H44-T_A1b-cross-domain-transfer.md) (T_A1b reps must beat token-averaged baseline by ≥10pp on cross-domain analogical retrieval); the protocol is [2026-05-18 isolation de-risk](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md), with the binary-verdict probe methodology pre-registered in [2026-05-20-probe-2-test-set-design](../experiment/2026-05-18-T_A1b-isolation-derisk/probe-2-test-set-design.md).

**2026-05-20 reframing.** Under [caddy-as-research-program](../decision/caddy-as-research-program.md): the architecture has **two active load-bearing T4 research targets**, not one — T_A1b (representation pathway) and K2+T_A3 (consolidation-policy pathway). The "single bet that decides the path" framing in earlier versions of this page assumed a single product wedge; with commercial decoupling, the architecture is held up by two distinct falsifiable bets on distinct mechanisms (CLS-theory-supported, see [m17-jepa-reconciliation](../open-question/m17-jepa-reconciliation.md)). Both decide its scientific footing; both can fail or succeed independently. Ordering between them is set by a forthcoming stack-rank exercise.

Concretely (T_A1b first, per sanity-prediction in [caddy-as-research-program § Commitments](../decision/caddy-as-research-program.md#commitments)):

- Train encoder + predictor in isolation with BYOL/JEPA-style loss (EMA target + stop-gradient + cosine)
- Probe trained reps for cross-domain analogical retrieval vs. token-averaged baseline
- If beat by ≥10pp: the representation pathway has scientific footing; continue to caddy build incorporating the result
- If lose-to-or-tie or beat by <5pp: T_A1b is REJECTED, the representation pathway closes. The K2+T_A3 pathway (H40) remains an independent research target; the wedge claim falls back to the consolidation-policy pathway and stack-rank re-evaluates.
- Probe trained reps for trajectory-state decodability (sub-claim test for [multi-field-memory-unit](../decision/multi-field-memory-unit.md) trajectory_state field)

`[ASSERTED]` Bolt-on-with-cog-sci-design-ideas remains a structurally real path, and on the commercial side it *is* the path (Eira). On the research side, it stays as a contrastive thought-tool — the within-family comparison this page articulates — but is no longer a fallback target for the research program. Negative result on the caddy research informs Eira's commercial direction; positive result strengthens the case for eventual commercial pivot back to caddy in v2/v3.

## Scope limits

- **This page is the comparison, not the experiment.** The T_A1 falsification protocol is forward work; the design is provisional here and should be promoted to a separate `experiment/` page once specified.
- **The comparison is within the discrete-unit family.** Continuous-update substrate (Hope-shape) is outside the family entirely and not part of the comparison; see [discrete-unit-memory-architecture § non-members](./discrete-unit-memory-architecture.md).
- **The comparison is the current best honest reading.** It will need revision if (a) T_A1 falsification produces a result, (b) a bolt-on-with-cog-sci-design-ideas system is demonstrated at the Norman-rubric level, or (c) one of the family-level capabilities (#1–#10, #17, #18) turns out to be structurally harder for one path than currently thought.

## Related

- [[caddy]] — canonical caddy definition; this page is its honest comparison against the within-family alternative.
- [[caddy-architecture]] — the detailed caddy spec; T_A1 is the load-bearing T4 there.
- [[discrete-unit-memory-architecture]] — the family the comparison is within. The M11 refinement that motivated this comparison originated there.
- [[substrate-as-memory]] — bolt-on memory's framing; this page argues bolt-on-with-cog-sci-design-ideas is a real competitive option, not just the current-incumbent shape.
- [[mechanism-gap-matrix]] — the matrix walk whose caddy column motivated this page's honest re-grading.
- [[norman-rubric]] — the external evaluation framework against which both paths will be measured.
- [[H42-learned-salience-function]] — falsifiable claim that applies identically to both paths.
- [tier-3-4-as-wedge](../decision/tier-3-4-as-wedge.md) — sharpens "the single bet" framing; tier 3-4 is the wedge target.
- [memory-retrieval-tiers](./memory-retrieval-tiers.md) — capability taxonomy that operationalizes the wedge claim.
- [H44-T_A1b-cross-domain-transfer](../hypothesis/H44-T_A1b-cross-domain-transfer.md) — the falsifiable form of T_A1b.
- [2026-05-18-T_A1b-isolation-derisk](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md) — the pre-registered de-risk protocol.
- [[H43-soft-composition-emergent-construction]] — falsifiable claim that applies only to caddy.
- [[memory-caddy]] — the open question the comparison feeds back into.

## Source archive

- AJ–Nils conversation 2026-05-17 (post-matrix-walk closeout). The methodology critique ("matrix walk underweighted bolt-on; inaccuracies in capabilities column") originated with AJ; the eighteen-design-ideas walk and the one-commitment-plus-one-bet reduction were produced jointly during the conversation.
- The M11 cross-examination of 2026-05-15 (logged in [discrete-unit-memory-architecture § Refinement (M11 walkthrough)](./discrete-unit-memory-architecture.md#refinement-m11-walkthrough-2026-05-15-integration-depth-not-capability-binary)) is the prior precedent for the "bolt-on can in principle implement the biological mechanism set" claim.
