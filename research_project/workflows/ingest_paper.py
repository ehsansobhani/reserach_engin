r"""
ingest_paper.py — Acquire a paper and extract metadata.

Usage:
    .venv\Scripts\python.exe workflows\ingest_paper.py --source <identifier>

Identifiers:
    arXiv ID  : e.g., "2301.12345"
    DOI       : e.g., "10.1000/xyz123"
    PDF path  : e.g., "C:/path/to/paper.pdf"
    URL       : e.g., "https://arxiv.org/abs/2301.12345"

Output:
    memory\papers\<key>_metadata.json
    memory\papers\<key>.pdf (if downloadable)
"""

import argparse
import json
import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from loguru import logger
import arxiv
import requests

PAPERS_DIR = PROJECT_ROOT / "memory" / "papers"
PAPERS_DIR.mkdir(parents=True, exist_ok=True)


def _make_key(title: str, year: int) -> str:
    """Generate a filesystem-safe citation key.

    Uses first 2 words + year to avoid collisions from generic first words.
    Replaces unsafe characters with underscore.
    """
    import re
    words = title.split()[:2]
    clean = "_".join(w.strip('":,') for w in words).lower()
    # Remove any remaining unsafe chars
    clean = re.sub(r'[<>:"/\\|?*]', '_', clean)
    return f"{clean}_{year}"


def _fetch_arXiv(arxiv_id: str) -> dict:
    """Download paper info and PDF from arXiv."""
    logger.info(f"Fetching arXiv paper: {arxiv_id}")
    client = arxiv.Client()
    search = arxiv.Search(
        query=arxiv_id,
        max_results=1,
        sort_by=arxiv.SortCriterion.Relevance
    )
    result = next(client.results(search))

    # Metadata
    meta = {
        "title": result.title,
        "authors": [a.name for a in result.authors],
        "year": result.published.year,
        "venue": "arXiv",
        "arxiv_id": result.entry_id.split("/")[-1],
        "abstract": result.summary,
        "doi": result.doi or "",
        "url": result.links[0].href if result.links else result.entry_id,
    }

    # Download PDF
    pdf_path = PAPERS_DIR / f"{meta['arxiv_id']}.pdf"
    if not pdf_path.exists():
        result.download_pdf(dirpath=str(PAPERS_DIR), filename=f"{meta['arxiv_id']}.pdf")
        logger.info(f"PDF saved: {pdf_path}")
    else:
        logger.info(f"PDF already exists: {pdf_path}")

    return meta


def _fetch_doi(doi: str) -> dict:
    """Fetch metadata via CrossRef API."""
    logger.info(f"Fetching DOI: {doi}")
    url = f"https://api.crossref.org/works/{doi}"
    resp = requests.get(url, headers={"Accept": "application/json"}, timeout=30)
    resp.raise_for_status()
    data = resp.json()["message"]

    authors = []
    for a in data.get("author", []):
        name = f"{a.get('given', '')} {a.get('family', '')}".strip()
        if name:
            authors.append(name)

    year = data.get("published-print", data.get("published-online", {}))
    year = year.get("date-parts", [[0]])[0][0]

    meta = {
        "title": data.get("title", [""])[0],
        "authors": authors,
        "year": year,
        "venue": data.get("container-title", [""])[0] if data.get("container-title") else "",
        "doi": doi,
        "arxiv_id": "",
        "abstract": data.get("abstract", ""),
        "url": data.get("URL", f"https://doi.org/{doi}"),
    }
    return meta


def _fetch_url(url: str) -> dict:
    """Fetch metadata by detecting source from URL."""
    logger.info(f"Fetching URL: {url}")
    if "arxiv.org" in url:
        arxiv_id = url.split("arxiv.org/abs/")[-1].strip()
        return _fetch_arXiv(arxiv_id)
    elif "doi.org" in url:
        doi = url.split("doi.org/")[-1].strip()
        return _fetch_doi(doi)
    else:
        raise ValueError(f"Unsupported URL: {url}")


def _fetch_pdf(path: str) -> dict:
    """Extract metadata from a local PDF using PyMuPDF."""
    import fitz

    logger.info(f"Reading PDF: {path}")
    doc = fitz.open(path)
    text = doc[0].get_text()

    # Try to extract title from first line
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    title = lines[0] if lines else "Unknown"

    meta = {
        "title": title,
        "authors": [],
        "year": 0,
        "venue": "PDF",
        "doi": "",
        "arxiv_id": "",
        "abstract": text[:1000],
        "url": path,
    }
    doc.close()
    return meta


def ingest(source: str) -> str:
    """Main ingest dispatcher."""
    source = source.strip()

    if Path(source).exists() and source.endswith(".pdf"):
        meta = _fetch_pdf(source)
    elif source.startswith("10."):
        meta = _fetch_doi(source)
    elif source.startswith("http"):
        meta = _fetch_url(source)
    elif "." in source and "/" not in source and len(source) < 20:
        # Likely an arXiv ID without prefix
        meta = _fetch_arXiv(source)
    else:
        raise ValueError(f"Could not parse source: {source}")

    key = _make_key(meta["title"], meta["year"])
    meta["key"] = key

    out_json = PAPERS_DIR / f"{key}_metadata.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    logger.info(f"Ingested: {key} — {meta['title']}")
    return key


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest a research paper")
    parser.add_argument("--source", required=True, help="arXiv ID, DOI, PDF path, or URL")
    args = parser.parse_args()

    try:
        key = ingest(args.source)
        print(f"[OK] Ingested: {key}")
    except Exception as e:
        logger.error(f"Ingest failed: {e}")
        sys.exit(1)