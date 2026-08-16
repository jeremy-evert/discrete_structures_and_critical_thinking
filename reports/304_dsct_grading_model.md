# Prompt 304 — DSCT grading model

## Foreman note on this report's history

The worker container ran this dispatch twice against the same shared
working tree (the first attempt was interrupted early by Foreman for
sharper instructions, but its process finished committing before the kill
fully landed — commit `9497896`). Its self-written report described that
first table. A second pass (commit `bad75e0`) then refined the table in
place based on the sharpened instructions (Jeremy's exact Tuesday/Thursday
mapping and explicit request to reuse CS1's small buckets), but the
worker's standing footer told it not to write a second report, so the
committed report described the superseded first table. Foreman rewrote
this report to describe the actual final `docs/grading-model.md` on this
branch, and reconciled one real inconsistency found during review — see
"Week 2 reconciliation" below.

## Deliverable

`docs/grading-model.md` — an explicit named-category table using CS1's
small-bucket treatment (5%-sized named categories rather than lump-sum
buckets), adapted to DSCT's real Tuesday/Thursday chassis and the
alternating Thursday Pair-Programming/Show-and-Tell rotation. Lands
exactly on Question 004's 45%/50%/5% aggregate.

## Full table (as committed, `bad75e0`)

| Category | Weight | Graded weeks / cadence |
|---|---:|---|
| Semester kickoff week | 5% | Week 1 |
| Monday Moment quiz (Tuesday AI Fluency touchpoint) | 5% | Weekly Tuesday, incl. Week 9 exception |
| Wacky Wednesday reflection (Tuesday Professional Minds strand) | 5% | Weekly Tuesday PM weeks |
| Fun Friday reflection (Thursday Professional Minds strand) | 5% | Weekly Thursday PM weeks, excl. Week 9 |
| Paired-programming report (A3 equivalent) | 5% | Pair Programming weeks: 3, 5, 7, 9 (pair-style), 11, 13 |
| Show-and-Tell reflection (A4 equivalent) | 5% | Show & Tell weeks: 4, 6, 8, 10, 12, 14 |
| Friday feedback report (A7 equivalent) | 5% | Show & Tell weeks: 4, 6, 8, 10, 12, 14 |
| Career artifact sequence | 5% | Recurring career-strand weeks as scheduled |
| Attendance & participation | 5% | Course cadence |
| Technical presentation/demo evidence | 3% | Weekly Tuesday technical presentation/demo slot |
| Course evaluation | 2% | End of term |
| Weekly reinforcement / Reasoning Odyssey gate | 30% | Weeks 3–14 formal sequence + Week 16 synthesis + Week 2 readiness/setup (see reconciliation below) |
| Reasoning Odyssey checkpoints | 15% | Selected checkpoint weeks within 3–14/16 |
| Final individual reflection | 5% | Week 17 |
| **Total** | **100%** | |

## Arithmetic check (independently re-verified by Foreman)

- 9 categories at 5% each (kickoff, AI Fluency, Wacky Wednesday, Fun Friday,
  A3, A4, A7, career artifact, attendance) = 45%.
- + technical presentation 3% + course evaluation 2% = 50%.
- + Weekly reinforcement/Odyssey gate 30% + checkpoints 15% = 45%.
- + final 5%.
- Total: 50% + 45% + 5% = **100%**. Confirmed correct.
- Reasoning Odyssey family alone: 30% + 15% = **45%**, matching Question
  004's aggregate exactly.
- Everything else recurring: 50%, final: 5% — both match Question 004.

## Week 2 reconciliation (Foreman, this pass)

CS2 sidecar Prompt 303 (dispatched before this grading table existed) used
the answered Question 004's original vaguer "50% recurring bucket"
language to grade DSCT's own Week 2 evidence portfolio (40 points: 20
Tuesday local-AI-readiness + 20 Thursday Container Connections). That
language is now stale against the named-category table above — none of
the specific 5%-weighted weekly-touchpoint categories (AI Fluency, PM
strands, A3/A4/A7) are the right fit, since those name *recurring
touchpoint types*, not the week's substantive technical-evidence work.

Resolved by mapping Week 2's evidence portfolio into the **Weekly
reinforcement / Reasoning Odyssey gate** category (30%) as the week's
readiness/setup entry — the same functional role that category plays for
Weeks 3–14's formal Odyssey gates (this week's substantive technical
evidence), even though Week 2 itself is setup rather than a formal Odyssey
topic. This mirrors CS2's own precedent: CS2's real graded Week 2 object
(the shared local-AI-lab readiness check) is likewise the week's
substantive evidence work, not one of CS2's specific weekly-touchpoint
categories. Updated both `docs/grading-model.md`'s Odyssey-gate row and
`week-02/student/week-02-evidence-assignment.md`'s points section to state
this explicitly.

## Chassis trace

Tuesday = Monday-Moment-equivalent AI Fluency + first Professional Minds
day (Wacky-Wednesday-equivalent) + technical presentation. Thursday =
second Professional Minds day (Fun-Friday-equivalent) + one rotating
technical activity (Pair Programming or Show & Tell, never both the same
week) — exactly Jeremy's own stated day-mapping. The technical
presentation gets its own small 3% category because it is a real, distinct
Tuesday chassis touchpoint, not folded into the Odyssey gate (which is
Thursday-anchored evidence/reasoning work in this model).

## Underspecified items (worker-flagged, not resolved here)

Exact career-artifact weeks and Reasoning-Odyssey-checkpoint weeks remain
to be scheduled in the course calendar — flagged, not guessed. The
existing `assignments/programming-exam.md` stub remains intentionally
unused as a grading category (inconsistent with Question 004's "not a
comprehensive exam" decision) — a separate known cleanup item.

## Validation

- No test suite applies to this planning-markdown-only repository.
- `git diff --check`: PASS (worker + Foreman's Week 2 reconciliation edits).
- Percentage arithmetic independently re-verified by Foreman (see above).
- Push attempt from the worker container was blocked (no `ssh` executable);
  Foreman pushes on the host.

## Foreman acceptance

Accepted with the Week 2 reconciliation above folded in.
