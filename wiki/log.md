---
name: Kyrja Wiki Ingest Log
status: living
last_ingested: 2026-05-23
sources: []
tags:
  - exclude-from-graph
---

# Kyrja Wiki — Ingest Log

*Append-only session record. Each entry: what changed, pages created/updated, next entry point. Keep entries ≤15 lines. For full session narratives prior to 2026-05-23, see [archive/log-2026-05-11-to-2026-05-22](./archive/log-2026-05-11-to-2026-05-22.md).*

### 2026-07-25 — Supermemory audit closes: smoke excluded for cause, valid result A=31%, H46 rejected

Nils (indigo). The audit AJ called for found the smoke's A=8% was instrument, not system: cap outage + supermemory-server v0.0.3 silent-failure bug emptied 340/626 docs. Store repaired on the subscription (throttled, health-gated, census-verified; the verification gate caught and blocked two further instrument bugs — a bursty throttle causing connection resets, and a cap-detector false positive on the corpus word "overloaded"). Pre-registered re-run: **A=31%, B-FAIL `set_50`** — below the scope-blind plateau (69%), same B failure as every scope-blind arm. Full-store census: 23 kernel value-memories, 0 scope-bound. H46 REJECTED by its own store-size-0 test; mechanism = discourse-level atomization (scope in aside; extraction severs cross-sentence binding). Pre-reg scorecard honest: P2 (`set_50` disappears) REFUTED — it was never an outage artifact but the canonical scope-blind wrong answer. Next: K/starvation probes, then 14-core sweep (pacing conversation with AJ first).

**Pages created:** experiment/2026-07-25-masq-supermemory-repair.md
**Pages updated:** experiment/2026-07-22-masq-supermemory-smoke.md (excluded-for-cause banner + 3 corrections); hypothesis/H46-consolidation-scope-smear.md (REJECTED); NOW.md

### 2026-07-22 — MASQ Supermemory smoke: below-floor result, held methodology-suspect

Nils (indigo). Ingested the first memory-system-under-test run: Supermemory (Opus-4.8 extraction, validated `claude -p` transport shim after metered-API cost blowout) landed below the scope-blind floor on the smoke core (A=8%, B-FAIL); retrieved memories carried zero scope bindings on both transports. Per AJ's call the result is recorded PRELIMINARY/METHODOLOGY-SUSPECT with pre-registered audit items (full-store census, K sensitivity, format-asymmetry bound, H46 store-size sweep) gating the 14-core sweep.

**Pages created:** experiment/2026-07-22-masq-supermemory-smoke.md; hypothesis/H46-consolidation-scope-smear.md
**Pages updated:** open-question/structured-memory-auto-scope-index.md; incumbent/supermemory.md; index.md; NOW.md

### 2026-06-10 — RL-caddy: fact-tier mechanics, supersession, Rock-3 contesting literature

Nils (indigo). Ingested synthesis from a 2026-06-08 Web-Claude RL learning session (transcript `web-claude-chat.txt`), interrogated against existing commitments. Three threads: (1) the fact/schema split is *format* not just timescale → read-mechanics split (byte payload re-encoded = reason-*about*; latent vector = reason-*with*) + LSM-tree frame where active forgetting = compaction. (2) Supersession solved by *silence-not-delete* (silent-engram primitive), decomposed into detection (*updating* stage) vs disposal (*forgetting* stage); the supersede/refine/multi-value detector is the open problem. (3) Rock 3 ("write policy won't train") now `[CONTESTED]` at the *text* level by Memory-R1/Mem-α/AgeMem/Memory-R2 (abstract-only); latent variant still open. Folded counterfactual-margin reward + multi-horizon critics + two design lemmas into caddy.md as Rock-3 mitigations. Kerros stays parked (MASQ active).

**Pages created:** concept/verbatim-vs-latent-tiers.md, concept/fact-supersession.md, source/yan-2025-memory-r1.md (abstract-only), source/yan-2026-memory-r2.md (abstract-only).
**Pages updated:** concept/caddy.md, concept/silent-engrams.md, concept/caddy-tier-semantics.md, concept/active-stages-framework.md, hypothesis/H34-forgetting-scores.md, index.md, NOW.md.

### 2026-06-08 (eve) — MASQ Gate 1: C3/C4 discriminability PASSED

