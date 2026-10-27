#!/usr/bin/env python3
"""Brute-force checks for every count/example claimed in the Week 11 decks."""
from itertools import product, combinations

def props(R, S):
    refl = all((a, a) in R for a in S)
    sym = all((b, a) in R for (a, b) in R)
    anti = all(a == b for (a, b) in R if (b, a) in R)
    trans = all((a, d) in R for (a, b) in R for (c, d) in R if b == c)
    return refl, sym, anti, trans

def count(n):
    S = range(n); P = [(a, b) for a in S for b in S]
    tot = eq = po = 0
    for bits in product([0, 1], repeat=len(P)):
        R = {p for p, x in zip(P, bits) if x}
        r, s, a, t = props(R, S); tot += 1
        eq += r and s and t; po += r and a and t
    return tot, eq, po

for n in (2, 3, 4):
    print("n=%d total, equivalences, partial orders:" % n, count(n))

S = [1, 2, 3, 6]; R = {(a, b) for a in S for b in S if b % a == 0}
print("divisibility on", S, sorted(R), len(R), "pairs")
print("refl,sym,anti,trans =", props(R, S))
print("(2,6) in R", (2, 6) in R, "(6,2) in R", (6, 2) in R)
M2 = {(a, b) for a in S for b in S if a % 2 == b % 2}
print("same parity on", S, "props", props(M2, S))
S12 = range(12); M4 = {(a, b) for a in S12 for b in S12 if a % 4 == b % 4}
print("mod 4 bins:", [[x for x in S12 if x % 4 == r] for r in range(4)], "props", props(M4, S12))
# both / neither examples from Tue note
print("both sym+anti {(1,1),(2,2)}:", props({(1,1),(2,2)}, [1,2]))
print("neither {(1,2),(2,1),(1,3)}:", props({(1,2),(2,1),(1,3)}, [1,2,3]))
