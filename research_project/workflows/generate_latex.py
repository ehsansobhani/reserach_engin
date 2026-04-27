"""
generate_latex.py — Convert proposal.md to a compilable LaTeX document.

Usage:
    .venv\Scripts\python.exe workflows\generate_latex.py [--input <path>] [--output <path>]

Reads:  outputs/proposal_drafts/proposal.md
Writes: outputs/proposal_drafts/proposal.tex
"""

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DEFAULT_INPUT  = PROJECT_ROOT / "outputs" / "proposal_drafts" / "proposal.md"
DEFAULT_OUTPUT = PROJECT_ROOT / "outputs" / "proposal_drafts" / "proposal.tex"

# ---------------------------------------------------------------------------
# LaTeX preamble
# ---------------------------------------------------------------------------

PREAMBLE = r"""\PassOptionsToPackage{colorlinks=true,linkcolor=black,citecolor=black,urlcolor=blue}{hyperref}
\documentclass[letterpaper, 12pt, oneside, doublespacing]{Thesis}

% === Encoding & fonts =========================================================
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{microtype}
\usepackage{textgreek}

% === Maths ===================================================================
\usepackage{amsmath,amssymb}

% === Tables ==================================================================
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{tabularx}
\usepackage{multirow}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}}

% === Graphics ================================================================
\usepackage{graphicx}
\usepackage{float}

% === Diagrams ================================================================
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds}

% === Lists ===================================================================
\usepackage{enumitem}
\setlist[itemize]{noitemsep, topsep=4pt}
\setlist[enumerate]{noitemsep, topsep=4pt}

% === Code / verbatim =========================================================
\usepackage{listings}
\lstset{
  basicstyle=\small\ttfamily,
  breaklines=true,
  frame=single,
  xleftmargin=6pt,
  xrightmargin=6pt,
}
\usepackage{fancyvrb}

% === Misc ====================================================================
\usepackage{xcolor}

% === Chapter heading format (suppress "Chapter X" label) =====================
\usepackage{titlesec}
\titleformat{\chapter}[hang]{\Large\bfseries}{\thechapter\quad}{0pt}{\Large\bfseries}
\titlespacing*{\chapter}{0pt}{20pt}{12pt}

% === Chapter 7 (prior work) packages =========================================
\usepackage{algorithm}
\usepackage{algorithmic}
\usepackage{siunitx}
\usepackage{colortbl}
\usepackage{threeparttable}
\usepackage{subcaption}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usepackage[acronym,nonumberlist,nomain]{glossaries}
\makeglossaries
\input{chapter7_glossary_defs}

% === Thesis metadata =========================================================
\title{ELECTRICAL VEHICLE FAST CHARGING PLANNING}
\authors{Ehsan Sobhani}
\addresses{}
\date{April 2026}
\subject{}
\keywords{BEV; fast-charging infrastructure; urban planning; spatial optimization; equity; phased deployment; meso-micro integration; systematic literature review; PRISMA}
"""

POSTAMBLE = r"""
\end{document}
"""

def _build_frontmatter(abstract_tex: str) -> str:
    return r"""
\begin{document}
\frontmatter
\maketitle

\setstretch{1.3}
\fancyhead{}
\fancyfoot[C]{\thepage}
\pagestyle{fancy}

\addtotoc{Abstract}
\begin{abstract}
  \addtocontents{toc}{}
""" + abstract_tex + r"""
\end{abstract}

\tableofcontents
\clearpage
\listoffigures
\clearpage
\listoftables
\clearpage

\mainmatter
\fancyhead{}
\fancyfoot[C]{\thepage}
\pagestyle{fancy}
"""

# ---------------------------------------------------------------------------
# Conversion helpers
# ---------------------------------------------------------------------------

def _protect_math(text: str) -> tuple[str, list[str]]:
    """Extract $...$ and $$...$$ spans; replace with placeholders."""
    placeholders: list[str] = []
    result = []
    i = 0
    while i < len(text):
        if text[i] == "$":
            # Check for $$
            if text[i:i+2] == "$$":
                end = text.find("$$", i + 2)
                if end != -1:
                    span = text[i:end+2]
                    placeholders.append(span)
                    result.append(f"\x00MATH{len(placeholders)-1}\x00")
                    i = end + 2
                    continue
            else:
                end = text.find("$", i + 1)
                if end != -1:
                    span = text[i:end+1]
                    placeholders.append(span)
                    result.append(f"\x00MATH{len(placeholders)-1}\x00")
                    i = end + 1
                    continue
        result.append(text[i])
        i += 1
    return "".join(result), placeholders


_GREEK_IN_MATH = str.maketrans({
    "α": r"\alpha",   "β": r"\beta",    "γ": r"\gamma",   "δ": r"\delta",
    "ε": r"\epsilon", "ζ": r"\zeta",    "η": r"\eta",     "θ": r"\theta",
    "ι": r"\iota",    "κ": r"\kappa",   "λ": r"\lambda",  "μ": r"\mu",
    "ν": r"\nu",      "ξ": r"\xi",      "ο": "o",         "π": r"\pi",
    "ρ": r"\rho",     "σ": r"\sigma",   "τ": r"\tau",     "υ": r"\upsilon",
    "φ": r"\phi",     "χ": r"\chi",     "ψ": r"\psi",     "ω": r"\omega",
    "Α": "A",         "Β": "B",         "Γ": r"\Gamma",   "Δ": r"\Delta",
    "Ε": "E",         "Ζ": "Z",         "Η": "H",         "Θ": r"\Theta",
    "Ι": "I",         "Κ": "K",         "Λ": r"\Lambda",  "Μ": "M",
    "Ν": "N",         "Ξ": r"\Xi",      "Ο": "O",         "Π": r"\Pi",
    "Ρ": "R",         "Σ": r"\Sigma",   "Τ": "T",         "Υ": r"\Upsilon",
    "Φ": r"\Phi",     "Χ": "X",         "Ψ": r"\Psi",     "Ω": r"\Omega",
})


def _restore_math(text: str, placeholders: list[str]) -> str:
    for idx, span in enumerate(placeholders):
        # Convert Greek Unicode inside math spans to LaTeX commands
        inner = span[1:-1] if span.startswith("$") and span.endswith("$") else span
        inner = inner.translate(_GREEK_IN_MATH)
        if span.startswith("$$"):
            converted = "$$" + inner[1:-1] + "$$"
        elif span.startswith("$"):
            converted = "$" + inner + "$"
        else:
            converted = span
        text = text.replace(f"\x00MATH{idx}\x00", converted)
    return text


