We are doing strict TDD in Python with unittest, in week-11/miracle_math/ only.

Do exactly ONE GREEN step for row 5 of TESTING_MAP.md:

1. Run `python -m unittest -v` and show the RED output BEFORE changing anything.
2. Make the SMALLEST change to chance_at_least_once in miracle_math.py that
   makes ALL tests pass. Only handle what the tests demand: a probability
   above 1. Do NOT also check for negative numbers; no test asks for that yet.
   Use a clear error message such as "chance_per_try must be between 0 and 1".
   Do NOT edit test_miracle_math.py.
3. Run `python -m unittest -v` and show everything GREEN.
4. In one sentence, name a bad input that would still sneak through, and
   suggest the test that would catch it. Do not write that test.
5. Update row 5 of TESTING_MAP.md: set Status to GREEN. Leave Commit blank.
6. Show `git status --short -- .` and `git diff -- .`
7. Stop. Do not commit.

Rules:
- Expressive names, no comments that restate the code, no clever one-liners.
- When I ask you to commit, commit miracle_math.py, test_miracle_math.py,
  TESTING_MAP.md, and prompts/05a_red_bad_probability.md and
  prompts/05b_green_bad_probability.md together in ONE commit.
