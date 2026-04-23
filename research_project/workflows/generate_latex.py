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

PREAMBLE = r"""\documentclass[12pt,a4paper]{article}

% === Encoding & fonts =========================================================
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{microtype}
\usepackage{textgreek}

% === Page geometry ============================================================
\usepackage[
  top=2.54cm, bottom=2.54cm,
  left=3.0cm,  right=2.54cm,
  headheight=14pt
]{geometry}

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

% === Lists ===================================================================
\usepackage{enumitem}
\setlist[itemize]{noitemsep, topsep=4pt}
\setlist[enumerate]{noitemsep, topsep=4pt}

% === Hyperlinks ==============================================================
\usepackage[
  colorlinks=true,
  linkcolor=black,
  citecolor=black,
  urlcolor=blue
]{hyperref}

% === Headers / footers =======================================================
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\textit{Urban BEV Fast-Charging Infrastructure --- Research Proposal}}
\fancyhead[R]{\small\thepage}
\renewcommand{\headrulewidth}{0.4pt}

% === Section formatting ======================================================
\usepackage{titlesec}
\titleformat{\section}{\large\bfseries}{\thesection.}{0.6em}{}[\titlerule]
\titleformat{\subsection}{\normalsize\bfseries}{\thesubsection}{0.5em}{}
\titleformat{\subsubsection}{\normalsize\itshape}{\thesubsubsection}{0.5em}{}

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

% === Abstract formatting =====================================================
\usepackage{abstract}
\renewcommand{\abstractnamefont}{\normalfont\bfseries}
\renewcommand{\abstracttextfont}{\normalfont\small}

% === Misc ====================================================================
\usepackage{xcolor}
\usepackage{setspace}
\onehalfspacing
\usepackage{parskip}
\setlength{\parskip}{6pt}

% === Bibliography ============================================================
\usepackage{natbib}

\begin{document}
"""

POSTAMBLE = r"""
\end{document}
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

def convert_table(lines: list[str]) -> str:
    """Convert a markdown table (list of raw lines) to a LaTeX longtable."""
    rows = []
    for line in lines:
        line = line.strip()
        if not line.startswith("|"):
            continue
        # separator row
        if re.match(r"^\|[-| :]+\|$", line):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)

    if not rows:
        return ""

    n_cols = max(len(r) for r in rows)
    # Build column spec: first column wider, rest auto
    col_spec = "L{4cm}" + " ".join(["L{3cm}"] * (n_cols - 1))
    # Trim to safe width
    if n_cols <= 3:
        col_spec = " ".join(["L{5cm}"] * n_cols)
    elif n_cols == 4:
        col_spec = "L{4.5cm} L{3.5cm} L{2.5cm} L{4cm}"
    elif n_cols == 5:
        col_spec = "L{3.5cm} L{2.5cm} L{2cm} L{2cm} L{3.5cm}"
    elif n_cols >= 6:
        col_spec = " ".join(["L{2.2cm}"] * n_cols)

    out = ["\\begin{longtable}{" + col_spec + "}",
           "\\toprule"]

    for i, row in enumerate(rows):
        # Pad to n_cols
        row = row + [""] * (n_cols - len(row))
        cells = [_process_inline(c) for c in row]
        out.append(" & ".join(cells) + r" \\")
        if i == 0:
            out.append("\\midrule")
            out.append("\\endhead")

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
            out.append(convert_table(table_lines))
            out.append("")
            continue

        # ── HR (---) ──────────────────────────────────────────────────────────
        if re.match(r"^---+\s*$", line):
            flush_abstract()
            out.append("\\bigskip\\noindent\\rule{\\linewidth}{0.4pt}\\bigskip\n")
            i += 1
            continue

        # ── H1 (title) ────────────────────────────────────────────────────────
        if line.startswith("# ") and not line.startswith("## "):
            flush_abstract()
            title = line[2:].strip()
            title_lines.append(_process_inline(title))
            i += 1
            continue

        # ── H2 (section) ──────────────────────────────────────────────────────
        if line.startswith("## "):
            flush_abstract()
            heading = line[3:].strip()
            # Abstract gets special treatment
            if heading.lower() == "abstract":
                # Emit title page first if not done
                if not title_done and title_lines:
                    _emit_title(out, title_lines, lines, i)
                    title_done = True
                out.append("\\begin{abstract}")
                in_abstract = True
            else:
                # Strip leading number for \section if already numbered
                m = re.match(r"^(\d+)\.\s+(.*)", heading)
                sec_title = m.group(2) if m else heading
                out.append(f"\\section{{{_process_inline(sec_title)}}}")
            i += 1
            continue

        # ── H3 (subsection) ───────────────────────────────────────────────────
        if line.startswith("### "):
            flush_abstract()
            heading = line[4:].strip()
            m = re.match(r"^[\d.]+\s+(.*)", heading)
            sub_title = m.group(1) if m else heading
            out.append(f"\\subsection{{{_process_inline(sub_title)}}}")
            i += 1
            continue

        # ── H4 (subsubsection) ────────────────────────────────────────────────
        if line.startswith("#### "):
            flush_abstract()
            heading = line[5:].strip()
            out.append(f"\\subsubsection{{{_process_inline(heading)}}}")
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

    md = input_path.read_text(encoding="utf-8")
    body = md_to_latex(md)

    tex = PREAMBLE + body + POSTAMBLE
    tex = postprocess(tex)
    output_path.write_text(tex, encoding="utf-8")

    lines = tex.count("\n")
    print(f"[OK] LaTeX written: {output_path} ({lines:,} lines)")


if __name__ == "__main__":
    main()
