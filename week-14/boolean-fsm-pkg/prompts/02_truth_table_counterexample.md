# Prompt 02 — Exhaust the truth table

Why: a single counterexample defeats a claim that two expressions agree on
every assignment.

Slide reference: Week 14 Tuesday, the false simplification.

```prompt-a
Write a small Python program using only the standard library. Define F = (P OR Q) AND (P OR NOT Q) and the proposed simplification B = P OR Q. Evaluate both expressions for all four Boolean assignments of P and Q, in the fixed order (False, False), (False, True), (True, False), (True, True). Print a compact table with P, Q, F, and B, then print the exact assignments where they differ. Do not simplify the expressions by inspection. The expected check is one mismatch, at P=False and Q=True.
```

Expected observable result: four rows are printed, and the only mismatch is
`P=False, Q=True`.

Predict first: which row will expose the proposed simplification, if any?

Likely AI drift: the program may print only true rows, use the wrong operator
precedence, or quietly replace the proposed expression.

Recovery: compare the printed four rows with the visible table on the slide;
the row `False, True` must remain visible.
