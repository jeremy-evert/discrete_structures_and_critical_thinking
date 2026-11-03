# Tuesday activity — model, trace, and audit a decision tree

Work individually first. Use the supplied synthetic scenario and keep the
Predict → Run → Explain loop visible in your notes. A **rooted tree** is a
connected hierarchy with one starting vertex and no cycles. A **decision tree**
uses questions in that tree to choose a route. The words `yes` and `no` below
are **edge labels**—answers written on branches—not vertices (named things) in
the tree.

```text
Start
└── eligible?
    ├── yes → needs aid?
    │          ├── yes → aid route
    │          └── no  → standard route
    └── no  → explain rule
```

The supplied intake note adds this relationship: some people on the aid route
need a **language-access review** before that route is usable. The review is not
shown as a vertex in the displayed tree. Do not claim facts about a real
admissions, benefits, or student system from this invented example.

## 1. Sources

Name the displayed decision tree and the supplied intake note. State that the
tree is a model, not a complete record of every condition in the note.

## 2. Rules / Assumptions

Define **root** (the starting vertex), **internal vertex** (a vertex with a
child), **leaf** (a vertex with no child), and one traversal. State what each
question means and whether each person is assumed to receive exactly one answer
at each split. State again that `yes` and `no` are edge labels.

## 3. Work

1. Label each root-to-leaf path with its answers.
2. Predict, then write, the preorder and breadth-first visit orders.
3. Trace the route for a synthetic person who is eligible and needs aid.
4. Add the language-access review as a new vertex, or state it as an explicit
   limitation. Explain why your choice matches the supplied note.

## 4. Check your answer

Use a second traversal or a partner's trace to check one route. Then test the
claim: “Everyone routed to aid can use the aid route immediately.” Does the
displayed tree establish that claim? Name the missing relationship or condition
that bears on the answer. A clean tree is not proof that all source conditions
were represented.

## 5. One-Sentence Summary

Write one sentence stating what the tree can establish and what it cannot
establish because the language-access relationship is outside the displayed
model.

## AI Fluency check

If an AI tool suggests a tree or trace, treat it as a proposal. Compare its
questions, vertices, edge labels, and source relationships with the supplied
materials. Record one specific check you made. If you did not use AI, state the
check you would require before trusting an AI-generated hierarchy.
