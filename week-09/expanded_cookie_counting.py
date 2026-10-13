"""
cookie_counting.py
------------------
How many batches of cookies can we make?
Exploring all four counting scenarios using an example cookie lineup.
"""

import math
import itertools

# ─────────────────────────────────────────────────────────────────
#  An Example Cookie Lineup
# ─────────────────────────────────────────────────────────────────
cookies = [
    "Peanut Butter",
    "Raspberry White Choc",
    "Chocolate Chip",
    "Macadamia Nut",
    "Sugar Cookie",
    "Snickerdoodle",
    "PB Chocolate Chip",
    "S'mores Cookie",
    "Twix Ice Cream Cookie",
]

n = len(cookies)   # total varieties
k = 3              # ← change this to try different batch sizes!

# ─────────────────────────────────────────────────────────────────
#  Helper: print a labeled section header
# ─────────────────────────────────────────────────────────────────
def header(title):
    print(f"\n{'='*65}")
    print(f"  {title}")
    print(f"{'='*65}")

def show_sample(results, label="batch"):
    """Print first 5 results, then a count."""
    for item in results[:5]:
        print(f"     {item}")
    if len(results) > 5:
        print(f"     ... ({len(results)} total {label}s)")
    else:
        print(f"     ({len(results)} total {label}s)")


header(f"COOKIE COUNTING  |  n={n} varieties  |  k={k} per batch")

# ─────────────────────────────────────────────────────────────────
#  CASE 1 — Combination: order does NOT matter, NO repeats
#
#  Thinking: "I want k different flavors. AB == BA — same batch."
#  Formula:  C(n, k)  =  n! / (k! × (n-k)!)
#            Divide out k! because the chosen group can rearrange
#            itself k! ways — we already counted all of those.
# ─────────────────────────────────────────────────────────────────
print("\n📦  CASE 1: Combination  (order ✗, repeats ✗)")
print(f"   Formula : C(n,k)  =  n! / (k! × (n-k)!)")
print(f"           = {n}! / ({k}! × {n-k}!)")
print(f"           = {math.factorial(n):,} / ({math.factorial(k)} × {math.factorial(n-k):,})")
c = math.comb(n, k)
print(f"           = {c}")
show_sample(list(itertools.combinations(cookies, k)))

# ─────────────────────────────────────────────────────────────────
#  CASE 2 — Permutation: order DOES matter, NO repeats
#
#  Thinking: "Slot 1, Slot 2, Slot 3 are distinct positions.
#             AB ≠ BA — different batch."
#  Formula:  P(n, k)  =  n! / (n-k)!
#            Same as combinations × k!  (we keep all orderings)
# ─────────────────────────────────────────────────────────────────
print("\n🔢  CASE 2: Permutation  (order ✓, repeats ✗)")
print(f"   Formula : P(n,k)  =  n! / (n-k)!")
print(f"           = {n}! / {n-k}!")
print(f"           = {math.factorial(n):,} / {math.factorial(n-k):,}")
p = math.perm(n, k)
print(f"           = {p}")
print(f"   Check   : C × k! = {c} × {k}! = {c} × {math.factorial(k)} = {p}  ✓")
show_sample(list(itertools.permutations(cookies, k)))

# ─────────────────────────────────────────────────────────────────
#  CASE 3 — Combination WITH repetition: order ✗, repeats ✓
#
#  Thinking: "I can bake the same flavor twice (or three times).
#             But {PB, PB, Choc} == {Choc, PB, PB} — same batch."
#  Formula:  C(n+k-1, k)  — "stars and bars"
#            Imagine distributing k cookies among n bins.
# ─────────────────────────────────────────────────────────────────
print("\n♻️   CASE 3: Combination w/ repetition  (order ✗, repeats ✓)")
print(f"   Formula : C(n+k-1, k)  =  (n+k-1)! / (k! × (n-1)!)")
print(f"           = C({n}+{k}-1, {k})  =  C({n+k-1}, {k})")
print(f"           = {math.factorial(n+k-1):,} / ({math.factorial(k)} × {math.factorial(n-1):,})")
cr = math.comb(n + k - 1, k)
print(f"           = {cr}")
show_sample(list(itertools.combinations_with_replacement(cookies, k)))

# ─────────────────────────────────────────────────────────────────
#  CASE 4 — Permutation WITH repetition: order ✓, repeats ✓
#
#  Thinking: "Every slot is independent. Each slot has n choices.
#             Do that k times."
#  Formula:  n^k
#            The simplest one! No factorial needed.
# ─────────────────────────────────────────────────────────────────
print("\n🔁  CASE 4: Permutation w/ repetition  (order ✓, repeats ✓)")
print(f"   Formula : n^k  =  {n}^{k}  =  {n**k}")
pr = n ** k
show_sample(list(itertools.product(cookies, repeat=k)))

# ─────────────────────────────────────────────────────────────────
#  SUMMARY TABLE
# ─────────────────────────────────────────────────────────────────
header(f"SUMMARY  (n={n} cookie varieties,  k={k} per batch)")
rows = [
    ("Combination      (order ✗, repeat ✗)", f"C(n,k)     = n!/(k!(n-k)!)", c),
    ("Permutation      (order ✓, repeat ✗)", f"P(n,k)     = n!/(n-k)!",     p),
    ("Combo w/ repeat  (order ✗, repeat ✓)", f"C(n+k-1,k) = stars&bars",    cr),
    ("Perm  w/ repeat  (order ✓, repeat ✓)", f"n^k        = {n}^{k}",        pr),
]
print(f"\n  {'Scenario':<42} {'Formula':<30} {'Count':>8}")
print(f"  {'-'*42} {'-'*30} {'-'*8}")
for label, formula, count in rows:
    print(f"  {label:<42} {formula:<30} {count:>8,}")
print()

# ─────────────────────────────────────────────────────────────────
#  BONUS: The relationship between all four cases
# ─────────────────────────────────────────────────────────────────
print("  KEY RELATIONSHIP:")
print(f"  Permutation = Combination × k!")
print(f"  {p} = {c} × {math.factorial(k)}   (no-repeat cases)")
print(f"\n  Adding repeats always INCREASES the count:")
print(f"  Combo no-repeat ({c}) → Combo w/repeat ({cr})")
print(f"  Perm  no-repeat ({p}) → Perm  w/repeat ({pr})")
print()
