r"""
classify_paper.py — Classify a paper against inclusion/exclusion criteria.

Usage:
    .venv\Scripts\python.exe workflows\classify_paper.py --key <paper_key>

Input:
    memory\papers\<key>_metadata.json
    memory\papers\<key>.pdf (if available)

Output:
    memory/papers/<key>_classification.md
"""

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from loguru import logger
import json

PAPERS_DIR = PROJECT_ROOT / "memory" / "papers"


# Inclusion criteria from agents/paper_classifier.md
INCLUDE_IF = [
    "EV charging infrastructure planning at urban or regional scale",
    "Spatial optimization for charging station placement",
    "Equity considerations in infrastructure distribution",
    "Utilization optimization for charging networks",
    "Rollout or phased deployment planning for infrastructure",
    "Zoning or land-use compatibility for charging infrastructure",
    "Meso-micro planning integration for infrastructure",
]

EXCLUDE_IF = [
    "Pure V2G (vehicle-to-grid) technical without spatial planning",
    "Highway-only corridor focus without urban context",
    "Pure engineering paper with no planning or optimization component",
    "Conference poster or workshop without sufficient methodology detail",
]

CATEGORIES = [
    "spatial_optimization",
    "equity_planning",
    "utilization_modeling",
    "rollout_sequencing",
    "zoning_land_use",
    "meso_micro_bridge",
    "review_synthesis",
    "general",
]

DISSERTATION_GAPS = [
    ("Gap 1", "Misaligned spatial units"),
    ("Gap 2", "Lack of zoning impact analysis"),
    ("Gap 3", "Equity and utilization separation"),
    ("Gap 4", "Static optimization dominance"),
    ("Gap 5", "Missing meso-micro integration"),
]


def classify(key: str) -> None:
    meta_path = PAPERS_DIR / f"{key}_metadata.json"
    if not meta_path.exists():
        raise FileNotFoundError(f"Metadata not found: {meta_path}")

    with open(meta_path, encoding="utf-8") as f:
        meta = json.load(f)

    logger.info(f"Classifying: {key} — {meta.get('title', 'NO TITLE')}")

    # Read abstract for classification decision
    abstract = meta.get("abstract", "")

    # Simple keyword-based classification
    # In production, this would use LLM reasoning via the paper_classifier agent
    text = (meta.get("title", "") + " " + abstract).lower()

    # Detect relevant themes
    themes = {
        "spatial_optimization": any(k in text for k in [
            "location", "placement", "spatial", "optimization", "sitING", "gis"
        ]),
        "equity_planning": any(k in text for k in [
            "equity", "fairness", "justice", "underserved", "accessible", "spatial accessibility"
        ]),
        "utilization_modeling": any(k in text for k in [
            "utilization", "demand", "capacity", "usage", "fill rate", "charging demand"
        ]),
        "rollout_sequencing": any(k in text for k in [
            "rollout", "phased", "deployment", "temporal", "staged", "sequential"
        ]),
        "zoning_land_use": any(k in text for k in [
            "zoning", "land use", "land-use", "regulatory", "compatibility", "ordinance"
        ]),
        "meso_micro_bridge": any(k in text for k in [
            "meso", "micro", "site-level", "implementation", "scaling", "multi-scale"
        ]),
        "review_synthesis": any(k in text for k in [
            "review", "systematic", "meta-analys", "survey", "overview"
        ]),
    }

    included_categories = [cat for cat, present in themes.items() if present]
    if not included_categories:
        included_categories = ["general"]

    # Exclusion logic
    excluded = False
    reason = ""

    if not any(k in text for k in ["charging", "ev ", "electric vehicle", "bev"]):
        excluded = True
        reason = "Paper does not address EV charging infrastructure"
    elif all(k in text for k in ["vehicle-to-grid", "v2g"]) and "infrastructure" not in text:
        excluded = True
        reason = "Focuses on V2G technical aspects without infrastructure planning"
    elif "highway" in text and "urban" not in text and "city" not in text:
        excluded = True
        reason = "Focuses on highway/corridor without urban context"

    # Determine mapped gaps
    gap_map = {
        "spatial_optimization": ["Gap 1"],
        "zoning_land_use": ["Gap 2"],
        "equity_planning": ["Gap 3"],
        "rollout_sequencing": ["Gap 4"],
        "meso_micro_bridge": ["Gap 5"],
    }

    mapped_gaps = []
    for cat in included_categories:
        if cat in gap_map:
            mapped_gaps.extend(gap_map[cat])

    from datetime import date
    today = date.today().isoformat()

    output = f"""# Classification: {meta.get('title', 'Unknown')}

**Key:** {key}
**arXiv ID:** {meta.get('arxiv_id', 'N/A')}
**DOI:** {meta.get('doi', 'N/A')}
**Date reviewed:** {today}

## Inclusion Decision

**Included:** {"Yes" if not excluded else "No"}
**Reason:** {reason if excluded else "Meets inclusion criteria — addresses relevant BEV charging infrastructure planning themes"}

## Categories

**Primary category:** {included_categories[0]}
**Secondary categories:** {", ".join(included_categories[1:]) if len(included_categories) > 1 else "None"}

## Mapped to Dissertation Gaps

"""
    for gap in DISSERTATION_GAPS:
        flag = "✓" if gap[0].replace("Gap ", "Gap ") in mapped_gaps else " "
        output += f"- [{flag}] {gap[0]}: {gap[1]}\n"

    output += f"""
## Abstract

 {abstract[:500]}{"..." if len(abstract) > 500 else ""}
"""

    out_path = PAPERS_DIR / f"{key}_classification.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output)

    logger.info(f"Classification written: {out_path}")
    if excluded:
        logger.info(f"  → Excluded: {reason}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Classify a paper")
    parser.add_argument("--key", required=True, help="Paper key (e.g., chen_2023)")
    args = parser.parse_args()

    try:
        classify(args.key)
        print(f"[OK] Classification complete: {args.key}")
    except Exception as e:
        logger.error(f"Classification failed: {e}")
        sys.exit(1)