"""
Setup Chapter 7 from the prior work ZIP.

1. Extracts all files to outputs/proposal_drafts/ (images → images/)
2. Extracts glossary/acronym defs → chapter7_glossary_defs.tex
3. Extracts body (Introduction..end of discussion) → chapter7_body.tex
4. Creates chapter7_prior_work.tex
5. Copies refs.bib → refs_chapter7.bib
6. Updates generate_latex.py to add packages, input files, bibliography
"""

import zipfile
import shutil
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
ZIP_PATH = PROJECT_ROOT / "Rethinking_Spatial_Units_in_EV_Fast_Charging_Planning__A_Meso_Level_Corridor_Based_Approach.zip"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "proposal_drafts"
IMAGES_DIR = OUTPUT_DIR / "images"

def extract_zip():
    """Extract all files from ZIP to output directory."""
    IMAGES_DIR.mkdir(exist_ok=True)
    with zipfile.ZipFile(ZIP_PATH) as z:
        for name in z.namelist():
            if name.startswith("images/"):
                dest = OUTPUT_DIR / name
                dest.parent.mkdir(exist_ok=True)
                dest.write_bytes(z.read(name))
                print(f"  Extracted: {name}")
            elif name == "refs.bib":
                dest = OUTPUT_DIR / "refs_chapter7.bib"
                dest.write_bytes(z.read(name))
                print("  Extracted refs.bib -> refs_chapter7.bib")

def build_chapter7_files():
    """Parse main.tex and build chapter7 LaTeX files."""
    with zipfile.ZipFile(ZIP_PATH) as z:
        content = z.read("main.tex").decode("utf-8")
    lines = content.split("\n")

    # ---- 1. Extract glossary defs (lines 47–545) ----
    # Lines with \newacronym or \newglossaryentry blocks
    gls_lines = []
    in_gls_block = False
    brace_depth = 0
    for i, line in enumerate(lines[47:546], start=47):
        stripped = line.strip()
        # Collect entire \newacronym or \newglossaryentry blocks
        if stripped.startswith(r"\newacronym") or stripped.startswith(r"\newglossaryentry"):
            in_gls_block = True
            brace_depth = 0
        if in_gls_block:
            gls_lines.append(line)
            brace_depth += line.count("{") - line.count("}")
            if brace_depth <= 0 and in_gls_block:
                in_gls_block = False

    glossary_tex = "\n".join(gls_lines)
    gls_file = OUTPUT_DIR / "chapter7_glossary_defs.tex"
    gls_file.write_text(
        "% Chapter 7 glossary and acronym definitions (extracted from main.tex)\n"
        "% These must be loaded BEFORE \\begin{document}\n\n"
        + glossary_tex + "\n",
        encoding="utf-8",
    )
    print(f"  Written: chapter7_glossary_defs.tex ({len(gls_lines)} lines)")

    # ---- 2. Extract body (line 647 → line before \bibliographystyle at 2656) ----
    # Find exact body start: first \section{Introduction}
    body_start = None
    bib_line = None
    for i, line in enumerate(lines):
        if body_start is None and r"\section{Introduction}" in line:
            body_start = i
        if bib_line is None and r"\bibliographystyle{elsarticle-num}" in line and i > 600:
            bib_line = i
            break

    body_lines_raw = lines[body_start:bib_line]

    # Adapt the body for Thesis.cls:
    # - \section → \section (keep as-is; we wrap in \chapter{})
    # - Remove \maketitle, \begin{frontmatter}...\end{frontmatter}, \printglossary
    # - Remove \bibliographystyle / \bibliography lines (handled at top level)
    # - \begin{abstract}...\end{abstract} → skip (already in proposal)
    # - Replace \begin{figure} \includegraphics paths (already use images/ prefix, keep)
    # - Replace \cite{...} → \cite{...} (keep, refs_chapter7.bib will be loaded)

    skip_envs = {"frontmatter", "abstract", "highlights", "keyword"}
    skip_env_stack = []
    adapted = []
    for line in body_lines_raw:
        stripped = line.strip()
        # Skip begin/end of unwanted environments
        for env in skip_envs:
            if stripped == f"\\begin{{{env}}}":
                skip_env_stack.append(env)
                break
            if stripped == f"\\end{{{env}}}":
                if skip_env_stack and skip_env_stack[-1] == env:
                    skip_env_stack.pop()
                    line = None  # signal to skip this line too
                break
        if skip_env_stack:
            continue
        if line is None:
            continue
        # Skip \printglossary, \bibliographystyle, \bibliography
        if any(stripped.startswith(cmd) for cmd in [
            r"\printglossary", r"\bibliographystyle", r"\bibliography{",
            r"\maketitle", r"\begin{document}", r"\end{document}",
        ]):
            continue
        adapted.append(line)

    body_tex = "\n".join(adapted)
    body_file = OUTPUT_DIR / "chapter7_body.tex"
    body_file.write_text(body_tex + "\n", encoding="utf-8")
    print(f"  Written: chapter7_body.tex ({len(adapted)} lines)")

    # ---- 3. Create chapter7_prior_work.tex ----
    chapter7_content = r"""\chapter{Rethinking Spatial Units in BEV Fast Charging Planning: A Meso-Level Mobility-Based Approach}
\label{ch:prior_work}

% This chapter presents the preliminary study that directly motivates the dissertation's core research
% questions. The full paper is reproduced here without modification.

\input{chapter7_body}
"""
    chap_file = OUTPUT_DIR / "chapter7_prior_work.tex"
    chap_file.write_text(chapter7_content, encoding="utf-8")
    print("  Written: chapter7_prior_work.tex")


