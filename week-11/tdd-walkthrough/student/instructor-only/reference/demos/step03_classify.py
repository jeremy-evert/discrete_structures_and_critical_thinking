"""Step 03: classify five relations as equivalence, partial order, or neither."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tests"))
from relations import antisymmetric_failure, reflexive_failure, symmetric_failure, transitive_failure

ARTIST = {"Slow Orbit": "Lantern Hill", "Slow Orbit Remix": "Lantern Hill", "Paper Moons": "Moss & Marrow",
          "Glass Harbor": "Moss & Marrow"}
TITLES = ["Slow Orbit", "Slow Orbit Remix", "Paper Moons", "Glass Harbor"]
LENGTHS = [180, 200, 240, 300]
LONGER = [180, 210, 240, 270]
QUEUE = ["Slow Orbit", "Paper Moons", "Glass Harbor", "Night Bus"]

RELATIONS = [
    ("shares an artist with", TITLES, lambda a, b: ARTIST[a] == ARTIST[b]),
    ("is no longer than", LENGTHS, lambda a, b: a <= b),
    ("title starts with the other's title", TITLES, lambda a, b: b.startswith(a)),
    ("is exactly 30 seconds longer than", LONGER, lambda a, b: b - a == 30),
    ("plays right after", QUEUE, lambda a, b: QUEUE.index(b) == QUEUE.index(a) + 1),
]

print("{0:<38}{1:<6}{2:<6}{3:<6}{4:<6}{5}".format("relation", "refl", "sym", "anti", "trans", "verdict"))
for name, items, rel in RELATIONS:
    r = reflexive_failure(rel, items) is None
    s = symmetric_failure(rel, items) is None
    a = antisymmetric_failure(rel, items) is None
    t = transitive_failure(rel, items) is None
    verdict = "equivalence" if (r and s and t) else "partial order" if (r and a and t) else "neither"
    print("{0:<38}{1:<6}{2:<6}{3:<6}{4:<6}{5}".format(name, *["yes" if x else "NO" for x in (r, s, a, t)], verdict))
