"""Supermemory arm for MASQ v2 — first structured memory-system-under-test.

Supermemory (https://github.com/supermemoryai/supermemory, self-hosted
`supermemory-server` v0.0.3) is an extraction-first memory engine: each ingested
document is chunked, embedded (local ONNX MiniLM), and passed through an LLM
"memory agent" that extracts discrete memories; search returns those memories.

Deployment-shaped ingest: ONE document per world session (writer/day header +
prose), the same units the vector arm retrieves over — this simulates a live
agent ingesting sessions as they happen, and lets the system's own extraction
decide what to keep. Query: the system's native memory search with the same
a_query the other retrieval arms use; results returned in the system's own
relevance order (no re-sorting — the ordering IS part of the system under test).

Extraction model: claude-opus-4-8 via Anthropic's OpenAI-compatible endpoint
(OPENAI_BASE_URL=https://api.anthropic.com/v1, OPENAI_MODEL=claude-opus-4-8 in
~/.supermemory/env) — frontier-LLM rule (AJ 2026-07-01): the native anthropic
provider hardcodes claude-haiku-4-5, which would be a silent confound.

Pre-registered (2026-07-15, before any reader call): K=20 memories per query;
server defaults otherwise (no rerank); endpoints >=13/15 ceiling-class,
<=9/15 plateau-class, 10-12 ambiguous -> seeds decide.

Idempotent: sessions carry custom_id = "<container>:<session_id>"; re-runs
ingest only missing sessions, so a completed container is never re-extracted.
"""
import os, sys, time

from supermemory import Supermemory

SM_URL = os.environ.get("SUPERMEMORY_URL", "http://localhost:6767")
SM_KEY = os.environ.get(
    "SUPERMEMORY_API_KEY",
    "")
K = 20
# 12h: with the proxy throttled to ~150 calls/h and stall-on-cap holding
# requests through a subscription-cap window, a full 626-doc ingest can
# legitimately take most of a night.
INGEST_TIMEOUT_S = 12 * 3600
POLL_S = 20
SELF_HEAL_ROUNDS = 1

_client = None


def _cl():
    global _client
    if _client is None:
        _client = Supermemory(api_key=SM_KEY, base_url=SM_URL, timeout=120.0)
    return _client


def _tag(family, corpus_dir):
    # "-cc" = claude-code-transport extraction (2026-07-21). The earlier
    # untagged containers hold the ~323 API-transport extractions kept as the
    # shim-fidelity comparison set; the experiment reads only "-cc" stores.
    m = family["meta"]
    size = os.path.basename(os.path.normpath(corpus_dir))
    return f"masq-{m['domain']}-s{m['seed']}-{size}-cc"


def _sessions(family):
    """Same retrievable units as arm_vector: every non-empty world session."""
    out = []
    for s in family["world_sessions"]:
        txt = s.get("prose") or s.get("text") or ""
        if txt.strip():
            out.append(s)
    return out


def _existing_custom_ids(tag):
    docs, page = [], 1
    while True:
        r = _cl().documents.list(container_tags=[tag], limit=200, page=page)
        batch = r.memories or []
        docs.extend(batch)
        if len(batch) < 200:
            break
        page += 1
    return {d.custom_id for d in docs if d.custom_id}, docs


