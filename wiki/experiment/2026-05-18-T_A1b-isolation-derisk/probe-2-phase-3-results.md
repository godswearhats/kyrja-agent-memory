---
type: experiment
name: Probe 2 Phase 3 results — confirmatory rating + blind identification gate
status: PROPOSED
last_ingested: 2026-05-22
sources: []
epistemic_tags: [measured]
tags: [t_a1b, probe-2, phase-3, test-set, rating, caddy]
---

Results from Phase 3 (confirmatory rater filtering) and the blind identification validation gate of the [Probe 2 test set pipeline](./probe-2-test-set-design.md). Phase 3 filters the 840 Phase 2 candidates down to an admitted pool; the blind identification gate tests pattern discriminability on the admitted pool before Phase 4 pair construction begins.

## Hypotheses tested

- [H44-T_A1b-cross-domain-transfer](../../hypothesis/H44-T_A1b-cross-domain-transfer.md) — this page records test-set construction results, not H44 verdict results. H44 remains PROPOSED until the trained encoder is probed.

## Method

### Phase 3: Confirmatory rating

Three context-free rater instances, each running a different model tier, rated all 840 candidates. Each rater received the [rater prompt](../../../experiments/T_A1b-isolation-derisk/pipeline/phase-3-rater-prompt.md) (pattern schemas, 5-point rubric, flag definitions) as system context, then processed candidates in pattern batches.

**Rater configuration:**

| Rater | Model | Batches rated |
|---|---|---|
| rater-1 | Opus 4.7 | All tiers (1-6) × all patterns |
| rater-2 | Opus 4.6 | All tiers (1-6) × all patterns |
| rater-3 | Sonnet 4.6 | All tiers (1-6) × all patterns |

Each rater saw stripped candidates (role/state metadata removed, tier labels removed) and rated independently. No rater saw another's output. Raters also flagged GRANULARITY, COSTUME, OVERLAP, and INCOMPLETE per the rubric.

**Inclusion threshold (pre-registered in [probe-2-test-set-design](./probe-2-test-set-design.md)):** mean ≥ 4.0 AND std < 0.7 across three raters.

### Blind identification gate

A stratified sample of 50 admitted candidates (10 per pattern) was presented to rater-1 (Opus 4.7) with pattern labels stripped. The rater received the five pattern schemas but was asked "which pattern does this most clearly instantiate?" rather than "how well does this instantiate pattern X?" Candidates were shuffled and assigned blind IDs (B-01 through B-50). Arc-mode candidates had structural preambles (scenario summaries, beat-order notes, beat-count lines) stripped to prevent leakage.

**Sample design:** For discovery (where OVERLAP flags concentrated), all 3 candidates with 2+ OVERLAP flags from confirmatory rating were included, with the remaining 7 drawn randomly. Other patterns: 10 random, stratified ~2-3 per domain.

**Pre-registered thresholds:** ≥80% overall accuracy, no single pattern below 60%.

## Results

### Confirmatory rating: admitted pool

`[MEASURED]` **755 / 840 candidates admitted (89.9%).**

| Pattern | Admitted | Total | Rate |
|---|---|---|---|
| Defection | 161 | 168 | 95.8% |
| Discovery | 164 | 168 | 97.6% |
| Reversal | 159 | 168 | 94.6% |
| Confrontation | 158 | 168 | 94.0% |
| Rescue | 113 | 168 | 67.3% |

Rescue's lower admission rate is driven by rescue × corporate event-mode: only 9/30 admitted. Rater notes indicate corporate "rescues" featured financial/reputational/administrative threats rather than present/imminent danger to identifiable parties — the generator interpreted "rescue" too broadly for the corporate domain. The filter correctly removed these borderline candidates. All other pattern × domain cells admit ≥70%.

### Confirmatory rating: inter-rater agreement

`[MEASURED]` **Fleiss' κ = 0.218 (ordinal), 0.356 (binary admit/reject).** Both below the pre-registered ≥0.6 target.

