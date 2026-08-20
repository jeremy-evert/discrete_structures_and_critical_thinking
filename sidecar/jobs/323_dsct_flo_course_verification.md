# Job 323 — Flo DSCT Course Verification and Recording Readiness

## Role

You are **Flo**, the bounded job-site worker for this verification shift.

Olivia the Owner owns acceptance and promotion decisions. You execute, gather evidence, repair only proved non-production/source/tooling defects within this job's authority, and return a durable package. A worker claim of success is not promotion.

## Outcome

Turn Piper 001's reconnaissance into executable job-site evidence for Fall 2026 **Discrete Structures and Critical Thinking**.

End with exactly one of:

- `READY FOR OWNER DECISION`
- `BLOCKED: <one precise reason>`

`READY FOR OWNER DECISION` means Olivia has enough evidence to decide the next production/deletion/adjudication step without another discovery pass.

This job does **not** authorize a SWOSU production Canvas write, deletion, pruning decision, or merge to `main`.

## Worksite and evidence destinations

- Owning repository: `jeremy-evert/discrete_structures_and_critical_thinking`
- Read authority baseline: current `main`
- DSCT worker branch: `golem/323-dsct-course-verification`
- Canonical report to prepare: `sidecar/reports/323_flo_course_verification.md`
- Raw/durable receipts: `sidecar/runs/323_flo_course_verification/`

If a proved shared-tooling repair is required, use a separate isolated job branch/worktree in the owning shared repository. Do not work directly in a dirty shared checkout and do not merge your own repair.

At completion, commit and push only the authorized job branch(es) and return their commit SHAs plus the report/receipt pointer to Olivia.

## Required starting anchors

Read these first and verify them against current Git rather than trusting prose blindly:

1. `sidecar/piper/reports/001_course_verification.md`
   - accepted Piper reconnaissance anchor: `d335e75c226e0eaaebd02f5b1d49b2042eedd55d`
2. `sidecar/jobs/321_dsct_preflight_to_green_to_write.md`
   - reuse its preflight machinery and safety boundaries; do not redo historical archaeology already superseded by current source
3. `sidecar/reports/321_luna_preflight_to_green_to_write.md` if present/current
4. `sidecar/reports/319_week1_production_launch.md`
5. current DSCT project truth, validators, metadata, grading model, and Week 1–17 source
6. current `foreman_interface` worker/dispatch doctrine relevant to this shift

Piper 001 is the accepted **report-stage reconnaissance** for this job. Treat its claims as hypotheses to execute/verify locally, not as substitute receipts.

## Current hypothesis from Piper 001

Verify, do not assume:

- 16 source-GREEN weeks; Week 2 source-YELLOW.
- Weeks 3–17 are authored even though the currently inspected public Course Foundry DSCT builder appeared wired only for Weeks 1–2.
- Current public Course Foundry appeared internally contradictory for production DSCT: production tooling targeted Canvas `74035` while the inspected DSCT builder accepted only Savnac course `4`.
- Production Canvas `74035` historically has Week 1 complete, Week 2 partial, unrelated published content, conflicting grading topology, active students, and existing submissions.
- No canonical lecture-recording workflow is yet proven for DSCT.

## Authority

You may:

- inspect DSCT, Course Foundry, relevant shared curriculum/tooling repositories, and current Git state;
- create isolated job branches/worktrees;
- run existing validators/tests/builders/dry-runs;
- make bounded DSCT or shared-tooling repairs only when execution proves a defect and the repair is needed to complete this verification;
- commit and push those bounded job branches for Olivia to review;
- inspect SWOSU production Canvas course `74035` **read-only**;
- inspect and use Savnac/non-production targets under their existing repository policy, including bounded writes only when already allowed by that policy and preceded by a fresh dry-run;
- perform bounded Zoom and Microsoft Teams recording tests using institutional accounts available on the job site;
- create temporary local/non-production test recordings and delete local temporary test artifacts when safe;
- use the actual Stafford 259 teaching machine/network/audio/display path for the final selected-platform test when physical access is available.

You may **not**:

