---
type: source
name: "MAGMA (arXiv 2601.03236) — adaptive routing for multi-graph memory"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [routing, multi-graph, locomo, retrieval, pending-verbatim-read]
---

## Citation

*MAGMA: Multi-Agent Graph-based Memory Architecture* (paraphrased title pending verbatim read). arXiv:2601.03236.

## Location

- arXiv: https://arxiv.org/abs/2601.03236

## Key claims (with our restatements)

### Adaptive routing ablation on LOCOMO

**Paper:** Reports an ablation in which the adaptive routing policy is removed (queries routed by a single default strategy rather than intent-classified routing). Reported LOCOMO benchmark score drops from **0.700 → 0.637** when routing is removed. The routing-removal drop is reported as larger than the drop from removing any single graph type (temporal, causal, entity).

**Our restatement:** `[ASSERTED]` — paper-reported ablation magnitude. Construct-validity caveats:
- LOCOMO is a single-agent, short-term, chatbot-style conversational benchmark; routing utility at enterprise-scale codebase queries is not measured.
- The "larger drop than any single graph type" comparison is internal to MAGMA's own component set; it does not generalize to "routing always beats single-method retrieval".
- Routing benefit may be specific to MAGMA's particular graph-type combination.

### Architectural claim

**Paper:** Argues that classifying query intent (temporal / causal / entity-based / factual) and routing to the appropriate graph-retrieval strategy outperforms running any single graph type alone.

**Our restatement:** Anchors the load-bearing evidence-for bullet on [H33-routing-matters](../hypothesis/H33-routing-matters.md):23.

## Construct-validity caveats

1. **Not read verbatim.** Per [feedback_load_bearing_sources], the 0.700 / 0.637 magnitudes and the "larger drop than any single graph type" comparison are paraphrased from deep-dive synthesis, not from a verbatim arXiv read. Promote to verbatim-read before any production decision rides on the magnitude.
2. **LOCOMO-only.** No replication on agentic-memory code benchmarks (LongMemEval, BEAM, EMem). The hypothesis derived from this paper (routing > single method) is empirically anchored on chatbot-style workloads.
3. **Vendor-internal ablation.** The ablation is reported by the paper authors on their own architecture; not an independent third-party study of routing-vs-no-routing on diverse architectures.

## Relevance to Kyrja

- Anchors the MAGMA cite on [H33-routing-matters](../hypothesis/H33-routing-matters.md):23 — primary evidence-for bullet.
- Open question on H33: does the MAGMA-LOCOMO finding generalize to enterprise codebase query distributions, or is it confined to conversational settings?

## Archive location

Not in `library/papers/`. Fetch from arXiv 2601.03236 for verbatim verification.
