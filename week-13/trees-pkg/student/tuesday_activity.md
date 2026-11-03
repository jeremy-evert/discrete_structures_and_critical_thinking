# Tuesday activity — model, trace, and audit a decision tree

Work individually first. If a partner is available, trade traces; otherwise
re-trace with the other traversal. Use the supplied synthetic scenario and keep
the Predict → Run → Explain loop visible in your notes. A **rooted tree** is a
connected hierarchy with one starting vertex and no cycles. A **decision tree**
uses questions in that tree to choose a route. The words `yes` and `no` below
are **edge labels**—answers written on branches—not vertices (named things) in
the tree.

```text
Start
└── eligible?
    ├── yes leads to needs aid?
    │          ├── yes leads to aid route
    │          └── no leads to standard route
    └── no leads to explain rule
```

The supplied intake note says:

> “Some students routed to the aid route need a language-access review before the
> route is usable.”

The language-access review must happen before the aid route is usable. The review
is not shown as a vertex in the displayed tree. Do not claim facts about a real
admissions, benefits, or student system from this invented example.

## How the prompts work

Paste each prompt into Claude Code, or your usual AI coding assistant, in a
scratch folder with Python 3 and pytest available. Here **run** means ask the
assistant to execute the Python file or pytest command and show its result. You
predict first, the assistant writes and runs code, and you compare its result
with your prediction. For the trace parts, paper-only work is the fallback.

## 1. Sources

Name the displayed decision tree and quote the supplied intake note. State that
the tree is a model, not a complete record of every condition in the note.

## 2. Rules / Assumptions

Define **root** (the starting vertex), **internal vertex** (a vertex with a
child), **leaf** (a vertex with no child), and one traversal. State that the
child order is left to right: `eligible?` comes before `explain rule`, and
`needs aid?` comes before its two outcomes. State what each question means and
whether each person is assumed to receive exactly one answer at each split.
State again that `yes` and `no` are edge labels and that an answer leads to the
next vertex; they are not vertices.

## 3. Work

1. Label each root-to-leaf path with its answers.
2. For the project tree, predict and write the preorder, postorder, and
   breadth-first visit orders.
3. For the decision tree, predict and write the preorder and breadth-first
   visit orders. Postorder is optional for the decision tree.
4. Trace the route for a synthetic person who is eligible and needs aid.
5. Add the language-access review as a new vertex, or state it as an explicit
   limitation. Explain why your choice matches the supplied note and why the
   review must happen before the aid route is usable.

## 4. Check your answer

Use a second traversal or a partner's trace to check one route. If no partner is
available, re-trace it with the other traversal. Then test the claim: “Everyone
routed to aid can use the aid route immediately.” Does the displayed tree
establish that claim? Name the missing relationship or condition that bears on
the answer. A clean tree is not proof that all source conditions were
represented.

## 5. One-Sentence Summary

Write one sentence stating what the tree can establish and what it cannot
establish because the language-access relationship is outside the displayed
model.

## AI Fluency check

If an AI tool suggests a tree or trace, treat it as a proposal. Compare its
questions, vertices, edge labels, child order, and source relationships with the
supplied materials. Record one specific check you made. If you did not use AI,
state the check you would require before trusting an AI-generated hierarchy.
