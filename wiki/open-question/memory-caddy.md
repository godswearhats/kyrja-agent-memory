---
type: open-question
name: Memory caddy — does the caddy concept survive empirical scrutiny against bolt-on baselines?
status: OPEN
last_ingested: 2026-05-21
sources: [../source/wayne-2018-merlin.md, ../source/borgeaud-2022-retro.md, ../source/honcho-docs.md, ../source/dong-2025-norman-episodic.md, ../source/hassabis-2026-memory-bottleneck.md, ../source/spens-2024-hippocampal-rag.md, ../source/pan-2025-mega.md, ../source/cetin-2024-namm.md, ../source/fountas-2024-em-llm.md, ../source/lampinen-2025-latent-learning.md, ../source/engramme-press-corpus.md]
epistemic_tags: [asserted, speculated]
tags: [path-decision, memory-architecture, caddy, consumer-reframe, distributed-systems, aj-originated, matrix-walkthrough-pattern, merlin-investigation]
---

> **Status note (2026-05-20):** Per [caddy-as-research-program](../decision/caddy-as-research-program.md), the caddy is a research program (commercial track is Eira's bolt-on, decoupled). The architecture has **two active load-bearing T4 research targets**: T_A1b (representation pathway, [H44](../hypothesis/H44-T_A1b-cross-domain-transfer.md), de-risked by [2026-05-18 isolation experiment](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md), probe-2 binary-verdict methodology in [2026-05-20-probe-2-test-set-design](../experiment/2026-05-18-T_A1b-isolation-derisk/probe-2-test-set-design.md)) and K2+T_A3 (consolidation-policy pathway, [H40](../hypothesis/H40-schema-fit-modulated-consolidation.md), de-risk protocol preserved in H40). Ordering between them is set by the stack-ranked queue in [decision/research-backlog-stack-rank](../decision/research-backlog-stack-rank.md). This open question's "live empirical bet" is two bets, not one — and both are part of the caddy's scientific footing.

> **Canonical concept definition:** see [concept/caddy](../concept/caddy.md) for the architectural definition, five commitments, three within-family axes, and the caddy/golfer analogy. This page is the live *open question* — whether the caddy's distinctive bets (especially commitment 5: auxiliary objective beyond consumer task loss) survive empirical scrutiny against bolt-on baselines.
>
> **Naming note (2026-05-15):** AJ ratified "caddy" / "caddy model" / "memory caddy" as the canonical Kyrja term for what this doc previously called "caddy." The file rename from `memory-caddy.md` to `memory-caddy.md` landed 2026-05-16. Past timestamped artifacts (log entries, lint reports, archived docs) preserve the historical term.

## The question

AJ proposed (2026-05-15, mid-M02 digest) a reframing of the substrate-vs-bolt-on path question, plus a candidate caddy architecture:

**Claim 1 — consumer reframe.** The substrate vs bolt-on axis is more usefully named by *who consumes the memory at retrieval time*:
- **Memory-for-the-model** (was: substrate) — read by the LLM's own forward pass; lives in the model's representations/weights.
- **Memory-for-the-agent** (was: bolt-on) — read by the agent's software loop; lives outside the model and is injected into the prompt.

Promoted into wiki vocabulary 2026-05-15 as [concept/memory-consumer-axis](../concept/memory-consumer-axis.md). The concept page is the canonical entry for the framing; the rest of this open question is about claims 2 and 3.

**Claim 2 — distributed-systems framing of bolt-on.** Today's bolt-on memory is descriptively a distributed system with the LLM as a stateless coprocessor. Vector DB (storage), embedding (LLM), retrieval scoring (software), admission (LLM), consolidation (LLM), conflict resolution (LLM) — orchestrated by the agent harness. This inherits every hard distributed-systems problem (consistency, ordering, partitions, schema evolution) *plus* the new problem that one of its services is non-deterministic. Current products are written by ML people, not distributed-systems people; the WAL / CRDT / MVCC toolkit isn't fully landed.

**Claim 3 — a caddy.** What if the right thing to build is a *separate model* whose entire job is being a queryable memory layer, accessed by the agent like a microservice?

| Path | Memory lives where | Memory is a... |
|---|---|---|
| Bolt-on | Outside primary LLM | Datastore (vector DB, KG, docs) |
| Substrate | Inside primary LLM | Learned weights/states of the LLM itself |
| **Caddy** | Outside primary LLM | **A separate model — own training, own internal representations, own update policy — accessed via API** |

This is meaningfully distinct from substrate (which puts memory *in* the primary LLM) and from bolt-on (which makes memory a non-learned datastore).

## Why it matters

If claim 3 is real and new, it changes the [path-decision](../NOW.md). It's not "pick substrate or bolt-on"; it's an additional leaf that may dominate both:

- The memory model can be **specialized + small** (doesn't need 70B params — needs good encoding, retrieval, consolidation).
- It can be **biologically faithful** in ways retrofitting the primary LLM struggles with. CLS / replay / schemas / reconsolidation become the memory model's job, not sidecar mechanisms ([[mechanism-gap-matrix]] M03-M13 become design targets, not adaptation problems).
- **Decouples memory from generation** — swap primary LLM (Sonnet → Opus → GPT-5 → ...) without losing memory.
- **Admission / consolidation become learned policies**, not LLM-call heuristics over an unlearned store.

The consumer reframe (claim 1) is also worth promoting into wiki vocabulary regardless of whether claim 3 survives, because it sharpens the existing axis.

**2026-05-18 wedge sharpening.** The question now has a concrete load-bearing test: [H44 — T_A1b cross-domain transfer](../hypothesis/H44-T_A1b-cross-domain-transfer.md), de-risked by [2026-05-18 isolation experiment](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md). The capability the caddy claims is reframed via [memory-retrieval-tiers](../concept/memory-retrieval-tiers.md): tier 3-4 (analogical and predictive retrieval) is what makes the architecture earn its existence; tier 1-2 is preserved as table-stakes side-effect via the [multi-field-memory-unit](../decision/multi-field-memory-unit.md) commitment. The path-decision is captured in [tier-3-4-as-wedge](../decision/tier-3-4-as-wedge.md). The question status remains OPEN until the de-risk experiment lands.

## Matrix-walkthrough findings (2026-05-15)

A pattern emerged during the [[mechanism-gap-matrix]] walkthrough. For each of four consecutive biological mechanisms (M03, M04, M05, M06), the caddy resolves frictions that exist for both bolt-on and substrate paths. The frictions differ per row; the resolution pattern is the same.

### M03 — Consolidation operator

AJ corrected an initial framing that RAG-based systems do "no consolidation." They do consolidate — Mem0 extracts facts, Cognee builds KGs, Zep maintains a temporal KG via Graphiti, Letta self-edits core memory. But the consolidation is **unlearned** (LLM call + structured store) and produces **static artifacts** (no re-consolidation loop — once a fact is written, it sits).

The matrix's M03 RAG column should be updated from ❌ to ⚠ with rationale: "implements consolidation, but target is a non-substrate store and the consolidation policy is unlearned." Pending next matrix-update pass.

**Caddy framing:** consolidation is a *learned policy* in the memory model itself, not LLM-call-as-coprocessor producing static structured artifacts. The sharpest articulation of what the caddy buys: learned-vs-unlearned integration.

### M04 — Selective experience replay

Prioritized Experience Replay (Schaul 2016) exists in RL and is mature ML toolkit, but hasn't crossed into LLM agent memory. The structural mismatch: **RL's slow store is trainable; LLM agents' slow store (frozen pretrained LLM) is not.** PER without a trainable target is just sampling order — no gradient destination, no point.

**Caddy framing:** the caddy provides a trainable target *by construction*. PER and the broader RL replay-buffer toolkit (importance sampling weights, n-step returns, distributed replay buffers like Ape-X) have somewhere to land. The reason PER hasn't crossed over isn't difficulty — it's that no existing AI memory architecture offers it a trainable target cheaply. Bolt-on has none. Substrate has one but the cost of updating it is prohibitive and the safety story (every replay risks breaking unrelated capabilities) is messy.

### M03/M04 design fork (online vs offline vs selective-replay)

The [online-vs-offline-consolidation](./online-vs-offline-consolidation.md) fork's framing changes under claim 3. If the three regimes apply to a small specialized memory model rather than to the primary LLM:
- Selective-replay (the biologically faithful regime, currently with zero implementations) becomes tractable — a memory model can afford the replay overhead the primary LLM can't.
- The substrate path's "modify the primary LLM" cost ceiling disappears for the memory model.

The biologically faithful regime, which is research-not-product for the substrate path, becomes the *natural* choice for the caddy.

### M05 — Schema-fit rate modulation

Three-way comparison:
- **Bolt-on:** schema-fit is easy (explicit schema in the KG / fact store / vector collection structure) but integration is unlearned.
- **Substrate:** schema-fit is hard (implicit schema in weights/activations; must be inferred via signals like perplexity, activation overlap, gradient alignment, MoE routing density), and integration is blocked by the frozen-LLM problem.
- **Caddy:** schema-fit is *both explicit (the memory model's design includes it) and learned (the integration policy is trainable)*.

The memory model has its own learned representation space. The encoder produces both (a) the representation and (b) a calibrated novelty score. The novelty score is part of the memory model's training signal — you train it to produce well-calibrated novelty scores. The score gates the update rate inside the memory model. Schema-fit becomes a **first-class architectural property**, not a retrofit.

### M06 — Silent engrams

Three-way comparison:
- **Bolt-on:** hard (vector DBs are exhaustive — every entry is reachable by similarity search; no "dormant tier" naturally exists).
- **Substrate:** hardest (no "stored but silent" state in a frozen LLM — information either affects the forward pass or it doesn't; introducing a dormant weight subspace is research-not-product).
- **Caddy: cleanest fit.** A memory model can have **internal state larger than its observable output channel**. Dormant representations live in the latent space; cues activate them through pattern completion. DNC/NTM/Memory Networks already explored this as an architectural primitive. The caddy inherits the primitive; the substrate path would have to invent it inside a frozen LLM.

This is arguably the strongest "caddy resolves what substrate can't" example in the matrix so far.

### M06 advantage analysis

Of the four engineering arguments for why biology evolved silent engrams (decoupling storage from retrieval, catastrophic-interference avoidance, cue-gated access, reconsolidation as opportunity), **decoupling storage durability from retrieval availability** is the most caddy-relevant. A separate memory model with a service API gives you storage and retrieval as **independent failure domains by construction** — the other two architectures couple them (vector DB stores + similarity retrieves; frozen LLM stores in weights + forward pass retrieves; both fail or both succeed).

### Cumulative pattern

Across four consecutive matrix rows (M03 → M06), the caddy resolves a friction that exists for *both* other paths. The frictions are different in each row (consolidation policy unlearned, no trainable target for replay, schema-fit hard to measure or unlearned, no architectural primitive for silent storage), but the resolution pattern is the same: **the caddy's architectural choices give the biological mechanism a natural home.**

This is starting to look like more than coincidence.

**Working hypothesis:** the biological-shape mechanism set is genuinely easier to instantiate in a separate-memory-model architecture than in either of the existing two paths.

**Falsification test:** continue the matrix walk (M07-M13). If the caddy stops resolving frictions, or if some mechanism is *harder* to instantiate in the caddy than in the other two, the pattern was selection bias on the early rows. If the pattern holds, the caddy moves from "intriguing speculation" to "the path with the strongest biological mapping" — which would change Kyrja's strategic stance materially.

### Required design properties (cumulative)

What the matrix walk is collectively saying a memory model must support, if it is to instantiate the biological mechanism set:

1. **Learned consolidation policy** (M03) — not LLM-call-as-coprocessor producing static artifacts; the integration step is trained.
2. **Trainable internal state** (M04) — gradient destination exists; replay-style techniques have somewhere to land.
3. **Schema-fit measurement and rate modulation** (M05) — explicit novelty score in the architecture, well-calibrated, gates update rate.
4. **Dormant representations + cue-driven activation** (M06) — internal state larger than observable output; pattern completion as the retrieval primitive, not similarity search.
5. **Decoupled storage and retrieval** (M06) — independent failure domains; storage durability ≠ retrieval availability.

**Status of the Honcho prior-art check (added 2026-05-15 after the parallel side-quest session):** Honcho re-ingest with verbatim verification was completed in the side-quest window earlier the same day. Findings: Honcho is **text-out** (`.chat()` returns prose; Representation endpoints return `string` per Python SDK v2.0.0; `get_context()` returns curated text context). Plastic Labs trains custom models (Neuromancer XR — fine-tuned Qwen3-8B), but at the **depth-0-1 rung** of the substrate-depth ladder — ingestion-time conclusion extraction with text outputs. None of the five required properties above are satisfied by Honcho. **The *outside-LLM × memory-for-the-model* cell of the consumer-axis 2×2 remains empty.** Full Honcho findings: [source/honcho-docs.md](../source/honcho-docs.md), [incumbent/honcho.md](../incumbent/honcho.md).

### The family-level reframe (added 2026-05-15 after M08 + eBay-patents reading)

`[ASSERTED]` AJ pulled on the matrix walkthrough's cumulative pattern mid-M08 and surfaced a sharper reading.

The earlier framing — "the caddy resolves frictions that exist for both other paths" — risks attributing a generic architectural advantage to a specific implementation route. The sharper reading: the resolution pattern is **discrete-unit-architecture-specific**, not caddy-specific. Both bolt-on and caddy are members of the same architectural family ([[discrete-unit-memory-architecture]]); continuous-update substrate (Hope-shape) is not.

Two pieces of evidence:

1. **AJ's eBay patents** ([WO 2018/191879 A1](https://patents.google.com/patent/WO2018191879A1) and [US 10,691,485 B2](https://patents.google.com/patent/US10691485B2)) implement the M03/M07/M08 architecture at production scale, in 2017-2018, for a *bolt-on shape* (stream + aggregating cache + transaction log + acknowledgement, not a memory model). The same architecture works for bolt-on memory. It just hasn't been combined with learned policies yet.
2. **The patent architecture doesn't translate to substrate** because substrate (in its mainstream continuous-gradient flavor) lacks the three required properties: discrete identifiable units, separate addressable store, and explicit consolidation events. Biology has all three. Bolt-on has all three. Caddy can have all three. Hope-shape substrate has none.

**Implication:** the matrix walkthrough was producing evidence for *the discrete-unit family* over *continuous-update substrate*, not for *caddy* over *bolt-on*. The caddy is differentiated within the family by its learned-policies-plus-separate-addressable-model-state combination — but the family-level architectural advantage is shared with bolt-on.

For Kyrja's path-decision, the question collapses:

- **Substrate (continuous-update mainstream)** is a thought-tool, not a product path — structurally unassailable for a startup without frontier-lab credibility and deep pockets.
- The real question is **which discrete-unit family member, with which learned policies, at what development cost**.

The required-design-properties list above is still load-bearing, but now reads as **what the caddy would do *within* the family**, not what makes the caddy a separate family.

See [[discrete-unit-memory-architecture]] for the full family definition, membership table, and the eBay-patents-as-precedent mapping.

### M11 walkthrough — schema induction, integration depth, biological priors (2026-05-15)

`[ASSERTED]` The M11 walkthrough (catastrophic interference avoidance via interleaved learning, McClelland 1995) refined the family-level reframe and surfaced two new load-bearing observations for the caddy question.

#### Hot store as training-data source for the cold store

AJ-originated reframing of what the consolidation channel actually does. The hot store is not a temporary buffer flushing to cold storage; it is the **training-data source** that generates the cold store's structure. Cold storage learns from what gets replayed, in what order, at what rate.

The biological "training data" has non-standard properties: non-i.i.d., non-deterministic, open-world, trajectory-shaped. Cortex is *trajectory-trained*, not dataset-trained — the final state is the result of a path through replay sessions, not optimisation over a corpus. The model is genuinely non-reproducible; training/inference distinction collapses.

Full development of this framing including the 100× temporal compression observation, the reverse-replay-as-automatic-credit-assignment observation, and the M10/M11 possible-unification observation lives in [consolidation-channel § hot-store-as-training-data](../concept/consolidation-channel.md#hot-store-as-training-data-source-for-the-cold-store-m11-reframing).

#### Schema induction is what the biology actually does

AJ-originated insight (2026-05-15, mid-M11). The biology isn't *implementing* a schema; it is *inducing* one. The hippocampus didn't come pre-loaded with "store place + event + outcome." Those structured codings *emerged* from neural plasticity in response to what turned out to be useful for future retrieval.

The architectural priors that biology has (grid cells, time cells, conjunctive binding mechanisms, multi-scale granularity, salience-modulated plasticity) constrain what the system can learn; the *content* of bindings — which place this place cell encodes, which event this event cell encodes, which conjunctions matter — is learned from experience.

Documented in [[cognitive-maps-and-conjunctive-coding]] (concept page surfaced from this walkthrough), which catalogues the biological mechanism set as a candidate architectural-prior list for a caddy.

#### Cross-examination: bolt-on can also induce schemas

The initial reading that "bolt-on commits to a storage representation upfront and so structurally cannot do schema induction" was too strong. AJ's pressure-test (2026-05-15) produced four buildable mechanisms by which a bolt-on system *can* induce its own schemas:

1. Learned embedding space (fine-tune embeddings on retrieval-success episodes)
2. Learned field structure / extraction (meta-model over the agent-LLM stream)
3. Learned salience / consolidation policy (PER-shape at write time)
4. Learned retrieval policy (learned routing instead of fixed kNN)

The real distinguisher between bolt-on and caddy is *integration depth*, not capability binary. Bolt-on requires four sub-systems with their own training loops, evaluations, and handoffs; caddy can train one model end-to-end with gradient flowing through. The trade-off is engineering complexity vs the cost of running a learned model in the inference loop.

Full development including the candidate genuinely-caddy-only properties (end-to-end gradient flow through memory; read-as-write coupling at zero latency; continuous online schema drift) lives in [discrete-unit-memory-architecture § integration-depth refinement](../concept/discrete-unit-memory-architecture.md#refinement-m11-walkthrough-2026-05-15-integration-depth-not-capability-binary).

#### AJ's substrate-antagonism intuition

`[SPECULATED]` Stated 2026-05-15 after the M11 cross-examine: substrate (memory-in-LLM) is structurally antagonistic to at least half of what the biological mechanism set will surface; bolt-on and caddy can both do everything, with varying degrees of success and difficulty.

This refines the family-level reframe with a quantitative prediction: roughly half of the biological mechanism set (M01-M13+) translates poorly or not at all to continuous-update substrate. Falsification test: continue the matrix walk through M12-M13. If any row shows substrate being a natural fit while the discrete-unit family members struggle, the intuition needs revision. If the pattern holds, the family-level framing's "substrate as thought tool, not product path" reading strengthens.

#### Calibration prediction status (matrix walk to date)

`[ASSERTED]` The calibration prediction logged in advance of M10-M13 ("shared architecture, learned-vs-unlearned-policy split as the family-internal differentiator") has been **refined twice** by the matrix walk:

- **M10 refinement (reconsolidation):** added a second axis — architectural coupling depth. Bolt-on can chain read-then-write; caddy can have read-as-write as the same operation. Not a capability break, but a coupling-depth distinction.
- **M11 refinement (interleaved consolidation):** added a third axis — integration depth. Bolt-on can implement biological mechanisms via decomposed sub-systems; caddy can implement them via end-to-end training. Not a capability break, but an engineering-complexity distinction.

The family-level framing is being *refined* rather than *broken* — but it is being refined more than the original "learned-vs-unlearned policies" framing predicted. The current best understanding of the within-family difference is a three-axis space:

| Axis | Bolt-on flavour | Caddy flavour |
|---|---|---|
| Policy learnedness | Can be learned, often hand-coded | Naturally learned |
| Architectural coupling | Read and write are separable | Read and write can be one operation |
| Integration depth | Decomposed sub-systems with handoffs | End-to-end trained model |

The prediction now reads: **both family members can implement biological mechanisms, with the caddy offering tighter integration / lower engineering overhead / better signal propagation, at the cost of a learned model in the inference loop.** Less dramatic than the original framing; more accurate.

#### Negative space identified during the M11 walk

`[SPECULATED]` Topics surfaced but not fully developed; flagged for future digs:

- **Granularity selection mechanism** — how does biology *choose* whether to bind an event as atomic, sub-sequence, or whole-episode? Observation is well-documented; mechanism is open.
- **Forgetting as the negative space of consolidation** — what *doesn't* get replayed decays. Active forgetting (Hardt, Nader & Nadel 2013, in [[mechanism-gap-matrix]] candidate rows) is the partner mechanism. The shape of forgetting is at least as important as the shape of consolidation.
- **Hippocampal "shuffler" function** — biology generates the interleaving by virtue of having a mixed bag of recent memories; the mixing emerges from selection policy, not from explicit shuffling. Engineering analogue not yet specified.
- **REM vs slow-wave sleep role differences** — most replay literature focuses on slow-wave sleep. REM's role (more associative, dream-content, possibly schema-integration) is largely missing from current matrix coverage. Possible M14 candidate row.
- **Continual-learning ML literature specifically** — EWC, knowledge distillation, generative replay, parameter-isolation. The ML community has engineered solutions to catastrophic interference without the dual-system architecture. Knowing their failure modes tells us what biology's design buys you.
- **Failure modes of consolidation** — PTSD, intrusive memories, recurring nightmares are arguably failures of reconsolidation/consolidation. The biology has well-known failure modes; we have not enumerated them as cost-of-architecture. AJ flagged "AI with PTSD" as scifi-horror territory worth thinking about.
- **Prefrontal cortex's role** — PFC selects what to replay in a goal-directed way; not just stochastic sampling from hippocampus. Possible specification of the "learned salience policy" the matrix has been gesturing at.

### M12 + M13 walkthrough — quasi-regular handling, temporal context, primitives-not-independent observation (2026-05-16)

`[ASSERTED]` The closing rows of the matrix walk completed the substrate-antagonism falsification test AJ logged after M11. Both M12 (quasi-regular handling) and M13 (temporal context as retrieval primitive) read substrate ❌ and caddy/bolt-on differentiated along the three-axis space — the family-level framing held. Two new observations surfaced.

#### M12 — quasi-regular handling

Biology walked: McClelland 1995's English past-tense argument (regular *walk → walked* rule plus exception *go → went*) as the canonical example of a domain that requires both episodic specifics and structural regularity simultaneously. U-shaped developmental learning curve (children produce *went* correctly, then over-regularise to *goed*, then recover *went*) as evidence that the two systems develop on different timescales with momentary interference between them. McClelland's deeper claim: any real-world cognitive domain is quasi-regular — communication style, codebase conventions, user preferences with topic-conditional exceptions, domain-specific terminology that interacts with general vocabulary. One system cannot do both jobs because the learning rates are structurally incompatible.

DB analog landed cleanly: **OLAP + OLTP problem with ETL pipeline.** Engineering converged on the same architectural separation as biology — episodic transaction store for specifics, accumulated analytical representation for regularities, periodic consolidation moving stable patterns from one to the other. The convergence is the data point, not the analogy.

**AI status:** bolt-on ❌ (episodes only — no abstracted regularity representation); substrate ❌ (structure only — pretrained regularities baked in, no episodic specifics). This is the **only matrix row so far where both family members have hard ❌ on opposite halves.** Other ❌ rows are missing one capability; M12 is missing perpendicular capabilities in each family member.

**Caddy reading:** could have both natively. Episodic store (commitment 1, separately-addressable model state) carries specifics. Learned representation (commitment 5's auxiliary objective shapes the regularity layer) carries patterns. A consolidation policy (commitment 2) moves stable regularities into the representation while preserving exceptions in the episodic plane. **Practical use case: long-running personal-assistant scenarios** — the regularity plane is *the agent's accumulated understanding of the user/domain*, persisting across sessions; the episodic plane is the agent's memory of specific events. Both queryable on every interaction. See [practical-use-case discussion](#m12-practical-use-case-caddy-with-both-planes) below if promoted; currently captured in session transcript.

#### M11 + M12 may not be independent mechanisms

`[SPECULATED]` Working observation, parallel to the M10/M11 unification flagged in [consolidation-channel](../concept/consolidation-channel.md). M11 (interleaved learning to avoid catastrophic interference) and M12 (quasi-regular handling) are usually catalogued as separate mechanisms but may be **two views of the same architectural commitment**: maintaining two systems with different learning rates and a consolidation operator between them. M11 names *why* the architecture is forced (interference avoidance under joint pressure); M12 names *what the architecture enables* (handling quasi-regular domains). Same primitive, different observational windows.

If this holds — and the M10/M11 possible-unification observation is consistent with it — then **the 13 matrix mechanisms may not be independent.** They may be observable consequences of a smaller set of architectural primitives. Candidate primitive set, from the walk so far:

- Discrete addressable memory units (the M01-M02-M06 substrate)
- Separate fast and slow representations with different learning rates (the CLS commitment underlying M01, M02, M03, M11, M12)
- Salience-modulated plasticity (the M04-M05-M09 thread)
- Consolidation operator moving information between tiers (the M03-M07-M10 thread)

Status: flagged for development if it becomes load-bearing for a Kyrja design decision. Not load-bearing now. If this consolidation holds under M14-M17 reads, the matrix-as-catalogue may need to be supplemented with a primitive-set page that the rows decompose into.

#### M13 — temporal context as retrieval primitive

Biology walked: Howard & Kahana 2002 TCM. Every memory trace is encoded with the current temporal context bound in — context is a vector that drifts slowly, carrying the "smell" of recent events. Retrieval reinstates the bound context, which biases the next retrieval toward items whose stored contexts overlap — temporal contiguity effect falls out of the mechanism. Connects to time cells (MacDonald 2011) and the conjunctive coding documented in [[cognitive-maps-and-conjunctive-coding]]: M13 is the *when* axis added to the *what + where* binding signature. The full hippocampal binding signature is *what + where + when*, and M13 is the read-side primitive that lets context-as-cue retrieve the bound trace.

Algorithmic crossover: TCM is mathematically close to the **successor representation** in reinforcement learning (Stachenfeld et al. 2017). Both are formalisations of "encode state along with a predictive-context smear." Useful pointer if the temporal-context primitive becomes load-bearing — there's a parallel RL literature with relevant tooling.

**DB analog:** closest to nothing in mainstream engineering. Vector similarity over a drifting context vector bound to every write is not how time-series DBs or vector DBs work. The honest read: M13 is the matrix row where biology has a primitive without a clean engineering equivalent. Closest fragments: distributed-tracing parent pointers (each span carries parent context — discrete, not continuous); shingled indexing (records encoded with recent-history fingerprints). No system combines them into the continuous drifting-context primitive.

**AI status:** substrate ❌ as a *persistent* mechanism (attention provides within-window temporal position; evaporates cross-session); bolt-on ❌ as a vector primitive (timestamps as metadata, recency as scalar weight — neither is a context vector). Caddy: could have natively — maintain a drifting context vector as part of caddy state, bind it into every episodic trace at write time, allow retrieval to cue on context similarity. H41 already captures the falsifier specification: [H41 — temporal-context retrieval](../hypothesis/H41-temporal-context-retrieval.md).

#### Substrate-antagonism tally check (post-M13)

`[ASSERTED]` AJ's intuition after the M11 cross-examine: substrate would be structurally antagonistic to ~half of the biological mechanism set. M12 + M13 both read substrate ❌ on the persistent / cross-session aspects of the mechanism. Counting through M01-M13:

| Mechanism | Substrate (persistent) status | Notes |
|---|---|---|
| M01 (fast store) | ✅ | Pretrained weights + context window |
| M02 (slow store) | ✅ | Pretrained weights |
| M03 (consolidation operator) | ⚠ → mostly ❌ | Hope online-only, Skill-SD offline-distillation only — no cross-session learning on closed-source LLMs |
| M04 (selective replay) | ❌ | No trainable cross-session target |
| M05 (schema-fit rate modulation) | ❌ | Fixed per implementation |
| M06 (silent engrams) | ❌ | No stored-but-silent state in frozen LLM |
| M07 (engram migration) | ⚠ | Hope's multi-frequency CMS gestures at it; doesn't migrate per memory |
| M08 (temporal coallocation) | ❌ | No within-LLM window mechanism |
| M09 (sparse competitive allocation) | ⚠ | MoE routing is load-balancing, not memory-allocation |
| M10 (reconsolidation) | ❌ | MEMIT/ROME edit but not retrieval-triggered |
| M11 (interleaved learning) | ⚠ | Continual-learning lit exists; not in agent products |
| M12 (quasi-regular handling) | ❌ | Structure only, no episodic specifics |
| M13 (temporal context primitive) | ❌ | No persistent retrieval-updated context vector |

`[ASSERTED]` 7/13 hard ❌, 3/13 ⚠, 2/13 ✅, 1/13 ✅ misleading (M02's frozen-after-pretrain caveat — biology updates lifetime, ours is frozen). The pattern AJ predicted is supported by the walk: substrate-as-persistent-mechanism is antagonistic to roughly half the biological set in the strict reading, and to most of the remainder in the asymmetric-implementation reading.

This **does not** support "substrate is unable to be a memory" — substrate-as-thought-tool reading still works for within-window state. It supports the existing [NOW.md framing](../NOW.md): substrate is not the Kyrja product path; the discrete-unit family is.

#### Calibration prediction status (final)

`[ASSERTED]` The calibration prediction logged in advance of M10-M13 was "shared architecture, learned-vs-unlearned-policy split as the family-internal differentiator." Walk through M13 produced the final refinement:

- M10 added **architectural coupling depth** as a second within-family axis (read-as-write coupling).
- M11 added **integration depth** as a third within-family axis (end-to-end vs decomposed sub-systems).
- M12 + M13 added no new within-family axes — both rows distinguish substrate from family-members, not bolt-on from caddy.

The three-axis space (policy learnedness × coupling depth × integration depth) survives the full walk. The bolt-on / caddy difference is differentiation along these three axes, not capability binary. The original "learned-vs-unlearned policies as sole differentiator" framing was too narrow but pointed in the right direction. **Family-level framing is well-calibrated for the M01-M13 set;** validated, not falsified.

#### Negative space and new candidate rows surfaced during M12 + M13

`[SPECULATED]` Topics that came up during the walk and merit future development:

- **Smaller-primitive-set decomposition** — the observation above (M11+M12 may be the same mechanism viewed two ways) needs testing across other matrix rows. M10/M11 was the first hint; M11/M12 was the second. If a third pair shows the same shape, the catalogue-as-rows framing needs supplementing with a primitive-set framing.
- **Read-side / write-side complementarity** — M13 is the first explicitly read-side mechanism in the matrix. Everything M01-M12 is storage or consolidation (write-side). Open question: are there other read-side primitives the matrix is missing? Modern Hopfield's pattern-completion-as-retrieval is one candidate. M14-M17 candidate rows should be screened for read-side mechanisms specifically.
- **Successor representation as algorithmic bridge** — Stachenfeld 2017 cross-link is the M13 algorithmic crossover. The RL literature on SR has tooling (eigendecomposition-based representations, multi-timescale SR) that may transfer to a caddy temporal-context implementation. Not load-bearing now; flagged for the H41 design pass.

### M14-M17 walkthrough — interface fork, anticipate-vs-predict, granularity, salience-as-load-bearing (2026-05-16 + 2026-05-17)

`[ASSERTED]` The matrix walk through M14 (Buzsáki SPW-Rs), M15 (Redondo & Morris STC), M16 (Schacter, Addis, Buckner prospective brain), and M17 (Hardt, Nader, Nadel active forgetting) produced four caddy-relevant findings beyond the per-row substrate-antagonism tallies. They live in their own subsections on dedicated pages; this section collects them as a cumulative summary.

#### Interface fork — soft composition vs hard selection

`[ASSERTED]` The M16 walk surfaced a design-fork in the caddy's output interface that determines whether the M16 *strong reading* (constructive recombination of fragments into novel composed outputs) is achievable through training. Hard selection (top-K stored items concatenated into context) structurally forecloses construction — no gradient signal can rewrite "return K records" into "return one composed thing." Soft composition (attention-style weighted blend of value vectors injected into the golfer's hidden state) makes composition the default behaviour — every attention computation is by construction a weighted sum.

Promoted to [H43 — soft-composition emergent construction](../hypothesis/H43-soft-composition-emergent-construction.md) as a falsifiable claim. The hypothesis is currently being prototyped in a parallel side-window borrowing from Memorizing Transformer, with co-training and a dedicated query head as architectural commitments. See also [concept/caddy § Interface fork](../concept/caddy.md) for the cross-link onto the caddy's commitments.

#### Anticipate vs predict (naming distinction)

`[ASSERTED]` AJ-originated (2026-05-17). **The caddy's job is *anticipation*, not *prediction*.** Prediction is the golfer's job — taking the swing, choosing the next token. The caddy's job is preparing material in a form useful for the golfer's prediction. A real-world golf caddy doesn't take shots, but they walk the course before the round, note wind shifts, and pre-club for conditions. Construction-via-soft-composition is the architectural shape that lets emergent anticipation cover the constructive work biology does in SPW-Rs.

#### Granularity ladder — runtime memory surface

`[ASSERTED]` Promoted to [concept/retrieval-granularity](../concept/retrieval-granularity.md). Five positions on the spectrum (per-token per-layer → per-token single-point → per-chunk → per-turn → multi-point heterogeneous), each anchored to a specific reference architecture. The current agent-memory product space (Mem0, Letta, Zep, Cognee, LightMem) all default to per-turn without testing finer alternatives; the language-modelling research literature (kNN-LM, RETRO, Memorizing Transformer) has shown for years that finer granularity is strictly more powerful at modest cost. The transfer hasn't happened — a real architectural blind spot.

AJ's emergence intuition: if the gate is learned end-to-end (cross-attention over a memory pool), the granularity question *partly dissolves* — the trained attention picks per query whether each memory matters. Per-token-per-layer is the safe default because it preserves the option to learn fine-grained access; coarser granularities foreclose it.

#### Off-line vs online surface (two surfaces, not one)

`[ASSERTED]` Biology operates at two granularities simultaneously (per M14 Buzsáki). The online surface (theta-mode during active behaviour) is continuous low-latency integration of memory into ongoing processing — maps to per-token / per-layer on the spectrum. The off-line surface (SPW-R during sleep / quiet wakefulness) is batch-oriented recombination of fragments — maps to a regime outside the spectrum entirely (runs between conversations, not during them).

For the caddy this means the granularity question is **two** choices: the *online* surface (where on the spectrum the runtime memory surface lives) and whether there's an *off-line* surface ([consolidation-channel](../concept/consolidation-channel.md)). The two are not in competition — they compose, doing different jobs. The off-line surface handles what M14 names: pre-built anticipation artifacts the caddy prepares during quiet periods.

AJ's framing (2026-05-17): the choice of communication interface between caddy and golfer (online surface) determines what work the caddy needs to do off-line. The two surfaces co-design.

#### Salience signal as the load-bearing variable across multiple rows

`[ASSERTED]` The M15 walk surfaced [salience-signal](salience-signal.md) as a load-bearing input variable that gates **five** matrix rows (M03 consolidation, M04 selective replay, M05 schema-fit modulation, M15 synaptic tagging, M17 active forgetting). The architectural choice (STC-shape vs hot-store-with-promotion) is largely a downstream implementation detail; the salience-computation problem is invariant.

For the caddy, this surfaces a query-head-as-online-salience framing: a dedicated query head in the golfer is the explicit *ask-the-caddy* operator, whose output is "what does the golfer need to know right now" — i.e., a salience computation. [H42](../hypothesis/H42-learned-salience-function.md) is the falsifiable claim. The query head is the online complement to the off-line salience signal that drives consolidation and forgetting; both are applications of the same upstream computation at different surfaces.

#### Pattern separation as architectural prerequisite for graded decay

`[ASSERTED]` The M17 walk surfaced [pattern-separation](../concept/pattern-separation.md) as the architectural prerequisite for graded decay. Without orthogonal coding, similar memories collide and *interference* dominates as the forgetting mode; per-memory decay rates have no meaningful referent. With orthogonal coding, memories don't collide; *then* salience-modulated per-memory decay becomes possible. DB analogy: per-key TTLs require non-colliding keys.

For the caddy this means [H34](../hypothesis/H34-forgetting-scores.md) (learned forgetting scores) has a precondition — the caddy's memory representation has to commit to a pattern-separation strategy (enforced via sparse coding / orthogonalization-on-write, or relied on statistically via high-d attention keys). High-d learned attention keys provide *some* pattern separation by default but not the *enforced* orthogonality biology has. Whether this matters empirically is an open question.

#### Substrate-antagonism tally (post M14-M17)

`[ASSERTED]` Per the [mechanism-gap-matrix](../concept/mechanism-gap-matrix.md) tally: 11 of 17 mechanisms have no implementation in either AI class (hard ❌); 4 of 17 are partial (⚠) typically via mechanisms designed for different purposes; 2 of 17 are present (✅, M01 and M02 — with M02 a misleading ✅). For substrate specifically: 7 of 17 hard ❌ for persistent / cross-session mechanisms, plus 4 of 17 ⚠ via mechanisms designed for other purposes. AJ's M11 substrate-antagonism intuition is supported by the full walk.

The four unification observations (M10/M11, M11/M12, M05/M10/M15, M03/M17) strengthen the working hypothesis that the matrix's row-catalogue is observing *consequences of a smaller primitive set* rather than independent mechanisms. The primitive-set page is now firmly flagged for future development.

---

## MERLIN investigation (2026-05-15, follow-on session)

Walked Wayne et al. 2018 MERLIN verbatim ([source/wayne-2018-merlin.md](../source/wayne-2018-merlin.md)) as the closest existing template for the caddy. Architecture summary: external memory matrix, content-addressed read head with learned keys + temperatures, **Memory-Based Predictor (MBP)** trained with a VAE-style variational lower bound on multi-modality reconstruction, policy trained separately via RL with a gradient stop between policy and the MBP's latent state, two ADAM optimisers with independent learning rates, memory matrix reset at episode start.

### Three-axis check against MERLIN

The prior framing — "MERLIN potentially checks all three axes" — was loose. The verbatim read produced a sharper verdict:

| Axis | MERLIN coverage | Notes |
|---|---|---|
| **1. Online learning** | Partial | Memory matrix accumulates one row per timestep within an episode; resets at episode start; weights only update during training. Within-episode buffer accumulation, NOT cross-deployment learning. |
| **2. Learned interface** | Strong | Content-addressed read head — cosine similarity between learned read keys and stored rows, softmax with learned per-key temperature, weighted sum as readout. Policy consumes the readout via concatenation. |
| **3. Computation-as-recall** | Partial | The read operation is parameterized (learned attention over storage), not a hash-table lookup. But the output is a linear combination of stored latents — attention-as-recall, not full-forward-pass-as-recall. |

`[ASSERTED]` from the verbatim source read. The replacement framing the rest of this open question now leans on: **MERLIN's distinctive structural element is not full coverage of the three axes — it is the joint training of memory representations with a non-task auxiliary loss (the MBP), through a learned interface, beside an RL-trained consumer with a gradient stop.** That is a more specific shape than "memory as a model" and a more measurable hypothesis.

### Sharpest research hypothesis surfaced: MBP-was-dropped

`[SPECULATED]` Hypothesis flagged for future testing.

The LLM-era retrieval-augmented language models — [RETRO](../source/borgeaud-2022-retro.md) (Borgeaud et al. 2022), Memorizing Transformer ([source/wu-2022-memorizing-transformer.md](../source/wu-2022-memorizing-transformer.md "pending") — Wu et al. 2022, verbatim re-read TODO) — co-train an LM with external memory via cross-attention. They inherited MERLIN's **read head** (learned attention into stored representations) but **dropped the MBP** (the world-model auxiliary loss that shaped MERLIN's memory representations). The training signal in RETRO/MemoTx is the LM's next-token loss alone; there is no separate auxiliary objective shaping memory.

**Candidate explanation:** the LLM's next-token prediction already does most of what the MBP did — it builds useful latent representations under a dense, always-available prediction signal. The MBP became redundant in the LLM era. `[SPECULATED]`.

**Hole in the candidate explanation:** next-token prediction shapes the **LLM's own representations** to be predictive of next tokens; it does not necessarily shape **the memory module's representations** to be a good storage substrate. Those could come apart. A memory module trained only with the LM's next-token gradient may end up with representations optimised for "what helps next-token prediction *given that the memory will be attended to*" rather than for "what is useful long-term storage of an experience." The MBP's separable, prediction-shaped objective on memory itself could plausibly recover what the simpler co-training misses.

**Testable hypothesis (as of 2026-05-15):** train three matched-size systems on the same agent-task corpus — (a) frozen-LLM + bolt-on retrieval baseline, (b) RETRO/MemoTx-style co-trained memory with LM-loss-only, (c) RETRO/MemoTx-shape + MBP-style auxiliary world-model loss on the memory module — and read the curves. As far as this investigation has surveyed, ablation (c) does not exist in the published literature. **This is the cleanest open empirical question the caddy investigation has surfaced.**

### Literature pass (2026-05-15 side-window) — the unexplored cell remains empty

`[ASSERTED]` Moderate-depth literature pass (one survey-repo fetch + ~6 targeted Semantic Scholar / arXiv queries + two verbatim full-text reads) surveyed the space for "co-trained memory module with auxiliary world-model-style loss on the memory representations." Findings:

**Strongest near-miss — [Memory³](https://arxiv.org/abs/2407.01178) (Yang et al. 2024).** 2.4B model trained from scratch with explicit memory as sparsified attention KVs cached externally. Two-stage pretraining: warmup (60B tokens, no memory) then continual-train (22B tokens, with memory KVs concatenated into self-attention). Verbatim read confirmed `[ASSERTED]`: **next-token loss only at both stages.** No auxiliary objective on memory representations. The "third form of memory" naming refers to a *storage tier within one LLM* (parameters / KV cache / explicit memory), not to a separate model. Memory³ has commitments 1-4 of the caddy roughly satisfied (separate storage, co-training, activation injection at scale, learned attention-as-recall) but commitment 5 explicitly absent. Memory³ is the **near-perfect natural baseline** for the MBP-was-dropped ablation: adding a JEPA-style or world-model-style auxiliary loss on the explicit-memory representations during continual-train is exactly the empirical question this hypothesis predicts.

**Closest auxiliary-loss precedent — [ICAE](https://arxiv.org/abs/2307.06945) (Ge et al. 2023, ICLR 2024).** LoRA-adapted LLM encoder + frozen LLM decoder, **dual pretraining objective** (autoencoding reconstruction + LM continuation). Their Table 5 ablation: combining AE+LM beats AE-only, beats LM-only, beats no-pretraining. The pattern survives: an auxiliary objective on the memory-producing encoder adds signal over LM-only. **Mechanism note (2026-05-20 verbatim read at [ge-2024-icae](../source/ge-2024-icae.md)):** both objectives are *token-space* next-token CE losses computed at the frozen decoder's output (§2.2.1, §2.2.2); the memory slots are intermediate hidden states with no direct loss term in representation space. Anti-collapse machinery is "frozen decoder must reconstruct text," not the BYOL triad (no stop-grad, no EMA). This is a **same-class-different-shape** precedent for commitment 5 — same class (auxiliary objective on a memory-producing encoder helps) but different shape from V-JEPA-style representation-space feature prediction. **Effect-size context:** Table 5's pretraining-at-all win is 6.4× over no-pretraining; the AE+LM-mix lift over either-alone is a smaller 1.3-1.4×. **Scope mismatch:** per-context compression (one document → ~128 memory slots), not experiential memory accumulating across deployments.

**Independent field-level confirmation — [LLM-JEPA](https://arxiv.org/abs/2509.14252) (Huang, LeCun, Balestriero 2025).** LeCun's group adds a JEPA-style embedding-space auxiliary loss to LLM training. **No memory module** — the objective is added inside the LLM's own pretraining. They do not cite Memorizing Transformer, RETRO, or MERLIN. Their gap statement is direct: *"The lack of JEPA-style LLM is a testimony of the challenge in designing such objectives for language."* This is independent confirmation from JEPA's inventors that the broader gap (auxiliary embedding-space objectives for language) exists at the field level — and that even when attacked, it is attacked inside the LLM rather than via a separate memory module.

**Distractors confirmed not in the cell.** Memory Decoder / MLP Memory (Cao, Wei et al. 2025) — separate memory modules trained to imitate a kNN retriever; auxiliary objective is retrieval-distillation, not world-modelling. Titans (Behrouz 2025) — continuous-update Hope-shape; outside the discrete-unit family. MemLong — non-differentiable ret-mem + partially trainable decoder; no auxiliary loss on memory.

**Net verdict.** The exact combination — *separately-stateful memory module + activation-injection interface + auxiliary world-model-style loss on memory representations* — remains unoccupied. The MBP-was-dropped hypothesis is **stronger after the literature pass**, not weaker. Memory³ in particular provides a clean comparator at 2.4B scale; the unexplored cell becomes a specific, well-posed ablation rather than a vague research direction.

**Pending verbatim reads from this pass.** Memorizing Transformer (Wu et al. 2022) is still cited but unanchored — `[pending]` source link remains. The Memory³ paper is now archived as yang-2024-memory3.pdf; a `source/yang-2024-memory3.md` page would be reasonable if Memory³ becomes load-bearing for a Kyrja decision.

### Consumer-axis collapse — Case A dominates

`[ASSERTED]` based on 2026-05-15 investigation; no comprehensive survey performed.

The consumer axis (`memory-for-the-model` vs `memory-for-the-agent`, [concept/memory-consumer-axis](../concept/memory-consumer-axis.md)) admits four cells. In modern agent architectures, **Case A — memory consumed by the primary LLM's forward pass — is overwhelmingly the realized shape.** Case B — memory consumed by the agent's software loop outside the LLM — is rare in practice and tends to collapse into **constraint/rule enforcement** (Constitutional-AI-style hard rules: "never delete files without confirming") rather than experiential memory. True experiential lessons want to influence reasoning, and reasoning happens in the LLM, not the agent harness.

**Consequence for the caddy question:** the architectural action lives **within Case A** and decomposes into three interface options for how memory output reaches the primary LLM:

| Interface | Shape | Cost | Existing examples |
|---|---|---|---|
| **(a) Text injection into prompt** | Memory module's output becomes tokens in the LLM's input. | Cheap; no LLM retraining. | All commercial agentic memory products: [Mem0](../incumbent/mem0.md), [Cognee](../incumbent/cognee.md), [Letta](../incumbent/letta.md), [Zep](../incumbent/zep.md), [Honcho](../incumbent/honcho.md). |
| **(b) Activation injection** | Memory output enters LLM's attention layers via cross-attention (Memorizing-Transformer-shape) or KV-cache injection. | Requires co-training of memory + LLM. | [RETRO](../source/borgeaud-2022-retro.md), Memorizing Transformer. Research-stage. |
| **(c) Adapter/LoRA modulation** | Memory output modulates a low-rank adapter on the LLM at inference. | Exotic; very few examples. | None deployed; isolated research papers. |

Interface (a) is the bolt-on path with a sophisticated memory back-end. Interfaces (b) and (c) are the **structurally novel** options that depend on co-training and pay the frontier-cost regime. The caddy investigation's architectural ground is mostly the question of which interface, under what training regime, and what the memory module's training objective should be.

### Memory module's true jobs — compression and retrieval, not generation

`[ASSERTED]` after AJ pushback on an earlier loose framing.

An earlier framing of the memory module as a "next-lesson predictor" was incorrect — it suggested generation of a sequence of lessons, which is not the architectural pattern Case A wants. The memory module's actual jobs in Case A are:

1. **Compression (write-side).** Take (trajectory, outcome) and produce a stored unit — an abstracted lesson, an atomic conclusion, a compressed experience. Generative, LLM-shaped at the unit boundary; can be the LLM itself reflecting on its own trajectory ([Reflexion](https://arxiv.org/abs/2303.11366)-style) or a separate fine-tuned model (Honcho's [Neuromancer XR](../source/honcho-docs.md) is the cleanest existing example).
2. **Retrieval (read-side).** Given the LLM's current context, surface relevant stored units. A retrieval/ranking task; the unit is then injected (interface a/b/c above) into the LLM's forward pass.

These two functions can be one model doing both jobs, two models, or a learned retriever paired with an LLM-based reflector. The caddy investigation's architectural choices live across these decompositions, not in a single "predict the next lesson" objective.

### Sidebar — granularity-ladder of surprise

`[ASSERTED]` Conceptual structure surfaced during 2026-05-15 investigation.

Surprise is not a single quantity — it lives at multiple granularities, and the memory-write trigger has to integrate across them:

| Level | Where it lives | Accessibility |
|---|---|---|
| **1. Token-level** | Per-token cross-entropy inside the LLM's forward pass | Dense, differentiable. Inaccessible from bolt-on against closed-source LLMs (logprobs are top-K truncated when exposed at all, and most agent frameworks do not request them). |
| **2. Turn-level** | Aggregated loss/confidence over a single LLM call | Derivable from (1) if available; not normally surfaced. |
| **3. Outcome-level** | Environmental signal — test passed/failed, code ran, user accepted | External to the LLM. Available to any agent loop that can observe outcomes. |
| **4. Reflective/abstracted** | A summary of what went wrong, produced by running the LLM on its own trajectory | Available to any system that can prompt the LLM to reflect. |

`[ASSERTED]` Memory-write triggers in practice come from levels 3 and 4 — outcomes plus reflection produce the lesson unit. Level 1's distinctive contribution is **retrospective**: after the outcome is known, identify moments in the trajectory where the LLM was overconfident given how things actually went. This is the agentic generalisation of [Prioritized Experience Replay](../source/yang-et-al-2024-selection-of-experience.md)'s TD-error reweighting from RL — surprise as a *post-hoc* reweighting signal across the trajectory, not a real-time write trigger.

**Structural consequence for the caddy:** the level-1 signal is inaccessible bolt-on against closed-source LLMs. Interfaces (b) and (c) above, under co-training, make it natively available because the gradients are owned. This is one of the concrete unlocks that co-training buys — not just a more efficient interface, but **access to a surprise signal that is structurally absent in bolt-on**.

Cross-link: [mechanism-gap-matrix](../concept/mechanism-gap-matrix.md) M03/M04 row (PER as the closest biological/RL analogue) and [consolidation-channel](../concept/consolidation-channel.md) (the operator the surprise signal would inform on the write path).

### Bottom line from the MERLIN investigation

The caddy question, after this investigation, is sharper than "is memory-as-a-separate-model real":

> Within Case A (memory consumed by the primary LLM), with interface (b) (activation injection via co-trained cross-attention), does adding an MBP-style auxiliary world-model loss on the memory module — beyond the LLM's own next-token loss — improve over the existing co-trained-memory baseline?

That is a measurable hypothesis with a known control (current RETRO/MemoTx ablations) and a clear architectural design (memory module's auxiliary objective). It is also a hypothesis squarely in the frontier-cost training regime, which means it is not a near-term entrepreneurial path — it is a research question of the kind a frontier lab with co-training budget could answer with a clean ablation.

---

## Closest existing reference points

None are quite the caddy. Key prior art to read:

- **kNN-LM** (Khandelwal 2020), **RETRO** (Borgeaud 2022), **Memorizing Transformer** (Wu 2022) — primary LLM augmented with a *datastore*, not a model. The datastore is a frozen index over LM activations. Bolt-on with smarter retrieval.
- **Larimar** (Das 2024) — Kanerva-style episodic memory bolted into the primary LLM's latent space. Memory is *part of* the LLM, not a separate service. Substrate-shaped.
- **Honcho** (Plastic Labs) — claimed something close to "memory model as service." **Verbatim architecture read completed 2026-05-15** ([source/honcho-docs.md](../source/honcho-docs.md), [incumbent/honcho.md](../incumbent/honcho.md)). Result: **text-out**. `.chat()` returns prose; Representation endpoints return `string`; `get_context()` returns curated text. Plastic Labs ships a fine-tuned Qwen3-8B (Neuromancer XR) doing ingestion-time conclusion extraction, but the outputs are stored as text. No learned-fusion interface to the consuming agent's primary LLM. **Honcho occupies the *outside-LLM × memory-for-the-agent* cell; the *outside-LLM × memory-for-the-model* cell is still empty.** Methodological note from the read: cost-gap-aware reading of absence (capability vs resource — see [memory: feedback_capability_vs_resource]).
- **Memory Networks** (Weston 2014), **NTM/DNC** (Graves 2014/2016) — read/write memory operations, but as *components inside* a larger network. Not a separate service.
- **Cartridges** (typically framed as task-specialized adapters, not memory models) — adjacent but not the same shape.

## The falsifiability hook

Claim 3 reduces to one design choice: **what does the memory model output, and how does the consuming LLM ingest it?** The 2026-05-15 MERLIN investigation refined this from a binary to a three-way framing:

- **Text out → interface (a)** → it's RAG with a sophisticated back-end. The memory model is an expensive compressor + retriever; the consuming LLM still ingests tokens. Collapses back into bolt-on. (All commercial agentic memory products live here.)
- **Representations out → interface (b)** → genuinely new at the interface. Memory module emits representations that enter the consuming LLM's attention layers via cross-attention. Requires co-training. Existing examples ([RETRO](../source/borgeaud-2022-retro.md), Memorizing Transformer) have proven the interface works but did not adopt MERLIN's auxiliary world-model loss.
- **Representations out + auxiliary loss → interface (b) + MBP-equivalent** → the unexplored cell. Memory module emits representations *and* is trained under a non-task auxiliary objective (MBP-shaped, or a contemporary equivalent). This is the unmeasured ablation surfaced by the MERLIN investigation.

If the third option collapses to either (a) or to the existing co-trained-memory baseline (b without auxiliary loss), claim 3 is dead. The architectural ground for claim 3 living lives in the unexplored cell.

## What evidence would resolve it

1. ~~**Honcho architecture read.**~~ ✅ Resolved 2026-05-15 — Honcho is text-out at depth-0-1; the caddy cell remains empty. (See above.)
2. ~~**A design sketch for a representation-out memory model.**~~ ✅ Resolved (architecturally) 2026-05-15 by the MERLIN investigation — the design exists in [Wayne et al. 2018](../source/wayne-2018-merlin.md) (memory matrix, content-addressed read head with learned keys, MBP auxiliary loss, gradient-stop between policy and memory latents). The LLM-era port via cross-attention exists in [RETRO](../source/borgeaud-2022-retro.md). What is still open is whether the *combination* — MERLIN's MBP auxiliary loss + RETRO's cross-attention interface — improves over plain co-trained memory. **That is now a specific empirical question, not an architectural-existence question.**
3. ~~**Existence proof from adjacent literature for the *combined* shape**~~ ✅ Resolved 2026-05-15 by the literature pass (above) — the cell is empty. Memory³ (Yang et al. 2024) is the closest natural baseline at scale; LLM-JEPA (Huang/LeCun/Balestriero 2025) independently confirms the gap at field level; ICAE (Ge et al. 2023) demonstrates auxiliary reconstruction objective helps over LM-only but for per-context scope. Promotes the MBP-was-dropped hypothesis from "open question" to "candidate hypothesis worth formulating" — but downgraded in load-bearing-ness by the M11 cross-examination (the caddy's distinctiveness from bolt-on is now characterized by three axes, not by this single ablation alone). See [Literature pass](#literature-pass-2026-05-15-side-window--the-unexplored-cell-remains-empty) above.
4. **Continuation of the matrix walk through M07-M13.** Falsification test for the cumulative pattern. If the caddy stops resolving frictions in later rows, the pattern was selection bias and the case weakens. If it holds, the strategic case strengthens.
5. **An MBP-equivalent auxiliary loss specification for the LLM era.** MERLIN's MBP was a multi-modality reconstruction objective (image, return, reward, action, velocity, text). The LLM-era analogue is not obvious — next-token prediction is already done by the consuming LLM. Candidate auxiliary objectives include: reconstruction loss on stored episodes (autoencoder-shaped), retrieval-quality loss against outcome ground truth, contrastive matching of (problem-pattern → lesson) pairs. If no specifiable auxiliary loss can be articulated that adds signal beyond the LLM's next-token loss, the MBP-was-dropped hypothesis is false — the LLM era was right to drop it.

## Competitive landscape and Norman rubric validation (2026-05-16 ingest)

`[ASSERTED]` Major expansion of the prior-art map and external-validation landscape. Three load-bearing findings:

### Finding 1 — The Norman rubric externally validates the caddy architecture

`[ASSERTED]` [Dong, Lu, Norman & Michelmann 2025](../source/dong-2025-norman-episodic.md), *Towards LLMs with human-like episodic memory*, Trends in Cognitive Sciences June 2025. The Princeton/NYU Norman lab — the leading academic group on hippocampal-CLS modelling — explicitly endorses the caddy architectural pattern by name. Verbatim (page 3): *"a memory system that rapidly stores information in a latent and lasting form (like the hippocampus in humans) and is separate from both the context window... and the weights of the main LLM."* They further endorse storing internal representations over verbatim text (commitment 4 of the caddy).

The paper specifies five evaluable properties — dynamic memory updating, event segmentation, selective encoding/retrieval, temporal contiguity, competition at retrieval — see [concept/norman-rubric](../concept/norman-rubric.md) for the full framework and scoring matrix. This is **the rubric** the caddy will be evaluated against in VC diligence and academic review.

Hassabis post-Gemini-3 publicly diagnoses the same wedge (context windows as "badly approximated hippocampus") — see [hassabis-2026-memory-bottleneck](../source/hassabis-2026-memory-bottleneck.md). Two independent external sources (top-tier journal + DeepMind CEO commentary) converge on the caddy thesis.

### Finding 2 — The cog-sci-grounded competitive cell is empty after 11 months

`[ASSERTED]` Comprehensive parallel-agent survey 2026-05-16 (four agent investigations: brain-inspired AI companies, academic neuro-AI bridge groups, startup/commercial landscape, stealth+founder-graph signals). **No system in the published literature scores 3/5 or higher on the [norman-rubric](../concept/norman-rubric.md).**

Direct cog-sci-grounded competitors with funding:

- **[Engramme](../incumbent/engramme.md)** — Harvard spinout (Kreiman + Madan), $1B raising. **Deep dive revealed: encrypted personal-data RAG with hippocampus-themed marketing.** Cites exactly one cog-sci mechanism by name (hippocampus); zero engagement with CLS, schema, reconsolidation, replay, temporal contiguity, competition. Scores 0/5 on Norman rubric. **Different product cell than the caddy.**
- **[NeoCognition](../incumbent/neocognition.md)** — $40M seed (Yu Su, OSU, NLP/agents). Stealth, unknown architecture. Yu Su's pedigree is NLP not cog-sci-memory. Watch flag with unknown ceiling.
- **[AMI Labs](../incumbent/ami-labs.md)** — LeCun's $1B seed at $3.5B. Integrated JEPA architecture, not sidecar. Different architectural cell — overlapping product mission, different shape.
- **[Humans&](../incumbent/humans-and.md)** — $480M at $4.48B (Zelikman + Goodman). Goodman is computational cog-sci (Bayesian, not neuro-memory). Pivot-watch candidate.

Frontier-lab moat risks:

- **Anthropic Auto Dream** (March 2026 feature) + **Lampinen recently hired from DeepMind** — most concerning frontier-lab combination. CLS-explicit framing in [Lampinen 2025](../source/lampinen-2025-latent-learning.md), REM-inspired consolidation feature shipped, talent on staff. Score on rubric: 1/5 currently (Auto Dream addresses dynamic updating only).
- **DeepMind Project Astra (Wayne)** — Hassabis publicly committed to memory as 2026 bottleneck; shipped architecture is still bolt-on RAG. Wayne, Lillicrap, Kirkpatrick, Kumaran all remain in-house. 6-18 month window between rhetoric and ship.

Academic prior art (cog-sci-grounded but no spinoff signal):

- **[Spens & Burgess 2024](../source/spens-2024-hippocampal-rag.md)** (UCL Burgess lab) — cleanest theoretical map. Uses Mistral-7B as neocortex, vector store as hippocampus (Hopfield-theoretical only), xRAG context compression as injection. **Score: 1.5/5 on Norman rubric.** Architecturally bolt-on/substrate hybrid, not caddy.
- **[MEGa](../source/pan-2025-mega.md)** (Pan/Hahami/Zhang/Sompolinsky, Harvard CBS / Hebrew U) — in-weights CLS-grounded gated LoRA per memory. Linear parameter growth limit. **Score: 1.5/5.** Architectural foil for sidecar pitch.

Mechanism-honest non-cog-sci:

- **[Sakana NAMM](../source/cetin-2024-namm.md)** — separately-trainable KV-cache retention policy, transferable across base models. Sidecar in engineering sense (transferable) but not memory-architecture sense (no persistent state). Score: 1/5. Useful as partial proof-of-concept for sidecar shape working at scale, not as competitor.

### Finding 3 — Post-Norman gap is persistent

`[ASSERTED]` Eleven months after Norman et al. published in TiCS June 2025, **no post-Norman publication systematically addresses the rubric.** Surveyed: Hope/Nested Learning (Dec 2025), NextMem (Feb 2026), GradMem (Mar 2026), Auto Dream (Mar 2026), AMI Labs framing (Mar 2026), Engramme (Mar 2026), NeoCognition (Apr 2026), MEGa (Apr 2025, predates Norman).

Most plausible interpretation: integrating all five properties in one system is research-program-scale work that doesn't fit the publish-a-paper-per-quarter cadence the field optimises for. Each property is non-trivial; doing all five at once requires architectural commitment, not feature add.

**This is the strongest evidence-shape for the caddy wedge being defensible.** Not "no one has thought of this" but "no one has built this, eleven months after the standards-setting paper said they should." See [norman-rubric § Why this matters](../concept/norman-rubric.md#why-this-matters).

### Updated falsifiability and resolution status

`[ASSERTED]` Items 1-5 of the original "What evidence would resolve it" remain valid. **Additional resolution criterion added 2026-05-16:**

6. **Norman-rubric score on a working caddy implementation.** The empirical bet is now externalisable: build a caddy that scores 3/5 or higher on the rubric (beats EM-LLM's 2.5/5 ceiling) and ideally 5/5 (closes the post-Norman gap). The Box 4 benchmark proposal in [dong-2025-norman-episodic](../source/dong-2025-norman-episodic.md) specifies the experimental shape. If a caddy cannot beat EM-LLM at academic scale, commitment 5 collapses and the caddy as a research contribution is dead. If it can, the differentiation case is empirically grounded against an externally-defined rubric.

### The pitch narrative as of 2026-05-16

`[ASSERTED]` The differentiation story is no longer "novel architectural pattern" but rather:

> *"Norman et al. specified the rubric for human-like MA-LLMs in TiCS June 2025. Eleven months on, the highest-scoring system is EM-LLM at 2.5/5 — a system Norman cites as a positive but partial step. No system satisfies the full rubric. We're proposing to be that system, on a sidecar caddy architecture that matches Norman's explicit recommendation of a memory system separate from both context window and LLM weights. Engramme is in a different cell (personal-data RAG with hippocampus marketing, 0/5 on the rubric). DeepMind's CEO has publicly diagnosed the same wedge but their shipped architecture is still bolt-on RAG. The cell is empirically open."*

This is a stronger pitch than novelty-claims because it rests on an external rubric, an external CEO endorsement of the wedge, and a measurable empirical gap.

## State as of pause

- AJ-proposed 2026-05-15 mid-M02 digest of the mechanism-gap matrix walkthrough.
- AJ flagged this as a side quest to pick up in a separate session window. He is relaying caddy moments from the active walkthrough into the separate window verbatim.
- Three claims captured. Claim 1 was promoted to [[memory-consumer-axis]] concept page on the same day. Claims 2 and 3 remain open here.
- **2026-05-15 synthesis update:** Matrix walkthrough produced a four-row cumulative pattern (M03→M06) where the caddy resolves frictions that exist for both other paths. Pattern captured in the "Matrix-walkthrough findings" section above, with a working hypothesis and a falsification test (continue the walk through M07-M13; pattern either holds or breaks).
- **2026-05-15 Honcho check (side-quest window):** completed. Honcho is text-out at depth-0-1; the *outside-LLM × memory-for-the-model* cell of the consumer-axis is still empty. Methodological correction surfaced: do not read "Plastic Labs has Neuromancer-XR-class capability but didn't ship representation-out" as a negative technical signal — the cost gap between fine-tuning Qwen3-8B and training a representation-out memory model with a learned-fusion interface is enormous. (`feedback_capability_vs_resource`.)
- **2026-05-15 MERLIN investigation (follow-on session):** completed. Verbatim read of [Wayne et al. 2018](../source/wayne-2018-merlin.md) produced the three-axis check (partial/strong/partial), the MBP-was-dropped hypothesis as the sharpest research question to fall out of the investigation, the consumer-axis collapse (Case A dominates; the architectural action lives in three interface options within Case A), the memory module's true jobs (compression + retrieval, not next-lesson generation), and the granularity-ladder of surprise. Methodological correction surfaced: a "next-lesson predictor" framing was retracted under AJ challenge — the memory module's job is conditional retrieval given context, not generation of a sequence of lessons. (`feedback_investigation_over_capture`.)
- **2026-05-15 literature pass (side-window):** completed. The combined-shape cell (co-trained memory + activation-injection interface + auxiliary loss on memory representations) is empty. Memory³ established as near-perfect natural baseline; LLM-JEPA independently confirms the gap at field level; ICAE demonstrates the auxiliary-loss pattern works at smaller scope. *Refinement 2026-05-20 (ICAE verbatim read):* ICAE is **same-class-different-shape** — same class (auxiliary objective on a memory-producing encoder helps at LLM scale) but token-space CE loss at frozen decoder output, not representation-space. The combined-shape cell remains empty for the representation-space family specifically. See [Literature pass](#literature-pass-2026-05-15-side-window--the-unexplored-cell-remains-empty). MBP-was-dropped hypothesis survives but is now downgraded from existential test to one of several within-family axes per the M11 cross-examination.
- **2026-05-15 main-window M10 + M11 walkthroughs:** completed. Matrix walk continued through reconsolidation (M10) and interleaved consolidation (M11). M11 cross-examination retracted the over-claim "bolt-on cannot induce schemas." Calibration prediction refined twice into a three-axis within-family space (policy learnedness, architectural coupling, integration depth). Three genuinely caddy-only properties (end-to-end gradient flow, read-as-write coupling, continuous online schema drift) survive — held loosely. AJ's substrate-antagonism intuition (substrate antagonistic to ~half of biology) flagged for M12/M13 falsification. New concept page [cognitive-maps-and-conjunctive-coding](../concept/cognitive-maps-and-conjunctive-coding.md) surfaced as architectural-prior list for the caddy.
- **2026-05-15 naming decision (side-window):** AJ ratified "caddy" / "caddy model" / "memory caddy" as the canonical term for this concept. The caddy/golfer analogy made the mapping precise. Concept-not-product distinction is load-bearing.
- **2026-05-16 ingest (this doc):** file rename `memory-model-third-path.md` → `memory-caddy.md`. New [concept/caddy](../concept/caddy.md) page created as canonical architectural definition. Body terminology refreshed throughout. Past timestamped artifacts (`lint/*`, prior `log.md` entries, `archive/*`) preserve historical "third-path" term.
- **2026-05-16 competitive prior-art survey + Norman rubric read (this session):** completed. Four parallel-agent investigations + two deeper-investigation passes + two paper reads (Norman + MEGa) + partial Spens & Burgess read. Eight new source pages + one new concept page (norman-rubric) + four new incumbent pages created. Norman rubric established as external evaluation framework; post-Norman gap finding documented; competitive landscape mapped (Engramme = different cell, AMI/Humans& = different architectural shape, NeoCognition = stealth unknown, Anthropic+Lampinen = top frontier-lab moat risk). See [norman-rubric](../concept/norman-rubric.md) for full scoring framework; see the **Competitive landscape and Norman rubric validation** section above for the synthesis.
- **2026-05-16 main-window M12 + M13 walkthroughs:** completed. Substrate-antagonism falsification test (AJ-logged after M11) passed: M12 + M13 both read substrate ❌ on persistent / cross-session aspects. Final substrate-antagonism tally: 7/13 hard ❌, 3/13 ⚠, 2/13 ✅, 1/13 ✅ misleading. Three-axis within-family space (policy learnedness × coupling depth × integration depth) survives the full M01-M13 walk; family-level framing well-calibrated. Two new speculations surfaced — M11+M12 may not be independent mechanisms (suggesting smaller-primitive-set decomposition under the matrix-as-rows catalogue), and M13 introduced the first explicitly read-side primitive in the matrix (open question: which other matrix rows have read-side complements).
- **2026-05-17 architecture-design session (side-window):** completed. First detailed architectural specification produced — see [caddy-architecture](../concept/caddy-architecture.md). Headline findings: (a) **Two load-bearing T4s, not four.** Adversarial-pressure pass plus inspiration-not-blueprint triage demoted R5 (read-as-write reconsolidation) as biological constraint not insight; absorbed T_A3 into K2 (same bet, two faces). Surviving load-bearing T4s: T_A1 (auxiliary world-model loss; the MBP-was-dropped bet) and K2+T_A3 (schema-fit-modulated continuous consolidation). Central research risk reduces to one experiment. (b) **MVP architecture distilled to ~17 operations** from the 25-op decomposition, inheriting Memorizing Transformer (read path), EM-LLM (event segmentation), MemTx §4.5 (lightly-finetuned base at 4% pretraining cost), and adding the auxiliary loss as the bet. (c) **Three-direction integration framework** ([caddy-interface-doors](../concept/caddy-interface-doors.md)): D-doors (caddy → golfer, 5 candidates), U-doors (golfer → caddy, 6 candidates), Q-doors (golfer actively probing caddy, 6 candidates; Q-doors AJ-originated mid-session). MVP commits to D2 + U1/U4 + Q1/Q4. (d) **Memorizing Transformer + EM-LLM verbatim reads** completed in-session — closes the only `[pending]` link in the caddy investigation and promotes EM-LLM STUB → full. Major correction: EM-LLM is NOT a sidecar (per-layer per-head KV-cache management inside attention pipeline). (e) **Two new feedback memories saved:** `inspiration_not_blueprint` (drove R5 demotion) and `capabilities_not_policies` (architectural commitments encode capabilities, not policies — drove the multi-layer-query-head refinement away from hard hot/cold partition). (f) **Team-memory extension surfaced.** Out of scope for MVP. The Q/K geometric-alignment property makes team memory feasible at the cold-store boundary; encoder is the shared protocol.
- **Next concrete actions:**
  1. M14-M17 candidate ingest pass (verbatim reads of Buzsáki 2015, Hardt/Nader/Nadel 2013, Schacter & Addis 2007, Frey & Morris 1997 if obtainable; source pages; promote surviving candidates to numbered rows in [[mechanism-gap-matrix]]; walk M14-M17 in the same row-by-row pattern). AJ approved 2026-05-16 to ingest before continuing the walk.
  2. ~~Verbatim re-read of Memorizing Transformer (Wu et al. 2022) — currently cited but not anchored to a `source/*` page (placeholder pending). Closes the only `[pending]` source link in the caddy investigation.~~ **DONE 2026-05-17.** See [source/wu-2022-memorizing-transformer](../source/wu-2022-memorizing-transformer.md). EM-LLM also promoted STUB → full.
  3. Specify candidate MBP-equivalent auxiliary objectives for the LLM-era caddy (reconstruction on stored episodes, retrieval-quality against outcomes, contrastive (problem-pattern → lesson) matching). If no specifiable loss adds signal beyond the LLM's next-token loss, commitment 5 of the caddy collapses and the hypothesis is dead.
  4. Optional (lower priority): walk Modern Hopfield literature (Ramsauer 2020, Krotov 2020) to give the cue-completion-retrieval commitment a mathematical instantiation story; walk continual-learning ML literature (EWC, generative replay, parameter-isolation) to characterise what biology's dual-system architecture buys beyond what direct ML continual-learning solutions achieve.

## Related

- [source/wayne-2018-merlin.md](../source/wayne-2018-merlin.md) — the verbatim-read template for the caddy; structural precedent for joint training of memory + consumer under separate losses; absent from the modern agent-memory survey.
- [source/borgeaud-2022-retro.md](../source/borgeaud-2022-retro.md) — the LLM-era inheritor of MERLIN's read head; load-bearing for the MBP-was-dropped hypothesis.
- [concept/memory-consumer-axis.md](../concept/memory-consumer-axis.md) — Case A vs Case B framing; this investigation tightens the axis to "Case A is overwhelmingly the realised shape."
- [concept/mechanism-gap-matrix.md](../concept/mechanism-gap-matrix.md) — the substrate-path due-diligence input. M03-M13 are the design targets if the caddy is real. M03/M04 PER row is the closest biological/RL analogue for the granularity-ladder's level-1 retrospective signal.
- [concept/substrate-as-memory.md](../concept/substrate-as-memory.md) — the substrate path; this question asks whether substrate-as-memory and memory-as-its-own-model are the same or different.
- [concept/consolidation-channel.md](../concept/consolidation-channel.md) — Kyrja's primary substrate-path wedge; MERLIN's MBP is a worked precedent for the channel's write-side objective being shaped by something other than the consumer's task loss.
- [concept/substrate-paradigms.md](../concept/substrate-paradigms.md) — MERLIN slots into P2 (substrate-as-module) taxonomically; closest historical ancestor of RETRO.
- [source/honcho-docs.md](../source/honcho-docs.md), [incumbent/honcho.md](../incumbent/honcho.md) — the prior-art check that closed claim-3-via-Honcho on 2026-05-15.
- [concept/norman-rubric](../concept/norman-rubric.md) — the externally-defined evaluation framework Kyrja's caddy will be measured against. Five properties + Box 4 benchmark proposal + scoring matrix.
- [source/dong-2025-norman-episodic](../source/dong-2025-norman-episodic.md) — the source paper for the rubric. Direct architectural endorsement of the caddy pattern.
- [source/hassabis-2026-memory-bottleneck](../source/hassabis-2026-memory-bottleneck.md) — Hassabis publicly validates the wedge from the CEO chair at DeepMind.
- [source/spens-2024-hippocampal-rag](../source/spens-2024-hippocampal-rag.md) — cleanest published theoretical map of the caddy concept. Academic only, no spinoff signal.
- [source/pan-2025-mega](../source/pan-2025-mega.md) — in-weights CLS-grounded foil to the sidecar caddy pitch.
- [source/cetin-2024-namm](../source/cetin-2024-namm.md) — Sakana NAMM. Partial proof-of-concept for sidecar shape working commercially (working-memory level, not long-term-memory level).
- [source/fountas-2024-em-llm](../source/fountas-2024-em-llm.md) — current Norman-rubric ceiling at 2.5/5. The empirical baseline to beat.
- [source/lampinen-2025-latent-learning](../source/lampinen-2025-latent-learning.md) — DeepMind paper, Lampinen now at Anthropic. Frontier-lab talent signal.
- [incumbent/engramme](../incumbent/engramme.md), [incumbent/neocognition](../incumbent/neocognition.md), [incumbent/ami-labs](../incumbent/ami-labs.md), [incumbent/humans-and](../incumbent/humans-and.md) — the four new direct/adjacent competitors surveyed 2026-05-16.
- [open-question/reservoir-computing](./reservoir-computing.md) — candidate concrete implementation of the caddy's preconfigured-vocabulary substrate. **Updated 2026-05-17:** the literature-review pass closed pure-RC (Sketch A) as empirically dead — both Pascanu/Jaeger 2011 and Sussillo/Abbott 2009 extended the architecture for hard tasks. Sketch B (S4-shape: structured-trained substrate; partially instantiated by the SSM lineage) and Sketch C (reservoir + writable buffer + off-line consolidation) remain alive. Sketch C is architecturally most distinct from the SSM lineage and from current memory-system designs, making it the most-interesting candidate for caddy-shape architectural exploration.
- [open-question/salience-signal](./salience-signal.md) — load-bearing input variable for caddy commitment 2 (learned consolidation policies) and candidate commitment 6 (STC-shape tagged-intermediate-tier). Surfaced 2026-05-17.
- [concept/lora](../concept/lora.md) — one of the explicitly-named consumer interface options in caddy commitment 4; also an M14-shape solution the LLM toolchain stumbled into.
- [concept/catastrophic-interference](../concept/catastrophic-interference.md) — the architectural problem the caddy must take a position on. The caddy's choice of substrate-shape determines which solution-shape (M11 / M14 / RC / LoRA) it inherits.
- [hypothesis/H42-learned-salience-function](../hypothesis/H42-learned-salience-function.md) — first falsifiable claim derived from the salience-signal question; directly relevant to caddy commitment 2.
- [concept/caddy-architecture](../concept/caddy-architecture.md) — detailed architectural specification (six components, 25 ops, tier labels, prototype scoping). The first concrete answer to "what does the caddy actually look like." Added 2026-05-17.
- [concept/caddy-interface-doors](../concept/caddy-interface-doors.md) — D/U/Q door framework for caddy/golfer integration. Mechanical specification of read/write/query paths. Added 2026-05-17.
- [source/wu-2022-memorizing-transformer](../source/wu-2022-memorizing-transformer.md) — verbatim-read source page. Architectural template for caddy read path; §4.5 is bolt-on viability proof.
- [NOW.md](../NOW.md) — the active question this open-question feeds into.
