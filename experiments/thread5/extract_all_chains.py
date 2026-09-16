#!/usr/bin/env python3
"""Extract ALL tool-call chains from sessions (no sampling).

Adapted from thread1/extract_chains.py — removes the sample limit
so we get the full corpus for the ceiling effect experiment.
"""

import json
import os
import sys

INDEX_PATH = "/mnt/team-data/processed/sessions_deduped.jsonl"
RAW_BASE = "/mnt/team-data/raw/conversations"
MIN_CHAIN_TOOLS = 4
MAX_CHAIN_INPUT_TOKENS = 15_000
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "all_chains.jsonl")


def load_sessions():
    with open(INDEX_PATH) as f:
        return [json.loads(line) for line in f]


def find_session_file(session):
    path = os.path.join(RAW_BASE, session["rel_path"])
    if os.path.exists(path):
        return path
    parts = session["rel_path"].split("/")
    alt = os.path.join(RAW_BASE, parts[0], "/".join(parts[1:]))
    if os.path.exists(alt):
        return alt
    return None


def parse_entries(path):
    entries = []
    with open(path) as f:
        for line in f:
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return entries


def extract_chains_from_session(session):
    path = find_session_file(session)
    if not path:
        return []

    entries = parse_entries(path)
    chains = []
    current_steps = []

    def flush_chain():
        nonlocal current_steps
        tool_count = sum(
            1
            for step in current_steps
            if step["role"] == "assistant"
            for b in step["content"]
            if b.get("type") == "tool_use"
        )
        if tool_count >= MIN_CHAIN_TOOLS:
            total_chars = sum(len(json.dumps(s["content"])) for s in current_steps)
            approx_tokens = total_chars // 4
            if approx_tokens <= MAX_CHAIN_INPUT_TOKENS:
                chains.append(
                    {
                        "session_id": session["session_id"],
                        "agent": session.get("canonical_agent", session.get("agent")),
                        "session_task": session.get("first_user_msg", ""),
                        "tool_count": tool_count,
                        "approx_tokens": approx_tokens,
                        "steps": current_steps,
                    }
                )
        current_steps = []

    for entry in entries:
        msg = entry.get("message", {})
        role = msg.get("role", "")
        content = msg.get("content", [])

        if not isinstance(content, list):
            if role == "user" and isinstance(content, str):
                flush_chain()
            continue

        if role == "assistant":
            has_tool_use = any(b.get("type") == "tool_use" for b in content)
            if has_tool_use:
                step_content = []
                for b in content:
                    if b.get("type") == "tool_use":
                        step_content.append(
                            {
                                "type": "tool_use",
                                "name": b["name"],
                                "input": b.get("input", {}),
                            }
                        )
                    elif b.get("type") == "text":
                        step_content.append({"type": "text", "text": b["text"]})
                current_steps.append({"role": "assistant", "content": step_content})
            else:
                flush_chain()

        elif role == "user":
            is_tool_result = any(
                isinstance(b, dict) and b.get("type") == "tool_result"
                for b in content
            )
            if is_tool_result:
                step_content = []
                for b in content:
                    if isinstance(b, dict) and b.get("type") == "tool_result":
                        result_text = b.get("content", "")
                        if isinstance(result_text, list):
                            result_text = "\n".join(
                                rb.get("text", "") for rb in result_text if isinstance(rb, dict)
                            )
                        if len(str(result_text)) > 8000:
                            result_text = str(result_text)[:8000] + "\n[...truncated]"
                        step_content.append(
                            {
                                "type": "tool_result",
                                "tool_use_id": b.get("tool_use_id", ""),
                                "content": str(result_text),
                            }
                        )
                current_steps.append({"role": "user", "content": step_content})
            else:
                flush_chain()

    flush_chain()
    return chains


def main():
    sessions = load_sessions()
    print(f"Loaded {len(sessions)} sessions", file=sys.stderr)

    all_chains = []
    for i, session in enumerate(sessions):
        chains = extract_chains_from_session(session)
        all_chains.extend(chains)
        if (i + 1) % 100 == 0:
            print(
                f"  [{i+1}/{len(sessions)}] {len(all_chains)} chains extracted",
                file=sys.stderr,
            )

    print(f"\nTotal chains (4+ tools, ≤{MAX_CHAIN_INPUT_TOKENS} tokens): {len(all_chains)}", file=sys.stderr)

    # Stats
    tool_counts = [c["tool_count"] for c in all_chains]
    token_counts = [c["approx_tokens"] for c in all_chains]
    print(f"Tool count range: {min(tool_counts)}-{max(tool_counts)}, "
          f"mean {sum(tool_counts)/len(tool_counts):.1f}", file=sys.stderr)
    print(f"Token range: {min(token_counts)}-{max(token_counts)}, "
          f"mean {sum(token_counts)/len(token_counts):.0f}", file=sys.stderr)
    print(f"Total input tokens (approx): {sum(token_counts):,}", file=sys.stderr)

    with open(OUTPUT_PATH, "w") as f:
        for i, chain in enumerate(all_chains):
            chain["chain_id"] = f"chain_{i:04d}"
            f.write(json.dumps(chain) + "\n")
    print(f"Wrote {len(all_chains)} chains to {OUTPUT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
