# 07 — The bug: matching is not transitive (red with a counterexample)

**Why:** if Jon is Johns' duplicate and John is Jonathan's, "same person" must also join Jon and Jonathan. The property test finds the break and names it.
**Slide:** Part 3, "Piece 3: same_person must be transitive". **Principle:** transitive property test; witness / counterexample.
**Recovery:** `tools/recover.sh 06`.

```prompt-a
Add tests/fixtures.py with SMITH_NAMES = ["Jon Smith", "John Smith", "Jonathan Smith",
"Maya Smith", "Maria Garcia"]. In merger/names.py add: same_person = similar_names
(our first-draft rule for "same person"). Write tests/test_transitivity.py: same_person must
be reflexive, symmetric and transitive over SMITH_NAMES, using the helpers in
tests/relations.py (import them with: from relations import ...). The transitive test must
fail with an assert message (assert witness is None, f"...") "'A' ~ 'B' and 'B' ~ 'C' but 'A' !~ 'C'" filled in from the witness.
Run pytest and show me the failure. Do not fix anything. Stop.
```

**What you should see:** exactly one failure, the transitive test, with `'Jon Smith' ~ 'John Smith' and 'John Smith' ~ 'Jonathan Smith' but 'Jon Smith' !~ 'Jonathan Smith'`. The other two pass.

**Predict first (30 seconds, ask the room before running):** Name three names where A~B and B~C but A is not ~C.
**Expected answer:** Jon, John, Jonathan. The test finds exactly this triple. A red test with a witness is the test doing its job.
**Common mistake / drift:** Claude fixes the code anyway. Say: "stop; leave it red; show me only the failure".