- write, delete, unpublish, rename, reorder, reconcile, or prune SWOSU production Canvas `74035`;
- infer that unrelated-looking production content is disposable;
- alter or destroy existing student submissions;
- merge any worker branch to `main`;
- force-push or rewrite shared history;
- clean/reset/stash unexplained dirt in shared checkouts;
- expose credentials, tokens, cookies, recording links requiring private access, or other reusable secrets in reports/receipts;
- choose a destructive production reconcile policy on Olivia/Jeremy's behalf;
- choose Zoom versus Teams solely from vendor feature lists.

## Work sequence

### 1. Establish exact Git/runtime truth

Capture durable receipts for:

- DSCT `main` SHA and clean/dirty state of the actual job-site checkout;
- Piper 001 report anchor and whether current `main` has advanced since it;
- Course Foundry remote `main` SHA;
- actual Brandy/shared Course Foundry checkout `HEAD`, branch, upstream, and dirt;
- whether any locally referenced Course Foundry commit/branch from prior reports exists only locally, is pushed, is superseded, or is canonical.

Do not normalize unexplained dirt. If the shared checkout is dirty, inspect it read-only and do execution from an isolated worktree/clone pinned to an exact SHA.

### 2. Reproduce the DSCT compiler/deployer contradiction

Using pinned revisions, prove the executable truth rather than reading comments alone.

At minimum:

- run the current DSCT source validators;
- run/build the current DSCT desired-course path;
- record exact week/module/object/assignment-group counts and a deterministic digest or equivalent reproducible summary;
- test Savnac course `4` behavior as permitted;
- test the production-target build path for course `74035` **without writing production**;
- explicitly prove or disprove Piper's reported `4` versus `74035` course-id guard contradiction;
- determine whether Weeks 3–17 are currently compiler-wired or only source-authored.

If a stale/partial/contradictory shared-tooling defect is proved, repair it on an isolated shared-tooling job branch, run focused tests, and leave the branch/commit for Olivia. Do not merge it yourself.

### 3. Build the deterministic desired-state model

Reuse Job 321's acceptance machinery. Do not reopen course philosophy.

Prove at minimum:

- intended Week 1–17 module coverage;
- Week 9 Fall Break Tuesday-only semantics;
- Week 15 no-new-obligation asynchronous semantics;
- Week 16 Farkle + Machine Learning synthesis;
- Week 17 final reflection;
- 100% grading model;
- Decision Gate drop-lowest rule;
- Odyssey Checkpoint replacement weeks;
- Farkle's separate category;
- unresolved token/placeholder absence;
- duplicate/zombie prevention;
- sane Fall 2026 dates/locks where source defines them;
- declared shared-source dependencies for Week 2;
- no hidden ZyBooks/paid requirement.

Leave deterministic receipts sufficient for Olivia or a fresh worker to reproduce the result.

### 4. Inspect production Canvas 74035 read-only

Freshly prove the target identity before relying on historical course id `74035`.

Inventory read-only:

- course identity and sections/enrollment counts relevant to safety;
- module names/order/item counts/publish state;
- assignment groups, weights, rules, rubrics, due/lock dates;
- Week 1 and Week 2 exact state;
- unrelated published modules/items;
- existing submission counts/statuses sufficient to prevent unsafe pruning;
- files/links where supported;
- student-facing visibility where a bounded read-only student-view mechanism exists.

Produce a semantic diff between the deterministic desired state and live production.

**Do not propose deletions as automatic fixes.** Classify every live-only object as `PRESERVE`, `OWNER ADJUDICATION REQUIRED`, or `UNKNOWN`, with evidence. Existing submissions automatically require preservation/adjudication, never silent deletion.

### 5. Investigate Week 2 without hammering production

Use the existing WAF evidence as a starting point.

Prefer local rendering/request inspection, Savnac/non-production reproduction, harmless request-shape comparison, and a narrowed hypothesis. Do not evade institutional controls and do not repeatedly probe production merely to discover a filter rule.

Return the smallest evidence-backed next action for the 12 historically missing Week 2 items.

### 6. Verify Zoom recording in a bounded 60-second test

Use the institutional Zoom identity available to the job site.

Record receipts for:

- signed-in institutional identity/account class without exposing private identifiers beyond what is necessary;
- whether local/computer recording is available;
- whether cloud recording is available under the institutional account;
- whether automatic recording can be enabled under current policy;
- one approximately 60-second recording containing microphone audio and a screen share;
- successful post-processing/playback;
- actual storage/output location and retention behavior discoverable from the account/app;
- any admin-policy blocker.

