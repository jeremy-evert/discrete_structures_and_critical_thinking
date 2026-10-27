#!/usr/bin/env python3
"""Recompute every number/example used in week11_thu_pair_reasoning.tex."""
from itertools import product, permutations
from fractions import Fraction

def props(R, S):
    refl = all((a, a) in R for a in S)
    sym = all((b, a) in R for (a, b) in R)
    anti = all(a == b for (a, b) in R if (b, a) in R)
    trans = all((a, d) in R for (a, b) in R for (c, d) in R if b == c)
    return refl, sym, anti, trans

# 1. Nontransitive dice (Efron-style, six faces each)
A = [2, 2, 4, 4, 9, 9]; B = [1, 1, 6, 6, 8, 8]; C = [3, 3, 5, 5, 7, 7]
def win(X, Y):
    w = sum(x > y for x in X for y in Y); t = sum(x == y for x in X for y in Y)
    return w, t, 36
for n, (X, Y) in {"A>B": (A, B), "B>C": (B, C), "C>A": (C, A)}.items():
    w, t, tot = win(X, Y); print("dice", n, "wins", w, "ties", t, "of", tot, "=", Fraction(w, tot))
print("means", [sum(d) / 6 for d in (A, B, C)])
dice = {"A": A, "B": B, "C": C}; S = list(dice)
beats = {(x, y) for x in S for y in S if x != y and win(dice[x], dice[y])[0] > win(dice[y], dice[x])[0]}
print("beats relation", sorted(beats), "props (refl,sym,anti,trans):", props(beats, S))
# Best reply to a rival who picks first: for each pick, who beats it
print("every die has a better reply:", all(any((y, x) in beats for y in S) for x in S))

# 2. Prerequisite deadlock: 3 courses, requires-cycle
cyc = {("Alg", "DS"), ("DS", "Sys"), ("Sys", "Alg")}
courses = ["Alg", "DS", "Sys"]
orders = [p for p in permutations(courses) if all(p.index(a) < p.index(b) for a, b in cyc)]
print("valid take-orders with cycle Alg<DS<Sys<Alg:", len(orders))
chain = {("Alg", "DS"), ("DS", "Sys")}
print("valid orders for chain Alg<DS<Sys:", len([p for p in permutations(courses) if all(p.index(a) < p.index(b) for a, b in chain)]))
diamond = {("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")}
print("valid orders for diamond A<B,C<D:", len([p for p in permutations("ABCD") if all(p.index(a) < p.index(b) for a, b in diamond)]))

# 3. Counting relations on a 3-set with property filters
S3 = range(3); P = [(a, b) for a in S3 for b in S3]
cnt = dict(total=0, refl=0, sym=0, refl_sym=0, sym_anti=0, eq=0, po=0, neither_sym_anti=0)
for bits in product([0, 1], repeat=9):
    R = {p for p, x in zip(P, bits) if x}; r, s, a, t = props(R, S3)
    cnt["total"] += 1; cnt["refl"] += r; cnt["sym"] += s; cnt["refl_sym"] += r and s
    cnt["sym_anti"] += s and a; cnt["eq"] += r and s and t; cnt["po"] += r and a and t
    cnt["neither_sym_anti"] += (not s) and (not a)
print("relations on 3 elements:", cnt)
print("formulas: 2^9 =", 2**9, " reflexive 2^6 =", 2**6, " symmetric 2^6 =", 2**6, " refl+sym 2^3 =", 2**3)

# 4. Worked classifier example: S={1,2,3,4}
S4 = [1, 2, 3, 4]
R = {(1,1),(2,2),(3,3),(4,4),(1,2),(2,1),(2,3),(3,2)}
print("worked R:", sorted(R), "props:", props(R, S4))
wit = [((a,b),(b2,c)) for (a,b) in R for (b2,c) in R if b == b2 and (a,c) not in R]
print("transitivity violations (chain -> missing pair):", [(x, (x[0][0], x[1][1])) for x in wit])
# smallest repair: transitive closure
Rc = set(R)
while True:
    new = {(a, d) for (a, b) in Rc for (c, d) in Rc if b == c} - Rc
    if not new: break
    Rc |= new
print("added by transitive closure:", sorted(Rc - R), "-> props:", props(Rc, S4))
blocks = sorted({frozenset(y for (x, y) in Rc if x == a) for a in S4}, key=min)
print("equivalence classes after repair:", [sorted(b) for b in blocks])
# Partner's claim "R is an equivalence" - challenge is one witness: chain (1,2),(2,3) without (1,3)
# Alternative claim: "R is a partial order" - witness (1,2),(2,1) with 1 != 2
print("claim 'partial order' broken by:", [(a, b) for (a, b) in R if a != b and (b, a) in R][:1])
# Matrix of R
print("matrix of R:")
for a in S4: print(" ", [1 if (a, b) in R else 0 for b in S4])
