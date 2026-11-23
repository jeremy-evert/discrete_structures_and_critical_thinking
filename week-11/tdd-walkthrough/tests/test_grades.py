import pytest

from merger.grades import letter_grade


# One test per bin, plus both sides of every boundary.
@pytest.mark.parametrize(
    "score, expected",
    [
        (100, "A"), (90, "A"),
        (89, "B"), (80, "B"),
        (79, "C"), (70, "C"),
        (69, "D"), (60, "D"),
        (59, "F"), (0, "F"), (45, "F"),
    ],
)
def test_each_bin_and_boundary(score, expected):
    assert letter_grade(score) == expected


@pytest.mark.parametrize("bad", [-1, 101])
def test_scores_outside_0_to_100_are_rejected(bad):
    with pytest.raises(ValueError):
        letter_grade(bad)
