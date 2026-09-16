---
type: experiment
name: T_A1b isolation de-risk — encoder + predictor probe before full caddy build
status: LANDED
last_ingested: 2026-05-25
sources: [../../source/wu-2022-memorizing-transformer.md, ../../source/fountas-2024-em-llm.md, ../../source/bardes-2024-vjepa.md, ../../source/ge-2024-icae.md]
epistemic_tags: [asserted, speculated]
tags: [t_a1b, jepa, derisk, falsification, pre-registered, caddy]
---

Umbrella for the **T_A1b isolation de-risk experiment** — queue item #1 of the [research backlog stack-rank](../../decision/research-backlog-stack-rank.md). Trains just the encoder and predictor on event-segmented narrative data with a JEPA-style auxiliary loss, in isolation from any LLM consumer or cross-attention integration. Probes the resulting representations for cross-domain structural transferability before committing engineering effort to the full caddy build. Scope: ~1 GPU, weeks not months. Falsification thresholds pre-registered before any code runs, per [[feedback_falsifiability_offers]] discipline. **2026-05-24 amendment:** arc-mode promoted to primary falsifier; event-mode demoted to diagnostic. See [probe-2-test-set-design § Pre-registration amendment log](./probe-2-test-set-design.md#pre-registration-amendment-log).

## Status

**LANDED — REJECTED (2026-05-25).** The run rejected the isolated, auxiliary-only, forward-prediction form of H44: arc-mode retrieval at 19.2% (chance 20%, p=0.62), tying the 15.2% baseline. Mechanism understood (predictable-XOR-high-rank trade-off). Full result, three-config table, and scope in **[derisk run results](./derisk-run-results.md)**. Scope: rejection is of the isolated form; the coupled formulation and the masked-prediction continuation ([masked-vs-forward-prediction](../../open-question/masked-vs-forward-prediction.md)) remain open.

