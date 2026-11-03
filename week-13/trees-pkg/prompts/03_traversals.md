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
Before running tests, paste YOUR predictions into these three lines:
preorder: [your predicted list]
postorder: [your predicted list]
breadth-first: [your predicted list]
Add pytest assertions for the exact verified traces. Use the reference module's
fixed child-order constants (such as TREE_CHILDREN) and any trace constants it
provides where possible; if a verified list must be recorded, take it from the
reference run, not from these prediction lines. Keep the pasted predictions as
notes for comparison, not as the test oracle. Run pytest and explain why a
depth-first implementation cannot produce the breadth-first trace.
```
