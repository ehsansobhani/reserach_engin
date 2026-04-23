"""
batch_search.py — Search arXiv for candidate papers and ingest them.

Usage:
    .venv\Scripts\python.exe workflows/batch_search.py [--max <N>]

Searches arXiv with multiple queries targeting BEV charging infrastructure
planning literature, deduplicates results, then runs ingest on each paper.
"""

import argparse
import json
import re
import sys
import os
import io
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from loguru import logger
import arxiv

# Queries targeting the dissertation themes
QUERIES = [
    # Core: EV charging infrastructure planning
    "EV charging infrastructure planning urban spatial optimization",
    # Equity + access
    "electric vehicle charging station location optimization equity accessibility",
    # Phased rollout / deployment
    "BEV charging deployment rollout phased urban infrastructure",
    # Zoning + land use
    "charging infrastructure land use zoning regulatory compatibility",
    # Utilization + demand
    "EV charging demand forecasting utilization optimization network",
    # Meso + multi-scale
    "EV charging infrastructure meso micro multi-scale planning",
    # Corridor + urban mobility
    "urban EV charging corridor mobility planning station placement",
    # Coverage + spatial justice
    "electric vehicle charging spatial justice coverage underserved",
    # Station siting + GIS
    "EV charging station siting GIS spatial optimization",
    # Temporal + sequential deployment
    "EV charging infrastructure temporal sequential staged deployment",
    # Gap 2: Zoning / land-use compatibility
    "electric vehicle charging zoning ordinance permitting municipal land use regulation",
    "EV charging station mixed-use district land use compatibility urban form",
    "EV charging parking policy zoning reform urban density incentive",
    # Gap 5: Meso-micro bridge
    "electric vehicle charging district-level meso site selection implementation planning",
    "EV charging infrastructure multi-scale urban district site level planning integration",
]

PAPERS_DIR = PROJECT_ROOT / "memory" / "papers"
PAPERS_DIR.mkdir(parents=True, exist_ok=True)


def _load_existing_ids() -> set[str]:
    """Load base arXiv IDs already ingested or previously failed.

    Strips version suffixes (e.g., '2510.24758v2' -> '2510.24758') so that
    a paper re-discovered with a different version number is still skipped.
    """
    existing = set()
    sources = [
        PROJECT_ROOT / "memory" / "ingested_papers.json",
        PROJECT_ROOT / "memory" / "failed_ingests.json",
    ]
    for path in sources:
        if path.exists():
            with open(path, encoding="utf-8") as f:
                for item in json.load(f):
                    existing.add(re.sub(r"v\d+$", "", item[0]))
    logger.info(f"Loaded {len(existing)} existing base IDs to skip")
    return existing


def search_and_collect(
    max_results: int = 100,
    existing_ids: set[str] | None = None,
) -> list[tuple[str, str, int]]:
    """Run queries, collect and deduplicate papers, skipping already-ingested IDs."""
    seen = set(existing_ids or set())
    collected = []

    for q in QUERIES:
        logger.info(f"Query: {q[:60]}...")
        try:
            client = arxiv.Client()
            search = arxiv.Search(
                query=q,
                max_results=50,
                sort_by=arxiv.SortCriterion.Relevance
            )
            results = list(client.results(search))
            for r in results:
                aid = r.entry_id.split("/")[-1]
                base_aid = re.sub(r"v\d+$", "", aid)
                if base_aid not in seen:
                    seen.add(base_aid)
                    collected.append((aid, r.title, r.published.year))
        except Exception as e:
            logger.warning(f"Query failed: {e}")
        time.sleep(1)  # be respectful to arXiv

    logger.info(f"Collected {len(collected)} unique new papers")
    return collected


def main():
    # Ensure UTF-8 stdout on Windows
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Search and ingest papers")
    parser.add_argument("--max", type=int, default=100, help="Max papers to ingest")
    args = parser.parse_args()

    # Load existing IDs to prevent re-ingestion
    existing_ids = _load_existing_ids()

    # Search
    papers = search_and_collect(max_results=args.max, existing_ids=existing_ids)
    to_ingest = papers[: args.max]

    print(f"\n=== Ingesting {len(to_ingest)} papers ===\n")

    # Ingest each
    from workflows.ingest_paper import ingest as _ingest

    ingested = []
    failed = []

    for i, (aid, title, year) in enumerate(to_ingest, 1):
        logger.info(f"[{i}/{len(to_ingest)}] Ingesting {aid}: {title[:50]}...")
        try:
            key = _ingest(aid)
            ingested.append((aid, key, title))
            print(f"  [OK] {aid} -> {key}")
        except Exception as e:
            failed.append((aid, title, str(e)))
            print(f"  [FAIL] {aid}: {e}")
        time.sleep(1)  # rate limit

    # Summary
    print(f"\n=== Summary ===")
    print(f"Ingested: {len(ingested)}")
    print(f"Failed:   {len(failed)}")

    # Save failed list (append to existing)
    failed_path = PAPERS_DIR.parent / "failed_ingests.json"
    if failed:
        existing_failed = json.load(open(failed_path, encoding="utf-8")) if failed_path.exists() else []
        with open(failed_path, "w", encoding="utf-8") as f:
            json.dump(existing_failed + failed, f, indent=2)
        print(f"Failed list saved to: {failed_path}")

    # Save ingested list (append to existing)
    ingested_path = PAPERS_DIR.parent / "ingested_papers.json"
    existing_ingested = json.load(open(ingested_path, encoding="utf-8")) if ingested_path.exists() else []
    with open(ingested_path, "w", encoding="utf-8") as f:
        json.dump(existing_ingested + ingested, f, indent=2)
    print(f"Ingested list saved to: {ingested_path} ({len(existing_ingested) + len(ingested)} total)")


if __name__ == "__main__":
    main()
