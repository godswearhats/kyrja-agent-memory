"""Audit 2 (pre-registered 2026-07-22): FULL-STORE scope-binding census.

Enumerates every extracted memory in a completed Supermemory container (not
just a retrieved top-K) with per-document provenance, and measures the
scope-binding rate over every kernel-entity memory. Also dumps the memories
extracted from the 18 chain sessions verbatim (audit 1's extraction-side
evidence: the stored document content shows what went IN; these memories show
what came OUT).

Usage: python3 audit_census.py <scenario_dir> [container_tag]
Writes <scenario_dir>/audit-census-<tag>.json and prints a summary.
"""
import json, os, re, sys

from supermemory import Supermemory

SM_URL = os.environ.get("SUPERMEMORY_URL", "http://localhost:6767")
SM_KEY = os.environ.get("SUPERMEMORY_API_KEY") or open(
    "api-key").read().strip()


def census(scenario_dir, tag=None):
    fam = json.load(open([os.path.join(scenario_dir, f)
                          for f in os.listdir(scenario_dir)
                          if f.startswith("family-")][0]))
    meta = fam["meta"]
    if tag is None:
        size = os.path.basename(os.path.normpath(scenario_dir))
        tag = f"masq-{meta['domain']}-s{meta['seed']}-{size}-cc"
    scopes = [s["name"] for s in meta["scopes"]]
    kernel = meta["kernel_entity"]                       # e.g. "/checkout"
    param_words = meta["param"].split()                  # e.g. ["rate","limit"]
    sess_by_id = {s["id"]: s for s in fam["world_sessions"]}

    # Kernel-entity memory: names the kernel endpoint EXACTLY (near-miss
    # endpoints like /checkout-admin are excluded by the negative lookahead)
    # and talks about the disambiguated parameter (or a req/s value).
    kernel_re = re.compile(re.escape(kernel) + r"(?![\w-])")
    param_re = re.compile("|".join([re.escape(meta["param"]),
                                    re.escape(meta["unit"]),
                                    r"\breq/s\b"]), re.I)
    scope_re = re.compile("|".join(re.escape(s) for s in scopes), re.I)

    cl = Supermemory(api_key=SM_KEY, base_url=SM_URL, timeout=120.0)
    docs, page = [], 1
    while True:
        r = cl.documents.list(container_tags=[tag], limit=200, page=page)
        batch = r.memories or []
        docs.extend(batch)
        if len(batch) < 200:
            break
        page += 1
    print(f"[census] {tag}: {len(docs)} documents", file=sys.stderr)

    rows = []          # one row per extracted memory
    doc_errors = []
    for i, d in enumerate(docs):
        if i and i % 100 == 0:
            print(f"[census] ...{i}/{len(docs)}", file=sys.stderr)
        try:
            g = cl.documents.get(d.id).model_dump()
        except Exception as e:
            doc_errors.append({"doc": d.id, "err": str(e)[:200]})
            continue
        sid = (g.get("custom_id") or g.get("customId") or "").split(":")[-1]
        kind = sess_by_id.get(sid, {}).get("kind", "?")
        content = g.get("content") or ""
        for m in (g.get("memories") or []):
            txt = (m.get("memory") or m.get("content") or "").strip()
            if not txt:
                continue
            rows.append({
                "doc_id": d.id, "session_id": sid, "session_kind": kind,
                "memory_id": m.get("id"), "memory": txt,
                "is_kernel": bool(kernel_re.search(txt)
                                  and param_re.search(txt)),
                "scope_bound": bool(scope_re.search(txt)),
                "doc_scope_in_content": bool(scope_re.search(content)),
            })

    kern = [r for r in rows if r["is_kernel"]]
    kern_bound = [r for r in kern if r["scope_bound"]]
    chain = [r for r in rows if r["session_kind"].startswith("chain_")]
    chain_bound = [r for r in chain if r["scope_bound"]]
    chain_docs = {r["session_id"] for r in chain}
    all_chain_sids = {s["id"] for s in fam["world_sessions"]
                      if s["kind"].startswith("chain_")}

    out = {
        "tag": tag, "n_documents": len(docs), "n_memories": len(rows),
        "n_kernel_memories": len(kern),
        "n_kernel_scope_bound": len(kern_bound),
        "n_chain_session_memories": len(chain),
        "n_chain_session_memories_scope_bound": len(chain_bound),
        "chain_sessions_with_any_memory": sorted(chain_docs),
        "chain_sessions_missing": sorted(all_chain_sids - chain_docs),
        "doc_errors": doc_errors,
        "kernel_memories": kern,
        "chain_session_memories": chain,
        "all_memories": rows,
    }
    path = os.path.join(scenario_dir, f"audit-census-{tag}.json")
    json.dump(out, open(path, "w"), indent=1)

    print(f"\n=== FULL-STORE CENSUS: {tag} ===")
    print(f"documents: {len(docs)}   extracted memories: {len(rows)}")
    print(f"kernel-entity ({kernel} {meta['param']}) memories: {len(kern)}")
    print(f"  of which scope-bound: {len(kern_bound)} "
          f"({100*len(kern_bound)/len(kern):.0f}%)" if kern else "  (none)")
    print(f"chain-session memories: {len(chain)} from "
          f"{len(chain_docs)}/{len(all_chain_sids)} chain sessions")
    print(f"  of which scope-bound: {len(chain_bound)}")
    if doc_errors:
        print(f"doc fetch errors: {len(doc_errors)}")
    print(f"written: {path}")
    return out


if __name__ == "__main__":
    census(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
