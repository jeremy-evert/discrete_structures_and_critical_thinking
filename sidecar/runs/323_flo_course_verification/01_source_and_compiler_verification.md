# Job 323 — Source and compiler verification

Verification date: 2026-08-20

## Source truth

Current DSCT source is unchanged from Piper 001's source-read anchor. Direct GitHub inspection also reconfirmed the special-semester semantics:

- Week 9 explicitly says Tuesday, October 13, 2026 only; Thursday, October 15 is Fall Break with no class, artifact, reflection, or Thursday due date.
- Week 15 explicitly says asynchronous Thanksgiving/travel buffer with no new formal DSCT topic, normal class meeting, required assignment, or new due date.
- Week 16 is the Farkle + Machine Learning synthesis and the grading model places it in its own 5% category, separate from ordinary Decision Gates and Odyssey checkpoints.
- Week 17 is a 5% individual final reflection and explicitly not a comprehensive/programming exam, Reasoning Defense, or new capstone.
- `course_metadata.yaml` states no required textbook and no required external course for Fall 2026; ZyBooks identifiers are historical provenance only.

The current grading model sums to exactly 100%:

`5 + 5 + 5 + 5 + 5 + 5 + 5 + 5 + 3 + 2 + 30 + 15 + 5 + 5 = 100`.

The settled rules include one dropped regular Decision Gate after highest-attempt retention; Odyssey checkpoints replace the ordinary Decision Gate in Weeks 7, 11, and 14; Week 16 is separate; Week 17 is separate.

## Fresh source yellow found by inspection

The Week 16 doctrine is semantically clear in `docs/grading-model.md`, but two current student-facing headings still use stale Decision Gate labeling:

- `week-16/README.md` contains the heading `Your Decision Gate evidence`.
- `assignments/week-16-farkle-evidence-receipt.md` is titled `Week 16 Decision Gate — Farkle + Machine Learning Evidence Receipt`, while its own purpose paragraph says the assignment is a separate 5% synthesis and **not an ordinary Decision Gate**.

This is a naming/UX defect, not evidence that Week 16's grading doctrine changed. It was not repaired in this shift because the required local validator/test execution environment was unavailable; no untested source mutation was pushed merely to improve wording.

## Current Course Foundry executable shape

Pinned remote Course Foundry `main`: `969b50aa7f07dedb96049103f52b8bcc9fa0ac5c`.

Current `course_foundry/dsct_desired_course.py` is explicitly a Week 1/2 builder. Its fixed current student surface is:

- 2 modules;
- Week 1: 8 student objects;
- Week 2: 19 student objects;
- total: 27 student objects;
- 2 assignment objects;
- 0 weighted assignment groups;
- `deployment_omissions()` explicitly lists `Weeks 3-17`.

Current tests reinforce this state by asserting only Week 1/2 modules and by asserting network commands refuse any DSCT course other than Savnac course 4.

## Reproduced 4-versus-74035 contradiction from the exact code path

The contradiction is present on current remote `main` and does not require a Canvas write to establish:

1. `course_foundry/production_deploy.py` registers DSCT as production course `74035` with builder `_build_dsct`.
2. `_build_dsct(paths, 74035)` calls `dsct_savnac_desired_course(context, course_id=74035)`.
3. `dsct_savnac_desired_course()` contains a guard requiring `course_id == 4` and raises otherwise.

Therefore the current production build path is expected to terminate before reconcile with the semantic equivalent of:

`ValueError: DSCT Savnac deployment is restricted to course 4, not 74035`

This disproves any claim that current public Course Foundry `main` is a functioning DSCT production build path. It also confirms Weeks 3–17 are currently AUTHORED in DSCT source but not WIRED in current public Course Foundry.

## Truth-state separation

| Slice | AUTHORED | WIRED | EXECUTED | PROMOTED |
|---|---|---|---|---|
| Week 1 | yes | yes | historical evidence yes; no fresh Job 323 execution | historical production complete (8/8) |
| Week 2 | yes, shared dependencies | yes | historical evidence yes; no fresh Job 323 execution | historical production partial (7/19) |
| Weeks 3–17 | yes | no on current Course Foundry `main` | no current execution evidence | no production evidence |

No state is inferred from another.

## Deterministic verification summary

A canonical machine-readable verification summary is stored at `sidecar/runs/323_flo_course_verification/desired_state_summary.json`.

SHA-256 of its canonical JSON form (sorted keys, compact separators, ASCII encoding):

`57d4e85321697b79ca177755bbe12ef499ebc1df254e5ad054231f4a982a7d1c`

This is a Job 323 verification-summary digest, **not** Course Foundry's `desired_course_digest()`. A genuine full DesiredCourse digest cannot be produced because current Course Foundry does not wire the full semester and this session could not execute a pinned local build.

## Validator status

Report 321 recorded current-source validator success at the same sibling dependency SHAs now present on their remote mains:

- `python3 scripts/validate_fall2026_source.py` -> PASS;
- `python3 assessment/verify_week02_contract_paths.py` -> 17 passed, 0 failed;
- `python3 scripts/validate_weeks_07_09.py` -> PASS;
- `python3 scripts/validate_week16_farkle.py` -> PASS;
- `git diff --check` -> PASS.

Because the current DSCT source tree is unchanged since Piper's later inspection and the sibling dependency SHAs remain identical, those receipts remain relevant historical evidence. Job 323 does **not** relabel them as fresh executions.

## Shared-tooling repair disposition

A Course Foundry repair is plainly required before production build verification can succeed: production target handling must no longer conflict with the builder, and Weeks 3–17 must be intentionally wired to the current source/grading contract. No shared-tooling worker branch was created in this shift because this environment cannot create and execute an isolated Course Foundry checkout with its test dependencies. An unexecuted repair would not satisfy Job 323's evidence standard.
