"""
Extract specific methodology/technique names from full PDF text for all included papers.
Saves results to memory/paper_approaches.json.
Searches methodology/abstract sections first, then full text, in priority order.
"""

import json
import re
import sys
from pathlib import Path

import pymupdf

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PAPERS_DIR = PROJECT_ROOT / "memory" / "papers"
OUT_FILE = PROJECT_ROOT / "memory" / "paper_approaches.json"

# ---------------------------------------------------------------------------
# Technique patterns — ordered from most specific to most generic.
# Each tuple: (search_regex_str, display_label)
# Matched case-insensitively; first match wins.
# ---------------------------------------------------------------------------
TECHNIQUE_PATTERNS = [
    # ── Stochastic / robust programming ────────────────────────────────────
    (r"two.stage stochastic.*?(?:milp|mixed.integer|programming)",
     "Two-stage stochastic MILP"),
    (r"two.stage stochastic",           "Two-stage stochastic programming"),
    (r"chance.constrained.*?(?:milp|programming)",
     "Chance-constrained MILP"),
    (r"chance.constrained",             "Chance-constrained programming"),
    (r"distributionally robust",        "Distributionally robust optimization"),
    (r"robust optimization model|robust optimization framework|robust optimization approach|propose.*?robust optim|robust optim.*?model",
                                        "Robust optimization"),
    (r"scenario.based stochastic",      "Scenario-based stochastic programming"),
    (r"stochastic.*?milp",              "Stochastic MILP"),
    (r"stochastic.*?mixed.integer",     "Stochastic MILP"),
    (r"stochastic.*?program",           "Stochastic programming"),
    # ── Bilevel / multi-level ───────────────────────────────────────────────
    (r"bilevel.*?milp",                 "Bilevel MILP"),
    (r"bilevel.*?programming",          "Bilevel programming"),
    (r"bilevel",                        "Bilevel optimization"),
    (r"multi.level.*?program",          "Multi-level programming"),
    (r"stackelberg",                    "Stackelberg game"),
    # ── MILP / MIP / ILP ───────────────────────────────────────────────────
    (r"\bmilp\b",                       "MILP"),
    (r"mixed.integer linear program",   "MILP"),
    (r"\bminlp\b",                      "MINLP"),
    (r"mixed.integer nonlinear program","MINLP"),
    (r"mixed.integer.*?program",        "Mixed-integer programming"),
    (r"\bilp\b",                        "Integer linear programming"),
    (r"integer linear program",         "Integer linear programming"),
    (r"integer program",                "Integer programming"),
    # ── Decomposition methods ───────────────────────────────────────────────
    (r"benders.*?decomposition",        "Benders decomposition"),
    (r"lagrangian relaxation",          "Lagrangian relaxation"),
    (r"column generation",              "Column generation"),
    (r"branch.and.(?:bound|cut|price)", "Branch-and-bound"),
    (r"branch.and.bound",               "Branch-and-bound"),
    # ── Convex / conic ─────────────────────────────────────────────────────
    (r"second.order cone",              "Second-order cone programming"),
    (r"\bsocp\b",                       "Second-order cone programming"),
    (r"semidefinite program",           "Semidefinite programming"),
    (r"\bsdp\b",                        "Semidefinite programming"),
    (r"convex.*?program",               "Convex programming"),
    (r"quadratic program",              "Quadratic programming"),
    (r"\bqp\b",                         "Quadratic programming"),
    # ── Multi-objective ─────────────────────────────────────────────────────
    (r"pareto.*?front",                 "Multi-objective (Pareto)"),
    (r"multi.objective.*?(?:milp|integer|linear)",
     "Multi-objective MILP"),
    (r"multi.objective.*?(?:genetic|nsga|moga)",
     "Multi-objective genetic algorithm"),
    (r"nsga.ii|nsga2",                  "NSGA-II"),
    (r"nsga.iii|nsga3",                 "NSGA-III"),
    (r"mopso",                          "Multi-objective PSO"),
    (r"multi.objective.*?optim",        "Multi-objective optimization"),
    (r"multiobjective.*?optim",         "Multi-objective optimization"),
    # ── Metaheuristics ─────────────────────────────────────────────────────
    (r"genetic algorithm",              "Genetic algorithm"),
    (r"\bga\b.*?(?:optim|charg|plac)",  "Genetic algorithm"),
    (r"particle swarm",                 "Particle swarm optimization"),
    (r"\bpso\b",                        "Particle swarm optimization"),
    (r"simulated annealing",            "Simulated annealing"),
    (r"tabu search",                    "Tabu search"),
    (r"ant colony",                     "Ant colony optimization"),
    (r"\baco\b",                        "Ant colony optimization"),
    (r"harmony search",                 "Harmony search"),
    (r"grey wolf",                      "Grey wolf optimizer"),
    (r"whale optimization",             "Whale optimization"),
    (r"firefly algorithm",              "Firefly algorithm"),
    (r"differential evolution",         "Differential evolution"),
    (r"evolutionary algorithm",         "Evolutionary algorithm"),
    (r"bee colony|bee algorithm",       "Bee colony algorithm"),
    (r"cuckoo search",                  "Cuckoo search"),
    (r"bat algorithm",                  "Bat algorithm"),
    (r"moth.flame",                     "Moth-flame optimization"),
    (r"salp swarm",                     "Salp swarm algorithm"),
    (r"harris hawks",                   "Harris hawks optimization"),
    (r"aquila optimizer",               "Aquila optimizer"),
    (r"tunicate swarm",                 "Tunicate swarm algorithm"),
    (r"electric eel foraging",          "Electric eel foraging optimizer"),
    (r"golden eagle",                   "Golden eagle optimizer"),
    # ── Dynamic programming / DP ────────────────────────────────────────────
    (r"dynamic program",                "Dynamic programming"),
    (r"markov decision",                "Markov decision process"),
    (r"\bmdp\b",                        "Markov decision process"),
    # ── Reinforcement learning ──────────────────────────────────────────────
    (r"deep q.network|\bdqn\b",          "Deep Q-network (DQN)"),
    (r"proximal policy optimization|\bppo\b(?=\s+algorithm|\s+agent|\s+model|\s+network|\s+train)",
                                        "Proximal policy optimization"),
    (r"soft actor.critic|\bsac\b(?=\s+algorithm|\s+agent|\s+policy)",
                                        "Soft actor-critic"),
    (r"actor.critic",                   "Actor-critic RL"),
    (r"multi.agent reinforcement",      "Multi-agent RL"),
    (r"reinforcement learning",         "Reinforcement learning"),
    # ── Deep learning ────────────────────────────────────────────────────────
    (r"graph neural network|\bgnn\b",    "Graph neural network"),
    (r"graph convolutional",            "Graph convolutional network"),
    # Transformer — explicitly ML context only (NOT power/electrical transformer)
    (r"transformer.(?:based|model|network|architecture|encoder|decoder)",
     "Transformer model"),
    (r"vision transformer|\bvit\b",     "Vision Transformer"),
    (r"attention.based.*?network|self.attention.*?network",
     "Attention-based network"),
    (r"long short.term memory|\blstm\b","LSTM"),
    (r"gated recurrent unit|\bgru\b",   "GRU"),
    (r"convolutional neural|\bcnn\b",   "Convolutional neural network"),
    (r"recurrent neural",               "Recurrent neural network"),
    (r"autoencoder",                    "Autoencoder"),
    (r"generative adversarial|\bgan\b", "Generative adversarial network"),
    (r"variational autoencoder|\bvae\b","Variational autoencoder"),
    (r"deep neural network|\bdnn\b",    "Deep neural network"),
    (r"deep learning",                  "Deep learning"),
    (r"neural network",                 "Neural network"),
    # ── Classical ML ─────────────────────────────────────────────────────────
    (r"random forest",                  "Random forest"),
    (r"xgboost|gradient boosting",      "Gradient boosting"),
    (r"support vector machine|svm",     "Support vector machine"),
    (r"k.means.*?cluster",              "k-means clustering"),
    (r"hierarchical cluster",           "Hierarchical clustering"),
    (r"dbscan",                         "DBSCAN clustering"),
    (r"k.nearest neighbor|knn",         "k-nearest neighbors"),
    (r"logistic regression",            "Logistic regression"),
    (r"linear regression",              "Linear regression"),
    (r"gaussian process",               "Gaussian process"),
    (r"bayesian.*?(?:optim|network|inference)",
     "Bayesian optimization"),
    (r"machine learning",               "Machine learning"),
    # ── Simulation ───────────────────────────────────────────────────────────
    (r"agent.based.*?(?:model|simulat)", "Agent-based simulation"),
    (r"monte carlo",                    "Monte Carlo simulation"),
    (r"discrete.event simulat",         "Discrete-event simulation"),
    (r"microsimulat",                   "Microsimulation"),
    (r"traffic simulat",                "Traffic simulation"),
    # ── Game theory ──────────────────────────────────────────────────────────
    (r"nash equilibrium",               "Nash equilibrium game"),
    (r"cooperative game",               "Cooperative game theory"),
    (r"non.cooperative game",           "Non-cooperative game theory"),
    (r"game.theoretic",                 "Game-theoretic model"),
    (r"auction.*?mechanism",            "Auction mechanism"),
    (r"mechanism design",               "Mechanism design"),
    # ── Network / flow ────────────────────────────────────────────────────────
    (r"network flow",                   "Network flow optimization"),
    (r"facility location",              "Facility location model"),
    (r"set.cover",                      "Set-cover formulation"),
    (r"p.median",                       "p-median model"),
    (r"p.center",                       "p-center model"),
    (r"maximal covering",               "Maximal covering model"),
    (r"location.allocation",            "Location-allocation model"),
    (r"covering.*?location",            "Covering location model"),
    # ── Spatial / GIS ────────────────────────────────────────────────────────
    (r"gis.based|geographic information system",
     "GIS-based analysis"),
    (r"spatial.*?(?:cluster|optim|analys)",
     "Spatial optimization"),
    (r"kernel density",                 "Kernel density estimation"),
    (r"voronoi",                        "Voronoi decomposition"),
    (r"gravity model",                  "Gravity model"),
    # ── Statistical / econometric ─────────────────────────────────────────────
    (r"discrete choice",                "Discrete choice model"),
    (r"stated preference",              "Stated preference analysis"),
    (r"revealed preference",            "Revealed preference analysis"),
    (r"survey.*?(?:analysis|data)",     "Survey-based analysis"),
    (r"regression analysis",            "Regression analysis"),
    (r"panel data",                     "Panel data analysis"),
    (r"causal inference",               "Causal inference"),
    (r"difference.in.difference",       "Difference-in-differences"),
    (r"propensity score",               "Propensity score matching"),
    (r"spatial econometric",            "Spatial econometrics"),
    # ── Queuing / operations ─────────────────────────────────────────────────
    (r"queuing theory|queueing",        "Queuing theory"),
    (r"markov chain",                   "Markov chain model"),
    (r"stochastic process",             "Stochastic process"),
    # ── Large language models ─────────────────────────────────────────────────
    (r"large language model",           "Large language model"),
    (r"\bllm\b.*?(?:plan|optim|agent|generat|reason)",
                                        "Large language model"),
    (r"chatgpt|gpt.(?:3|4|o)",         "GPT-based model"),
    # BERT: require ML context (not acronym for circuit/sensor terminology)
    (r"\bBERT\b.*?(?:embed|pretrain|fine.tun|transforme|NLP|language)",
                                        "BERT-based model"),
    # ── Generic fallbacks ────────────────────────────────────────────────────
    (r"linear program",                 "Linear programming"),
    (r"heuristic.*?approach",           "Heuristic approach"),
    (r"meta.heuristic",                 "Metaheuristic"),
    (r"exact.*?(?:algorithm|method)",   "Exact algorithm"),
    (r"approximation.*?algorithm",      "Approximation algorithm"),
    (r"greedy.*?algorithm",             "Greedy algorithm"),
    (r"optimization model",             "Optimization model"),
]

