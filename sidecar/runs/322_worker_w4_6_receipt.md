# Job 322 worker receipt — Weeks 4–6

## Scope and authority

Worker package: Fall 2026 Weeks 4–6 only. No Canvas, Savnac, grading-model,
planning-contract, or other-course changes were made.

The requested `sidecar/prompts/322_worker_w4_6.md` was not present in this
worktree at start. The worker scope was therefore resolved from the branch
name `golem/job322-w4-6` and Job 322's explicit worker split: Weeks 4–6.

## Delivered source

| Week | Topic / Thursday mode | Package |
|---|---|---|
| 4 | Logic, Claims & Proof / Show & Tell | `week-04/` overview; Tuesday and Thursday student activities; ordinary Decision Gate; Tuesday and Thursday instructor run-of-show |
| 5 | Sets, Functions & Sequences / Pair Reasoning | `week-05/` overview; Tuesday and Thursday student activities; ordinary Decision Gate; Tuesday and Thursday instructor run-of-show |
| 6 | Algorithms, Correctness & Growth / Show & Tell | `week-06/` overview; Tuesday and Thursday student activities; ordinary Decision Gate; Tuesday and Thursday instructor run-of-show |

Each package names dates, targets, prerequisite assumptions, a Tuesday worked
example, the weekly AI failure check, the individual technical evidence path,
the frozen Thursday activity, evidence/revision expectations, local
provenance, and instructor facilitation materials. They reuse rather than copy
the established Show & Tell, Pair Reasoning, five-part reasoning, rubric, and
grading contracts.

## Validation

- `git diff --check` — pass.
- Structural package check for all required Week 4–6 files — pass.
- Placeholder scan (`todo`, `tbd`, `source_pending`, `placeholder`, insert
  markers, and `fixme`) across new packages — pass.
- `python3 scripts/validate_week16_farkle.py` — pass; emitted the green
  validation receipt `sidecar/runs/week16_farkle_validation_20260819T124558Z.md`.

## Handoff

The package is ready for foreman integration and the Job 322 repository-level
validator. The absent worker-brief file should be restored or its intended
receipt naming checked by the foreman; it did not prevent this bounded source
delivery.
