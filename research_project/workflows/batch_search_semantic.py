"""
batch_search_semantic.py — Ingest up to 100 new papers via OpenAlex API.

OpenAlex is a free, open scholarly database indexing papers from Scopus,
Web of Science, PubMed, Google Scholar, and arXiv. No API key required.
Rate limit: 10 req/s (polite pool with email in User-Agent).

Usage:
    .venv\Scripts\python.exe workflows\batch_search_semantic.py [--max 100] [--year 2020]

Reads:  memory/ingested_papers.json, memory/failed_ingests.json, memory/papers/*_metadata.json
Writes: memory/papers/<key>_metadata.json  (via ingest_paper.ingest)
        memory/ingested_papers.json  (appended, never overwrites)
        memory/failed_ingests.json   (appended, never overwrites)
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path

import requests

PROJECT_ROOT  = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from loguru import logger
import workflows.ingest_paper as ingest_module

PAPERS_DIR    = PROJECT_ROOT / "memory" / "papers"
INGESTED_PATH = PROJECT_ROOT / "memory" / "ingested_papers.json"
FAILED_PATH   = PROJECT_ROOT / "memory" / "failed_ingests.json"

# OpenAlex — free, generous rate limits, covers Scopus + WoS + GS + arXiv
OPENALEX_URL  = "https://api.openalex.org/works"
# Polite pool: include email in User-Agent for higher rate limits
OA_HEADERS    = {
    "User-Agent": "BEV-ChargingResearch/1.0 (phd-research; mailto:e.sobhani2000@gmail.com)"
}

# Mandatory keywords: title MUST contain at least one from each group to be relevant
# Group A: vehicle type / energy
_TITLE_TERMS_A = {
    "electric vehicle", "ev charging", "bev", "plug-in", "evcs",
    "charging station", "charging infrastructure", "charging network",
    "fast charg", "dc fast", "level 2 charg",
}
# Group B: planning / spatial dimension
_TITLE_TERMS_B = {
    "locat", "siting", "placement", "planning", "deploy", "rollout",
    "spatial", "optimal", "optimiz", "equity", "access", "utiliz",
    "zoning", "land use", "infrastructure", "network", "station",
}

def _is_relevant(title: str) -> bool:
    """Return True only if title contains EV/charging AND a planning-related term."""
    t = title.lower()
    has_a = any(k in t for k in _TITLE_TERMS_A)
    has_b = any(k in t for k in _TITLE_TERMS_B)
    return has_a and has_b

# ---------------------------------------------------------------------------
# Search queries — OpenAlex uses full-text search across title+abstract
# ---------------------------------------------------------------------------
QUERIES = [
    # Gap 1 — spatial unit / placement optimization
    "electric vehicle charging station location optimization urban",
    "EV charging infrastructure spatial optimization GIS city",
    "battery electric vehicle charging station placement demand corridor",
    "EV charging station siting traffic analysis zone spatial",
    "electric vehicle charging network design urban optimization",

    # Gap 2 — zoning and land use
    "electric vehicle charging zoning ordinance land use regulation",
    "EV charging station land use compatibility mixed use zoning",
    "charging station municipal permitting zoning urban policy",
    "EV charging infrastructure land use planning regulatory",

    # Gap 3 — equity and utilization
    "electric vehicle charging equity accessibility underserved communities",
    "EV charging infrastructure equity low income environmental justice",
    "electric vehicle charging station utilization efficiency optimization",
    "EV charging equity multi-objective optimization coverage",
    "public EV charging station equity socioeconomic disparities",

    # Gap 4 — phased / sequential deployment
    "electric vehicle charging infrastructure phased deployment rollout",
    "EV charging station multi-stage sequential planning budget",
    "electric vehicle charging network expansion stochastic planning temporal",
    "EV charging investment planning phase optimization demand uncertainty",

    # Gap 5 — meso / micro / multi-scale
    "electric vehicle charging multi-scale planning district site level",
    "EV charging infrastructure hierarchical planning district implementation",
    "electric vehicle charging station site selection urban district",
]


# ---------------------------------------------------------------------------
# Deduplication
# ---------------------------------------------------------------------------

def _strip_version(aid: str) -> str:
    return re.sub(r"v\d+$", "", (aid or "").strip())


def _load_existing() -> tuple[set[str], set[str], set[str]]:
    """Return (arxiv_ids, dois, title_prefixes) already in the corpus."""
    arxiv_ids: set[str] = set()
    dois:      set[str] = set()
    titles:    set[str] = set()

    for path in (INGESTED_PATH, FAILED_PATH):
        if path.exists():
            for entry in json.loads(path.read_text(encoding="utf-8")):
                raw = entry[0] if isinstance(entry, list) else entry.get("id", "")
                if raw:
                    arxiv_ids.add(_strip_version(raw))

    for meta_path in PAPERS_DIR.glob("*_metadata.json"):
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            aid = meta.get("arxiv_id", "")
            if aid:
                arxiv_ids.add(_strip_version(aid))
            doi = meta.get("doi", "")
            if doi:
                dois.add(doi.lower().strip())
            t = meta.get("title", "")
            if t:
                titles.add(t.lower().strip()[:80])
        except Exception:
            pass

    logger.info(f"Existing corpus: {len(arxiv_ids)} arXiv IDs | {len(dois)} DOIs | {len(titles)} titles")
    return arxiv_ids, dois, titles


def _is_duplicate(paper: dict, arxiv_ids: set, dois: set, titles: set) -> bool:
    doi = (paper.get("doi") or "").lower().strip()
    if doi and doi in dois:
        return True

    # OpenAlex stores arXiv IDs in ids.arxiv
    ids   = paper.get("ids") or {}
    aid   = ids.get("arxiv", "")
    if not aid:
        # sometimes in locations
        for loc in paper.get("locations") or []:
            src = (loc.get("source") or {})
            if "arxiv" in (src.get("id") or "").lower():
                url = loc.get("landing_page_url") or ""
                m   = re.search(r"arxiv\.org/abs/([^\s/]+)", url)
                if m:
                    aid = m.group(1)
                    break
    if aid and _strip_version(aid) in arxiv_ids:
        return True

    t = ((paper.get("title") or "")).lower().strip()[:80]
    if t and t in titles:
        return True

    return False


# ---------------------------------------------------------------------------
# OpenAlex query
# ---------------------------------------------------------------------------

def _oa_search(query: str, year_from: int, page: int = 1, per_page: int = 100) -> list[dict]:
    """Query OpenAlex works endpoint with EV concept filter."""
    # C543663470 = "Electric vehicle" concept in OpenAlex
    # C2778905547 = "Charging station" concept
    # Using title_and_abstract.search instead of 'search' to match within paper text
    params = {
        "filter":   (
            f"title_and_abstract.search:{query},"
            f"publication_year:>{year_from - 1},"
            f"type:article|preprint"
        ),
        "sort":     "cited_by_count:desc",
        "per_page": per_page,
        "page":     page,
        "select":   "id,doi,title,authorships,publication_year,abstract_inverted_index,"
                    "primary_location,ids,open_access,cited_by_count",
    }
    try:
        resp = requests.get(OPENALEX_URL, params=params, headers=OA_HEADERS, timeout=30)
        if resp.status_code == 429:
            logger.warning("OpenAlex rate limit — sleeping 15 s")
            time.sleep(15)
            return []
        resp.raise_for_status()
        return resp.json().get("results", [])
    except Exception as e:
        logger.warning(f"OpenAlex query failed: {e}")
        return []


def _reconstruct_abstract(inverted: dict | None) -> str:
    """Reconstruct abstract from OpenAlex inverted index format."""
    if not inverted:
        return ""
    positions: list[tuple[int, str]] = []
    for word, pos_list in inverted.items():
        for p in pos_list:
            positions.append((p, word))
    positions.sort()
    return " ".join(w for _, w in positions)


def _extract_ids(paper: dict) -> tuple[str, str]:
    """Return (doi, arxiv_id) from OpenAlex work record."""
    doi = (paper.get("doi") or "").replace("https://doi.org/", "").strip()

    # ArXiv ID from ids dict
    ids = paper.get("ids") or {}
    aid = (ids.get("arxiv") or "").replace("https://arxiv.org/abs/", "").strip()

    # Also check open_access PDF URL
    if not aid:
        oa = paper.get("open_access") or {}
        url = oa.get("oa_url") or ""
        m   = re.search(r"arxiv\.org/(?:abs|pdf)/([^\s/?]+)", url)
        if m:
            aid = m.group(1)

    return doi, _strip_version(aid)


# ---------------------------------------------------------------------------
# Ingest one paper
# ---------------------------------------------------------------------------

def _ingest_paper(doi: str, arxiv_id: str, title: str) -> tuple[bool, str]:
    """Try DOI first (Scopus/journal), fall back to arXiv."""
    if doi:
        try:
            key = ingest_module.ingest(doi)
            return True, key
        except Exception as e:
            logger.debug(f"DOI ingest failed ({doi}): {e}")

    if arxiv_id:
        try:
            key = ingest_module.ingest(arxiv_id)
            return True, key
        except Exception as e:
            logger.debug(f"arXiv ingest failed ({arxiv_id}): {e}")

    return False, ""


# ---------------------------------------------------------------------------
# Append-safe JSON writers
# ---------------------------------------------------------------------------

def _append_json(path: Path, entries: list) -> None:
    existing = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    path.write_text(
        json.dumps(existing + entries, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Ingest new papers via OpenAlex")
    parser.add_argument("--max",  type=int, default=100, help="Max new papers to ingest")
    parser.add_argument("--year", type=int, default=2020, help="Minimum publication year")
    args = parser.parse_args()

    arxiv_ids, dois, titles = _load_existing()

    # Collect candidates across all queries (deduplicated by OpenAlex ID)
    candidates: list[dict]  = []
    seen_oa_ids: set[str]   = set()

    print(f"[INFO] Querying OpenAlex ({len(QUERIES)} queries, year >= {args.year}) ...")

    for q_idx, query in enumerate(QUERIES):
        if len(candidates) >= args.max * 4:
            break
        results = _oa_search(query, args.year)
        new_in_q = 0
        for paper in results:
            oa_id = paper.get("id", "")
            if oa_id in seen_oa_ids:
                continue
            seen_oa_ids.add(oa_id)

            year = paper.get("publication_year") or 0
            if year < args.year:
                continue

            title = paper.get("title") or ""
            if not _is_relevant(title):
                continue  # off-topic — reject before dedup check

            doi, aid = _extract_ids(paper)
            if not doi and not aid:
                continue  # no ingest path

            if _is_duplicate(paper, arxiv_ids, dois, titles):
                continue

            candidates.append(paper)
            new_in_q += 1

        print(f"  Query {q_idx+1:2d}/{len(QUERIES)}: \"{query[:52]}\" -> {new_in_q} new")
        time.sleep(0.5)  # polite pool allows 10 req/s

    print(f"\n[INFO] {len(candidates)} unique new candidates. Ingesting up to {args.max} ...")

    ingested: list = []
    failed:   list = []

    for paper in candidates[:args.max]:
        title  = paper.get("title") or "Unknown"
        year   = paper.get("publication_year") or 0
        doi, aid = _extract_ids(paper)

        # Reconstruct venue
        ploc   = paper.get("primary_location") or {}
        src    = ploc.get("source") or {}
        venue  = src.get("display_name") or "Unknown"

        source_tag = "Scopus/journal" if doi and not aid else ("arXiv" if aid else "unknown")
        print(f"  [{source_tag}] ({year}) {title[:62]}")

        ok, key = _ingest_paper(doi, aid, title)
        if ok:
            record_id = doi or aid
            ingested.append([record_id, key, title])
            if aid:
                arxiv_ids.add(aid)
            if doi:
                dois.add(doi.lower().strip())
            titles.add(title.lower().strip()[:80])
            print(f"    [OK] -> {key}")
        else:
            failed.append([doi or aid or "", title, year, venue])
            print(f"    [FAIL] no valid ingest path")

        time.sleep(1)

    _append_json(INGESTED_PATH, ingested)
    _append_json(FAILED_PATH,   failed)

    print(f"\n{'='*60}")
    print(f"[DONE]  New papers ingested : {len(ingested)}")
    print(f"        Failed              : {len(failed)}")
    print(f"        Source              : OpenAlex (Scopus + WoS + Google Scholar + arXiv)")
    print(f"        Papers directory    : {PAPERS_DIR}")


if __name__ == "__main__":
    main()
