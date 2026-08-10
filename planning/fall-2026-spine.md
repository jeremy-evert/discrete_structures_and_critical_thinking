# Discrete Structures and Critical Thinking — Fall 2026 17-Week Planning Spine

**Status: planning spine, not finished curriculum.** This document exists so
`course_foundry` prompt 045 (the shared Week-at-a-Glance landing-page
system) has real semester structure to build against. This is a
structural mapping of the 14 existing topic lessons in `lessons/` onto 17
real Fall 2026 weeks — it does NOT author new daily lecture/topic content.
Every week below either points at an existing `lessons/NN-*.md` file
verbatim or is marked `TBD`/`placeholder` honestly.

DSCT meets **Tuesday/Thursday, 12:30–1:45 PM** (COMSC-2043-1420) — this
spine is Tuesday/Thursday dated, not Monday/Wednesday/Friday. There was
previously no dated calendar for this course at all (`docs/planning/` is
empty except a `.gitkeep`); this file is the first one.

## Holiday impact recomputed for T/Th (not copied from the M/W/F spine)

Real Fall 2026 facts, same source facts as `computer_science_1/planning/
block-map.md`, recomputed here for Tuesday/Thursday specifically because
T/Th holiday impact is NOT the same as M/W/F:

- **Labor Day, Mon Sep 7** — does not fall on a Tuesday or Thursday. No
  T/Th class is affected.
- **Fall Break begins Wed Oct 14, 10 PM** — Tuesday Oct 13 meets normally
  (before the break starts). **Thursday Oct 15 falls inside the break** —
  no Thursday class that week.
- **Thanksgiving begins Tue Nov 24, 10 PM** — Tuesday Nov 24's class meets
  normally (break starts that evening, after the 12:30–1:45 PM class).
  **Thursday Nov 26 is Thanksgiving Day** — no Thursday class that week.
- **Finals Dec 7–11** — week 17; the section's Tuesday/Thursday final
  exam days fall inside that week.

## 14-lesson-to-15-teaching-week allocation

17 weeks total: Week 1 is the universal cross-course kickoff (no DSCT
lesson content), Week 17 is finals. That leaves 15 teaching weeks
(Weeks 2–16) for the 14 lessons in `lessons/01-*.md` through `14-*.md`.
Allocation: one lesson per week, Weeks 2–15 (14 weeks, 14 lessons,
1:1) — the cleanest honest mapping, no lesson split across weeks and no
week left contentless. Week 16 becomes a review/integration buffer before
finals (matches the same "review week before finals" pattern
`computer_science_2`'s spine and `computer_architecture`'s spine both
already use). This is a planning choice, not a fact drawn from any
existing dated source — flagged as such.

## Spine table

| Week | Dates (Tue/Thu) | Topic | Status | Notes |
|---|---|---|---|---|
| 1 | Aug 18 / Aug 20 | Universal course kickoff (`semester_kickoff_week`) | planned | Same universal kickoff content CS1/CS2/Architecture Week 1 uses; no DSCT-specific lesson content this week. |
| 2 | Aug 25 / Aug 27 | `lessons/01-orientation-and-learning-practice.md` | placeholder | Daily content TBD — lesson skeleton exists, no dated Canvas content built. |
| 3 | Sep 1 / Sep 3 | `lessons/02-logic-proofs-and-sequences.md` | placeholder | TBD. |
| 4 | Sep 8 / Sep 10 | `lessons/03-functions-and-matrices.md` | placeholder | TBD. |
| 5 | Sep 15 / Sep 17 | `lessons/04-algorithms.md` | placeholder | TBD. |
| 6 | Sep 22 / Sep 24 | `lessons/05-cryptography.md` | placeholder | TBD. |
| 7 | Sep 29 / Oct 1 | `lessons/06-recursion.md` | placeholder | TBD. |
| 8 | Oct 6 / Oct 8 | `lessons/07-counting.md` | placeholder | TBD. |
| 9 | Oct 13 / ~~Oct 15~~ | `lessons/08-probability.md` | placeholder | No Thursday meeting — Fall Break begins Wed Oct 14, 10 PM. |
| 10 | Oct 20 / Oct 22 | `lessons/09-relations.md` | placeholder | TBD. |
| 11 | Oct 27 / Oct 29 | `lessons/10-graphs.md` | placeholder | TBD. |
| 12 | Nov 3 / Nov 5 | `lessons/11-trees.md` | placeholder | TBD. |
| 13 | Nov 10 / Nov 12 | `lessons/12-boolean-algebra.md` | placeholder | TBD. |
| 14 | Nov 17 / Nov 19 | `lessons/13-finite-state-machines.md` | placeholder | TBD. |
| 15 | Nov 24 / ~~Nov 26~~ | `lessons/14-synthesis-and-applications.md` | placeholder | No Thursday meeting — Thanksgiving Day. Tuesday meets normally. |
| 16 | Dec 1 / Dec 3 | Review & integration buffer | placeholder | No lesson file maps here by design — buffer before finals. Content TBD. |
| 17 | Dec 7–11 | Finals week | planned | Final exam days fall inside this week; assignment/exam structure not yet built. |

## Explicitly not yet decided (flag, don't fabricate)

- **No daily granularity beyond the lesson title:** each lesson file gives
  Objectives/Key content/Historical materials, not a Tuesday-vs-Thursday
  split. This spine repeats the same lesson topic across both meeting days
  of its week rather than inventing a two-part breakdown the source doesn't
  contain.
- **Assignments/quizzes tie-in:** `assignments/`, `quizzes/`,
  `monday_moments/`, and `reflections/` exist as topic-shaped content, not
  week-dated content. No attempt is made here to assign them to specific
  weeks — that is future content-authoring work, not this spine.
- **Week 16's buffer content and Week 17's finals structure** are both
  genuinely undecided; marking them `placeholder` is the honest state, not
  a stand-in for real content this document is hiding.
