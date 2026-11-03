"""Small, synthetic examples for the Week 13 trees lesson.

The dependency graph and the directory-style tree are deliberately separate
models.  In the graph, ``A -> B`` means that A must be completed before B.
In the tree, a parent-child edge means containment in the displayed layout.
Keeping those meanings separate makes the dropped cross-link visible.
"""

from collections import deque


VERTICES = (
    "project",
    "plan",
    "build",
    "requirements",
    "design",
    "tests",
    "docs",
)

# A directed edge (A, B) means "complete A before B."
GRAPH_EDGES = frozenset(
    {
        ("project", "plan"),
        ("project", "build"),
        ("plan", "requirements"),
        ("plan", "design"),
        ("build", "tests"),
        ("build", "docs"),
        ("requirements", "tests"),
    }
)

# Tuple values freeze the left-to-right order used by every traversal.
# These edges mean containment, not dependency.
TREE_CHILDREN = {
    "project": ("plan", "build"),
    "plan": ("requirements", "design"),
    "build": ("tests", "docs"),
    "requirements": (),
    "design": (),
    "tests": (),
    "docs": (),
}

TREE_EDGES = frozenset(
    (parent, child)
    for parent, children in TREE_CHILDREN.items()
    for child in children
)

# The clean decision tree keeps yes/no as edge labels.  They are not nodes.
DECISION_CHILDREN = {
    "Start": ("eligible?",),
    "eligible?": ("needs aid?", "explain rule"),
    "needs aid?": ("aid route", "standard route"),
    "aid route": (),
    "standard route": (),
    "explain rule": (),
}

DECISION_EDGE_LABELS = {
    ("eligible?", "needs aid?"): "yes",
    ("eligible?", "explain rule"): "no",
    ("needs aid?", "aid route"): "yes",
    ("needs aid?", "standard route"): "no",
}

# This relation came from the intake note but is not represented by the tree.
INTAKE_RELATIONS = frozenset({("language-access review", "aid route")})  # review comes before the route is usable


def tree_edges(children=TREE_CHILDREN):
    """Return parent-child edges in a tree, preserving no hidden relations."""
    return frozenset(
        (parent, child)
        for parent, child_names in children.items()
        for child in child_names
    )


def audit_dropped_edges(graph_edges=GRAPH_EDGES, children=TREE_CHILDREN):
    """Return graph dependencies absent from the displayed tree."""
    return set(graph_edges) - set(tree_edges(children))


def preorder(root, children):
    """Visit a node before its children, from left to right."""
    result = []

    def visit(node):
        result.append(node)
        for child in children[node]:
            visit(child)

    visit(root)
    return result


def postorder(root, children):
    """Visit all children before their parent, from left to right."""
    result = []

    def visit(node):
        for child in children[node]:
            visit(child)
        result.append(node)

    visit(root)
    return result


def breadth_first(root, children):
    """Visit each level before moving to the next level."""
    result = []
    pending = deque([root])
    while pending:
        node = pending.popleft()
        result.append(node)
        pending.extend(children[node])
    return result


def decision_trace(eligible, needs_aid=None):
    """Trace the decision tree; ``yes`` and ``no`` remain edge labels."""
    trace = ["Start", "eligible?"]
    if not eligible:
        trace.append("explain rule")
        return trace
    trace.append("needs aid?")
    trace.append("aid route" if needs_aid else "standard route")
    return trace


def decision_tree_traces():
    """Return the three exact traces used in the lesson."""
    return {
        "preorder": preorder("Start", DECISION_CHILDREN),
        "postorder": postorder("Start", DECISION_CHILDREN),
        "breadth-first": breadth_first("Start", DECISION_CHILDREN),
    }


if __name__ == "__main__":
    print("graph edges:", sorted(GRAPH_EDGES))
    print("tree edges:", sorted(TREE_EDGES))
    print("dropped edges:", sorted(audit_dropped_edges()))
    print("preorder:", ", ".join(preorder("project", TREE_CHILDREN)))
    print("postorder:", ", ".join(postorder("project", TREE_CHILDREN)))
    print("breadth-first:", ", ".join(breadth_first("project", TREE_CHILDREN)))
