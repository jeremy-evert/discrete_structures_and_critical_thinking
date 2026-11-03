# Week 13 concept map — from relationships to a checked hierarchy

The map starts with a concrete folder or work-order picture. Read the arrows
with their meaning written beside them; an arrow is not automatically the same
kind of relationship in every model.

| Concrete question | Term and first-use meaning | Checkable evidence | Limit to watch |
|---|---|---|---|
| What things and relationships are present? | A **graph** stores vertices (named things) and edges (relationships). | List the seven synthetic vertices and seven directed edges. | A picture can omit an edge. |
| What must happen first? | A **dependency** says one item must be completed before another. | State the direction of each work-order edge. | Dependency is not the same as folder placement. |
| What is shown inside a folder? | **Containment** says an item is shown under another item. | List each tree parent and its children. | A containment tree may drop a dependency. |
| Where does the picture begin? | A **rooted tree** has one root and no cycles; the **root** is its starting vertex. | Identify `project` and count one starting point. | A general graph may not have one root. |
| Who is directly above or below? | A **parent** is directly above a **child**. | Every non-root vertex has one parent. | A cross-branch relationship is not a parent-child edge. |
| Which items stop? | A **leaf** has no children. | Mark `requirements`, `design`, `tests`, and `docs` in the folder picture. | A leaf can still have a dependency in the original graph. |
| How far down is an item? | **Depth** is the number of parent-child steps from the root. | Count steps on one root-to-leaf path. | Depth measures containment, not work effort. |
| What belongs below one item? | A **subtree** is a vertex and all descendants below it. | Circle one branch and list its members. | A subtree is not automatically a complete dependency set. |
| How do we visit every item? | A **traversal** is a rule for visiting vertices. | Write a trace and verify that each vertex appears once. | The order depends on the rule and frozen child order. |
| What is visited first? | **Preorder** visits a parent before its children. | Compare the trace with the definition. | It is not a level-by-level order. |
| What is visited last? | **Postorder** visits children before their parent. | The root appears at the end. | It does not mean “latest work” in the dependency sense. |
| How do levels work? | **Breadth-first** visits one level before the next. | The two children of the root appear before grandchildren. | A depth-first procedure cannot produce this trace. |
| What relationship crosses branches? | A **cross-link** is a relationship not represented by the displayed parent-child hierarchy. | Compare graph edges with tree edges. | A tidy diagram can still be incomplete. |
| How are choices shown? | A **decision tree** uses questions at internal vertices and answers as edge labels. | Trace an eligible/aided route and label each answer. | A route can omit a condition from the source notes. |

## The method that connects the map to your work

For each claim, use:

**Sources → Rules/Assumptions → Work → Check → One-Sentence Summary.**

Start each step with **Predict**, then **Run**, then **Explain**. In the
explanation, distinguish a successful search for a vertex from an audit that
checks whether relationships were preserved.
