#!/usr/bin/env python3
"""Run every example and claim in relations_test_first_concepts.md.

Standard library only, Python 3.9+. Usage:  python3 relations_test_first_check.py [concepts.md]
Exits 0 only if every stated expected result is correct.

What it checks:
  1. Every ```case block in the sheet: all seven expected True/False results, every
     stated witness (it must really break the property), and that each pair uses only
     listed items.
  2. Coverage: each taught property has at least one demo that passes and one that fails
     (reflexive, symmetric, antisymmetric, transitive; asymmetric, equivalence and partial order too).
  3. Drift: each one-line test shown in the sheet is the same expression the functions
     here return.
  4. The functions themselves, against a second, differently written reading of every
     definition, on all 512 relations over 3 items, plus the known counts for 3 items.
"""
import itertools
import os
import re
import sys

PROPERTIES = ["reflexive", "symmetric", "antisymmetric", "transitive",
              "asymmetric", "equivalence", "partial_order"]
TAUGHT = ["reflexive", "symmetric", "antisymmetric", "transitive"]


# ---- the tests (the sheet shows each expression; check 3 compares them) -------------

def is_reflexive(items, pairs):
    return all((a, a) in pairs for a in items)


def is_symmetric(items, pairs):
    return all((b, a) in pairs for (a, b) in pairs)


def is_antisymmetric(items, pairs):
    return all(a == b for (a, b) in pairs if (b, a) in pairs)


def is_transitive(items, pairs):
    return all((a, d) in pairs for (a, b) in pairs for (c, d) in pairs if b == c)


def is_asymmetric(items, pairs):
    return all((b, a) not in pairs for (a, b) in pairs)


def is_equivalence(items, pairs):
    return is_reflexive(items, pairs) and is_symmetric(items, pairs) and is_transitive(items, pairs)


def is_partial_order(items, pairs):
    return is_reflexive(items, pairs) and is_antisymmetric(items, pairs) and is_transitive(items, pairs)


TESTS = {
    "reflexive": is_reflexive, "symmetric": is_symmetric,
    "antisymmetric": is_antisymmetric, "transitive": is_transitive,
    "asymmetric": is_asymmetric, "equivalence": is_equivalence,
    "partial_order": is_partial_order,
}


def breaks(prop, w, items, pairs):
    """True if witness w really breaks the property."""
    if prop == "reflexive":
        return len(w) == 1 and w[0] in items and (w[0], w[0]) not in pairs
    if prop == "symmetric":
        return len(w) == 2 and w in pairs and (w[1], w[0]) not in pairs
    if prop == "antisymmetric":
        return len(w) == 2 and w[0] != w[1] and w in pairs and (w[1], w[0]) in pairs
    if prop == "transitive":
        return (len(w) == 3 and (w[0], w[1]) in pairs and (w[1], w[2]) in pairs
                and (w[0], w[2]) not in pairs)
    if prop == "asymmetric":
        return len(w) == 2 and w in pairs and (w[1], w[0]) in pairs
    return False


# ---- parsing the sheet -----------------------------------------------------------

def parse_cases(text):
    cases = []
    for block in re.findall(r"```case\n(.*?)```", text, re.S):
        c = {}
        for line in block.strip().splitlines():
            key, _, val = line.partition(":")
            c[key.strip()] = val.strip()
        cases.append(c)
    return cases


def kv(s):
    out = {}
    for tok in s.split():
        k, _, v = tok.partition("=")
        out[k] = v
    return out


# ---- checks ----------------------------------------------------------------------

class Report:
    def __init__(self):
        self.ok = 0
        self.bad = []

    def check(self, cond, msg):
        if cond:
            self.ok += 1
        else:
            self.bad.append(msg)


def check_cases(text, rep):
    cases = parse_cases(text)
    ids = [c.get("id") for c in cases]
    rep.check(len(set(ids)) == len(ids), "duplicate case ids: %r" % ids)
    demos = {p: {"pass": [], "fail": []} for p in PROPERTIES}
    witnesses = 0
    for c in cases:
        cid = c.get("id", "?")
        items = c["items"].split()
        pairs = set()
        for tok in c["pairs"].split():
            a, _, b = tok.partition("->")
            rep.check(a in items and b in items, "%s: pair %s uses an unlisted item" % (cid, tok))
            pairs.add((a, b))
        exp = kv(c["expect"])
        rep.check(sorted(exp) == sorted(PROPERTIES), "%s: expect must list all of %s" % (cid, PROPERTIES))
        for p in PROPERTIES:
            want = exp.get(p) == "T"
            got = TESTS[p](items, pairs)
            rep.check(got == want, "%s: %s stated %s, test gives %s" % (cid, p, want, got))
        for p, w in kv(c.get("witness", "")).items():
            wt = tuple(w.split(","))
            witnesses += 1
            rep.check(p in TESTS and not TESTS[p](items, pairs),
                      "%s: witness for %s but the property holds" % (cid, p))
            rep.check(breaks(p, wt, items, pairs), "%s: %s is not a real witness for %s" % (cid, w, p))
        for p, kind in kv(c.get("demo", "")).items():
            rep.check(kind in ("pass", "fail") and p in demos, "%s: bad demo %s=%s" % (cid, p, kind))
            if kind in ("pass", "fail") and p in demos:
                demos[p][kind].append(cid)
                rep.check(TESTS[p](items, pairs) == (kind == "pass"),
                          "%s: demo %s=%s contradicts the test" % (cid, p, kind))
        # every failing taught property in a demo case must come with a witness
        for p, kind in kv(c.get("demo", "")).items():
            if kind == "fail" and p in ("reflexive", "symmetric", "antisymmetric", "transitive", "asymmetric"):
                rep.check(p in kv(c.get("witness", "")), "%s: failing demo %s has no witness" % (cid, p))
    for p in ("reflexive", "symmetric", "antisymmetric", "transitive", "asymmetric", "equivalence", "partial_order"):
        rep.check(demos[p]["pass"], "no passing demo for %s" % p)
        rep.check(demos[p]["fail"], "no failing demo for %s" % p)
    return len(cases), witnesses, demos


