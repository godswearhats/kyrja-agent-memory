#!/usr/bin/env python3
"""wiki-lint: enforce SCHEMA.md lint rules over the Kyrja wiki.

Usage:
    lint.py [--wiki <dir>] [--rule <name>] [--format markdown|json]
            [--include-inventory]

Implements the deterministic rules from SCHEMA.md §"Lint rules (definitions)".
The contradiction rule (rule 4) is replaced by a tagged-claim inventory the
calling agent reviews for collisions. Does NOT auto-fix.

v0.4 (2026-05-13): retired rule_unsourced_claim and rule_untagged_claim
(regex couldn't reliably detect the five legitimate evidence-anchoring shapes
without high false-positive rates). Replaced with two structural rules:
rule_tagged_page_needs_sources and rule_source_page_has_citation. See
concept/evidence-anchoring.md for the framework.

v0.5.3 (2026-05-17): retired rule_stale_source (rule 1) — fired after the
author had already decided whether to propagate, so it could only flag
decisions that had been made, never surface ones that had been missed.
Discipline replaced by author-side propagation at edit time (see
SCHEMA.md § Lint rules). Rule 8 (missing-construct-validity) now exempts
source/* pages: paper-internal measurements have the experimental paradigm
AS their construct.
"""
import argparse
import json
import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field, asdict
from datetime import date
from pathlib import Path
from typing import Any

DEFAULT_WIKI = Path("wiki")

LINK_RE = re.compile(r'\[([^\]]*)\]\(([^)\s]+)(?:\s+"([^"]*)")?\)')
TAG_RE = re.compile(r'`\[(MEASURED|ASSERTED|SPECULATED|CONTESTED)\]`')
FRONTMATTER_RE = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "#")

# Root-level files exempt from page-type classification per v0.3.
ROOT_EXEMPT = {"BIG-PICTURE.md", "index.md", "log.md", "NEXT.md", "SCHEMA.md"}

# Files exempt from the dangling-link rule. SCHEMA.md contains illustrative
# example links that aren't real targets; log.md is append-only and may
# reference historical paths that no longer exist. Documented in
# wiki/log.md (2026-05-12 Schema v0.3.1 entry).
DANGLING_LINK_EXEMPT = {"SCHEMA.md", "log.md"}

EPISTEMIC_TAGS_INLINE = {"MEASURED", "ASSERTED", "SPECULATED", "CONTESTED"}


@dataclass
class Finding:
    rule: str
    file: str
    line: int | None
    message: str
    severity: str = "warn"  # warn | error | info


@dataclass
class Page:
    path: Path
    rel: str
    frontmatter: dict[str, Any] = field(default_factory=dict)
    body: str = ""
    body_start_line: int = 1
    is_root_exempt: bool = False


# ----- Parsing -----

