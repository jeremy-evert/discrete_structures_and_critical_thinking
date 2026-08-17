# COMSC-2043 — Grading Model (Fall 2026 source model)

This is the DSCT source model for a 100% grade. It uses the small named
category treatment established by CS1/CS2, adapted to DSCT's Tuesday/Thursday
chassis. It is a source document; no Canvas, Savnac, or student-system write
is implied.

## Final weights

| Category | Weight | Canvas/Savnac object shape | Graded weeks |
|---|---:|---|---|
| Semester kickoff week | 5% | Shared kickoff assignment group / exit-ticket objects | Week 1 |
| Monday Moment quiz (Tuesday AI Fluency touchpoint) | 5% | Short quiz or text-entry object using shared AI Fluency content | Weekly Tuesday touchpoint, including the Tuesday-only Week 9 exception |
| Wacky Wednesday reflection (Tuesday Professional Minds strand) | 5% | Professional Minds reflection object | Weekly Tuesday Professional Minds weeks |
| Fun Friday reflection (Thursday Professional Minds strand) | 5% | Professional Minds reflection object | Weekly Thursday Professional Minds weeks, excluding the Week 9 break |
| Pair Reasoning report (A3 equivalent) | 5% | Individual text-entry/upload report with rubric | Pair Reasoning weeks: 3, 5, 7, 9 pair-style work, 11, 13 |
| Show-and-Tell reflection (A4 equivalent) | 5% | Individual text-entry/upload reflection with rubric | Show & Tell weeks: 4, 6, 8, 10, 12, 14 |
| Friday feedback report (A7 equivalent) | 5% | Individual critique/revision/evidence receipt with rubric | Show & Tell weeks: 4, 6, 8, 10, 12, 14 |
| Career artifact sequence | 5% | Connected artifact/update uploads with rubric; may be attached to the active Odyssey evidence package | Recurring career-strand weeks as scheduled; not a comprehensive exam |
| Attendance & participation | 5% | Instructor-entered attendance/participation group | Course cadence: scheduled Tuesday/Thursday touchpoints |
| Technical presentation/demo evidence | 3% | Individual presentation/demo evidence receipt with rubric; may be a text entry, upload, link, or live-demonstration receipt | Weekly Tuesday technical presentation/demo slot |
| Course evaluation | 2% | End-of-term completion object | End of term |
| Weekly reinforcement / Reasoning Odyssey gate | 30% | Weekly Odyssey gate objects with gate rubrics | Active recurring-work weeks, including Week 16 Farkle + ML synthesis; Weeks 3–14 are the formal technical sequence; Week 2's local-AI-lab/Container-Connections evidence portfolio also lands here as the week's readiness/setup entry (this week's substantive technical evidence, not a formal Odyssey topic) |
| Reasoning Odyssey checkpoints | 15% | Larger Odyssey checkpoint objects with checkpoint rubrics | Checkpoint weeks selected within Weeks 3–14 and/or Week 16, with the specific weeks published in the course schedule |
| Final individual reflection | 5% | Low-stress individual text-entry/upload reflection object with rubric | Week 17 finals period |
| **Total** | **100%** | | |

## Aggregate check

The weekly Reasoning Odyssey write-up family is deliberately explicit:

`Weekly reinforcement / Reasoning Odyssey gate 30% + Reasoning Odyssey checkpoints 15% = 45%`.

Everything else is recurring course work or the final:

`9 recurring categories × 5% + technical presentation/demo 3% + course evaluation 2% = 50%`
(kickoff, Tuesday AI Fluency, the two Professional Minds strands, A3, A4, A7,
career artifact sequence, and attendance, plus the Tuesday presentation and
course evaluation) and `Final individual reflection 5%`.

Therefore:

`45% Odyssey + 50% other recurring work + 5% final = 100%`.

The table's direct sum is also:

`5 + 5 + 5 + 5 + 5 + 5 + 5 + 5 + 5 + 3 + 2 + 30 + 15 + 5 = 100%`.

## Chassis and rotation boundaries

Tuesday contains the Monday-Moment-equivalent AI Fluency touchpoint, the
first Professional Minds day (the Wacky-Wednesday-equivalent strand), and the
technical presentation/demo. Thursday contains the second Professional Minds
day (the Fun-Friday-equivalent strand) and exactly one rotating technical
activity. The technical presentation has its own small evidence-receipt
category because it is an explicit Tuesday chassis touchpoint; it is not a new
five-day-cadence category.

The Thursday activity categories are not simultaneous. Pair Reasoning uses
the A3-equivalent category on its live weeks; Show & Tell uses the
A4-equivalent and A7-equivalent categories on its live weeks. The category
weights are semester-level weighted groups, so each group contains only the
objects that exist in its applicable rotation. Week 9 is the frozen exception:
Thursday is Fall Break and its pair-style work is folded into Tuesday. Week 14
is the Show & Tell / mini-capstone end of the rotation.

The weekly gate is the evidence receipt for the actual technical work, not a
second unrelated essay. Its package may include sources/rules/work/check/
summary reasoning and the active Thursday artifact when that week has one;
the Tuesday presentation/demo receipt is recorded in its separate 3% group.
The checkpoint group contains larger Odyssey evidence packages and remains
inside the 45% Odyssey family.

Week 16 Farkle + Machine Learning synthesis is recurring work inside the 30%
weekly gate, not a separate project bucket. Week 17 is the individual
reflection at 5%; this model creates no comprehensive programming exam or
Reasoning Defense category. The existing `assignments/programming-exam.md`
template is therefore not used as a grading category until a later explicit
policy decision.

Exact Canvas/Savnac object IDs, due dates, drop-lowest behavior, and the exact
checkpoint-week selection remain deployment questions. The career artifact
sequence is named because the repository contains that real artifact family,
but its per-week schedule still needs to be published by the course build.

## Revision, resubmission, and highest-score policy

This is settled doctrine (Jeremy + ChatGPT, 2026-08-17):

> **Too late, sucker is not the policy. Better reasoning later is still better reasoning.**

For eligible DSCT evidence-bearing reasoning work — including the weekly
Reasoning Odyssey gate objects and the Reasoning Odyssey checkpoints —
revisions and resubmissions remain open for as long as the course is open,
not just until a nominal due date:

1. **Revisions/resubmissions stay open while the course is open and the
   submission system can still accept the work.** A later checkpoint
   occurring after an earlier gate's due date does not, by itself, close
   that earlier gate to revision. A checkpoint may mark an intellectual
   milestone; it must not become a gradebook guillotine that removes the
   incentive to finish or improve earlier work. The only things that can
   actually close submission are an explicit, separately authoritative
   course or institutional boundary — e.g. the end-of-course grading
   deadline — never the mere existence of a later checkpoint.
2. Each attempt is evaluated fresh for academic quality, on its own merits.
3. **Lateness never contaminates the academic-quality judgment.** Marker and
   Coach grade the submitted work itself, with no due/submission timestamps
   in view. The deterministic late-work adjustment is applied afterward, at
   the trusted course edge, to that attempt's own timestamp.
4. That late-work adjustment is the existing shared curriculum default: 1%
   per 24 hours late, calculated continuously to the second/hour rather than
   rounded up by the day, with instructor-granted excused-late time reducing
   the counted lateness. DSCT does not fork or reimplement this arithmetic.
   The canonical policy lives at
   `swosu_cs_curriculum/shared/philosophy/late_work_policy.md`, and the
   canonical deterministic adapter is
   `course_foundry/course_foundry/late_work_policy.py` (established by the
   accepted Marker-sidecar late-work integration). DSCT reuses both as-is.
5. **The student keeps the highest recorded score earned across attempts for
   that item.** A later attempt's recorded score (its own fresh quality
   score, adjusted for its own lateness) is compared against the highest
   score already on record for that item, and the higher of the two becomes
   the recorded grade. A later attempt can never lower an already-earned
   grade — at worst it simply does not replace it.