_COMPILED_TECH = [
    (re.compile(pat, re.IGNORECASE | re.DOTALL), label)
    for pat, label in TECHNIQUE_PATTERNS
]


def extract_pdf_text(pdf_path: Path, max_pages: int = 50) -> str:
    try:
        doc = pymupdf.open(str(pdf_path))
        pages = min(len(doc), max_pages)
        chunks = []
        for i in range(pages):
            chunks.append(doc[i].get_text("text"))
        doc.close()
        return "\n".join(chunks)
    except Exception as e:
        print(f"  [warn] {pdf_path.name}: {e}", file=sys.stderr)
        return ""


def _priority_text(full_text: str) -> str:
    """Return abstract + methodology section text (tight windows), then full text."""
    sections = []
    # Abstract: up to 1500 chars after the word "abstract"
    for m in re.finditer(r"\babstract\b[\s\S]{0,1500}", full_text, re.IGNORECASE):
        sections.append(m.group(0))
        break  # only first abstract
    # Methodology / problem formulation / proposed method sections: tight 2000-char windows
    for header_re in [
        r"(?:^|\n)\s*(?:\d+\.?\s*)?(?:methodology|proposed method|problem formulation|"
        r"mathematical formulation|optimization model|solution approach|"
        r"algorithm design|method(?:s|\s+and\s))\b[^\n]{0,100}\n[\s\S]{0,2000}",
    ]:
        for m in re.finditer(header_re, full_text, re.IGNORECASE | re.MULTILINE):
            sections.append(m.group(0))
            if len(sections) >= 4:
                break
    # Prepend high-priority sections; append full text as fallback
    return " ".join(sections) + " " + full_text[:8000]