Nils (indigo). Built + ran Gate 1 (10 blind transcripts; neutral Opus via `claude -p` + AJ by hand) to test whether collision-vs-supersession is legible from *intent*, not wall-clock. Result: human+Opus+key 100% (8/8) on clear items, robust to time/verb misdirection → thesis cell (C3/C4) validated. **Value-awareness hinge** locked (collision ⟺ writer believes no value exists; supersession ⟺ aware a value exists by any route; party-awareness → A-layer). **Recency-default finding**: AJ correctly classified every collision yet reported the recent value = the A/B decoupling, reproduced by hand. Also added the kernel⊕embedding split to the worked-family doc. ONE decision **parked for AJ**: C3 B-layer = surface (capability) vs escalate (policy). Artefacts: `masq/gate1/` (RESULTS.md is the entry point).

**Pages created:** none (wiki experiment page deferred to post-decision).
**Pages updated:** NOW.md.

### 2026-06-08 — MASQ reframe: A+B factorial scientific rebuild

Nils (indigo). AJ's "do the right science, unconstrain" pass reframed MASQ from attribution-only to a statistically-defensible **A+B factorial** benchmark of multi-party-*temporal* memory (A = memory quality, B = decision quality; party×time interaction = headline). Corpus audit found ≈8 independent distinctive events → rebuild not patch; apparatus discarded; reader → Opus. Verbatim-read Du 2026 (2603.07670) and re-read MemoryArena Table 3 (resolved the "40–60%" = PS, SR≈0). Corrected two secondhand wiki errors (replication numbers not in Du; 40–60% is a fair PS gloss). Next: one worked C4 scenario family before any generator.

**Pages created:** experiment/2026-06-08-masq-corpus-audit, decision/masq-ab-factorial-design, source/du-2026-autonomous-memory-survey.
**Pages updated:** decision/masq-paper-as-active-program, concept/multi-party-attribution-gap, concept/benchmark-replication-gap, source/memory-surveys-2026, source/he-2026-memoryarena, NOW.md, index.md.

### 2026-05-23 — Wiki maintenance: NOW.md, log.md, ingest skill, SCHEMA v0.6

Nils (indigo). NOW.md rewritten from 353-line append-log to 65-line state document. Session signposts removed — that role belongs to log.md alone. log.md archived (2507 lines → [archive/log-2026-05-11-to-2026-05-22](./archive/log-2026-05-11-to-2026-05-22.md)) and restarted with ≤15-line entry discipline. Wiki-ingest skill simplified (6 steps → 4). SCHEMA bumped to v0.6.

**Pages updated:** NOW.md, log.md, SCHEMA.md, wiki-ingest SKILL.md.
**Archive created:** archive/log-2026-05-11-to-2026-05-22.md.

### 2026-05-24 — Pre-implementation items #5e and #6 complete

