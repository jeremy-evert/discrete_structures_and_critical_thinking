# DSCT deterministic deployment manifest — required graded objects

Campaign: Olivia's `owner_20260825_cs2_dsct_pure_course_recovery_map_april.md` (commit `3bb54121c3822fca4416f8a3777602912bc3d29c`), Track B. `create_assignment`/`update_assignment` are blocked in the current session — this manifest is the deployment queue for a later authorized pass.

Course: `74035`. Weeks 1–2 are already live (`DSCT Week 1 — Reasoning Odyssey`, 8 items; `DSCT Week 2 — Build the Lab`, 7 items) — not touched, not part of this manifest. Week 3 (container/LaTeX runway) has authored, validated toolchain content (`week-03/`, Prompts 307/316) but is explicitly not a formal graded topic week per the spine — no manifest row.

**Correction to this session's earlier, wrong assumption:** Weeks 4–14 are fully authored, not missing. Full inventory below is read directly from `week-NN/student/*.md`, not assumed.

| Week | Source | Canvas title | Category (target) | Class | Notes |
|---|---|---|---|---|---|
| 4 | `week-04/student/decision-gate.md` | Decision Gate — Week 4: Logic, Claims & Proof | Decision Gate (30% group) | gate | Thursday activity: Show & Tell (in-class, ungraded; evidence may appear inside the gate submission) |
| 5 | `week-05/student/decision-gate.md` | Decision Gate — Week 5: Sets, Functions & Sequences | Decision Gate | gate | Thursday: Pair Reasoning (in-class, ungraded) |
| 6 | `week-06/student/decision-gate.md` | Decision Gate — Week 6: Algorithms, Correctness & Growth | Decision Gate | gate | Thursday: Show & Tell (in-class, ungraded) |
| 7 | `week-07/student/odyssey-checkpoint-1.md` | Reasoning Odyssey Checkpoint 1 — Weeks 4–7 | Reasoning Odyssey checkpoints (15% group, one-third) | checkpoint | Replaces the ordinary Decision Gate this week (no double submission) |
| 8 | `week-08/student/decision-gate.md` | Decision Gate — Week 8: Induction, Recursion & Recurrences | Decision Gate | gate | No separate Thursday artifact file found |
| 9 | `week-09/student/decision-gate.md` | Decision Gate — Week 9: Counting & Combinatorial Reasoning | Decision Gate | gate | Tuesday-only (Thursday is Fall Break); pair-style work folded into Tuesday |
| 10 | `week-10/student/decision-gate.md` | Decision Gate — Week 10: Probability, Uncertainty & Evidence | Decision Gate | gate | No separate Thursday artifact file found |
| 11 | `week-11/student/odyssey-checkpoint-2.md` | Reasoning Odyssey Checkpoint 2 — Weeks 8–11 | Reasoning Odyssey checkpoints | checkpoint | Replaces the ordinary Decision Gate this week |
| 12 | `week-12/student/decision-gate.md` | Decision Gate — Week 12: Graphs & Network Reasoning | Decision Gate | gate | No separate Thursday artifact file found |
| 13 | `week-13/student/decision-gate.md` | Decision Gate — Week 13: Trees, Search & Decision Structures | Decision Gate | gate | Thursday: Pair Reasoning (in-class, ungraded) |
| 14 | `week-14/student/odyssey-checkpoint-3.md` | Reasoning Odyssey Checkpoint 3 — Weeks 11–14 | Reasoning Odyssey checkpoints | checkpoint | Replaces the ordinary Decision Gate this week; Thursday: Show & Tell mini-capstone (in-class, ungraded) — two distinct activities, not a merged double submission |
| 16 | `assignments/week-16-farkle-evidence-receipt.md` | Farkle + Machine Learning Synthesis | Farkle + ML Synthesis (5%) | final-tier | Already source-ready; not yet checked live-deployed (Week 16 module not yet built) |
| 17 | `assignments/week-17-final-individual-reflection.md` + `-rubric.md` | Final Individual Reflection | Final individual reflection (5%) | final | Already source-ready |

**Totals:** 8 Decision Gates (weeks 4,5,6,8,9,10,12,13) + 3 checkpoints (7,11,14) + 1 Farkle synthesis (16) + 1 final reflection (17) = **13 graded objects** to deploy.

## Submission type / points

Source files do not pin an exact points value per gate (unlike CS2's rubric files, which do). Recommend equal-weight gates within the 30% Decision Gate group (8 gates × equal points) and equal one-third-of-15% per checkpoint (matching `docs/grading-model.md`'s own "each an equal one-third (5%) of the category" language) — exact point values are a deployment seam, not invented here. Submission type: `online_text_entry` + `online_upload` (matches the pattern used by every other course's Odyssey-style gate).

## Not part of this manifest (retired, do not deploy)

Monday Moment quiz, Wacky Wednesday reflection, Fun Friday reflection, Pair Reasoning report, Show & Tell report, Career artifact sequence — retired per Decision 029, marked in place in `assignments/career-artifact-sequence.md`, `assignments/show-and-tell-artifact.md`, `assignments/pair-reasoning-report.md`. The in-class Pair Reasoning/Show & Tell activities themselves continue (see `week-NN/student/thursday-pair-reasoning.md` / `thursday-show-and-tell.md`) — only their separate graded Canvas object is retired.

## Open owner question blocking the final weight migration (not blocking this manifest)

See `docs/grading-model.md`'s "Open owner question" section: retiring the six categories above leaves the surviving disciplinary categories at 70%, not 100%. Two precedent-backed redistribution options are recorded there, neither chosen. This manifest's rows do not require that question to be resolved — the objects themselves (title, source, category, class) are exact regardless of the eventual point/weight split; only the live group-weight change is gated on it.
