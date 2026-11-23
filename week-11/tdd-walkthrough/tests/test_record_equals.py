from fixtures import RECORDS
from merger.records import is_duplicate
from relations import reflexive_failure, symmetric_failure


def test_a_record_is_a_duplicate_of_itself():
    assert reflexive_failure(is_duplicate, RECORDS) is None


def test_is_duplicate_gives_the_same_answer_in_both_directions():
    witness = symmetric_failure(is_duplicate, RECORDS)
    assert witness is None, "asymmetric: is_duplicate({0!r}, {1!r}) is True but swapped is False".format(*witness)
