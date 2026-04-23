"""
extract_paper.py — Automated extraction from abstract + metadata for all included papers.

Usage:
    .venv\Scripts\python.exe workflows\extract_paper.py [--key <key>]

Without --key, processes all included papers that lack an extraction file.
Output: memory/papers/<key>_extraction.md
"""

import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from loguru import logger

PAPERS_DIR = PROJECT_ROOT / "memory" / "papers"

# ── Detection patterns ──────────────────────────────────────────────────────

SCOPE_PATTERNS = {
    "site":         ["site-level", "parcel-level", "site design", "site selection", "site siting"],
    "neighborhood": ["neighborhood", "district-level", "census tract", "block-level"],
    "corridor":     ["corridor", "highway corridor", "inter-city route", "en-route"],
    "regional":     ["regional", "multi-city", "statewide", "national-scale", "province"],
    "city":         ["city-scale", "city scale", "urban area", "metropolitan", "intracity",
                     "localized urban", "city-wide", "citywide", "city level"],
}
SCOPE_ORDER = ["site", "neighborhood", "corridor", "regional", "city"]

APPROACH_PATTERNS = {
    "optimization": ["milp", "mixed-integer", "linear program", "optimize", "optimization",
                     "bilevel", "bi-level", "min-max", "mathematical program", "integer program",
                     "lp model", "convex", "lagrangian", "branch and bound"],
    "simulation":   ["simulat", "agent-based", "monte carlo", "discrete event",
                     "stochastic simulat", "queuing model", "queue"],
    "empirical":    ["real-world", "real world", "actual data", "survey", "empirical",
                     "case study", "observed", "field study", "historical data",
                     "real data", "collected data", "dataset"],
}

SPATIAL_UNIT_KEYWORDS = [
    "traffic analysis zone", "TAZ", "grid cell", "grid-based", "hexagon",
    "parcel", "census tract", "block group", "administrative zone",
    "district", "polygon", "fishnet", "voronoi",
]

DATA_SOURCE_PATTERNS = {
    "real":       ["real-world", "real world", "actual", "empirical data", "collected",
                   "observed", "real data", "field data"],
    "synthetic":  ["synthetic", "generated", "simulated data", "hypothetical network",
                   "artificially"],
    "hypothetical": ["hypothetical", "illustrative", "test network", "toy example",
                     "benchmark network"],
}

MULTI_OBJ_PATTERNS = [
    "multi-objective", "multiobjective", "pareto", "bi-objective",
    "two objectives", "dual objective", "triple objective",
]

MICRO_PATTERNS = [
    "site-level", "parcel-level", "micro-scale", "street-level",
    "station design", "site layout", "facility design",
]

LIMITATION_KEYWORDS = [
    "limitation", "future work", "future research", "drawback",
    "not consider", "beyond the scope", "cannot", "restricted to",
    "simplif", "we do not", "does not account",
]


# ── Helper functions ─────────────────────────────────────────────────────────

def _lower(text: str) -> str:
    return text.lower()


def detect_scope(text: str) -> str:
    t = _lower(text)
    for scope in SCOPE_ORDER:
        if any(k in t for k in SCOPE_PATTERNS[scope]):
            return scope
    return "city"


def detect_approach(text: str) -> str:
    t = _lower(text)
    hits = {cat for cat, kws in APPROACH_PATTERNS.items() if any(k in t for k in kws)}
    if len(hits) >= 2:
        return "mixed"
    if hits:
        return next(iter(hits))
    return "optimization"


def detect_spatial_unit(text: str) -> str:
    t = _lower(text)
    for kw in SPATIAL_UNIT_KEYWORDS:
        if kw.lower() in t:
            return kw
    return "not specified"


def detect_data_source(text: str) -> str:
    t = _lower(text)
    for src in ["real", "synthetic", "hypothetical"]:
        if any(k in t for k in DATA_SOURCE_PATTERNS[src]):
            return src
    return "not specified"


def detect_multi_obj(text: str) -> bool:
    t = _lower(text)
    return any(k in t for k in MULTI_OBJ_PATTERNS)


def detect_micro(text: str) -> bool:
    t = _lower(text)
    return any(k in t for k in MICRO_PATTERNS)


def extract_limitations(abstract: str) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", abstract.strip())
    found = [s.strip() for s in sentences
             if any(k in s.lower() for k in LIMITATION_KEYWORDS)]
    return found[:3]


def parse_gaps(class_text: str) -> dict[int, bool]:
    gaps = {}
    for i in range(1, 6):
        gaps[i] = f"[✓] Gap {i}" in class_text
    return gaps


def parse_categories(class_text: str) -> tuple[str, list[str]]:
    primary = "general"
    secondary = []
    for line in class_text.split("\n"):
        if "**Primary category:**" in line:
            primary = line.split("**Primary category:**")[1].strip()
        if "**Secondary categories:**" in line:
            sec = line.split("**Secondary categories:**")[1].strip()
            if sec and sec.lower() != "none":
                secondary = [c.strip() for c in sec.split(",")]
    return primary, secondary


