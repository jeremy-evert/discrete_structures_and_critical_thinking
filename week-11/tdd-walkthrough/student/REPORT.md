# REPORT: DSCT Thursday 10-29 student workbook

Run id `35500c603cc96e5accc3d0587a2c0c75` · Ivy / Foreman Intern · Claude Code / sonnet on maise · branch `ivy/dsct-thu-student-20261027` · base `origin/flo/dsct-w11-tue-deck` (`a40a7e4`).

**Terminal state: COMPLETE with stated limits** (see Limits; one decision for Jeremy). Not merged, not on main (DSCT feeds a deploy). No Canvas, no student data.

## What was built (all under `week-11/tdd-walkthrough/student/`)

| Deliverable | Files |
|---|---|
| Parallel problem ("clean up a playlist"), synthetic data | `starter/` (what students get), `instructor-only/reference/` (solution) |
| Reference solution on a commit ladder | tags `student-ref-step-01` … `19`, same ladder numbering as Anna's `tdd-step-NN`; `instructor-only/ladder_check.sh` |
| Step 01–03 reference demos | `instructor-only/reference/demos/` + recorded output, `check_demos.sh` |
| Student workbook | `WORKBOOK.md`, `WORKBOOK.pdf` (17 pp), numbered 01–14 like Anna's `STEPS.md` prompts |
| Glossary | `GLOSSARY.md/.pdf` (aligned to the terms in Anna's handout glossary: test, assert, red/green, TDD, stub, fixture, relation, ordered pair, equivalence, partial order, partition/bin, boundary, property test, witness/counterexample, canonical key, design smell, dependency) |
| Facilitator page | `FACILITATOR.md/.pdf` |
| Evidence | `instructor-only/dry-run/*`, `instructor-only/review/*` |

Design as asked: concrete-before-abstract pictures per beat, why-before-how (soup, smoke alarm), one new idea per step, every step ends in visible red/green, PREDICT–RUN–EXPLAIN every step, red normalised, terms defined in place. Students write their own predictions, the Step 07 witness (they choose the three lengths; the starter deliberately contains none), and the One-Sentence Summary. Claude is allowed for code; an honesty log separates "AI proposed" from "we verified".

## Acceptance checks

| Check | Result |
|---|---|
| `pytest` red at each red tag, green at each green tag, clean clone | **Pass.** `ladder_check.sh`: 19/19 `ok` (e.g. 01 `5 failed`, 06 `1 failed, 17 passed`, 07 `20 passed`, 19 `37 passed`). Run on Python 3.14.4 only. |
| Transitivity counterexample is a committed failing test before the fix | **Pass.** Tag 06 fails with `not transitive: 1 ~ 2 and 2 ~ 3, but 1 !~ 3 (lengths 200, 204, 208)`; tag 07 is green and keeps the old counterexample as a test. |
| Step 01–03 demos reproduce the stated outputs | Pass (`check_demos.sh`). |
| Starter equals reference before students add anything | Pass (`check_starter.sh`, comments ignored). |
| Dry run as a student (fresh Claude, workbook only) | Two runs, logs in `instructor-only/dry-run/`. Run 1 (workbook v0, Steps 1–19): every red/green matched; workbook alone sufficed, but 10 gaps found. Run 2 (v2, fast path + Steps 09–14): every red/green matched, 27 passed at end; 7 further gaps found. **All listed gaps fixed** except those under Limits. The "student" and the "coach" were the same model, so this tests the text and the code path, not a human novice. |
| Fresh-eyes read for unexplained terms; glossary completeness | One read of v2 (`dry-run/fresh_eyes_workbook_v2.md`, ~45 terms, 22 stuck points, 16 leaks). Fixed: Step 03 leak of the witness lengths (replaced the relation), glossary leak and wrong "gap of 5", backwards "leaves first" sentence, missing definitions (A3b box, Python words, terminal, pip, listing), glossary step numbers re-mapped, missing glossary rows added. **Not re-read after the fixes**, so completeness is not independently re-verified. |
| Adversarial review (Sandy/Sol, Codex) | Receipt 1 on `d3a4e8b`: **REPAIR** (3 repairs: stale step numbers, timing note, `ladder_check.sh` silent success on clone failure). All repaired in `1ac43b6`. Receipt 2 on `1ac43b6`: **REPAIR** (one finding: the glossary still gave the 200/204/208 witness; fixed after the receipt in the next commit). A third Sandy pass was **not** run, so there is no CLEAR receipt for the final commit; none is needed because nothing here self-merges. |
| Pushed with tip SHA and tag list | See Tip below. |
| Python 3.9+ | Reference avoids newer syntax (no `match`, no `X | Y` types, no walrus); **only run on 3.14**, 3.9 not installed on maise. |

## Fit with the existing Thursday plan (stated plainly; nothing existing was edited)

- Extends `week-11/instructor/thursday-run-of-show.md` in the same six-block shape; the 75-minute table replaces the "compare representations" block with the pair build. The run-of-show table itself totals 85 minutes against a 75-minute meeting; the facilitator page flags that.
- **Conflict needing Jeremy's call:** the run-of-show says "Do not require code or driver/navigator roles." The workbook makes code the default with a paper path (Steps 01–03, 07, summary). Facilitator page §1 row 1.
- `assignments/pair-reasoning-report.md` is marked RETIRED (Decision 029) while `week-11/README.md` still says to submit it; unresolved, flagged (row 3). The workbook's fields map onto the six report fields (§5).
- Checkpoint 2 stays individual; workbook output feeds its items 3 and 4.

## Limits and what is missing

1. **Time.** The model dry runs estimate 50 min for the fast path (01, 06, 07, 08) alone and 65–75 with setup and write-up, longer than the 30-minute build slot; the full 14 steps about 3 hours. The class plan is therefore the fast path, with Step 08 finishable on the projector. Nothing was timed with real students.
2. Steps 02–05 and 09–14 are written and dry-run, but are homework or later by design.
3. Anna's `STEPS.md`/prompts landed during the run; I aligned numbers and glossary terms to them but did not diff against her final guide (`INSTRUCTOR_GUIDE.md`) or prompts text beyond `STEPS.md`, `STUDENT_HANDOUT.md`, `00_session_rules.md`. Her glossary wording is matched where the handout states it.
4. PDFs are rendered via headless Chromium from Markdown; I checked text extraction and page counts, not every page visually.
5. Python 3.9 untested (above). Sandy's sandbox was read-only, so her own runs of the checkers failed; her static checks stand, mine ran the checkers.
6. Evidence-Sheet pages are inside the workbook; there is no separate printable sheet.

## Tip and tags

See `jobs/ivy/reports/35500c603cc96e5accc3d0587a2c0c75/chain_report.md` for the final tip SHA, tag list and Sandy receipt 2. Tags: `student-ref-step-01` … `student-ref-step-19` (pushed).