def _escape(text: str) -> str:
    """Escape LaTeX special characters, preserving $...$ math spans."""
    text, math_spans = _protect_math(text)

    # Dashes first (before backslash mangling)
    text = text.replace("—", "---")   # em-dash
    text = text.replace("–", "--")    # en-dash
    # Backslash
    text = text.replace("\\", r"\textbackslash{}")
    # Standard LaTeX specials (no $ — protected above)
    text = text.replace("&",  r"\&")
    text = text.replace("%",  r"\%")
    text = text.replace("#",  r"\#")
    text = text.replace("^",  r"\^{}")
    text = text.replace("_",  r"\_")
    text = text.replace("{",  r"\{")
    text = text.replace("}",  r"\}")
    text = text.replace("~",  r"\textasciitilde{}")
    # Quotes
    text = re.sub(r'"([^"]*)"', r"``\1''", text)
    # Unicode symbols → LaTeX math
    text = text.replace("→", r"$\rightarrow$")
    text = text.replace("↓", r"$\downarrow$")
    text = text.replace("≥", r"$\geq$")
    text = text.replace("≤", r"$\leq$")
    text = text.replace("×", r"$\times$")
    text = text.replace("Θ", r"$\Theta$")
    text = text.replace("λ", r"$\lambda$")
    text = text.replace("ε", r"$\varepsilon$")
    text = text.replace("τ", r"$\tau$")
    # Accented chars not in T1 → transliterate
    text = text.replace("Ľ", r"\v{L}")
    text = text.replace("ľ", r"\v{l}")
    text = text.replace("ř", r"\v{r}")
    text = text.replace("ş", r"\c{s}")
    text = text.replace("ğ", r"\u{g}")
    # Restore math spans (they contain raw $)
    text = _restore_math(text, math_spans)
    return text


def _inline(text: str) -> str:
    """Convert inline markdown to LaTeX (bold, italic, code, links)."""
    # Bold+italic ***
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"\\textbf{\\textit{\1}}", text)
    # Bold **
    text = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", text)
    # Italic *
    text = re.sub(r"\*([^*\n]+?)\*", r"\\textit{\1}", text)
    # Inline code `...`
    text = re.sub(r"`([^`]+)`", r"\\texttt{\1}", text)
    # Markdown links [text](url)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\\href{\2}{\1}", text)
    return text


def _process_inline(text: str) -> str:
    return _inline(_escape(text))


# ---------------------------------------------------------------------------
# Table converter
# ---------------------------------------------------------------------------

_APPROACH_LABELS = {
    "optimization": "Mathematical Optimization",
    "simulation":   "Simulation-Based",
    "empirical":    "Empirical / Case Study",
    "mixed":        "Mixed Methods",
}

# Technique keywords searched (in priority order) in paper abstracts
_TECHNIQUE_PATTERNS = [
    ("two-stage stochastic",       "two-stage stochastic programming"),
    ("robust optimization",        "robust optimization"),
    ("bilevel",                    "bilevel programming"),
    ("multi-objective",            "multi-objective optimization"),
    ("multiobjective",             "multi-objective optimization"),
    ("reinforcement learning",     "reinforcement learning"),
    ("deep learning",              "deep learning"),
    ("neural network",             "neural network"),
    ("machine learning",           "machine learning"),
    ("genetic algorithm",          "genetic algorithm"),
    ("particle swarm",             "particle swarm optimization"),
    ("milp",                       "MILP"),
    ("mixed-integer linear",       "MILP"),
    ("mixed-integer nonlinear",    "MINLP"),
    ("mixed-integer",              "mixed-integer programming"),
    ("stochastic program",         "stochastic programming"),
    ("dynamic program",            "dynamic programming"),
    ("integer program",            "integer programming"),
    ("linear program",             "linear programming"),
    ("agent-based",                "agent-based simulation"),
    ("monte carlo",                "Monte Carlo simulation"),
    ("discrete event",             "discrete-event simulation"),
    ("traffic simulat",            "traffic simulation"),
    ("regression",                 "regression analysis"),
    ("clustering",                 "clustering"),
    ("gis",                        "GIS-based analysis"),
    ("spatial analysis",           "spatial analysis"),
    ("graph-based",                "graph-based approach"),
    ("network flow",               "network flow"),
    ("queueing",                   "queuing theory"),
    ("case study",                 "case study"),
]

# Populated by main() from memory/papers/*_metadata.json and *_extraction.md
_KEY_TITLE_MAP: dict[str, str] = {}
_APPROACH_DETAILS: dict[str, str] = {}   # key → elaborated approach (from abstract)
_PDF_APPROACHES: dict[str, str] = {}     # key → specific technique (from full PDF)


def _raw_key(cell: str) -> str:
    """Strip backticks from a markdown table cell to get the paper key."""
    return re.sub(r"^`(.+)`$", r"\1", cell.strip())


def _key_to_cite(raw_key: str) -> str:
    """Return a \\cite{key} link for use in the Paper column."""
    return f"\\cite{{{raw_key}}}"


def _expand_approach(key: str, code: str) -> str:
    """Return elaborated approach string for a paper.
    Priority: PDF-extracted specific technique > abstract-derived > generic label."""
    if key in _PDF_APPROACHES:
        return _PDF_APPROACHES[key]
    detail = _APPROACH_DETAILS.get(key, "")
    if detail:
        return detail
    return _APPROACH_LABELS.get(code.strip().lower(), code)


def _extract_technique(abstract: str) -> str:
    """Find the most specific technique label from an abstract."""
    text = abstract.lower()
    for keyword, label in _TECHNIQUE_PATTERNS:
        if keyword in text:
            return label
    return ""


