---
type: concept
name: Verbatim-vs-latent tiers — facts and schemas differ in format, not just timescale
status: living
last_ingested: 2026-06-10
sources: [../source/wu-2022-memorizing-transformer.md]
epistemic_tags: [asserted, speculated]
tags: [caddy, two-tier, storage-format, read-mechanics, reasoning-with-vs-about, lsm, provenance-web-claude]
---

## Definition

`[ASSERTED]` The caddy's two memory tiers differ in **storage format**, not merely in timescale or hardware location. The **schema tier** stores *latent* representations (learned vectors shaped by the auxiliary loss, consolidated by EMA drift); the **fact tier** stores *verbatim bytes* (the original text span) with a learned representation attached only as a retrieval **key**. This is a third axis orthogonal to the lifecycle axis (just-admitted / consolidated) and the hardware axis (HBM / RAM / NVMe) already named in [caddy-tier-semantics](./caddy-tier-semantics.md).

The format split is forced by the nature of facts. `[ASSERTED]` Facts ("the daughter is named Saoirse", "the key rotates on the 15th") are **arbitrary** (no statistical structure to reconstruct from), require **exact recall** (an approximation is worse than nothing), and are **low-frequency** (one occurrence, no reinforcement). Dense latent storage is lossy by design — its virtue for schemas (compression of regularities) is a fatal flaw for facts (reconstruction = confabulation; "Saoirse" → "Siobhan"). This is the same failure mode as parametric memory in LLMs, where hallucination *is* the reconstruction error of dense lossy storage.

This page exists because the format distinction is load-bearing for the read mechanics, the learning channels, and the supersession problem — referenced by [caddy](./caddy.md), [caddy-architecture](./caddy-architecture.md), [caddy-tier-semantics](./caddy-tier-semantics.md), [fact-supersession](./fact-supersession.md), and [silent-engrams](./silent-engrams.md).

> **Provenance.** The facts-vs-schemas *format* split and the read-mechanics split below originated in a 2026-06-08 Web-Claude session (transcript at `web-claude-chat.txt`), interrogated by Nils on 2026-06-10 per [[feedback_external_claude_conversations]]. They survived interrogation but remain `[SPECULATED]` design proposals, not measured results.

## The core principle: the key indexes, never reconstructs

`[ASSERTED]` In the fact tier, **the vector is only ever the index, never the content.** A stored fact is a row `{id, key_vector, payload_bytes, metadata}`: the `payload` is raw text (bytes), the `key_vector` is the encoder's event representation living in an ANN index (FAISS/HNSW-shape) that points at the payload by id. You never reconstruct the fact from a vector — you retrieve a pointer and fetch the original bytes. That single discipline is what makes "verbatim" actually verbatim and is the precise difference from storing a memory *as* a dense vector.

Mechanically, the fact tier **is a vector-indexed store of text** — the same substrate as RAG. What differs from naive RAG is (a) the key is a *learned* event representation, not an off-the-shelf sentence embedding, and (b) write/retrieve are *policy* decisions, not cosine-threshold lookups. This "rehabilitates RAG": the objection was never that text storage is wrong, it was that retrieval was dumb. The intelligence moves from the encoding into the policy.

## The read-mechanics split

`[SPECULATED]` The injection path differs by tier, and the difference maps cleanly onto the *reason-with* vs *reason-about* distinction:

| | Schema tier | Fact tier |
|---|---|---|
| Key | latent vector | latent vector |
| Payload | latent vector | **bytes (text)** |
| Read path | inject learned vectors directly into cross-attention | **re-encode** retrieved text → hidden states → cross-attention |
| Character | reasoning *with* (never leaves vector space) | reasoning *about* (text re-textualized then re-encoded) |
| Loss profile | lossy-by-design (correct for regularities) | lossless (correct for arbitrary facts) |

`[SPECULATED]` The re-encode-on-read step has a sub-fork (the [Memorizing Transformer](../source/wu-2022-memorizing-transformer.md) / RETRO design space): **(a) store text, re-encode on retrieval** (deterministic, lossless, costs a retrieval-time forward pass) vs **(b) cache the consumer's KV vectors at write time** (faster read, but the cached vectors are lossy and pinned to a frozen-consumer snapshot — reintroducing the confabulation risk the fact tier exists to kill). For the fact tier, option (a) is the format-consistent choice.

