---
type: open-question
name: "Freeze topology — what gets frozen, when, and does anything stay unfrozen during use?"
status: OPEN
last_ingested: 2026-06-12
program: kerros
sources: [../concept/caddy.md, ./thinks-with-wedge-sizing.md, ./incremental-integration-cost.md, ../source/yan-2026-memory-r2.md]
epistemic_tags: [speculated]
tags: [kerros, caddy, freeze-topology, training-schedule, continual-rl, exploratory]
---

> **Explicitly UNCOMMITTED (2026-06-12).** AJ's direct instruction: *we have theories about the right path, but we should not commit to what gets frozen when without empirical data.* The "freeze everything parametric at deployment" picture comes from the `[SPECULATED]` 2026-05-30 RL-controller framing on [caddy](../concept/caddy.md) and is **one point in the design space, not a decision**. Future sessions must not inherit frozen-by-default silently. Per [[feedback_capabilities_not_policies]]: freeze *schedule* is a policy; the architecture's only obligation is not to foreclose the options.

## The question

For each parametric piece of the caddy/golfer system, three regimes are available, and the choice is per-component, not global:

1. **Always-frozen after training** (the 2026-05-30 framing's default),
2. **Scheduled thaws** — frozen during use, periodically retrained offline on accumulated experience, redeployed versioned (immutable-infrastructure shape; fits the sleep/consolidation analogy),
3. **Runtime-plastic** — some parameters continue updating during use (biology's actual regime; hippocampus never freezes).

> **Which components sit in which regime, and on what schedule — and what empirical signal would tell us?**

## The component inventory `[SPECULATED]`

Pieces whose freeze status must each be decided (none decided yet): golfer backbone; golfer's memory-interface params (W_Q_mem head, cross-attention block — new params, must be trained at some point); caddy encoder; write/consolidation policy; retrieval policy. The store *contents* are mutable in every regime — the question is only about parameters.

What we actually know:

- The five ratified caddy commitments are **freeze-agnostic**. Commitment 4's "co-trained" constrains training, not deployment.
- "Co-trained" likely means **staged** freezing even at training time: [Memory-R2](../source/yan-2026-memory-r2.md) froze the answer agent while training the memory policy specifically for reward stability; the counterfactual-margin reward sketch (caddy § Rock-3 mitigations) likewise assumes a frozen golfer during caddy training. `[MEASURED for Memory-R2; SPECULATED as transfer]`
- Rock 2 (caddy § 2026-05-30) already records the cost of regime 1: it forfeits RL's headline superpower, continual skill acquisition.

## The RL-continually-unfrozen branch (AJ, 2026-06-12 — to explore)

AJ's instinct: bringing RL into the architecture *lends itself* to leaving some part continuously unfrozen — RL is natively an online-learning framework, and freezing it is the deviation, not the default. Threads to pursue when this question goes active:

- Which single component gives the most value per unit of runtime-plasticity risk? (Candidate intuition: retrieval/query side — short credit horizons, errors recoverable; write-side plasticity compounds errors into the store.)
- What does the continual-RL literature say about plasticity loss / catastrophic forgetting in small policies updated online — is slow per-deployment drift even stable?
- Does regime 3 on *any* component collapse the cheap-write-vs-compositional-read trade-off this framing was built to escape ([incremental-integration-cost](./incremental-integration-cost.md))? If runtime gradient updates are back, what did freezing buy?
- The operand-vs-grammar bound ([thinks-with-wedge-sizing](./thinks-with-wedge-sizing.md)) is a *consequence of regime 1*. A runtime-plastic component is the only path to "new grammar from experience" — which would change the wedge-sizing answer, not just the architecture.

## Interaction: where do schemas live? `[SPECULATED]`

K2+T_A3 (continuous online schema drift — active load-bearing T4) interacts with this axis: if schemas live in policy *weights*, regime 1 forecloses T_A3; if schemas live in the *store as data*, T_A3 survives any freeze regime as operand-level change. Surfaced 2026-06-12; not yet committed either way. This is the sharpest single sub-question because a freeze choice could silently kill a load-bearing research target.

## What evidence would resolve it

- Empirical: per-component ablation in any eventual prototype — train with regime 1 vs 2 vs 3 on one component at a time; pre-register metrics before running ([[feedback_falsifiability_offers]]).
- Literature: continual-RL stability results; whether any of the RL-memory cluster (Memory-R1/R2, Mem-α, AgeMem) updates policies after deployment — **resolved 2026-06-12, all four verified on full read: NONE do.** Every cluster member freezes its policy at deployment; only store contents change in use. Regime 3 has no precedent in this cluster — **and the pattern extends to the three 2026-06-12 follow-up reads ([Mem-T](../source/yue-2026-mem-t.md), [TreeMem](../source/mao-2026-treemem.md), [ElasticMem](../source/feng-2026-elasticmem.md)): all freeze every policy at deployment; 7/7 across the full read set.** ElasticMem even freezes its memory *bank* (read-only, batch-built offline) — the most-frozen design yet seen. Training-time freezing, though, spans both poles: R1/R2/Mem-α each freeze a counterpart model for reward stability, while [AgeMem](../source/yu-2026-agemem.md) trains one unified policy (write + read + answer) jointly with no frozen counterpart — existence proof that joint training-time plasticity converges, at the cluster's shortest horizon.
- Cost accounting: actual price of a scheduled thaw (regime 2) at prototype scale — if cheap, regime 2 dominates regime 1 and the "frozen forever" picture dissolves for free.

## Status

OPEN — no commitment. Created 2026-06-12 from AJ's overcommitment check during the freeze-inventory discussion (session log will carry the narrative).