# Ordered list of (search_pattern, display_label) — longer/more-specific first
# Searched with word boundaries in both title and abstract
_PLACE_LIST = [
    # Multi-word cities first (to avoid partial matches)
    ("New York City",       "New York, USA"),
    ("New York",            "New York, USA"),
    ("Los Angeles",         "Los Angeles, USA"),
    ("San Francisco",       "San Francisco, USA"),
    ("San Diego",           "San Diego, USA"),
    ("Orange County",       "Orange Co., USA"),
    ("Sioux Falls",         "Sioux Falls, USA"),
    ("Kansas City",         "Kansas City, USA"),
    ("Las Vegas",           "Las Vegas, USA"),
    ("Salt Lake City",      "Salt Lake City, USA"),
    ("Southern California", "S. California, USA"),
    ("Ho Chi Minh City",    "Ho Chi Minh, Vietnam"),
    ("Ho Chi Minh",         "Ho Chi Minh, Vietnam"),
    ("Hong Kong",           "Hong Kong"),
    ("Abu Dhabi",           "Abu Dhabi, UAE"),
    ("West Java",           "West Java, Indonesia"),
    ("São Paulo",           "São Paulo, Brazil"),
    # Single-word cities — US
    ("Toronto",   "Toronto, Canada"),   ("Ottawa",    "Ottawa, Canada"),
    ("Vancouver", "Vancouver, Canada"), ("Montreal",  "Montreal, Canada"),
    ("Calgary",   "Calgary, Canada"),   ("Edmonton",  "Edmonton, Canada"),
    ("Chicago",   "Chicago, USA"),      ("Houston",   "Houston, USA"),
    ("Seattle",   "Seattle, USA"),      ("Boston",    "Boston, USA"),
    ("Atlanta",   "Atlanta, USA"),      ("Denver",    "Denver, USA"),
    ("Phoenix",   "Phoenix, USA"),      ("Portland",  "Portland, USA"),
    ("Austin",    "Austin, USA"),       ("Detroit",   "Detroit, USA"),
    ("Minneapolis","Minneapolis, USA"), ("Pittsburgh","Pittsburgh, USA"),
    ("Columbus",  "Columbus, USA"),     ("Charlotte", "Charlotte, USA"),
    ("Nashville",  "Nashville, USA"),   ("Raleigh",   "Raleigh, USA"),
    # US States (fallback when no city)
    ("Michigan",   "Michigan, USA"),  ("California", "California, USA"),
    ("Texas",      "Texas, USA"),     ("Florida",    "Florida, USA"),
    ("Illinois",   "Illinois, USA"),  ("Ohio",       "Ohio, USA"),
    ("Maryland",   "Maryland, USA"),
    # Europe
    ("London",    "London, UK"),       ("Birmingham", "Birmingham, UK"),
    ("Manchester","Manchester, UK"),   ("Edinburgh",  "Edinburgh, UK"),
    ("Paris",     "Paris, France"),    ("Lyon",       "Lyon, France"),
    ("Toulouse",  "Toulouse, France"),
    ("Berlin",    "Berlin, Germany"),  ("Munich",     "Munich, Germany"),
    ("Hamburg",   "Hamburg, Germany"), ("Frankfurt",  "Frankfurt, Germany"),
    ("Cologne",   "Cologne, Germany"),
    ("Amsterdam", "Amsterdam, NL"),    ("Utrecht",    "Utrecht, NL"),
    ("Oslo",      "Oslo, Norway"),     ("Bergen",     "Bergen, Norway"),
    ("Stockholm", "Stockholm, Sweden"),("Gothenburg", "Gothenburg, Sweden"),
    ("Copenhagen","Copenhagen, DK"),   ("Aarhus",     "Aarhus, DK"),
    ("Vienna",    "Vienna, Austria"),  ("Graz",       "Graz, Austria"),
    ("Zurich",    "Zurich, CH"),       ("Geneva",     "Geneva, CH"),
    ("Chur",      "Chur, CH"),
    ("Barcelona", "Barcelona, Spain"), ("Madrid",     "Madrid, Spain"),
    ("Valencia",  "Valencia, Spain"),  ("Seville",    "Seville, Spain"),
    ("Rome",      "Rome, Italy"),      ("Milan",      "Milan, Italy"),
    ("Turin",     "Turin, Italy"),     ("Naples",     "Naples, Italy"),
    ("Brussels",  "Brussels, Belgium"),("Hasselt",    "Hasselt, Belgium"),
    ("Helsinki",  "Helsinki, Finland"),
    ("Lisbon",    "Lisbon, Portugal"),  ("Porto",     "Porto, Portugal"),
    ("Warsaw",    "Warsaw, Poland"),    ("Krakow",    "Krakow, Poland"),
    ("Prague",    "Prague, Czechia"),   ("Budapest",  "Budapest, Hungary"),
    ("Bucharest", "Bucharest, Romania"),("Athens",    "Athens, Greece"),
    ("Ljubljana", "Ljubljana, Slovenia"),
    ("Luxembourg","Luxembourg City"),   ("Bettembourg","Bettembourg, LU"),
    ("Malaga",    "Malaga, Spain"),
    # Middle East
    ("Dubai",     "Dubai, UAE"),       ("Riyadh",    "Riyadh, KSA"),
    ("Istanbul",  "Istanbul, Turkey"), ("Ankara",    "Ankara, Turkey"),
    ("Tel Aviv",  "Tel Aviv, Israel"),
    # Asia
    ("Beijing",   "Beijing, China"),   ("Shanghai",  "Shanghai, China"),
    ("Shenzhen",  "Shenzhen, China"),  ("Chengdu",   "Chengdu, China"),
    ("Wuhan",     "Wuhan, China"),     ("Nanjing",   "Nanjing, China"),
    ("Guangzhou", "Guangzhou, China"), ("Hangzhou",  "Hangzhou, China"),
    ("Lanzhou",   "Lanzhou, China"),   ("Tianjin",   "Tianjin, China"),
    ("Wuxi",      "Wuxi, China"),      ("Chongqing", "Chongqing, China"),
    ("Zhengzhou", "Zhengzhou, China"),
    ("Singapore", "Singapore"),
    ("Tokyo",     "Tokyo, Japan"),     ("Osaka",     "Osaka, Japan"),
    ("Seoul",     "Seoul, Korea"),     ("Busan",     "Busan, Korea"),
    ("Delhi",     "Delhi, India"),     ("Mumbai",    "Mumbai, India"),
    ("Bangalore", "Bangalore, India"), ("Chennai",   "Chennai, India"),
    ("Hyderabad", "Hyderabad, India"),
    ("Hanoi",     "Hanoi, Vietnam"),   ("Jakarta",   "Jakarta, Indonesia"),
    ("Bangkok",   "Bangkok, Thailand"),("Kuala Lumpur","Kuala Lumpur, Malaysia"),
    # Oceania
    ("Sydney",    "Sydney, Australia"),("Melbourne", "Melbourne, Australia"),
    ("Brisbane",  "Brisbane, Australia"),
    # Africa & Americas
    ("Cairo",     "Cairo, Egypt"),     ("Nairobi",   "Nairobi, Kenya"),
    ("Johannesburg","Johannesburg, SA"),
    ("Santiago",  "Santiago, Chile"),  ("Bogota",    "Bogota, Colombia"),
    ("Lima",      "Lima, Peru"),
    # Countries (last resort — only when no city found above)
    ("China",     "China"),     ("Germany",    "Germany"),
    ("Netherlands","Netherlands"), ("France",  "France"),
    ("Italy",     "Italy"),     ("Spain",      "Spain"),
    ("Indonesia", "Indonesia"), ("Vietnam",    "Vietnam"),
    ("Switzerland","Switzerland"), ("Luxembourg","Luxembourg"),
    ("Norway",    "Norway"),    ("Sweden",     "Sweden"),
    ("Denmark",   "Denmark"),   ("Finland",    "Finland"),
    ("Poland",    "Poland"),    ("Australia",  "Australia"),
    ("Brazil",    "Brazil"),    ("India",      "India"),
    ("Japan",     "Japan"),     ("Korea",      "Korea"),
    ("Turkey",    "Turkey"),    ("Israel",     "Israel"),
    ("Europe",    "Europe (multi-city)"),
]

