# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

Systematic review research automation framework for PhD research on urban BEV (Battery Electric Vehicle) fast-charging rollout planning — covering mobility-aligned zoning, meso-level planning, equity-utilization optimization, phased deployment, and meso-micro planning integration.

## Python Environment

All Python operations use the virtual environment at `.venv\Scripts\python.exe` (absolute: `E:\qualification_exam\research_project\.venv\Scripts\python.exe`).

```
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Common Commands

```bash
# Single paper: ingest → classify → summarize
.venv\Scripts\python.exe workflows\ingest_paper.py --source <arXiv-ID|DOI|PDF-path|URL>
.venv\Scripts\python.exe workflows\classify_paper.py --key <paper_key>
.venv\Scripts\python.exe workflows\generate_summary.py --key <paper_key>

# Rebuild literature matrix from all classified papers
.venv\Scripts\python.exe workflows\update_matrix.py

# Generate Related Work section from matrix
.venv\Scripts\python.exe workflows\build_related_work.py [--output <path>]

# Batch search arXiv and ingest papers (rate-limited, 1s between requests)
.venv\Scripts\python.exe workflows\batch_search.py [--max <N>]
```

## Architecture

### Data Flow

```
External source (arXiv / DOI / PDF / URL)
    ↓ ingest_paper.py
memory/papers/<key>_metadata.json
memory/papers/<key>.pdf
    ↓ classify_paper.py
memory/papers/<key>_classification.md
    ↓ generate_summary.py  (skips if excluded)
memory/papers/<key>_summary.md
    ↓ update_matrix.py
memory/literature_matrix.md            ← primary data store
    ↓ build_related_work.py
memory/related_work.md
```

### Paper Key Format

Keys are generated as `<first_two_words_of_title>_<year>` (lowercase, unsafe chars replaced with `_`). Example: `urban_ev_2023`. The `memory/papers/` directory holds all per-paper files named with this key.

### Dissertation Gap Framework

All classification and extraction aligns papers to five gaps:

| Gap | Label | Description |
|-----|-------|-------------|
| 1 | Misaligned spatial units | Administrative zoning doesn't represent corridor mobility |
| 2 | Lack of zoning impact analysis | Few studies compare zoning schemas systematically |
| 3 | Equity and utilization separation | Most studies optimize one but not both |
| 4 | Static optimization dominance | Phased rollout sequencing is ignored |
| 5 | Missing meso-micro integration | No bridge from urban rollout to site implementation |

### Agents (`agents/`)

Markdown system prompts defining Claude agent roles. Each agent is invoked by giving Claude the file contents as its role context. Agents write outputs to `memory/` files.

| Agent | Role |
|-------|------|
| `paper_classifier.md` | Inclusion/exclusion decisions; maps to gap categories |
| `literature_reviewer.md` | Reads and summarizes papers |
| `gap_analyzer.md` | Identifies gaps from reviewed literature |
| `methodology_builder.md` | Designs review methodology |
| `proposal_writer.md` | Synthesizes findings into proposals |
| `citation_manager.md` | Manages BibTeX references |

### Skills (`skills/systematic_review/`)

- `SKILL.md` — PRISMA-compliant 5-stage pipeline (Ingest → Classify → Extract → Map → Synthesize)
- `extraction_schema.yaml` — Full extraction schema covering problem, methodology, spatial dimensions, demand, optimization, equity, utilization, rollout, zoning, meso-micro bridge, quality, and gap mapping
- `prisma_template.md` — PRISMA 2020 flowchart and protocol template

### Classify Logic

`classify_paper.py` uses keyword matching on title + abstract. In production use, the `paper_classifier.md` agent applies LLM reasoning. The script's keyword lists are the canonical inclusion/exclusion criteria — update them when the review protocol changes.

### Batch Search

`batch_search.py` runs 10 arXiv queries targeting the five gap themes, deduplicates by arXiv ID, and calls `ingest_paper.ingest()` directly. Failed ingests are logged to `memory/failed_ingests.json`; successful ones to `memory/ingested_papers.json`.

## Writing Style

Academic, concise, evidence-based, synthesis-oriented. Avoid first-person. Prioritize clarity and precision.
