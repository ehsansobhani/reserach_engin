---
name: systematic-review
description: Conduct a PRISMA-compliant systematic literature review for urban BEV fast-charging rollout planning research.
---

# Systematic Review Skill

You are conducting a systematic literature review for a PhD dissertation on **urban BEV fast-charging rollout planning**. Your work follows PRISMA 2020 guidelines and maintains structured, reproducible methodology.

## Core Workflow

Every paper goes through a 5-stage pipeline:

```
1. INGEST   → Acquire paper (arXiv ID, PDF, URL)
2. CLASSIFY → Apply inclusion/exclusion criteria
3. EXTRACT  → Populate extraction schema fields
4. MAP      → Assign to dissertation gap categories
5. SYNTHESIZE → Update literature matrix and gap analysis
```

## Stage Descriptions

### 1. Ingest

Receive a paper identifier (arXiv ID, DOI, PDF path, or URL). Use `workflows/ingest_paper.py`:
```
.venv\Scripts\python.exe workflows\ingest_paper.py --source <identifier>
```

The script downloads the paper, extracts metadata (title, authors, year, abstract), and creates:
- `memory/papers/<key>.pdf` (if PDF downloaded)
- `memory/papers/<key>_metadata.json` (metadata)

### 2. Classify

Apply inclusion/exclusion criteria from `agents/paper_classifier.md`. Output a classification file:
- `memory/papers/<key>_classification.md`

If excluded, write reason and stop. If included, proceed to extraction.

### 3. Extract

Read the paper content (PDF or abstract) and populate the extraction schema (see `skills/systematic_review/extraction_schema.yaml`). Write to:
- `memory/papers/<key>_extraction.md`

### 4. Map

Assign the paper to one or more dissertation gaps from `memory/research_gaps.md`:
- Gap 1: Misaligned spatial units
- Gap 2: Lack of zoning impact analysis
- Gap 3: Equity and utilization separation
- Gap 4: Static optimization dominance
- Gap 5: Missing meso-micro integration

### 5. Synthesize

Run `workflows/update_matrix.py` to update the literature matrix:
```
.venv\Scripts\python.exe workflows\update_matrix.py
```

Then run `workflows/generate_summary.py` to produce the markdown summary.

## PRISMA Compliance

Follow the PRISMA 2020 protocol defined in `skills/systematic_review/prisma_template.md`. Key requirements:
- Document every decision at each pipeline stage
- Record exclusion reasons precisely
- Maintain flow diagram data (counts at each stage)
- Do not skip stages — every included paper must complete all 5 stages

## Quality Standards

- Extraction must be based on direct paper evidence, not inference
- Every mapped gap must cite a specific finding from the paper
- Classification decisions must reference explicit inclusion/exclusion criteria
- All dates, counts, and decisions logged with timestamps

## Output Files

All outputs written to `memory/papers/`:
- `<key>_metadata.json` — raw metadata
- `<key>_classification.md` — inclusion decision
- `<key>_extraction.md` — structured data extraction
- `<key>_summary.md` — narrative summary

Where `<key>` = `firstauthor_year` (e.g., `chen_2023`).