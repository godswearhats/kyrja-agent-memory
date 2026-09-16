#!/usr/bin/env python3
"""Generate a memory encoding from the Task 2 transcript using Opus 4.6.

Exp 2 — C-Replication on Task 3.
Differences from parent generate_encoding.py:
  - Source = Task 2 (where_keep_attrs_scalar) transcript.
  - Distiller model = claude-opus-4-6 explicitly (not the `opus` alias).
  - Variants restricted to A and C.

Usage:
    generate_encoding.py {A,C,all}
"""

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

EXP_DIR = Path(__file__).parent.parent
PARENT_EXP_DIR = EXP_DIR.parent
PROMPTS_DIR = PARENT_EXP_DIR / "prompts"
SOURCES_DIR = EXP_DIR / "sources"
ENCODINGS_DIR = EXP_DIR / "encodings"
CLAUDE_BIN = "/opt/claude"

DISTILLER_MODEL = "claude-opus-4-6"

VARIANTS = {
    "A": {"prompt": "A_briefing_1200.md", "source": "task2_full.md"},
    "C": {"prompt": "C_structured_1200.md", "source": "task2_full.md"},
}


def generate(variant_letter):
    if variant_letter not in VARIANTS:
        print(f"Unknown variant: {variant_letter}")
        sys.exit(1)

    cfg = VARIANTS[variant_letter]
    prompt_template = (PROMPTS_DIR / cfg["prompt"]).read_text()
    source = (SOURCES_DIR / cfg["source"]).read_text()
    full_prompt = prompt_template.replace("{transcript}", source)

    print(f"Variant {variant_letter}: prompt={cfg['prompt']}, source={cfg['source']}")
    print(f"  distiller model: {DISTILLER_MODEL}")
    print(f"  prompt length: {len(full_prompt)} chars")
    print(f"  invoking Claude...")

    start = time.time()
    result = subprocess.run(
        [
            CLAUDE_BIN,
            "--setting-sources", "",
            "--model", DISTILLER_MODEL,
            "-p", full_prompt,
            "--output-format", "json",
            "--no-session-persistence",
            "--disable-slash-commands",
            "--dangerously-skip-permissions",
            "--allow-dangerously-skip-permissions",
        ],
        capture_output=True,
        text=True,
        timeout=300,
    )
    elapsed = time.time() - start

    if result.returncode != 0:
        print(f"  ERROR: returncode={result.returncode}")
        print(f"  stderr: {result.stderr[:500]}")
        sys.exit(1)

    try:
        parsed = json.loads(result.stdout)
    except json.JSONDecodeError:
        print(f"  ERROR: could not parse JSON output")
        print(f"  stdout (first 500): {result.stdout[:500]}")
        sys.exit(1)

    encoding_text = parsed.get("result", "").strip()
    if not encoding_text:
        print(f"  ERROR: empty result")
        print(f"  full parsed: {json.dumps(parsed, indent=2)[:1000]}")
        sys.exit(1)

    out_path = ENCODINGS_DIR / f"{variant_letter}_encoding.md"
    out_path.write_text(encoding_text)

    meta_path = ENCODINGS_DIR / f"{variant_letter}_meta.json"
    meta = {
        "variant": variant_letter,
        "prompt_file": cfg["prompt"],
        "source_file": cfg["source"],
        "elapsed_sec": elapsed,
        "model": DISTILLER_MODEL,
        "usage": parsed.get("usage", {}),
        "total_cost_usd": parsed.get("total_cost_usd", 0),
        "duration_ms": parsed.get("duration_ms", 0),
        "num_turns": parsed.get("num_turns", 0),
        "output_chars": len(encoding_text),
        "output_words": len(encoding_text.split()),
    }
    meta_path.write_text(json.dumps(meta, indent=2))

    print(f"  done in {elapsed:.1f}s")
    print(f"  output: {len(encoding_text)} chars, {len(encoding_text.split())} words")
    print(f"  cost: ${parsed.get('total_cost_usd', 0):.4f}")
    print(f"  saved: {out_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("variant", choices=sorted(VARIANTS.keys()) + ["all"])
    args = parser.parse_args()

    if args.variant == "all":
        for v in sorted(VARIANTS.keys()):
            generate(v)
            print()
    else:
        generate(args.variant)


if __name__ == "__main__":
    main()
