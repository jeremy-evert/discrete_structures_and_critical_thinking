# Worker 322 — Weeks 15 and 17 package / recurring-source audit

## Scope and starting truth

This bounded worker package owns Week 15, Week 17, and an inventory of the
recurring categories that those weeks must not contradict. The requested file
`sidecar/prompts/322_worker_w15_17_audit.md` was not present in this isolated
worktree at inspection time; scope was therefore taken from the explicit
Worker E unit in `sidecar/jobs/322_dsct_source_completion.md` and the frozen
contracts it names. No Canvas, Savnac, or shared-repository write was made.

Starting HEAD: `4b0e33a`.

## Packages authored

| Week | Student-facing source | Instructor-facing source | Classification after this package |
|---:|---|---|---|
| 15 | `week-15/README.md` | `week-15/instructor/asynchronous-buffer-note.md` | `SOURCE READY` — intentional asynchronous buffer, not a missing week |
| 17 | `week-17/README.md`; `assignments/week-17-final-individual-reflection.md`; `assignments/week-17-final-individual-reflection-rubric.md` | `week-17/instructor/final-reflection-run-of-show.md` | `SOURCE READY` — individual 5% reflection, no exam |

Week 15 intentionally has no new topic, normal meeting, required artifact,
grade, or due date. It offers only optional use of already-open revision paths
and a Week 16 preview. Week 17 asks for two identifiable prior course
artifacts and evidence-bearing reflection on changed reasoning, evidence, AI
judgment, transfer, and uncertainty. It does not create a new project or
comprehensive exam.

## Recurring-category source audit

| Grading-model category | Existing DSCT source / status |
|---|---|
| Semester kickoff week (5%) | `week-01/` and `reports/301_week1_launch_package.md` — landed package |
| Tuesday AI Fluency (5%) | `docs/grading-model.md` plus Tuesday chassis in `planning/fall-2026-weekly-architecture.md` — per-week formal lessons remain another worker's package responsibility |
| Tuesday/Thursday Professional Minds strands (5% each) | Grading/chassis sources exist; architecture correctly labels the per-week shared content `SOURCE_PENDING` rather than inventing it |
| Pair Reasoning (5%) | `assignments/pair-reasoning-report.md` and frozen Weeks 5, 7, 9, 11, 13 cadence |
| Show & Tell (5%) | `assignments/show-and-tell-artifact.md` and frozen Weeks 4, 6, 8, 10, 12, 14 cadence |
| Career artifact sequence (5%) | `assignments/career-artifact-sequence.md`, `templates/career-evidence-pack.md`; exact live schedule remains a build/deployment seam |
| Attendance/participation (5%) | `docs/grading-model.md` only; Week 15 does not create an attendance expectation |
| Technical demo evidence (3%) | `docs/grading-model.md` Tuesday chassis; formal-week instances belong with each week package |
| Course evaluation (2%) | `docs/grading-model.md` end-of-term object; deployment object remains external |
| Decision Gates (30%) | `assignments/weekly-problem-solving-writeup.md`, `templates/weekly-rubric.md`, and contracted architecture; one regular gate is dropped after retained-score resolution |
| Odyssey checkpoints (15%) | `docs/grading-model.md`: exactly Weeks 7, 11, 14; they replace regular Decision Gates that week |
| Farkle + ML synthesis (5%) | `week-16/`, `assignments/week-16-farkle-evidence-receipt.md` — separate from Gates/checkpoints |
| Final individual reflection (5%) | This worker's Week 17 assignment, rubric, README, and instructor guide |

The audit does not manufacture assignments where a frozen source points to a
shared or future week-local package. In particular, no Week 15 category,
Thursday meeting, or due date was invented.

## Planning drift observed

`planning/fall-2026-spine.md` still labels Week 17
`CONTRACTED_NOT_AUTHORED` and says its grading weight/final format remain
open. That statement conflicts with the accepted `docs/grading-model.md`,
which settles Week 17 as a 5% Final individual reflection. This worker leaves
the global planning-status reconciliation to the Foreman; the source package
above is deliberately aligned to the higher-authority grading model.

## Validation record

Run after authoring:

```text
git diff --check
python3 -m pytest -q
python3 assessment/verify_week02_contract_paths.py
```

Expected local interpretation: Week 2 validation is a separate package and
does not gate this worker's Week 15/17 source. The final receipt records the
actual command results and ending commit.
