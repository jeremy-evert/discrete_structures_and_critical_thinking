# 12 — Put it together: merge_duplicates

**Why:** the pieces now combine. Records with equal keys merge; nothing is lost or counted twice; input order does not matter.
**Slide:** Part 3, "Piece 6: merge_duplicates". **Principle:** equivalence partitioning (the classes are the merged records).
**Recovery:** red = `tools/recover.sh 14`; green = `tools/recover.sh 15`.

```prompt-a
Test first. Stub merger/pipeline.py with merge_duplicates(records) raising NotImplementedError.
It returns Merged(ids, name, email) tuples (a namedtuple), one per group of duplicates, sorted
by ids; ids is the sorted tuple of the members' ids; name and email come from the lowest-id member.
Write tests/test_pipeline.py with RECORDS: (1) the result as (ids, name) pairs is
[((1,),"Jon Smith"), ((2,3),"John Smith"), ((4,),"Maya Smith"), ((5,),"Maria Garcia")];
(2) every input id appears in exactly one merged record; (3) merge_duplicates(RECORDS) equals
merge_duplicates(list(reversed(RECORDS))). Run pytest, show it red, stop.
```

```prompt-b
Implement it in merger/pipeline.py with exactly these module-level functions:
duplicate_key(record) = (canonical_key(record.name), record.email); group_records(records)
groups by duplicate_key calling duplicate_key; merge_group(group); and merge_duplicates calling
group_records and merge_group. Do not edit the tests. Run pytest: all green. Then print
merge_duplicates(RECORDS), one line each. Stop.
```

**What you should see (green):** four lines; Jon alone (no email), John+Jonathan merged as ids (2, 3).

**Predict first (30 seconds, ask the room before running):** How many merged records come out of five input records?
**Expected answer:** Four: John and Jonathan merge (ids 2, 3); Jon has no email so stays apart.
**Common mistake / drift:** Claude changes merge rules. Recovery: tools/recover.sh 15.
