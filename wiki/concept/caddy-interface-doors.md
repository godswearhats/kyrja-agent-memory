---
type: concept
name: Caddy interface doors — D-doors, U-doors, Q-doors framework for caddy/golfer integration
status: living
last_ingested: 2026-05-17
sources: [../source/wu-2022-memorizing-transformer.md, ../source/fountas-2024-em-llm.md, ../source/borgeaud-2022-retro.md, ../source/khandelwal-2020-knn-lm.md, ../source/hu-2021-lora.md]
epistemic_tags: [asserted, speculated]
tags: [caddy, architecture, integration, doors, design-vocabulary]
---

## Definition

`[ASSERTED]` **Caddy interface doors** is the architectural-vocabulary framework for describing where data flows between the [caddy](./caddy.md) and the golfer (the LLM consumer), and when in the processing lifecycle. The framework enumerates three categories of door:

- **D-doors (caddy → golfer):** five architectural points where memory content can be injected into the LLM's forward pass
- **U-doors (golfer → caddy):** six architectural points where information from the LLM can flow into the caddy
- **Q-doors (golfer querying-into-caddy):** six mechanisms by which the LLM can actively probe the caddy, beyond passive cross-attention

The framework crosses with six temporal phases (pre-turn, input processing, generation, post-turn, inter-turn, offline consolidation) to produce a matrix of *which doors are active when*.

This page exists because the door framework is referenced by [caddy](./caddy.md), [caddy-architecture](./caddy-architecture.md), [memory-caddy](../open-question/memory-caddy.md), and [memory-consumer-axis](./memory-consumer-axis.md), and because different door choices represent distinct, independently-testable design points (own lifecycle clause of anti-sprawl satisfied).

## Out-doors: caddy → golfer (D1-D5)

`[ASSERTED]` Five architectural candidates for how memory content reaches the LLM's processing:

| Door | Architectural location | Cost | Existing example |
|---|---|---|---|
| **D1** Input-level injection | Before block 1, in embedding space | Cheap; affects everything downstream uniformly | xRAG (one-token prepend) |
| **D2** Cross-attention, single mid-layer | Inserted at one block (~70% depth) | Moderate; one new attention block in the forward pass | [Memorizing Transformer](../source/wu-2022-memorizing-transformer.md) (layer 9 of 12) |
| **D3** Cross-attention, multiple layers | Inserted at several blocks (every Nth layer) | Higher; multiple injection points throughout the stack | [RETRO](../source/borgeaud-2022-retro.md) (every 3rd layer) |
| **D4** Adapter/LoRA modulation | Modulates existing weights at chosen layers; no new attention block | Moderate; caddy outputs parameters, not activations | [MEGa](../source/pan-2025-mega.md)-style (but in-weights, not sidecar) |
| **D5** Logit modulation at output | Final layer; biases the output distribution | Very cheap; very late and shallow | [kNN-LM](../source/khandelwal-2020-knn-lm.md) interpolation |

`[ASSERTED]` Per [caddy](./caddy.md) commitment C4, **text-injection at the prompt level is disallowed** — it collapses the architecture back into bolt-on. D-doors operate at the embedding/activation/parameter/logit level, not the token level.

`[ASSERTED]` **D2/D3 vs D4 have distinct capability profiles**, not just cost/mechanism differences. Cross-attention (D2/D3) carries arbitrary new content via K_mem/V_mem vectors — anything representable in the embedding space can be transmitted. Adapter/LoRA modulation (D4) is constrained by the structure of the base model: per [Hu et al. 2021 § 7.3](../source/hu-2021-lora.md), LoRA-shape ΔW only amplifies directions already latent in W — content the base doesn't encode cannot be transmitted via D4. Choice between activation-injection doors (D2/D3) and parameter-injection door (D4) is therefore a **capability choice, not a cost choice**.

**Current choice (per [caddy-architecture](./caddy-architecture.md)): D2.** Single mid-layer cross-attention at ~70% depth, validated by Memorizing Transformer.

## In-doors: golfer → caddy (U1-U6)

`[ASSERTED]` Six architectural candidates for how information from the LLM reaches the caddy:

| Door | Where | What the caddy gets |
|---|---|---|
| **U1** Raw input tokens | Before block 1 | What the user said, verbatim |
| **U2** Per-layer activations | At any chosen block(s) | The LLM's representation of input at that depth |
| **U3** Attention patterns | At any block | Which tokens attended to which |
| **U4** Per-token surprise / loss signal | During next-token prediction | Where the LLM was confused — gold for selective encoding (Norman N3) |
| **U5** Output logits / sampled tokens | After final layer | What the LLM said |
| **U6** Final hidden state | After block N, before output projection | The LLM's compressed representation of the whole input |