Pre-implementation items (all complete before the run) per [NOW.md § Current sub-task](../../NOW.md#current-sub-task):

| # | Item | Status |
|---|---|---|
| 1 | V-JEPA verbatim read | ✓ done 2026-05-20 ([bardes-2024-vjepa](../../source/bardes-2024-vjepa.md)) |
| 2 | ICAE verbatim read | ✓ done 2026-05-20 ([ge-2024-icae](../../source/ge-2024-icae.md)) |
| 3 | Training-corpus concrete selection + provenance verification | ✓ done 2026-05-24 — [training-corpus-selection](./training-corpus-selection.md). ~10.80M tokens: Gutenberg (52 books inc. all Austen, 6 genres) + EDGAR MD&A (173 filings) + earnings calls (293 transcripts). Segmentation quality check passed. Anti-contamination verified. |
| 4 | Encoder/predictor architecture specifics (base LLM, layer N, dims) | ✓ done 2026-05-24 — Phi-3-mini INT4, layer 20, encoder d_E=384 depth 4, predictor d_P=128 depth 6, causal block masking (24 context + 8 target), γ=1.0, per-event targets. See [experiment-spec § Architecture](./experiment-spec.md#architecture). |
| 5 | Structural-pattern pairing methodology pre-registration | ✓ done — see [Probe 2 test set design](./probe-2-test-set-design.md), [Probe 2 calibration record](./probe-2-calibration-record.md), and the Maren-authored source files |
| 5b | Test set Phase 2 generation | ✓ done 2026-05-22 — 840 candidates across 5 patterns × 4 domains × 3 model tiers. See [manifest](../../../experiments/probes/phase-2-candidates/manifest.md) |
| 5c | Test set Phase 3 filtering + blind ID gate | ✓ done 2026-05-22 — 755/840 admitted (89.9%), blind identification 92% accuracy (46/50). See [Phase 3 results](./probe-2-phase-3-results.md) |
| 5d | Test set Phase 4 pair construction (event-mode) | ✓ done 2026-05-23 — 200 retrieval problems, 4 distractor tiers, event-mode test set LOCKED. See [Phase 4 results](./probe-2-phase-4-results.md) |
| 5e | Test set Phase 4 pair construction (arc-mode) | ✓ done 2026-05-24 — 125 retrieval problems (25/pattern), 4 distractor tiers, arc-mode test set LOCKED. See [Phase 4 arc-mode results](./probe-2-phase-4-arc-results.md) |
| 6 | Baseline-floor pre-check | ✓ done 2026-05-24 — 15.2% top-1 (below chance). Floor regime: ≥10pp threshold → SUPPORTED at ≥25.2%. See [experiment-spec § Baseline-floor result](./experiment-spec.md#baseline-floor--ceiling-pre-check). |

Arc-mode feasibility gate: **PASSED** 2026-05-22 (4/4 mean 5.0). See [probe-2-calibration-record](./probe-2-calibration-record.md). Arc-mode promoted to primary falsifier 2026-05-24.

## Results

**REJECTED.** The full three-config results, the predictable-XOR-high-rank trade-off, the predict-the-mean control, and the scope of the rejection are in **[derisk-run-results.md](./derisk-run-results.md)**. Headline: the one valid (rank-347) run retrieved at chance — arc-mode 19.2% top-1 (chance 20%, baseline 15.2%, p=0.62), predictor skill +1.1%.

## Hypotheses tested

- **[H44-T_A1b-cross-domain-transfer](../../hypothesis/H44-T_A1b-cross-domain-transfer.md)** — primary hypothesis. T_A1b produces representations whose cross-domain analogical retrieval beats a token-averaged baseline by ≥10pp.
- Sub-claim within H44 (failure mode 4): the predictor's internal state encodes position-in-schema-arc decodably. This underwrites the `trajectory_state` field in [multi-field-memory-unit](../../decision/multi-field-memory-unit.md).

## Documents in this folder

- **[derisk-run-results.md](./derisk-run-results.md)** — **the run results (REJECTED).** Three-config table (pure V-JEPA → variance-only → VICReg), the predictable-XOR-high-rank trade-off, the predict-the-mean control, verdict, and scope. Raw artifacts (code, checkpoints, cache) linked.
- **[experiment-spec.md](./experiment-spec.md)** — the full pre-registration. Method (architecture, data, deliberate-deviations), three probes (collapse check, cross-domain structural retrieval, trajectory-state decodability), falsification thresholds, construct-validity notes, precedent-anchored effect-size context.
- **[probe-2-test-set-design.md](./probe-2-test-set-design.md)** — methodology pre-registration for Probe 2's test set: two-mode design (event-mode + arc-mode), event-granularity definition, pattern set, domain set, distractor tiering, anti-contamination, generation pipeline (Phase 1 calibration → Phase 2 LM generation → Phase 3 rater filtering → Phase 4 pair construction), rater protocol, statistical power.
- **[probe-2-calibration-record.md](./probe-2-calibration-record.md)** — the calibration-stage record: the five formal state-machine schemas, operationalisation principles, ratification record from the AJ-Nils calibration session (2026-05-21 → 2026-05-22), seed-draft sweep findings as methodology lessons. Arc-mode feasibility gate: PASSED (4/4 mean 5.0, 2026-05-22).
- **[phase-2-generation-prompts.md](./phase-2-generation-prompts.md)** — prompt templates and execution plan for Phase 2 LM candidate generation. Event-mode and arc-mode prompt templates with locked schemas inlined, forbidden vocabulary per pattern, domain descriptions, pattern-specific constraints, per-pattern worked-example references, three-tier model execution plan (Opus 4.7 / Opus 4.6 / Sonnet 4.6), quality gates.
- **[probe-2-phase-3-results.md](./probe-2-phase-3-results.md)** — Phase 3 confirmatory rating results (755/840 admitted, 3-rater protocol, inter-rater agreement analysis) and blind identification validation gate (92% accuracy, 5×5 confusion matrix, discovery↔defection asymmetry quantified). Actionable findings for Phase 4 pair construction.
- **[probe-2-phase-4-results.md](./probe-2-phase-4-results.md)** — Phase 4 event-mode pair construction results. 200 retrieval problems, 4 distractor tiers, Hard-tier Jaccard caveat documented. Event-mode test set LOCKED (diagnostic).
- **[probe-2-phase-4-arc-results.md](./probe-2-phase-4-arc-results.md)** — Phase 4 arc-mode pair construction results. 125 retrieval problems (25/pattern), 4 distractor tiers, Hard-tier Jaccard caveat documented. Arc-mode test set LOCKED (primary falsifier).
- **[training-corpus-selection.md](./training-corpus-selection.md)** — Training corpus selection results. ~10.80M tokens from 3 sources (Gutenberg + EDGAR MD&A + earnings calls). Segmentation quality check, anti-contamination verification.

## Source artifacts (test-set candidate content)

- **[source/event-seeds-maren.md](./source/event-seeds-maren.md)** — 15 event-mode calibration seeds (5 defection / 5 discovery / 5 reversal × corporate domain), authored by Maren (purple). Voice diversified across 5 registers (present tense / dialogue-driven / first-person / free indirect / embedded document); discovery-mechanism diversified across 9 non-document-mediated and 6 document-mediated; commitment-type diversified across written / verbal / role-based. Each seed carries a role + state metadata line for calibration; metadata is stripped before Phase 3 rater filtering.
- **[source/event-seeds-confrontation-rescue-maren.md](./source/event-seeds-confrontation-rescue-maren.md)** — 10 event-mode calibration seeds (5 confrontation / 5 rescue × corporate domain), authored by Maren (purple), Nils QA'd. Completes five-pattern coverage. Resolution shapes varied (confrontation); threat and intervention types varied (rescue). Same five-register voice distribution.
- **[source/arc-sequences-maren.md](./source/arc-sequences-maren.md)** — 4 arc-mode feasibility-gate sequences (defection × corporate / fantasy / ecclesiastical-historical / sci-fi), authored by Maren (purple). Beat structures varied (4 / 5 / 5 / 6 events); voices varied (dialogue-driven / free indirect / embedded document / present tense); S3 historical is domain-native (1390s Augustinian priory), not corporate-in-period-costume. Gate: PASSED 2026-05-22 (4/4 mean 5.0).

## Cross-stage links

- **Backlog rank**: queue item #1, [research-backlog-stack-rank](../../decision/research-backlog-stack-rank.md).
- **Decision underwritten by this experiment**: [tier-3-4-as-wedge](../../decision/tier-3-4-as-wedge.md) — negative result triggers reversal.
- **Decisions tested by sub-claim**: [multi-field-memory-unit](../../decision/multi-field-memory-unit.md) — trajectory_state field tested by probe 3.
- **Capability under test**: [memory-retrieval-tiers](../../concept/memory-retrieval-tiers.md) — tier 3 (analogical / cross-domain).
- **Architecture this experiment de-risks**: [caddy-architecture](../../concept/caddy-architecture.md) — op T_A1 is the load-bearing T4 here.
- **Open question resolved by this experiment**: [memory-caddy](../../open-question/memory-caddy.md).
- **Related open question**: [m17-jepa-reconciliation](../../open-question/m17-jepa-reconciliation.md) — raised by T_A1b's mechanism interacting with M17.

## Construct-validity note

Probe 2 (the binary verdict probe on H44) measures cross-domain structural retrieval accuracy on a closed pattern × domain test set with pre-registered thresholds (≥10pp lift = SUPPORTED, ≤5pp = REJECTED, 5–10pp = INCONCLUSIVE). The construct-validity gap — whether "structural retrieval on hand-crafted narrative pairs" measures the wedge capability ("tier 3 retrieval on agentic traces") — is addressed in the experiment spec's § Construct-validity note and is the load-bearing extrapolation from probe 2 to wedge claim. Probe 2 is a *necessary* condition for the wedge, not a sufficient one; ecological validity on agent traces is a separate downstream question deferred until H44 is SUPPORTED.
