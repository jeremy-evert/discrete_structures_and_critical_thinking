# 02 — A property checker that shows its witness

**Why:** a "yes" needs a reason and a "no" needs a counterexample. The checker prints the exact pair or triple that breaks a property.
**Slide:** Part 1, "Four questions, four witnesses". **Principle:** witness / counterexample.
**Recovery:** `cp reference/demos/properties.py demos/`.

```prompt-a
Create demos/properties.py. Four functions taking (items, pairs): reflexive, symmetric,
antisymmetric, transitive. Each returns None when the property holds, otherwise a witness:
the first failing item, pair, or triple, trying items in the order given.
Add report(title, items, pairs) printing a heading and one line per property:
"holds" or "FAILS  witness: ...".
At the bottom (under a main guard) call report for:
 (a) "sits next to": ITEMS and SITS_NEXT_TO imported from demos/seating.py;
 (b) "divides" on the numbers 1..12 (a divides b).
Run python demos/properties.py and show me the output.
```

**What you should see:**
- (a) sits next to: reflexive FAILS (witness `Ana`), symmetric holds, antisymmetric FAILS (witness `Ana, Ben`), transitive FAILS (witness `Ana, Ben, Ana`).
- (b) divides on 1..12: reflexive holds, symmetric FAILS (witness `1, 2`), antisymmetric holds, transitive holds.

**Predict first (30 seconds, ask the room before running):** Does 'sits next to' hold reflexive? Does 'divides' hold symmetric?
**Expected answer:** No: nobody sits next to themselves. No: 1 divides 2 but 2 does not divide 1.
**Common mistake / drift:** Claude prints True/False only. Re-ask: "print the witness, the actual pair that breaks it".
