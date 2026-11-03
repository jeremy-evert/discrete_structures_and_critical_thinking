# Prompt 03 — Equivalence, satisfiability, and universal claims

Why: “one witness exists” and “every assignment works” are different claims.

Slide reference: Week 14 Tuesday, the equivalence and SAT checks.

```prompt-a
Extend a small standard-library Boolean evaluator with an equivalence checker. It must enumerate every assignment for the variables that occur and return a list of counterexamples, not just True or False. Check that E = (P AND Q) OR (P AND NOT Q) is equivalent to S = P, and check that F = (P OR Q) AND (P OR NOT Q) is not equivalent to B = P OR Q. Print the counterexample for the second pair exactly as a mapping from variable names to Boolean values. State why an empty counterexample list supports equivalence only for the variables and operators actually supplied.
```

Expected observable result: the first pair has no counterexamples; the second
pair returns exactly `{'P': False, 'Q': True}`.

Predict first: which result should be empty, and which result should contain a
mapping?

Likely AI drift: it may compare only one chosen assignment or return a vague
sentence instead of the counterexample.

Recovery: keep the reference evaluator’s fixed four-row order and print the
mapping before any summary sentence.

```prompt-b
Using the same evaluator, write three separate checks. First, return one satisfying witness for P, meaning one assignment that makes P true. Second, decide whether P is a tautology, meaning true for every assignment, and if it is not, print one counterexample. Third, classify P OR NOT P and P AND NOT P as tautology or unsatisfiable. Explain in one sentence why a satisfying witness for P does not prove that P is always true. Do not use the words “equivalent” or “always” without showing the assignments that justify them.
```

Expected observable result: a witness for `P` is printed; `P` is not a
tautology; `P OR NOT P` is a tautology; `P AND NOT P` has no satisfying
witness.

Predict first: can one true row establish a tautology?

Likely AI drift: it may confuse satisfiable with universally true, or report
the first witness as a proof of every row.

Recovery: ask for the complete assignment table and label witness,
counterexample, and tautology as separate checks.
