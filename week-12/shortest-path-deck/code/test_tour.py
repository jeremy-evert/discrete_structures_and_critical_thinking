import math
import pytest
from tour import (read_table, tour_length, greedy_tour, guess_and_check,
                  brute_force, tour_count, legs)

D = read_table()


def test_table_is_6x6_with_blank_diagonal():
    assert len(D) == 30
    assert all(a != b for a, b in D)


def test_asymmetric_legs_not_equal():
    assert D[(1, 2)] != D[(2, 1)]
    assert all(D[(a, b)] != D[(b, a)] for a in range(1, 7) for b in range(a + 1, 7))


def test_tour_123456_total():
    assert [d for _, _, d in legs([1, 2, 3, 4, 5, 6], D)] == [11, 12, 10, 6, 6, 10]
    assert tour_length([1, 2, 3, 4, 5, 6], D) == 55


def test_greedy_tour():
    assert greedy_tour(D) == [1, 3, 5, 2, 6, 4]
    assert tour_length(greedy_tour(D), D) == 39


def test_brute_force_no_worse_than_greedy_and_strictly_better_here():
    best, total, count = brute_force(D)
    assert total <= tour_length(greedy_tour(D), D)
    assert total == 34 and best == [1, 5, 2, 6, 3, 4]


def test_permutation_count_matches_formula():
    for n in range(2, 7):
        sub = {k: v for k, v in D.items() if k[0] <= n and k[1] <= n}
        assert brute_force(sub)[2] == tour_count(n) == math.factorial(n - 1)


def test_guess_and_check_best_so_far_never_rises_and_is_valid():
    runs = guess_and_check(D, 20, seed=1)
    bests = [b for _, _, b in runs]
    assert bests == sorted(bests, reverse=True)
    assert all(sorted(t) == [1, 2, 3, 4, 5, 6] for t, _, _ in runs)
    assert bests[-1] >= 34


def test_reverse_tour_is_a_different_tour():
    assert tour_length([1, 6, 5, 4, 3, 2], D) == 56 and tour_length([1, 2, 3, 4, 5, 6], D) == 55
