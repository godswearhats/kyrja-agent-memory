"""Lexical BM25 retrieval arm for MASQ v2.

The companion/foil to `arm_vector`. Vector RAG floors on this benchmark because
the embedder collapses the near-identical scope strings into one neighbourhood
(cos(checkout-web, checkout-api) = 0.869), so it retrieves a clean chain for the
WRONG scope. BM25 is lexical: `checkout-web` and `checkout-api` are different
tokens, not nearby vectors. This arm tests the mechanistic hypothesis directly:

    if the failure is embedding-space scope-merge, lexical retrieval should
    clear the floor; if BM25 *also* floors, the failure is downstream of
    retrieval (the reader cannot exploit a correctly-scoped chain either).

Tokenization is proper IR tokenization — lowercase, split on non-alphanumeric so
hyphens break (`checkout-web` -> `checkout`, `web`). This is the Lucene/ES default
analyzer behaviour, and it is the *strongest fair* configuration for lexical
retrieval here: the shared prefix `checkout` carries ~0 IDF while the distinguishing
suffix (`web`/`api`/`internal`/...) becomes a high-IDF discriminator. Using the
toy `.lower().split()` instead would glue punctuation to tokens (`checkout-web:`)
and unfairly cripple BM25 — we deliberately give lexical its best honest shot.

Okapi BM25 is implemented standalone (k1=1.5, b=0.75, the canonical defaults) to
keep the arm dependency-free, matching `arm_vector`'s self-contained style. The
reader and grader are untouched; this arm differs from paste/lww/ceiling/vector
only in the context string it returns, isolating retrieval strategy as the single
variable.
"""
import math
import re
from collections import Counter

K1 = 1.5
B = 0.75
_TOK = re.compile(r"[a-z0-9]+")


def _tokenize(text):
    return _TOK.findall(text.lower())


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
    parts = [f"— {s['writer']}, day {s['day']}\n  {s.get('prose', s.get('text', ''))}"
             for s in selected]
    return "[Retrieved memories]\n\n" + "\n\n".join(parts) + "\n"


def _bm25_scores(doc_tokens, query_tokens):
    """Okapi BM25 score of each document against the query."""
    N = len(doc_tokens)
    doc_len = [len(d) for d in doc_tokens]
    avgdl = (sum(doc_len) / N) if N else 0.0
    # document frequency per term
    df = Counter()
    doc_tf = []
    for d in doc_tokens:
        tf = Counter(d)
        doc_tf.append(tf)
        for t in tf:
            df[t] += 1
    # idf with the standard BM25 (+0.5) smoothing, floored at 0
    idf = {t: max(0.0, math.log((N - n + 0.5) / (n + 0.5) + 1.0)) for t, n in df.items()}
    q_terms = set(query_tokens)
    scores = []
    for i in range(N):
        tf = doc_tf[i]
        dl = doc_len[i]
        s = 0.0
        for t in q_terms:
            f = tf.get(t, 0)
            if not f:
                continue
            denom = f + K1 * (1.0 - B + B * dl / (avgdl + 1e-9))
            s += idf.get(t, 0.0) * (f * (K1 + 1.0)) / denom
        scores.append(s)
    return scores


def make_bm25_arm(k=10):
    def arm(family, _corpus_dir):
        sess = _sessions(family)
        if not sess:
            return "[No memories retrieved]"
        doc_tokens = [_tokenize(t) for _, t in sess]
        q_tokens = _tokenize(family["a_query"])
        scores = _bm25_scores(doc_tokens, q_tokens)
        k_eff = min(k, len(sess))
        order = sorted(range(len(sess)), key=lambda i: scores[i], reverse=True)[:k_eff]
        selected = [sess[i][0] for i in order]
        return _format(selected)
    return arm


if __name__ == "__main__":
    # Smoke: confirm lexical retrieval separates the confusable scopes that the
    # embedder merged. Three docs, query targets checkout-web.
    docs = [
        ("checkout-web /checkout rate limit set to 500 by Grace", "web"),
        ("checkout-api /checkout rate limit set to 300 by Lena", "api"),
        ("the quarterly planning kickoff happened, scope TBD", "chatter"),
    ]
    dt = [_tokenize(t) for t, _ in docs]
    q = _tokenize("In the context of checkout-web: what is the /checkout rate limit?")
    sc = _bm25_scores(dt, q)
    for (txt, tag), s in zip(docs, sc):
        print(f"  bm25={s:6.3f}  [{tag}]  {txt}")
    print(f"top -> {docs[max(range(len(sc)), key=lambda i: sc[i])][1]} (want: web)")
