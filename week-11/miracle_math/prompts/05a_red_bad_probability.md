We are doing strict TDD in Python with unittest, in week-11/miracle_math/ only.
Files: miracle_math.py, test_miracle_math.py, TESTING_MAP.md.

Do exactly ONE RED step for row 5 of TESTING_MAP.md (bad input):

1. Run `python -m unittest -v` and show the output BEFORE changing anything.
2. Add ONE new test class to test_miracle_math.py named TestAtLeastOnceRejectsBadInput
   with exactly one test:
   test_probability_above_one_raises_value_error:
       with self.assertRaises(ValueError):
           chance_at_least_once(1.5, 3)
   Do NOT change existing tests. Do NOT touch miracle_math.py.
3. BEFORE running, predict RED or GREEN in one sentence. Then say what the
   function currently returns for (1.5, 3) and why that number is nonsense
   as a probability.
4. Run `python -m unittest -v` and show the output. Confirm it is a FAIL
   (wrong behavior), not an ERROR (could not run), and explain the difference
   in one sentence.
5. Update row 5 of TESTING_MAP.md: set Status to RED. Leave Commit blank.
   Do not change any other row.
6. Show `git status --short -- .` and `git diff -- .`
7. Stop. Do not fix the code. Do not commit.

Rules:
- Expressive names, no comments that restate the code, no clever one-liners.
- Never stage __pycache__ or .bak files. Never touch files outside week-11/miracle_math/.