# Populated in main() from extraction files
_LOCATION_MAP: dict[str, str] = {}


def _extract_location(text: str) -> str:
    """Find the most specific place name from title+abstract text."""
    for pattern, label in _PLACE_LIST:
        if re.search(r'\b' + re.escape(pattern) + r'\b', text, re.IGNORECASE):
            return label
    return ""


# Ordered synthetic/theoretical study type patterns
_STUDY_TYPE_PATTERNS = [
    # Named benchmark networks
    (r'\bSioux[\s\-]Falls\b',                  "Sioux Falls (benchmark)"),
    (r'\bIEEE\s+\d+[\-\s]bus\b',               "IEEE bus test system"),
    (r'\bIEEE\s+test\b',                        "IEEE test system"),
    (r'\b33[\-\s]bus\b',                        "IEEE 33-bus network"),
    (r'\b69[\-\s]bus\b',                        "IEEE 69-bus network"),
    (r'\bSFO\s+network\b',                      "SF road network"),
    # Synthetic/simulated data
    (r'\bsynthetic\s+(network|data|graph|instance|case)',  "Synthetic network"),
    (r'\bsimulated\s+(network|data|environment|scenario)', "Simulated scenario"),
    (r'\brandom(ly)?\s+(generat|sampl|simulat)',           "Randomly generated"),
    (r'\bnumerical\s+(experiment|simulation|study|result)', "Numerical simulation"),
    (r'\bmimick(s|ing)?\s+real[\s\-]world\b',              "Synthetic (real-world proxy)"),
    (r'\btest\s+(network|case|bed|instance)',               "Synthetic test case"),
    (r'\brealistic\s+(network|scenario|case|data)',         "Realistic synthetic network"),
    (r'\bsmall[\s\-]scale\s+network\b',                    "Small-scale test network"),
    (r'\bbenchmark\b',                                      "Benchmark instance"),
    # Agent/game/queueing — purely theoretical
    (r'\bgame[\s\-]theoret',          "Game-theoretic model"),
    (r'\bnon[\s\-]cooperative\s+game', "Non-cooperative game model"),
    (r'\bqueueing\s+(model|theor)',    "Queueing-theory model"),
    (r'\bMarkov\s+(chain|decision)',   "Markov decision model"),
    # General / analytical frameworks
    (r'\banalytical\s+(framework|model|approach|result)', "Analytical framework"),
    (r'\btheoretical\s+(framework|model|analysis)',        "Theoretical model"),
    (r'\bgeneral\s+(framework|formulation|model)',         "General framework"),
    (r'\bco[\s\-]simulation\b',        "Co-simulation testbed"),
    (r'\breal[\s\-]time\s+simulat',    "Real-time simulation"),
    # Global/multi-city reviews
    (r'\bglobal\s+review\b',           "Global review"),
    (r'\bmulti[\s\-]city\b',           "Multi-city study"),
    (r'\b(worldwide|global|international)\b', "International / general"),
]


def _classify_study_type(text: str) -> str:
    """Return a descriptive study-type label for papers with no real-world location."""
    for pattern, label in _STUDY_TYPE_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return label
    return "General / theoretical"


def _latex_location(loc: str) -> str:
    """Escape a location string for a LaTeX table cell.
    Replaces '/' with '{\\slash}' so LaTeX can break long slash-delimited names."""
    loc = _process_inline(loc)
    loc = loc.replace("/", "{\\slash}")
    return loc