# Methods that couldn't exist before a given year
_MIN_YEAR = {
    "Transformer model": 2017,
    "Vision Transformer": 2020,
    "BERT-based model": 2018,
    "Large language model": 2022,
    "GPT-based model": 2020,
    "Deep Q-network (DQN)": 2015,
    "Proximal policy optimization": 2017,
    "Soft actor-critic": 2018,
    "GRU": 2014,
    "LSTM": 1997,
    "Graph neural network": 2017,
    "Graph convolutional network": 2016,
}


def find_technique(text: str, year: int = 9999) -> str:
    priority = _priority_text(text)
    for cre, label in _COMPILED_TECH:
        if cre.search(priority):
            min_yr = _MIN_YEAR.get(label, 0)
            if year >= min_yr:
                return label
    return ""


def get_pdf_for_key(key: str) -> Path | None:
    candidates = list(PAPERS_DIR.glob(f"{key}.pdf"))
    if not candidates:
        candidates = list(PAPERS_DIR.glob(f"{key}v*.pdf"))
    if not candidates:
        meta_file = PAPERS_DIR / f"{key}_metadata.json"
        if meta_file.exists():
            meta = json.loads(meta_file.read_text(encoding="utf-8"))
            arxiv_id = meta.get("arxiv_id", "")
            if arxiv_id:
                candidates = list(PAPERS_DIR.glob(f"{arxiv_id}*.pdf"))
    return candidates[0] if candidates else None


