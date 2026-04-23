r"""
build_related_work.py — Generate a Related Work section from the literature matrix.

Usage:
    .venv\Scripts\python.exe workflows\build_related_work.py [--output <path>]

Reads:
    memory\literature_matrix.md
    memory\papers\<key>_summary.md (all)

Outputs:
    memory/related_work.md (default)
"""

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from loguru import logger

PAPERS_DIR = PROJECT_ROOT / "memory" / "papers"
MATRIX_PATH = PROJECT_ROOT / "memory" / "literature_matrix.md"
OUTPUT_PATH = PROJECT_ROOT / "memory" / "related_work.md"


def group_by_category() -> dict:
    """Group paper summaries by their primary category."""
    groups = {}
    for class_file in PAPERS_DIR.glob("*_classification.md"):
        if "_classification" not in class_file.stem:
            continue
        key = class_file.stem.replace("_classification", "")
        with open(class_file, encoding="utf-8") as f:
            text = f.read()
            if "**Included:** No" in text:
                continue
            primary = "general"
            for line in text.split("\n"):
                if "**Primary category:**" in line:
                    primary = line.split("**Primary category:**")[1].strip()

        if primary not in groups:
            groups[primary] = []
        groups[primary].append(key)
    return groups


def build_related_work(output_path: Path) -> None:
    groups = group_by_category()

    sections = []

    category_order = [
        ("spatial_optimization", "## Spatial Optimization for Charging Infrastructure"),
        ("equity_planning", "## Equity in Charging Infrastructure Planning"),
        ("utilization_modeling", "## Utilization and Demand Modeling"),
        ("rollout_sequencing", "## Rollout and Phased Deployment"),
        ("zoning_land_use", "## Zoning and Land-Use Compatibility"),
        ("meso_micro_bridge", "## Bridging Meso and Micro Scales"),
        ("review_synthesis", "## Reviews and Meta-Analyses"),
        ("general", "## Other Relevant Work"),
    ]

    for cat_id, cat_title in category_order:
        if cat_id not in groups:
            continue

        sections.append(cat_title)
        sections.append("")

        for key in groups[cat_id]:
            summary_path = PAPERS_DIR / f"{key}_summary.md"
            meta_path = PAPERS_DIR / f"{key}_metadata.json"

            if meta_path.exists():
                with open(meta_path, encoding="utf-8") as f:
                    meta = json.load(f)
                title = meta.get("title", key)
                authors = meta.get("authors", [])
                year = meta.get("year", "?")
                venue = meta.get("venue", "")
                authors_str = ", ".join(authors[:3])
                if len(authors) > 3:
                    authors_str += " et al."

                sections.append(f"**{authors_str} ({year}).** {title}. {venue}.")
                sections.append(f"  - Key: `{key}`")

            if summary_path.exists():
                with open(summary_path, encoding="utf-8") as f:
                    summary = f.read()
                # Extract key findings section if present
                if "## Key Findings" in summary:
                    findings_start = summary.index("## Key Findings")
                    next_section = summary.find("## ", findings_start + 1)
                    if next_section > 0:
                        findings = summary[findings_start:next_section].strip()
                    else:
                        findings = summary[findings_start:].strip()
                    # Only add if not placeholder
                    if "[TO BE COMPLETED BY AGENT]" not in findings:
                        sections.append(f"  - Findings: {findings[:200]}...")

            sections.append("")

    content = "# Related Work\n\n"
    content += "The following section is organized by theme, drawing from the reviewed literature.\n\n"
    content += "\n".join(sections)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    logger.info(f"Related work written to: {output_path}")
    print(f"[OK] Related work generated: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build related work section")
    parser.add_argument("--output", default=str(OUTPUT_PATH),
                        help="Output file path")
    args = parser.parse_args()

    try:
        build_related_work(Path(args.output))
    except Exception as e:
        logger.error(f"Build failed: {e}")
        sys.exit(1)