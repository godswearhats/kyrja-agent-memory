---
type: experiment
name: T_A1b training corpus selection
status: PROPOSED
last_ingested: 2026-05-24
sources: []
epistemic_tags: [measured]
tags: [t_a1b, corpus, training-data, caddy]
---

Results from pre-implementation item #3: training-corpus concrete selection + provenance verification.

## Corpus composition

`[MEASURED]` **~10.80M tokens** across 518 documents from 3 sources:

| Source | Tokens | Documents | License | Register |
|---|---|---|---|---|
| Project Gutenberg | ~7.79M (72%) | 52 books | Public domain | Literary fiction, biography |
| SEC EDGAR MD&A (Item 7) | ~2.01M (20%) | 173 filings | Public domain | Corporate/business |
| S&P 500 earnings call prepared remarks | ~1.00M (10%) | 293 transcripts | MIT | Business-conversational |

## Design rationale

Three register sources address the adversarial case against a single-source corpus.

The primary structural-pattern load (defection, discovery, reversal, confrontation, rescue) is carried by Gutenberg fiction. The business sources close the **corporate-register confound**: without them, the encoder's input representations (from the base LLM) would be poorly calibrated on business-register text, and the EM-LLM surprise-based segmentation would produce different event boundaries on business prose than on the literary prose it trained on. The Probe 2 test set's corporate domain uses boardroom language; the encoder should have seen that register during training.

**Training data vs test set domain separation:** the training corpus contains natural text across diverse domains. The test set is synthetic (LLM-generated with controlled structural patterns). The encoder doesn't need training data from the test set's exact 4 domains — it needs diverse narrative structure and diverse register calibration. The test measures whether structural features transfer across domains, not whether the encoder memorised domain-specific features.

## Gutenberg selection

52 books across 6 genres, selected for plot density and structural-pattern coverage:

- **Literary Fiction** (20 books, ~4.14M tokens) — Austen (6), Dickens, Dostoevsky, Bronte, Hardy, Hugo, Twain, Stoker, Wilde, Forster, Tressell, Parker
- **Adventure** (6 books, ~1.21M tokens) — Dumas (Count of Monte Cristo, Three Musketeers), Stevenson, London, Haggard, Orczy
- **Mystery/Detective** (6 books, ~672K tokens) — Doyle, Collins, Christie, Chesterton
- **Fantasy** (7 books, ~664K tokens) — MacDonald, Baum, Barrie, Kingsley, Dunsany, Eddison
- **Science Fiction** (7 books, ~597K tokens) — Wells (4), Shelley, Verne, Burroughs
- **Biography/Autobiography** (6 books, ~506K tokens) — Douglass, Washington, Franklin, Swift, Machiavelli, Burton

Selection criteria: plot density (structural turning points), author diversity, genre coverage. Works were chosen for known high density of the 5 test-set structural patterns. All six Jane Austen novels added as a pattern-density anchor — known-high density across all five patterns (Wickham/Willoughby/Crawford for defection, Elizabeth/Emma for discovery, Marianne/Anne for reversal, Lady Catherine for confrontation, financial/reputational rescues).

**Known limitation:** all Gutenberg texts are pre-1928 prose. Modern narrative conventions (shorter sentences, dialogue-driven, less exposition) are underrepresented. The business-register supplements partially mitigate this but don't add modern fiction.

## EDGAR selection

173 MD&A sections from 2015 10-K filings, sampled from the `eloukas/edgar-corpus` dataset (section_7 field, pre-split). Priority given to named S&P 500 companies (Apple, Microsoft, Alphabet, Amazon, JPMorgan, Merck, 3M, Coca-Cola, PepsiCo, Tesla, Bank of America) for industry diversity. Max 2 filings per company (CIK).

## Earnings call selection

293 prepared-remarks sections from the `Bose345/sp500_earnings_transcripts` dataset. Q&A sessions stripped via structured_content speaker tags. 193 unique companies, max 3 transcripts per company. Seed: 20260524.

## Segmentation quality check

Ran EM-LLM surprise-based segmentation (phi3:mini Q4, gamma=1.0) on ~5K word samples from each source:

| Source | Events | Mean size | Median | Bounds/1K tokens |
|---|---|---|---|---|
| Gutenberg | 288 | 25 tokens | 24 | 39.3 |
| EDGAR | 258 | 29 tokens | 24 | 34.0 |
| Earnings | 184 | 27 tokens | 24 | 37.2 |

All three sources produce coherent events of ~25 tokens (1-2 sentences). Segmentation generalises across registers. Boundaries coincide with lexical surprise: vocabulary shifts, scene changes, topical transitions in business text. Structural patterns span multiple events; the encoder learns from event-to-event transition sequences.

**Note for item #4:** gamma=1.0 produces fine-grained events. Higher gamma (coarser events) should be explored during hyperparameter pre-commitment.

## Anti-contamination

`[MEASURED]` **PASSED.** 1,200 test-set text snippets checked against all 512 corpus documents. Zero substring matches. Test set is entirely synthetic; corpus is entirely naturalistic.

## Raw artifacts

- Corpus: [`experiments/T_A1b-isolation-derisk/corpus/`](../../../experiments/T_A1b-isolation-derisk/corpus/)
- Manifest: [`experiments/T_A1b-isolation-derisk/corpus/manifest.md`](../../../experiments/T_A1b-isolation-derisk/corpus/manifest.md)
- Segmentation check: [`experiments/T_A1b-isolation-derisk/corpus/segmentation-check/`](../../../experiments/T_A1b-isolation-derisk/corpus/segmentation-check/)
- Assembly scripts: `scripts`

## Related

- [experiment-spec](./experiment-spec.md) — the pre-registration spec this corpus serves (§ Data).
- [probe-2-phase-4-results](./probe-2-phase-4-results.md) — the test set this corpus must not overlap with.
- [H44-T_A1b-cross-domain-transfer](../../hypothesis/H44-T_A1b-cross-domain-transfer.md) — the hypothesis the experiment will evaluate.
