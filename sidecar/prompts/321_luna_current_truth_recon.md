# Job 321 — bounded current-truth reconnaissance

## Worker mode

Errand. Read-only reconnaissance only. Work in an isolated DSCT worktree at
the exact SHA supplied by the Foreman.

## Job

Reconstruct the current DSCT course and its deployment boundary so the
Foreman can author the Job 321 preflight report.

## Read first

- `AGENTS.md` if present
- `README.md`
- `sidecar/jobs/321_dsct_preflight_to_green_to_write.md`
- current source and relevant reports/prompts only

## Required findings

1. Record the exact DSCT HEAD SHA and origin/main SHA.
2. Inventory Weeks 1–17 from actual student-facing source and classify each
   `SOURCE READY`, `PARTIAL`, `STRUCTURE ONLY`, or `MISSING`, naming paths.
3. Inventory assignments, rubrics, grading groups/weights/drop rules, dates,
   Week 15 asynchronous behavior, and Week 16/17 behavior from source.
4. Identify current deployment/validator support and its exact paths and
   dependency assumptions.
5. Inspect available DSCT branches and reports for useful unpromoted work;
   distinguish branch tips from content that is actually absent on main.
6. Inspect the shared Course Foundry repository read-only: exact SHA,
   worktree dirt/runtime state, and DSCT-relevant builder/deployer/validator
   support. Do not clean, reset, stash, normalize, or modify it.
7. Inspect only documented, read-only live Canvas access if available and
   safe, verifying the DSCT target identity rather than assuming course 74035.
   Never write production Canvas. If access is unavailable, prove that
   precisely and report the smallest next gate.

## Forbidden scope

- No production Canvas mutation of any kind.
- No writes to Course Foundry, JTT, or any other course repository.
- No DSCT source mutation, branch promotion, cleanup, force-push, or
  deletion.
- Do not infer completion from labels or historical reports.

## Done means

Return a durable report at
`sidecar/reports/321_worker_current_truth_recon.md` and a compact Worker
Report in the final response. Every material claim must include a path,
command/output reference, or explicit `UNVERIFIED`/`BLOCKED` reason. The
report is not done if any week classification, SHA, dependency SHA, or live
target claim lacks evidence.

## Acceptance criterion

The report must make it possible for the Foreman to identify at least one
concrete, falsifiable next unit. If it merely repeats historical summaries or
asserts that the course is ready without current-path evidence, it fails.

## Evidence

The worker may write only the report named above in its isolated branch. Do
not commit the Foreman's final Job 321 report.
