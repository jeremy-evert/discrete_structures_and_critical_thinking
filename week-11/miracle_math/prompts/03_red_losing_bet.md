We are doing strict TDD in Python with unittest, in week-11/miracle_math/ only.
Files: miracle_math.py, test_miracle_math.py, TESTING_MAP.md.

Do exactly ONE RED step for row 3 of TESTING_MAP.md:

1. Run `python -m unittest -v` and show the output BEFORE changing anything.
2. Add exactly ONE test to the TestAtLeastOnce class in test_miracle_math.py:
   name: test_de_mere_double_six_in_twenty_four_rolls_is_a_losing_bet
   body: chance = chance_at_least_once(1 / 36, 24)
         self.assertLess(chance, 0.5)
   Do NOT change any existing test. Do NOT touch miracle_math.py.
3. BEFORE running, write one sentence predicting RED or GREEN, and why.
4. Run `python -m unittest -v` and show the output.
5. If the new test is GREEN immediately, prove it is not a weak test:
   a. Temporarily change 24 to 25 in that test only.
   b. Run the tests and show that it FAILS. Print the actual chance value.
   c. Change 25 back to 24.
   d. Run the tests and show that everything is GREEN again.
6. Update row 3 of TESTING_MAP.md: set Status to GREEN. Leave Commit blank.
   Do not change any other row.
7. Show `git status --short -- .` and `git diff -- .`
8. Stop. Do not write the next test. Do not commit.

Rules:
- Expressive names, no comments that restate the code, no clever one-liners.
- Never stage __pycache__. Never touch files outside week-11/miracle_math/.
- When I later ask you to commit, commit test_miracle_math.py and TESTING_MAP.md
  together in ONE commit, plus miracle_math.py only if it changed.
