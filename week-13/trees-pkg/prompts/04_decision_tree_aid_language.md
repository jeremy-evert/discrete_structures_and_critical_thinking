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
