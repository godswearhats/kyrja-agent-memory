---
type: source
name: "MOOM (arXiv 2509.11860) — 3-dimensional forgetting scores with competition inhibition"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [forgetting, consolidation, manage-layer, cognitive-inspired, pending-verbatim-read]
---

## Citation

*MOOM* (paraphrased title pending verbatim read). arXiv:2509.11860.

## Location

- arXiv: https://arxiv.org/abs/2509.11860

## Key claims (with our restatements)

### 3-dimensional forgetting score

**Paper:** Scores memories on three dimensions for demotion / forgetting decisions:
1. **Temporal decay** — older memories accumulate decay pressure.
2. **Retrieval reinforcement** — recently-accessed memories resist decay.
3. **Competition suppression** — memories that compete (similar content, overlapping retrieval contexts) inhibit each other; "loser" memories take on additional decay pressure.

The competition signal is sourced from injection-competition logs that are a byproduct of normal retrieval+injection — no extra data collection required.

**Our restatement:** `[ASSERTED]` — paper-anchored architectural claim. The mechanism is novel relative to pure-recency-decay (LRU / Ebbinghaus-curve) approaches because the third dimension uses cross-memory signal rather than per-memory signal.

### Calibration

**Paper:** Reports β=0.9 (access reinforcement weight), α=0.1 (recency weight) as a 9:1 access-to-recency ratio that performs well on the paper's benchmark.

**Our restatement:** `[ASSERTED]` — paper-reported calibration. Construct-validity caveat: calibration is benchmark-specific. Paper benchmark is single-agent chatbot-style; the 9:1 ratio for coding workloads (where temporal-relevance patterns differ — a recent bug fix may matter more than a frequently-accessed stale config note) is not validated.

### Cognitive-science grounding

**Paper:** Frames the competition-inhibition mechanism as cognitive-science-inspired — human forgetting is driven by interference / competition, not just time-since-last-access.

**Our restatement:** Analogical evidence the decomposition is meaningful, not direct empirical validation that the human-memory mechanism transfers to LLM agent memory.

## Construct-validity caveats

1. **Not read verbatim.** Per [feedback_load_bearing_sources], all formula details, β/α magnitudes, and benchmark results on this page are paraphrased from deep-dive synthesis, not from a verbatim arXiv read.
2. **Single-benchmark calibration.** The 9:1 ratio is from one benchmark; cross-domain robustness is unknown.
3. **Chatbot vs. coding workload mismatch.** MOOM's evaluation is single-agent conversational; the [H34-forgetting-scores](../hypothesis/H34-forgetting-scores.md) hypothesis asks whether the mechanism generalizes to coding workloads, which is unmeasured.

## Relevance to Kyrja

- Anchors the MOOM cite on [H34-forgetting-scores](../hypothesis/H34-forgetting-scores.md):23 — primary evidence-for bullet.
- Sibling to [admission-control](../concept/admission-control.md): admission decides what enters; MOOM-style scoring decides what stays.
- Operationalizes one of the four active stages (controlled forgetting) from [active-stages-framework](../concept/active-stages-framework.md).

## Archive location

Not in `library/papers/`. Fetch from arXiv 2509.11860 for verbatim verification.