Nils (indigo). Arc-mode pair construction (#5e): 125 retrieval problems (25/pattern) from 219 admitted arc-mode candidates. Arc-mode test set LOCKED. Anti-contamination passed (82,574 snippets, 0 matches). Baseline-floor pre-check (#6): Phi-3-mini layer-20 token-averaged features on the 125 arc-mode problems → 15.2% top-1 (below 20% chance). Target–distractor cosine separation: -0.0001. Floor regime confirmed; SUPPORTED threshold locked at ≥25.2%. All six pre-implementation items complete. Implementation begins next session.

**Pages created:** probe-2-phase-4-arc-results.md.
**Pages updated:** experiment-spec.md (baseline-floor result + raw artifacts), README.md (items #5e/#6 done, status), probe-2-test-set-design.md (arc-mode locked), NOW.md (all items complete, next step = implementation).

### 2026-05-25 — T_A1b isolation de-risk ran → REJECTED; artifacts consolidated

Nils (indigo). The de-risk ran three configs (pure V-JEPA → variance-only → VICReg) and REJECTED the isolated forward-prediction form of H44: a predictable-XOR-high-rank trade-off, with the one valid (rank-347) run retrieving at chance (arc 19.2%, skill +1.1%). Rejection scoped to the isolated auxiliary-only form; coupled formulation + masked-prediction continuation left open. H40 promotion + tier-3-4 wedge reversal HELD pending masked-prediction. Separately, all run artifacts moved out of the `indigo/` workspace into [research/experiments/T_A1b-isolation-derisk/](../experiments/T_A1b-isolation-derisk/) (code rewired, 4 wiki pages' links repointed).

**Pages created:** experiment/.../derisk-run-results.md, open-question/masked-vs-forward-prediction.md.
**Pages updated:** H44 (PROPOSED→REJECTED + scope/outcome), experiment README (→LANDED), multi-field-memory-unit (trajectory_state caveat), index.md, NOW.md.

### 2026-05-25 — wiki-lint

Nils (indigo). Ran lint post-ingest. 28 findings, **0 errors**. The ingest introduced 5 (1 status-mismatch + 4 missing-construct-validity), all fixed in-session; the remaining 28 are pre-existing (2 tagged-page-needs-sources on decision pages, 13 pending-links, 13 missing-CV on older experiment/concept pages) and deferred to a dedicated cleanup. No rule-4 contradictions from the new content. Report at [lint/2026-05-25.md](./lint/2026-05-25.md).

### 2026-05-25 — T_A1b ceiling probe: arc test conflates pattern with vocabulary

Nils (indigo). Ran the training-free full-arc ceiling probe after the de-risk verdict was withdrawn (scale confound). Cosine retrieval at chance on every readout, but a bag-of-words classifier decodes the arc patterns at 82% (clean narrative) / 100% (leaked answer-key scaffolding) — so the test conflates pattern with vocabulary and cannot validate tier-3 *structural* retrieval (hits H44's own "fancy embedding for free" failure mode). Cleaned the test set to a narrative-only canonical file; flagged the tier-3 wedge premise for a drawing-board rethink. Reusable gate recorded: a valid tier-3 test must drive an order-blind baseline (BoW) to chance.

**Pages created:** experiment/2026-05-18-T_A1b-isolation-derisk/ceiling-probe.md; open-question/tier-3-structural-vs-semantic.md
**Pages updated:** H44; probe-2-test-set-design; memory-retrieval-tiers; tier-3-4-as-wedge; caddy-architecture; masked-vs-forward-prediction; NOW; index

### 2026-05-25 — "Kyrja" umbrella split; Kerros research program named + introduced

Nils (indigo). After the ceiling-probe finding, AJ diagnosed that "Kyrja" conflated two distinct goals: a commercial product (memory the *agent* uses, bolt-on) and a research contribution to AGI (memory the *model* thinks with). Named the research program **Kerros** (Finnish: layer/stratum). Dividing line ratified: **integration, not persistence** — a result counts only if it beats a bolt-on control (the boltability gate); the same test sorts wiki content between programs. Beachhead = cross-session continuity. SCHEMA v0.7: optional `program:` field, lazy assignment, chronicle-preserving. First-pass `program: kerros` on the substrate core (4 pages), product-era language scrubbed. tier-3-4-as-wedge deferred (needs a split, not a move).

**Pages created:** concept/kerros.md.
**Pages updated:** SCHEMA.md (v0.7); substrate-as-memory; substrate-paradigms; cross-session-continuity; consolidation-channel; index.md; NOW.md.

### 2026-05-26 — Kerros wide pass: capability map → one bet; integration gate; literature survey

Nils (indigo). Re-graded the mechanism-gap matrix through a refined integration gate (binary → **scaling separation**); the 17 mechanisms collapse to one Kerros bet — **non-frozen weights** (composition read-side, consolidation write-side). M10 reconsolidation excluded (feature-for-biology, bug-for-software). Beachhead moved cross-session-continuity → composition separation. Literature survey (ParamMem, Skill-SD, Experience Compression Spectrum full read) places Kerros in the unoccupied bridge between the scaffold-memory and weight-integration communities; the composition separation is empirically unclaimed in what we checked. Corrected the ParamMem mischaracterisation on the Xu page.

**Pages created:** concept/integration-gate.md; source/zhang-2026-compression-spectrum.md.
**Pages updated:** kerros; xu-2026-agentic-memo; mechanism-gap-matrix; research-backlog-stack-rank (→SUPERSEDED); cross-session-continuity (demoted); consolidation-channel; memory-consumer-axis; index; NOW.

### 2026-05-26 — Borrowed integrity discipline from ARS (silent-failure checks)

Nils (indigo). Mined the ARS skill suite for transferable mechanisms; folded the genuinely-additive ones into our working style as a methodological decision rather than adopting the framework. Three checks: pre-graduation hard-block checklist (notebook→experiment), ground-truth isolation (taint-tracking), independent-reader rule (frame-lock). Concession discipline went to memory, not the wiki. Rejected the Collaboration Depth Rubric (construct validity). Honest provenance flag: the failure taxonomy's primary (Lu 2026 Nature) is unverified — we cite ARS, which we read, not the paper.

**Pages created:** decision/research-integrity-checks.md; source/ars-academic-research-skills.md.
**Pages updated:** concept/evidence-anchoring.md (reciprocal see-also); index.md.

### 2026-05-27 — Factored-operator beachhead: spec locked + Phase 1 validation passed

Nils (indigo). Ingested the composition-separation beachhead — a pre-registered spec (factored-operator task = adjusted-cosine of hidden per-symbol vectors; text-only bolt-on control with no inference-time execution; modular-arith negative control; ceiling-relative thresholds) and a CPU-only Phase-1 task-validation that cleared all three gates with idealised stand-ins: matrix completion separates from lookup/marginals, the fan opens (50%→15% of the table as `k` grows), and the order-blind floor drops to chance once the embeddings are centred+normalised (→ cosine). Phase 2 (real Phi-3 arms) is next.

**Pages created:** experiment/2026-05-26-factored-operator-beachhead/spec.md; experiment/2026-05-26-factored-operator-beachhead/phase1-results.md.
**Pages updated:** concept/integration-gate.md; NOW.md; index.md.

### 2026-05-27 — wiki-lint

Nils (indigo). Ran lint post-ingest. 33 findings, 1 error (pre-existing dangling link in source/ars-academic-research-skills). Exactly one finding was session-introduced — a stray [MEASURED] tag on a Method-section line in phase1-results.md — fixed in-session. Remaining 32 pre-existing/steady-state (3 tagged-page-needs-sources, 13 pending links, 15 missing-CV on older T_A1b pages). No rule-4 contradictions. Report at [lint/2026-05-27.md](./lint/2026-05-27.md).

### 2026-05-27 — Factored-operator beachhead Phase 2: integrated arm pivots QLoRA→full-FT

Nils (indigo). Built the real LLM arms; found the locked "QLoRA Phi-3" integrated arm cannot learn the task — collapses to the label marginal (loss floors at ln C, predicts one class) across every rank/lr, frozen and trainable embeddings, even overfitting 256 examples. A diagnostic ladder (MLP probe on frozen embeds 0.45 → from-scratch tiny transformer learns it → full-FT Qwen2.5-0.5B works, ceiling 0.523 at k=64) localised the failure to the *setup*, not the task or the bet. Revised the spec: integrated arm → full fine-tune, base Phi-3 → small model that full-FTs on 11GB, absolute 40-pt gap → headroom/scaling-relative (this is a gating experiment for our confidence, not peer review). Precondition fix, not goalpost move. The composition separation itself (sample-efficiency + fan-open across k) is still unrun.

**Pages created:** experiment/2026-05-26-factored-operator-beachhead/phase2-results.md.
**Pages updated:** spec.md (revision + status); NOW.md (current state + next step); index.md.

### 2026-05-28 — The substantive run: two gates (existence + efficiency)

Nils (indigo). Ran the bet. AJ's catch split it into two gates: Gate 1 = existence (the Xu-Thm-1 fan-open) — CLEARED at k=64/128 (integrated 0.523/0.500 vs Sonnet bolt-on 0.267/0.167, gap widens then bolt-on floors at chance; k=256=0.277 parked as an under-data artifact). Gate 2 = efficiency (is the *write* cheap enough to be memory, not a retrain) — the question Xu's sample-complexity theorem doesn't reach. First Gate-2 result is negative: the cheapest write (freeze transformer, train only a new symbol's embedding row) fits train but fails to generalise (few-shot at chance, retention exact); diagnosis = underdetermined in parameter space (896-d row, no low-rank prior, data sufficient). Low-rank-constrained write is the pending decider.

**Pages created:** experiment/2026-05-26-factored-operator-beachhead/scaling-and-memory-gates.md; open-question/incremental-integration-cost.md.
**Pages updated:** concept/integration-gate.md (existence-vs-efficiency refinement); concept/consolidation-channel.md (first per-rung write-cost data); spec.md (second-gate pointer); NOW.md (state + next step); index.md.

### 2026-05-30 — Strategy exploration: the write is the whole bet (no committed direction)

Nils (indigo). A strategy session, not an experiment — recorded as exploratory threads, not a chosen path (AJ flagged not to overindex). Key moves: Gate 1's read was *bought with a training write*, so it proves the prize exists but the cheap write is the whole bet; the Gate-2 toy decider parked (reversible — rank built in → low power; wrong substrate). The write question widened to a possible cheap-write-vs-compositional-read trade-off (cheap real-time writes exist but only into non-parametric stores = Xu Ω(k²) bad-composition). AJ's caddy reframed as a co-trained-then-frozen RL controller (operands not grammar; three open rocks incl. NTM/DNC/MERLIN trainability). Market read: new-operands ≈ p90 of paid spend but mostly RAG-served; caddy wins only in the high-composition corner. Next: none queued; if resumed, *measure* the corner, don't run another toy.

**Pages created:** open-question/thinks-with-wedge-sizing.md.
**Pages updated:** open-question/incremental-integration-cost.md (toy decider parked, widened to the trade-off); concept/integration-gate.md (read-bought-with-training-write sharpening); concept/caddy.md (frozen RL-controller framing + rocks); concept/consolidation-channel.md (consolidation-as-credit-assignment lens); experiment/2026-05-26-factored-operator-beachhead/scaling-and-memory-gates.md (decider parked); NOW.md; index.md.

### 2026-05-30 — wiki-lint

Nils (indigo). Ran lint over ~140 pages post-ingest. 39 findings (1 error, 16 warn, 22 info) — **zero session-introduced**. New page clean; fixed 2 pre-existing missing-CV warnings on pages touched today (integration-gate, incremental-integration-cost). 1 error (ars-academic-research-skills dangling link) and 3 tagged-page-needs-sources are carried steady-state from 2026-05-27. No rule-4 contradictions. Report at [lint/2026-05-30.md](./lint/2026-05-30.md).

### 2026-06-07 — MASQ paper becomes the active program; Kerros parked

Nils (indigo). Strategy session (AJ's career reframe: legible artifact first) + Phase 0 execution. MASQ → independent multi-party memory-attribution benchmark paper. Phase 0 passed both gates: kill criterion clean (no benchmark scores who-said-what over a multi-party shared workspace — ~15-benchmark survey + 3 verbatim reads with keyword sweeps at zero hits) and team-data real-corpus feasibility (2,653 sessions/553M tokens, injection straightforward; scrub audit pending). Kerros parked, reversible — no finding superseded; resume threads in NOW.md. kyrja_* retrievers removed from MASQ (independence). New program value `masq-bench`.

**Pages created:** decision/masq-paper-as-active-program.md; concept/multi-party-attribution-gap.md; source/wu-2024-longmemeval.md; source/he-2026-memoryarena.md; source/mei-2026-atm-bench.md.
**Pages updated:** concept/kerros.md (parked status note); open-question/billion-scale-benchmark-gap.md (MASQ-scope sub-question answered: billion-scale gap remains); NOW.md (rewrite); index.md (program blurb + 5 entries).

### 2026-06-07 — wiki-lint

Nils (indigo). Ran lint post-MASQ-ingest over ~145 pages. 38 findings → 37 after fix; **zero session-introduced remain**. The one new finding (multi-party-attribution-gap flagged empty-sources) was a parser limitation — linter reads only inline `sources: [...]`, not block-list YAML; converted my two new sourced pages to inline form. Remainder all steady-state (1 ars dangling error, the 3-page tagged-sources trio, 13 pending-link info, 20 pre-existing missing-CV). No rule-4 contradictions (LongMemEval 49%-Mem0 vs 30%-GPT-4o adjacency cleared as different claims). Flagged parser/author-convention drift for AJ. Report at [lint/2026-06-07.md](./lint/2026-06-07.md).

### 2026-06-07 — SCHEMA v0.7.1 (lint-parser tolerance)

Nils (indigo). Fixed `parse_frontmatter` (lint.py) to read block-list YAML, not just inline `sources: [...]` — block form was silently read as empty, causing a false `tagged-page-needs-sources` warning on today's new pages. Genuinely-empty sources still read falsy (rule 3 intact). Added "Note on list syntax" to § Mandatory frontmatter; version bumped v0.7→v0.7.1. Unit-tested block/inline/empty; full lint run stable at 37 findings (the 3-page tagged-sources trio are genuine `sources: []`, unaffected).

### 2026-06-07 — Cleared tagged-page-needs-sources trio

Nils (indigo). Resolved the 3 steady-state tagged-page-needs-sources findings honestly (no fabricated provenance, per internal-synthesis≠external-evidence). tier-3-structural-vs-semantic → sources=[ceiling-probe.md] (the [MEASURED] BoW-82% genuinely from it); research-backlog-stack-rank → sources=[T_A1b-isolation-derisk/README.md] (cited, descriptive roll-up; SUPERSEDED chronicle). caddy-as-research-program had no source/* or experiment/* citation — its lone [ASSERTED] tagged the strategic decision statement itself (a choice attributed in-prose to AJ+Eira+advisors, not an empirical claim); dropped the mis-scoped tag rather than invent a source. tagged-page-needs-sources now 0.

### 2026-06-09 — Gate 1 folded in; surface rubric locked

Nils (indigo). Gate 1 (blind C3/C4 discriminability, run 2026-06-08) formally ingested: PASSED — 8/8 clear items three-way (AJ ⟷ Opus ⟷ key), traps held; value-awareness = C3/C4 hinge. Parked surface-vs-escalate call RESOLVED with AJ: C3 B-layer pass/fail = SURFACE (fixed-reader argument: B is a probe of what memory delivered; Opus never escalates → escalate-bar flattens the metric). New invariants: B output = (action, conflict_flag); uniform surface-termed preamble on every item → C1/C2/C4 = false-alarm arm; bare-set middle banned pending probe. Worked family amended (§7, authoritative) = generation spec.
**Pages created:** experiment/2026-06-08-masq-gate1-c3c4-discriminability.md.
**Pages updated:** decision/masq-ab-factorial-design.md (B-layer + hinge commitments, gate-1 link); index.md. Next: bare-set boundary probe, then confusable-sibling embedding.

### 2026-06-09 — Bare-set probe LANDED: ban confirmed, generation rules frozen

Nils (indigo). Pre-registered probe (PREREG locked, Opus sealed before AJ's blind pass): bare-set middle is illegible — AJ⟷Opus agreement 0/6 on unmarked items (AJ: UNCLEAR-skew; Opus: COLLISION-skew + one fabricated awareness route). Prediction miss reported: Opus does NOT recency-default on classification; its rule is absence-of-route → collision. Whisper arm 4/4: presupposition verbs admitted as C4 soft markers. New invariant: C3 presupposition scrub (purpose clauses absolute, no comparatives/counterfactual-present). Generation rules now frozen; next = confusable-sibling embedding.
**Pages created:** experiment/2026-06-09-masq-bareset-probe.md.
**Pages updated:** decision/masq-ab-factorial-design.md (ban confirmed + presupposition discipline; rules frozen); index.md. Spec amended: c4-worked-family.md §7.4.

### 2026-06-12 — Rock-3 cluster verbatim reads COMPLETE (4/4); freeze topology opened as uncommitted axis

Nils (indigo). Kerros temporarily active (MASQ paused ~1 wk). Full verbatim reads of all four RL-memory cluster papers; Rock 3 verdict landed: text-level claim survives in all four, convergence always purchased with reward densification (turn-attribution / curriculum+rerollouts / per-action LM-judge / ground-truth shaping). Latent-port question sharpened to "which densifier survives a store an LM judge can't read?". Separately, AJ flagged overcommitment risk on freeze schedules → freeze topology recorded as an explicitly UNCOMMITTED open axis. Bonus: Mem-α's conflict-resolution exclusion = quote-grade third-party statement of MASQ's gap.

**Pages created:** source/wang-2025-mem-alpha.md; source/yu-2026-agemem.md; open-question/freeze-topology.md.
**Pages updated:** source/yan-2025-memory-r1.md + source/yan-2026-memory-r2.md (abstract-only → full-read); concept/caddy.md (Rock 3 cluster-complete + freeze-topology anchor); concept/fact-supersession.md (cluster sightings of the three-case detector confusion); concept/multi-party-attribution-gap.md (training-side corroboration); concept/caddy-vs-bolt-on.md (cluster = bolt-on-with-learned-controller in the wild); NOW.md (rewritten); index.md.

### 2026-06-12 — Citation sweep + STALE full read; MASQ plans updated

Nils (indigo). Citation sweep of the RL-memory cluster (~100 R1 citers, 15 Mem-α citers, arXiv keyword sweep) surfaced STALE (2605.06527) as MASQ's closest temporal-leg neighbor → full verbatim read. Gap claim survives (single-user; commonsense-mediated, no attribution); STALE lacks negative controls — MASQ's false-alarm arm is the missing control. Borrowed into harness pre-reg: repeated-call variance check + grading-robustness note. Sweep also logged structural-credit-assignment papers (Mem-T, TreeMem) as candidate latent-survivable densifiers — unread, queued.

**Pages created:** source/chao-2026-stale.md; (masq-paper/) FUTURE.md, reads/stale-2605.06527-notes.md.
**Pages updated:** concept/multi-party-attribution-gap.md (STALE qualifier + refresh log); concept/fact-supersession.md (CUPMem sighting, fourth case); masq-paper/harness/DESIGN.md §5 (pre-reg additions, AJ approved); NOW.md; index.md.

### 2026-06-12 — Densifier follow-up trio full-read (Mem-T, TreeMem, ElasticMem); Rock-3 latent question answered as far as the literature goes

Nils (indigo). The sweep-queued reads, all three verbatim. Verdict: structural credit assignment (branch-and-average over outcomes) is a replicated, content-free densifier family — Mem-T (retrieval trees + provenance-gated hindsight credit; construction deflates to filtered SFT) and TreeMem (pipeline trees; beats uniform broadcast AND engineered rewards in a controlled comparison) — that ports in principle to an LM-judge-illegible store, but is demonstrated text-only at short horizons, each paper dodging the long write horizon differently. ElasticMem (first RL+latent-memory paper) confirms the latent write cell is empty: read-side-only training over a frozen offline text-derived bank. Freeze pattern now 7/7: no paper updates policies post-deployment. No MASQ contact ("multi-agent" = pipeline roles throughout); gap untouched.

**Pages created:** source/yue-2026-mem-t.md; source/mao-2026-treemem.md; source/feng-2026-elasticmem.md.
**Pages updated:** concept/caddy.md (Rock-3 paragraph: replicated candidate answer + empty-cell clause); concept/fact-supersession.md (Mem-T fifth sighting); open-question/freeze-topology.md (7/7 deployment-freeze); NOW.md (rewritten); index.md.

### 2026-06-30 — MASQ retrieval arms: ranking floors, scope-filter ties oracle

Nils (indigo). First memory-system-under-test arms on MASQ v2. Scope-filter (`WHERE scope`) ties the oracle ceiling 15/15; vector 6/15, bm25 8/15 ≤ paste 9/15 (zero-loss paired, p≤0.03, n=15). Bottleneck is exclusion not recall (retrievers recall target ~2.8/3, flood top-10 with ~5.5 siblings); reader is not the bottleneck (scope-filter ties ceiling without resolution labels); "lexical rescues embedding merge" REJECTED (bm25≈vector). Ingested with construct-validity guardrails per AJ (synthetic + oracle filter → demonstrates the failure mode, does not validate production architecture).

**Pages created:** experiment/2026-06-30-masq-retrieval-arms.md; hypothesis/H45-exclusion-over-recall.md; open-question/structured-memory-auto-scope-index.md.
**Pages updated:** decision/structured-filter-first.md (MASQ controlled anchor + scope caveat); decision/precision-over-recall.md (exclusion-beats-recall, construct-limited); hypothesis/H33-routing-matters.md (method-equivalence strengthens falsifier #3); NOW.md (rewritten — MASQ active); index.md.

### 2026-06-30 — wiki-lint

Nils (indigo). Ran lint over the full tree after the MASQ ingest. 44 findings, **0 errors** (exit 0): 31 missing-construct-validity (warn) + 13 dangling-link-pending (info). 7 construct-validity warnings on this session's authored/edited pages fixed in-session (keyword-proximity edits) and re-verified clean; 24 pre-existing + 13 pending accepted as out of scope. Rule-4 sweep: the bm25≈vector "method barely matters" claim is consistently MEASURED across Thread-5 / structured-filter-first / MASQ — convergence, not contradiction. Report at [lint/2026-06-30.md](./lint/2026-06-30.md). Drift noted (non-acting): per-tag construct-validity rule double-flags consolidated-note experiment pages.
