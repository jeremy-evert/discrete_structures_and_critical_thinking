# 03 — Equivalence, partial order, or neither

**Why:** the whole lesson in one table. The same four questions sort every relation into a kind.
**Slide:** Part 1, "Sorting relations into kinds". **Principle:** equivalence vs partial order.
**Recovery:** `cp reference/demos/classify.py demos/`.

```prompt-a
Create demos/classify.py using the four checkers in demos/properties.py. Print a table with
columns: relation, reflexive, symmetric, antisymmetric, transitive, verdict (yes/no per property).
verdict = "equivalence" if reflexive+symmetric+transitive; "partial order" if
reflexive+antisymmetric+transitive; otherwise "neither".
Relations: (1) same birthday month, on 6 invented students given as (name, month) pairs;
(2) "a divides b" on 1..12; (3) "a <= b" on 1..6; (4) "sits next to" from demos/seating.py;
(5) "a < b" on 1..6. Run it and show me the table.
```

**What you should see:** verdicts in order: equivalence, partial order, partial order, neither, neither. (Row 5: `<` fails reflexive, so it is "neither".)

**Predict first (30 seconds, ask the room before running):** Which row will say 'neither'? Which will say 'partial order'?
**Expected answer:** 'sits next to' and 'a < b' are neither; divides and <= are partial orders; birthday month is an equivalence.
**Common mistake / drift:** Students say '<' is a partial order. It is strict, so it fails reflexive. Run the table and read the 'refl' column.