This is a **kappa paradox** — κ is suppressed by extreme prevalence skew, not by actual disagreement. `[MEASURED]` 90%+ of ratings are 5; chance agreement is already ~91% on the binary scale. Observed pairwise within-1 agreement is 93-98% across all rater pairs. The κ metric is structurally unable to distinguish "raters agree because they're all rating high" from "raters agree because the candidates are genuinely strong." Given that the candidates were generated specifically to instantiate the patterns cleanly, high agreement on high scores is the expected and desirable outcome.

**Construct-validity note on κ:** The pre-registered κ ≥ 0.6 target was appropriate as a discriminability check — if the candidates were ambiguous or poorly constructed, κ would be meaningfully high because raters would disagree on *which score to assign*. The ceiling effect (most candidates earning 5) means κ is uninformative here. The pairwise agreement rates (93-98%) and the admission rate distribution across patterns are the more informative quality indicators.

### Confirmatory rating: flags

`[MEASURED]` **17 OVERLAP flags across all raters, 15 on admitted candidates.**

| Flag type | Count | On admitted | Notes |
|---|---|---|---|
| OVERLAP (total) | 17 | 15 | |
| — discovery ↔ defection | ~12 | ~10 | Dominant overlap. 3 admitted discovery candidates flagged by 2+ raters. |
| — rescue ↔ reversal | ~3 | ~2 | Mostly filtered out by admission threshold. |
| — rescue ↔ confrontation | ~2 | ~2 | Minor. |
| GRANULARITY | small | arc-only | Did not affect scores. Confirmed AJ's prediction that this would be arc-specific. |
| COSTUME | negligible | — | |
| INCOMPLETE | negligible | — | |

**Discovery ↔ defection overlap** is a genuine structural feature: "someone discovers that someone else violated a commitment" instantiates both patterns. This is not a test-set defect — it's a property of the pattern schemas that the blind identification gate was designed to quantify.

### Blind identification gate

`[MEASURED]` **Overall accuracy: 46/50 (92%).** Passes the ≥80% threshold.

**Confusion matrix:**

|  | →Defec. | →Disco. | →Rever. | →Confr. | →Rescu. | Acc. |
|---|---|---|---|---|---|---|
| **Defection** | **10** | · | · | · | · | 100% |
| **Discovery** | 2 | **8** | · | · | · | 80% |
| **Reversal** | 1 | · | **8** | · | 1 | 80% |
| **Confrontation** | · | · | · | **10** | · | 100% |
| **Rescue** | · | · | · | · | **10** | 100% |

All patterns ≥60%. Three patterns at 100%. **Gate passes.**

**The four errors:**

| Blind ID | True ID | True → Predicted | Secondary | Confidence | Note |
|---|---|---|---|---|---|
| B-19 | Di-arc-Co2-4 | discovery → defection | discovery | high | OVERLAP-flagged (2+ raters). Rater named true pattern as secondary. |
| B-21 | Di-arc-Sf1-3 | discovery → defection | confrontation | medium | OVERLAP-flagged (2+ raters). Arc emphasizes violation chain. |
| B-49 | R-arc-Co3-02 | reversal → defection | reversal | medium | Merger betrayal reads as commitment violation. True pattern was secondary. |
| B-11 | R-Sf1-3 | reversal → rescue | — | high | EVA scenario; rater saw rescue structure (intervention + save). |

**Discovery → defection asymmetry:** 2/10 discovery candidates misclassified as defection; 0/10 defection candidates misclassified as discovery. Both misclassified discovery candidates were the ones with 2+ OVERLAP flags from Phase 3 — the same ambiguity surfaced in both gates. The third OVERLAP-flagged candidate (Di-Sf6-4) was correctly identified as discovery, with defection noted as secondary.

**Confidence calibration:** `[MEASURED]` 36/38 high-confidence calls correct (95%); 10/12 medium-confidence calls correct (83%). Rater flagged uncertainty where uncertainty existed.

### Construct-validity note

The confirmatory rating measures whether candidates clearly instantiate their *labeled* pattern — it's a quality filter, not a discriminability test. The blind identification gate measures discriminability — whether the pattern is recoverable without the label. Together they answer: "are the admitted candidates clean enough to serve as unambiguous positive examples in retrieval pairs?"

