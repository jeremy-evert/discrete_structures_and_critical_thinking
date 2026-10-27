from itertools import product

import merger.names
import merger.pipeline
import merger.records
from merger.deps import build_graph, leaves_first
from relations import antisymmetric_failure, transitive_failure

MODULES = (merger.names, merger.records, merger.pipeline)


def test_graph_reads_the_real_code():
    graph = build_graph(*MODULES)
    assert graph["merge_duplicates"] == {"group_records", "merge_group"}
    assert graph["group_records"] == {"duplicate_key"}
    assert graph["duplicate_key"] == {"canonical_key"}
    assert graph["canonical_key"] == {"_split"}
    assert graph["_split"] == set()


def test_test_order_puts_every_function_after_everything_it_depends_on():
    graph = build_graph(*MODULES)
    order = leaves_first(graph)
    assert sorted(order) == sorted(graph)
    position = {name: i for i, name in enumerate(order)}
    for name, needs in graph.items():
        for dep in needs:
            assert position[dep] < position[name], "{} must be tested before {}".format(dep, name)
    assert graph[order[0]] == set(), "the first function to test must need nothing else"


def closure(graph):
    """Pairs (a, b) meaning 'a depends on b', directly or through others."""
    pairs = {(a, b) for a, needs in graph.items() for b in needs}
    changed = True
    while changed:
        changed = False
        for (a, b), (c, d) in product(list(pairs), repeat=2):
            if b == c and (a, d) not in pairs:
                pairs.add((a, d))
                changed = True
    return pairs


def test_depends_on_is_a_partial_order_on_the_real_code():
    graph = build_graph(*MODULES)
    depends = closure(graph)

    def rel(a, b):
        return (a, b) in depends

    names = sorted(graph)
    assert transitive_failure(rel, names) is None
    assert antisymmetric_failure(rel, names) is None
    assert not any(a == b for a, b in depends), "a function must not depend on itself"
