"""
run_gap_analysis.py — Aggregate extraction data and produce detailed gap analysis.

Usage:
    .venv\Scripts\python.exe workflows\run_gap_analysis.py

Reads: memory/papers/*_extraction.md (fallback: *_classification.md + *_metadata.json)
Writes: memory/research_gaps.md
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from loguru import logger

PAPERS_DIR = PROJECT_ROOT / "memory" / "papers"
OUTPUT_PATH = PROJECT_ROOT / "memory" / "research_gaps.md"

GAPS = {
    1: ("Misaligned Spatial Units",
        "Administrative zoning boundaries poorly represent actual mobility corridor patterns, "
        "creating spatial misalignment between infrastructure supply and travel demand."),
    2: ("Lack of Zoning Impact Analysis",
        "Systematic comparison of alternative zoning schemas — ordinance types, land-use "
        "categories, regulatory frameworks — for charging infrastructure siting is absent."),
    3: ("Equity and Utilization Separation",
        "Most studies optimize equity of access or infrastructure utilization independently; "
        "joint multi-objective treatment is rare."),
    4: ("Static Optimization Dominance",
        "The overwhelming majority of models optimize a single planning period. "
        "Phased, budget-constrained, adaptive rollout sequencing is underrepresented."),
    5: ("Missing Meso-Micro Integration",
        "No integrated framework bridges meso-scale city-level rollout plans to "
        "micro-scale site-level implementation specifications."),
}

SUB_GAPS = {
    1: [
        "Mobility-corridor spatial unit construction (vs. administrative TAZ)",
        "Cross-jurisdictional demand integration",
        "Trip-chain-based spatial disaggregation",
        "Validation of corridor vs. admin spatial unit accuracy",
    ],
    2: [
        "Comparative analysis of ≥2 distinct municipal zoning schemas",
        "Land-use compatibility scoring methodology",
        "Regulatory heterogeneity modeled as optimization constraint",
        "Zoning ordinance impact on station density and equity outcomes",
    ],
    3: [
        "Joint equity + utilization in a single objective function",
        "Pareto frontier between equity and utilization computed",
        "Gini or accessibility index used alongside utilization metric",
        "Temporal equity (peak vs. off-peak access) measured",
    ],
    4: [
        "Multi-stage / phased location model with budget constraint per phase",
        "Adaptive phase-transition trigger criteria defined",
        "Demand uncertainty modeled across phases (stochastic)",
        "Value of sequential planning quantified vs. static",
    ],
    5: [
        "Explicit meso-to-micro translation method defined",
        "Site-level siting criteria derived from meso output",
        "Minimum viable information set for site-level decisions specified",
        "Feedback loop from micro constraints to meso plan defined",
    ],
}


def _parse_field(text: str, field: str) -> str:
    m = re.search(r"\*\*" + re.escape(field) + r":\*\*\s*(.+)", text)
    return m.group(1).strip() if m else ""


def _bool_field(text: str, field: str) -> bool:
    val = _parse_field(text, field)
    return val.lower() == "true"


def load_paper(key: str) -> dict | None:
    meta_path = PAPERS_DIR / f"{key}_metadata.json"
    class_path = PAPERS_DIR / f"{key}_classification.md"
    ext_path = PAPERS_DIR / f"{key}_extraction.md"

    if not meta_path.exists():
        return None

    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    class_text = class_path.read_text(encoding="utf-8") if class_path.exists() else ""

    if "**Included:** Yes" not in class_text:
        return None

    record = {
        "key": key,
        "title": meta.get("title", "Unknown"),
        "authors": meta.get("authors", []),
        "year": meta.get("year", 0),
        "venue": meta.get("venue", "arXiv"),
        "arxiv_id": meta.get("arxiv_id", ""),
        "abstract": meta.get("abstract", ""),
    }

    # Parse gaps from classification checkboxes
    record["gaps"] = {i: f"[✓] Gap {i}" in class_text for i in range(1, 6)}

    # Get category
    primary = "general"
    secondary = []
    for line in class_text.split("\n"):
        if "**Primary category:**" in line:
            primary = line.split("**Primary category:**")[1].strip()
        if "**Secondary categories:**" in line:
            sec = line.split("**Secondary categories:**")[1].strip()
            if sec and sec.lower() != "none":
                secondary = [c.strip() for c in sec.split(",")]
    record["category"] = primary
    record["secondary"] = secondary

    # Parse from extraction file if available, else derive from categories
    if ext_path.exists():
        ext = ext_path.read_text(encoding="utf-8")
        record["scope"] = _parse_field(ext, "Geographic scope") or "city"
        record["approach"] = _parse_field(ext, "Approach") or "optimization"
        record["equity"] = _bool_field(ext, "Equity measured")
        record["utilization"] = _bool_field(ext, "Utilization measured")
        record["phased"] = _bool_field(ext, "Phased approach")
        record["zoning"] = _bool_field(ext, "Zoning considered")
        record["meso"] = _bool_field(ext, "Meso-level")
        record["micro"] = _bool_field(ext, "Micro-level")
        record["multi_obj"] = _bool_field(ext, "Multi-objective")
    else:
        all_cats = (primary + " " + " ".join(secondary)).lower()
        record["scope"] = "city"
        record["approach"] = "optimization"
        record["equity"] = "equity_planning" in all_cats
        record["utilization"] = "utilization_modeling" in all_cats
        record["phased"] = "rollout_sequencing" in all_cats
        record["zoning"] = "zoning_land_use" in all_cats
        record["meso"] = "meso_micro_bridge" in all_cats
        record["micro"] = False
        record["multi_obj"] = False

    return record


def _auth_short(paper: dict) -> str:
    authors = paper["authors"]
    if not authors:
        return "Unknown"
    last = authors[0].split()[-1]
    return last + " et al." if len(authors) > 1 else last


def build_research_gaps_md(records: list[dict]) -> str:
    total = len(records)
    lines = [
        "# Dissertation Research Gaps — Detailed Analysis",
        "",
        f"**Total included papers:** {total}",
        f"**Generated from:** systematic extraction of {total} papers.",
        "",
    ]

    # Per-gap sections
    for gap_num in range(1, 6):
        label, desc = GAPS[gap_num]
        papers_in_gap = [r for r in records if r["gaps"].get(gap_num)]
        n = len(papers_in_gap)
        level = "Low" if n < 10 else "Medium" if n < 50 else "High"

        lines += [
            "---",
            f"## Gap {gap_num} — {label}",
            "",
            f"**Definition:** {desc}",
            "",
            f"**Papers addressing this gap:** {n} of {total} ({100*n/total:.0f}%)",
            f"**Coverage level:** {level}",
            "",
            "### What Remains Unaddressed",
            "",
        ]
        for sub in SUB_GAPS[gap_num]:
            lines.append(f"- {sub}")
        lines.append("")

        if papers_in_gap:
            lines += [
                "### Papers Addressing This Gap",
                "",
                "| Key | Authors | Year | Approach | Scope | Equity | Util. | Phased |",
                "|-----|---------|------|----------|-------|--------|-------|--------|",
            ]
            for p in sorted(papers_in_gap, key=lambda x: x["year"], reverse=True):
                auth = _auth_short(p)
                eq = "Y" if p["equity"] else "N"
                util = "Y" if p["utilization"] else "N"
                ph = "Y" if p["phased"] else "N"
                lines.append(
                    f"| `{p['key']}` | {auth} | {p['year']} | "
                    f"{p['approach']} | {p['scope']} | {eq} | {util} | {ph} |"
                )
        else:
            lines.append("*No papers directly address this gap as a primary contribution.*")
        lines.append("")

    # Gap summary table
    lines += [
        "---",
        "## Gap Coverage Summary",
        "",
        "| Gap | Label | N Papers | % | Level | Key Missing Dimension |",
        "|-----|-------|----------|---|-------|-----------------------|",
    ]
    for gap_num in range(1, 6):
        label, _ = GAPS[gap_num]
        n = sum(1 for r in records if r["gaps"].get(gap_num))
        pct = f"{100*n/total:.0f}%"
        level = "Low" if n < 10 else "Medium" if n < 50 else "High"
        missing = SUB_GAPS[gap_num][0][:80]
        lines.append(f"| Gap {gap_num} | {label} | {n} | {pct} | {level} | {missing} |")
    lines.append("")

    # Methodology distribution
    by_approach = Counter(r["approach"] for r in records)
    lines += [
        "---",
        "## Methodology Distribution",
        "",
        "| Approach | N | % of Corpus |",
        "|----------|---|-------------|",
    ]
    for approach, cnt in by_approach.most_common():
        lines.append(f"| {approach} | {cnt} | {100*cnt/total:.1f}% |")
    lines.append("")

    # Spatial scope
    by_scope = Counter(r["scope"] for r in records)
    lines += [
        "## Spatial Scope Distribution",
        "",
        "| Scope | N | % |",
        "|-------|---|---|",
    ]
    for scope, cnt in by_scope.most_common():
        lines.append(f"| {scope} | {cnt} | {100*cnt/total:.1f}% |")
    lines.append("")

    # Category distribution
    by_cat = Counter(r["category"] for r in records)
    lines += [
        "## Primary Category Distribution",
        "",
        "| Category | N | % |",
        "|----------|---|---|",
    ]
    for cat, cnt in by_cat.most_common():
        lines.append(f"| {cat} | {cnt} | {100*cnt/total:.1f}% |")
    lines.append("")

    # Thematic flag summary
    flags = [
        ("Equity measured", sum(1 for r in records if r["equity"])),
        ("Utilization measured", sum(1 for r in records if r["utilization"])),
        ("Phased approach", sum(1 for r in records if r["phased"])),
        ("Zoning considered", sum(1 for r in records if r["zoning"])),
        ("Meso-level", sum(1 for r in records if r["meso"])),
        ("Multi-objective", sum(1 for r in records if r["multi_obj"])),
    ]
    lines += [
        "## Thematic Coverage Flags",
        "",
        "| Dimension | N | % of Corpus |",
        "|-----------|---|-------------|",
    ]
    for dim, cnt in flags:
        lines.append(f"| {dim} | {cnt} | {100*cnt/total:.1f}% |")
    lines.append("")

    return "\n".join(lines) + "\n"


def main():
    # Load all included papers
    records = []
    seen_arxiv_ids: set[str] = set()

    for cf in sorted(PAPERS_DIR.glob("*_classification.md")):
        key = cf.stem.replace("_classification", "")
        r = load_paper(key)
        if r is None:
            continue
        # Deduplicate by arxiv_id
        aid = r.get("arxiv_id", "")
        if aid and aid in seen_arxiv_ids:
            logger.warning(f"Duplicate arXiv ID {aid} for key {key} — skipping")
            continue
        if aid:
            seen_arxiv_ids.add(aid)
        records.append(r)

    logger.info(f"Loaded {len(records)} unique included papers")

    content = build_research_gaps_md(records)
    OUTPUT_PATH.write_text(content, encoding="utf-8")
    logger.info(f"Research gaps written: {OUTPUT_PATH}")
    print(f"[OK] Gap analysis complete: {len(records)} papers -> {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
