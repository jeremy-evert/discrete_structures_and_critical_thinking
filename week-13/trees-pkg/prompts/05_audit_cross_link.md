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
