# Relations in your tests: a live test-driven walkthrough

**What this is and why.** Students often can't connect words like *equivalence*, *partial order*, *reflexive*, *symmetric*, *antisymmetric* and *transitive* to real problems. This folder lets you teach them by building a small Python program live, one tiny test at a time, so the class watches every idea earn its place. The program merges duplicate student records (synthetic names only: Jon / John / Jonathan Smith). Each step runs the same loop: **Predict** (guess), **Run** (see red or green), **Explain** (say why). Red tests are normal and good. Tuesday: Jeremy demonstrates with Claude. Thursday: students repeat the process on a parallel problem.

## START HERE (reading order)
1. This README.
2. [`STEPS.md`](STEPS.md): the 15 steps on one page.
3. [`INSTRUCTOR_GUIDE.md`](INSTRUCTOR_GUIDE.md): what to say, ask, type, with minutes and a 75-minute cut.
4. [`prompts/00_session_rules.md`](prompts/00_session_rules.md), then `prompts/01_...` through `14_...`: the exact text you paste into Claude.
5. `deck/`: the slides (separate session; see status below).
6. `student/`: Thursday student workbook (Ivy's lane; see status below).

## Folder map
| Folder / file | What is in it |
|---|---|
| `merger/` | the Python program as it stands at the tip (the finished answer) |
| `tests/` | its tests (pytest) |
| `prompts/` | numbered classroom prompts 00 to 14 and their README |
| `reference/demos/` | known-good copies of the three demo scripts (prompts 01 to 03) |
| `tools/` | `recover.sh` (restore a known-good step) and `ladder_check.sh` (check every step) |
| `deck/` | Beamer slides and notes (not on this branch yet) |
| `student/` | Thursday workbook (not on this branch yet) |
| `STUDENT_HANDOUT.md`, `CONCEPT_MAP.md` | one-page handout with glossary; concept table |
| `REPORT.md` | status, ladder output, dry-run table |

## Commands
Get the branch (once):
```bash
git clone git@github.com:jeremy-evert/discrete_structures_and_critical_thinking.git dsct
cd dsct && git fetch --tags && git checkout anna/dsct-tdd-relations-20261027
cd week-11/tdd-walkthrough && python3 -m pip install -r requirements.txt   # needs Python 3.9+
```
Step the ladder (19 tagged steps; odd/even pairs are red then green):
```bash
git checkout tdd-step-06        # a red step: one test fails on purpose
python3 -m pytest -q            # see the red
git checkout tdd-step-07        # the fix
python3 -m pytest -q            # see the green
git switch anna/dsct-tdd-relations-20261027   # back to the branch tip (finished program)
```
(`python` instead of `python3` if that is what your machine calls it.)

Recover during a live class (Claude's output drifted): in your live folder run
```bash
LADDER_REPO=~/dsct tools/recover.sh 07     # restores merger/ and tests/ to tdd-step-07
```
Check every step at once, from a clean copy: `tools/ladder_check.sh` (prints pass/fail counts per tag).

## Building the deck PDFs
Slides and speaker notes build as two separate PDFs from one `.tex`: `cd deck && ./build.sh` (the same pattern as `presentations/beamer/week11_tue_relations/build.sh`). Needs `pdflatex`. Status below.

## Status (updated 2026-10-27 11:05 CDT)
| Deliverable | Status |
|---|---|
| Project + 19-tag commit ladder | done, verified by `ladder_check.sh` (11:00) |
| `STEPS.md` | done |
| Prompts 00 to 14 | done; independent dry run 21 of 23 phases matched, wording fixed afterwards, fixes not yet re-run |
| `INSTRUCTOR_GUIDE.md` | done; fresh-eyes read pending |
| `STUDENT_HANDOUT.md`, `CONCEPT_MAP.md` | done |
| `REPORT.md` | done, open items listed |
| `deck/` slides + notes | in progress: other session (`anna-dsct-tdd-deck`), due 12:00 first usable, 16:00 final |
| `student/` Thursday workbook | in progress: Ivy (branch `ivy/dsct-thu-student-20261027`) |

## Who to ask
Flo (lead foreman) for priorities and decisions; Anna (this lane: project, ladder, prompts, guide, dry run); Ivy (Thursday student workbook); Jeremy decides when it runs (Tuesday core cut, two sessions, Thursday 10-29, or later).
