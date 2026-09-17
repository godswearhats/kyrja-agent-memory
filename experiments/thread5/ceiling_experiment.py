#!/usr/bin/env python3
"""Ceiling effect experiment: same memories, different retrieval quality.

Retrieval tiers:
  T0: No memory (question only)
  T1: BM25 keyword matching
  T2: Semantic embedding (nomic-embed-text)
  T3: Hybrid BM25 + embedding with RRF fusion

For each query × tier, retrieves top-k memories, asks Haiku to answer,
then scores against ground truth using F1 token overlap.

Uses async concurrency for Haiku calls, sequential for embeddings (Ollama).
"""

import anthropic
import asyncio
import json
import os
import re
import sys
import time
import urllib.request

import numpy as np
from rank_bm25 import BM25Okapi

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
HAIKU_MODEL = "claude-haiku-4-5-20251001"
EMBED_MODEL = "nomic-embed-text"
TOP_K = 3
CONCURRENCY = 10

SCRIPT_DIR = os.path.dirname(__file__)
DEFAULT_ENCODINGS = os.path.join(SCRIPT_DIR, "all_encodings.jsonl")
DEFAULT_GT = os.path.join(SCRIPT_DIR, "ground_truth_full.jsonl")
DEFAULT_RESULTS = os.path.join(SCRIPT_DIR, "ceiling_results_full.json")

ENCODINGS_PATH = DEFAULT_ENCODINGS if os.path.exists(DEFAULT_ENCODINGS) else os.path.join(SCRIPT_DIR, "..", "thread1", "pilot_encodings.jsonl")
GROUND_TRUTH_PATH = DEFAULT_GT if os.path.exists(DEFAULT_GT) else os.path.join(SCRIPT_DIR, "ground_truth.jsonl")
RESULTS_PATH = DEFAULT_RESULTS if os.path.exists(DEFAULT_ENCODINGS) else os.path.join(SCRIPT_DIR, "ceiling_results.json")

QA_PROMPT_WITH_CONTEXT = """Answer the question using ONLY the memories provided.
Give a direct, factual answer in 1-3 sentences.

<memories>
{memories}
</memories>

Question: {query}

Answer:"""

QA_PROMPT_NO_CONTEXT = """Answer the following question. If you don't know, say "I don't know."
Give a direct, factual answer in 1-3 sentences.

Question: {query}

Answer:"""


def get_embedding(text, prefix="search_document: "):
    payload = json.dumps({"model": EMBED_MODEL, "prompt": prefix + text}).encode()
    req = urllib.request.Request(
        f"{OLLAMA_HOST}/api/embeddings",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read())
    return np.array(data["embedding"], dtype=np.float32)


def tokenize(text):
    return re.findall(r'\w+', text.lower())


def f1_score(prediction, reference):
    pred_tokens = tokenize(prediction)
    ref_tokens = tokenize(reference)
    if not pred_tokens or not ref_tokens:
        return 0.0
    common = set(pred_tokens) & set(ref_tokens)
    if not common:
        return 0.0
    precision = len(common) / len(pred_tokens)
    recall = len(common) / len(ref_tokens)
    return 2 * precision * recall / (precision + recall)