The 92% blind accuracy on a 5-class problem (chance = 20%) with three patterns at 100% indicates the admitted pool is structurally clean. The discovery ↔ defection overlap is bounded (2/10, asymmetric, concentrated in previously-flagged arcs) and informative for Phase 4 distractor design rather than threatening to the pool's validity.

## Limitations

- **Blind identification used one rater (Opus 4.7) not three.** Sufficient for a go/no-go gate on gross confusion but not for precise confusion-rate estimation. The 2/10 discovery→defection rate has wide confidence intervals at n=10.
- **κ target missed.** The ≥0.6 target was pre-registered but is uninformative due to ceiling effect. This is a known statistical property of κ under extreme prevalence skew, not a methodology failure, but the pre-registration should have anticipated it. Future experiments should pre-register an alternative agreement metric (e.g., Gwet's AC1, which handles high-prevalence distributions) alongside κ.
- **Rescue × corporate weakness.** 9/30 event-mode rescue × corporate candidates admitted (30%). The admitted pool has thinner rescue × corporate coverage, which may constrain pair construction in that cell.

## Actionable findings for Phase 4

1. **Avoid using OVERLAP-flagged discovery candidates as distractors for defection pairs** (and vice versa). They are partial structural matches, not clean negatives. Specifically: Di-Sf6-4, Di-arc-Co2-4, Di-arc-Sf1-3.
2. **Rescue × corporate pairs will draw from a shallow pool** (9 event-mode candidates). May need to lean on arc-mode rescue × corporate (which admitted at higher rates) or accept fewer rescue × corporate pairs.
3. **Discovery → defection confusion is asymmetric.** Defection candidates are unambiguous; discovery candidates occasionally read as defection when a commitment-violation chain is prominent. This means defection distractors in discovery pairs are harder than discovery distractors in defection pairs — useful for calibrating the Hard and Adversarial distractor tiers.

## Raw artifacts

- Phase 3 rater prompt: [experiments/T_A1b-isolation-derisk/pipeline/phase-3-rater-prompt.md](../../../experiments/T_A1b-isolation-derisk/pipeline/phase-3-rater-prompt.md)
- Stripped candidates (rater input): [experiments/T_A1b-isolation-derisk/pipeline/phase-3-rating/candidates/](../../../experiments/T_A1b-isolation-derisk/pipeline/phase-3-rating/candidates/)
- Confirmatory rating output: `rater-{1,2,3}/ratings/{defection,discovery,reversal,confrontation,rescue}.jsonl`
- Blind identification prompt: [experiments/T_A1b-isolation-derisk/pipeline/phase-3-rating/blind-identification/prompt.md](../../../experiments/T_A1b-isolation-derisk/pipeline/phase-3-rating/blind-identification/prompt.md)
- Blind identification candidates (stripped, shuffled): [experiments/T_A1b-isolation-derisk/pipeline/phase-3-rating/blind-identification/candidates.md](../../../experiments/T_A1b-isolation-derisk/pipeline/phase-3-rating/blind-identification/candidates.md)
- Blind identification mapping (answer key): [experiments/T_A1b-isolation-derisk/pipeline/phase-3-rating/blind-identification/mapping.json](../../../experiments/T_A1b-isolation-derisk/pipeline/phase-3-rating/blind-identification/mapping.json)
- Phase 2 generation manifest: [experiments/probes/phase-2-candidates/manifest.md](../../../experiments/probes/phase-2-candidates/manifest.md)

## Related

- [probe-2-test-set-design](./probe-2-test-set-design.md) — the methodology pre-registration this page reports results against.
- [probe-2-calibration-record](./probe-2-calibration-record.md) — Phase 1 calibration that preceded this.
- [phase-2-generation-prompts](./phase-2-generation-prompts.md) — the generation pipeline that produced the 840 candidates.
- [H44-T_A1b-cross-domain-transfer](../../hypothesis/H44-T_A1b-cross-domain-transfer.md) — the hypothesis this test set will eventually evaluate.
