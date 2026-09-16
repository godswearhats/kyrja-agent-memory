#!/usr/bin/env python3
"""Encode all chains with intent+outcome strategy via Haiku API.

Runs concurrent requests for speed. Requires ANTHROPIC_API_KEY.
Supports resume — safe to re-run if interrupted.
"""

import anthropic
import asyncio
import json
import os
import sys
import time

MODEL = "claude-haiku-4-5-20251001"
CHAINS_PATH = os.path.join(os.path.dirname(__file__), "all_chains.jsonl")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "all_encodings.jsonl")
MAX_RETRIES = 5
RETRY_DELAY = 2
CONCURRENCY = 10

ENCODING_PROMPT = """You are encoding an agent's tool-call chain for a memory system. Produce a summary that captures:
1. INTENT — What was the agent trying to accomplish? What triggered this chain?
2. OUTCOME — What actually happened? Did it succeed, fail, or partially succeed?
3. KEY DECISIONS — Any non-obvious choices the agent made (e.g., picked approach A over B).

Format: Three labeled sections (Intent, Outcome, Key Decisions), each 1-3 sentences.

<chain>
{chain_text}
</chain>

Write the intent+outcome encoding:"""

QUERY_PROMPT = """You are generating a realistic retrieval query for a memory system. Given this record of what an agent did, write a question that a user or agent might ask in a FUTURE session where this memory would be the most relevant result.

The query should be natural — the kind of thing someone would actually type when they're trying to remember or find out something. It should NOT quote specifics from the chain verbatim, but should be about the same topic/task/problem.

Write exactly ONE query, nothing else.

<chain>
{chain_text}
</chain>

Query:"""


def format_chain_for_prompt(chain):
    lines = []
    lines.append(f"Session task: {chain['session_task']}")
    lines.append(f"Agent: {chain['agent']}")
    lines.append("")

    step_num = 0
    for step in chain["steps"]:
        if step["role"] == "assistant":
            for block in step["content"]:
                if block["type"] == "tool_use":
                    step_num += 1
                    lines.append(f"[Step {step_num}] Tool: {block['name']}")
                    input_str = json.dumps(block["input"], indent=2)
                    if len(input_str) > 2000:
                        input_str = input_str[:2000] + "\n  [...]"
                    lines.append(f"  Input: {input_str}")
                elif block["type"] == "text":
                    text = block["text"]
                    if len(text) > 500:
                        text = text[:500] + " [...]"
                    lines.append(f"  Agent reasoning: {text}")
        elif step["role"] == "user":
            for block in step["content"]:
                if block["type"] == "tool_result":
                    result = block["content"]
                    if len(result) > 2000:
                        result = result[:2000] + "\n  [...]"
                    lines.append(f"  Result: {result}")
                    lines.append("")

    return "\n".join(lines)


async def call_haiku(client, prompt, max_tokens=1024):
    for attempt in range(MAX_RETRIES):
        try:
            response = await client.messages.create(
                model=MODEL,
                max_tokens=max_tokens,
                messages=[{"role": "user", "content": prompt}],
            )
            return response
        except anthropic.RateLimitError:
            wait = RETRY_DELAY * (2 ** attempt)
            await asyncio.sleep(wait)
        except Exception as e:
            if attempt == MAX_RETRIES - 1:
                raise
            await asyncio.sleep(RETRY_DELAY)
    return None


async def encode_one(client, chain, sem, counter, total, out_file, lock):
    async with sem:
        chain_text = format_chain_for_prompt(chain)

        enc_resp = await call_haiku(client, ENCODING_PROMPT.format(chain_text=chain_text))
        if not enc_resp:
            return None

        q_resp = await call_haiku(client, QUERY_PROMPT.format(chain_text=chain_text), max_tokens=256)
        if not q_resp:
            return None

        record = {
            "chain_id": chain["chain_id"],
            "intent_outcome": enc_resp.content[0].text,
            "synthetic_query": q_resp.content[0].text.strip(),
        }

        in_tok = enc_resp.usage.input_tokens + q_resp.usage.input_tokens
        out_tok = enc_resp.usage.output_tokens + q_resp.usage.output_tokens

        async with lock:
            out_file.write(json.dumps(record) + "\n")
            out_file.flush()
            counter["done"] += 1
            counter["in_tok"] += in_tok
            counter["out_tok"] += out_tok
            n = counter["done"]
            if n % 50 == 0 or n == 1 or n == total:
                elapsed = time.time() - counter["t0"]
                rate = n / elapsed * 60
                eta = (total - n) / (n / elapsed) / 60
                print(
                    f"  [{n}/{total}] {rate:.0f} chains/min — "
                    f"{counter['in_tok']:,} in / {counter['out_tok']:,} out — "
                    f"ETA {eta:.0f} min",
                    file=sys.stderr,
                )

        return record


async def main():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    client = anthropic.AsyncAnthropic()

    with open(CHAINS_PATH) as f:
        chains = [json.loads(line) for line in f]
    print(f"Loaded {len(chains)} chains", file=sys.stderr)

    done_ids = set()
    if os.path.exists(OUTPUT_PATH):
        with open(OUTPUT_PATH) as f:
            for line in f:
                try:
                    done_ids.add(json.loads(line)["chain_id"])
                except (json.JSONDecodeError, KeyError):
                    pass
        print(f"Resuming: {len(done_ids)} already encoded", file=sys.stderr)

    remaining = [c for c in chains if c["chain_id"] not in done_ids]
    print(f"Encoding {len(remaining)} chains with concurrency={CONCURRENCY}...\n", file=sys.stderr)

    sem = asyncio.Semaphore(CONCURRENCY)
    lock = asyncio.Lock()
    counter = {"done": 0, "in_tok": 0, "out_tok": 0, "t0": time.time()}

    with open(OUTPUT_PATH, "a") as out:
        tasks = [
            encode_one(client, chain, sem, counter, len(remaining), out, lock)
            for chain in remaining
        ]
        await asyncio.gather(*tasks)

    elapsed = time.time() - counter["t0"]
    print(
        f"\nDone in {elapsed/60:.1f} min. "
        f"Total tokens: {counter['in_tok']:,} in / {counter['out_tok']:,} out",
        file=sys.stderr,
    )
    print(f"Wrote to {OUTPUT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    asyncio.run(main())