class MemoryPool:
    """Holds encoded memories and supports multiple retrieval methods."""

    def __init__(self, encodings):
        self.ids = [e["chain_id"] for e in encodings]
        self.texts = [e["intent_outcome"] for e in encodings]
        self.n = len(self.texts)

        print(f"Building indexes for {self.n} memories...", file=sys.stderr)

        # BM25 index
        t0 = time.time()
        tokenized = [tokenize(t) for t in self.texts]
        self.bm25 = BM25Okapi(tokenized)
        print(f"  BM25 index: {time.time()-t0:.1f}s", file=sys.stderr)

        # Embedding index
        t0 = time.time()
        vecs = []
        for i, t in enumerate(self.texts):
            vecs.append(get_embedding(t))
            if (i + 1) % 200 == 0:
                print(f"  Embedded {i+1}/{self.n}...", file=sys.stderr)
        self.embeddings = np.array(vecs)
        self.emb_norms = self.embeddings / np.linalg.norm(self.embeddings, axis=1, keepdims=True)
        print(f"  Embedding index ({self.n} vectors): {time.time()-t0:.1f}s", file=sys.stderr)

    def retrieve_bm25(self, query, k=TOP_K):
        scores = self.bm25.get_scores(tokenize(query))
        top_idx = np.argsort(-scores)[:k]
        return [(self.ids[i], self.texts[i], float(scores[i])) for i in top_idx]

    def retrieve_semantic(self, query, k=TOP_K):
        q_vec = get_embedding(query, prefix="search_query: ")
        q_norm = q_vec / np.linalg.norm(q_vec)
        sims = self.emb_norms @ q_norm
        top_idx = np.argsort(-sims)[:k]
        return [(self.ids[i], self.texts[i], float(sims[i])) for i in top_idx]

    def retrieve_hybrid(self, query, k=TOP_K, rrf_k=60):
        bm25_scores = self.bm25.get_scores(tokenize(query))
        bm25_ranking = np.argsort(-bm25_scores)

        q_vec = get_embedding(query, prefix="search_query: ")
        q_norm = q_vec / np.linalg.norm(q_vec)
        sims = self.emb_norms @ q_norm
        sem_ranking = np.argsort(-sims)

        rrf_scores = np.zeros(self.n)
        for rank, idx in enumerate(bm25_ranking):
            rrf_scores[idx] += 1.0 / (rrf_k + rank + 1)
        for rank, idx in enumerate(sem_ranking):
            rrf_scores[idx] += 1.0 / (rrf_k + rank + 1)

        top_idx = np.argsort(-rrf_scores)[:k]
        return [(self.ids[i], self.texts[i], float(rrf_scores[i])) for i in top_idx]


def build_prompt(query, memories):
    if not memories:
        return QA_PROMPT_NO_CONTEXT.format(query=query)
    mem_text = "\n\n".join(f"[Memory {i+1}]\n{text}" for i, (_, text, _) in enumerate(memories))
    return QA_PROMPT_WITH_CONTEXT.format(memories=mem_text, query=query)


def prepare_all_tasks(pool, gt_records):
    """Pre-compute all retrieval results (uses Ollama embeddings, must be sequential)."""
    tiers = ["T0_no_memory", "T1_bm25", "T2_semantic", "T3_hybrid"]
    tasks = []

    print(f"\nPre-computing retrieval for {len(gt_records)} queries × {len(tiers)} tiers...", file=sys.stderr)
    t0 = time.time()

    for qi, gt in enumerate(gt_records):
        query = gt["query"]
        chain_id = gt["chain_id"]
        ground_truth = gt["ground_truth"]

        for tier in tiers:
            if tier == "T0_no_memory":
                memories = []
            elif tier == "T1_bm25":
                memories = pool.retrieve_bm25(query)
            elif tier == "T2_semantic":
                memories = pool.retrieve_semantic(query)
            elif tier == "T3_hybrid":
                memories = pool.retrieve_hybrid(query)

            prompt = build_prompt(query, memories)
            retrieved_ids = [m[0] for m in memories] if memories else []
            hit = chain_id in retrieved_ids

            tasks.append({
                "chain_id": chain_id,
                "tier": tier,
                "prompt": prompt,
                "ground_truth": ground_truth,
                "retrieval_hit": hit,
                "retrieved_ids": retrieved_ids,
            })

        if (qi + 1) % 200 == 0:
            elapsed = time.time() - t0
            rate = (qi + 1) / elapsed
            eta = (len(gt_records) - qi - 1) / rate / 60
            print(f"  [{qi+1}/{len(gt_records)}] {rate:.1f} queries/s — ETA {eta:.1f} min", file=sys.stderr)

    print(f"  Retrieval done in {time.time()-t0:.1f}s", file=sys.stderr)
    return tasks


