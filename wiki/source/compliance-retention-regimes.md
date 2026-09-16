---
type: source
name: "Compliance retention regimes — HIPAA, SOX, EU AI Act statutory floors"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [compliance, retention, regulated-enterprise, hipaa, sox, eu-ai-act, pending-verbatim-read]
---

## Citation

Statutory and regulatory retention requirements for three common regulated regimes that bound `retention_floor_years` (F12) from below in the [scale model](../decision/scale-model-audit-corrections.md). This stub captures the *floors* as they are commonly summarized; verbatim verification against current statute / final regulatory text is pending.

## Location

- **HIPAA** — record retention floor commonly cited as 6 years for required documentation. Authoritative reference: U.S. Department of Health and Human Services, *HIPAA Administrative Simplification* — Title 45 CFR §164.530(j). Canonical text: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164
- **SOX** — Sarbanes-Oxley Act §802 records-retention provisions commonly cited as 7 years for audit work papers. 18 U.S.C. §1520. https://www.govinfo.gov/app/details/PLAW-107publ204
- **EU AI Act** — retention obligations for high-risk AI systems run from 6 months (post-market monitoring documentation in some sub-categories) up to 10 years (technical documentation under Article 18 / 19). Final text Regulation (EU) 2024/1689. https://eur-lex.europa.eu/eli/reg/2024/1689/oj

## Key claims (with our restatements)

### Retention floors

**Statute:** HIPAA ~6 years; SOX ~7 years; EU AI Act 6 months – 10 years depending on sub-category.

**Our restatement:** `[ASSERTED]` — three commonly-cited retention floors for the regulated regimes Kyrja's scale model has to bound by. *Construct-validity:* "retention floor" here is a regulatory minimum-hold, not a system-design parameter; what the floor obligates is record-keeping for compliance audit, not specifically agent memory retention. Mapping floor → consolidation-rate-bound is a Kyrja-internal interpretation: a regulated tenant cannot consolidate-away (forget) memory faster than its retention obligation would permit if the memory is in the audited record-keeping scope.

## Construct-validity caveats

1. **Not read verbatim.** Per [load-bearing sources discipline], the specific section / article references on this page are paraphrased from common summaries, not from a verbatim read of the current statutory text. Verbatim verification is required before any load-bearing claim citing this page is upgraded from `[ASSERTED]` to `[MEASURED]`.
2. **Statutes update.** HIPAA, SOX, and EU AI Act texts are amended over time; the floors as summarized are stable but the obligated-records scope can drift.
3. **Floor-to-system mapping is interpretive.** "Memory consolidation cannot run faster than retention floor" is a Kyrja design rule, not a regulatory mandate; the statute mandates record-keeping, not memory-system architecture.

## Relevance to Kyrja

- Bounds `retention_floor_years` (F12) in [scale-model-audit-corrections](../decision/scale-model-audit-corrections.md) from below.
- Anchors [f12-retention-wiring](../open-question/f12-retention-wiring.md) — the open scale-model bug that F12 isn't wired into `simulate()`'s consolidation-rate constraint.

## Archive location

Not in `library/papers/`. Fetch from the linked official URLs (eCFR, GovInfo, EUR-Lex) for verbatim verification.
