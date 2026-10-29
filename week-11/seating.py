#!/usr/bin/env python3
"""
demos/seating.py  -  COMSC 2043 DSCT, Week 11: Relations in Your Tests

THE BIG IDEA, IN PLAIN WORDS
============================

Five students sit in one row, in this order:

    +-----+   +-----+   +-----+   +-----+   +-----+
    | Ana |---| Ben |---| Cy  |---| Dee |---| Eli |
    +-----+   +-----+   +-----+   +-----+   +-----+

A RELATION is just a list of "who is linked to whom".
Here the link is "sits next to". That's all a relation is:
a set of pairs. No formulas, no magic.


THE VOCABULARY, ONE PHRASE AT A TIME
====================================

ORDERED PAIR  (a, b)
    Two things in a set ORDER. (a, b) reads "a is linked to b".
    (Ben, Cy) and (Cy, Ben) are DIFFERENT pairs, the same way
    the point (2, 6) is a different spot on a graph than (6, 2).
    It is NOT a set like {Ben, Cy}, where order does not matter.

RELATION
    A set of ordered pairs. It answers one yes/no question for
    every pair of items: "is a linked to b?"
    If (a, b) is in the set the answer is yes; otherwise no.
    It is NOT a function. A function gives each input exactly one
    output. Ben sits next to TWO people (Ana and Cy), and a relation
    is fine with that.

REFLEXIVE      "every item is linked to itself"
    For every a, the pair (a, a) is in the set.
    Does Ana sit next to Ana? No. So "sits next to" is NOT reflexive.
    Compare "is in the same row as": Ana IS in the same row as Ana,
    so that one IS reflexive.

SYMMETRIC      "every link works both ways"
    If (a, b) is in the set, then (b, a) is in it too.
    If Ben sits next to Cy, Cy sits next to Ben. So it IS symmetric.
    Compare "sits to the left of": Ana is left of Ben, but Ben is
    NOT left of Ana. That one is NOT symmetric.

ANTISYMMETRIC  "two-way links only happen from an item to itself"
    If (a, b) AND (b, a) are both in the set, then a and b must be
    the same item.
    This is NOT the opposite of symmetric. It is a different rule.
    "sits next to" has (Ben, Cy) and (Cy, Ben), and Ben is not Cy,
    so it is NOT antisymmetric.
    Compare "sits at or to the left of": the only way both
    a-before-b and b-before-a hold is if a IS b. That one IS
    antisymmetric.

TRANSITIVE     "a chain a -> b -> c always has the shortcut a -> c"
    Ana sits next to Ben, and Ben sits next to Cy...
    ...but Ana does NOT sit next to Cy. That is a broken chain.
    So "sits next to" is NOT transitive.
    Compare "sits in the same row": that one chains. Same row as
    Ben, Ben same row as Cy, so Ana is in the same row as Cy.

EQUIVALENCE RELATION = reflexive + symmetric + transitive
    It sorts items into groups (like "same row", "same major",
    "same email after lowercasing").
    "sits next to" is NOT one. It fails reflexive and transitive.
    The two failures are different. Not being reflexive is a small
    gap you could patch by adding (a, a). Not being transitive breaks
    the idea of a group, because neighbors of neighbors are not
    neighbors.

PARTIAL ORDER = reflexive + antisymmetric + transitive
    A "comes before" relation where some pairs might have no order.
    Example: course prerequisites (CS1 before CS2, but Art and
    Physics have no order between them).
    "sits next to" is NOT one: it is symmetric where a partial order
    must be antisymmetric.

PROPERTY TEST
    A test that checks one of the rules above over EVERY item, not
    just one hand-picked example.

WITNESS
    The concrete pair or triple that proves a "no". It is a
    counterexample you can print, for example:
        transitive? NO, witness = (Ana, Ben, Cy)

CANONICAL KEY
    One standard spelling every variant gets rewritten to before
    comparing ("  ANA " -> "ana"). It is how you build an
    equivalence relation on purpose.

DEPENDENCY / CYCLE
    "a needs b" is a relation, too. A cycle is a chain that loops
    back: a needs b, b needs a. Cycles break partial orders and
    cause circular-import errors.


WHY ANY OF THIS MATTERS FOR SOFTWARE
====================================
    * __eq__ must be an equivalence relation, or `in`, sets, and
      dicts quietly misbehave.
    * Sort comparators must act like orders (transitive!), or
      sort() gives inconsistent results.
    * Build tools and package managers need dependencies to form a
      partial order with no cycles.
    * Social graphs ("follows" vs "is friends with") are relations,
      and symmetric or not is a real design decision.


HOW THIS FILE SHOWS THE RELATION THREE WAYS
===========================================
    1. As a SET of pairs   -> what the math definition says
    2. As a MATRIX of 0/1  -> where you can SEE the properties
    3. As a DIGRAPH        -> who points to whom (an adjacency list)

Run:  python3 demos/seating.py
"""


