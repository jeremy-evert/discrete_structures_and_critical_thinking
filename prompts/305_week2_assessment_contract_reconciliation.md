# Prompt 305 — DSCT Week 2 assessment contract (reconciled onto merged main)

## Why this matters

DSCT launches 2026-08-18. Week 2's instructional package and named-category
grading model (`docs/grading-model.md`, 45/50/5 aggregate) are already
authored and merged on `main` (reports/303, reports/304). What is still
missing is a fail-closed **assessment contract** for Week 2's graded local-AI
readiness artifact: a Marker-facing rubric-to-criteria mapping with concrete
full-credit/failure-mode/critical-error text, plus a small local acceptance
battery (3-5 fixture cases) to prove the contract actually discriminates
strong work from weak/fabricated work before any live grading touches it.

This work already exists, unmerged, on two stale remote branches that predate
this session's own Week 2 authoring and were never integrated:

- `origin/agent/prompt303-dsct-week2` (2026-08-14) — an independent Week 2
  build with a different file layout (`week-02/student/tuesday/`,
  `week-02/student/thursday/` subfolders, `assessment/` fixtures scaffold).
- `origin/agent/prompt305-dsct-assessment` (2026-08-14) — built on top of the
  above, adds `assessment/week-02-readiness-assessment-contract.yaml`,
  `assessment/week-02-approved-materials.yaml`, and
  `assessment/fixtures/week-02/*.md` + `manifest.yaml` (8 fixture cases:
  strong-complete-ready, strong-not-ready, assertion-only,
  deliciously-wrong-ai-style, invalid-counterexample,
  passing-test-universal-overclaim, supplied-receipt-as-own-evidence,
  wrong-system-model).

These two branches cannot be merged as-is: they restructure `week-02/` in a
way that conflicts with the already-merged, already-live Week 2 package on
`main`, and their branch's `docs/grading-model.md` is a **stale deletion**
relative to `main`'s real merged grading model — do not resurrect that
deletion.

## Task

Port the **assessment contract and fixtures only** (not the competing
week-02 restructure, not the branch's grading-model deletion) from
`origin/agent/prompt305-dsct-assessment` onto current `main`:

1. Read `main`'s actual merged Week 2 package (`week-02/student/`,
   `week-02/instructor/`, `docs/grading-model.md`,
   `reports/303_week2_instructional_package.md`,
   `reports/304_dsct_grading_model.md`) as project truth. Do not read the
   stale branches' own week-02 files as truth — they are superseded.
2. Read `origin/agent/prompt305-dsct-assessment`'s
   `assessment/week-02-readiness-assessment-contract.yaml`,
   `assessment/week-02-approved-materials.yaml`, and
   `assessment/fixtures/week-02/` (via `git show
   origin/agent/prompt305-dsct-assessment:<path>`, do not check out that
   branch directly).
3. Reconcile the contract's `assignment`/`recurring_method`/`criteria`
   fields against `main`'s actual merged rubric
   (`week-02/student/week-02-evidence-rubric.md`) and grading model
   (`docs/grading-model.md`). Where the stale contract references files or
   structure that no longer exist on `main` (e.g. the old
   `week-02/student/tuesday/` layout), repoint references at `main`'s real
   paths. Do not invent new criteria; the contract's actual pedagogical
   content (full-credit evidence, failure modes, critical errors) is real
   authored work worth preserving as-is where it still applies.
4. Bring over the fixture cases (`assessment/fixtures/week-02/*.md` +
   `manifest.yaml`) unchanged unless a fixture literally references the old
   file layout and needs a path fix.
5. Land this as new files under `discrete_structures_and_critical_thinking/`
   (e.g. `assessment/week-02-readiness-assessment-contract.yaml`,
   `assessment/week-02-approved-materials.yaml`,
   `assessment/fixtures/week-02/`) — additive only. Do not touch
   `week-02/`, `docs/grading-model.md`, or any other already-merged Week 2
   file.
6. Write `reports/305_week2_assessment_contract_reconciliation.md`
   describing exactly what was ported, what was repointed, and what (if
   anything) from the stale branches was deliberately left behind and why.

## Forbidden

- Do not merge, rebase onto, or check out either stale branch directly as
  the working branch.
- Do not modify `week-02/`, `docs/grading-model.md`, `course_metadata.yaml`,
  or any Week 1 file.
- Do not wire this contract into Marker, Coach, or any live grading path —
  this prompt is source/contract authoring only, matching the original
  Prompt 305's own stated policy (`live_rollout: not authorized`).
- Do not push or force-push the stale remote branches; leave them as-is for
  Foreman to prune/document separately.

## Acceptance criterion (falsifiable)

The ported contract must be internally consistent with `main`'s real merged
Week 2 rubric and file paths — i.e. every file path the contract references
(`submission_path`, `recurring_method.source.path`,
`course_extension.repository`/`path`) must resolve to a real file at the
commit this work lands on. Prove it: write and run a small script (or
inline check) that loads the YAML and asserts every referenced repo-relative
path exists; paste its pass output into the report. A report claiming
"paths reconciled" without that check's real output is not accepted.

## Evidence destination

`reports/305_week2_assessment_contract_reconciliation.md`, branch
`golem/dsct-305-assessment-contract`, pushed for Foreman review.
