# 04 — Bins and boundaries (first red, first green)

**Why:** scores in the same bin behave the same, so one test per bin plus both sides of each boundary covers 101 possible inputs.
**Slide:** Part 3, "Piece 1: letter_grade" (red slide, then green slide). **Principle:** equivalence partitioning, boundaries.
**Recovery:** red state = `tools/recover.sh 01`; green state = `tools/recover.sh 02`.

```prompt-a
Test first. Create merger/__init__.py (empty), a stub merger/grades.py whose
letter_grade(score) just raises NotImplementedError, and tests/test_grades.py.
Spec: 90-100 A, 80-89 B, 70-79 C, 60-69 D, 0-59 F; scores outside 0-100 raise ValueError.
Tests: one parametrized test covering each bin and both sides of every boundary
(59/60, 69/70, 79/80, 89/90) plus 0 and 100, and a test that -1 and 101 raise ValueError.
Run pytest and show me. Every test must be red. Do not implement letter_grade. Stop.
```

**What you should see (red):** all tests FAILED with `NotImplementedError`.

```prompt-b
Now make those tests pass with the simplest correct letter_grade. Do not edit the tests.
Run pytest and show me it is all green. Then print the bins: for each letter, the lowest
and highest score 0..100 that gets it. Stop.
```

**What you should see (green):** all passed; bins A 90-100, B 80-89, C 70-79, D 60-69, F 0-59.

**Predict first (30 seconds, ask the room before running):** Run it red: what will pytest say? Why must it fail before we write code?
**Expected answer:** Every test fails with NotImplementedError. A test that cannot fail proves nothing; red shows the test is able to notice a missing feature.
**Common mistake / drift:** Claude writes the implementation in the red step. Say: "delete that, stub only".
