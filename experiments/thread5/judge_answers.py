#!/usr/bin/env python3
"""LLM-as-judge scoring for ceiling effect experiment.

Takes the existing results (answers + ground truth) and asks Haiku
to judge semantic correctness, bypassing F1's lexical bias.
"""

import anthropic
import asyncio
import json
import os
import sys
import time

MODEL = "claude-haiku-4-5-20251001"
CONCURRENCY = 10

SCRIPT_DIR = os.path.dirname(__file__)
RESULTS_PATH = os.path.join(SCRIPT_DIR, "ceiling_results_full.json")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "ceiling_judged_full.json")

JUDGE_PROMPT = """You are judging whether an answer is factually correct given a reference answer.

<reference_answer>
{ground_truth}
</reference_answer>

<candidate_answer>
{answer}
</candidate_answer>

Does the candidate answer convey the same key facts as the reference? Minor wording differences are fine. The candidate must capture the essential information, not just share some words.

Reply with exactly one of:
- CORRECT — captures the key facts
- PARTIAL — gets some facts right but misses important ones
- WRONG — factually incorrect or unrelated

Then one sentence explaining why. Format: VERDICT: explanation"""


async def judge_one(client, item, sem, counter, total, lock):
    async with sem:
        prompt = JUDGE_PROMPT.format(
            ground_truth=item["ground_truth"],
            answer=item["answer"],
        )

        for attempt in range(5):
            try:
                response = await client.messages.create(
                    model=MODEL,
                    max_tokens=100,
                    messages=[{"role": "user", "content": prompt}],
                )
                verdict_text = response.content[0].text.strip()
                break
            except anthropic.RateLimitError:
                await asyncio.sleep(2 ** attempt)
            except Exception:
                if attempt == 4:
                    verdict_text = "ERROR: failed after retries"
                await asyncio.sleep(1)

        if verdict_text.startswith("CORRECT"):
            score = 1.0
        elif verdict_text.startswith("PARTIAL"):
            score = 0.5
        else:
            score = 0.0

        result = {
            "chain_id": item["chain_id"],
            "tier": item["tier"],
            "judge_score": score,
            "judge_verdict": verdict_text,
        }

        async with lock:
            counter["done"] += 1
            counter["results"].append(result)
            n = counter["done"]
            if n % 500 == 0 or n == total:
                elapsed = time.time() - counter["t0"]
                rate = n / elapsed
                eta = (total - n) / rate / 60
                print(f"  [{n}/{total}] {rate:.0f} calls/s — ETA {eta:.1f} min", file=sys.stderr)

        return result


async def run_judging(items):
    client = anthropic.AsyncAnthropic()
    sem = asyncio.Semaphore(CONCURRENCY)
    lock = asyncio.Lock()
    counter = {"done": 0, "results": [], "t0": time.time()}

    print(f"Judging {len(items)} answers via Haiku (concurrency={CONCURRENCY})...", file=sys.stderr)

    await asyncio.gather(*[
        judge_one(client, item, sem, counter, len(items), lock)
        for item in items
    ])

    elapsed = time.time() - counter["t0"]
    print(f"  Done in {elapsed/60:.1f} min ({len(items)/elapsed:.0f} calls/s)", file=sys.stderr)
    return counter["results"]


def main():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    with open(RESULTS_PATH) as f:
        data = json.load(f)

    # Load ground truth for lookup
    gt_path = os.path.join(SCRIPT_DIR, "ground_truth_full.jsonl")
    with open(gt_path) as f:
        gt_map = {json.loads(line)["chain_id"]: json.loads(line)["ground_truth"] for line in f}

    items = []
    for r in data["results"]:
        items.append({
            "chain_id": r["chain_id"],
            "tier": r["tier"],
            "answer": r["answer"],
            "ground_truth": gt_map.get(r["chain_id"], ""),
        })

    print(f"Loaded {len(items)} answer-reference pairs", file=sys.stderr)

    judged = asyncio.run(run_judging(items))

    # Aggregate by tier
    import numpy as np
    tiers = ["T0_no_memory", "T1_bm25", "T2_semantic", "T3_hybrid"]
    summary = {}
    for tier in tiers:
        scores = [r["judge_score"] for r in judged if r["tier"] == tier]
        correct = sum(1 for s in scores if s == 1.0)
        partial = sum(1 for s in scores if s == 0.5)
        wrong = sum(1 for s in scores if s == 0.0)
        summary[tier] = {
            "mean_score": round(float(np.mean(scores)), 4),
            "correct_pct": round(correct / len(scores) * 100, 1),
            "partial_pct": round(partial / len(scores) * 100, 1),
            "wrong_pct": round(wrong / len(scores) * 100, 1),
            "n": len(scores),
        }

    output = {"summary": summary, "results": judged}
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n{'='*60}", file=sys.stderr)
    print(f"JUDGE RESULTS (n={len(items)//len(tiers)} queries)", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)
    for tier in tiers:
        s = summary[tier]
        print(
            f"  {tier:15s}  score={s['mean_score']:.4f}  "
            f"correct={s['correct_pct']:.1f}%  partial={s['partial_pct']:.1f}%  wrong={s['wrong_pct']:.1f}%",
            file=sys.stderr,
        )
    print(f"\nWrote to {OUTPUT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
