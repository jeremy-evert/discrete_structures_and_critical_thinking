# Job 323 — Flo DSCT Course Verification and Recording Readiness

Verification date: 2026-08-20

## Scope and boundary

This shift executed as Flo under Job 323. The durable work is confined to `golem/323-dsct-course-verification` and the authorized report/receipt destinations.

No SWOSU production Canvas write, delete, unpublish, rename, reorder, reconcile, or prune operation was performed. No Savnac write was performed. No shared checkout was cleaned/reset/stashed. No branch was merged to `main`. No force-push or history rewrite was performed. No credentials, tokens, cookies, private recording links, or reusable secrets were written to receipts.

## Executive result

`BLOCKED: the institutional/physical Job 323 runtime is unavailable in this session — GitHub is reachable, but Brandy/Savnac/SWOSU Canvas/Zoom/Teams and Stafford 259 execution surfaces are not — so the required fresh local executions, read-only production inventory, recording tests, delivery test, and classroom repeat cannot be truthfully completed.`

The independent Git/GitHub work that does not require those capabilities is complete and durable below.

## Exact anchors

| Component | Exact current evidence |
|---|---|
| DSCT remote `main` | `04d122577633687b93f72e228f7a0202fc54a952` |
| Piper accepted report commit | `d335e75c226e0eaaebd02f5b1d49b2042eedd55d` |
| Piper source-read anchor | `21881a2a2b2b4a7303dee902f5b630bc8c37318f` |
| Course Foundry remote `main` | `969b50aa7f07dedb96049103f52b8bcc9fa0ac5c` |
| `local_ai_lab_setup` remote `main` | `b2b2ec1afcea98c59a5ab3818cd361a29eb0f99c` |
| `windows_classroom` remote `main` | `f87e340aad4bf4e4e2c064abc676afdcc5260b48` |
| Worker branch | `golem/323-dsct-course-verification` |

Current DSCT `main` is only two commits ahead of Piper's original source-read anchor, and those commits add only the Piper report and Job 323. Therefore current DSCT project truth/source is unchanged from Piper's source inspection. Current Course Foundry `main` is also exactly the same revision Piper inspected. The two Week 2 sibling dependency mains are exactly the SHAs that Report 321 used when its 17-path dependency validator passed.

Report 321's locally inspected Course Foundry SHA `9ca412b4e9f75dd46fe183626b52309f3107bfcc` is not remotely retrievable from GitHub now and is not promoted as a canonical anchor.

## AUTHORED → WIRED → EXECUTED → PROMOTED

| Course slice | AUTHORED | WIRED | EXECUTED | PROMOTED |
|---|---|---|---|---|
| Week 1 | Yes | Yes | Historical execution evidence; no fresh Job 323 local execution | Historical production complete, 8/8 |
| Week 2 | Yes; shared-source dependency seam remains explicit | Yes | Historical execution evidence; no fresh Job 323 local execution | Historical production partial, 7/19 |
| Weeks 3–17 | Yes | **No on current public Course Foundry** | No current full-semester execution evidence | No production evidence |

No later state is inferred from an earlier state.

## Source-model verification

Current source and metadata still establish:

- intended Weeks 1–17 coverage;
- Week 9 as Tuesday-only, with Thursday, October 15, 2026 explicitly Fall Break and no Thursday obligation;
- Week 15 as an asynchronous/no-new-obligation buffer;
- Week 16 as Farkle + Machine Learning synthesis in its own 5% category;
- Week 17 as the 5% final individual reflection, not a comprehensive exam;
- a grading model whose direct sum is 100%;
- one dropped **regular** Decision Gate after highest-attempt retention;
- Weeks 7, 11, and 14 as Odyssey Checkpoints that replace the ordinary Decision Gate for those weeks;
- no required textbook and no required external course for Fall 2026; ZyBooks is historical provenance only.

### Fresh source naming yellow

Direct inspection found a current student-facing naming inconsistency in Week 16: `week-16/README.md` says `Your Decision Gate evidence`, and `assignments/week-16-farkle-evidence-receipt.md` is titled `Week 16 Decision Gate — ...`, while the same assignment body and `docs/grading-model.md` explicitly say this is a separate 5% synthesis and **not an ordinary Decision Gate**. This is a naming/UX defect, not a grading-policy change. It was not patched without the required executable validation environment.

## Current compiler/deployer truth

At Course Foundry `969b50aa7f07dedb96049103f52b8bcc9fa0ac5c`, the DSCT builder is still explicitly Week 1/2-only.

Its current static student surface is:

- 2 modules;
- Week 1: 8 student objects;
- Week 2: 19 student objects;
- total: 27 student objects;
- 2 assignments;
- 0 weighted assignment groups;
- an explicit `Weeks 3-17` omission.

The current tests also assert that the DSCT plan contains only Weeks 1–2 and that network commands refuse any DSCT course other than Savnac course 4.

### Production-course contradiction reproduced from the exact current code path

The public production path is internally contradictory:

1. `production_deploy.py` registers DSCT production course `74035` with `_build_dsct`.
2. `_build_dsct(..., 74035)` passes `74035` into `dsct_savnac_desired_course()`.
3. `dsct_savnac_desired_course()` rejects every course id other than `4`.

Thus current `production_deploy.build_plan("dsct")` is expected to fail before reconcile with the course-id guard. Piper's `4` versus `74035` hypothesis is confirmed against unchanged current remote code.