6. Because of (5), a strong-but-late revision can raise the recorded grade
   even after a weak on-time first attempt, and a student who resubmits
   weaker work risks nothing: the earlier higher score simply stands. This is
   a deliberate incentive for students to keep improving weak reasoning
   rather than treating a missed deadline or a rough first attempt as a
   closed door.
7. Revision means substantive improvement to the evidence or reasoning, not
   cosmetic polish. Examples: correcting an invalid inference; narrowing or
   changing a claim; adding stronger evidence; repairing a proof, test, or
   model; responding to criticism or counterevidence surfaced in Pair
   Reasoning or Show & Tell; sharpening an evidence boundary or uncertainty
   statement; adding a discriminating test or counterexample.

In plain terms for students: due dates matter and help you keep pace; missing
one does not make the work worthless; late work is still worth doing;
revisions and resubmissions are welcome for as long as the course accepts
work; every new attempt may raise your grade; your highest recorded score is
the one that counts; later submissions still receive the same continuous
late-work adjustment as any other late work; and substantive revision is
encouraged because this course values changed reasoning in response to
evidence.

Exact Canvas/Savnac resubmission-window mechanics, the precise end-of-course
hard-close date imposed by the institutional grading deadline, and how the
highest-recorded-score comparison is wired into the gradebook are deployment
seams, not open policy questions — the doctrine above is settled, and those
remain implementation work for the course build.
