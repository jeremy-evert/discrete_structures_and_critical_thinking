# 09 — The other fix: group by chains (union-find) and its tradeoff

**Why:** when you have no key, link everything connected by any chain of matches. The result is an equivalence, but it can join people who never matched directly.
**Slide:** Part 3, "Alternative: group by chains". **Principle:** equivalence partitioning; witness / counterexample.
**Recovery:** red = `tools/recover.sh 08`; green = `tools/recover.sh 09`.

```prompt-a
Test first. Stub merger/grouping.py with group_by_chain(items, rel) raising NotImplementedError.
It returns a list of groups (each a list, first-seen order): items are in the same group when
linked by any chain of rel matches. Write tests/test_grouping.py:
1) group_by_chain(SMITH_NAMES, similar_names) == [["Jon Smith","John Smith","Jonathan Smith"],
   ["Maya Smith"], ["Maria Garcia"]];
2) "same group" is reflexive, symmetric and transitive over SMITH_NAMES (use the helpers);
3) tradeoff: Jon Smith and Jonathan Smith are NOT similar_names, yet share a group.
Run pytest, show it red, stop.
```

```prompt-b
Implement group_by_chain with union-find (connected components), no other dependencies.
Do not edit the tests. Run pytest: all green. Then print the groups for SMITH_NAMES. Stop.
```

**What you should see (green):** three groups: the three Smiths together, `Maya Smith`, `Maria Garcia`.

**Predict first (30 seconds, ask the room before running):** Which two names get grouped though they were never similar to each other?
**Expected answer:** Jon Smith and Jonathan Smith: joined through John Smith.
**Common mistake / drift:** Claude returns groups in another order. Recovery: tools/recover.sh 09.
