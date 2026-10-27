from fixtures import TRACKS
from playlist.duplicates import is_duplicate
from relations import reflexive_failure, symmetric_failure


def test_a_track_is_a_duplicate_of_itself():
    assert reflexive_failure(is_duplicate, TRACKS) is None


def test_is_duplicate_gives_the_same_answer_in_both_directions():
    witness = symmetric_failure(is_duplicate, TRACKS)
    assert witness is None, (
        "asymmetric: is_duplicate({0.id}, {1.id}) is True but is_duplicate({1.id}, {0.id}) is False".format(*witness)
    )
