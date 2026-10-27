from functools import cmp_to_key
from itertools import permutations

from fixtures import TRACKS
from playlist.ordering import compare
from relations import antisymmetric_failure, transitive_failure


def at_or_before(a, b):
    return compare(a, b) <= 0


def test_order_is_antisymmetric():
    witness = antisymmetric_failure(at_or_before, TRACKS)
    assert witness is None, (
        "tracks {0.id} and {1.id} are each 'at or before' the other, yet they are different tracks".format(*witness)
    )


def test_order_is_transitive():
    assert transitive_failure(at_or_before, TRACKS) is None


def test_sorting_gives_one_answer_no_matter_how_the_input_was_shuffled():
    answers = {
        tuple(sorted(shuffled, key=cmp_to_key(compare)))
        for shuffled in permutations(TRACKS)
    }
    assert len(answers) == 1
