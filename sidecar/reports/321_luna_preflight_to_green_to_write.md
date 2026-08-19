# Job 321 — Luna DSCT preflight

## Scope and authority

This was a DSCT-only preflight. SWOSU production Canvas was read only; no
Canvas, Savnac, JTT, sibling-course, or shared Course Foundry mutation was
performed. The canonical report supersedes the older blocked Job 321 report;
the Job 322 source-completion handoff was independently checked against
current Git.

## SHA set

| Component | Exact SHA / state |
|---|---|
| DSCT `main` and `origin/main` | `40658baaac87c81a81654ddf7c83bfa9d3be3558` |
| `../local_ai_lab_setup` | `b2b2ec1afcea98c59a5ab3818cd361a29eb0f99c` (clean) |
| `../windows_classroom` | `f87e340aad4bf4e4e2c064abc676afdcc5260b48` (clean) |
| Course Foundry inspected commit | `9ca412b4e9f75dd46fe183626b52309f3107bfcc` |
| Harbor inspected commit | `5d69e3ede4b6f1ab4cb32cf003faea79f7df8cc` |

The shared Course Foundry checkout is materially dirty and diverged; it was
not cleaned or mutated. Tooling was inspected from an isolated disposable
clone pinned to the exact Course Foundry SHA above.

## Job 322 handoff verification

`sidecar/reports/322_luna_dsct_source_completion.md` is present in current
canonical `main` and its source-ready verdict is consistent with the current
tree. Current source contains student-facing Weeks 1–17 coverage; the prior
report's claim that Weeks 4–15 and 17 were missing is stale and was not used.

Week classification from current source:

| Week | Current classification |
|---:|---|
| 1 | Source ready |
| 2 | Authored; external sibling paths now resolve |
| 3 | Container/LaTeX toolchain runway |
| 4–6 | Authored formal packages |
| 7 | Authored; Odyssey Checkpoint 1 replaces Decision Gate |
| 8 | Authored formal package |
| 9 | Authored Tuesday-only package; Thursday Fall Break |
| 10 | Authored formal package |
| 11 | Authored; Odyssey Checkpoint 2 replaces Decision Gate |
| 12–13 | Authored formal packages |
| 14 | Authored; Boolean/FSM mini-capstone; Checkpoint 3 replaces Decision Gate |
| 15 | Authored asynchronous Thanksgiving/Mexico travel buffer |
| 16 | Validated Farkle + Machine Learning synthesis |
| 17 | Authored final reflection and rubric |

The source contract preserves the 100% grading model, 30% Decision Gates with
one regular drop, 15% Odyssey checkpoints in Weeks 7/11/14, the separate 5%
Week 16 category, and the 5% Week 17 reflection. Week 15 adds no required
meeting, topic, or due date.

## Validation

Fresh checks from the real Brandy checkout:

```text
python3 scripts/validate_fall2026_source.py
PASS: Fall 2026 DSCT source package contract satisfied

python3 assessment/verify_week02_contract_paths.py
17 passed, 0 failed — ALL PATHS RESOLVED

python3 scripts/validate_weeks_07_09.py
PASS: Weeks 7–9 package contract satisfied

python3 scripts/validate_week16_farkle.py
PASS / exit 0

git diff --check
PASS
```

The Week 16 validator emitted the untracked local receipt
`sidecar/runs/week16_farkle_validation_20260819T142036Z.md`; it was preserved
and is not part of this report commit. No DSCT implementation source needed
repair. The accepted source commits are recorded in the Job 322 handoff; this
shift promotes only this preflight evidence report.

## Fresh production read-only identity and state

Read-only Canvas calls against `https://swosu.instructure.com` authenticated as
Jeremy Paul Evert (`id=24406`, `login_id=evertj`). Course discovery returned
129 courses and exactly one matching Fall 2026 DSCT target:

```text
id=74035
name=Fall 2026 Discrete Structures (COMSC-2043-1420)
course_code=COMSC-2043-1420.2026FA
workflow_state=available
account_id=39
enrollment_term_id=290
default_view=modules
```

The target has 15 active students and 1 active teacher. Existing submissions
are present on A01 (2), A02 (2), A03 (1), A04 (1), and A05 (1); none are graded.
All other inspected assignments have zero submissions.

## Production semantic diff and safety result

The fresh live readback does not match the desired full-semester DSCT shape:

- Live Canvas has 7 published modules and 38 items: `DSCT Week 1` (8),
  `DSCT Week 2` (7), three unrelated kickoff/career modules (20 total), an
  advisor module (1), and an optional/bonus module (2).
- Live has 13 published assignments, all in `Semester kickoff week` (5%).
  The `Assignments` group is 0%, and `apply_assignment_group_weights=false`.
- Live assignments have rubrics, no lock/unlock dates, and due dates ranging
  from 2026-08-18 through 2026-08-22; two optional/advisor assignments have no
  due date.
- Live has one visible unlocked PDF (`DSCT_Day1_Own_Your_Path.pdf`) and three
  external SharePoint slide links.

The source desired state is a complete Weeks 1–17 course with its frozen
grading topology and Fall 2026 dates. The observed module, assignment,
grading, and asset facts therefore establish a material semantic mismatch.
An exact create/update/delete inventory was not generated because doing so
would require choosing whether the five unrelated published modules, their
assignments, and existing student submissions are intended content. No
deletes or writes are authorized in this shift.

## Savnac / non-production

No Savnac target read or dry-run was used. Current Course Foundry support is
explicitly DSCT-scoped: sandbox course `4`, production registry `74035`, and
the DSCT operator pins `dry_run=True`, `force=False`, and
`prune_scope="none"`. A future bounded Savnac preflight may use the exact
tooling/source SHA set above after independently confirming course 4 and its
runtime identity. This shift does not claim a non-production result.

## Yellows and exact remaining action

Non-blocking yellow: a few planning documents retain stale generic status
words such as `CONTRACTED_NOT_AUTHORED`/`SOURCE_PENDING`, although the current
spine, packages, and validators are green.

**BLOCKED: the freshly identified production course contains unrelated
published content, a conflicting kickoff-only grading topology, and existing
student submissions, so a safe production semantic diff/reconcile cannot be
approved without human adjudication of that live state.**

Exact remaining action: obtain that adjudication in a separately authorized
production-closeout shift, then regenerate the desired-vs-live semantic diff
and independently re-read the target immediately before any bounded write.

**Verdict:** `BLOCKED`
BLOCKED: live course 74035 has unrelated published content, conflicting grading topology, and existing submissions requiring human adjudication before a safe reconcile.
