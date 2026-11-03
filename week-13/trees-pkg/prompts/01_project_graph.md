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
