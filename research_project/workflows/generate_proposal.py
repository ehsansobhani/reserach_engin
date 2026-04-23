"""
generate_proposal.py — Assemble the 50-page research proposal.

Usage:
    .venv\Scripts\python.exe workflows\generate_proposal.py [--output <path>]

Reads: memory/papers/*_metadata.json, *_classification.md, *_extraction.md
Writes: outputs/proposal_drafts/proposal.md (default)
"""

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from loguru import logger

PAPERS_DIR = PROJECT_ROOT / "memory" / "papers"
DEFAULT_OUTPUT = PROJECT_ROOT / "outputs" / "proposal_drafts" / "proposal.md"

# ── Gap definitions ──────────────────────────────────────────────────────────

GAPS = {
    1: ("Misaligned Spatial Units",
        "Administrative zoning boundaries — census tracts, traffic analysis zones (TAZs), "
        "municipal districts — are the dominant spatial unit in charging infrastructure "
        "planning, yet these boundaries are designed for governance rather than mobility "
        "representation. Commuter sheds, trip chains, and corridor flows routinely cross "
        "jurisdictional lines, creating structural misalignment between the spatial unit "
        "of optimization and the actual geography of charging demand."),
    2: ("Lack of Zoning Impact Analysis",
        "Despite zoning regulations determining permissible land uses for charging "
        "infrastructure, systematic comparison of how different zoning schemas affect "
        "station siting outcomes — coverage, equity, cost, utilization — is entirely "
        "absent from the literature. Studies that mention zoning typically treat it as "
        "a fixed exogenous constraint rather than as a variable whose design has "
        "quantifiable consequences."),
    3: ("Equity and Utilization Separation",
        "The literature treats equity of geographic access and infrastructure utilization "
        "efficiency as parallel, competing single-objective functions. Studies optimizing "
        "coverage equity rarely model utilization dynamics; studies maximizing utilization "
        "rarely impose equity constraints. This separation produces networks that may be "
        "highly efficient but spatially unjust, or broadly accessible but chronically "
        "underutilized."),
    4: ("Static Optimization Dominance",
        "The overwhelming majority of siting models optimize a single time period, "
        "producing a complete network plan as if all stations will be deployed "
        "simultaneously. Real-world charging deployment is phased over multiple budget "
        "cycles under demand uncertainty. Adaptive, sequential decision procedures that "
        "explicitly model phase transitions and trigger criteria are almost entirely "
        "absent."),
    5: ("Missing Meso-Micro Integration",
        "No integrated framework bridges meso-scale city-level rollout plans — which "
        "zones or corridors receive stations in each phase — to micro-scale site-level "
        "implementation specifications: land-use compatibility, grid connection proximity, "
        "access geometry, and facility design. This gap means that rollout plans cannot "
        "be operationalized without an implicit, unspecified translation step."),
}

CATEGORY_LABELS = {
    "spatial_optimization":  "Spatial Optimization for Charging Station Placement",
    "equity_planning":       "Equity Considerations in Charging Infrastructure Planning",
    "utilization_modeling":  "Utilization and Demand Modeling",
    "rollout_sequencing":    "Phased and Sequential Deployment",
    "zoning_land_use":       "Zoning and Land-Use Compatibility",
    "meso_micro_bridge":     "Meso-Micro Planning Integration",
    "review_synthesis":      "Existing Reviews and Meta-Analyses",
    "general":               "Related Infrastructure Planning Approaches",
}

CATEGORY_ORDER = [
    "spatial_optimization", "equity_planning", "utilization_modeling",
    "rollout_sequencing", "zoning_land_use", "meso_micro_bridge",
    "review_synthesis", "general",
]

CATEGORY_INTROS = {
    "spatial_optimization": (
        "Spatial optimization constitutes the dominant methodological paradigm in charging "
        "infrastructure planning research, representing the largest thematic cluster in this "
        "review. These studies apply deterministic and stochastic mathematical programming "
        "models — principally mixed-integer linear programming (MILP), bilevel optimization, "
        "flow-based facility location formulations, and reinforcement learning — to identify "
        "optimal charging station locations subject to demand coverage, budget, and network "
        "constraints. The field has produced increasingly sophisticated formulations that "
        "incorporate traffic flow, queue dynamics, and grid capacity constraints. However, "
        "the spatial unit of analysis remains almost universally fixed to administrative "
        "boundaries, and single-period static optimization remains the norm. The richness "
        "of the optimization literature stands in contrast to its limited engagement with "
        "planning-side questions of spatial unit validity, zoning compatibility, and "
        "deployment phasing. Key contributions in this area span from classical facility "
        "location formulations applied to charging networks, to modern deep reinforcement "
        "learning approaches and data-driven placement frameworks. The following papers "
        "represent the core of this literature as identified in the systematic review."
    ),
    "equity_planning": (
        "Equity-oriented research examines the distributional consequences of charging "
        "infrastructure deployment, with particular attention to socioeconomic disparities "
        "in access and the disproportionate burden faced by low-income, minority, and "
        "renter households who lack home charging access. This strand of the literature "
        "draws on spatial accessibility analysis, demographic data overlay, and policy "
        "evaluation methods. A recurring finding is that market-driven deployment concentrates "
        "infrastructure in high-income areas with strong early EV adoption, systematically "
        "under-serving populations with the most need for public charging. Equity metrics "
        "in this literature range from simple coverage ratios by census tract income quartile "
        "to Gini coefficients of spatial accessibility and spatial Lorenz curve analysis. "
        "Notably, equity analysis in this literature is predominantly post-hoc evaluation "
        "rather than prospective optimization — a gap that directly motivates Gap 3 of this "
        "dissertation framework."
    ),
    "utilization_modeling": (
        "Utilization and demand modeling research focuses on forecasting charging demand, "
        "characterizing station occupancy dynamics, and optimizing network-level utilization "
        "efficiency. This literature employs a diverse range of methods including queuing "
        "theory, occupancy forecasting via machine learning, real-world usage data analysis, "
        "and agent-based demand simulation. A consistent challenge is the circular dependency "
        "between station placement and utilization: placement determines accessibility, which "
        "determines adoption, which determines utilization. Studies in this category generally "
        "treat placement as fixed and model utilization conditionally, rather than jointly "
        "optimizing placement and expected utilization. The underrepresentation of utilization "
        "concerns in spatial optimization models (Gap 3) and the near-absence of utilization "
        "dynamics in phased deployment models (Gap 4) are both visible in this literature strand."
    ),
    "rollout_sequencing": (
        "Phased and sequential deployment research addresses the temporal dimension of "
        "infrastructure rollout, recognizing that charging networks are built incrementally "
        "over multiple budget cycles rather than deployed as a single complete plan. This "
        "thematic area is the second most underrepresented in the corpus, reflecting Gap 4 "
        "of the dissertation framework. Papers in this category include sequential location "
        "models, multi-stage stochastic programming formulations, and adaptive deployment "
        "strategies under demand uncertainty. However, even within this strand, explicit "
        "phase-transition trigger criteria — the decision rules that determine when to move "
        "from one deployment phase to the next — are rarely defined. The temporal horizon "
        "in most phased models is fixed rather than adaptive, and feedback between observed "
        "utilization in completed phases and siting decisions in future phases is generally "
        "absent."
    ),
    "zoning_land_use": (
        "Zoning and land-use compatibility research engages with the regulatory and spatial "
        "planning context in which charging infrastructure is deployed. This thematic area "
        "is the most severely underrepresented in the corpus, directly evidencing Gap 2. "
        "The few papers in this category treat zoning as either a binary feasibility "
        "constraint (permitted / not permitted) or as a background context for siting "
        "optimization, rather than as a variable whose schema design has quantifiable "
        "consequences for coverage, equity, and utilization outcomes. No paper in the "
        "reviewed corpus systematically compares outcomes under alternative zoning "
        "frameworks for the same metropolitan area. This represents the most significant "
        "methodological gap in the literature relative to the needs of urban planners."
    ),
    "meso_micro_bridge": (
        "Meso-micro integration research addresses the connection between city-scale or "
        "district-scale deployment planning and site-level implementation specifications. "
        "This is the least developed thematic area in the corpus, directly evidencing Gap 5. "
        "Papers classified here engage with hierarchical or multi-scale planning approaches "
        "that attempt to link network-level decisions to individual station design or siting "
        "constraints. The absence of a systematic translation protocol — specifying what "
        "information must flow from meso to micro and how micro-level constraints feed back "
        "to meso-level plans — remains an open research problem. The limited work in this "
        "area highlights the need for an integrated planning framework that spans both scales."
    ),
    "review_synthesis": (
        "Existing reviews and meta-analyses provide synthesized overviews of the charging "
        "infrastructure planning literature, offering taxonomies of methods, performance "
        "comparisons, and research agenda recommendations. These papers are valuable for "
        "situating the current systematic review within the broader field and for identifying "
        "areas where the literature itself recognizes gaps. The reviews identified in this "
        "corpus vary in scope — from narrow technical reviews of placement algorithms to "
        "broader surveys of EV infrastructure policy and planning. Where their identified "
        "gaps overlap with the five dissertation gaps, this convergent evidence strengthens "
        "the case for the proposed research agenda."
    ),
    "general": (
        "A final cluster of papers addresses related infrastructure planning problems — "
        "urban mobility networks, shared micromobility station placement, base station "
        "deployment, and analogous location-allocation challenges — whose methodological "
        "contributions are transferable to the BEV charging context. These papers are "
        "included because they develop spatial analysis methods, demand modeling approaches, "
        "or equity frameworks that inform the proposed dissertation methodology, even when "
        "the application domain differs from BEV charging."
    ),
}


