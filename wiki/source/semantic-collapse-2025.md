---
type: source
name: "Embedding collapse — Semantic Collapse (Denham 2025) and Length-Induced Collapse (ACL 2025)"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [embedding-collapse, recall-cascade, mode-2]
---

## Citation

Two papers covering complementary facets of the production embedding-collapse phenomenon:

1. Denham. *Semantic Collapse in Embedding Space.* SSRN, September 2025.
2. ACL 2025. *Length-Induced Embedding Collapse in PLM-Based Models.*

## Location

- Denham (SSRN): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5547918
- Length-induced (ACL 2025): https://aclanthology.org/2025.acl-long.1396.pdf

## Key claims (with our restatements)

### Semantic-collapse formalization (Denham 2025)

**Paper:** Formalizes embeddings as **neighborhood semantics**, quantifies collapse through entropy. Shows how semantic boundaries disperse within embedding neighborhoods — distinct concepts become close, similar concepts may not be distinguishable.

**Our restatement:** Provides the theoretical scaffolding for the "embedding crowding" claim (mode 2 of the [cascading-failures product](../concept/cascading-failures.md)). The entropy framing is the right primitive — collapse is *measurable*, not just "vibes-y."

### Length-induced collapse (ACL 2025)

**Paper:** Document length systematically causes embedding representations to collapse in PLM-based models. Longer documents → more compressed embeddings, less discriminative.

**Our restatement:** Directly relevant to agentic memory: distilled memories range from short slot-format encodings to long prose dumps. The slot-format-wins-on-cost finding from [Exp 1 + Exp 2](../experiment/2026-05-11-write-quality-variance/README.md) is consistent with avoiding length-induced collapse on the write side — though we have not measured this directly.

### Production observations (vendor consensus)

**Deep-dive synthesis (not formally in these papers):** Production embedding collapse is rare in demos but common at scale. Causes: fine-tuning on narrow domains, repetitive/templated documents (enterprise logs, internal docs), loss of global structure. Manifests as embedding space becoming nearly 1-dimensional. Appears gradually and silently.

**Our restatement:** `[ASSERTED]` from deep-dive prose summarizing vendor reports; the formalization papers above provide the mechanism, vendor reports provide the prevalence claim.

## Relevance to Kyrja

- Anchors the **mode-2 (embedding crowding)** term of the [cascading-failures product](../concept/cascading-failures.md).
- Source for [embedding collapse](../concept/embedding-collapse.md) concept page.
- Complementary to [Weller 2025 LIMIT](./weller-2025-limit.md): LIMIT bounds *representability* (what the dimension *can* encode); collapse describes what real-world embeddings *do* encode (often much less than the bound allows).

## Archive location

Not currently in `library/papers/`. Fetch from SSRN / ACL Anthology to verify specific claims.