def _ingest(family, tag):
    sess = _sessions(family)
    have, docs = _existing_custom_ids(tag)

    # A document whose extraction failed (e.g. the API key ran out of credit
    # mid-ingest) must not satisfy the idempotency check — delete it so it is
    # re-added below, otherwise the store is silently incomplete.
    failed = [d for d in docs if d.status == "failed" and d.custom_id]
    if failed:
        print(f"    [supermemory] {tag}: retrying {len(failed)} failed "
              f"documents", file=sys.stderr)
        for d in failed:
            _cl().documents.delete(d.id)
            have.discard(d.custom_id)

    todo = [s for s in sess if f"{tag}:{s['id']}" not in have]
    if todo:
        print(f"    [supermemory] {tag}: ingesting {len(todo)}/{len(sess)} "
              f"sessions", file=sys.stderr)
        for s in todo:
            content = f"— {s['writer']}, day {s['day']}\n{s.get('prose') or s['text']}"
            _cl().documents.add(content=content, container_tag=tag,
                                custom_id=f"{tag}:{s['id']}")

    # Wait until every session document for this container is done.
    t0 = time.time()
    last = None
    while time.time() - t0 < INGEST_TIMEOUT_S:
        have, docs = _existing_custom_ids(tag)
        pending = [d for d in docs
                   if d.custom_id and d.custom_id.startswith(f"{tag}:")
                   and d.status not in ("done", "failed")]
        failed = [d for d in docs if d.status == "failed"]
        if len(have) >= len(sess) and not pending:
            if failed:
                # An incomplete memory store must never be queried — a graded
                # result on partial ingest would be silently invalid.
                raise RuntimeError(
                    f"supermemory ingest for {tag}: {len(failed)} documents "
                    f"failed extraction; fix the cause (API credit?) and "
                    f"re-run — failed docs are deleted+retried on resume")
            return
        state = (len(have), len(pending))
        if state != last:
            print(f"    [supermemory] {tag}: {len(have)}/{len(sess)} queued, "
                  f"{len(pending)} processing", file=sys.stderr)
            last = state
        time.sleep(POLL_S)
    raise TimeoutError(f"supermemory ingest incomplete for {tag} "
                       f"after {INGEST_TIMEOUT_S}s")


def _zero_yield_docs(tag):
    """Docs whose extraction produced no memories. supermemory-server v0.0.3
    marks a document 'done' even when every LLM call behind it failed (the
    2026-07-22 silent contamination), so done-status alone proves nothing —
    a store is queryable only when every document yielded >=1 memory."""
    _, docs = _existing_custom_ids(tag)
    out = []
    for d in docs:
        if not (d.custom_id or "").startswith(f"{tag}:"):
            continue
        g = _cl().documents.get(d.id).model_dump()
        if not [m for m in (g.get("memories") or [])
                if (m.get("memory") or m.get("content") or "").strip()]:
            out.append(d)
    return out


def _ensure_yield(family, tag):
    """Enforce the ingest-side validity invariant, with one self-heal round."""
    for round_ in range(SELF_HEAL_ROUNDS + 1):
        empty = _zero_yield_docs(tag)
        if not empty:
            return
        if round_ == SELF_HEAL_ROUNDS:
            raise RuntimeError(
                f"supermemory store {tag}: {len(empty)} documents have zero "
                f"extracted memories after {SELF_HEAL_ROUNDS} self-heal "
                f"round(s) — store is contaminated (LLM outage during "
                f"ingest?); refusing to query. Docs: "
                f"{[d.custom_id for d in empty][:10]}...")
        print(f"    [supermemory] {tag}: {len(empty)} zero-yield docs — "
              f"self-heal round {round_ + 1}: delete + re-extract",
              file=sys.stderr)
        for d in empty:
            _cl().documents.delete(d.id)
        _ingest(family, tag)


def arm_supermemory(family, corpus_dir):
    tag = _tag(family, corpus_dir)
    _ingest(family, tag)
    _ensure_yield(family, tag)
    r = _cl().search.memories(q=family["a_query"], container_tag=tag, limit=K)
    results = r.results or []
    if not results:
        return "[No memories retrieved]"
    lines = []
    for m in results:
        mem = getattr(m, "memory", None) or getattr(m, "content", "") or ""
        if str(mem).strip():
            lines.append(f"- {str(mem).strip()}")
    return "[Retrieved memories]\n\n" + "\n".join(lines) + "\n"


if __name__ == "__main__":
    # Smoke: ingest + query one scenario dir given on the command line.
    import json, glob
    d = sys.argv[1]
    fam = json.load(open(glob.glob(os.path.join(d, "family-*.json"))[0]))
    t0 = time.time()
    ctx = arm_supermemory(fam, d)
    print(f"[{time.time()-t0:.0f}s] context ({len(ctx)} chars):\n")
    print(ctx)
