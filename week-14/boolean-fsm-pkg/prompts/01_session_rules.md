# Prompt 01 — Make the claim checkable

Why: a confident answer is not evidence until its terms and test are visible.

Slide reference: Week 14 Tuesday, the small-step rules.

```prompt-a
Act as a careful checking partner for a two-variable Boolean example. Before writing code, state what an expression, a Boolean variable, an assignment, and equivalence mean in plain language. Use only the operators AND, OR, and NOT. Keep the example synthetic and self-contained. Then propose the smallest Python standard-library evaluator you would need for a truth table. Do not claim two expressions are equivalent until every assignment has been checked. Show one predicted row before showing the rest.
```

Expected observable result: the response defines its terms, names the four
assignments for `P` and `Q`, and separates a prediction from an exhaustive
check.

Predict first: what must be checked before “equivalent” is justified?

Likely AI drift: it may use an undefined operator, skip an assignment, or
announce equivalence from one matching row.

Recovery: return to the committed deck example and write all four rows by hand
before comparing any generated output.