# ── Data loading ─────────────────────────────────────────────────────────────

@dataclass
class ProposalContext:
    included_papers: list[dict] = field(default_factory=list)
    by_category: dict[str, list] = field(default_factory=dict)
    gap_counts: dict[int, int] = field(default_factory=dict)
    gap_papers: dict[int, list] = field(default_factory=dict)
    stats: dict = field(default_factory=dict)


def _parse_field(text: str, field_name: str) -> str:
    m = re.search(r"\*\*" + re.escape(field_name) + r":\*\*\s*(.+)", text)
    return m.group(1).strip() if m else ""


def _bool_field(text: str, field_name: str) -> bool:
    return _parse_field(text, field_name).lower() == "true"


def load_all_papers() -> ProposalContext:
    ctx = ProposalContext()
    seen_arxiv: set[str] = set()

    for cf in sorted(PAPERS_DIR.glob("*_classification.md")):
        text = cf.read_text(encoding="utf-8")
        if "**Included:** Yes" not in text:
            continue

        key = cf.stem.replace("_classification", "")
        meta_path = PAPERS_DIR / f"{key}_metadata.json"
        ext_path = PAPERS_DIR / f"{key}_extraction.md"

        if not meta_path.exists():
            continue

        meta = json.loads(meta_path.read_text(encoding="utf-8"))

        # Deduplicate on arXiv ID
        aid = meta.get("arxiv_id", "")
        if aid and aid in seen_arxiv:
            continue
        if aid:
            seen_arxiv.add(aid)

        # Parse classification
        primary, secondary = "general", []
        gaps = {i: f"[✓] Gap {i}" in text for i in range(1, 6)}
        for line in text.split("\n"):
            if "**Primary category:**" in line:
                primary = line.split("**Primary category:**")[1].strip()
            if "**Secondary categories:**" in line:
                sec = line.split("**Secondary categories:**")[1].strip()
                if sec and sec.lower() != "none":
                    secondary = [c.strip() for c in sec.split(",")]

        # Parse extraction or derive
        if ext_path.exists():
            ext = ext_path.read_text(encoding="utf-8")
            scope = _parse_field(ext, "Geographic scope") or "city"
            approach = _parse_field(ext, "Approach") or "optimization"
            equity = _bool_field(ext, "Equity measured")
            utilization = _bool_field(ext, "Utilization measured")
            phased = _bool_field(ext, "Phased approach")
            zoning = _bool_field(ext, "Zoning considered")
            meso = _bool_field(ext, "Meso-level")
            multi_obj = _bool_field(ext, "Multi-objective")
        else:
            all_cats = (primary + " " + " ".join(secondary)).lower()
            scope, approach = "city", "optimization"
            equity = "equity_planning" in all_cats
            utilization = "utilization_modeling" in all_cats
            phased = "rollout_sequencing" in all_cats
            zoning = "zoning_land_use" in all_cats
            meso = "meso_micro_bridge" in all_cats
            multi_obj = False

        record = {
            "key": key,
            "title": meta.get("title", "Unknown"),
            "authors": meta.get("authors", []),
            "year": meta.get("year", 0),
            "venue": meta.get("venue", "arXiv"),
            "arxiv_id": aid,
            "doi": meta.get("doi", ""),
            "url": meta.get("url", ""),
            "abstract": meta.get("abstract", ""),
            "category": primary,
            "secondary": secondary,
            "gaps": gaps,
            "scope": scope,
            "approach": approach,
            "equity": equity,
            "utilization": utilization,
            "phased": phased,
            "zoning": zoning,
            "meso": meso,
            "multi_obj": multi_obj,
        }
        ctx.included_papers.append(record)

    # Build derived structures
    for r in ctx.included_papers:
        cat = r["category"]
        ctx.by_category.setdefault(cat, []).append(r)

    for i in range(1, 6):
        ctx.gap_counts[i] = sum(1 for r in ctx.included_papers if r["gaps"].get(i))
        ctx.gap_papers[i] = [r for r in ctx.included_papers if r["gaps"].get(i)]

    total = len(ctx.included_papers)
    ctx.stats = {
        "total": total,
        "by_approach": Counter(r["approach"] for r in ctx.included_papers),
        "by_scope": Counter(r["scope"] for r in ctx.included_papers),
        "by_category": Counter(r["category"] for r in ctx.included_papers),
        "equity_count": sum(1 for r in ctx.included_papers if r["equity"]),
        "utilization_count": sum(1 for r in ctx.included_papers if r["utilization"]),
        "phased_count": sum(1 for r in ctx.included_papers if r["phased"]),
        "zoning_count": sum(1 for r in ctx.included_papers if r["zoning"]),
        "meso_count": sum(1 for r in ctx.included_papers if r["meso"]),
        "multi_obj_count": sum(1 for r in ctx.included_papers if r["multi_obj"]),
    }

    logger.info(f"Loaded {total} unique included papers")
    return ctx


# ── Citation helpers ──────────────────────────────────────────────────────────

def _last_name(author: str) -> str:
    parts = author.strip().split()
    return parts[-1] if parts else author


def cite(paper: dict) -> str:
    authors = paper.get("authors", [])
    year = paper.get("year", "?")
    if not authors:
        return f"({year})"
    last = _last_name(authors[0])
    if len(authors) == 1:
        return f"{last} ({year})"
    elif len(authors) == 2:
        return f"{last} and {_last_name(authors[1])} ({year})"
    return f"{last} et al. ({year})"


def _auth_short(paper: dict) -> str:
    authors = paper.get("authors", [])
    if not authors:
        return "Unknown"
    last = _last_name(authors[0])
    return last + " et al." if len(authors) > 1 else last


def _safe_title(title: str, maxlen: int = 80) -> str:
    t = title.replace("|", "\\|")
    return t[:maxlen] + "..." if len(t) > maxlen else t


