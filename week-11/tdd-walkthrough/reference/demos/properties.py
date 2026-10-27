from itertools import product


def reflexive(items, pairs):
    for a in items:
        if (a, a) not in pairs:
            return (a,)
    return None


def symmetric(items, pairs):
    for a, b in product(items, repeat=2):
        if (a, b) in pairs and (b, a) not in pairs:
            return (a, b)
    return None


def antisymmetric(items, pairs):
    for a, b in product(items, repeat=2):
        if a != b and (a, b) in pairs and (b, a) in pairs:
            return (a, b)
    return None


def transitive(items, pairs):
    for a, b, c in product(items, repeat=3):
        if (a, b) in pairs and (b, c) in pairs and (a, c) not in pairs:
            return (a, b, c)
    return None


def report(title, items, pairs):
    print(title)
    for name, check in [("reflexive", reflexive), ("symmetric", symmetric),
                        ("antisymmetric", antisymmetric), ("transitive", transitive)]:
        w = check(items, pairs)
        print("  %-14s %s" % (name, "holds" if w is None else "FAILS  witness: " + ", ".join(map(str, w))))


if __name__ == "__main__":
    from seating import ITEMS, SITS_NEXT_TO
    report("sits next to", ITEMS, SITS_NEXT_TO)
    nums = list(range(1, 13))
    report("divides (1..12)", nums, {(a, b) for a in nums for b in nums if b % a == 0})
