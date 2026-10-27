"""Witness finders. Each one hunts for a concrete counterexample to a property.

A "relation" here is just a function rel(a, b) that answers True or False.
Each finder returns the first counterexample it finds (a tuple), or None if
it finds none among the items you give it. None means "this property holds
for these items", which is good news.
"""
from itertools import product


def reflexive_failure(rel, items):
    """An item that is not related to itself."""
    for a in items:
        if not rel(a, a):
            return (a,)
    return None


def symmetric_failure(rel, items):
    """a is related to b, but b is not related to a."""
    for a, b in product(items, repeat=2):
        if rel(a, b) and not rel(b, a):
            return (a, b)
    return None


def antisymmetric_failure(rel, items):
    """Two different items that are each 'related' to the other."""
    for a, b in product(items, repeat=2):
        if a != b and rel(a, b) and rel(b, a):
            return (a, b)
    return None


def transitive_failure(rel, items):
    """a ~ b and b ~ c, but a is not related to c."""
    for a, b, c in product(items, repeat=3):
        if rel(a, b) and rel(b, c) and not rel(a, c):
            return (a, b, c)
    return None
