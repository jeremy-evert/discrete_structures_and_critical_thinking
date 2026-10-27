"""Tiny relation checkers. Each returns a concrete witness (a counterexample) or None.

A "relation" here is just a function rel(a, b) -> bool, plus a list of items to try.
"""
from itertools import product


def reflexive_failure(rel, items):
    for a in items:
        if not rel(a, a):
            return (a,)
    return None


def symmetric_failure(rel, items):
    for a, b in product(items, repeat=2):
        if rel(a, b) and not rel(b, a):
            return (a, b)
    return None


def antisymmetric_failure(rel, items):
    """rel(a,b) and rel(b,a) but a != b."""
    for a, b in product(items, repeat=2):
        if a != b and rel(a, b) and rel(b, a):
            return (a, b)
    return None


def transitive_failure(rel, items):
    for a, b, c in product(items, repeat=3):
        if rel(a, b) and rel(b, c) and not rel(a, c):
            return (a, b, c)
    return None