def convert_table(lines: list[str], caption: str = "") -> str:
    """Convert a markdown table (list of raw lines) to a LaTeX longtable."""
    rows = []
    header_cells: list[str] = []
    for line in lines:
        line = line.strip()
        if not line.startswith("|"):
            continue
        # separator row
        if re.match(r"^\|[-| :]+\|$", line):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)
        if not header_cells:
            header_cells = [c.lower() for c in cells]

    if not rows:
        return ""

    # Detect paper-list tables: has "key" in first col, and either "gap" or "equity"/"util"/"phased"
    is_paper_table = (
        len(header_cells) >= 6
        and "key" in header_cells[0]
        and (
            any("gap" in h for h in header_cells)
            or any(h in ("equity", "util.", "phased") for h in header_cells)
        )
    )

    # Locate column indices
    approach_col = next((i for i, h in enumerate(header_cells) if "approach" in h), -1)
    scope_col    = next((i for i, h in enumerate(header_cells) if "scope" in h), -1)

    n_cols = max(len(r) for r in rows)
    # Column spec — paper tables get dedicated layouts
    if is_paper_table and n_cols == 6:
        # Paper  Authors  Year  Approach(wide)  Location  Gaps
        col_spec = "L{0.9cm} L{2.2cm} L{0.8cm} L{3.3cm} L{2.5cm} L{1.5cm}"
    elif is_paper_table and n_cols == 7:
        # Paper  Authors  Year  Approach  Location  Gap1  Gap2...
        col_spec = "L{0.9cm} L{2.0cm} L{0.7cm} L{2.6cm} L{2.2cm} L{0.9cm} L{0.9cm}"
    elif is_paper_table and n_cols == 8:
        # Paper  Authors  Year  Approach  Location  Equity  Util.  Phased
        col_spec = "L{0.9cm} L{1.8cm} L{0.7cm} L{2.5cm} L{2.1cm} L{0.7cm} L{0.7cm} L{0.7cm}"
    elif n_cols <= 2:
        col_spec = " ".join(["L{6cm}"] * n_cols)
    elif n_cols == 3:
        col_spec = "L{3.5cm} L{4.5cm} L{4.5cm}"
    elif n_cols == 4:
        col_spec = "L{4.5cm} L{3.5cm} L{2.5cm} L{4cm}"
    elif n_cols == 5:
        col_spec = "L{3.5cm} L{2.5cm} L{2cm} L{2cm} L{3.5cm}"
    else:
        per_col = min(2.0, 11.5 / max(n_cols, 1))
        col_spec = " ".join([f"L{{{per_col:.1f}cm}}"] * n_cols)

    # Build the header row cells
    header_row = list(rows[0]) + [""] * (n_cols - len(rows[0]))
    if is_paper_table:
        if header_row[0].lower().strip() == "key":
            header_row[0] = "Paper"
        if scope_col >= 0 and header_row[scope_col].lower().strip() == "scope":
            header_row[scope_col] = "Location"
    header_cells_bold = [f"\\textbf{{{_process_inline(c)}}}" for c in header_row]
    header_line = " & ".join(header_cells_bold) + r" \\"

    out = ["\\begin{longtable}{" + col_spec + "}"]

    # ── First-page header (caption appears here only → single LOT entry) ──────
    if caption:
        out.append(f"\\caption{{{caption}}}\\\\[4pt]")
    out.append("\\toprule")
    out.append(header_line)
    out.append("\\midrule")
    out.append("\\endfirsthead")

    # ── Continuation header (no caption → no extra LOT entries) ──────────────
    if caption:
        out.append(
            f"\\multicolumn{{{n_cols}}}{{l}}"
            f"{{\\small\\textit{{Table \\thetable\\ --- continued}}}}\\\\[2pt]"
        )
    out.append("\\toprule")
    out.append(header_line)
    out.append("\\midrule")
    out.append("\\endhead")

    # ── Data rows ─────────────────────────────────────────────────────────────
    for i, row in enumerate(rows[1:], start=1):
        row = row + [""] * (n_cols - len(row))
        if is_paper_table:
            raw_key = _raw_key(row[0])
            if approach_col >= 0:
                row[approach_col] = _expand_approach(raw_key, row[approach_col])
            cells = [_key_to_cite(raw_key)]
            for ci, c in enumerate(row[1:], start=1):
                if ci == scope_col and scope_col >= 0:
                    loc_val = _LOCATION_MAP.get(raw_key, "General / theoretical")
                    cells.append(_latex_location(loc_val))
                else:
                    cells.append(_process_inline(c))
        else:
            cells = [_process_inline(c) for c in row]
        out.append(" & ".join(cells) + r" \\")

    out.append("\\bottomrule")
    out.append("\\end{longtable}")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Main converter
# ---------------------------------------------------------------------------

def md_to_latex(md: str) -> str:
    lines = md.split("\n")
    out: list[str] = []
    i = 0
    in_abstract = False
    abstract_done = False
    title_done = False
    title_lines: list[str] = []

    def flush_abstract():
        nonlocal in_abstract, abstract_done
        if in_abstract:
            out.append("\\end{abstract}\n")
            in_abstract = False
            abstract_done = True

    while i < len(lines):
        line = lines[i]

        # ── Code block ──────────────────────────────────────────────────────
        if line.strip().startswith("```"):
            flush_abstract()
            lang = line.strip()[3:].strip()
            i += 1
            code_lines = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            code = "\n".join(code_lines)
            # Replace box-drawing chars with ASCII equivalents for pdfLaTeX
            box_map = str.maketrans({
                "┌": "+", "┐": "+", "└": "+", "┘": "+",
                "├": "+", "┤": "+", "┬": "+", "┴": "+", "┼": "+",
                "─": "-", "│": "|", "╔": "+", "╗": "+", "╚": "+", "╝": "+",
                "═": "=", "║": "|", "↓": "v", "→": ">", "←": "<", "↑": "^",
                "×": "x", "≥": ">=", "≤": "<=", "≈": "~=",
            })
            code = code.translate(box_map)
            # Use lstlisting for code, Verbatim for ASCII diagrams
            if lang in ("", "text", "ascii") or any(c in code for c in ["+--", "| ", "v"]):
                out.append("\\begin{Verbatim}[fontsize=\\small]")
                out.append(code)
                out.append("\\end{Verbatim}\n")
            else:
                out.append(f"\\begin{{lstlisting}}[language={lang or 'text'}]")
                out.append(code)
                out.append("\\end{lstlisting}\n")
            continue

        # ── Table ────────────────────────────────────────────────────────────
        if line.strip().startswith("|"):
            flush_abstract()
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            # Check if the preceding non-blank output line was a bold caption
            caption_tex = ""
            cap_match = None
            for k in range(len(out) - 1, -1, -1):
                if out[k].strip() == "":
                    continue
                cap_m = re.match(
                    r"^\\noindent\s*\\textbf\{Table\s+[\d.]+:\s*(.*?)\}\\?\s*$",
                    out[k].strip()
                )
                if cap_m:
                    caption_tex = cap_m.group(1).rstrip("\\").strip()
                    out.pop(k)
                break
            inner = convert_table(table_lines, caption=caption_tex)
            out.append(inner)
            out.append("")
            continue

        # ── HR (---) ──────────────────────────────────────────────────────────
        if re.match(r"^---+\s*$", line):
            flush_abstract()
            out.append("\\bigskip\\noindent\\rule{\\linewidth}{0.4pt}\\bigskip\n")
            i += 1
            continue

        # ── H1 (title) — already in \title{} in PREAMBLE, skip ──────────────
        if line.startswith("# ") and not line.startswith("## "):
            i += 1
            continue

        # ── H2 (chapter) ─────────────────────────────────────────────────────
        if line.startswith("## "):
            flush_abstract()
            heading = line[3:].strip()
            # Skip Abstract section body — already placed in frontmatter
            if heading.lower() == "abstract":
                i += 1
                while i < len(lines) and not lines[i].startswith("## "):
                    i += 1
                continue
            m = re.match(r"^(\d+)\.\s+(.*)", heading)
            ch_title = m.group(2) if m else heading
            # Expected Contributions and Timeline is commented out
            COMMENTED_CHAPTERS = {"Expected Contributions and Timeline"}
            if ch_title.strip() in COMMENTED_CHAPTERS:
                out.append("\\iffalse % ---- Chapter commented out ----")
                out.append(f"\\chapter{{{_process_inline(ch_title)}}}")
                i += 1
                while i < len(lines) and not lines[i].startswith("## "):
                    out.append(_process_inline(lines[i]))
                    i += 1
                out.append("\\fi % ---- end of commented-out chapter ----")
                continue
            out.append(f"\\chapter{{{_process_inline(ch_title)}}}")
            i += 1
            continue

        # ── H3 (section) ─────────────────────────────────────────────────────
        if line.startswith("### "):
            flush_abstract()
            heading = line[4:].strip()
            m = re.match(r"^[\d.]+\s+(.*)", heading)
            sec_title = m.group(1) if m else heading
            out.append(f"\\section{{{_process_inline(sec_title)}}}")
            i += 1
            continue

        # ── H4 (subsection) ──────────────────────────────────────────────────
        if line.startswith("#### "):
            flush_abstract()
            heading = line[5:].strip()
            out.append(f"\\subsection{{{_process_inline(heading)}}}")
            i += 1
            continue

        # ── Unordered list ────────────────────────────────────────────────────
        if re.match(r"^[-*+] ", line):
            flush_abstract()
            out.append("\\begin{itemize}")
            while i < len(lines) and re.match(r"^[-*+] ", lines[i]):
                item = lines[i][2:].strip()
                out.append(f"  \\item {_process_inline(item)}")
                i += 1
            out.append("\\end{itemize}\n")
            continue

        # ── Ordered list ──────────────────────────────────────────────────────
        if re.match(r"^\d+\. ", line):
            flush_abstract()
            out.append("\\begin{enumerate}")
            while i < len(lines) and re.match(r"^\d+\. ", lines[i]):
                item = re.sub(r"^\d+\. ", "", lines[i]).strip()
                out.append(f"  \\item {_process_inline(item)}")
                i += 1
            out.append("\\end{enumerate}\n")
            continue

        # ── Blank line ────────────────────────────────────────────────────────
        if line.strip() == "":
            if in_abstract:
                out.append("")
            else:
                out.append("")
            i += 1
            continue

        # ── Bold-only line (paragraph heading) ────────────────────────────────
        if re.match(r"^\*\*[^*]+\*\*\s", line) or re.match(r"^\*\*[^*]+\*\*$", line):
            flush_abstract()
            out.append("\n\\noindent " + _process_inline(line) + "\n")
            i += 1
            continue

        # ── Regular paragraph ─────────────────────────────────────────────────
        out.append(_process_inline(line))
        i += 1

    flush_abstract()
    return "\n".join(out)


