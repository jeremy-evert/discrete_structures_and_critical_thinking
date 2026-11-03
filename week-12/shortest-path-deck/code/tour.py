"""Shortest-path (closed tour) toolkit for the Week 12 deck. Cities are numbered 1..n."""
import csv
import itertools
import math
import random
from pathlib import Path

DEFAULT_TABLE = Path(__file__).resolve().parent.parent / "data" / "distances.csv"


def read_table(path=DEFAULT_TABLE):
    """Return {(from, to): distance}; the diagonal is blank and is skipped."""
    dist = {}
    with open(path, newline="") as f:
        rows = list(csv.reader(f))
    cols = [int(c) for c in rows[0][1:]]
    for row in rows[1:]:
        a = int(row[0])
        for b, cell in zip(cols, row[1:]):
            if cell != "":
                dist[(a, b)] = int(cell)
    return dist


def tour_length(tour, dist):
    """Total length of the closed tour: each leg, then the leg back to the start."""
    return sum(dist[(tour[i], tour[(i + 1) % len(tour)])] for i in range(len(tour)))


def legs(tour, dist):
    return [(tour[i], tour[(i + 1) % len(tour)], dist[(tour[i], tour[(i + 1) % len(tour)])])
            for i in range(len(tour))]


def greedy_tour(dist, start=1):
    """Always go to the nearest unvisited city (ties: lowest city number)."""
    cities = sorted({a for a, _ in dist})
    tour, left = [start], set(cities) - {start}
    while left:
        here = tour[-1]
        nxt = min(left, key=lambda c: (dist[(here, c)], c))
        tour.append(nxt)
        left.remove(nxt)
    return tour


def guess_tour(dist, rng, start=1):
    """Roll for the next city; a repeat is rejected and rolled again. Returns (tour, rolls)."""
    cities = sorted({a for a, _ in dist})
    tour, rolls = [start], []
    while len(tour) < len(cities):
        pick = rng.choice(cities)
        rolls.append(pick)
        if pick not in tour:
            tour.append(pick)
    return tour, rolls


def guess_and_check(dist, k, seed=0, start=1, with_rolls=False):
    """k random tours; returns list of (tour, total, best_so_far_total)
    (plus the die rolls, rejected ones included, when with_rolls=True)."""
    rng = random.Random(seed)
    out, best = [], math.inf
    for _ in range(k):
        t, rolls = guess_tour(dist, rng, start)
        total = tour_length(t, dist)
        best = min(best, total)
        out.append((t, total, best, rolls) if with_rolls else (t, total, best))
    return out


def expected_rolls(n):
    """Expected die rolls to fill the n-1 free slots when repeats are rejected."""
    return sum(n / (n - k) for k in range(1, n))


def brute_force(dist, start=1):
    """Try every order of the other cities with the start fixed. Returns (best_tour, best_total, count)."""
    cities = sorted({a for a, _ in dist})
    others = [c for c in cities if c != start]
    best, best_total, count = None, math.inf, 0
    for p in itertools.permutations(others):
        t = [start, *p]
        count += 1
        total = tour_length(t, dist)
        if total < best_total:
            best, best_total = t, total
    return best, best_total, count


def tour_count(n):
    """Closed tours of n cities, start fixed, direction matters: (n-1)!"""
    return math.factorial(n - 1)