No shared Course Foundry repair branch was created because this shift lacks an isolated executable Course Foundry checkout and dependencies. Job 323 requires a repair to be executed and validated; an untested speculative repair would not meet that contract. A later executable repair must address both the production target guard and intentional Weeks 3–17 wiring against the current source/grading model.

## Deterministic desired-state receipt

`sidecar/runs/323_flo_course_verification/desired_state_summary.json` contains the canonical verification summary for the current source contract and current compiler shape.

Canonical JSON SHA-256:

`57d4e85321697b79ca177755bbe12ef499ebc1df254e5ad054231f4a982a7d1c`

This is explicitly a Job 323 verification-summary digest, not Course Foundry's full `desired_course_digest()`. A full-semester DesiredCourse digest cannot honestly be produced because current Course Foundry does not wire Weeks 3–17 and this session could not execute a pinned local build.

## Validator status

Report 321 previously recorded:

- `scripts/validate_fall2026_source.py` -> PASS;
- `assessment/verify_week02_contract_paths.py` -> 17 passed, 0 failed;
- `scripts/validate_weeks_07_09.py` -> PASS;
- `scripts/validate_week16_farkle.py` -> PASS;
- `git diff --check` -> PASS.

The source tree has not changed since Piper's later source inspection, and the two sibling dependency mains remain the exact Report 321 SHAs. Those are still relevant durable receipts, but Job 323 does **not** relabel them as fresh executions. The local execution shell for this session could not clone from GitHub because outbound DNS/network access failed, so the requested fresh validator/build execution could not be performed.

## Production Canvas 74035

The required fresh Job 323 production read-only inventory could not be performed because this session has no SWOSU Canvas runtime/API surface.

The latest accepted durable read-only inventory is Report 321, which recorded course `74035`, 15 active students, 1 teacher, 7 published modules / 38 items, Week 1 at 8 items, Week 2 at 7 items, unrelated-looking published surfaces, a kickoff-only conflicting grading topology with weighting disabled, and existing submissions on A01–A05.

Those facts are historical accepted evidence, not a fresh Job 323 readback.

Until a fresh readback and Owner adjudication:

- submission-bearing objects are `PRESERVE` and `OWNER ADJUDICATION REQUIRED`;
- unrelated-looking published modules/items are `OWNER ADJUDICATION REQUIRED`;
- uncaptured live objects are `UNKNOWN`;
- nothing is classified as automatically safe to delete.

## Week 2 WAF seam

Report 319's evidence remains the narrowest durable diagnosis: a trivial probe page succeeded, but the real next page (`Aider as the Coding Client`) received the CloudFront block, leaving Week 2 at 7/19. Report 321 later still observed 7 items.

Job 323 made zero production probes. The smallest next action is a pinned local render plus Savnac/non-production reproduction of the historically first blocked item, followed by harmless request/body comparison there. Only after that should one bounded production dry-run/read-only comparison be considered. Production should not be hammered to discover a filter rule.

## Zoom, Teams, Canvas delivery, and Stafford 259

None of the required approximately 60-second recording tests could be executed in this session:

- no institutional Zoom meeting recording control is available;
- no institutional Teams meeting recording control is available;
- no Savnac/Canvas student-context delivery test surface is available;
- no physical Stafford 259 teaching-machine/audio/display/network access is available.

No test recording was created or published. No Zoom-versus-Teams policy choice is made.

### HUMAN NUDGE — for Foreman/Owner review

Provide one interactive institutional job-site session with both Zoom and Teams meeting controls, Savnac/read-only Canvas access, and the actual Stafford 259 teaching machine. Run both bounded microphone + screen-share recording tests; verify processing/storage/sharing; verify the chosen candidate's student delivery path in non-production; then repeat the best verification candidate through Stafford 259's real classroom audio/display/network path.

## Durable receipts

- `sidecar/runs/323_flo_course_verification/00_git_runtime_anchors.md`
- `sidecar/runs/323_flo_course_verification/01_source_and_compiler_verification.md`
- `sidecar/runs/323_flo_course_verification/02_production_and_week2_evidence.md`
- `sidecar/runs/323_flo_course_verification/03_recording_and_delivery_gates.md`
- `sidecar/runs/323_flo_course_verification/desired_state_summary.json`

## Owner gates preserved

1. Fresh institutional runtime capability is required to execute the pinned validators/builders, Savnac verification, and read-only production Canvas inventory.
2. Existing live production content/submissions still require Owner adjudication before any future reconcile/deletion policy can be approved.
3. Zoom/Teams and the final Stafford 259 classroom repeat require interactive institutional/physical access; final recording policy remains an Owner choice after evidence exists.

## Overall outcome

`BLOCKED: the institutional/physical Job 323 runtime is unavailable in this session, so required fresh execution, production read-only, recording, delivery, and classroom evidence cannot be completed.`

### Course verdict

`COURSE: BLOCKED — fresh pinned build/validator, Savnac, and production read-only evidence cannot be executed from this session; current public Course Foundry also remains Week 1/2-only with the confirmed 4-versus-74035 guard contradiction.`

### Recording verdict

`RECORDING: BLOCKED — no institutional Zoom/Teams recording control or Stafford 259 physical classroom path is available to perform the required 60-second tests and final repeat.`

### Production gate

`PRODUCTION: NO WRITE PERFORMED`
