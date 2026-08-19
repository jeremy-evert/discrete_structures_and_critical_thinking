# Tuesday activity — Trace before you trust recursion

Consider the recursively defined sum:

`S(0) = 0` and `S(n) = n + S(n - 1)` for integers `n > 0`.

## Worked example

`S(3) = 3 + S(2) = 3 + 2 + S(1) = 3 + 2 + 1 + S(0) = 6`.

The base case stops the trace. Each recursive call reduces a nonnegative
input by one, so the trace reaches that base case.

## Your trace and check

1. Trace `S(4)` and identify the base case and the reducing rule.
2. A proposed definition says `T(0) = 1` and `T(n) = T(n + 1)` for `n > 0`.
   Explain why it fails as a terminating recursive definition. Give the
   smallest input that exposes the problem.
3. For the claim `S(n) = n(n + 1)/2`, write the base-case check and describe
   the logical bridge an inductive step would need. You do not need to write
   a full formal proof, but do not say merely “assume it works.”
4. Record Sources, Rules/Assumptions, Work, Check, and a One-Sentence
   Summary.

## AI fluency check

If AI proposes a proof or recurrence solution, inspect whether it verifies
the base case and whether the next line follows from the stated hypothesis.
