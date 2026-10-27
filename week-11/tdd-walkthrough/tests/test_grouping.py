from fixtures import SMITH_NAMES
from merger.grouping import group_by_chain
from merger.names import same_person, similar_names
from relations import reflexive_failure, symmetric_failure, transitive_failure


def test_chained_matches_end_up_in_one_group():
    groups = group_by_chain(SMITH_NAMES, similar_names)
    assert groups == [["Jon Smith", "John Smith", "Jonathan Smith"], ["Maya Smith"], ["Maria Garcia"]]


def test_same_group_is_an_equivalence_relation():
    groups = group_by_chain(SMITH_NAMES, similar_names)
    group_of = {name: i for i, g in enumerate(groups) for name in g}

    def same_group(a, b):
        return group_of[a] == group_of[b]

    assert reflexive_failure(same_group, SMITH_NAMES) is None
    assert symmetric_failure(same_group, SMITH_NAMES) is None
    assert transitive_failure(same_group, SMITH_NAMES) is None


def test_tradeoff_chain_grouping_merges_pairs_that_were_never_similar():
    groups = group_by_chain(SMITH_NAMES, similar_names)
    jon, jonathan = "Jon Smith", "Jonathan Smith"
    assert not similar_names(jon, jonathan)
    assert any(jon in g and jonathan in g for g in groups)
