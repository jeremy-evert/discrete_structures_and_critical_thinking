# Week 13 handout — Trees, search, and decision structures

## Start with two pictures

Imagine a shared project folder. A folder view answers **containment**: what is
shown inside this folder? Now imagine a work-order list. A work-order view
answers **dependency**: what must be completed before something else can begin?
The same names can appear in both pictures, but their arrows do different jobs.

A **graph** is a collection of named things and relationships. Each named thing
is a **vertex** (also called a node), and a relationship is an **edge**. In this
week's work-order graph, a directed edge `A -> B` means “A must be completed
before B.” In a folder tree, a parent-child edge means “B is shown under A.”
Write down which meaning you are using before you draw or search.

## The synthetic example

Use this invented, non-sensitive project model:

```text
vertices: project, plan, build, requirements, design, tests, docs

project -> plan
project -> build
plan -> requirements
plan -> design
build -> tests
build -> docs
requirements -> tests
```

The last relationship crosses from the planning side to the build side. A
directory-style tree can still be useful:

```text
project
├── plan
│   ├── requirements
│   └── design
└── build
    ├── tests
    └── docs
```

Treat this as a model to check, not as proof that every work-order relationship
survived the conversion. The audit is part of the lesson.

## Predict → Run → Explain

Use the same loop for every traversal or search:

1. **Predict:** write the order or result you expect before using a program.
2. **Run:** run the supplied synthetic example or trace it on paper.
3. **Explain:** compare the result with your prediction and name the reason for
   any difference.

An unexpected result is useful evidence. Do not edit a test or change the
model just to make the output look familiar.

## A tree is a special kind of model

A **rooted tree** is a connected hierarchy with one starting vertex and no
cycles. The starting vertex is the **root**. A vertex directly above another is
its **parent**; the vertex below it is its **child**. A vertex with no children
is a **leaf**. The number of parent-to-child steps from the root is its
**depth**. A vertex together with all of its descendants is a **subtree**.

For the folder picture, `project` is the root. Read the child order from left
to right and keep it fixed. A tree is a hierarchy because each non-root item
has one parent. That rule makes lookup and traversal predictable, but it can
also hide a relationship that belongs to the original graph.

## Traversal vocabulary

A **path** is a sequence of vertices connected by edges; this carries forward
our Week 12 vocabulary. A **traversal** is a rule for visiting vertices.

- **Preorder:** visit the parent, then recursively visit each child from left
  to right.
- **Postorder:** visit all children from left to right, then visit the parent.
- **Breadth-first:** visit the root, then each level from left to right before
  moving to the next level.
- **Inorder:** visit-left, parent, visit-right; this is a convention for binary
  trees, so do not use it as the default for this general tree.

Before you run, write one line for each requested order. Then check that every
vertex appears once and that the order follows the definition.

## The audit question

A **cross-link** is a relationship between branches that is not a parent-child
relationship in the displayed hierarchy. Compare the original dependency edges
with the tree's containment edges. If an edge is absent, say exactly which
relationship is absent and whether that changes the claim you want to make.

The Week 13 failure mode is a clean hierarchy that silently erases a relevant
relationship. Finding every vertex is not the same as preserving every edge.

## Tuesday method: Sources → Rules/Assumptions → Work → Check → One-Sentence Summary

Use these five headings in the Tuesday activity:

1. **Sources:** name the supplied synthetic graph, tree, or decision scenario.
2. **Rules/Assumptions:** define what an edge means, state the child order, and
   state how a decision answer is interpreted.
3. **Work:** show the tree, routes, traversal traces, or edge comparison.
4. **Check:** use a second trace, an exact set comparison, or a counterexample
   attempt. A **counterexample** is one concrete case that defeats a broad
   claim.
5. **One-Sentence Summary:** state what the model supports and the limit that
   remains.

## Decision structures

A **decision tree** is a rooted tree whose edges represent answers to questions.
Keep the answer words on the edges. In the Tuesday activity, `yes` and `no`
are edge labels, not extra vertices. A decision tree can show a route without
proving that every condition needed for the route has been checked. Compare its
questions with the supplied notes before making a stronger claim.

## A useful final check

Complete this sentence after each model:

> “This structure establishes __________ because I checked __________; it does
> not establish __________ because __________ is outside the model.”

That sentence keeps a convenient picture from becoming a claim larger than its
evidence.