def parse_frontmatter(text: str) -> tuple[dict[str, Any], str, int]:
    """Return (frontmatter_dict, body, body_start_lineno)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text, 1
    fm_text = m.group(1)
    body = text[m.end():]
    body_start = text[:m.end()].count("\n") + 1

    fm: dict[str, Any] = {}
    current_key: str | None = None
    for line in fm_text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")) and current_key:
            # Continuation line under the current key. Block-list YAML items
            # ("  - value") accumulate into the current key as a list — both
            # the inline form (`sources: [a, b]`) and the block form
            # (`sources:\n  - a\n  - b`) are valid YAML and Obsidian renders
            # both, so the linter must read both (drift fix 2026-06-07).
            # Other multiline content (folded/literal scalars) is preserved-raw
            # (ignored), as before.
            stripped = line.strip()
            if stripped.startswith("-"):
                item = stripped[1:].strip().strip('"').strip("'")
                if item:
                    existing = fm.get(current_key)
                    if isinstance(existing, list):
                        existing.append(item)
                    else:
                        # key was opened with an empty scalar; promote to list
                        fm[current_key] = [item]
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                fm[key] = [v.strip().strip('"').strip("'") for v in inner.split(",") if v.strip()] if inner else []
            elif val.startswith('"') and val.endswith('"'):
                fm[key] = val[1:-1]
            elif val:
                fm[key] = val
            else:
                fm[key] = ""
            current_key = key
    return fm, body, body_start


def load_pages(wiki: Path) -> list[Page]:
    pages = []
    for md in sorted(wiki.rglob("*.md")):
        rel = str(md.relative_to(wiki))
        # The lint/ directory contains lint reports which quote epistemic
        # tags and link patterns as data, not as live claims. Skip entirely.
        if rel.startswith("lint/") or rel.startswith("lint" + os.sep):
            continue
        # The archive/ directory contains retired root files preserved for
        # historical reference. Their relative paths and content are frozen
        # and intentionally not maintained; expecting their links to
        # resolve from the archive/ subdir is anti-purpose. SCHEMA v0.5.1.
        if rel.startswith("archive/") or rel.startswith("archive" + os.sep):
            continue
        try:
            text = md.read_text()
        except (UnicodeDecodeError, PermissionError):
            continue
        fm, body, body_start = parse_frontmatter(text)
        pages.append(Page(
            path=md, rel=rel, frontmatter=fm, body=body,
            body_start_line=body_start,
            is_root_exempt=(rel in ROOT_EXEMPT),
        ))
    return pages


def is_external(path: str) -> bool:
    return not path or path.startswith(EXTERNAL_PREFIXES)


def extract_links(page: Page) -> list[tuple[int, str, str | None, str | None]]:
    """Return list of (lineno, target_path_part, anchor, title) for non-external links."""
    out = []
    for i, line in enumerate(page.body.splitlines(), start=page.body_start_line):
        for m in LINK_RE.finditer(line):
            target = m.group(2)
            if is_external(target):
                continue
            path_part, _, anchor = target.partition("#")
            if not path_part:
                continue
            out.append((i, path_part, anchor or None, m.group(3)))
    return out


def resolve_link(page: Page, path_part: str) -> Path:
    return (page.path.parent / path_part).resolve()


# ----- Rules -----

# Rule 1 (stale-source) retired in v0.5.3. See SCHEMA.md § Lint rules
# (author-side propagation paragraph) for the replacement discipline.


def rule_orphan(pages: list[Page], inbound: dict[Path, list[tuple[Path, int]]]) -> list[Finding]:
    """Rule 2: page has zero inbound links. Root files exempt."""
    findings = []
    for page in pages:
        if page.is_root_exempt:
            continue
        if not inbound.get(page.path.resolve()):
            findings.append(Finding(
                rule="orphan",
                file=page.rel, line=None,
                message="zero inbound links",
                severity="info",  # may be intentional
            ))
    return findings


def rule_tagged_page_needs_sources(pages: list[Page]) -> list[Finding]:
    """Rule 3 (v0.4): page with any [MEASURED] or [ASSERTED] tag must declare
    a non-empty `sources:` frontmatter list.

    Replaces the v0.3 same-bullet inline-link heuristic. Evidence anchoring
    has five legitimate shapes (see concept/evidence-anchoring.md); only the
    page-level commitment in `sources:` is reliably checkable. This rule
    enforces the structural invariant: a tagged page must declare what it
    draws from.

    Applies to: concept/, decision/, hypothesis/, open-question/, incumbent/.
    Exempted: source/ (the page IS the source), experiment/ (sources are in
    method/results prose), root-exempt files.
    """
    applicable_types = {"concept", "decision", "hypothesis", "open-question", "incumbent"}
    findings = []
    for page in pages:
        if page.is_root_exempt:
            continue
        page_type = page.frontmatter.get("type", "")
        if page_type not in applicable_types:
            continue
        # Does the page have any MEASURED/ASSERTED tag?
        tagged = False
        for m in TAG_RE.finditer(page.body):
            if m.group(1) in ("MEASURED", "ASSERTED"):
                tagged = True
                break
        if not tagged:
            continue
        sources = page.frontmatter.get("sources", [])
        if isinstance(sources, list) and len(sources) > 0:
            continue
        findings.append(Finding(
            rule="tagged-page-needs-sources",
            file=page.rel, line=None,
            message=f"{page_type} page has [MEASURED]/[ASSERTED] tags but `sources:` frontmatter is empty",
            severity="warn",
        ))
    return findings


def rule_source_page_has_citation(pages: list[Page]) -> list[Finding]:
    """Rule 3b (v0.4): a source/* page must contain at least one external URL
    in its body. The URL is the page's anchoring commitment to its underlying
    artifact (paper, vendor doc, dataset).

    Catches the failure mode where a source/* page is created but never wired
    to its actual source — i.e. Kyrja-internal synthesis structurally disguised
    as external evidence.
    """
    url_re = re.compile(r'https?://')
    findings = []
    for page in pages:
        if page.is_root_exempt:
            continue
        if page.frontmatter.get("type", "") != "source":
            continue
        if url_re.search(page.body):
            continue
        findings.append(Finding(
            rule="source-page-needs-citation",
            file=page.rel, line=None,
            message="source/* page has no external URL in body — cannot verify it points to an external artifact",
            severity="error",
        ))
    return findings


def rule_dangling_link(pages: list[Page]) -> list[Finding]:
    """Rules 5 + 9: link target doesn't exist; flag with-pending vs without-pending."""
    findings = []
    for page in pages:
        if page.rel in DANGLING_LINK_EXEMPT:
            continue
        for lineno, path_part, _anchor, title in extract_links(page):
            target_abs = resolve_link(page, path_part)
            if target_abs.exists():
                continue
            if title == "pending":
                # Known-future target. SCHEMA exempts these from the dangling rule;
                # report as info severity for visibility only.
                findings.append(Finding(
                    rule="dangling-link-pending",
                    file=page.rel, line=lineno,
                    message=f"pending target: {path_part}",
                    severity="info",
                ))
            else:
                findings.append(Finding(
                    rule="dangling-link",
                    file=page.rel, line=lineno,
                    message=f"target does not exist: {path_part}",
                    severity="error",
                ))
    return findings


def rule_status_mismatch(pages: list[Page], by_abs: dict[Path, Page]) -> list[Finding]:
    """Rule 6: easy deterministic cases.

    - Hypothesis SUPPORTED/REJECTED: must link at least one experiment/* page.
    - Decision with `superseded_by:` set: status must be SUPERSEDED, not ACTIVE.
    - Experiment LANDED: must have a Results or Verdicts section.
    """
    findings = []
    for page in pages:
        if page.is_root_exempt:
            continue
        page_type = page.frontmatter.get("type", "")
        status = page.frontmatter.get("status", "")

        if page_type == "hypothesis" and status in ("SUPPORTED", "REJECTED"):
            has_exp_link = any(
                p.startswith("../experiment/") or p.startswith("./experiment/") or p.startswith("experiment/")
                or "/experiment/" in p
                for _, p, _, _ in extract_links(page)
            )
            if not has_exp_link:
                findings.append(Finding(
                    rule="status-mismatch",
                    file=page.rel, line=None,
                    message=f"hypothesis status={status} but no experiment/* link",
                    severity="error",
                ))

        if page_type == "decision":
            sb = page.frontmatter.get("superseded_by", [])
            if sb and status == "ACTIVE":
                findings.append(Finding(
                    rule="status-mismatch",
                    file=page.rel, line=None,
                    message=f"decision status=ACTIVE but superseded_by is set to {sb}",
                    severity="error",
                ))

        if page_type == "experiment" and status == "LANDED":
            if not re.search(r'^##\s+(Results|Verdicts|Verdict)', page.body, re.MULTILINE | re.IGNORECASE):
                # Umbrella pages may delegate to siblings; check for "Verdicts per hypothesis" etc.
                if not re.search(r'^##\s+Verdicts? per hypothesis', page.body, re.MULTILINE | re.IGNORECASE):
                    findings.append(Finding(
                        rule="status-mismatch",
                        file=page.rel, line=None,
                        message="experiment status=LANDED but no Results/Verdicts section",
                        severity="warn",
                    ))
    return findings


def rule_missing_construct_validity(pages: list[Page]) -> list[Finding]:
    """Rule 8: [MEASURED] tag without a construct-validity note in the same section.

    Window is ±400 chars around the tag, bounded backward by the nearest `##`
    section header. This catches the natural pattern where construct-validity
    is stated in a section header or shared preamble above the measurements.

    v0.5.3: source/* pages exempt. We are quoting paper-internal measurements
    where the experimental paradigm IS the construct; the source page already
    documents the paper's methodology. Rule was designed to enforce Kyrja-
    authored construct-validity statements when translating findings into
    claims — that work happens on concept/decision/hypothesis/experiment pages.
    """
    section_header_re = re.compile(r'^##\s+.*$', re.MULTILINE)
    cv_re = re.compile(r'construct[-\s]validity', re.IGNORECASE)
    findings = []
    for page in pages:
        if page.is_root_exempt:
            continue
        if page.frontmatter.get("type", "") == "source":
            continue
        body = page.body
        for m in TAG_RE.finditer(body):
            if m.group(1) != "MEASURED":
                continue
            tag_pos = m.start()
            # Find nearest `##` header before the tag — backward bound.
            section_start = 0
            for hm in section_header_re.finditer(body, 0, tag_pos):
                section_start = hm.start()
            # Backward window: from section_start to tag_pos (capped at 400 chars back).
            back_start = max(section_start, tag_pos - 400)
            # Forward window: 400 chars past the tag.
            forward_end = min(len(body), tag_pos + 400)
            window = body[back_start:forward_end]
            if cv_re.search(window):
                continue
            lineno = page.body_start_line + body[:tag_pos].count("\n")
            findings.append(Finding(
                rule="missing-construct-validity",
                file=page.rel, line=lineno,
                message="[MEASURED] tag without construct-validity note in the same section (±400 chars, bounded by ## header)",
                severity="warn",
            ))
    return findings


def tagged_claim_inventory(pages: list[Page]) -> list[dict[str, Any]]:
    """Surface every tagged claim for agent review (replaces deterministic rule 4)."""
    inventory = []
    for page in pages:
        if page.is_root_exempt:
            continue
        for i, line in enumerate(page.body.splitlines()):
            for tag_m in TAG_RE.finditer(line):
                inventory.append({
                    "file": page.rel,
                    "line": page.body_start_line + i,
                    "tag": tag_m.group(1),
                    "text": line.strip()[:200],
                })
    return inventory


# ----- Graph build -----

def build_inbound(pages: list[Page]) -> dict[Path, list[tuple[Path, int]]]:
    inbound: dict[Path, list[tuple[Path, int]]] = defaultdict(list)
    for page in pages:
        for lineno, path_part, _anchor, _title in extract_links(page):
            target_abs = resolve_link(page, path_part)
            inbound[target_abs].append((page.path, lineno))
    return inbound


# ----- Output -----

ALL_RULES = [
    "orphan", "tagged-page-needs-sources",
    "source-page-needs-citation", "dangling-link", "dangling-link-pending",
    "status-mismatch", "missing-construct-validity",
]


def run_all_rules(pages: list[Page], rules: list[str]) -> list[Finding]:
    by_abs = {p.path.resolve(): p for p in pages}
    inbound = build_inbound(pages)
    findings: list[Finding] = []
    if "orphan" in rules:
        findings += rule_orphan(pages, inbound)
    if "tagged-page-needs-sources" in rules:
        findings += rule_tagged_page_needs_sources(pages)
    if "source-page-needs-citation" in rules:
        findings += rule_source_page_has_citation(pages)
    if "dangling-link" in rules or "dangling-link-pending" in rules:
        dl = rule_dangling_link(pages)
        if "dangling-link" not in rules:
            dl = [f for f in dl if f.rule == "dangling-link-pending"]
        if "dangling-link-pending" not in rules:
            dl = [f for f in dl if f.rule == "dangling-link"]
        findings += dl
    if "status-mismatch" in rules:
        findings += rule_status_mismatch(pages, by_abs)
    if "missing-construct-validity" in rules:
        findings += rule_missing_construct_validity(pages)
    return findings


def format_markdown(findings: list[Finding], inventory: list[dict] | None) -> str:
    today = date.today().isoformat()
    lines = [f"# Wiki Lint Report — {today}", ""]

    by_rule: dict[str, list[Finding]] = defaultdict(list)
    for f in findings:
        by_rule[f.rule].append(f)

    counts = ", ".join(f"{r}={len(by_rule[r])}" for r in ALL_RULES if r in by_rule) or "(none)"
    lines.append(f"**Summary:** {len(findings)} findings — {counts}")
    lines.append("")

    for rule in ALL_RULES:
        rule_findings = by_rule.get(rule, [])
        if not rule_findings:
            continue
        sev_counts = defaultdict(int)
        for f in rule_findings:
            sev_counts[f.severity] += 1
        sev = ", ".join(f"{s}={n}" for s, n in sev_counts.items())
        lines.append(f"## {rule} ({len(rule_findings)} findings — {sev})")
        lines.append("")
        for f in rule_findings:
            loc = f"{f.file}:{f.line}" if f.line else f.file
            lines.append(f"- **{f.severity}** `{loc}` — {f.message}")
        lines.append("")

    if inventory is not None:
        lines.append(f"## Tagged-claim inventory ({len(inventory)} entries)")
        lines.append("")
        lines.append("*Review for rule-4 contradictions: same claim across pages with different epistemic tags.*")
        lines.append("")
        by_tag: dict[str, list[dict]] = defaultdict(list)
        for item in inventory:
            by_tag[item["tag"]].append(item)
        for tag in ("MEASURED", "ASSERTED", "SPECULATED", "CONTESTED"):
            items = by_tag.get(tag, [])
            if not items:
                continue
            lines.append(f"### [{tag}] ({len(items)})")
            lines.append("")
            for item in items:
                lines.append(f"- `{item['file']}:{item['line']}` — {item['text']}")
            lines.append("")

    return "\n".join(lines) + "\n"


def format_json(findings: list[Finding], inventory: list[dict] | None) -> str:
    out = {
        "date": date.today().isoformat(),
        "findings": [asdict(f) for f in findings],
    }
    if inventory is not None:
        out["inventory"] = inventory
    return json.dumps(out, indent=2)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--wiki", type=Path, default=DEFAULT_WIKI,
                        help=f"Wiki root (default: {DEFAULT_WIKI})")
    parser.add_argument("--rule", action="append", default=None,
                        help=f"Run a single rule (repeatable). Available: {', '.join(ALL_RULES)}")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown",
                        help="Output format")
    parser.add_argument("--include-inventory", action="store_true",
                        help="Include tagged-claim inventory (for rule 4 review)")
    args = parser.parse_args()

    wiki = args.wiki.resolve()
    if not wiki.exists():
        print(f"error: wiki dir not found: {wiki}", file=sys.stderr)
        return 2

    rules = args.rule if args.rule else ALL_RULES
    unknown = [r for r in rules if r not in ALL_RULES]
    if unknown:
        print(f"error: unknown rule(s): {unknown}. Available: {ALL_RULES}", file=sys.stderr)
        return 2

    pages = load_pages(wiki)
    findings = run_all_rules(pages, rules)
    inventory = tagged_claim_inventory(pages) if args.include_inventory else None

    if args.format == "json":
        print(format_json(findings, inventory))
    else:
        print(format_markdown(findings, inventory), end="")

    # Exit code: 0 if no errors, 1 if any error-severity findings.
    has_errors = any(f.severity == "error" for f in findings)
    return 1 if has_errors else 0


if __name__ == "__main__":
    sys.exit(main())