`[ASSERTED]` A consequence worth stating plainly: the fact tier is honestly closer to *reasoning-about*, and **that is correct, not a regression.** Facts should be inspectable, supersedable, and exact; the reasoning-*with* aspiration was always really about the schema tier. The original "RAG is something the model reasons about, memory should be something it reasons with" intuition resolves into: *schemas* are reasoned with, *facts* are reasoned about, and a good memory system needs both.

## Two learning channels follow from the format

`[ASSERTED]` Because the consumer-LM gradient can flow into learned representations but **cannot flow into verbatim text** (bytes are not a parameter), the two tiers learn through different channels:

- **Schema tier** — mostly **gradient-trained**: the auxiliary loss and the consumer-LM gradient shape the latent payloads.
- **Fact tier** — mostly **policy-trained**: the *decision* of what text to store / keep / supersede / retrieve is gradient-opaque and is therefore RL territory. The only gradient-trainable parts are the retrieval keys and the cross-attention handling of re-encoded content.

`[SPECULATED]` This is a clean confirmation of the gradient/RL division of labour: the more a tier relies on lossless storage, the more its learning burden shifts from the differentiable signal to the reinforcement signal. See [caddy § Rock 3 mitigations](./caddy.md).

## The maintenance frame: the fact tier is an LSM-tree

`[ASSERTED]` Writes are append-only on the hot path (append payload + key at each event boundary); the expensive maintenance — eviction, silencing, supersession reconciliation — runs offline between sessions. That is structurally a **log-structured merge tree**: a hot append-only log plus background compaction. [seven-layer-stack](./seven-layer-stack.md) already names consolidation as "streaming LSM-style compaction"; this page connects that frame specifically to the fact tier.

`[ASSERTED]` The payoff of the LSM frame: **active forgetting is the compaction policy.** Supersession, staleness, and unbounded growth are all compaction-time concerns, not write-time ones — see [fact-supersession](./fact-supersession.md) for the full development. A purely synchronous "supersede action" on the write path (the instinct in the Web-Claude transcript) is what you reach for when you lack the compaction frame.

## Why this matters

- It turns the two-tier design from a timescale story into a **format + read-path + learning-channel** story, which is what actually determines the mechanics.
- It resolves the founding "reason-with vs reason-about" intuition rather than leaving it as a slogan.
- It makes the fact tier's maintenance (LSM compaction) the natural home for the supersession and forgetting machinery, which the success-case narrative hid.

## Scope limits

- This page is about *format and mechanics*. The *change-over-time* problem (a fact that was true, then changed) is [fact-supersession](./fact-supersession.md).
- It does not settle the re-encode (a) vs KV-cache (b) sub-fork empirically — that is an open implementation question.
- Hardware-tier placement (HBM/RAM/NVMe) and lifecycle state remain the separate axes of [caddy-tier-semantics](./caddy-tier-semantics.md).

## Related

- [caddy-tier-semantics](./caddy-tier-semantics.md) — the orthogonal hardware/lifecycle axes; format is the third axis added here
- [fact-supersession](./fact-supersession.md) — the compaction-time problem this tiering creates
- [caddy](./caddy.md) — commitment 3 (cue-completion retrieval) and Rock 3 (write-policy training)
- [caddy-architecture](./caddy-architecture.md) — the operation set these tiers implement
- [silent-engrams](./silent-engrams.md) — the available/silent/absent primitive the fact tier needs for supersession
- [seven-layer-stack](./seven-layer-stack.md) — "LSM-style compaction" at the consolidation layer
- [[feedback_external_claude_conversations]] — provenance discipline for the Web-Claude-originated pieces

## Source archive

Synthesized 2026-06-10 from the 2026-06-08 Web-Claude transcript (`web-claude-chat.txt`), interrogated against existing wiki commitments. Read-side template grounded in [Memorizing Transformer](../source/wu-2022-memorizing-transformer.md).
