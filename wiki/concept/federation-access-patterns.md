---
type: concept
name: Federation access patterns — what flat-vector + RAG can't express
status: timeless
last_ingested: 2026-05-12
sources: [../source/memory-surveys-2026.md]
epistemic_tags: [asserted, speculated]
tags: [multi-agent, federation, distributed-systems, governance]
---

## The claim

**Cross-agent federated retrieval is structurally different from single-agent retrieval, not just bigger.** The primitive stack that serves single-agent memory — flat vector index + RAG over the agent's own corpus — was not architected to serve federation. Treating "federated memory" as "Pinecone with more shards" misses the requirements that actually distinguish the workload class.

The right analogy is **Spanner-shape primitives applied to vector retrieval**, not horizontal scaling of an existing primitive.

## Single-agent shape

Single-agent retrieval is "this agent at this point in time wants memory similar to this query." Top-k semantic search over the agent's own memory. Permissions are implicit (the agent owns its corpus); provenance is trivial (one source); conflict resolution doesn't fire because there's no second writer.

This is what flat-vector + RAG was designed for. Glean's architecture serves it well. Most incumbent memory products ([cognee](../incumbent/cognee.md), [mem0](../incumbent/mem0.md), [zep](../incumbent/zep.md), [lightmem](../incumbent/lightmem.md), [letta](../incumbent/letta.md)) target this shape.

## Federation shape — four new requirements

At least four primitives that single-agent memory does not need:

1. **Identity-aware filtering.** `[ASSERTED]` Which agents have permission to read which memories? A query-time access-control problem, not just a similarity problem. Existing vector-DB primitives don't natively express "agent A can read agent B's memories about topic X but not topic Y." Closest analogue is row-level security in transactional databases, but the keys are semantic ("topic X") not exact, and the policy surface is wider.

2. **Cross-tenant security.** Preventing memory leakage between customers. Harder than pre-vector-DB tenancy because semantic similarity leaks across what otherwise look like isolated indexes — a vector embedding of "our pricing model" from tenant A may sit close in space to tenant B's pricing model, and naive top-k retrieval would happily surface either.

3. **Provenance tracking.** Which agent produced this memory, when, with what context, why. Required both for security (audit and revocation) and for downstream reasoning (an agent reading another agent's memory needs to know whose claim it is to decide how much to trust it). A flat-vector store carries embeddings, not the lineage of how each one came to be.

4. **Conflict resolution at retrieval time.** If agent A wrote "the customer prefers email" and agent B wrote "the customer prefers SMS," the retrieval layer has to either surface both for the reading agent's reasoning, or surface a synthesised resolution. Today's vector DBs don't have this primitive — they return top-k by similarity and let the caller deal with contradictions.

These aren't engineering-add-ons to a vector DB. They are more like the requirements that distinguish a distributed transactional database from a key-value store. The hard problems are at the architecture layer, not the integration layer.

## Why "Spanner-shape, not Pinecone-with-shards"

Spanner's contribution wasn't horizontal scaling — sharded key-value stores had that. It was offering *transactional consistency* across globally distributed data while preserving the operational properties that made distributed storage usable. The hard parts (TrueTime, Paxos groups, schema-aware sharding) were architectural primitives, not bigger boxes.

Federated agent memory is analogously not "vector retrieval with more nodes." It is the question of *what consistency, security, and conflict primitives* need to exist for a multi-agent system to read across other agents' memories *correctly* — by a definition of correctness the field has not yet formalised (see [multi-agent-consistency](../open-question/multi-agent-consistency.md)).

`[ASSERTED]` This framing is reasoning by analogy to distributed databases, not a direct empirical finding. The hypothesis it conditions is [H31-distributed-systems-mapping](../hypothesis/H31-distributed-systems-mapping.md), which is itself PROPOSED, not validated.

*Construct-validity:* the four-requirements list is a structural argument from first principles plus the [CMU 2603.10062 position paper](../source/memory-surveys-2026.md) framing. It is not a survey of which existing systems do or don't satisfy each requirement — that survey doesn't exist publicly. The list could be wrong by missing a fifth requirement, or by over-stating one (e.g. if cross-tenant semantic leakage turns out to be empirically rare in practice).

## How this maps onto the seven-layer stack

The seven-layer stack ([seven-layer-stack](./seven-layer-stack.md)) was framed for single-tenant single-agent memory. Federation adds at least one new layer — call it **governance + multi-agent consistency** — on top, which no current incumbent ships at all. Effectively this makes the integration-gap moat wider for federation use-cases than for single-agent ones: even if an incumbent shipped 5+ of the seven layers tomorrow, they would still be missing the federation primitives.

This sharpens the moat in the federation segment specifically. It does not by itself say federation is the right wedge to pursue — that is a path-selection question that lives in commercial framing (coral), not here.

## What would falsify

- **Empirical demonstration that flat-vector + RAG suffices.** A federated multi-agent deployment running at non-trivial scale (>10 agents, >1M cross-readable memories) on a flat vector store with no special primitives, performing well on a representative workload that exercises permissions, provenance, and conflict.
- **One of the four requirements collapses.** For example, if cross-tenant semantic leakage turns out to be rare enough in practice that hash-partitioned indexes are sufficient (no special primitive needed), requirement 2 demotes from architectural to operational.
- **A different decomposition turns out cleaner.** If the right primitives are not "identity + tenancy + provenance + conflict" but, say, "scope + audit + reconciliation," and the four-requirements framing turns out to be a less coherent cut than the alternative.

## Related

- [multi-agent-consistency](../open-question/multi-agent-consistency.md) — the consistency-definition question this concept conditions.
- [H31-distributed-systems-mapping](../hypothesis/H31-distributed-systems-mapping.md) — the distributed-DB analogy this concept inherits.
- [H32-eventual-consistency](../hypothesis/H32-eventual-consistency.md) — the wedge's current bet on which consistency model.
- [H35-conflict-rate](../hypothesis/H35-conflict-rate.md) — empirical complement: how often does requirement 4 actually fire?
- [multi-agent-governance](../open-question/multi-agent-governance.md) — broader governance scope: includes the four requirements above plus audit, RBAC, and revocation.
- [seven-layer-stack](./seven-layer-stack.md) — the existing layered framing this concept extends.
- Eira six-questions doc (2026-04-30) §C2 — origin of this concept.
