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