def _emit_title(out: list[str], title_lines: list[str], lines: list[str], i: int):
    """Emit \\maketitle block. Scan ahead for **Program:** / **Date:** metadata."""
    program, date_str, author = "", "", "ES"
    for line in lines[max(0, i-10):i+10]:
        m = re.match(r"\*\*Program:\*\*\s*(.*)", line)
        if m:
            program = m.group(1).strip()
        m = re.match(r"\*\*Date:\*\*\s*(.*)", line)
        if m:
            date_str = m.group(1).strip()

    title_text = " ".join(title_lines)
    out.insert(0, (
        f"\\title{{\\LARGE\\bfseries {title_text}}}\n"
        f"\\author{{\\large {author}\\\\\\small {program}}}\n"
        f"\\date{{{date_str}}}\n"
        "\\maketitle\n"
        "\\thispagestyle{empty}\n"
        "\\newpage\n"
        "\\tableofcontents\n"
        "\\newpage\n"
    ))


# ---------------------------------------------------------------------------
# Post-processing: ensure ASCII-safe output for pdfLaTeX
# ---------------------------------------------------------------------------

_LATIN_EXT = {
    # Accented chars not in T1 encoding — transliterate
    "ů": r"\r{u}",   # ů
    "Ů": r"\r{U}",   # Ů
    "ž": r"\v{z}",   # ž
    "Ž": r"\v{Z}",   # Ž
    "č": r"\v{c}",   # č
    "Č": r"\v{C}",   # Č
    "š": r"\v{s}",   # š
    "Š": r"\v{S}",   # Š
    "ř": r"\v{r}",   # ř
    "Ř": r"\v{R}",   # Ř
    "ľ": r"\v{l}",   # ľ
    "Ľ": r"\v{L}",   # Ľ
    "ń": r"\'n",     # ń
    "Ń": r"\'N",     # Ń
    # Common T1 chars (included for safety — inputenc should handle these)
    "à": r"\`a",     # à
    "á": r"\'a",     # á
    "â": r"\^a",     # â
    "ä": r'\"a',     # ä
    "æ": r"\ae",     # æ
    "ç": r"\c{c}",   # ç
    "è": r"\`e",     # è
    "é": r"\'e",     # é
    "ê": r"\^e",     # ê
    "ë": r'\"e',     # ë
    "í": r"\'i",     # í
    "ñ": r"\~n",     # ñ
    "ó": r"\'o",     # ó
    "ô": r"\^o",     # ô
    "ö": r'\"o',     # ö
    "ø": r"\o",      # ø
    "ú": r"\'u",     # ú
    "ü": r'\"u',     # ü
    "À": r"\`A",     # À
    "Á": r"\'A",     # Á
    "Ä": r'\"A',     # Ä
    "Æ": r"\AE",     # Æ
    "É": r"\'E",     # É
    "Ö": r'\"O',     # Ö
    "Ø": r"\O",      # Ø
    "Ü": r'\"U',     # Ü
    "ß": r"\ss{}",   # ß
    "ą": r"\k{a}",   # ą
    "Ą": r"\k{A}",   # Ą
    "ć": r"\'c",     # ć
    "Ć": r"\'C",     # Ć
    "ę": r"\k{e}",   # ę
    "Ę": r"\k{E}",   # Ę
    "ś": r"\'s",     # ś
    "Ś": r"\'S",     # Ś
    "ź": r"\'z",     # ź
    "Ź": r"\'Z",     # Ź
    "ż": r"\.z",     # ż
    "Ż": r"\.Z",     # Ż
}

_GREEK_TEXT = {
    # Greek outside math — use textgreek package
    "α": r"\textalpha{}",   "β": r"\textbeta{}",   "γ": r"\textgamma{}",
    "λ": r"\textlambda{}",  "μ": r"\textmu{}",      "π": r"\textpi{}",
    "σ": r"\textsigma{}",   "τ": r"\texttau{}",     "ω": r"\textomega{}",
    "Θ": r"\textTheta{}",   "Λ": r"\textLambda{}",  "Σ": r"\textSigma{}",
    "Ω": r"\textOmega{}",
}


