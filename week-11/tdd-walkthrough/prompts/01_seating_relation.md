# 01 — A relation you can see: who sits next to whom

**Why:** a relation is just a set of ordered pairs. Before any vocabulary, the class sees pairs, a matrix and a digraph for something they know.
**Slide:** Part 1, "A relation is a set of pairs" (and the matrix and digraph slides).
**Recovery:** `cp reference/demos/seating.py demos/` then `python3 demos/seating.py`.

```prompt-a
Create demos/seating.py. Students: Ana, Ben, Cy, Dee, Eli (in that order, a list named ITEMS).
Relation "sits next to": Ana-Ben, Ben-Cy, Cy-Dee, Dee-Eli, and each pair works both ways.
Store it as a set of ordered pairs named SITS_NEXT_TO (so 8 pairs).
When run as a script, print:
 1. the pairs, sorted;
 2. a 5x5 matrix of 0/1 with the names as row and column labels;
 3. a digraph as text, one line per student listing all neighbours, like "Ben -> Ana, Cy".
Then run: python3 demos/seating.py   and show me the output.
```

**What you should see:** 8 pairs; a matrix that is symmetric top-left to bottom-right (ones next to the diagonal, zeros on the diagonal); lines `Ana -> Ben`, `Ben -> Ana, Cy`, … `Eli -> Dee`.

**Predict first (30 seconds, ask the room before running):** How many pairs will there be, and will the matrix look the same flipped across the diagonal?
**Expected answer:** 8 pairs (4 neighbours, both ways). Yes, symmetric: if Ana sits next to Ben then Ben sits next to Ana.
**Common mistake / drift:** Claude stores only 4 pairs (one way). Say: "each pair works both ways, so 8 ordered pairs".