def patch_generate_latex():
    """Patch generate_latex.py to include Chapter 7 packages, glossary, and input."""
    gen_path = PROJECT_ROOT / "workflows" / "generate_latex.py"
    src = gen_path.read_text(encoding="utf-8")

    # ---- A. Add packages to PREAMBLE (before \documentclass line) ----
    extra_packages = r"""\\PassOptionsToPackage{ruled,linesnumbered}{algorithm2e}
\\usepackage{algorithm}
\\usepackage{algorithmic}
\\usepackage{siunitx}
\\siunitx{table-format=1.4}
\\usepackage{colortbl}
\\usepackage{threeparttable}
\\usepackage{subcaption}
\\usepackage{pgfplots}
\\pgfplotsset{compat=1.18}
\\usepackage[acronym,nonumberlist,nomain]{glossaries}
\\makeglossaries
\\input{chapter7_glossary_defs}
"""
    # Insert just before \documentclass
    docclass_marker = r"\\documentclass["
    if docclass_marker in src and extra_packages.strip() not in src:
        # Find where the PREAMBLE string starts building
        # The preamble is defined as a multi-line string in generate_latex.py
        # Look for the line that has \PassOptionsToPackage{colorlinks (already there)
        # and insert our extra packages right before \documentclass
        old_snippet = r"\\PassOptionsToPackage{colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue}{hyperref}\n\\documentclass["
        new_snippet = r"\\PassOptionsToPackage{colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue}{hyperref}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\\usepackage{siunitx}\n\\usepackage{colortbl}\n\\usepackage{threeparttable}\n\\usepackage{subcaption}\n\\usepackage{pgfplots}\n\\pgfplotsset{compat=1.18}\n\\usepackage[acronym,nonumberlist,nomain]{glossaries}\n\\makeglossaries\n\\input{chapter7_glossary_defs}\n\\documentclass["
        if old_snippet in src:
            src = src.replace(old_snippet, new_snippet)
            print("  Patched: added packages to PREAMBLE")
        else:
            print("  WARNING: could not find PassOptionsToPackage line for package injection")

    # ---- B. Inject \input{chapter7_prior_work} before bibliography ----
    old_bib = r'r"\\bibliography{references}"'
    new_bib = r'r"\\input{chapter7_prior_work}\n\\bibliography{references,refs_chapter7}"'
    if old_bib in src:
        src = src.replace(old_bib, new_bib)
        print("  Patched: bibliography line now includes refs_chapter7")
    else:
        # Try alternate forms
        old_bib2 = '"\\\\bibliography{references}"'
        new_bib2 = '"\\\\input{chapter7_prior_work}\\n\\\\bibliography{references,refs_chapter7}"'
        if old_bib2 in src:
            src = src.replace(old_bib2, new_bib2)
            print("  Patched (alt): bibliography line now includes refs_chapter7")
        else:
            print("  WARNING: could not find bibliography line to patch")

    gen_path.write_text(src, encoding="utf-8")


def remove_chapter8_from_proposal():
    """Remove the manually-added Chapter 8 preliminary study from proposal.md."""
    prop_path = OUTPUT_DIR / "proposal.md"
    src = prop_path.read_text(encoding="utf-8")

    # Find ## 8. Preliminary Study section and remove it
    # Chapter 8 starts with "## 8." and ends before "## 9." (References)
    # Use regex to find and remove
    pattern = re.compile(
        r'\n## 8\. Preliminary Study.*?(?=\n## 9\. References|\Z)',
        re.DOTALL
    )
    new_src = pattern.sub("", src)

    if new_src != src:
        # Renumber References back from 9 to 8
        new_src = new_src.replace("## 9. References", "## 8. References")
        prop_path.write_text(new_src, encoding="utf-8")
        print("  Removed Chapter 8 Preliminary Study from proposal.md")
        print("  Renumbered References: 9 -> 8")
    else:
        print("  No Chapter 8 found in proposal.md (already removed or not present)")


if __name__ == "__main__":
    print("=== Setting up Chapter 7 ===")
    print("\n[1] Extracting ZIP files...")
    extract_zip()

    print("\n[2] Building chapter7 LaTeX files...")
    build_chapter7_files()

    print("\n[3] Patching generate_latex.py...")
    patch_generate_latex()

    print("\n[4] Removing Chapter 8 from proposal.md...")
    remove_chapter8_from_proposal()

    print("\nDone. Next: run generate_latex.py then pdflatex.")
