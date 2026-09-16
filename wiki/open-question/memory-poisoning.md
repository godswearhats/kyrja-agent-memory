---
type: open-question
name: Memory poisoning and adversarial writes at scale
status: OPEN
last_ingested: 2026-05-12
sources: []
epistemic_tags: [asserted]
tags: [security, adversarial, governance, write-path]
---

## The question

**If one compromised agent (or a prompt-injected agent) writes malicious memories into a pooled store, how does the poison propagate to other agents?** What detection, isolation, and revocation primitives are needed?

Row-level security and per-agent write quotas are mentioned in incumbent docs but not implemented at scale. Memory-poisoning attacks on RAG systems are an emerging research area; the agent-memory variant has the additional risk that compromised memories propagate through *consolidation* (one memory's claim becomes input to another memory's synthesis).

## Why it matters

- **Wedge architecture is pooled.** [org-wide-store-repo-scoped-queries](../decision/org-wide-store-repo-scoped-queries.md) commits to org-wide storage. A poison-blast-radius is the entire org's repo-scoped queries that match the poisoned memory's compound key.
- **Consolidation amplifies.** Once consolidation lands (post-wedge), a poisoned memory could become input to a consolidated insight, masking its provenance and making downstream detection harder. The "self-generating training data" advantage in [rl-target-encoding-vs-consolidation](./rl-target-encoding-vs-consolidation.md) is also a risk surface.
- **Defense vs detection.** Defenses (signed writes, immutable audit, content-policy gates) and detections (drift monitoring, outlier flagging) are different problems with different costs.
- **Adversarial co-evolution.** As detection improves, attackers shift to subtler patterns (small drifts in many memories rather than one obvious lie). The right framing is probably continuous adversarial robustness, not a one-time hardening.

## What evidence would resolve it

- **Threat model.** Who's the adversary — compromised agent, prompt-injected agent, malicious insider, compromised CI pipeline? Each implies a different control surface.
- **Detection benchmark.** Adversarial writes injected into a clean corpus, measured against detection methods (signature drift, content-policy gates, anomaly detection on the embedding space). No public benchmark exists.
- **Per-layer hardening matrix.** Which of the [seven-layer-stack](../concept/seven-layer-stack.md) layers needs its own poison-resistance posture? Admission control is the obvious first defense; governance and consolidation are also exposed.

## Related

- [admission-control](../concept/admission-control.md) — first-line defense; admission gate can incorporate poison-detection signals
- [seven-layer-stack](../concept/seven-layer-stack.md) — governance layer (7th) covers this in the broadest framing
- [multi-agent-governance](./multi-agent-governance.md) — broader governance question; this is the security-specific sub-question
- [worst-case-source](./worst-case-source.md) — adjacent: distillation from degraded sources (non-adversarial cousin)
- Deep-dive §11 Q19 origin: agentic-memory-scaling-deep-dive.md
