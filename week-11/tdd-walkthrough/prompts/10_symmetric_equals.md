# 10 — Records and a one-sided "equals"

**Why:** a first-draft `is_duplicate` treats a missing email as "matches anything" from one side only. The symmetry test shows a concrete pair.
**Slide:** Part 3, "Piece 4: is_duplicate must be symmetric". **Principle:** reflexive and symmetric property tests; witness / counterexample.
**Recovery:** red = `tools/recover.sh 10`; green = `tools/recover.sh 11`.

```prompt-a
Test first. Add merger/records.py: a frozen dataclass Record(id: int, name: str,
email: Optional[str] = None) and the first-draft is_duplicate(a, b) =
same_person(a.name, b.name) and (a.email is None or a.email == b.email).
Add to tests/fixtures.py: RECORDS = [Record(1,"Jon Smith"), Record(2,"John Smith","js@example.edu"),
Record(3,"Jonathan Smith","js@example.edu"), Record(4,"Maya Smith","maya@example.edu"),
Record(5,"Maria Garcia","mg@example.edu")]. Write tests/test_record_equals.py: is_duplicate must
be reflexive and symmetric over RECORDS (use the helpers); the symmetric failure message names both
records. Run pytest. Exactly the symmetric test should fail. Show me and stop.
```

```prompt-b
Fix is_duplicate so swapping a and b can never change the answer: same_person on the names AND
a.email == b.email. Do not edit the tests. Run pytest: all green. Then print is_duplicate for
Record 1 vs Record 2 and Record 2 vs Record 1. Stop.
```

**What you should see (green):** both directions print `False` (a missing email is no longer a wildcard).

**Predict first (30 seconds, ask the room before running):** Record 1 has no email. Which direction says 'duplicate' and which says 'not'?
**Expected answer:** is_duplicate(1,2) is True (missing email matches anything), is_duplicate(2,1) is False. Same two records, different answers.
**Common mistake / drift:** Claude makes the test pass by checking both directions inside is_duplicate. Ask for 'emails must be equal'.