# ---------------------------------------------------------------------------
# Citation injection: add ~\cite{key} after bold author-year citation spans
# ---------------------------------------------------------------------------

def _strip_latex_cmds(s: str) -> str:
    """Remove LaTeX commands to recover approximate plain text."""
    # \cmd{content} → content  (one level)
    s = re.sub(r"\\[a-zA-Z@]+\{([^{}]*)\}", r"\1", s)
    # Standalone accent/symbol commands: \' \` \" \^ \~ \= \. \u \v \H \t \b \c \d \k \r
    s = re.sub(r"\\[a-zA-Z@'`\"^~=.uvHtbcdkr]+", "", s)
    return s


def _normalize_name(s: str) -> str:
    """Lowercase + strip accents for fuzzy name matching."""
    import unicodedata
    nfd = unicodedata.normalize("NFD", s)
    return "".join(c for c in nfd if unicodedata.category(c) != "Mn").lower()


def _build_cite_map(papers_dir: Path) -> dict[str, str]:
    """Return {normalized_last_name+year: bibtex_key} from all metadata files."""
    import json as _json
    result: dict[str, str] = {}
    for meta_file in papers_dir.glob("*_metadata.json"):
        try:
            data = _json.loads(meta_file.read_text(encoding="utf-8"))
            key = data.get("key", "")
            year = str(data.get("year", ""))
            authors = data.get("authors", [])
            if key and year and authors:
                last = authors[0].strip().split()[-1]
                norm = _normalize_name(last)
                lookup = norm + year
                if lookup not in result:        # keep first if collision
                    result[lookup] = key
        except Exception:
            pass
    return result


def _inject_cites(body: str, cite_map: dict[str, str]) -> str:
    """Append ~\\cite{key} after every \\textbf{Author...(YEAR)} span in LaTeX body.

    Uses manual string parsing (no regex on backslashes) to locate each
    \\textbf{} span and scan for the matching closing brace.
    """
    import unicodedata

    MARKER = "\\textbf{"   # literal Python string with one backslash
    result: list[str] = []
    pos = 0

    while True:
        start = body.find(MARKER, pos)
        if start == -1:
            result.append(body[pos:])
            break
        result.append(body[pos:start])

        # Walk forward from the opening { to find the matching closing }
        depth = 0
        i = start + len(MARKER) - 1  # index of opening {
        while i < len(body):
            if body[i] == "{":
                depth += 1
            elif body[i] == "}":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        end = i   # index of closing }

        full_span = body[start : end + 1]          # \textbf{...}
        content   = body[start + len(MARKER) : end] # inside the braces

        # Only process spans that end with (YYYY)
        year_m = re.search(r"\((\d{4})\)\s*$", content)
        if year_m:
            year = year_m.group(1)
            author_raw = content[: year_m.start()].strip()
            # Strip LaTeX accent/symbol commands to get plain text
            author_plain = _strip_latex_cmds(author_raw).strip()
            # Remove trailing "et al."
            author_plain = re.sub(r"\s+et\s+al\.\s*$", "", author_plain).strip()
            if author_plain:
                last_name = author_plain.split()[-1]
                nfd = unicodedata.normalize("NFD", last_name)
                norm = "".join(
                    c for c in nfd if unicodedata.category(c) != "Mn"
                ).lower()
                key = cite_map.get(norm + year, "")
                # Skip if a \cite already follows immediately
                tail = body[end + 1 : end + 8]
                already_cited = "cite{" in tail
                if key and not already_cited:
                    result.append(full_span + "~\\cite{" + key + "}")
                    pos = end + 1
                    continue

        result.append(full_span)
        pos = end + 1

    return "".join(result)


