"""
generate_bibtex.py — Generate BibTeX references from all included papers.

Usage:
    .venv\Scripts\python.exe workflows\generate_bibtex.py

Reads: memory/papers/*_metadata.json + *_classification.md
Writes: memory/references.bib
"""

import json
import sys
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from loguru import logger

PAPERS_DIR = PROJECT_ROOT / "memory" / "papers"
BIB_PATH = PROJECT_ROOT / "memory" / "references.bib"

_BIBTEX_ESCAPES = str.maketrans({
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "{": "",
    "}": "",
    "~": r"\~{}",
})


def _sanitize(value: str) -> str:
    return value.translate(_BIBTEX_ESCAPES).strip()


def _format_authors(authors: list[str]) -> str:
    if not authors:
        return "Unknown Author"
    return " and ".join(authors)


def make_entry(key: str, meta: dict) -> str:
    title = _sanitize(meta.get("title", "Unknown"))
    authors = _format_authors(meta.get("authors", []))
    year = str(meta.get("year", 0))
    venue = _sanitize(meta.get("venue", "arXiv"))
    doi = meta.get("doi", "")
    arxiv_id = meta.get("arxiv_id", "")
    url = meta.get("url", "")

    # Use @article for DOI-bearing papers, @misc for arXiv-only
    if doi and venue.lower() not in ("arxiv", "pdf", ""):
        entry_type = "article"
    else:
        entry_type = "misc"

    lines = [f"@{entry_type}{{{key},"]
    lines.append(f"  title = {{{title}}},")
    lines.append(f"  author = {{{authors}}},")
    lines.append(f"  year = {{{year}}},")

    if entry_type == "article":
        lines.append(f"  journal = {{{venue}}},")
        if doi:
            lines.append(f"  doi = {{{doi}}},")
    else:
        if arxiv_id:
            lines.append(f"  howpublished = {{arXiv preprint}},")
            lines.append(f"  note = {{arXiv:{arxiv_id}}},")
        if url:
            lines.append(f"  url = {{{url}}},")

    lines.append("}")
    return "\n".join(lines)


def main():
    included_keys = []
    seen_arxiv: set[str] = set()

    for cf in sorted(PAPERS_DIR.glob("*_classification.md")):
        text = cf.read_text(encoding="utf-8")
        if "**Included:** Yes" not in text:
            continue
        key = cf.stem.replace("_classification", "")
        meta_path = PAPERS_DIR / f"{key}_metadata.json"
        if not meta_path.exists():
            continue
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        aid = meta.get("arxiv_id", "")
        if aid and aid in seen_arxiv:
            logger.warning(f"Duplicate arXiv ID {aid} for key {key} — skipping")
            continue
        if aid:
            seen_arxiv.add(aid)
        included_keys.append((key, meta))

    logger.info(f"Generating BibTeX for {len(included_keys)} papers")

    entries = []
    failed = []
    for key, meta in included_keys:
        try:
            entries.append(make_entry(key, meta))
        except Exception as e:
            logger.error(f"BibTeX failed for {key}: {e}")
            failed.append(key)

    header = (
        "% BibTeX references — Urban BEV Fast-Charging Infrastructure Planning\n"
        "% Systematic literature review\n"
        f"% Generated: {date.today().isoformat()}\n"
        "% Encoding: utf-8\n\n"
    )
    BIB_PATH.write_text(header + "\n\n".join(entries) + "\n", encoding="utf-8")

    logger.info(f"BibTeX written: {BIB_PATH} ({len(entries)} entries, {len(failed)} failed)")
    print(f"[OK] BibTeX: {len(entries)} entries written to {BIB_PATH}")
    if failed:
        print(f"  Failed: {failed}")


if __name__ == "__main__":
    main()
