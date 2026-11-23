We are doing strict TDD in Python with unittest, in week-11/miracle_math/ only.
Files: miracle_math.py, test_miracle_math.py, TESTING_MAP.md.

Do exactly ONE step for row 4 of TESTING_MAP.md (edge cases):

1. Run `python -m unittest -v` and show the output BEFORE changing anything.
2. Add ONE new test class to test_miracle_math.py named TestAtLeastOnceEdgeCases
   with exactly three tests:
   test_zero_tries_never_succeeds:        chance_at_least_once(0.5, 0) is 0
   test_impossible_event_never_happens:   chance_at_least_once(0, 100) is 0
   test_certain_event_always_happens:     chance_at_least_once(1, 3) is 1
   Use assertAlmostEqual(places=10). Do NOT change existing tests.
3. BEFORE running, write one sentence per test predicting RED or GREEN, and why.
4. Run `python -m unittest -v` and show the output.
5. If they pass immediately, prove they are not weak tests:
   a. Copy miracle_math.py to miracle_math.py.bak.
   b. Temporarily replace the body of chance_at_least_once with:
      expected_count = number_of_tries * chance_per_try
      return expected_count
   c. Run the tests. Show which tests FAIL and the actual values they got.
   d. Explain in 2 sentences why n * p is an expected COUNT, not a PROBABILITY,
      and why it can be bigger than 1.
   e. Restore miracle_math.py from miracle_math.py.bak, then delete the .bak file.
   f. Run `git diff -- miracle_math.py` and confirm it is EMPTY.
   g. Run the tests and show everything GREEN.
6. Update row 4 of TESTING_MAP.md: set Status to GREEN. Leave Commit blank.
   Do not change any other row.
7. Show `git status --short -- .` and `git diff -- .`
8. Stop. Do not write the next test. Do not commit.

Rules:
- Expressive names, no comments that restate the code, no clever one-liners.
- Never stage __pycache__ or .bak files. Never touch files outside week-11/miracle_math/.
- When I later ask you to commit, commit test_miracle_math.py and TESTING_MAP.md
  together in ONE commit, plus miracle_math.py only if it changed.
