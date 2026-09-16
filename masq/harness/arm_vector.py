"""OB1-style vector-RAG retrieval arm for MASQ v2.

Reimplements the minimal pgvector core of OB1 (https://github.com/NateBJones-Projects/OB1):
embed every memory, then return the top-k by inner-product against the query. At
n ~= 600 sessions a brute-force numpy inner product is *exact*, so pgvector's HNSW
index (an approximation that only matters at millions of vectors) buys nothing —
we keep the identical retrieval contract without standing up a database. OB1 is
cited as the reference design.

Embedder: Ollama `nomic-embed-text` (768-d, local, free, off the Anthropic cap).
Document/query prefixes follow the model card ("set it up correctly"). The reader
and grader are untouched — this arm differs from paste/lww/ceiling only in the
context string it returns, isolating retrieval quality as the single variable.
"""
import hashlib, json, os, pickle, urllib.request
import numpy as np

OLLAMA = os.environ.get("OLLAMA_HOST", "http://192.168.109.1:11434")
EMB_MODEL = "nomic-embed-text"
_CACHE = os.path.join(os.path.dirname(__file__), ".emb_cache")


def _embed_one(text):
    req = urllib.request.Request(
        f"{OLLAMA}/api/embeddings",
        data=json.dumps({"model": EMB_MODEL, "prompt": text}).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        v = np.asarray(json.load(r)["embedding"], dtype=np.float32)
    n = np.linalg.norm(v)
    return v / (n + 1e-9)   # normalize -> cosine == inner product


def _embed_matrix(texts, cache_key):
    os.makedirs(_CACHE, exist_ok=True)
    h = hashlib.sha256()
    for t in texts:
        h.update(t.encode()); h.update(b"\x00")
    cp = os.path.join(_CACHE, f"{cache_key}_{h.hexdigest()[:12]}.pkl")
    if os.path.exists(cp):
        with open(cp, "rb") as f:
            return pickle.load(f)
    vecs = np.stack([_embed_one("search_document: " + t) for t in texts])
    with open(cp, "wb") as f:
        pickle.dump(vecs, f)
    return vecs


def _sessions(family):
    """All world sessions as retrievable units — the same material paste sees."""
    out = []
    for s in family["world_sessions"]:
        txt = s.get("prose") or s.get("text") or ""
        if txt.strip():
            out.append((s, txt))
    return out


def _format(selected):
    """Retrieved sessions, re-sorted into temporal order for the reader."""
    selected = sorted(selected, key=lambda s: s["day"])
    parts = [f"— {s['writer']}, day {s['day']}\n  {s.get('prose', s.get('text',''))}"
             for s in selected]
    return "[Retrieved memories]\n\n" + "\n\n".join(parts) + "\n"


def make_vector_arm(k=10):
    def arm(family, _corpus_dir):
        sess = _sessions(family)
        if not sess:
            return "[No memories retrieved]"
        texts = [t for _, t in sess]
        meta = family.get("meta", {})
        ck = f"v2_{meta.get('domain','d')}_{meta.get('target_scope','s')}_{len(texts)}"
        seg_v = _embed_matrix(texts, ck)
        q = family["a_query"]
        q_v = _embed_one("search_query: " + q)
        sims = seg_v @ q_v
        k_eff = min(k, len(sess))
        top = np.argsort(sims)[-k_eff:][::-1]
        selected = [sess[i][0] for i in top]
        return _format(selected)
    return arm


if __name__ == "__main__":
    # Smoke: confirm the embedder is reachable and that near-identical scope
    # prose produces near-identical vectors (the merge the benchmark probes).
    a = _embed_one("checkout-web /checkout rate limit set to 500 by Grace")
    b = _embed_one("checkout-api /checkout rate limit set to 300 by Lena")
    c = _embed_one("the quarterly planning kickoff happened, scope TBD")
    print(f"dim={a.shape[0]}")
    print(f"cos(scope-A, scope-B near-identical) = {float(a @ b):.3f}")
    print(f"cos(scope-A, unrelated chatter)      = {float(a @ c):.3f}")
