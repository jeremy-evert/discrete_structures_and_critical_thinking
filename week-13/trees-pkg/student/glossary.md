# Week 13 glossary — plain-language vocabulary

These definitions use the same synthetic project and decision examples as the
handout. The arrow meaning must always be stated before a trace or claim.

| Term | Definition and concrete example |
|---|---|
| **vertex** | A named thing in a graph. In this week, `project` and `tests` are vertices. Week 12 also called this a node. |
| **edge** | A relationship between two vertices. A directed edge has a direction, such as `build -> tests`. |
| **path** | A sequence of connected vertices. `project -> plan -> design` is a path in the synthetic graph. |
| **rooted tree** | A tree with one chosen starting vertex, called its root, and no cycles. |
| **root** | The starting vertex of a rooted tree. It has no parent; `project` is the root of the folder-style example. |
| **parent** | The vertex directly above a child in the tree. `plan` is a parent of `requirements` in the displayed tree. |
| **child** | A vertex directly below a parent in the tree. `design` is a child of `plan`. |
| **leaf** | A vertex with no children in the displayed tree. `docs` is a leaf. A leaf can still have a dependency elsewhere. |
| **depth** | The number of parent-child steps from the root. The root has depth 0. |
| **subtree** | A vertex plus every descendant below it. The `plan` subtree includes `plan`, `requirements`, and `design`. |
| **preorder** | A traversal that visits a parent before its children, keeping the stated left-to-right order. |
| **postorder** | A traversal that visits all children before their parent. |
| **breadth-first** | A traversal that visits one depth level before moving to the next level. |
| **cross-link** | A relationship between branches that is not represented by a parent-child edge in the displayed hierarchy. |
| **hierarchy** | An arrangement in levels, where each item has a place under a larger item. A rooted tree is one kind of hierarchy. |
| **decision tree** | A rooted tree in which questions are internal vertices and answers such as `yes` and `no` label the edges to the next question or outcome. |
| **dependency** | A “must happen before” relationship. `requirements -> tests` means requirements must be completed before tests. |
| **containment** | A “is shown under” relationship, like a file inside a folder. It is different from dependency even when the same names are used. |
| **dependency vs containment** | Dependency describes order of work; containment describes placement in a hierarchy. Never silently substitute one meaning for the other. |
| **graph** | A model made from vertices and edges. It may have cross-links or cycles. |
| **tree** | A connected graph organized from one root with no cycles; in this package, child order is fixed left to right. |
| **traversal** | A repeatable rule for visiting vertices and recording their order. |
| **internal vertex** | A vertex with at least one child in the displayed tree. In the decision tree, `eligible?` is internal. |
| **edge label** | Text attached to an edge to say why that branch is taken. In the decision tree, `yes` and `no` are labels, not vertices. |
| **counterexample** | One concrete case that shows a broad claim is false or too strong. |
