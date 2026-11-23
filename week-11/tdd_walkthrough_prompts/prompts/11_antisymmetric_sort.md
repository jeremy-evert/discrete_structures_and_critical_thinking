# 11 — Antisymmetry: a sort that cannot break ties

**Why:** an order must never call two different records "each at or before the other". A comparator that returns 0 for different people makes sorting depend on input order.
**Slide:** Part 3, "Piece 5: ordering is antisymmetric". **Principle:** antisymmetric property test; witness / counterexample.
**Recovery:** red = `tools/recover.sh 12`; green = `tools/recover.sh 13`.

```prompt-a
Test first. Add merger/ordering.py with the first-draft compare(a, b) for Records: compare the
family name only (last word of name, lowercase), returning -1, 0 or 1.
Write tests/test_ordering.py using RECORDS and the helpers, with at_or_before(a, b) meaning
compare(a, b) <= 0: (1) at_or_before is antisymmetric (message names the two records);
(2) it is transitive; (3) sorting RECORDS with functools.cmp_to_key(compare) gives the SAME list
for every permutation of RECORDS (itertools.permutations). Run pytest. Expect the antisymmetric
and the shuffle tests to fail. Show me and stop.
```

```prompt-b
Fix compare with a unique key: (family name lowercase, given name lowercase, id), so that
compare returns 0 only for the very same record. Put it in a function sort_key(record).
Do not edit the tests. Run pytest: all green. Then print RECORDS sorted. Stop.
```

**What you should see (red):** the witness is `Jon Smith` and `John Smith` (same family name). **Green:** all pass; sorted order Garcia first, then the Smiths by given name.

**Predict first (30 seconds, ask the room before running):** If the comparator only looks at the family name, what happens to Jon Smith and John Smith?
**Expected answer:** It returns 0 for both, so each is 'at or before' the other though they differ. Sort result depends on input order.
**Common mistake / drift:** Claude uses sorted(key=...) instead of a comparator. The prompt asks for compare(); restate it.
