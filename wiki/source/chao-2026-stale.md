---
type: source
name: "Chao et al. 2026 — STALE: implicit-conflict benchmark for single-user latent-state memory"
status: timeless
last_ingested: 2026-06-12
sources: []
tags: [benchmark, memory-eval, implicit-conflict, supersession, masq-neighbor, full-read]
---

> **STATUS: FULL-TEXT READ COMPLETE (2026-06-12, Nils).** Verbatim read of the arXiv full text (main body + appendices A–H, incl. construction pipeline, seed ontology, judge-validation study, CUPMem schema), per [[feedback_load_bearing_sources]]. Page created directly at full-read status. Found via the 2026-06-12 citation sweep of the RL-memory cluster.

## Citation

Hanxiang Chao, Yihan Bai, Rui Sheng, Tianle Li, Yushi Sun. *STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?* arXiv:2605.06527. Wuhan University / CUHK / HKUST. Published 2026-05-07.

## Location

- https://arxiv.org/abs/2605.06527
- PDF: https://arxiv.org/pdf/2605.06527
- Code: https://github.com/icedreamc/STALE — Dataset: https://huggingface.co/datasets/STALEproj/STALE (CC BY 4.0)
- Local archive: pending download to `kyrja/library/papers/`

## What the benchmark actually is (verified)

- **Single-user assistant memory reframed as latent user-state tracking** (§3.1, App. B): each user message is partial, noisy evidence of an evolving latent state S_t over ~104 attributes (10-category seed ontology, Table 4). 400 expert-validated instances; each plants ONE conflict pair (m_o, m_n) in a ~152K-token haystack of 50 sessions (~593 turns), distractors sampled from LongMemEval and filtered against the target attribute (Table 5, §3.4).
- **Implicit Conflict, formally defined** (§3.2): Axiom 1 — m_n renders the old belief invalid under world knowledge; **Axiom 2 — no utterance explicitly negates/corrects/marks obsolescence** (surface negation like "I no longer…" disqualifies). Independent invention of MASQ's bare-set/whisper-verb finding: the conflict must be surface-illegible or the task trivializes.
- **Two conflict types** (§3.3): **Type I co-referential** (same attribute, incompatible values — their supersession analogue; e.g. Seattle → new lease + utilities in Portland) and **Type II propagated** (update to attribute b cascades via commonsense dependency to invalidate attribute a; e.g. broken leg invalidates cycling commute — the dependency chain is never stated).
- **Three probes per instance** (§3.5): **SR** State Resolution (is the old belief still valid?), **PR** Premise Resistance (query falsely presupposes the stale state), **IPA** Implicit Policy Adaptation (downstream request whose safe execution depends on the update). PR ≅ MASQ presupposition machinery; IPA ≅ MASQ B-layer.
- **Construction pipeline** (§3.4, App. D): LLM "Logic Attacker" generates conflicts → strict LLM verifier (rejects syntactically-obvious pairs) → human review of every instance (Accept / Weak Reject / Wrong Type / Reject rubric, App. D.3). ~$0.12/instance. Same shape as MASQ generator v2.

## Headline results (verified, Table 2)

- Best model (Gemini-3.1-pro): **55.2% overall**. Most systems far below; most memory frameworks (Zep, A-mem, mem-0, LiCoMemory) score **below plain GPT-4o-mini**.
- **PR is the collapse dimension**: Gemini-3.1-pro 92% SR vs 30% PR (Type I), 14% (Type II); Qwen3.5-27B falls 76% → 4%. Models comply with stale premises they can explicitly identify as stale.
- **Type II < Type I everywhere** — propagated/cascading invalidation is systematically harder.
- **The current-state adjudication gap** (§4.4, Table 3, LightMem diagnostics): new evidence retrieved in 67.8–77.5% of cases, yet only **3.3%** of co-retrieved old entries judged as needing update; PR failure-despite-visible-new-evidence = **99.0%**. *"Visibility does not imply authority."* Retrieval succeeds; behavior fails.
- **CUPMem** (their prototype, §5, App. F): write-side adjudication — typed two-level state schema, per-slot {KEEP, STALE, REPLACE, UNKNOWN} decisions, schema-guided propagation search, readout constrained to adjudicated state. Same backbone jumps **8.7% → 68.0%** (PR: near-zero → 78/75%). Write-side hygiene, not retrieval, is the lever.