**Current choice: U1 + U4.** Raw input for cue construction; surprise signal for event-boundary segmentation (Norman N2 mechanism from [EM-LLM](../source/fountas-2024-em-llm.md)).

## Query-doors: golfer actively probing caddy (Q1-Q6)

`[ASSERTED]` The third category, surfaced AJ-originated 2026-05-17 mid-architecture-design. D-doors and U-doors describe passive flows — the caddy decides what to push out via D-doors, the LLM's normal forward pass naturally provides U-door inputs. **Neither describes the LLM actively reaching INTO the caddy.**

Six candidate mechanisms, in increasing order of speculative-ness:

| Door | Mechanism | Existing precedent | Tier |
|---|---|---|---|
| **Q1** Cross-attention queries (implicit) | LLM's Q vectors at layer N probe caddy's K-space | RETRO, MemTx, EM-LLM | T1 |
| **Q2** Multi-hop iterative retrieval | LLM queries, processes, generates follow-up query, re-retrieves | ReAct, Self-RAG, FLARE | T1 (at token level) |
| **Q3** Function-calling for memory | LLM emits `<retrieve query="X">` tokens; system parses, retrieves | Function-calling LLMs, MCP servers | T1 (at token level) |
| **Q4** Activation-level query head | Dedicated learned `W_Q_mem` projection at chosen layer; produces query vectors specifically for caddy; all within one forward pass | None at LLM scale | **T4** |
| **Q5** Metacognitive probes | LLM asks "do you know about X?"; caddy returns structured response (confidence, match count, conflicts) | Confidence-based deferral exists; structured probes don't | **T4** |
| **Q6** Caddy as workspace | LLM treats caddy as scratchpad — writes intermediate state to caddy mid-reasoning, reads back later | Working-memory architectures in cog-sci; partial in some agent frameworks | T3-T4 |

`[ASSERTED]` Q1 is the implicit "passive query" door — cross-attention IS a form of the LLM looking into the caddy, but predetermined-and-passive: the golfer always probes through the same fixed cross-attention door, with whatever queries naturally emerge. The golfer cannot decide to "look more" or "look at something specific."

`[ASSERTED]` **Q4 is the architectural primitive the caddy currently commits to.** The dedicated W_Q_mem head, co-trained with the caddy's K-space, is exactly Q4. See [caddy-architecture § Dedicated vs repurposed query head](./caddy-architecture.md#dedicated-vs-repurposed-query-head).

Q2/Q3 are interesting agentic extensions. Q5/Q6 are deeper research questions.

## Cog-sci anchor: cue-driven vs strategic retrieval

`[ASSERTED]` Human memory has two retrieval modes:

- **Cue-driven retrieval (passive)** — something in current context reminds you of something. Fast, automatic, effortless. Matches D-doors.
- **Strategic retrieval (active)** — you deliberately try to recall something specific. Slow, effortful, frontal-cortex-directed. Matches Q4-Q6.

`[ASSERTED]` Both are real properties of human memory. Norman et al. cover both implicitly under their property 3 (selective encoding/retrieval).

`[ASSERTED]` Per [[feedback_inspiration_not_blueprint]], strategic retrieval is a structural insight (the functional need for active probing of memory is real), not a biological constraint. Without it, the caddy is purely reactive. With it, the caddy is *interrogable*.

## Temporal phases

`[ASSERTED]` Memory flow happens in distinct phases:

```
PHASE 1: Pre-turn (user message arrives)
  └→ Cue retrieval based on incoming message
  └→ Memory prepared for injection
     (Caddy reads U1; produces output for D1-D4)

PHASE 2: LLM input processing
  └→ One-shot injection at input (D1), OR
  └→ Continuous injection mid-pass (D2/D3), OR
  └→ Late modulation (D4/D5)
     (Caddy output → golfer; possibly per-token if D3)

PHASE 3: LLM generation
  └→ Per-token injection (only if architecture supports it)
  └→ Each generated token may itself become a new cue
     (Tighter caddy-golfer coupling than Phase 2)

PHASE 4: Post-turn (turn complete)
  └→ Caddy encodes the full turn into hot store
  └→ Surprise/loss signals (U4) determine what's encoded
     (Golfer → caddy; the WRITE path)

PHASE 5: Inter-turn / online consolidation
  └→ Hot-store items may get re-encoded as more context arrives
  └→ Schema-fit decisions get revisited
     (Caddy alone; no LLM involvement)

PHASE 6: Offline / overnight consolidation
  └→ Bulk hot → cold consolidation
  └→ Auxiliary loss training (T_A1!) happens here
  └→ Schema drift (T_A3) accumulates
     (Caddy alone; substantial compute; downtime window)
```