Do not publish a test recording publicly.

### 7. Verify Microsoft Teams recording in a bounded 60-second test

Use the institutional Microsoft 365 identity available to the job site.

Record receipts for:

- organizer identity/license availability;
- recording control availability;
- one approximately 60-second recording containing microphone audio and a screen share;
- successful processing/playback;
- actual OneDrive/SharePoint storage destination;
- sharing/permission behavior relevant to later Canvas delivery;
- whether automatic recording is available under current tenant/meeting policy;
- any retention/expiration behavior visible to the organizer;
- any admin-policy blocker.

Do not publish a test recording publicly.

### 8. Verify the Canvas delivery path without production mutation

Determine the smallest reliable student delivery pattern for a processed recording link/file.

Prefer a Savnac/non-production verification where possible. Prove that the selected link/storage permission shape can be opened from the intended student context without granting excessive access.

Production Canvas remains read-only.

### 9. Repeat the winning recording path in Stafford 259

After Zoom and Teams evidence exists, select the **best verification candidate** for the classroom repeat based on observed reliability and institutional fit. This is not a final Owner policy decision if both remain viable.

On the actual Stafford 259 teaching machine/environment, repeat the full approximately 60-second test through the real:

- machine/account sign-in;
- microphone/audio path;
- screen/display/share path;
- classroom network;
- recording start indicator;
- recording stop/processing;
- playback/storage confirmation.

If physical classroom access is unavailable, do not fake this gate. Finish all independent work, then issue one narrow `HUMAN NUDGE` stating exactly what physical action/access is required. The job may end `BLOCKED` on this one gate if everything else is complete.

### 10. Define the operational fallback

For the recommended candidate, document:

- start-of-class visual confirmation that recording is active;
- manual-start fallback if automatic recording is unavailable;
- after-class check that processing completed;
- where the durable asset lives;
- how the Canvas student link should be delivered;
- what happens if processing fails;
- retention/expiration concern requiring Owner policy.

Do not create a new third-party recorder dependency unless separately authorized.

## Evidence contract

Write the canonical report:

`sidecar/reports/323_flo_course_verification.md`

Write raw receipts under:

`sidecar/runs/323_flo_course_verification/`

Receipts should include enough command/test/output detail to reproduce claims, but must not contain secrets. Useful receipt classes include:

- Git/runtime anchors;
- validator/test results;
- desired-state summary/digest;
- Course Foundry contradiction reproduction and any repair test evidence;
- production Canvas read-only inventory/semantic diff;
- Week 2 investigation;
- Zoom 60-second test;
- Teams 60-second test;
- Savnac/non-production recording-delivery test;
- Stafford 259 classroom repeat.

The report must explicitly separate the four truth states where relevant:

`AUTHORED → WIRED → EXECUTED → PROMOTED`

Do not infer one from another.

## Owner gates to preserve

Stop and return evidence rather than crossing these gates:

1. **Any SWOSU production Canvas write.**
2. **Any deletion/pruning/adjudication of existing live production objects.**
3. **Any action that could damage or detach existing student submissions.**
4. **Final Zoom-versus-Teams policy choice when both remain viable.**
5. **Retention/public-sharing policy requiring Jeremy/Olivia judgment.**
6. **Physical Stafford 259 access if the agent cannot obtain it.**
7. **Merge/promotion to `main`.** Olivia/Foreman accepts and promotes worker packages.

## Final report requirements

End `sidecar/reports/323_flo_course_verification.md` with:

### Course verdict

One of:

`COURSE: READY FOR OWNER DECISION`

or

`COURSE: BLOCKED — <precise blocker>`

### Recording verdict

One of:

`RECORDING: VERIFIED — <candidate and evidence pointer>`

`RECORDING: OWNER CHOICE — both Zoom and Teams verified`

or

`RECORDING: BLOCKED — <precise blocker>`

### Production gate

Always state:

`PRODUCTION: NO WRITE PERFORMED`

## Web/UI completion pointer

When the durable package is committed and pushed, return only a compact completion summary to Jeremy:

- course verdict;
- recording verdict;
- branch name(s);
- commit SHA(s);
- report path;
- receipts path;
- at most three genuine Owner decisions/gates.

Do not paste the full investigation into the Web UI. The repository is the system of record.
