# Phase 2 Generation Manifest

**Started:** 2026-05-22
**Completed:** 2026-05-22
**Generator:** Nils (Indigo)
**Spot-check cell:** Defection x Fantasy (batches 1-3) -- PASSED all quality gates

## Quality Gates (final)

- **File count:** 180/180 (120 event-mode + 60 arc-mode)
- **Candidate count:** 600 event-mode candidates (5 per file), 240 arc-mode sequences (4 per file) = **840 total**
- **Forbidden vocabulary:** PASS (2 borderline edge cases flagged for review -- see notes)
- **Metadata blocks:** PASS (all event-mode files have role/state metadata on every candidate)
- **Candidate counts per file:** PASS (all files have exact expected counts)

### Forbidden vocabulary notes

Two borderline cases for AJ's review (not blocking):
1. `arc-mode/discovery/historical/batch-2.md` line 57: "exposed the scheme" -- counterfactual clause, natural prose usage
2. `arc-mode/reversal/historical/batch-3.md` line 29: "an unexpected visit" -- appears in a structural beat label, not narrative prose

## Progress

### Event-mode Phase A (batches 1-3)

| Pattern | Corporate | Fantasy | Historical | Sci-fi |
|---|---|---|---|---|
| Defection B1-B3 | DONE | DONE | DONE | DONE |
| Discovery B1-B3 | DONE | DONE | DONE | DONE |
| Reversal B1-B3 | DONE | DONE | DONE | DONE |
| Confrontation B1-B3 | DONE | DONE | DONE | DONE |
| Rescue B1-B3 | DONE | DONE | DONE | DONE |

### Event-mode Phase B (batches 4-6, with dedup)

| Pattern | Corporate | Fantasy | Historical | Sci-fi |
|---|---|---|---|---|
| Defection B4-B6 | DONE | DONE | DONE | DONE |
| Discovery B4-B6 | DONE | DONE | DONE | DONE |
| Reversal B4-B6 | DONE | DONE | DONE | DONE |
| Confrontation B4-B6 | DONE | DONE | DONE | DONE |
| Rescue B4-B6 | DONE | DONE | DONE | DONE |

### Arc-mode (batches 1-3)

| Pattern | Corporate | Fantasy | Historical | Sci-fi |
|---|---|---|---|---|
| Defection B1-B3 | DONE | DONE | DONE | DONE |
| Discovery B1-B3 | DONE | DONE | DONE | DONE |
| Reversal B1-B3 | DONE | DONE | DONE | DONE |
| Confrontation B1-B3 | DONE | DONE | DONE | DONE |
| Rescue B1-B3 | DONE | DONE | DONE | DONE |

### Counts

- Event-mode Phase A: 60/60 done
- Event-mode Phase B: 60/60 done
- Arc-mode: 60/60 done
- **Total: 180/180 done -- 840 candidates generated**

### Model tiers used

- **Tier A (Opus 4.7):** Batches 1 and 4 (event), Batch 1 (arc)
- **Tier B (Opus 4.6):** Batches 2 and 5 (event), Batch 2 (arc)
- **Tier C (Sonnet 4.6):** Batches 3 and 6 (event), Batch 3 (arc)
