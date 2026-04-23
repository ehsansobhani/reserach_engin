r"""
generate_summary.py — Produce a structured markdown summary for a paper.

Usage:
    .venv\Scripts\python.exe workflows\generate_summary.py --key <paper_key>

Input:
    memory\papers\<key>_metadata.json
    memory\papers\<key>_classification.md
    memory\papers\<key>.pdf (if available)

Output:
    memory/papers/<key>_summary.md
"""

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from loguru import logger
import yaml

PAPERS_DIR = PROJECT_ROOT / "memory" / "papers"
SCHEMA_PATH = PROJECT_ROOT / "skills" / "systematic_review" / "extraction_schema.yaml"


def _load_schema() -> dict:
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _extract_from_pdf(pdf_path: Path) -> str:
    """Extract text from PDF using PyMuPDF."""
    import fitz
    doc = fitz.open(str(pdf_path))
    text = "\n".join(page.get_text() for page in doc)
    doc.close()
    return text


def generate_summary(key: str) -> None:
    meta_path = PAPERS_DIR / f"{key}_metadata.json"
    class_path = PAPERS_DIR / f"{key}_classification.md"

    if not meta_path.exists():
        raise FileNotFoundError(f"Metadata not found: {meta_path}")

    with open(meta_path, encoding="utf-8") as f:
        meta = json.load(f)

    # Read classification if exists
    included = True
    primary_cat = "general"
    if class_path.exists():
        with open(class_path, encoding="utf-8") as f:
            class_text = f.read()
            if "**Included:** No" in class_text:
                included = False
            for line in class_text.split("\n"):
                if "**Primary category:**" in line:
                    primary_cat = line.split("**Primary category:**")[1].strip()

    if not included:
        logger.info(f"Paper {key} was excluded — skipping summary")
        return

    logger.info(f"Generating summary: {key}")

    # Load schema for reference
    schema = _load_schema()

    # Try to read PDF text
    pdf_path = PAPERS_DIR / f"{meta.get('arxiv_id', key)}.pdf"
    if pdf_path.exists():
        full_text = _extract_from_pdf(pdf_path)
    else:
        full_text = meta.get("abstract", "")

    # Build structured summary
    from datetime import date
    today = date.today().isoformat()

    title = meta.get("title", "Unknown")
    authors = ", ".join(meta.get("authors", ["Unknown"]))
    year = meta.get("year", "?")
    venue = meta.get("venue", "Unknown")

    summary = f"""# Paper Summary: {title}

**Key:** {key}
**Authors:** {authors}
**Year:** {year}
**Venue:** {venue}
**Category:** {primary_cat}
**Date summarized:** {today}

## Metadata

- **arXiv ID:** {meta.get('arxiv_id', 'N/A')}
- **DOI:** {meta.get('doi', 'N/A')}
- **URL:** {meta.get('url', 'N/A')}

## Abstract

{meta.get('abstract', 'No abstract available.')}

## Key Findings

<!-- Synthesize key findings from full text below -->

<!-- [TO BE COMPLETED BY AGENT] -->

## Methodology

<!-- Characterize approach: optimization, simulation, empirical, mixed -->

<!-- [TO BE COMPLETED BY AGENT] -->

## Spatial and Planning Dimensions

<!-- Note planning scale, spatial units, zoning considerations -->

<!-- [TO BE COMPLETED BY AGENT] -->

## Equity and Utilization Treatment

<!-- Note how equity and utilization are defined and measured -->

<!-- [TO BE COMPLETED BY AGENT] -->

## Limitations

<!-- Note limitations stated by authors or evident from analysis -->

<!-- [TO BE COMPLETED BY AGENT] -->

## Relevance to Dissertation

<!-- State how this paper connects to the dissertation's five gaps -->

<!-- [TO BE COMPLETED BY AGENT] -->
"""

    out_path = PAPERS_DIR / f"{key}_summary.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(summary)

    logger.info(f"Summary written: {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate paper summary")
    parser.add_argument("--key", required=True, help="Paper key (e.g., chen_2023)")
    args = parser.parse_args()

    try:
        generate_summary(args.key)
        print(f"[OK] Summary generated: {args.key}")
    except Exception as e:
        logger.error(f"Summary generation failed: {e}")
        sys.exit(1)