The caddy is active in all six phases. Phase 6 is where the *learning* happens. Phases 1-5 are mostly inference-time operations using whatever the caddy learned in past Phase-6 cycles.

## The matrix view

| Phase | Out-doors active | In-doors active | Query-doors active | What happens |
|---|---|---|---|---|
| 1 Pre-turn | (preparing D-output) | U1 | Q1 (implicit) | Cue retrieval |
| 2 Input processing | D1 / D2 / D3 / D4 | U2 / U3 (continuous) | Q1, possibly Q4 | Memory shapes LLM processing |
| 3 Generation | D2 / D3 / D5 | U4 / U5 (continuous) | Q1, possibly Q2/Q4 | Memory shapes output; output shapes memory |
| 4 Post-turn | — | U1 + U4 + U5 (full turn) | — | Caddy encodes turn |
| 5 Inter-turn | — | — | — | Caddy housekeeping |
| 6 Offline | — | — | — | Caddy training (T_A1) |

## Capabilities not policies

`[ASSERTED]` The door framework is a *capability vocabulary*, not a *routing policy*. Per [[feedback_capabilities_not_policies]]: opening a door = giving the system a capability. Hard-coding what flows through it = baking in policy.

Example: AJ proposed (2026-05-17) splitting memory queries by layer — one layer queries hot store, another queries cold store. This was rejected because it hard-codes a routing policy (hot vs cold) that K2's schema-fit-modulated consolidation was designed to make at runtime. The refined version — two query heads asking different *kinds* of questions (specific events vs general patterns), with the caddy deciding where to look — preserves capability without baking in policy.

## Current door commitments

`[ASSERTED]` Per [caddy-architecture](./caddy-architecture.md):

```
Out-door:     D2 (single mid-layer cross-attention at ~70% depth)
In-doors:     U1 (raw input for cue) + U4 (surprise for selective encoding)
Query-door:   Q1 (cross-attention) + Q4 (dedicated W_Q_mem head)
              The W_Q_mem head is the caddy's commitment to Q4.

Active in:    Phases 1-3 (inference); Phase 4 (encoding);
              Phase 6 (offline auxiliary-loss training).
              Phase 5 inter-turn consolidation: deferred.
```

## Why this matters

- **Names the architectural integration surface concretely.** Future design decisions can be located by door choice rather than relitigated.
- **Distinguishes capability from policy.** The door framework provides the architectural substrate; learned mechanisms (gate, retrieval, consolidation) provide the policy.
- **Maps onto cog-sci retrieval modes.** Q-doors specifically capture the cue-driven vs strategic-retrieval distinction that Norman et al. and broader episodic-memory literature treat as structural.
- **Constrains the experimental program.** The current commitment is D2 + U1/U4 + Q1/Q4. Additional door combinations are deferred research-prototype variants. Each is an independent design point.

## Scope limits

- **Door framework, not implementation.** Specific projection matrices, gate parameters, attention patterns — all downstream of which doors are chosen.
- **Research-prototype-targeted.** Production concerns (rate limiting at door boundaries, throughput, latency) are out of scope.
- **Does not commit to specific door combinations beyond the current set.** Multi-layer integration (D3-shape), per-token coupling (D3 with very fine granularity), Q4+Q5 combinations — all open design space.

## Related

- [[caddy]] — the architectural concept these doors connect
- [[caddy-architecture]] — the detailed architecture; this page is its integration-interface specification
- [[memory-caddy]] — the live open question
- [[memory-consumer-axis]] — Norman endorsement of internal-representations-over-text aligns with the activation-level door choice
- [[consolidation-channel]] — Phase 6 consolidation is the channel's primary operating regime
- [[norman-rubric]] — selective retrieval (N3) and competition (N5) are query-door properties
- [[feedback_capabilities_not_policies]] — discipline that shaped Q-door design
- [[feedback_inspiration_not_blueprint]] — discipline that justified including strategic-retrieval Q-doors (insight) and excluding R5 read-as-write (constraint)

## Source archive

- 2026-05-17 main design session (Nils side-window) — architectural interface deep dive; AJ-originated Q-doors framework; matrix view
- D-doors and U-doors enumerations grounded in [Memorizing Transformer](../source/wu-2022-memorizing-transformer.md), [EM-LLM](../source/fountas-2024-em-llm.md), [RETRO](../source/borgeaud-2022-retro.md), [kNN-LM](../source/khandelwal-2020-knn-lm.md)