def main():
    existing: dict[str, str] = {}
    if OUT_FILE.exists():
        existing = json.loads(OUT_FILE.read_text(encoding="utf-8"))

    meta_files = list(PAPERS_DIR.glob("*_metadata.json"))
    print(f"Total papers: {len(meta_files)}")

    to_process = []
    for mf in meta_files:
        key = mf.stem.replace("_metadata", "")
        if key in existing:
            continue
        clf_file = PAPERS_DIR / f"{key}_classification.md"
        if not clf_file.exists():
            continue
        clf_text = clf_file.read_text(encoding="utf-8", errors="replace")
        if "**Included:** Yes" not in clf_text and "**Included:** yes" not in clf_text:
            continue
        to_process.append(key)

    print(f"Papers to process (no cached approach): {len(to_process)}")

    found = {}
    no_pdf = []
    no_match = []
    for key in sorted(to_process):
        pdf = get_pdf_for_key(key)
        if not pdf:
            no_pdf.append(key)
            continue
        text = extract_pdf_text(pdf)
        if not text.strip():
            no_pdf.append(key)
            continue
        # Read year from metadata for year-gating
        meta_f = PAPERS_DIR / f"{key}_metadata.json"
        paper_year = 9999
        if meta_f.exists():
            try:
                meta = json.loads(meta_f.read_text(encoding="utf-8"))
                paper_year = int(str(meta.get("year", 9999))[:4])
            except Exception:
                pass
        technique = find_technique(text, year=paper_year)
        if technique:
            found[key] = technique
            print(f"  [found] {key:50s} -> {technique}")
        else:
            no_match.append(key)
            print(f"  [none]  {key:50s}")

    print(f"\nFound: {len(found)}  No PDF: {len(no_pdf)}  No match: {len(no_match)}")

    existing.update(found)
    OUT_FILE.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Saved {len(existing)} entries to {OUT_FILE.name}")


if __name__ == "__main__":
    main()
