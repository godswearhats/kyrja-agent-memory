#!/usr/bin/env python3
"""Sweep generator v2 — produce N scenarios × M sizes for MASQ pilot/headline.

For each (domain, seed, size): embedding.py v2 → compose.py → verify.py.
Stops on any verify failure.

Output layout:
    sweep/<domain>/s<seed>/<size>/
        family-<domain>.json   corpus.md

Usage:
    python3 sweep.py --scenarios 4 --sizes 6k,25k,60k,150k,400k
    python3 sweep.py --scenarios 4 --sizes 6k,60k   # quick subset
    python3 sweep.py --seeds 2001,2002 --domains rate-limit  # explicit
"""
import argparse, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ATOM_BANK = os.path.join(HERE, "atoms", "atom-bank.json")

SIZES = {
    "6k":   dict(n_siblings=8,   n_chatter=40,   n_collisions=2,
                 n_scopes=2, n_near_misses=1, days=28),
    "25k":  dict(n_siblings=30,  n_chatter=200,  n_collisions=4,
                 n_scopes=3, n_near_misses=2, days=90),
    "60k":  dict(n_siblings=60,  n_chatter=520,  n_collisions=6,
                 n_scopes=4, n_near_misses=3, days=180),
    "150k": dict(n_siblings=100, n_chatter=1400, n_collisions=10,
                 n_scopes=4, n_near_misses=3, days=365),
    "400k": dict(n_siblings=150, n_chatter=3800, n_collisions=16,
                 n_scopes=5, n_near_misses=4, days=730),
}

DOMAINS = ["rate-limit", "ownership", "merge-policy"]


def run(cmd, label):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  FAIL  {label}", file=sys.stderr)
        print(r.stdout, file=sys.stderr)
        print(r.stderr, file=sys.stderr)
        sys.exit(1)
    return r.stdout


def generate_one(domain, seed, size_key, out_root):
    cfg = SIZES[size_key]
    raw_dir = os.path.join(out_root, domain, f"s{seed}", f"{size_key}-raw")
    final_dir = os.path.join(out_root, domain, f"s{seed}", size_key)

    if os.path.isdir(final_dir):
        fams = [f for f in os.listdir(final_dir)
                if f.startswith("family-") and f.endswith(".json")]
        if fams:
            print(f"  SKIP  {domain}/s{seed}/{size_key} (already exists)")
            return True

    run([sys.executable, os.path.join(HERE, "embedding.py"),
         "--domain", domain,
         "--n-siblings", str(cfg["n_siblings"]),
         "--n-chatter", str(cfg["n_chatter"]),
         "--n-collisions", str(cfg["n_collisions"]),
         "--n-scopes", str(cfg["n_scopes"]),
         "--n-near-misses", str(cfg["n_near_misses"]),
         "--days", str(cfg["days"]),
         "--seed", str(seed),
         "--out", raw_dir],
        f"embedding {domain}/s{seed}/{size_key}")

    run([sys.executable, os.path.join(HERE, "compose.py"),
         raw_dir,
         "--atom-bank", ATOM_BANK,
         "--out", final_dir],
        f"compose {domain}/s{seed}/{size_key}")

    fam_file = [f for f in os.listdir(final_dir)
                if f.startswith("family-") and f.endswith(".json")][0]
    result = run([sys.executable, os.path.join(HERE, "verify.py"),
                  os.path.join(final_dir, fam_file)],
                 f"verify {domain}/s{seed}/{size_key}")

    if "FAILURES" in result:
        print(f"  FAIL  verify failed for {domain}/s{seed}/{size_key}")
        print(result)
        return False

    corpus_path = os.path.join(final_dir, "corpus.md")
    with open(corpus_path) as f:
        words = len(f.read().split())
    tokens = int(words * 1.33)
    print(f"  OK    {domain}/s{seed}/{size_key} — {tokens:,} tokens")

    import shutil
    shutil.rmtree(raw_dir, ignore_errors=True)
    parent = os.path.dirname(raw_dir)
    try:
        os.rmdir(parent)
    except OSError:
        pass

    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scenarios", type=int, default=4,
                    help="scenarios per domain (ignored if --seeds given)")
    ap.add_argument("--seeds", default=None,
                    help="explicit comma-separated seeds")
    ap.add_argument("--domains", default=",".join(DOMAINS),
                    help="comma-separated domain list")
    ap.add_argument("--sizes", default=",".join(SIZES),
                    help="comma-separated size keys")
    ap.add_argument("--out", default=os.path.join(HERE, "sweep"))
    ap.add_argument("--base-seed", type=int, default=2001,
                    help="starting seed (when using --scenarios)")
    a = ap.parse_args()

    domains = [d.strip() for d in a.domains.split(",")]
    size_keys = [s.strip() for s in a.sizes.split(",")]
    for s in size_keys:
        if s not in SIZES:
            print(f"unknown size: {s} (choose from {sorted(SIZES)})",
                  file=sys.stderr)
            sys.exit(1)

    if a.seeds:
        seeds = [int(s.strip()) for s in a.seeds.split(",")]
    else:
        seeds = list(range(a.base_seed, a.base_seed + a.scenarios))

    total = len(domains) * len(seeds) * len(size_keys)
    print(f"Sweep: {len(domains)} domains × {len(seeds)} seeds × "
          f"{len(size_keys)} sizes = {total} worlds")
    print(f"  domains: {domains}")
    print(f"  seeds:   {seeds}")
    print(f"  sizes:   {size_keys}")
    print(f"  output:  {a.out}")
    print()

    done, failed = 0, 0
    for domain in domains:
        for seed in seeds:
            for size_key in size_keys:
                ok = generate_one(domain, seed, size_key, a.out)
                if ok:
                    done += 1
                else:
                    failed += 1
                    print(f"\nABORTED at {domain}/s{seed}/{size_key}")
                    sys.exit(1)

    print(f"\nSweep complete: {done}/{total} worlds generated, {failed} failed")


if __name__ == "__main__":
    main()
