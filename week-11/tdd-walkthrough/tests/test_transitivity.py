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