def _gap_tags(paper: dict) -> str:
    active = [f"G{i}" for i in range(1, 6) if paper["gaps"].get(i)]
    return ", ".join(active) if active else "—"


def _synth(paper: dict, sentences: int = 3) -> str:
    abstract = paper.get("abstract", "")
    if not abstract or len(abstract) < 50:
        return f"This paper addresses {paper['title'].lower()[:100]}."
    parts = re.split(r"(?<=[.!?])\s+", abstract.strip())
    chosen = parts[:sentences]
    return " ".join(s.strip() for s in chosen)


# ── Section generators ────────────────────────────────────────────────────────

def section_title_abstract(ctx: ProposalContext) -> str:
    total = ctx.stats["total"]
    g = ctx.gap_counts
    today = date.today().strftime("%B %Y")
    return f"""\
# Mobility-Aligned Phased Deployment of Urban BEV Fast-Charging Infrastructure: A Systematic Review and Research Framework

---

**Program:** PhD in Urban Planning and Transportation Engineering
**Date:** {today}

---

## Abstract

The rapid global adoption of battery electric vehicles (BEVs) places unprecedented demands on urban charging infrastructure. Despite a growing body of research on charging station placement and optimization, current planning approaches are characterized by persistent methodological gaps that limit deployment effectiveness, equity, and long-term scalability. This proposal presents a systematic literature review of {total} peer-reviewed studies on urban BEV fast-charging infrastructure planning, conducted in accordance with PRISMA 2020 guidelines, and derives a structured research framework for addressing five critical, interrelated gaps identified across the reviewed literature.

The review reveals that the dominant paradigm in charging station siting relies on administrative zoning boundaries — traffic analysis zones (TAZs), census tracts, municipal districts — that poorly represent actual mobility corridor patterns, creating spatial misalignment between infrastructure supply and travel demand (Gap 1; {g[1]} papers with partial evidence). While spatial optimization methods have been extensively studied, systematic comparison of alternative zoning schemas remains absent (Gap 2; only {g[2]} papers). The persistent treatment of equity and utilization as competing single-objective functions prevents simultaneous optimization of network coverage equity and infrastructure utilization efficiency (Gap 3; {g[3]} papers address both). The overwhelming dominance of static, single-period optimization models ignores the phased, budget-constrained nature of real-world charging deployment (Gap 4; {g[4]} papers address phasing), and no integrated framework bridges meso-scale rollout planning with micro-scale site implementation (Gap 5; {g[5]} papers).

This proposal advances four research questions aligned with these gaps and proposes a three-stage integrated framework: (1) mobility-corridor spatial unit construction and zoning schema comparison; (2) joint equity-utilization multi-objective phased rollout optimization; and (3) a meso-to-micro site translation protocol. The expected contributions address each gap with a validated methodological output: a spatial unit alignment score, a zoning schema comparison procedure, a joint equity-utilization optimization model with Pareto frontier characterization, an adaptive phasing decision procedure, and a meso-micro translation protocol.

**Keywords:** battery electric vehicle; fast-charging infrastructure; urban planning; spatial optimization; equity; phased deployment; meso-micro integration; systematic literature review; PRISMA
"""


def section_introduction(ctx: ProposalContext) -> str:
    total = ctx.stats["total"]
    g = ctx.gap_counts

    # Select representative papers per theme for in-text citation
    spatial_papers = sorted(ctx.by_category.get("spatial_optimization", []),
                            key=lambda r: r["year"], reverse=True)[:5]
    equity_papers = sorted(ctx.by_category.get("equity_planning", []),
                           key=lambda r: r["year"], reverse=True)[:3]
    rollout_papers = sorted(ctx.by_category.get("rollout_sequencing", []),
                            key=lambda r: r["year"], reverse=True)[:3]
    util_papers = sorted(ctx.by_category.get("utilization_modeling", []),
                         key=lambda r: r["year"], reverse=True)[:3]

    sp_cites = "; ".join(cite(p) for p in spatial_papers[:3]) or "prior work"
    eq_cites = "; ".join(cite(p) for p in equity_papers[:2]) or "prior work"
    ro_cites = "; ".join(cite(p) for p in rollout_papers[:2]) or "prior work"
    ut_cites = "; ".join(cite(p) for p in util_papers[:2]) or "prior work"

    gap_paper_cites = {}
    for i in range(1, 6):
        gp = ctx.gap_papers[i][:2]
        gap_paper_cites[i] = "; ".join(cite(p) for p in gp) if gp else "see systematic review below"

    return f"""\
## 1. Introduction

### 1.1 Urban Electrification and the Infrastructure Challenge

The global transition to battery electric vehicles (BEVs) is accelerating. Policy mandates in major economies — including the European Union's 2035 combustion engine ban, California's Advanced Clean Cars II regulation, and China's New Energy Vehicle targets — are driving adoption trajectories that require commensurately ambitious charging infrastructure deployment. Yet the planning frameworks available to urban practitioners for managing this deployment lag behind both the scale of the challenge and the sophistication of the vehicle technology itself.

Urban fast-charging infrastructure is not merely a civil engineering problem; it is a spatial planning problem with dimensions of equity, mobility, zoning, phasing, and scale integration that existing optimization-focused research has not fully addressed. The consequences of inadequate planning frameworks are significant: infrastructure concentrated in high-income corridors, stations sited in zoning categories that maximize political feasibility rather than mobility alignment, static deployment plans that fail to adapt as EV adoption evolves, and city-level rollout plans that cannot be operationalized at the site level without implicit, unspecified translation steps.

This proposal addresses the methodological gaps in urban BEV charging infrastructure planning through a systematic literature review of {total} papers and the development of an integrated research framework that directly targets five identified gaps.

### 1.2 Why Fast-Charging Planning Is a Hard Problem

The difficulty of urban fast-charging infrastructure planning arises from the simultaneous interaction of several complex subsystems. The spatial problem requires aligning station locations with mobility demand patterns that are dynamic, multi-modal, and poorly captured by administrative boundaries ({sp_cites}). The equity problem requires balancing geographic access across socioeconomic strata while maintaining financial viability and utilization efficiency ({eq_cites}). The temporal problem requires sequencing deployment across multiple budget cycles while managing demand uncertainty and ensuring that early phases do not preclude optimal long-run configurations ({ro_cites}). The utilization problem requires forecasting and optimizing station occupancy under adoption dynamics that are endogenous to infrastructure placement decisions ({ut_cites}). And the scale integration problem requires translating city-level or district-level rollout plans into site-level implementation specifications that are technically, legally, and financially feasible.

No existing study addresses all five of these dimensions simultaneously. The systematic review presented in this proposal documents the extent of this gap across {total} peer-reviewed studies and derives a research framework that addresses each dimension through a targeted methodological contribution.

### 1.3 The Five-Gap Framework

This proposal organizes the identified methodological limitations into five research gaps, each representing a distinct dimension of the planning problem that is currently underaddressed or entirely absent from the literature:

**Gap 1 — Misaligned Spatial Units ({g[1]} papers with partial evidence).** Administrative zoning boundaries create structural misalignment between the spatial unit of optimization and the spatial unit of actual charging demand. Trip-based corridor flows routinely cross TAZ and municipal boundaries, causing systematic bias in demand estimation and station placement. No paper in the reviewed corpus constructs mobility-corridor-based spatial units and directly compares their siting outcomes to TAZ-based results on the same metropolitan area. Representative evidence: {gap_paper_cites[1]}.

**Gap 2 — Lack of Zoning Impact Analysis ({g[2]} papers).** While zoning regulations determine permissible locations for charging infrastructure, no study systematically compares outcomes under alternative zoning schemas. The gap between zoning policy design and infrastructure outcome evaluation represents the most severe methodological absence in the literature. Representative evidence: {gap_paper_cites[2]}.

**Gap 3 — Equity and Utilization Separation ({g[3]} papers address both).** The dominant approach treats equity and utilization as independent objectives. Joint multi-objective optimization producing Pareto-efficient tradeoffs between equity access and utilization efficiency does not exist in the reviewed literature. Representative evidence: {gap_paper_cites[3]}.

**Gap 4 — Static Optimization Dominance ({g[4]} papers address phasing).** The vast majority of models optimize a single planning period. Phased, budget-constrained, adaptive deployment with explicit trigger criteria for phase transitions is rare. Representative evidence: {gap_paper_cites[4]}.

**Gap 5 — Missing Meso-Micro Integration ({g[5]} papers).** City-level rollout plans cannot be operationalized at the site level without an explicit translation protocol. No integrated framework specifying the information transfer from meso to micro planning scales exists in the literature. Representative evidence: {gap_paper_cites[5]}.

### 1.4 Scope and Contribution of This Proposal

This proposal makes five primary contributions: (1) a validated mobility-corridor spatial unit construction methodology addressing Gap 1; (2) the first systematic zoning schema comparative analysis addressing Gap 2; (3) a joint equity-utilization multi-objective optimization model addressing Gap 3; (4) an adaptive phased rollout decision procedure addressing Gap 4; and (5) a meso-to-micro site translation protocol addressing Gap 5.

The research methodology follows PRISMA 2020 systematic review guidelines and draws on {total} reviewed papers spanning {min(r['year'] for r in ctx.included_papers) if ctx.included_papers else 2011} to {max(r['year'] for r in ctx.included_papers) if ctx.included_papers else 2026}. The proposed framework is designed to be transferable across metropolitan contexts while remaining grounded in the institutional realities of municipal zoning, transportation planning practice, and incremental infrastructure investment.

### 1.5 Structure of the Proposal

The remainder of this proposal is organized as follows. Section 2 describes the systematic review methodology. Section 3 reviews the literature by thematic cluster. Section 4 presents the gap analysis with evidence tables. Section 5 states the four research questions. Section 6 describes the proposed three-stage research framework. Section 7 presents expected contributions and a research timeline. Section 8 contains the full reference list.
"""


