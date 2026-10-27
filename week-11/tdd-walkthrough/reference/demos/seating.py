ITEMS = ["Ana", "Ben", "Cy", "Dee", "Eli"]
_NEIGHBORS = [("Ana", "Ben"), ("Ben", "Cy"), ("Cy", "Dee"), ("Dee", "Eli")]
SITS_NEXT_TO = {(a, b) for a, b in _NEIGHBORS} | {(b, a) for a, b in _NEIGHBORS}

if __name__ == "__main__":
    print("pairs:", sorted(SITS_NEXT_TO))
    print()
    print("     " + " ".join("%-3s" % n for n in ITEMS))
    for a in ITEMS:
        print("%-4s " % a + " ".join("%-3d" % ((a, b) in SITS_NEXT_TO) for b in ITEMS))
    print()
    for a in ITEMS:
        print(a, "->", ", ".join(b for b in ITEMS if (a, b) in SITS_NEXT_TO))