async def answer_one(client, task, sem, counter, total, lock):
    async with sem:
        for attempt in range(5):
            try:
                response = await client.messages.create(
                    model=HAIKU_MODEL,
                    max_tokens=256,
                    messages=[{"role": "user", "content": task["prompt"]}],
                )
                answer = response.content[0].text.strip()
                break
            except anthropic.RateLimitError:
                await asyncio.sleep(2 ** attempt)
            except Exception as e:
                if attempt == 4:
                    answer = ""
                await asyncio.sleep(1)

        f1 = f1_score(answer, task["ground_truth"])

        result = {
            "chain_id": task["chain_id"],
            "tier": task["tier"],
            "answer": answer,
            "f1": f1,
            "retrieval_hit": task["retrieval_hit"],
            "retrieved_ids": task["retrieved_ids"],
        }

        async with lock:
            counter["done"] += 1
            counter["results"].append(result)
            n = counter["done"]
            if n % 200 == 0 or n == total:
                elapsed = time.time() - counter["t0"]
                rate = n / elapsed
                eta = (total - n) / rate / 60
                print(
                    f"  [{n}/{total}] {rate:.0f} calls/s — ETA {eta:.1f} min",
                    file=sys.stderr,
                )

        return result


async def run_qa(tasks):
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    client = anthropic.AsyncAnthropic()
    sem = asyncio.Semaphore(CONCURRENCY)
    lock = asyncio.Lock()
    counter = {"done": 0, "results": [], "t0": time.time()}

    print(f"\nRunning {len(tasks)} QA calls via Haiku (concurrency={CONCURRENCY})...", file=sys.stderr)

    await asyncio.gather(*[
        answer_one(client, task, sem, counter, len(tasks), lock)
        for task in tasks
    ])

    elapsed = time.time() - counter["t0"]
    print(f"  QA done in {elapsed/60:.1f} min ({len(tasks)/elapsed:.0f} calls/s)", file=sys.stderr)
    return counter["results"]


def main():
    # Load data
    with open(GROUND_TRUTH_PATH) as f:
        gt_records = [json.loads(line) for line in f]
    print(f"Loaded {len(gt_records)} ground truth records", file=sys.stderr)

    with open(ENCODINGS_PATH) as f:
        encodings = [json.loads(line) for line in f]
    encodings = [e for e in encodings if e.get("intent_outcome") and e.get("synthetic_query")]
    print(f"Loaded {len(encodings)} encodings", file=sys.stderr)

    # Build memory pool (embedding is the slow part)
    pool = MemoryPool(encodings)

    # Pre-compute retrieval (sequential, uses Ollama embeddings)
    tasks = prepare_all_tasks(pool, gt_records)

    # Run QA via Haiku (concurrent)
    all_results = asyncio.run(run_qa(tasks))

    # Aggregate
    tiers = ["T0_no_memory", "T1_bm25", "T2_semantic", "T3_hybrid"]
    summary = {}
    for tier in tiers:
        tier_results = [r for r in all_results if r["tier"] == tier]
        f1s = [r["f1"] for r in tier_results]
        hits = [r["retrieval_hit"] for r in tier_results]
        summary[tier] = {
            "mean_f1": round(float(np.mean(f1s)), 4),
            "std_f1": round(float(np.std(f1s)), 4),
            "median_f1": round(float(np.median(f1s)), 4),
            "retrieval_hit_rate": round(float(np.mean(hits)), 4) if tier != "T0_no_memory" else None,
            "n": len(tier_results),
        }

    output = {"summary": summary, "results": all_results}
    with open(RESULTS_PATH, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n{'='*60}", file=sys.stderr)
    print(f"RESULTS SUMMARY (n={len(gt_records)})", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)
    for tier in tiers:
        s = summary[tier]
        hit_str = f"  hit_rate={s['retrieval_hit_rate']:.3f}" if s["retrieval_hit_rate"] is not None else ""
        print(f"  {tier:15s}  mean_F1={s['mean_f1']:.4f}  std={s['std_f1']:.4f}{hit_str}", file=sys.stderr)
    print(f"\nWrote detailed results to {RESULTS_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