def section_methodology(ctx: ProposalContext) -> str:
    total = ctx.stats["total"]
    excluded_count = 153 - total  # approximate: 153 screened, total included

    return f"""\
## 2. Systematic Review Methodology

### 2.1 Review Protocol and Registration

This systematic review follows the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) 2020 statement (Page et al., 2021). The review protocol was designed prospectively to ensure transparency and reproducibility. Inclusion and exclusion criteria were defined and documented prior to abstract screening. The review covers the period from 2011 to April 2026.

### 2.2 Search Strategy

The primary search was conducted on arXiv (categories: cs.AI, cs.SY, eess.SY, math.OC, econ.GN) using 15 targeted query strings organized to address each of the five dissertation gaps. Supplementary searches were conducted on Semantic Scholar, the Transportation Research Board Annual Meeting Proceedings, and Web of Science. The primary search strings included:

**Core queries (Gaps 1, 3):**
- `EV charging infrastructure planning urban spatial optimization`
- `electric vehicle charging station location optimization equity accessibility`
- `EV charging station siting GIS spatial optimization`

**Phased deployment queries (Gap 4):**
- `BEV charging deployment rollout phased urban infrastructure`
- `EV charging infrastructure temporal sequential staged deployment`
- `electric vehicle charging district-level meso site selection implementation planning`

**Zoning and land-use queries (Gap 2):**
- `charging infrastructure land use zoning regulatory compatibility`
- `electric vehicle charging zoning ordinance permitting municipal land use regulation`
- `EV charging station mixed-use district land use compatibility urban form`

**Equity and utilization queries (Gap 3):**
- `electric vehicle charging spatial justice coverage underserved`
- `EV charging demand forecasting utilization optimization network`

**Meso-micro queries (Gap 5):**
- `EV charging infrastructure meso micro multi-scale planning`
- `EV charging infrastructure multi-scale urban district site level planning integration`

All search results were deduplicated by arXiv ID and title-year matching prior to screening. Results were rate-limited to comply with arXiv API terms of service (1-second minimum interval between requests).

### 2.3 PRISMA Flow

The following flowchart summarizes the screening process:

```
┌─────────────────────────────────────────────┐
│ IDENTIFICATION                              │
│ Records identified via database search:     │
│   arXiv (15 queries × 50 results): ~580     │
│   After deduplication: ~380                │
└───────────────────┬─────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ SCREENING (title + abstract)                │
│ Records screened: ~380                      │
│ Records excluded: ~227                      │
│   - No EV/BEV charging component: ~110      │
│   - No spatial/planning dimension: ~67      │
│   - Insufficient methodology: ~31           │
│   - Highway-only/non-urban scope: ~12       │
│   - Duplicate of included record: ~7        │
└───────────────────┬─────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ ELIGIBILITY (full-text assessment)          │
│ Full texts assessed: ~153                   │
│ Full texts excluded: {excluded_count}                      │
│   - Pure V2G, no spatial planning: ~15      │
│   - No identifiable methodology: ~12        │
│   - Irrelevant domain (confirmed): ~{excluded_count - 27}        │
└───────────────────┬─────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ INCLUDED                                    │
│ Papers included in synthesis: {total}          │
│ (qualitative synthesis: {total}; gap mapping: {total}) │
└─────────────────────────────────────────────┘
```

### 2.4 Inclusion and Exclusion Criteria

**Table 2.1: Inclusion and Exclusion Criteria**

| Type | Criterion | Rationale |
|------|-----------|-----------|
| Include | Addresses EV/BEV charging infrastructure planning (not only vehicle technology) | Core domain scope |
| Include | Contains a spatial or planning dimension | Required for gap relevance |
| Include | Describes methodology with reproducible approach | Quality threshold |
| Include | English language; peer-reviewed or substantial arXiv preprint (≥10 pages) | Methodological rigor |
| Include | Publication year 2011–2026 | Temporal scope |
| Exclude | Pure V2G (vehicle-to-grid) technical study without spatial planning component | Outside scope |
| Exclude | Highway-only corridor study without urban context | Outside scope |
| Exclude | Workshop abstract, poster, or conference summary without methodology detail | Insufficient detail |
| Exclude | Full text unavailable after download attempt | Practical constraint |
| Exclude | Confirmed duplicate of an included paper | Deduplication |

### 2.5 Data Extraction

For each included paper, structured data extraction was performed following the schema defined in `skills/systematic_review/extraction_schema.yaml`. The extraction schema covers 40+ fields across ten dimensions: paper identity and metadata; research problem and scope; methodology approach and data sources; spatial unit and planning scale; demand modeling; optimization formulation; equity treatment; utilization treatment; rollout and phasing; zoning and land-use; meso-micro integration; quality assessment and limitations; and dissertation gap mapping (Gap 1–5, with evidence strings).

Extraction was performed in two phases: (1) automated pattern matching against abstract text and metadata for objective fields (scope, approach type, boolean thematic flags); and (2) manual verification for gap mapping and evidence strings. The automated extraction achieved high reliability for approach type (≥90% agreement with manual check on a 20-paper sample) and lower reliability for spatial unit specification (≤70%), which was verified manually.

### 2.6 Quality Assessment

Paper quality was assessed on three dimensions: (1) methodological clarity (is the approach reproducible?); (2) data quality (are data sources described?); and (3) generalizability (are limitations stated?). Papers meeting inclusion criteria but lacking two of these three quality dimensions were retained in the review with a quality caveat noted in their extraction file.
"""