def postprocess(tex: str) -> str:
    """Replace non-ASCII chars in non-verbatim regions."""
    segments = re.split(r'(\\begin\{(?:Verbatim|lstlisting|verbatim)\}.*?\\end\{(?:Verbatim|lstlisting|verbatim)\})',
                        tex, flags=re.DOTALL)
    result = []
    for i, seg in enumerate(segments):
        if i % 2 == 1:
            # Inside verbatim — leave as-is
            result.append(seg)
        else:
            # Outside verbatim — translate
            for char, replacement in _LATIN_EXT.items():
                seg = seg.replace(char, replacement)
            for char, replacement in _GREEK_TEXT.items():
                seg = seg.replace(char, replacement)
            # Strip any remaining high-unicode as last resort
            seg = "".join(c if ord(c) <= 127 or c in "àáâäæçèéêëíñóôöøúüÀÁÄÆÉÖØÜß" else "?" for c in seg)
            result.append(seg)
    return "".join(result)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Convert proposal.md to LaTeX")
    parser.add_argument("--input",  default=str(DEFAULT_INPUT),  help="Input markdown file")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output .tex file")
    args = parser.parse_args()

    input_path  = Path(args.input)
    output_path = Path(args.output)

    # Build key → title and key → approach-detail lookups
    papers_dir = PROJECT_ROOT / "memory" / "papers"
    import json as _json
    for meta_file in papers_dir.glob("*_metadata.json"):
        try:
            data = _json.loads(meta_file.read_text(encoding="utf-8"))
            key = data.get("key", "")
            title = data.get("title", "")
            if key and title:
                _KEY_TITLE_MAP[key] = title
        except Exception:
            pass
    print(f"[info] Loaded {len(_KEY_TITLE_MAP)} paper titles for table rendering")

    # Load PDF-extracted specific technique names
    approaches_path = PROJECT_ROOT / "memory" / "paper_approaches.json"
    if approaches_path.exists():
        _PDF_APPROACHES.update(_json.loads(approaches_path.read_text(encoding="utf-8")))
    print(f"[info] Loaded {len(_PDF_APPROACHES)} PDF-extracted approach techniques")

    # Load curated paper_locations.json (hand-verified via web search)
    curated_locs_path = PROJECT_ROOT / "memory" / "paper_locations.json"
    curated_keys: set[str] = set()
    if curated_locs_path.exists():
        curated = _json.loads(curated_locs_path.read_text(encoding="utf-8"))
        _LOCATION_MAP.update({k: v for k, v in curated.items() if v})
        curated_keys = set(curated.keys())

    # Build approach details and location map from extraction files
    for ext_file in papers_dir.glob("*_extraction.md"):
        try:
            text = ext_file.read_text(encoding="utf-8")
            key_m = re.search(r"\*\*Key:\*\*\s*(\S+)", text)
            code_m = re.search(r"\*\*Approach:\*\*\s*(\S+)", text)
            abs_m = re.search(r"## Abstract\s*\n(.*)", text, re.DOTALL)
            if not key_m:
                continue
            key = key_m.group(1)
            code = code_m.group(1).strip().lower() if code_m else "optimization"
            abstract = abs_m.group(1).strip() if abs_m else ""
            # Approach
            base = _APPROACH_LABELS.get(code, code.title())
            technique = _extract_technique(abstract)
            _APPROACH_DETAILS[key] = f"{base} ({technique})" if technique else base
            # Location — curated values take priority; only derive if not already set
            if key in curated_keys:
                continue
            title = _KEY_TITLE_MAP.get(key, "")
            combined = title + " " + abstract
            loc = _extract_location(combined)
            if loc:
                _LOCATION_MAP[key] = loc
            elif abstract:
                # Fall back to study-type classification
                _LOCATION_MAP[key] = _classify_study_type(combined)
        except Exception:
            pass
    print(f"[info] Loaded {len(_APPROACH_DETAILS)} approach details, {len(_LOCATION_MAP)} locations")

    # Build cite map: normalized_last_name+year → bibtex key
    cite_map = _build_cite_map(papers_dir)
    print(f"[info] Built cite map with {len(cite_map)} entries")

    PRISMA_TIKZ = r"""
\begin{figure}[H]
\centering
\begin{tikzpicture}[
  node distance = 8mm and 12mm,
  mainbox/.style = {
    rectangle, rounded corners=6pt,
    draw=blue!50!black, fill=blue!7, line width=1.2pt,
    text width=70mm, minimum height=18mm,
    align=left, font=\small, inner sep=6pt
  },
  inclbox/.style = {
    rectangle, rounded corners=6pt,
    draw=green!50!black, fill=green!8, line width=1.2pt,
    text width=70mm, minimum height=14mm,
    align=left, font=\small, inner sep=6pt
  },
  exclbox/.style = {
    rectangle, rounded corners=4pt,
    draw=orange!60!black, fill=orange!7, line width=1pt,
    text width=56mm, minimum height=14mm,
    align=left, font=\footnotesize, inner sep=5pt
  },
  arrow/.style  = {-{Stealth[length=7pt]}, thick, blue!60!black},
  sarrow/.style = {-{Stealth[length=6pt]}, thick, orange!60!black},
]
%% ---- Main column ----
\node[mainbox] (id) {%
  \textbf{Identification}\\[3pt]
  Records identified (OpenAlex / arXiv): \textbf{$\sim$580}\\
  After deduplication: \textbf{$\sim$380}%
};

\node[mainbox, below=of id] (screen) {%
  \textbf{Screening} \textit{(title \& abstract)}\\[3pt]
  Records screened: \textbf{$\sim$380}\\
  Records excluded: \textbf{$\sim$227}%
};

\node[mainbox, below=of screen] (elig) {%
  \textbf{Eligibility} \textit{(full-text review)}\\[3pt]
  Full texts assessed: \textbf{$\sim$153}\\
  Full texts excluded: \textbf{$\sim$47}%
};

\node[inclbox, below=of elig] (incl) {%
  \textbf{Included}\\[3pt]
  Studies in qualitative synthesis and gap mapping: \textbf{200}%
};

%% ---- Arrows between main boxes ----
\draw[arrow] (id.south)     -- (screen.north);
\draw[arrow] (screen.south) -- (elig.north);
\draw[arrow] (elig.south)   -- (incl.north);

%% ---- Exclusion box: screening ----
\node[exclbox, right=of screen] (excl1) {%
  \textbf{Excluded ($\sim$227):}\\[2pt]
  No EV/BEV charging component: $\sim$110\\
  No spatial/planning dimension: $\sim$67\\
  Insufficient methodology: $\sim$31\\
  Highway-only / non-urban scope: $\sim$12\\
  Duplicate of included record: $\sim$7%
};

%% ---- Exclusion box: eligibility ----
\node[exclbox, right=of elig] (excl2) {%
  \textbf{Excluded ($\sim$47):}\\[2pt]
  Pure V2G, no spatial planning: $\sim$15\\
  No identifiable methodology: $\sim$12\\
  Irrelevant domain (confirmed): $\sim$20%
};

%% ---- Side arrows ----
\draw[sarrow] (screen.east) -- (excl1.west);
\draw[sarrow] (elig.east)   -- (excl2.west);

\end{tikzpicture}
\caption{PRISMA 2020 flow diagram for the systematic literature review.}
\label{fig:prisma}
\end{figure}
"""

    md = input_path.read_text(encoding="utf-8")

    # Extract abstract text from proposal.md for frontmatter
    abstract_tex = ""
    abs_match = re.search(r"^## Abstract\s*\n(.*?)(?=^## )", md, re.MULTILINE | re.DOTALL)
    if abs_match:
        abs_md = abs_match.group(1).strip()
        abstract_tex = md_to_latex(abs_md)

    body = md_to_latex(md)

    # Inject TikZ PRISMA figure
    body = body.replace("\\%\\%PRISMA\\_TIKZ\\%\\%", PRISMA_TIKZ)
    body = body.replace("%%PRISMA_TIKZ%%", PRISMA_TIKZ)

    # Inject ~\cite{key} after bold author-year citation spans
    body = _inject_cites(body, cite_map)
    n_cites = body.count(r"\cite{")
    print(f"[info] Injected {n_cites} \\cite{{}} links into body")

    # Replace References chapter with BibTeX commands
    for ref_marker in (r"\chapter{References}", r"\section{References}"):
        idx = body.find(ref_marker)
        if idx != -1:
            body = body[:idx] + "\n\\input{chapter7_prior_work}\n\n\\nocite{*}\n\\bibliographystyle{IEEEtran}\n\\bibliography{references,refs_chapter7}\n"
            break

    frontmatter = _build_frontmatter(abstract_tex)
    tex = PREAMBLE + frontmatter + body + POSTAMBLE
    tex = postprocess(tex)
    output_path.write_text(tex, encoding="utf-8")

    lines = tex.count("\n")
    print(f"[OK] LaTeX written: {output_path} ({lines:,} lines)")


if __name__ == "__main__":
    main()
