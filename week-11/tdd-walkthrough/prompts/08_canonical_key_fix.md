# 08 — The fix: stop comparing, start normalizing

**Why:** equal keys are a true equivalence by construction: reflexive, symmetric, transitive for free. Tradeoff: we only know the nicknames in our table.
**Slide:** Part 3, "Fix: canonical key". **Principle:** equivalence partitioning; witness / counterexample (the old one stays recorded).
**Recovery:** `tools/recover.sh 07`.

```prompt-a
Fix it without touching the three property tests. In merger/names.py add
NICKNAMES = {"jon": "jonathan", "john": "jonathan", "johnny": "jonathan", "jonny": "jonathan"},
canonical_key(full_name) = the nickname-normalized lowercase given name + " " + lowercase
family name, and redefine same_person(a, b) as canonical_key(a) == canonical_key(b).
Keep similar_names unchanged. Add a test that keeps the old counterexample on record:
transitive_failure(similar_names, SMITH_NAMES) == ("Jon Smith", "John Smith", "Jonathan Smith").
Run pytest: all green. Then print the canonical key of every name in SMITH_NAMES. Stop.
```

**What you should see:** all green; keys `jonathan smith` (x3), `maya smith`, `maria garcia`.

**Predict first (30 seconds, ask the room before running):** Will the three property tests pass now with no change to them?
**Expected answer:** Yes. Equal keys are an equivalence by construction. Tradeoff: only nicknames in the table are known.
**Common mistake / drift:** Claude edits the property tests to pass. Say: "do not edit the tests".