def check_drift(text, rep):
    blocks = re.findall(r"```python\n(.*?)```", text, re.S)
    shown = "\n".join(blocks)
    import inspect
    for p in ("reflexive", "symmetric", "antisymmetric", "transitive", "asymmetric"):
        src = inspect.getsource(TESTS[p])
        expr = src.split("return ", 1)[1].strip()
        rep.check(expr in shown, "sheet does not show the exact test expression for %s: %s" % (p, expr))
    for name in ("is_equivalence", "is_partial_order"):
        rep.check(name in text, "sheet does not mention %s" % name)
    expr = inspect.getsource(is_partial_order).split("return ", 1)[1].strip()
    rep.check(expr in shown, "sheet does not show the exact partial-order test: %s" % expr)


def all_relations(n):
    items = list(range(n))
    cells = [(a, b) for a in items for b in items]
    for bits in itertools.product([0, 1], repeat=len(cells)):
        yield items, {c for c, bit in zip(cells, bits) if bit}


def second_reading(items, pairs):
    """Same five questions, written the long way (explicit loops over items, no shared idioms)."""
    refl = True
    for a in items:
        if (a, a) not in pairs:
            refl = False
    sym = True
    for a in items:
        for b in items:
            if (a, b) in pairs and (b, a) not in pairs:
                sym = False
    anti = True
    for a in items:
        for b in items:
            if a != b and (a, b) in pairs and (b, a) in pairs:
                anti = False
    trans = True
    for a in items:
        for b in items:
            for c in items:
                if (a, b) in pairs and (b, c) in pairs and (a, c) not in pairs:
                    trans = False
    asym = True
    for a in items:
        for b in items:
            if (a, b) in pairs and (b, a) in pairs:
                asym = False
    return refl, sym, anti, trans, asym


def check_exhaustive(rep):
    counts = {p: 0 for p in PROPERTIES}
    total = 0
    for items, pairs in all_relations(3):
        total += 1
        sr = second_reading(items, pairs)
        mine = (is_reflexive(items, pairs), is_symmetric(items, pairs), is_antisymmetric(items, pairs),
                is_transitive(items, pairs), is_asymmetric(items, pairs))
        rep.check(sr == mine, "two readings disagree on %r" % sorted(pairs))
        loops = any((a, a) in pairs for a in items)
        rep.check(is_asymmetric(items, pairs) == (is_antisymmetric(items, pairs) and not loops),
                  "asymmetric != antisymmetric and no loops on %r" % sorted(pairs))
        for p in PROPERTIES:
            if TESTS[p](items, pairs):
                counts[p] += 1
    # known counts of labelled relations on 3 items (independent of this code)
    known = {"reflexive": 64, "symmetric": 64, "antisymmetric": 216, "transitive": 171,
             "asymmetric": 27, "equivalence": 5, "partial_order": 19}
    for p, n in known.items():
        rep.check(counts[p] == n, "count of %s relations on 3 items is %d, expected %d" % (p, counts[p], n))
    return total, counts


def main(argv):
    here = os.path.dirname(os.path.abspath(__file__))
    path = argv[1] if len(argv) > 1 else os.path.join(here, "relations_test_first_concepts.md")
    with open(path, encoding="utf-8") as f:
        text = f.read()
    rep = Report()
    ncases, nwit, demos = check_cases(text, rep)
    check_drift(text, rep)
    total, counts = check_exhaustive(rep)
    print("sheet: %s" % os.path.basename(path))
    print("cases parsed: %d   witnesses verified: %d" % (ncases, nwit))
    for p in PROPERTIES:
        d = demos[p]
        print("  %-14s pass demos: %-28s fail demos: %s" % (p, ",".join(d["pass"]) or "-", ",".join(d["fail"]) or "-"))
    print("exhaustive: %d relations on 3 items; counts %s" % (total, ", ".join("%s=%d" % (p, counts[p]) for p in PROPERTIES)))
    print("assertions passed: %d   failed: %d" % (rep.ok, len(rep.bad)))
    for m in rep.bad:
        print("FAIL: " + m)
    if rep.bad:
        print("CHECKS FAILED")
        return 1
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
