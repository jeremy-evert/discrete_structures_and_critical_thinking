# Prompt 02: convert the graph into a directory-style tree

Use the fixed synthetic graph and state clearly when an edge changes meaning.

```prompt-a
Predict which relationships will be shown by this directory-style tree:
project has children plan and build; plan has children requirements and design;
build has children tests and docs. Convert the seven-vertex synthetic graph into
that exact tree, with children visited left-to-right. State plainly that a tree edge
means containment (“is shown under”), while the original graph edge means dependency
(“must be completed before”). Print each parent and its children. Run it, then explain
which graph relation is not shown by the tree.
```

```prompt-b
Predict the checks a valid tree should pass. Add pytest tests that check the root is
project, every non-root vertex has one parent, all seven vertices appear exactly once,
and the tree is acyclic. Check the fixed child order project=(plan, build),
plan=(requirements, design), and build=(tests, docs). Run pytest and explain each
check using only the synthetic tree.
```
