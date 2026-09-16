# ATM-Bench (arXiv 2603.01990) — verbatim positioning notes for MASQ

*Read 2026-06-07 (Nils, via verbatim-quote extraction; 100% of paper text covered incl. appendices A–G, exhaustive keyword sweep). Mei, Chen, Yang, Hou, Li, Byrne. Mar 2026. NOTE: survey agent had cited this as "arXiv 2606" — wrong; it is 2603.01990. Closest surface-neighbor to MASQ; the most important kill-criterion check.*

## Party structure: single user, first-person life-log

- §3.1: "the task of retrieving and reasoning over **a user's** long-term, multimodal, and multi-source personal memories."
- §B.3 (annotation rule): "Questions must be written as if asked by **the photo owner** ('Where did I…', 'When did I…')."
- "Resolving Personal References" = resolving entities in the *owner's own* memory (Fig. 1A: "resolve the user's reference ('Grace') by linking to the user's past memory") — referents IN the data, not parties WRITING to a shared store.
- Sweep: speaker 0, workspace 0, multi-party/multi-user 0, who said/decided 0. "Team" = the annotation team (once).

## Tasks (§3.2) and the conflicting-evidence point

- PR (personal references), ME (multi-evidence composition across modalities), MUT (memory update over time), ABS (abstention).
- **Conflicting evidence = temporal recency within one person's records**, not cross-party disagreement: Fig 1(B) "resolves conflicts between booking records and finalized invoices, and **prioritizes later-updated memory entries**"; §F.1 "reconcile conflicting memories by **preferring the most recent and authoritative record**."
- Hard set (§3.3): avg **6.3 evidence items** per query (vs 1.6), evidence span avg 226 days, max 933.

## Corpus & anonymization — REUSABLE TEMPLATE for our team-data scrub

- ~4 years real personal data, informed consent (§3.2, §A.2). Sizes (Table 2): 6,741 emails, 3,759 images, 533 videos; 1,038 QA pairs; ~2.25M-token context.
- **§A.1 pipeline**: VLM risk screening (Qwen2.5-VL-7B + GPT-4o-mini) → automated face blurring → manual redaction (~150 hrs); emails: metadata stripping + **LLM paraphrase to remove linguistic fingerprints** + **synthetic PII injection** (dummy tracking numbers, fictitious addresses). Adopt this shape for MASQ-v2's /mnt/team-data scrub.

## Scoring + headline

- QS = answer-type-aware (EM for numbers, Jaccard for lists, LLM-judge GPT-5-mini for open-ended) (§3.4 Eq. 2–3); **Joint@k = QS × Recall@k** (Eq. 4).
- "<20% on Hard" = **Joint@10**, not raw QS (§1 contribution 4; Table 3: best = Mem0_Agentic 16.0). Oracle-with-gold-evidence on Hard: GPT-5 ≈ 74.7 QS (Table 4) — hard even with perfect retrieval.
- SGM (§4.2): fixed-schema key-value fields (time, location, entities, OCR, tags); "SGM and DM encompass the same information and differ only in how this information is formatted"; +20% over DM on Hard under Oracle (§5.2). **Schema has no authoring-party field.**

## Kill-criterion verdict

**Does NOT test attribution across multiple memory-writing parties.** One person, many modalities/times — orthogonal axis to MASQ's many parties, shared workspace. **Design flag for MASQ:** their MUT result shows recency is a strong conflict-resolution prior → in MASQ's conflicting-needle queries, **vary author and recency independently** or authorship effects will be confounded with recency.
