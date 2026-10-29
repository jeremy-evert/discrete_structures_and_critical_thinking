# 06 — The fuzzy rule: "looks alike enough"

**Why:** the merger needs a first rule for "same person". We write the obvious one, a fuzzy name match, test-first.
**Slide:** Part 3, "Piece 2: similar_names" (red, green). **Principle:** equivalence partitioning (names of one person form a bin).
**Recovery:** red = `tools/recover.sh 04`; green = `tools/recover.sh 05`.

```prompt-a
Test first. Create a stub merger/names.py with similar_names(a, b) raising NotImplementedError,
and tests/test_similarity.py. Names are "Given Family". Spec: two names are similar when the
family names are equal (ignoring case) and the given names' closeness is at least 0.5, where
closeness = 1 - edit_distance(given_a, given_b) / max(len of the two given names), lowercase.
Tests: "Jon Smith" ~ "John Smith"; "John Smith" ~ "Jonathan Smith";
"Jon Smith" is NOT similar to "Maria Garcia"; NOT similar to "Jon Jones"; case does not matter
("jon smith" ~ "JON SMITH"). Run pytest, show it red, stop.
```

```prompt-b
Implement similar_names. In merger/names.py put: a helper _split(full_name) returning the
lowercase (given, family) pair; edit_distance(a, b), the usual insert/delete/substitute count;
THRESHOLD = 0.5; and similar_names. Do not edit the tests. Run pytest: all green. Then print
similar_names for every pair among Jon Smith, John Smith, Jonathan Smith. Stop.
```

**What you should see (green):** Jon~John True, John~Jonathan True, **Jon~Jonathan False**. Point at that last line; it is the setup for the next step.

**Predict first (30 seconds, ask the room before running):** Will 'Jon' and 'Jonathan' count as similar?
**Expected answer:** Surprise: no (closeness about 0.375). Jon~John and John~Jonathan are yes. Write the guess on the board before running.
**Common mistake / drift:** Edit distance written differently gives other numbers. Recovery: tools/recover.sh 05.