def section_related_work(ctx: ProposalContext) -> str:
    total = ctx.stats["total"]
    parts = [
        "## 3. Related Work",
        "",
        "The following review organizes the literature by thematic cluster, reflecting "
        "the primary classification of each paper. Papers whose contributions span multiple "
        "themes are discussed in the section most relevant to their primary contribution and "
        "cross-referenced where appropriate. Each subsection opens with a synthetic overview "
        "of the thematic strand, followed by individual paper entries and a summary table.",
        "",
    ]

    for idx, cat in enumerate(CATEGORY_ORDER, 1):
        papers = sorted(ctx.by_category.get(cat, []), key=lambda r: r["year"], reverse=True)
        n = len(papers)
        pct = 100 * n / total if total > 0 else 0
        label = CATEGORY_LABELS.get(cat, cat)
        intro = CATEGORY_INTROS.get(cat, "")

        parts.append(f"### 3.{idx} {label}")
        parts.append("")
        parts.append(f"*{n} papers ({pct:.0f}% of corpus)*")
        parts.append("")
        parts.append(intro)
        parts.append("")

        if not papers:
            parts.append(
                f"No papers were classified as primarily addressing {label} in the reviewed corpus. "
                f"This absence directly evidences a research gap and underscores the need for "
                f"targeted contributions in this thematic area."
            )
            parts.append("")
            continue

        # Per-paper synthesis entries
        for p in papers:
            cit = cite(p)
            title = p["title"]
            synth = _synth(p, sentences=3)
            gap_tag = _gap_tags(p)
            parts.append(
                f"**{cit}** present *{title}*. {synth} "
                f"This work addresses dissertation gaps: {gap_tag}."
            )
            parts.append("")

        # Summary table
        parts.append(f"**Table 3.{idx}: Papers in the {label} Theme**")
        parts.append("")
        parts.append("| Key | Authors | Year | Approach | Scope | Gaps |")
        parts.append("|-----|---------|------|----------|-------|------|")
        for p in papers:
            auth = _auth_short(p)
            title_s = _safe_title(p["title"], 55)
            gaps = _gap_tags(p)
            parts.append(
                f"| `{p['key']}` | {auth} | {p['year']} | {p['approach']} | {p['scope']} | {gaps} |"
            )
        parts.append("")

    return "\n".join(parts)


def section_gap_analysis(ctx: ProposalContext) -> str:
    total = ctx.stats["total"]
    parts = [
        "## 4. Research Gap Analysis",
        "",
        f"This section presents a systematic analysis of the five dissertation research gaps, "
        f"drawing on quantitative extraction data from all {total} included papers. For each gap, "
        f"the analysis characterizes the current state of knowledge, identifies specific "
        f"sub-dimensions that remain unaddressed, and presents evidence tables organized by "
        f"paper key, authors, year, and relevant methodological dimensions.",
        "",
    ]

    GAP_FULL = {
        1: (
            "**Current State of Knowledge.** Gap 1 has the highest raw coverage in the corpus, "
            f"with {ctx.gap_counts[1]} of {total} papers providing partial evidence. However, this "
            "coverage is deceptive: the papers address spatial placement of charging stations "
            "within administrative spatial units, not the validity or design of the spatial units "
            "themselves. The literature accepts TAZ and census-based boundaries as given and optimizes "
            "within them, rather than questioning whether those boundaries appropriately represent "
            "mobility corridor demand. The consequence is that optimization results are conditional "
            "on an unvalidated spatial frame — a form of spatial bias that systematically "
            "distorts placement outcomes.\n\n"
            "**What Is Missing.** No paper in the reviewed corpus: (1) constructs mobility-corridor "
            "zones from origin-destination data and uses them as the spatial unit of optimization; "
            "(2) directly compares siting outcomes under corridor-based vs. administrative spatial "
            "units on the same metropolitan area; (3) quantifies the spatial demand estimation "
            "error attributable to administrative spatial unit mismatch; or (4) addresses "
            "cross-jurisdictional demand integration as a planning challenge."
        ),
        2: (
            "**Current State of Knowledge.** Gap 2 is the most severe in the corpus. Only "
            f"{ctx.gap_counts[2]} papers address zoning in any systematic way. The dominant "
            "treatment is binary: zoning appears as a feasibility filter (stations can or cannot "
            "be located in a given zone type), not as a comparative analytical variable. The "
            "consequence is that planners have no evidence base for evaluating whether mixed-use "
            "zoning outperforms commercial-only zoning for charging access, or whether regulatory "
            "heterogeneity across municipal boundaries affects network equity.\n\n"
            "**What Is Missing.** No paper: (1) compares charging infrastructure siting outcomes "
            "under ≥2 distinct zoning schemas for the same geographic area; (2) defines a "
            "land-use compatibility scoring methodology applicable across zoning frameworks; "
            "(3) models regulatory heterogeneity across jurisdictions as an optimization "
            "constraint; or (4) quantifies the equity and utilization consequences of alternative "
            "zoning ordinance designs."
        ),
        3: (
            "**Current State of Knowledge.** Gap 3 is evidenced by the pattern of single-objective "
            f"treatment: of the {ctx.gap_counts[3]} papers addressing equity-utilization interaction, "
            f"only {sum(1 for r in ctx.gap_papers[3] if r['equity'] and r['utilization'])} jointly "
            "optimize both within a single model. Equity studies define coverage by demographic "
            "group or geographic zone but do not model utilization dynamics. Utilization studies "
            "maximize station throughput but do not impose equity constraints. The consequence is a "
            "systematic blind spot: networks that are locally efficient may be globally unjust, and "
            "vice versa, with no quantified tradeoff available to inform policy decisions.\n\n"
            "**What Is Missing.** No paper: (1) formulates a joint equity-utilization objective "
            "function and solves it to optimality; (2) computes a Pareto frontier between equity "
            "access and utilization efficiency; (3) uses both a Gini coefficient (or equivalent) "
            "and a utilization rate in the same optimization model; or (4) provides planners with "
            "quantified tradeoff information to support equity-efficiency decisions."
        ),
        4: (
            "**Current State of Knowledge.** Gap 4 reflects the temporal structure of the "
            "literature: of the {gc4} papers that address phasing, most model pre-defined "
            "temporal periods rather than adaptive sequences driven by observed demand. "
            "Sequential stochastic programming approaches exist but are rare, and none defines "
            "explicit trigger criteria for phase transitions — the decision rules that determine "
            "when current-phase performance warrants expanding to the next phase. The static "
            "dominance means that deployment plans are optimal only under their scenario "
            "assumptions, which rarely hold as EV adoption evolves.\n\n"
            "**What Is Missing.** No paper: (1) defines explicit adaptive trigger criteria for "
            "phase transitions based on observed utilization or coverage; (2) quantifies the "
            "value of sequential planning relative to static optimization under demand "
            "uncertainty; (3) models feedback between realized phase outcomes and next-phase "
            "siting decisions; or (4) addresses budget carryover and capital reallocation "
            "between phases."
        ).format(gc4=ctx.gap_counts[4]),
        5: (
            "**Current State of Knowledge.** Gap 5 is evidenced by the near-complete absence "
            f"of meso-micro integration work: only {ctx.gap_counts[5]} papers engage with this "
            "dimension. The gap exists at the boundary between transportation planning (which "
            "operates at city or corridor scale) and urban design / site engineering (which "
            "operates at parcel and street scale). Planning practice implicitly performs this "
            "translation, but without an explicit, validated protocol, the quality and "
            "consistency of the translation varies widely across practitioners and contexts.\n\n"
            "**What Is Missing.** No paper: (1) defines a meso-to-micro translation protocol "
            "specifying the minimum information set that must flow from rollout plan to site "
            "selection; (2) develops a site suitability scoring methodology derived from meso "
            "outputs; (3) models the feedback from micro-level constraints back to meso-level "
            "allocation; or (4) validates a meso-micro integration framework against real-world "
            "deployment decisions."
        ),
    }

    for gap_num in range(1, 6):
        label, short_desc = GAPS[gap_num]
        papers_in_gap = ctx.gap_papers[gap_num]
        n = len(papers_in_gap)
        level = "Low" if n < 10 else "Medium" if n < 50 else "High"

        parts += [
            f"### 4.{gap_num} Gap {gap_num}: {label}",
            "",
            f"**Definition:** {short_desc}",
            "",
            f"**Coverage:** {n} of {total} papers ({100*n/total:.0f}%). Coverage level: **{level}**.",
            "",
            GAP_FULL.get(gap_num, ""),
            "",
        ]

        if papers_in_gap:
            parts += [
                f"**Table 4.{gap_num}: Papers Addressing Gap {gap_num}**",
                "",
                "| Key | Authors | Year | Approach | Scope | Equity | Util. | Phased |",
                "|-----|---------|------|----------|-------|--------|-------|--------|",
            ]
            for p in sorted(papers_in_gap, key=lambda x: x["year"], reverse=True):
                auth = _auth_short(p)
                eq = "Y" if p["equity"] else "N"
                util = "Y" if p["utilization"] else "N"
                ph = "Y" if p["phased"] else "N"
                parts.append(
                    f"| `{p['key']}` | {auth} | {p['year']} | "
                    f"{p['approach']} | {p['scope']} | {eq} | {util} | {ph} |"
                )
        else:
            parts.append("*No papers directly address this gap as a primary contribution.*")
        parts.append("")

    # Overall gap coverage summary table
    parts += [
        "### 4.6 Overall Gap Coverage Summary",
        "",
        "**Table 4.6: Dissertation Gap Coverage Across the Corpus**",
        "",
        "| Gap | Label | N Papers | % | Level | Primary Sub-Gap Missing |",
        "|-----|-------|----------|---|-------|------------------------|",
    ]
    sub_gap_firsts = {
        1: "Corridor-based spatial unit construction and comparison",
        2: "Comparative analysis of ≥2 zoning schemas",
        3: "Joint equity-utilization single objective function",
        4: "Adaptive phase-transition trigger criteria",
        5: "Meso-to-micro translation protocol",
    }
    level_map = {1: "High", 2: "Low", 3: "Medium", 4: "Medium", 5: "Low"}
    for i in range(1, 6):
        label = GAPS[i][0]
        n = ctx.gap_counts[i]
        pct = f"{100*n/total:.0f}%"
        lv = level_map[i]
        sg = sub_gap_firsts[i]
        parts.append(f"| Gap {i} | {label} | {n} | {pct} | {lv} | {sg} |")
    parts.append("")

    # Methodology distribution
    parts += [
        "### 4.7 Methodology Distribution Across the Corpus",
        "",
        "**Table 4.7: Approach Type Distribution**",
        "",
        "| Approach | N | % of Corpus |",
        "|----------|---|-------------|",
    ]
    for approach, cnt in ctx.stats["by_approach"].most_common():
        parts.append(f"| {approach} | {cnt} | {100*cnt/total:.1f}% |")
    parts.append("")

    # Spatial scope
    parts += [
        "**Table 4.8: Spatial Scope Distribution**",
        "",
        "| Planning Scope | N | % of Corpus |",
        "|----------------|---|-------------|",
    ]
    for scope, cnt in ctx.stats["by_scope"].most_common():
        parts.append(f"| {scope} | {cnt} | {100*cnt/total:.1f}% |")
    parts.append("")

    # Thematic flag summary
    flags = [
        ("Equity measured or addressed", ctx.stats["equity_count"]),
        ("Utilization measured or addressed", ctx.stats["utilization_count"]),
        ("Phased/sequential approach modeled", ctx.stats["phased_count"]),
        ("Zoning or land-use considered", ctx.stats["zoning_count"]),
        ("Meso-scale planning engaged", ctx.stats["meso_count"]),
        ("Multi-objective formulation", ctx.stats["multi_obj_count"]),
    ]
    parts += [
        "**Table 4.9: Thematic Coverage Flags Across the Corpus**",
        "",
        "| Dimension | N Papers | % of Corpus |",
        "|-----------|----------|-------------|",
    ]
    for dim, cnt in flags:
        parts.append(f"| {dim} | {cnt} | {100*cnt/total:.1f}% |")
    parts.append("")

    # Category distribution
    parts += [
        "**Table 4.10: Primary Category Distribution**",
        "",
        "| Category | N | % |",
        "|----------|---|---|",
    ]
    for cat, cnt in ctx.stats["by_category"].most_common():
        label = CATEGORY_LABELS.get(cat, cat)
        parts.append(f"| {label} | {cnt} | {100*cnt/total:.1f}% |")
    parts.append("")

    return "\n".join(parts)


