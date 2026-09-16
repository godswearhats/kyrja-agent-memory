#!/usr/bin/env python3
"""Generate ground truth answers for ceiling effect experiment.

For each chain+query pair, gives gemma3:12b the FULL original chain
and asks it to answer the query. This is the "open book exam" --
the model has complete context, no retrieval needed.
"""

import json
import os
import sys
import time
import urllib.request

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://192.168.109.1:11434")
MODEL = "gemma3:12b"

SCRIPT_DIR = os.path.dirname(__file__)
DEFAULT_CHAINS = os.path.join(SCRIPT_DIR, "all_chains.jsonl")
DEFAULT_ENCODINGS = os.path.join(SCRIPT_DIR, "all_encodings.jsonl")
DEFAULT_OUTPUT = os.path.join(SCRIPT_DIR, "ground_truth_full.jsonl")

# Fall back to pilot data if full data doesn't exist
CHAINS_PATH = DEFAULT_CHAINS if os.path.exists(DEFAULT_CHAINS) else os.path.join(SCRIPT_DIR, "..", "thread1", "pilot_chains.jsonl")
ENCODINGS_PATH = DEFAULT_ENCODINGS if os.path.exists(DEFAULT_ENCODINGS) else os.path.join(SCRIPT_DIR, "..", "thread1", "pilot_encodings.jsonl")
OUTPUT_PATH = DEFAULT_OUTPUT if os.path.exists(DEFAULT_CHAINS) else os.path.join(SCRIPT_DIR, "ground_truth.jsonl")

PROMPT_TEMPLATE = """You are answering a question based on the record of work below.
Give a direct, factual answer in 1-3 sentences. Do not explain your reasoning.

<work_record>
{chain_text}
</work_record>

Question: {query}

Answer:"""


def format_chain(chain):
    lines = [f"Session task: {chain.get('session_task', 'unknown')}"]
    for step in chain.get("steps", []):
        if step["role"] == "assistant":
            for block in step["content"]:
                if block["type"] == "tool_use":
                    lines.append(f"Tool: {block['name']} — Input: {json.dumps(block['input'])[:500]}")
                elif block["type"] == "text" and block["text"].strip():
                    lines.append(f"Reasoning: {block['text'][:300]}")
        elif step["role"] == "user":
            for block in step["content"]:
                if block["type"] == "tool_result":
                    lines.append(f"Result: {block['content'][:500]}")
    return "\n".join(lines)


def call_ollama(prompt, model=MODEL):
    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.1, "num_predict": 256},
    }).encode()
    req = urllib.request.Request(
        f"{OLLAMA_HOST}/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read())


def main():
    with open(CHAINS_PATH) as f:
        chains = {json.loads(line)["chain_id"]: json.loads(line) for line in f}

    with open(ENCODINGS_PATH) as f:
        encodings = [json.loads(line) for line in f]

    done_ids = set()
    if os.path.exists(OUTPUT_PATH):
        with open(OUTPUT_PATH) as f:
            for line in f:
                done_ids.add(json.loads(line)["chain_id"])
        print(f"Resuming: {len(done_ids)} already done", file=sys.stderr)

    remaining = [e for e in encodings if e["chain_id"] not in done_ids and e.get("synthetic_query")]
    print(f"Generating ground truth for {len(remaining)} queries ({len(done_ids)} done)", file=sys.stderr)

    with open(OUTPUT_PATH, "a") as out:
        for i, enc in enumerate(remaining):
            chain = chains.get(enc["chain_id"])
            if not chain:
                print(f"  [{i+1}/{len(remaining)}] {enc['chain_id']} — chain not found, skipping", file=sys.stderr)
                continue

            chain_text = format_chain(chain)
            prompt = PROMPT_TEMPLATE.format(chain_text=chain_text, query=enc["synthetic_query"])

            t0 = time.time()
            result = call_ollama(prompt)
            elapsed = time.time() - t0

            record = {
                "chain_id": enc["chain_id"],
                "query": enc["synthetic_query"],
                "ground_truth": result["response"].strip(),
                "eval_duration_ms": result.get("eval_duration", 0) // 1_000_000,
                "total_duration_ms": result.get("total_duration", 0) // 1_000_000,
            }
            out.write(json.dumps(record) + "\n")
            out.flush()

            preview = record["ground_truth"][:80].replace("\n", " ")
            print(
                f"  [{i+1}/{len(remaining)}] {enc['chain_id']} — {elapsed:.1f}s — {preview}...",
                file=sys.stderr,
            )

    print(f"\nDone. Wrote to {OUTPUT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
