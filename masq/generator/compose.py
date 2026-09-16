#!/usr/bin/env python3
"""Atom-bank composition engine — v2 (multi-scope chains).

Reads a family JSON (from embedding.py v2) + atom-bank.json, populates `prose`
on all sessions via seeded multi-layer composition, and re-renders the corpus.

v2 changes:
 - Chain-write sessions (kind starts with "chain_") get ≥1 scope-context atom
   injected into the composed prose around the locked sentence.
 - Scope-context atoms are read from family meta (per scope).
 - Near-miss sessions and sibling sessions compose as before.
 - Single corpus output (no C1-C4 cell variants).

Layers:
  L0  atoms (from atom-bank.json, per writer) + scope-context atoms (per scope)
  L1  compound sentence = atom + connective + atom
  L2  paragraph = 2-3 compound sentences
  L3  session body = 1-2 paragraphs + optional locked sentence

Usage:
    python3 compose.py <family_dir> --atom-bank <path> [--seed 42] [--out <dir>]
"""
import argparse, json, os, random, sys

from domains import DOMAINS
from embedding import render_md


def load_bank(path):
    with open(path) as f:
        bank = json.load(f)
    return bank["atoms"], bank["connectives"]


def lower_start(s):
    if not s:
        return s
    if s[0] == "I" and len(s) > 1 and not s[1].isalpha():
        return s
    return s[0].lower() + s[1:]


def _draw_atoms(writer_atoms, n, rng):
    """Sample n atoms without replacement (no repeats within a session)."""
    if n <= len(writer_atoms):
        return rng.sample(writer_atoms, n)
    return [rng.choice(writer_atoms) for _ in range(n)]


def compose_body(writer_atoms, connectives, rng, locked=None, scope_atoms=None):
    """Compose a session body from atoms + optional locked sentence.

    If scope_atoms is provided (for chain-write sessions), at least one
    scope-context atom is injected into the pre-locked compounds, ensuring
    the scope name appears in the same session as the config write.
    """
    if locked is None:
        n_compounds = rng.choices([2, 3], weights=[60, 40])[0]
        atoms = _draw_atoms(writer_atoms, n_compounds * 2, rng)
        parts = []
        for i in range(n_compounds):
            a1, a2 = atoms[i * 2], atoms[i * 2 + 1]
            conn = rng.choice(connectives)
            parts.append(f"{a1} {conn} {lower_start(a2)}")
        return " ".join(parts)

    n_pre = rng.choices([1, 2], weights=[65, 35])[0]
    n_post = rng.choices([0, 1], weights=[30, 70])[0]
    n_compounds = n_pre + n_post

    atoms_needed = n_compounds * 2
    if scope_atoms:
        # Replace one atom with a scope-context atom (always in pre-locked)
        scope_atom = rng.choice(scope_atoms)
        regular = _draw_atoms(writer_atoms, atoms_needed - 1, rng)
        atoms = regular[:1] + [scope_atom] + regular[1:]
    else:
        atoms = _draw_atoms(writer_atoms, atoms_needed, rng)

    idx = 0
    parts = []
    for _ in range(n_pre):
        a1, a2 = atoms[idx], atoms[idx + 1]
        conn = rng.choice(connectives)
        parts.append(f"{a1} {conn} {lower_start(a2)}")
        idx += 2
    parts.append(locked)
    for _ in range(n_post):
        a1, a2 = atoms[idx], atoms[idx + 1]
        conn = rng.choice(connectives)
        parts.append(f"{a1} {conn} {lower_start(a2)}")
        idx += 2
    return "\n\n".join(parts)


def _scope_atoms_map(fam):
    """Build scope_name → context_atoms from family meta."""
    return {s["name"]: s["context_atoms"]
            for s in fam["meta"].get("scopes", [])}


def compose_family(fam, atoms, connectives, seed):
    rng = random.Random(seed)
    scope_map = _scope_atoms_map(fam)

    for s in fam["world_sessions"]:
        w_atoms = atoms.get(s["writer"], [])
        if not w_atoms:
            w_atoms = atoms.get(list(atoms.keys())[0], [])

        scope_ctx = None
        if s["kind"].startswith("chain_") and s.get("scope"):
            scope_ctx = scope_map.get(s["scope"])

        if s["kind"] in ("chatter_generic", "chatter_cover", "chatter_scope"):
            s["prose"] = compose_body(w_atoms, connectives, rng, locked=None)
        else:
            s["prose"] = compose_body(w_atoms, connectives, rng,
                                      locked=s["text"],
                                      scope_atoms=scope_ctx)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("family_dir")
    ap.add_argument("--atom-bank",
                    default=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                         "atoms", "atom-bank.json"))
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))
    fam_dir = (a.family_dir if os.path.isabs(a.family_dir)
               else os.path.join(here, a.family_dir))
    fam_file = [f for f in os.listdir(fam_dir)
                if f.startswith("family-") and f.endswith(".json")][0]
    fam = json.load(open(os.path.join(fam_dir, fam_file)))
    dom = DOMAINS[fam["meta"].get("domain", "rate-limit")]
    atoms, connectives = load_bank(a.atom_bank)

    seed = a.seed if a.seed is not None else fam["meta"]["seed"] + 7919
    compose_family(fam, atoms, connectives, seed)

    out_name = a.out or fam_dir.rstrip("/") + "-composed"
    out = out_name if os.path.isabs(out_name) else os.path.join(here, out_name)
    os.makedirs(out, exist_ok=True)

    with open(os.path.join(out, fam_file), "w") as f:
        json.dump(fam, f, indent=2, default=str)

    m = fam["meta"]
    tag = (f"seed={m['seed']} scopes={m.get('n_scopes', '?')} "
           f"sib={m['n_siblings']} chat={m['n_chatter']} +composed")

    # v2: single corpus (no cells)
    if "cells" in fam:
        # v1 compat: render per-cell corpora
        for cid, c in fam["cells"].items():
            md = render_md(dom, fam["world_sessions"], tag)
            with open(os.path.join(out, f"corpus-{cid}.md"), "w") as f:
                f.write(md)
            words = len(md.split())
    else:
        md = render_md(dom, fam["world_sessions"], tag)
        with open(os.path.join(out, "corpus.md"), "w") as f:
            f.write(md)
        words = len(md.split())

    print(f"composed {len(fam['world_sessions'])} sessions; "
          f"corpus ≈{words} words (≈{int(words * 1.33)} tokens)")
    print(f"wrote {out}/")


if __name__ == "__main__":
    main()
