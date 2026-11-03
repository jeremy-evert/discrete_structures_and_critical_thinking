# Prompt 04: trace a decision tree

Model a synthetic eligibility route and keep yes/no as edge labels, not nodes.

```prompt-a
Predict the route for a synthetic person who is eligible and needs aid. Model this
decision tree: Start has child eligible?; from eligible?, yes leads to needs aid?
and no leads to explain rule; from needs aid?, yes leads to aid route and no leads
to standard route. Store yes and no as edge labels, not as vertices. Add a note
linking aid route and language-access review, because that relation is not in the
displayed tree. State plainly that the language-access review must happen before
the aid route is usable. Run a trace for eligible=yes and needs aid=yes. Explain
which step the tree shows and which language-access condition it does not show.
Use no real intake data.
```

```prompt-b
Predict the route and the missing relationship before testing. Add pytest tests for
the eligible-plus-aid trace, the exact preorder and breadth-first traces of the
decision tree, and the fact that yes and no are edge labels rather than nodes.
Postorder is optional for this decision-tree check. Use the reference module's
decision-tree constants where possible, and do not put yes or no into the node
lists. Run pytest. Explain why “aid route” is not enough to prove that the review
has happened before the route is usable.
```