def derive_flags(primary: str, secondary: list[str]) -> dict[str, bool]:
    all_cats = (primary + " " + " ".join(secondary)).lower()
    return {
        "equity_measured": "equity_planning" in all_cats,
        "utilization_measured": "utilization_modeling" in all_cats,
        "phased_approach": "rollout_sequencing" in all_cats,
        "zoning_considered": "zoning_land_use" in all_cats,
        "meso_level": "meso_micro_bridge" in all_cats,
    }


def build_extraction_md(
    key: str,
    meta: dict,
    primary_cat: str,
    scope: str,
    spatial_unit: str,
    approach: str,
    data_source: str,
    multi_obj: bool,
    flags: dict,
    gaps: dict,
    limitations: list[str],
) -> str:
    title = meta.get("title", "Unknown")
    authors = ", ".join(meta.get("authors", ["Unknown"]))
    year = meta.get("year", "?")
    abstract = meta.get("abstract", "")

    lim_block = ("\n".join(f"- {l}" for l in limitations)
                 if limitations else "None detected in abstract.")

    def yn(v: bool) -> str:
        return "True" if v else "False"

    return f"""# Extraction: {title}

**Key:** {key}
**Authors:** {authors}
**Year:** {year}
**Category:** {primary_cat}

## Problem Scope

- **Geographic scope:** {scope}
- **Spatial unit:** {spatial_unit}

## Methodology

- **Approach:** {approach}
- **Data source:** {data_source}
- **Multi-objective:** {yn(multi_obj)}

## Thematic Flags

- **Equity measured:** {yn(flags.get('equity_measured', False))}
- **Utilization measured:** {yn(flags.get('utilization_measured', False))}
- **Phased approach:** {yn(flags.get('phased_approach', False))}
- **Zoning considered:** {yn(flags.get('zoning_considered', False))}
- **Meso-level:** {yn(flags.get('meso_level', False))}
- **Micro-level:** {yn(flags.get('micro_level', False))}

## Gap Mapping

- **Gap 1 (Misaligned spatial units):** {yn(gaps.get(1, False))}
- **Gap 2 (Zoning impact analysis):** {yn(gaps.get(2, False))}
- **Gap 3 (Equity-utilization joint):** {yn(gaps.get(3, False))}
- **Gap 4 (Phased rollout):** {yn(gaps.get(4, False))}
- **Gap 5 (Meso-micro bridge):** {yn(gaps.get(5, False))}

## Limitations Detected

{lim_block}

## Abstract

{abstract}
"""


def extract_paper(key: str) -> None:
    meta_path = PAPERS_DIR / f"{key}_metadata.json"
    class_path = PAPERS_DIR / f"{key}_classification.md"
    out_path = PAPERS_DIR / f"{key}_extraction.md"

    if not meta_path.exists():
        raise FileNotFoundError(f"Metadata not found: {meta_path}")

    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    class_text = class_path.read_text(encoding="utf-8") if class_path.exists() else ""

    if "**Included:** No" in class_text:
        logger.debug(f"Skipping excluded: {key}")
        return

    abstract = meta.get("abstract", "")
    title = meta.get("title", "")
    text = title + " " + abstract

    primary_cat, secondary_cats = parse_categories(class_text)
    gaps = parse_gaps(class_text)
    flags = derive_flags(primary_cat, secondary_cats)
    flags["micro_level"] = detect_micro(text)

    scope = detect_scope(text)
    approach = detect_approach(text)
    spatial_unit = detect_spatial_unit(text)
    data_source = detect_data_source(text)
    multi_obj = detect_multi_obj(text)
    limitations = extract_limitations(abstract) if abstract else []

    content = build_extraction_md(
        key=key, meta=meta, primary_cat=primary_cat,
        scope=scope, spatial_unit=spatial_unit, approach=approach,
        data_source=data_source, multi_obj=multi_obj,
        flags=flags, gaps=gaps, limitations=limitations,
    )
    out_path.write_text(content, encoding="utf-8")
    logger.info(f"Extraction written: {key}")


def main():
    parser = argparse.ArgumentParser(description="Extract paper data from abstract + metadata")
    parser.add_argument("--key", help="Process a single paper key")
    args = parser.parse_args()

    if args.key:
        extract_paper(args.key)
        print(f"[OK] Extracted: {args.key}")
        return

    # Batch: all included papers without extraction files
    included_keys = []
    for cf in sorted(PAPERS_DIR.glob("*_classification.md")):
        text = cf.read_text(encoding="utf-8")
        if "**Included:** Yes" in text:
            included_keys.append(cf.stem.replace("_classification", ""))

    logger.info(f"Processing {len(included_keys)} included papers")
    success, skip, fail = 0, 0, 0

    for key in included_keys:
        ext_path = PAPERS_DIR / f"{key}_extraction.md"
        if ext_path.exists():
            skip += 1
            continue
        try:
            extract_paper(key)
            success += 1
        except Exception as e:
            logger.error(f"Failed {key}: {e}")
            fail += 1

    print(f"[OK] Extraction complete: {success} written, {skip} skipped, {fail} failed")


if __name__ == "__main__":
    main()
