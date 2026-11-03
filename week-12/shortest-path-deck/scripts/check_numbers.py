#!/usr/bin/env python3
"""Fail if a slide number is stale or typed by hand.
 1. deck/numbers.tex and deck/table_*.tex must equal what the committed code computes now.
 2. Every \\N macro defined must be used on some slide (no dead numbers).
 3. Part files may not contain the deck's key numbers as bare literals (they must come from macros)."""
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root / "scripts"))
sys.path.insert(0, str(root / "code"))
import make_numbers as mn  # noqa: E402

deck = root / "deck"
bad = []
n = mn.build()
if (deck / "numbers.tex").read_text() != mn.render(n):
    bad.append("deck/numbers.tex is stale: run scripts/make_numbers.py")
D = mn.read_table(root / "data" / "distances.csv")
g, (best, _, _) = mn.greedy_tour(D), mn.brute_force(D)
for name, t in (("plain", None), ("nat", [1, 2, 3, 4, 5, 6]), ("greedy", g), ("best", best)):
    if (deck / f"table_{name}.tex").read_text() != mn.table_tex(D, t):
        bad.append(f"deck/table_{name}.tex is stale")
body = "".join(p.read_text() for p in sorted(deck.glob("part*.tex")))
for k in n:
    if "\\" + mn.macro_name(k) not in body and not k.endswith("raw"):
        bad.append(f"macro \\{mn.macro_name(k)} defined but unused")
# literals that must only appear through macros (strip macros and \note text first is NOT done: notes count too)
stripped = re.sub(r"\\N[A-Za-z]+", "", body)
key = {str(n["TotalNat"]), str(n["TotalRev"]), str(n["GreedyTotal"]), str(n["BestTotal"]), "87", "362", "24.2"}
for lit in sorted(key):
    for m in re.finditer(r"(?<![\d.,])" + re.escape(lit) + r"(?![\d])", stripped):
        line = stripped.count("\n", 0, m.start()) + 1
        bad.append(f"bare literal {lit} in part files (stripped line {line}); use the macro")
if bad:
    print("\n".join(bad))
    sys.exit(1)
print(f"numbers consistent: {len(n)} macros, 4 tables, no bare key literals")
