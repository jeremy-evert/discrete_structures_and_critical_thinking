# Prompt 03: trace a tree in three ways

Predict each visit order before running the same fixed-child-order tree.

```prompt-a
Predict the visit order for preorder (parent before children), postorder (children
before parent), and breadth-first (level by level) on the synthetic project tree.
Implement those three traversals without changing the child order. Run them from
project and print the three traces. Explain why inorder is not used: inorder belongs
to binary-tree conventions, while this is a general rooted tree.
```

```prompt-b
Predict the exact lists before running tests. Add pytest assertions for preorder
[project, plan, requirements, design, build, tests, docs], postorder
[requirements, design, plan, tests, docs, build, project], and breadth-first
[project, plan, build, requirements, design, tests, docs]. Run pytest and explain
why a depth-first implementation cannot produce the breadth-first trace.
```
