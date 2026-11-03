# Week 13 handout — Trees, search, and decision structures

## Start with two pictures

A **model** is a simplified representation used to ask a checkable question. A
**claim** is a sentence about what that model establishes. A **network** is a
graph: a collection of named things and relationships between them. Each named
thing is a **vertex** (also called a node), and each relationship is an **edge**.
In a **directed edge**, the direction is part of the meaning.

Imagine a shared project folder. A folder view answers **containment**: what is
shown inside this folder? Now imagine a work-order list. A **dependency** is a
“must happen before” relationship. The same names can appear in both pictures,
but their edges do different jobs.

Put these meanings in one box before you draw or look up a name:

> `A -> B` means a dependency: complete A first. In a decision tree, an edge
> label such as `yes` means the answer leads to the next vertex. `Predict -> Run
> -> Explain` names the steps in order.

## The synthetic example

Use this invented, non-sensitive project **model**:

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

Here each arrow is a dependency, so it says that the item on the left must be
completed first. A **conversion** changes this graph into another display:

```text
project
├── plan
│   ├── requirements
│   └── design
└── build
    ├── tests
    └── docs
```

In this directory-style tree, each parent-child edge means “shown under,” not
automatically “must be completed before.” Treat the conversion as a model to
check, not proof that every work-order relationship survived. The audit is part
of the lesson.

## How the prompts work

Paste each prompt into Claude Code, or your usual AI coding assistant, in a
scratch folder with Python 3 and pytest available. Here **run** means ask the
assistant to execute the Python file or pytest command and show its result. You
predict first, the assistant writes and runs code, and you compare its result
with your prediction. For the trace parts, paper-only work is the fallback.

## Predict → Run → Explain

Use the same loop for every traversal or search:

1. **Predict:** write the order or result you expect before using a program.
2. **Run:** execute the supplied synthetic example, or follow it on paper.
3. **Explain:** compare the result with your prediction and name the reason for
   any difference.

An unexpected result is useful evidence. Do not edit a test or change the model
just to make the output look familiar.

## A tree is a special kind of model

A **rooted tree** is a connected hierarchy with one starting vertex and no
cycles. **Connected** means that the vertices in this displayed structure are
joined by paths. A **cycle** is a path that can return to a vertex already
visited. The starting vertex is the **root**. A vertex directly above another is
its **parent**; the vertex below it is its **child**. A vertex with no children
is a **leaf**. The number of parent-to-child steps from the root is its
**depth**. A **descendant** is any vertex below another vertex, not only its
immediate child. A vertex together with all of its descendants is a **subtree**.

For the folder picture, `project` is the root. A **branch** is one path from a
junction where paths separate down through its descendants; here `plan` and `build` begin two
branches. Read the child order from left to right and keep it fixed. A tree is
a hierarchy because each non-root item has one parent. That rule makes lookup
and traversal predictable, but it can also hide a relationship from the
original graph.

## Traversal vocabulary

A **path** is a sequence of vertices connected by edges. A **traversal** is a
rule for visiting vertices and recording the visit order; that recorded list is
a **trace**.

- **Preorder:** visit the parent, then recursively visit each child from left
  to right. **Recursion** means solving a problem by applying the same rule to
  a smaller part; **recursively** means doing that again for each child.
- **Postorder:** visit all children from left to right, then visit the parent.
- **Breadth-first:** visit the root, then each level from left to right before
  moving to the next level.
- **Depth-first:** finish a branch before moving to its sibling. Preorder and
  postorder are depth-first examples here.
- **Inorder:** visit-left, parent, visit-right. This is a convention for a
  **binary tree**, a tree where each vertex has at most two children. We do not
  use inorder for this general rooted tree.

Before you run, write one line for each requested order. Then check that every
vertex appears once and that the order follows the definition.

## The audit question

An **audit** is a deliberate check of a model against its source. A **set** is
a collection with no order or repeats. Compare the set of original dependency
edges with the set of tree parent-child edges. If an edge is absent, say exactly
which relationship is absent and whether that changes the claim you want to
make. A **test** is an executable check that fails when an expected condition is
false; **pytest** is the Python tool used to run these tests. An **assert** is a
test statement that makes that expected condition explicit.

The Week 13 failure mode is a clean hierarchy that silently erases a relevant
relationship. Finding every vertex is not the same as preserving every edge.
An **edge case** is a boundary or unusual input worth checking, such as the
missing-node search in this lesson. A **counterexample** is one concrete case
that defeats a broad claim.

## Decision structures

A **decision tree** is a rooted tree whose questions divide choices into
branches. A **split** is one such question with possible answers. A **route**
is the path selected by the answers. Keep the answer words on the edges: `yes`
leads to the next vertex, and `no` leads to the other branch. In the Tuesday
activity, `yes` and `no` are edge labels, not extra vertices.

The supplied note uses a **language-access review**, meaning a check that the
route is usable for the language-access needs described by the note. It says
that the review must happen before the aid route is usable. The displayed tree
does not show that condition, so a route trace alone cannot prove it happened.

## Evidence and the course method

**Search** means checking whether a named vertex or relationship can be found in
the model. **Discriminating evidence** is a check whose result can distinguish
between competing claims, such as an exact edge comparison or a missing-node
search. A **bounded conclusion** is a conclusion limited to what the evidence
actually checks.

Use these five headings in the Tuesday activity:

1. **Sources:** name the supplied synthetic graph, tree, or decision scenario.
2. **Rules/Assumptions:** define what an edge means, state the child order, and
   state how a decision answer is interpreted.
3. **Work:** show the tree, routes, traversal traces, or edge comparison.
4. **Check:** use a second trace, an exact set comparison, or a counterexample
   attempt.
5. **One-Sentence Summary:** state what the model supports and the limit that
   remains.

Student work is a shared learning resource: Others in the course will see your
work, and reading your classmates' work is part of the assignment. Use only
synthetic examples and omit private information.

## A useful final check

Complete this sentence after each model:

> “This structure establishes __________ because I checked __________; it does
> not establish __________ because __________ is outside the model.”

That sentence keeps a convenient picture from becoming a claim larger than its
evidence.