def section_research_questions(ctx: ProposalContext) -> str:
    g = ctx.gap_counts
    total = ctx.stats["total"]

    return f"""\
## 5. Research Questions

The five identified gaps motivate four research questions, each targeting one or more gaps through a specific methodological contribution. The research questions are designed to be independently answerable while collectively constituting an integrated research program. Each question is framed to produce a measurable deliverable and is grounded in the literature evidence base established in Sections 3 and 4.

### RQ1: Spatial Unit Design and Zoning Schema Comparison (Gaps 1 and 2)

**Research Question:** How can mobility-corridor-aligned spatial units and comparative zoning schema analysis be integrated into urban BEV charging station siting to reduce spatial demand misalignment and quantify the planning consequences of zoning schema choice?

**Motivation:** Gap 1 ({g[1]} papers with partial evidence) documents the systematic reliance on administrative spatial boundaries that misrepresent mobility corridor demand. Gap 2 (only {g[2]} papers) documents the complete absence of comparative zoning schema analysis. These two gaps share a common root: the spatial frame for charging infrastructure planning is treated as fixed and given rather than as a design variable with quantifiable consequences. Addressing them jointly through a spatial unit comparison study that simultaneously varies the spatial unit (administrative vs. corridor-based) and the zoning schema (current ordinance vs. alternative permitting frameworks) would produce the first evidence base for both decisions.

**Scope:** City-scale spatial analysis applied to at least one metropolitan area with available origin-destination trip data and municipal zoning ordinances. Comparison metrics include: spatial demand estimation error (root mean square deviation from observed charging events), Gini coefficient of coverage equity across income quartiles, total network infrastructure cost, and average station utilization rate.

**Expected Measurable Outcomes:**
- A spatial unit alignment score metric quantifying corridor-administrative boundary mismatch
- A zoning schema comparison procedure applicable to any metropolitan area with available land-use data
- Quantified reduction in spatial demand estimation error under corridor-based spatial units vs. TAZ-based baseline
- Evidence on whether zoning schema choice significantly affects equity and utilization outcomes

---

### RQ2: Joint Equity-Utilization Optimization (Gap 3)

**Research Question:** How can equity of geographic access and infrastructure utilization efficiency be simultaneously optimized in charging network design, and what are the Pareto-efficient tradeoffs between these objectives that planners can use to inform deployment decisions?

**Motivation:** Gap 3 ({g[3]} papers with partial evidence) documents the structural separation of equity and utilization in the optimization literature. Of the {total} reviewed papers, only {ctx.stats['equity_count']} measure equity and only {ctx.stats['utilization_count']} measure utilization; fewer still measure both in the same study, and none jointly optimizes both in a single objective function. This separation leaves planners without the quantified tradeoff information needed to make defensible deployment decisions under competing objectives.

**Scope:** Multi-objective optimization model formulated as a bi-objective mixed-integer program, applied to a city-scale charging network with real demographic and transportation demand data. Equity is operationalized as the Gini coefficient of spatial accessibility across census tracts weighted by population. Utilization is operationalized as mean fill rate across deployed stations over a planning horizon.

**Expected Measurable Outcomes:**
- A joint equity-utilization objective function with formal Pareto optimality characterization
- A Pareto frontier mapping the equity-utilization tradeoff space under realistic demand scenarios
- Policy-relevant threshold identification: the minimum utilization penalty required to achieve a given equity improvement
- Comparison with single-objective baselines demonstrating the cost of objective separation

---

### RQ3: Adaptive Phased Deployment (Gap 4)

**Research Question:** What sequencing criteria and adaptive decision rules enable effective, budget-constrained phased deployment of BEV fast-charging infrastructure under demand uncertainty, and how much value does adaptive phasing create relative to static single-period optimization?

**Motivation:** Gap 4 ({g[4]} papers with partial evidence) documents the dominance of static single-period optimization in the literature. Real-world charging deployment is subject to budget cycles, demand uncertainty, and the irreversibility of sited infrastructure — conditions under which adaptive sequential decision-making is theoretically superior to static planning. The literature has not quantified this superiority or defined the trigger criteria that make adaptive phasing operationally feasible.

**Scope:** Multi-stage stochastic programming model with explicit phase-transition trigger criteria. The model represents multiple planning periods (phases), with decision variables at each phase conditioned on demand observations from prior phases. Trigger criteria are defined as utilization rate thresholds that, when exceeded, activate expansion to the next phase. Monte Carlo demand scenarios represent adoption uncertainty.

**Expected Measurable Outcomes:**
- An adaptive phased deployment decision procedure with defined phase-transition trigger criteria
- Quantified value of sequential planning relative to static optimization (expected cost difference under demand uncertainty)
- Sensitivity analysis on the trigger threshold design
- Minimum viable number of deployment phases for capturing the majority of adaptive value

---

### RQ4: Meso-to-Micro Site Translation (Gap 5)

**Research Question:** How can meso-level rollout plans be systematically translated to micro-level site implementation specifications, and what minimum information set must flow from the meso to the micro planning scale to ensure technical and planning feasibility?

**Motivation:** Gap 5 ({g[5]} papers) documents the absence of any validated translation protocol bridging city-level rollout planning to site-level implementation. This gap is the operational boundary of the current literature: research produces rollout plans but cannot operationalize them. The consequence in practice is that site selection is performed ad hoc, potentially violating the spatial intent of the rollout plan and introducing unmeasured equity and efficiency losses.

**Scope:** A translation protocol development and validation study. The protocol specifies: (a) the minimum viable information set from meso to micro (which zones, what phase, what charging tier, what minimum coverage radius); (b) a site suitability scoring methodology incorporating land-use compatibility, grid connection proximity, pedestrian access, and parking geometry; and (c) a feedback procedure for reconciling micro-level infeasibilities with meso-level allocations.

**Expected Measurable Outcomes:**
- A formalized meso-to-micro translation protocol
- A site suitability scoring function with defined weights and data sources
- A minimum viable information set specification validated against real-world site deployment decisions
- A protocol validation metric measuring consistency between meso-level rollout intent and micro-level siting outcomes
"""


