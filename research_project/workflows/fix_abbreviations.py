"""
fix_abbreviations.py — Enforce first-use-only abbreviation definitions in proposal.md.

Rule:
  - First occurrence: "full form (ABBR)" — kept as-is (defines the abbreviation).
  - All subsequent occurrences of the full form: replaced by ABBR alone.
  - Handles singular/plural variants automatically.

Usage:
    .venv\Scripts\python.exe workflows\fix_abbreviations.py
"""

import re
import sys
from pathlib import Path

PROJECT_ROOT  = Path(__file__).parent.parent
PROPOSAL_PATH = PROJECT_ROOT / "outputs" / "proposal_drafts" / "proposal.md"

# ---------------------------------------------------------------------------
# Abbreviation table
# Each entry: (singular_long, plural_long, abbr_singular, abbr_plural)
# Order matters — more specific entries first to avoid partial replacement.
# ---------------------------------------------------------------------------
ABBREVS = [
    # Infrastructure-specific
    ("battery electric vehicle",         "battery electric vehicles",         "BEV",   "BEVs"),
    ("electric vehicle charging station","electric vehicle charging stations", "EVCS",  "EVCSs"),
    ("fast charging station",            "fast charging stations",             "FCS",   "FCSs"),
    ("mobile charging station",          "mobile charging stations",           "MCS",   "MCSs"),
    ("battery swapping station",         "battery swapping stations",          "BSS",   "BSSs"),
    ("electric vehicle",                 "electric vehicles",                  "EV",    "EVs"),
    # Spatial / planning
    ("traffic analysis zone",            "traffic analysis zones",             "TAZ",   "TAZs"),
    ("geographic information system",    "geographic information systems",     "GIS",   "GIS"),
    ("origin-destination",               "origin-destination",                 "OD",    "OD"),
    # Methods
    ("mixed-integer linear programming", "mixed-integer linear programs",      "MILP",  "MILP"),
    ("mixed-integer linear program",     "mixed-integer linear programs",      "MILP",  "MILP"),
    ("reinforcement learning",           "reinforcement learning",             "RL",    "RL"),
    ("multi-objective optimization",     "multi-objective optimization",       "MOO",   "MOO"),
    ("vehicle-to-grid",                  "vehicle-to-grid",                    "V2G",   "V2G"),
    ("preferred reporting items for systematic reviews and meta-analyses",
     "preferred reporting items for systematic reviews and meta-analyses",    "PRISMA","PRISMA"),
    # Quality / experience
    ("quality of experience",            "quality of experience",              "QoE",   "QoE"),
    ("quality of service",               "quality of service",                 "QoS",   "QoS"),
    # Energy / grid
    ("state of charge",                  "states of charge",                   "SoC",   "SoCs"),
    ("energy management system",         "energy management systems",          "EMS",   "EMS"),
    ("energy storage system",            "energy storage systems",             "ESS",   "ESS"),
    ("plug-in electric vehicle",         "plug-in electric vehicles",          "PEV",   "PEVs"),
]


# ---------------------------------------------------------------------------
# Core engine
# ---------------------------------------------------------------------------

class AbbreviationFixer:
    def __init__(self, abbrevs: list):
        self.abbrevs = abbrevs
        # Track which abbreviations have already been defined in the text
        self.defined: set[str] = set()

    def _build_definition_pattern(self, singular: str, plural: str, abbr_s: str, abbr_p: str):
        """Regex that matches the first-use definition: 'long form (ABBR)'."""
        # Match singular or plural long form followed by (ABBR) or (ABBRs)
        lf_pat = f"(?:{re.escape(singular)}|{re.escape(plural)})"
        abbr_pat = f"(?:{re.escape(abbr_s)}s?|{re.escape(abbr_p)})"
        return re.compile(
            rf"({lf_pat})\s*\(({abbr_pat})\)",
            re.IGNORECASE
        )

    def _build_replacement_pattern(self, singular: str, plural: str):
        """Regex that matches long form occurrences (singular or plural)."""
        # Plural first to avoid partial matches
        return re.compile(
            rf"\b({re.escape(plural)}|{re.escape(singular)})\b",
            re.IGNORECASE
        )

    def process(self, text: str) -> str:
        """Process text line-by-line, preserving headings and code blocks."""
        lines = text.split("\n")
        result = []
        in_code  = False
        in_table = False  # tables — keep as-is for readability

        for line in lines:
            # Track fenced code blocks
            if line.strip().startswith("```"):
                in_code = not in_code
                result.append(line)
                continue
            if in_code:
                result.append(line)
                continue

            # Skip markdown headings (##, ###) — leave them unchanged
            if re.match(r"^#{1,4} ", line):
                result.append(line)
                continue

            # Process inline text
            line = self._process_line(line)
            result.append(line)

        return "\n".join(result)

    def _process_line(self, line: str) -> str:
        # Maps placeholder → original definition text so shorter terms can't
        # corrupt a longer term's first-use definition on the same line.
        placeholders: dict[str, str] = {}

        for singular, plural, abbr_s, abbr_p in self.abbrevs:
            key = abbr_s

            def_pat = self._build_definition_pattern(singular, plural, abbr_s, abbr_p)
            m = def_pat.search(line)
            if m:
                if key not in self.defined:
                    # First use: protect this span with a placeholder so shorter
                    # abbreviations processed later cannot corrupt the long form.
                    self.defined.add(key)
                    ph = f"\x00DEF_{key}\x00"
                    placeholders[ph] = m.group(0)
                    line = line[: m.start()] + ph + line[m.end() :]
                    # Fall through to Step 2 to replace any other occurrences of
                    # the same long form that appear later on this same line.
                else:
                    # Already defined: collapse "long form (ABBR)" → "ABBR".
                    line = def_pat.sub(lambda mx: mx.group(2), line)
                    # Fall through to Step 2 for any remaining bare long-form
                    # occurrences on this line.

            # Step 2: Replace bare long-form occurrences (runs even on the
            # definition line so same-line duplicates are abbreviated too).
            if key in self.defined:
                rep_pat = self._build_replacement_pattern(singular, plural)

                def smart_replace(m, _s=singular, _p=plural, _as=abbr_s, _ap=abbr_p):
                    matched = m.group(0)
                    is_plural = matched.lower() == _p.lower()
                    abbr = _ap if is_plural else _as
                    if matched[0].isupper():
                        abbr = abbr[0].upper() + abbr[1:]
                    return abbr

                line = rep_pat.sub(smart_replace, line)

        # Restore all protected first-use definition spans.
        for ph, original in placeholders.items():
            line = line.replace(ph, original)

        return line


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    text = PROPOSAL_PATH.read_text(encoding="utf-8")
    original_words = len(text.split())

    fixer = AbbreviationFixer(ABBREVS)
    fixed = fixer.process(text)

    # Count replacements made
    replacements = 0
    orig_lines = text.split("\n")
    fixed_lines = fixed.split("\n")
    for o, f in zip(orig_lines, fixed_lines):
        if o != f:
            replacements += 1

    PROPOSAL_PATH.write_text(fixed, encoding="utf-8")
    fixed_words = len(fixed.split())

    print(f"[OK] Abbreviations fixed: {replacements} lines changed")
    print(f"     Abbreviations defined: {len(fixer.defined)} ({', '.join(sorted(fixer.defined))})")
    print(f"     Word count: {original_words:,} -> {fixed_words:,}")
    print(f"     Output: {PROPOSAL_PATH}")


if __name__ == "__main__":
    main()
