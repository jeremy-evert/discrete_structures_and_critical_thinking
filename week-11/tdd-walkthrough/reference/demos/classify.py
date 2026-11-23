from properties import reflexive, symmetric, antisymmetric, transitive
from seating import ITEMS, SITS_NEXT_TO


def rows():
    students = [("Ana", 1), ("Ben", 1), ("Cy", 2), ("Dee", 2), ("Eli", 3), ("Fay", 3)]
    n12, n6 = list(range(1, 13)), list(range(1, 7))
    return [
        ("same birthday month", students, {(a, b) for a in students for b in students if a[1] == b[1]}),
        ("a divides b (1..12)", n12, {(a, b) for a in n12 for b in n12 if b % a == 0}),
        ("a <= b (1..6)", n6, {(a, b) for a in n6 for b in n6 if a <= b}),
        ("sits next to", ITEMS, SITS_NEXT_TO),
        ("a < b (1..6)", n6, {(a, b) for a in n6 for b in n6 if a < b}),
    ]


if __name__ == "__main__":
    print("%-22s %-5s %-5s %-5s %-5s %s" % ("relation", "refl", "symm", "anti", "trans", "verdict"))
    for name, items, pairs in rows():
        r, s, a, t = (f(items, pairs) is None for f in (reflexive, symmetric, antisymmetric, transitive))
        verdict = "equivalence" if r and s and t else "partial order" if r and a and t else "neither"
        yn = lambda x: "yes" if x else "no"
        print("%-22s %-5s %-5s %-5s %-5s %s" % (name, yn(r), yn(s), yn(a), yn(t), verdict))
