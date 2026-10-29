#!/usr/bin/env python3
"""
properties.py  -  COMSC 2043 DSCT, Week 11: Relations in Your Tests

THE STORY: THE CLASSROOM INSPECTOR
==================================

Every relation in this file is just a bag of ordered pairs:
"who is linked to whom". The inspector does not trust the bag.
She walks the room with four questions on a clipboard. For each
question she either says "holds", or she points at ONE concrete
item, pair or triple and says "THIS is why not."

That pointed-at thing is called a WITNESS. A witness is the most
useful thing a failing test can give you, because it turns
"something is wrong" into "here is exactly what is wrong".


QUESTION 1: REFLEXIVE  "Is every item linked to itself?"
--------------------------------------------------------
    Check:   for every a, is (a, a) in the bag?
    Witness: the first ITEM a with no (a, a).

    Real life, HOLDS:
        "has the same birthday as"  - you share your own birthday.
        "is as tall as or taller than" - you are as tall as you.
        "x == x" in code - a value should equal itself.
    Real life, FAILS:
        "sits next to"  - you do not sit next to yourself.
        "is the parent of" - nobody is their own parent.
        float("nan") == float("nan") is False in Python. This is a real
        bug source: a NaN in a list cannot be found with `in` or `==`.


QUESTION 2: SYMMETRIC  "Does every link work both ways?"
-------------------------------------------------------
    Check:   whenever (a, b) is in the bag, is (b, a) in it too?
    Witness: the first PAIR (a, b) whose reverse is missing.

    Real life, HOLDS:
        "is married to", "sits next to", "is a Facebook friend of".
    Real life, FAILS:
        "follows on Instagram" - you can follow a celebrity who
        does not follow you back.
        "owes money to", "is the parent of".
    Why it matters in code: a buggy equality check like
    a.lower() == b  says "Bob" matches "bob" but "bob" does not
    match "Bob". Whether a link is one-way or two-way is a real
    design decision (Twitter "follow" vs Facebook "friend").


QUESTION 3: ANTISYMMETRIC  "Do two-way links only happen to yourself?"
---------------------------------------------------------------------
    Check:   if (a, b) AND (b, a) are both in the bag, is a == b?
    Witness: the first PAIR (a, b) of DIFFERENT items linked both ways.

    This is NOT "the opposite of symmetric". It is a separate rule
    about ranking. It says: two different things cannot both come
    before each other.

    Real life, HOLDS:
        "is at most as old as" (<=) - if I am <= you and you are
        <= me, we are the same age... for numbers that means the same
        number.
        "divides", "is a prerequisite of (or equal to)",
        "is a folder inside (or equal to)".
    Real life, FAILS:
        "sits next to" - Ana and Ben are linked both ways but are
        different people.
        Software versions compared by number: "1.0" <= "1.0.0" and
        "1.0.0" <= "1.0", yet the strings differ. Sorting and "which
        is newer?" logic gets confused.


QUESTION 4: TRANSITIVE  "Does every chain have a shortcut?"
----------------------------------------------------------
    Check:   whenever (a, b) and (b, c) are in the bag, is (a, c)?
    Witness: the first TRIPLE (a, b, c) where the shortcut is missing.

    Real life, HOLDS:
        "is older than", "is an ancestor of", "is in the same
        class section as", "divides".
    Real life, FAILS:
        "is a friend of" - your friend's friend may be a stranger.
        Rock-paper-scissors "beats" - rock beats scissors, scissors
        beats paper, but rock does NOT beat paper.
    Why it matters in code: sort() assumes its comparison is
    transitive. Give it one that is not and the result can change
    depending on the starting order.

    A sneaky witness: a chain can go out and come BACK.
    Ana -> Ben -> Ana needs the shortcut Ana -> Ana. So any relation
    that is symmetric but not reflexive is also not transitive.
    Watch for that in the output below.


PUTTING THE ANSWERS TOGETHER
============================
    reflexive + symmetric     + transitive  = EQUIVALENCE RELATION
        Sorts things into groups. "same birthday", "same email after
        lowercasing", Python's == on well-behaved values.

    reflexive + antisymmetric + transitive  = PARTIAL ORDER
        A "comes before" where some pairs have no order.
        Course prerequisites, build steps, "divides".
        3 and 5: neither divides the other, so there is no order
        between them. That is the "partial" part.

Run:  python3 properties.py
"""

from seating import ITEMS, SITS_NEXT_TO


# ---------------------------------------------------------------
# THE FOUR QUESTIONS
# Each one returns None when the property holds.
# Otherwise it returns the FIRST witness, trying items in the
# order they appear in `items`. Same input, same witness, every run.
# ---------------------------------------------------------------

def reflexive(items, pairs):
    """Every item linked to itself. Witness: an item."""
    for a in items:
        if (a, a) not in pairs:
            return a
    return None


def symmetric(items, pairs):
    """Every link works both ways. Witness: a one-way pair (a, b)."""
    for a in items:
        for b in items:
            if (a, b) in pairs and (b, a) not in pairs:
                return (a, b)
    return None


def antisymmetric(items, pairs):
    """Two-way links only from an item to itself. Witness: (a, b) with a != b."""
    for a in items:
        for b in items:
            if a != b and (a, b) in pairs and (b, a) in pairs:
                return (a, b)
    return None


def transitive(items, pairs):
    """Every chain a->b->c has the shortcut a->c. Witness: (a, b, c)."""
    for a in items:
        for b in items:
            if (a, b) not in pairs:
                continue
            for c in items:
                if (b, c) in pairs and (a, c) not in pairs:
                    return (a, b, c)
    return None


PROPERTY_CHECKS = [reflexive, symmetric, antisymmetric, transitive]


# ---------------------------------------------------------------
# THE INSPECTOR'S REPORT
# ---------------------------------------------------------------

def describe_witness(witness):
    """Show a witness the way we write it on the board: Ana or (Ana, Ben)."""
    if isinstance(witness, tuple):
        return "(" + ", ".join(str(part) for part in witness) + ")"
    return str(witness)


def report(title, items, pairs):
    print(f"=== {title} ===")
    for check in PROPERTY_CHECKS:
        witness = check(items, pairs)
        if witness is None:
            result = "holds"
        else:
            result = f"FAILS witness: {describe_witness(witness)}"
        print(f"   {check.__name__:<14} {result}")
    print()


if __name__ == "__main__":
    # (a) The seating row from seating.py: Ana - Ben - Cy - Dee - Eli
    report("sits next to", ITEMS, SITS_NEXT_TO)

    # (b) "a divides b" on 1..12, meaning b % a == 0.
    #     (2, 6) is in: 2 divides 6.   (6, 2) is out: 6 does not divide 2.
    numbers = list(range(1, 13))
    divides_pairs = {(a, b) for a in numbers for b in numbers if b % a == 0}
    report("divides on 1..12", numbers, divides_pairs)