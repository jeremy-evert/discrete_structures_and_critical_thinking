# 14 — A cycle: no first thing to test

**Why:** if two functions need each other, the order stops being a partial order (antisymmetry breaks) and there is no leaf to test first. That is a design smell, and the code should say so.
**Slide:** Part 3, "Piece 8: cycles are a smell". **Principle:** antisymmetric property test; partial-order test ordering; witness / counterexample.
**Recovery:** red = `tools/recover.sh 18`; green = `tools/recover.sh 19`.

```prompt-a
Test first. In merger/deps.py add class CycleError(Exception). Write tests/test_cycles.py with
LOOP = {"parse": {"validate"}, "validate": {"parse"}, "report": {"validate"}}:
(1) leaves_first(LOOP) raises CycleError whose message contains "parse" and "validate";
(2) using the transitive-closure code from test_dependencies.py (import it:
from test_dependencies import closure; if there is no function called closure, extract it there
first without changing behaviour), antisymmetric_failure on LOOP's closure is ("parse","validate").
Run pytest. The cycle test should fail (the second test may already pass: say so). Stop.
```

```prompt-b
Make leaves_first detect cycles: track the current path and raise CycleError with a message like
"dependency cycle: parse -> validate -> parse". Do not edit the tests. Run pytest: all green.
Then print the message for LOOP. Stop.
```

**What you should see (green):** `dependency cycle: parse -> validate -> parse`.

**Predict first (30 seconds, ask the room before running):** If parse needs validate and validate needs parse, which do we test first?
**Expected answer:** Neither. No first item exists; the order is not a partial order. That is a design smell, and the error says so.
**Common mistake / drift:** Claude loops forever or silently orders it. The red test catches both.
