# 05 — The bins ARE an equivalence relation (and our reusable checkers)

**Why:** "lands in the same bin" is reflexive, symmetric, transitive. We also build the relation checkers that every later step reuses.
**Slide:** Part 3, "Piece 1b: bins are an equivalence". **Principle:** equivalence partitioning; reflexive/symmetric/transitive property tests.
**Recovery:** `tools/recover.sh 03`.

```prompt-a
Add tests/relations.py with four helpers, each taking (rel, items) where rel(a, b) -> bool:
reflexive_failure, symmetric_failure, antisymmetric_failure, transitive_failure.
Each returns None if the property holds, else the first witness tuple, trying items in order
with itertools.product: (a,) / (a, b) / (a, b) with a != b / (a, b, c).
Then tests/test_grade_relation.py: same_bin(a, b) is letter_grade(a) == letter_grade(b).
Over scores range(0, 101, 3) plus 59, 60, 69, 70, 79, 80, 89, 90, 100, assert it is
reflexive, symmetric and transitive using the helpers; also assert scores 0..100 land in
exactly five distinct letters. Run pytest and show me. These should pass immediately.
```

**What you should see:** all green on the first run. Say aloud: "This test passed at once. That is allowed here: it records a fact."

**Predict first (30 seconds, ask the room before running):** This test is about to pass on its first run. Is that a problem?
**Expected answer:** Not here: it records a fact about code we already wrote. A first-run pass for NEW behaviour is a warning sign (the test may be too weak).
**Common mistake / drift:** Claude tests only one pair. Ask for 'every pair among these scores'.
