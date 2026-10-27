from fixtures import SMITH_NAMES
from merger.names import same_person
from relations import reflexive_failure, symmetric_failure, transitive_failure


def test_same_person_is_reflexive():
    assert reflexive_failure(same_person, SMITH_NAMES) is None


def test_same_person_is_symmetric():
    assert symmetric_failure(same_person, SMITH_NAMES) is None


def test_same_person_is_transitive():
    witness = transitive_failure(same_person, SMITH_NAMES)
    assert witness is None, (
        "not transitive: {0!r} ~ {1!r} and {1!r} ~ {2!r}, but {0!r} !~ {2!r}".format(*witness)
    )


def test_fuzzy_match_is_still_not_an_equivalence():
    """Keep the old counterexample on record: closeness is a hint, not an equivalence."""
    from merger.names import similar_names

    assert transitive_failure(similar_names, SMITH_NAMES) == (
        "Jon Smith", "John Smith", "Jonathan Smith",
    )


def test_canonical_key_puts_the_three_spellings_in_one_bin():
    from merger.names import canonical_key

    assert {canonical_key(n) for n in SMITH_NAMES[:3]} == {"jonathan smith"}
    assert canonical_key("Maya Smith") != canonical_key("Jonathan Smith")
