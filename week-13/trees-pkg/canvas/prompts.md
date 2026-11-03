# Prompt 01: model the project dependency graph

Use only the synthetic project data below, and keep the Predict → Run → Explain loop.

```prompt-a
Predict which seven vertices and seven directed edges you expect before you run anything.
Use the synthetic project graph with vertices project, plan, build, requirements, design,
tests, and docs. In this lesson, a directed edge A -> B means “A must be completed
before B.” Write a small Python module that stores exactly these edges:
project -> plan, project -> build, plan -> requirements, plan -> design,
build -> tests, build -> docs, and requirements -> tests. Print the vertices and the
sorted edge list. Run the module. Explain how your output matches the prediction.
Do not use real project, student, employee, or host data.
```

```prompt-b
Predict what an exact edge-set test should catch. Add pytest tests for the seven
synthetic vertices and the exact seven-edge set listed in prompt-a. Do not edit these
tests later, even if a later prompt produces a surprising result. Run pytest and show
the short result. Explain what an exact set check tells us that a picture alone may not.
```


<!-- PROMPT FILE SEPARATOR -->

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


<!-- PROMPT FILE SEPARATOR -->

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


<!-- PROMPT FILE SEPARATOR -->

# Prompt 04: trace a decision tree

Model a synthetic eligibility route and keep yes/no as edge labels, not nodes.

```prompt-a
Predict the route for a synthetic person who is eligible and needs aid. Model this
decision tree: Start -> eligible?; from eligible?, yes -> needs aid? and no -> explain
rule; from needs aid?, yes -> aid route and no -> standard route. Store yes and no as
edge labels, not as vertices. Add the original intake relation aid route ->
language-access review as a separate note, because it is not in the displayed tree.
Run a trace for eligible=yes and needs_aid=yes. Explain which step the tree shows and
which language-access relationship it does not show. Use no real intake data.
```

```prompt-b
Predict the route and the missing relationship before testing. Add pytest tests for
the eligible-plus-aid trace [Start, eligible?, needs aid?, aid route], for the exact
preorder/postorder/breadth-first traces of the decision tree, and for the fact that
yes and no are edge labels rather than nodes. Run pytest. Explain why “aid route” is
not enough to prove that every needed language-access review has happened.
```


<!-- PROMPT FILE SEPARATOR -->

# Prompt 05: audit the dropped cross-link

Compare relations directly; a clean hierarchy can erase a relevant relation.

```prompt-a
Predict whether the directory-style tree contains every dependency from the
synthetic graph. Compare the exact graph edge set with the tree parent-child edge set.
Run the audit and print the dropped set. It must be {requirements -> tests}. Explain
the AI failure mode: a clean hierarchy can erase a relevant relation, because a
dependency edge can cross from one branch to another even when the tree looks tidy.
```

```prompt-b
Predict that the regression test should name one missing edge. Add a pytest test that
asserts the audit returns exactly {(requirements, tests)}. Also add a clearly labeled
strict expected-failure test for the intentionally false claim that a hierarchy
preserves every graph dependency; use pytest.mark.xfail(strict=True, reason=...).
Run pytest and explain why the expected failure is evidence about the claim, not a
broken test suite. Do not replace the expected-failure marker with a passing test.
```


<!-- PROMPT FILE SEPARATOR -->

# Prompt 06: check a search claim against the model

Use an exact node set and one missing-node case to bound a claim.

```prompt-a
Predict which searches should succeed before running them. Write a search helper for
the seven synthetic tree nodes and test searches for project, requirements, tests,
and docs. Then test a missing-node search for language-access review. Run the helper
and print each result. Explain that finding a node is not the same as proving every
dependency involving that node is present.
```

```prompt-b
Predict that all seven known nodes will be found and the missing node will not. Add
pytest assertions for those cases. Then assert that the tree cannot support the
stronger claim “all dependencies are preserved,” because the exact audit reports
requirements -> tests as absent. Run pytest and explain the difference between a
successful node search and a complete relationship audit.
```


<!-- PROMPT FILE SEPARATOR -->

# Prompt 07: explain the model's limit

Finish with a bounded conclusion supported by the synthetic checks.

```prompt-a
Predict the evidence you will print before running the complete suite. Run the full
pytest suite and print the project preorder, postorder, and breadth-first traces, the
decision-tree traces, and the dropped dependency set. Then write one bounded
conclusion: the tree is a useful containment view with a fixed traversal order, but
it does not preserve the requirements -> tests dependency. Explain which result is a
direct check and which statement is a limitation of the model. Use synthetic data
only, and do not edit tests while explaining the result.
```
