# Miracle Math: Rules for Claude

We are teaching strict TDD in Python with unittest to beginner students.
Work ONLY inside week-11/miracle_math/.

## Files
- miracle_math.py: the code
- test_miracle_math.py: the tests
- TESTING_MAP.md: the test ladder. Every row has a Status (PLANNED, RED, GREEN) and a Commit hash.
- prompts/: one saved prompt per TDD step

## TDD rules
1. Do exactly ONE step per prompt: either RED or GREEN, never both.
2. RED: add exactly one test. Do not touch miracle_math.py.
3. GREEN: make the smallest change to miracle_math.py that passes ALL tests.
   Never edit tests to make them pass. Never add features no test asks for.
4. Before running tests, predict RED or GREEN in one sentence and say why.
5. Run `python -m unittest -v` before and after every change, and show the output.
6. If a new test passes immediately, prove it is not weak: temporarily break
   the code or the test, show it fails, restore it, and confirm `git diff` is clean.
7. Stop after the step. Do not start the next row.

## Code style
- Expressive names. Break formulas into named steps a beginner can read aloud.
- No comments that restate the code. No clever one-liners.
- Compare floats with assertAlmostEqual.

## Git rules
- Never commit unless I explicitly ask.
- When I ask, commit the test, the code it drove, TESTING_MAP.md, and that step's
  prompt file together in ONE commit.
- Never stage __pycache__ or .bak files. Never stage files outside this folder.
- Never rewrite history: no amend, no reset, no rebase.
