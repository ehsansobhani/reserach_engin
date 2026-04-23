r"""
update_matrix.py — Refresh the literature matrix with all ingested papers.

Usage:
    .venv\Scripts\python.exe workflows\update_matrix.py

Reads:
    memory\papers\<key>_metadata.json
    memory\papers\<key>_classification.md
    memory\papers\<key>_summary.md (if exists)

Outputs:
    memory\literature_matrix.md
"""

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from loguru import logger

PAPERS_DIR = PROJECT_ROOT / "memory" / "papers"
MATRIX_PATH = PROJECT_ROOT / "memory" / "literature_matrix.md"


def build_matrix() -> None:
    # Collect all papers with metadata and classification
    papers = []
    for meta_file in PAPERS_DIR.glob("*_metadata.json"):
        key = meta_file.stem.replace("_metadata", "")
        with open(meta_file, encoding="utf-8") as f:
            meta = json.load(f)

        class_file = PAPERS_DIR / f"{key}_classification.md"
        included = False
        primary_cat = "unknown"
        mapped_gaps = []

        if class_file.exists():
            with open(class_file, encoding="utf-8") as f:
                text = f.read()
                included = "**Included:** Yes" in text
                for line in text.split("\n"):
                    if "**Primary category:**" in line:
                        primary_cat = line.split("**Primary category:**")[1].strip()
                    if "✓ Gap" in line:
                        parts = line.strip().split("]", 1)
                        if len(parts) > 1:
                            mapped_gaps.append(parts[1].strip())

        if not included:
            continue

        papers.append({
            "key": key,
            "title": meta.get("title", "Unknown"),
            "authors": meta.get("authors", []),
            "year": meta.get("year", "?"),
            "venue": meta.get("venue", "Unknown"),
            "arxiv_id": meta.get("arxiv_id", ""),
            "doi": meta.get("doi", ""),
            "category": primary_cat,
            "gaps": mapped_gaps,
        })

    # Sort by year descending
    papers.sort(key=lambda p: p.get("year", 0), reverse=True)

    # Build markdown table
    lines = [
        "# Literature Matrix",
        "",
        f"**Total included papers:** {len(papers)}",
        "",
        "| # | Key | Title | Authors | Year | Venue | Category | Gaps |",
        "|---|-----|-------|---------|------|-------|----------|------|",
    ]

    for i, p in enumerate(papers, 1):
        authors_str = ", ".join(p["authors"][:3])
        if len(p["authors"]) > 3:
            authors_str += " et al."
        title_short = p["title"][:60] + "..." if len(p["title"]) > 60 else p["title"]
        gaps_str = ", ".join(p["gaps"]) if p["gaps"] else "—"

        lines.append(
            f"| {i} | `{p['key']}` | {title_short} | {authors_str} | "
            f"{p['year']} | {p['venue']} | {p['category']} | {gaps_str} |"
        )

    # Write matrix
    content = "\n".join(lines) + "\n"
    with open(MATRIX_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    logger.info(f"Literature matrix updated: {len(papers)} papers")
    print(f"[OK] Matrix updated: {len(papers)} papers at {MATRIX_PATH}")


if __name__ == "__main__":
    try:
        build_matrix()
    except Exception as e:
        logger.error(f"Matrix update failed: {e}")
        sys.exit(1)