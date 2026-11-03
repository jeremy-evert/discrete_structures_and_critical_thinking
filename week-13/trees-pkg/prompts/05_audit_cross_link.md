# Prompt 05: audit the dropped cross-link

Compare relations directly; a clean hierarchy can erase a relevant relation.

```prompt-a
Predict whether the directory-style tree contains every dependency from the
synthetic graph. Before running, paste your predicted dropped edge set here:
dropped: [your predicted set]. Compare the exact graph edge set with the tree
parent-child edge set. Run the audit and print the actual dropped set. Compare it
with the prediction and explain any difference. Explain the AI failure mode: a
clean hierarchy can erase a relevant relation, because a dependency edge can
cross from one branch to another even when the tree looks tidy. Do not use a real
project or any personal data.
```

```prompt-b
Predict whether the regression test will name a missing edge. Add a pytest test
that asserts the audit result from the reference module's GRAPH_EDGES and
TREE_EDGES constants, rather than using your prediction as the oracle. Also add a
clearly labeled strict expected-failure test for the intentionally false claim
that a hierarchy preserves every graph dependency; use
pytest.mark.xfail(strict=True, reason=...). Run pytest and explain why the
expected failure is evidence about the claim, not a broken test suite. Do not
replace the expected-failure marker with a passing test.
```