## Methodology worth borrowing ([[feedback_borrow_not_adopt]])

- **Judge validation with error-direction check** (App. E.3): stratified 240-response human study; 95.8% agreement, κ=0.92; crucially FPR 1.5% vs FNR 7.5% — the judge *deflates* rather than inflates. (MASQ's grading is closed-form exact-match, so this burden doesn't arise — but the protocol is mandatory if open-ended grading ever enters.)
- **Repeated-call variance study** (App. E.2): fixed 20-instance subset × 5 repeated target-model calls; report mean±sd; confirm findings hold in every run. Separates serving nondeterminism from benchmark instability. **Adopted into MASQ harness pre-registration 2026-06-12** (harness DESIGN §5).

## The construct-validity hole (our critique)

**No negative controls.** All 400 instances contain a conflict; the correct SR answer is always "the old belief is invalid." A system with a blanket staleness bias — always reject premises, always say things changed — scores well, and the benchmark cannot distinguish paranoia from understanding. Nothing in §3.4/App. D constructs conflict-free control instances. MASQ's C1/C2/C4 false-alarm arm with hit-vs-false-alarm discrimination is exactly the missing control; this contrast is now part of the design rationale on [multi-party-attribution-gap](../concept/multi-party-attribution-gap.md).

## What STALE does NOT cover (the axis separation)

- **One user, one writer — no attribution.** Invalidation operates via commonsense world knowledge (a broken leg precludes cycling); MASQ invalidation operates via *another party's authority* over a shared store (who decided, when, with what standing). STALE structurally cannot pose an attribution question. The multi-party × temporal × decision-quality cell stays empty.
- **One conflict pair, one-shot transition per instance** (own Limitations, App. A): no repeated updates, no coupled propagation, no gradual drift. MASQ chains already exceed this.
- **Schema-dependent fix**: CUPMem requires a hand-built life-domain ontology; their own framing — schema-free state tracking "remains fundamental and far from solved." Team-decision content (MASQ's domain) is schema-free territory.

## Important caveats

- All scenarios LLM-generated (human-validated); distractors from LongMemEval rather than persona-consistent histories — ecological-validity limits acknowledged (App. A).
- LLM-judge scoring (Gemini-3.1-flash-lite) — validated as above, but IPA agreement is lowest (91.3%, all errors conservative).
- Entanglement accepted by design: long-context retrieval ability and instruction-following are confounded with conflict resolution (App. A states this; their evaluation measures the end-to-end pipeline).

## Relevance to Kyrja

- **MASQ positioning**: occupies the *single-user* implicit-conflict cell — the temporal leg of [multi-party-attribution-gap](../concept/multi-party-attribution-gap.md) is no longer empty; the Mem-α exclusion quote now needs a STALE qualifier. Differentiation is clean: commonsense-mediated vs authority-mediated invalidation.
- **Design validation**: independent convergence on implicit-only conflict, premise probes, and decision-layer scoring; "visibility ≠ authority" is the empirical case for MASQ's B-layer.
- **[fact-supersession](../concept/fact-supersession.md)**: CUPMem's UNKNOWN_CURRENT is a fourth case (invalid-but-no-replacement) our three-case detector lacks.
- **Future MASQ extensions** (post-headline, logged in `masq-paper/FUTURE.md`): cross-party cascading invalidation (Type II analogue); reopened-not-redecided state.

## Audit history

- 2026-06-12 — page created at **full-read** status by Nils (indigo); all claims verified against full text with section/table numbers.

## Archive location

arXiv:2605.06527 (HTML full text read 2026-06-12). PDF download to `kyrja/library/papers/` pending.