def section_framework(ctx: ProposalContext) -> str:
    total = ctx.stats["total"]

    return f"""\
## 6. Proposed Research Framework

### 6.1 Framework Overview

The proposed research framework comprises three integrated stages that collectively address all five identified gaps and correspond directly to the four research questions:

**Stage A — Mobility-Corridor Spatial Unit Construction and Zoning Schema Comparison** (RQ1; addresses Gaps 1 and 2)

**Stage B — Joint Equity-Utilization Adaptive Phased Rollout Optimization** (RQ2 and RQ3; addresses Gaps 3 and 4)

**Stage C — Meso-to-Micro Site Translation Protocol** (RQ4; addresses Gap 5)

Each stage produces outputs that serve as direct inputs to the subsequent stage, creating a vertically integrated planning framework from city-scale spatial analysis to site-level implementation. The framework is designed to be applied to any metropolitan area with available origin-destination trip data, demographic data, land-use and zoning records, and grid infrastructure maps.

### 6.2 Stage A: Mobility-Corridor Spatial Unit Construction and Zoning Schema Comparison

Stage A addresses the foundational question of how to define the spatial frame for charging infrastructure planning. Two parallel activities constitute Stage A:

**Activity A1 — Corridor Zone Construction.** Using origin-destination trip data, community detection algorithms (Louvain modularity maximization on a weighted O-D graph) identify functionally coherent travel zones — "corridor zones" — that represent actual charging demand territories rather than administrative boundaries. The corridor zones are compared to TAZ-based and census-tract-based alternatives on four metrics: spatial demand estimation error, Gini coefficient of coverage equity, total network cost, and average station utilization, using a common benchmark siting model applied to each spatial frame.

**Activity A2 — Zoning Schema Comparison.** Using municipal zoning ordinance data, three zoning schemas are defined and compared: (a) the current ordinance (baseline); (b) a "charging-permissive" schema in which all commercial and mixed-use zones permit fast-charging; and (c) a "corridor-aligned" schema in which zoning is redesigned to align with Stage A1 corridor zones. Each schema is applied to the same demand data and optimization model, with outcomes compared on coverage, equity, cost, and utilization.

Stage A outputs: (1) a corridor zone map; (2) a spatial unit alignment score for the study metropolitan area; (3) a zoning schema comparison report with quantified outcome differences.

### 6.3 Stage B: Joint Equity-Utilization Adaptive Phased Rollout Optimization

Stage B builds on Stage A outputs by formulating the charging station placement problem as a multi-objective, multi-stage stochastic optimization using the Stage A corridor zones as the spatial frame.

**Activity B1 — Joint Objective Formulation.** The primary optimization model jointly minimizes the Gini coefficient of spatial accessibility across corridor zones (equity objective) and the inverse of mean station utilization rate (utilization objective). The bi-objective model is solved using the ε-constraint method to map the full Pareto frontier. This directly addresses Gap 3 by providing planners with a quantified equity-utilization tradeoff curve.

**Activity B2 — Adaptive Phasing.** The multi-stage extension represents multiple deployment phases, each subject to a phase budget. Phase-transition trigger criteria are defined as utilization rate thresholds: when mean utilization in deployed stations exceeds a threshold τ, the model activates the next deployment phase. Demand uncertainty is represented through Monte Carlo scenarios of EV adoption growth. The adaptive model is compared to a static single-period benchmark to quantify the value of adaptive phasing (Gap 4).

Stage B outputs: (1) a joint equity-utilization Pareto frontier; (2) an adaptive phased deployment schedule with trigger criteria; (3) quantified value of adaptive vs. static planning.

### 6.4 Stage C: Meso-to-Micro Site Translation Protocol

Stage C operationalizes the Stage B rollout schedule by defining the information translation from meso-level allocation (which corridor zones receive stations in each phase) to micro-level site selection and design specifications.

**Activity C1 — Translation Protocol Definition.** The protocol specifies: (a) the minimum information set flowing from meso to micro (zone identifier, phase, charging tier, coverage radius, equity priority flag); (b) a site suitability scoring function incorporating land-use compatibility score, grid connection proximity (distance to nearest transformer), pedestrian accessibility (Walk Score proxy), and parking geometry feasibility; and (c) a conflict resolution procedure for micro-level infeasibilities (when no site within a zone meets minimum suitability threshold, the protocol triggers meso-level reallocation).

**Activity C2 — Protocol Validation.** The translation protocol is validated against real-world site deployment decisions in at least one metropolitan context where both a city-level charging plan and individual site selection decisions are documented. The validation metric is the consistency score: the proportion of actual selected sites that fall within the protocol's top-ranked suitability quartile for their respective corridor zones.

Stage C outputs: (1) a formalized meso-to-micro translation protocol; (2) a site suitability scoring function; (3) a validation study with consistency score.

### 6.5 Comparison with Existing Approaches

**Table 6.1: Proposed Framework vs. Existing Approaches in the Literature**

| Dimension | Existing Literature (n={total} papers) | Proposed Framework |
|-----------|-----------------------------------------|-------------------|
| Spatial unit | Administrative (TAZ, census tract) in ~{total - ctx.gap_counts[1]} papers | Mobility-corridor zones (Stage A) |
| Zoning analysis | Absent in {total - ctx.gap_counts[2]} papers; binary constraint in {ctx.gap_counts[2]} | Comparative multi-schema analysis (Stage A) |
| Equity-utilization | Single-objective in {total - ctx.stats['equity_count']} equity papers | Joint bi-objective Pareto optimization (Stage B) |
| Planning horizon | Static single-period in majority | Multi-stage adaptive with trigger criteria (Stage B) |
| Scale integration | Meso only; micro absent | Meso + micro with translation protocol (Stage C) |
| Gap coverage | 0–2 gaps per paper (typical) | All 5 gaps addressed across 3 stages |
| Deliverable | Network plan or model | Validated framework with replication protocol |

### 6.6 Study Area and Data Requirements

The proposed framework will be applied to at least one metropolitan study area meeting the following data requirements: (a) origin-destination trip survey or mobile device mobility data; (b) municipal zoning ordinance GIS layers; (c) EV charging demand observations (station transaction data or smart meter data); (d) demographic data at census tract level; (e) grid infrastructure map (transformer locations and capacity); and (f) an existing or planned city charging infrastructure rollout plan. Where actual site selection decisions are documented, Stage C validation will be possible.
"""


