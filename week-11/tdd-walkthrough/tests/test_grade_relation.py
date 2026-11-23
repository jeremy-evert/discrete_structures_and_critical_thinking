from merger.grades import letter_grade
from relations import reflexive_failure, symmetric_failure, transitive_failure

SCORES = list(range(0, 101, 3)) + [59, 60, 69, 70, 79, 80, 89, 90, 100]


def same_bin(a, b):
    return letter_grade(a) == letter_grade(b)


def test_every_score_lands_in_exactly_one_bin():
    bins = {}
    for s in range(0, 101):
        bins.setdefault(letter_grade(s), []).append(s)
    assert sorted(bins) == ["A", "B", "C", "D", "F"]
    assert sum(len(v) for v in bins.values()) == 101


def test_same_bin_is_an_equivalence_relation():
    assert reflexive_failure(same_bin, SCORES) is None
    assert symmetric_failure(same_bin, SCORES) is None
    assert transitive_failure(same_bin, SCORES) is None
