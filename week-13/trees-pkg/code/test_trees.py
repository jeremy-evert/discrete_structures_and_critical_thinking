import pytest

from trees import (
    DECISION_CHILDREN,
    DECISION_EDGE_LABELS,
    GRAPH_EDGES,
    TREE_CHILDREN,
    TREE_EDGES,
    audit_dropped_edges,
    breadth_first,
    decision_trace,
    decision_tree_traces,
    postorder,
    preorder,
    tree_edges,
)


def test_exact_synthetic_graph_vertices_and_edges():
    assert set(GRAPH_EDGES) == {
        ("project", "plan"),
        ("project", "build"),
        ("plan", "requirements"),
        ("plan", "design"),
        ("build", "tests"),
        ("build", "docs"),
        ("requirements", "tests"),
    }


def test_tree_edges_are_containment_edges():
    assert TREE_EDGES == {
        ("project", "plan"),
        ("project", "build"),
        ("plan", "requirements"),
        ("plan", "design"),
        ("build", "tests"),
        ("build", "docs"),
    }
    assert tree_edges(TREE_CHILDREN) == TREE_EDGES


def test_project_traversals_have_exact_frozen_order():
    assert preorder("project", TREE_CHILDREN) == [
        "project",
        "plan",
        "requirements",
        "design",
        "build",
        "tests",
        "docs",
    ]
    assert postorder("project", TREE_CHILDREN) == [
        "requirements",
        "design",
        "plan",
        "tests",
        "docs",
        "build",
        "project",
    ]
    assert breadth_first("project", TREE_CHILDREN) == [
        "project",
        "plan",
        "build",
        "requirements",
        "design",
        "tests",
        "docs",
    ]


def test_silent_drop_audit_names_the_cross_link():
    assert audit_dropped_edges() == {("requirements", "tests")}


@pytest.mark.xfail(
    strict=True,
    reason="A clean hierarchy can erase the relevant requirements-to-tests relation.",
)
def test_naive_hierarchy_preserves_everything_is_intentionally_red():
    """This deliberately false claim must stay visibly marked as expected red."""
    assert audit_dropped_edges() == set()


def test_decision_tree_uses_yes_no_as_edge_labels():
    assert DECISION_EDGE_LABELS == {
        ("eligible?", "needs aid?"): "yes",
        ("eligible?", "explain rule"): "no",
        ("needs aid?", "aid route"): "yes",
        ("needs aid?", "standard route"): "no",
    }
    assert "yes" not in DECISION_CHILDREN
    assert "no" not in DECISION_CHILDREN


def test_decision_trace_for_eligible_with_aid():
    assert decision_trace(eligible=True, needs_aid=True) == [
        "Start",
        "eligible?",
        "needs aid?",
        "aid route",
    ]


def test_decision_tree_traversals_have_exact_traces():
    assert decision_tree_traces() == {
        "preorder": [
            "Start",
            "eligible?",
            "needs aid?",
            "aid route",
            "standard route",
            "explain rule",
        ],
        "postorder": [
            "aid route",
            "standard route",
            "needs aid?",
            "explain rule",
            "eligible?",
            "Start",
        ],
        "breadth-first": [
            "Start",
            "eligible?",
            "needs aid?",
            "explain rule",
            "aid route",
            "standard route",
        ],
    }


def test_child_order_is_frozen_in_tuples():
    assert TREE_CHILDREN["project"] == ("plan", "build")
    assert TREE_CHILDREN["plan"] == ("requirements", "design")
    assert TREE_CHILDREN["build"] == ("tests", "docs")
    assert all(isinstance(children, tuple) for children in TREE_CHILDREN.values())
    assert all(isinstance(children, tuple) for children in DECISION_CHILDREN.values())