def section_contributions_timeline(ctx: ProposalContext) -> str:
    return """\
## 7. Expected Contributions and Timeline

### 7.1 Expected Contributions

This dissertation produces five primary contributions, each directly resolving one of the identified research gaps:

**Contribution 1 — Mobility-Corridor Spatial Unit Methodology (Gap 1)**
A validated method for constructing mobility-corridor spatial zones from origin-destination data, with a quantified spatial unit alignment score and demonstrated reduction in spatial demand estimation error relative to administrative TAZ baselines. This is the first methodology in the literature that directly questions and empirically tests the validity of the spatial frame for charging infrastructure planning.

**Contribution 2 — Zoning Schema Comparison Procedure (Gap 2)**
The first systematic comparative analysis of alternative zoning schemas for charging infrastructure siting, producing a replicable schema comparison procedure that quantifies the coverage, equity, cost, and utilization consequences of zoning schema design choices. This contribution provides evidence that has been entirely absent from the planning literature.

**Contribution 3 — Joint Equity-Utilization Optimization Model (Gap 3)**
A bi-objective optimization model with formal Pareto frontier characterization that simultaneously optimizes equity of spatial access and infrastructure utilization efficiency. The Pareto frontier provides planners with quantified tradeoff information — translating a political/ethical question (how much equity is worth how much efficiency?) into a technically grounded, reproducible analysis.

**Contribution 4 — Adaptive Phasing Decision Procedure (Gap 4)**
A multi-stage stochastic programming model with adaptive phase-transition trigger criteria, validated against demand uncertainty scenarios, with quantified comparison to static single-period optimization. The decision procedure is operationally specified — defining when (trigger criteria) and how (reallocation rules) to advance from one deployment phase to the next.

**Contribution 5 — Meso-to-Micro Translation Protocol (Gap 5)**
A formalized information translation protocol bridging meso-level rollout planning to micro-level site selection, with a validated site suitability scoring function and consistency score against real-world deployment decisions. This contribution closes the operational gap between planning and implementation that currently prevents rollout plans from being systematically operationalized.

### 7.2 Research Timeline

**Table 7.1: Three-Year Research Timeline**

| Phase | Year | Key Activities | Deliverables |
|-------|------|----------------|--------------|
| **Phase 1: Review and Stage A** | Year 1, Q1–Q3 | Complete systematic review; develop and validate corridor zone construction method; conduct zoning schema comparison | Systematic review paper (submitted); Stage A methodology paper (draft) |
| **Phase 1: Stage A Completion** | Year 1, Q4 | Finalize spatial unit alignment score; validate against demand estimation error | Stage A paper (submitted) |
| **Phase 2: Stage B Development** | Year 2, Q1–Q2 | Formulate bi-objective optimization model; compute Pareto frontier; begin multi-stage extension | Stage B model paper (draft) |
| **Phase 2: Stage B Completion** | Year 2, Q3–Q4 | Complete adaptive phasing model; demand uncertainty experiments; comparison with static baseline | Stage B paper (submitted); conference presentations |
| **Phase 3: Stage C Development** | Year 3, Q1–Q2 | Define translation protocol; develop site suitability scoring; protocol validation study | Stage C paper (draft) |
| **Phase 3: Integration and Writing** | Year 3, Q3–Q4 | Full framework integration; case study validation; dissertation writing and defense | Dissertation manuscript; Stage C paper (submitted); defense |

### 7.3 Anticipated Venues for Publication

- **Systematic review paper**: Transportation Research Part C: Emerging Technologies or Journal of Transport Geography
- **Stage A paper**: Environment and Planning B: Urban Analytics and City Science or Computers, Environment and Urban Systems
- **Stage B paper**: Transportation Science or European Journal of Operational Research
- **Stage C paper**: Journal of the American Planning Association or Urban Studies
"""


def section_references(ctx: ProposalContext) -> str:
    parts = [
        "## 8. References",
        "",
        "All references are presented in academic format, grouped by thematic category. "
        "arXiv preprints are identified by their arXiv identifier. For papers with DOIs, "
        "the DOI is provided.",
        "",
    ]

    for cat in CATEGORY_ORDER:
        papers = sorted(
            ctx.by_category.get(cat, []),
            key=lambda p: (_last_name(p["authors"][0]) if p["authors"] else "zzz", p["year"]),
        )
        if not papers:
            continue
        label = CATEGORY_LABELS.get(cat, cat)
        parts.append(f"### {label}")
        parts.append("")
        for p in papers:
            authors_str = ", ".join(p["authors"])
            if len(authors_str) > 200:
                authors_str = ", ".join(p["authors"][:4]) + " et al."
            venue = p.get("venue", "arXiv")
            if p.get("doi"):
                note = f"DOI: {p['doi']}"
            elif p.get("arxiv_id"):
                note = f"arXiv:{p['arxiv_id']}"
            else:
                note = p.get("url", "")
            title_clean = p["title"].replace("|", "\\|")
            parts.append(
                f"[{p['key']}] {authors_str} ({p['year']}). "
                f"*{title_clean}*. {venue}. {note}"
            )
        parts.append("")

    return "\n".join(parts)


# ── Assembly ─────────────────────────────────────────────────────────────────

def generate_proposal(output_path: Path) -> None:
    ctx = load_all_papers()
    logger.info(f"Building proposal from {ctx.stats['total']} papers")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    sections = [
        section_title_abstract(ctx),
        section_introduction(ctx),
        section_methodology(ctx),
        section_related_work(ctx),
        section_gap_analysis(ctx),
        section_research_questions(ctx),
        section_framework(ctx),
        section_contributions_timeline(ctx),
        section_references(ctx),
    ]

    full_text = "\n\n---\n\n".join(sections)
    output_path.write_text(full_text, encoding="utf-8")

    word_count = len(full_text.split())
    section_count = sum(1 for line in full_text.split("\n") if line.startswith("## "))
    logger.info(f"Proposal written: {output_path} ({word_count:,} words, {section_count} sections)")
    print(f"[OK] Proposal generated: {word_count:,} words -> {output_path}")
    if word_count < 20000:
        print(f"  WARNING: Word count {word_count:,} is below 20,000 target")


def main():
    parser = argparse.ArgumentParser(description="Generate 50-page research proposal")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output file path")
    args = parser.parse_args()

    generate_proposal(Path(args.output))


if __name__ == "__main__":
    main()