# ---------------------------------------------------------------
# THE ITEMS
# A list, because the ORDER matters: it is the seating order, and
# it fixes the row/column order of the matrix below.
# ---------------------------------------------------------------
ITEMS = ["Ana", "Ben", "Cy", "Dee", "Eli"]


# ---------------------------------------------------------------
# THE RELATION: "sits next to"
#
# Picture the row:   Ana - Ben - Cy - Dee - Eli
#
# There are 4 physical "touches" between seats. Each touch becomes
# TWO ordered pairs, one for each direction, because an ordered
# pair only points ONE way:
#
#     Ana ---> Ben     (Ana, Ben)
#     Ana <--- Ben     (Ben, Ana)
#
# 4 touches x 2 directions = 8 ordered pairs.
#
# Writing both directions by hand is what makes this relation
# SYMMETRIC. Forgetting one would be a bug, and a symmetric
# property test would catch it with a witness like (Ana, Ben).
# ---------------------------------------------------------------
SITS_NEXT_TO = {
    ("Ana", "Ben"), ("Ben", "Ana"),
    ("Ben", "Cy"),  ("Cy", "Ben"),
    ("Cy", "Dee"),  ("Dee", "Cy"),
    ("Dee", "Eli"), ("Eli", "Dee"),
}

# What this set does NOT contain is just as important:
#   ("Ana", "Ana")  -> missing, so the relation is NOT reflexive
#   ("Ana", "Cy")   -> missing, so the chain Ana->Ben->Cy has no
#                      shortcut, and the relation is NOT transitive


def is_related(first_student, second_student):
    """The relation as a yes/no question: is (first, second) in the set?"""
    return (first_student, second_student) in SITS_NEXT_TO


# ---------------------------------------------------------------
# VIEW 1: THE PAIRS, SORTED
# A set has no order of its own, so we sort it to make the output
# the same every run. Sorting is for display only.
# ---------------------------------------------------------------
def print_sorted_pairs():
    print("1. SITS_NEXT_TO as ordered pairs (sorted)")
    print(f"   {len(SITS_NEXT_TO)} pairs:")
    for first_student, second_student in sorted(SITS_NEXT_TO):
        print(f"   ({first_student}, {second_student})")
    print()


# ---------------------------------------------------------------
# VIEW 2: THE MATRIX
#
# Row = first item of the pair (the "from").
# Column = second item (the "to").
# Cell is 1 if (row, column) is in the relation, else 0.
#
# Where to LOOK in the matrix for each property:
#
#   REFLEXIVE       -> the main diagonal (top-left to bottom-right)
#                      must be ALL 1s.  Here it is all 0s.
#
#            Ana Ben Cy ...
#       Ana [ * ]
#       Ben     [ * ]
#       Cy          [ * ]      <- these cells
#
#   SYMMETRIC       -> the matrix is a MIRROR image across that
#                      diagonal: cell [r][c] == cell [c][r].
#
#   ANTISYMMETRIC   -> no off-diagonal cell has a 1 that is
#                      mirrored by another 1.
#
#   TRANSITIVE      -> harder to see by eye; that is exactly why
#                      we write property tests for it.
# ---------------------------------------------------------------
def print_matrix():
    print("2. Matrix (row -> column, 1 = sits next to)")
    column_width = 5
    header = " " * column_width + "".join(name.rjust(column_width) for name in ITEMS)
    print("   " + header)
    for row_student in ITEMS:
        cells = ""
        for column_student in ITEMS:
            bit = 1 if is_related(row_student, column_student) else 0
            cells += str(bit).rjust(column_width)
        print("   " + row_student.ljust(column_width) + cells)
    print()
    print("   Look: the diagonal is all 0  -> NOT reflexive.")
    print("   Look: it mirrors across the diagonal -> symmetric.")
    print("   Look: the 1s hug the diagonal -> a straight row of seats.")
    print()


# ---------------------------------------------------------------
# VIEW 3: THE DIGRAPH (directed graph) AS TEXT
#
# "Digraph" means each pair is an ARROW from first to second.
# Listing each student's arrows gives an "adjacency list", which is
# how most real programs store graphs (social networks, maps,
# import graphs).
#
# Because the relation is symmetric, every arrow has a partner
# going back, so it reads like a two-way street:
#
#     Ana <--> Ben <--> Cy <--> Dee <--> Eli
#
# Ends of the row (Ana, Eli) have 1 neighbor; the middle has 2.
# ---------------------------------------------------------------
def neighbors_of(student):
    """All students this student points to, in seating (ITEMS) order."""
    return [other for other in ITEMS if is_related(student, other)]


def print_digraph():
    print("3. Digraph as text (each student -> who they sit next to)")
    for student in ITEMS:
        print(f"   {student} -> {', '.join(neighbors_of(student))}")
    print()


if __name__ == "__main__":
    print_sorted_pairs()
    print_matrix()
    print_digraph()
