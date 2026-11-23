# Job 323 — Git/runtime anchors

Verification date: 2026-08-20

## DSCT repository

- Owning repository: `jeremy-evert/discrete_structures_and_critical_thinking`.
- Current remote `main`: `04d122577633687b93f72e228f7a0202fc54a952`.
- Job branch created from that exact commit: `golem/323-dsct-course-verification`.
- Piper accepted report commit: `d335e75c226e0eaaebd02f5b1d49b2042eedd55d`.
- `main` is exactly one commit ahead of the Piper accepted commit, and that one commit adds only `sidecar/jobs/323_dsct_flo_course_verification.md`.
- Piper's original source-read anchor was `21881a2a2b2b4a7303dee902f5b630bc8c37318f`. Current `main` is two commits ahead of that anchor, adding only the Piper report and Job 323. Therefore DSCT project truth/source has not changed since Piper inspected it.

## Shared dependencies

- `jeremy-evert/local_ai_lab_setup` remote `main`: `b2b2ec1afcea98c59a5ab3818cd361a29eb0f99c`.
- `jeremy-evert/windows_classroom` remote `main`: `f87e340aad4bf4e4e2c064abc676afdcc5260b48`.
- Those are exactly the dependency SHAs used by Report 321 when `assessment/verify_week02_contract_paths.py` passed 17/17 paths.

## Course Foundry

- `jeremy-evert/course_foundry` remote `main`: `969b50aa7f07dedb96049103f52b8bcc9fa0ac5c`.
- This is the same Course Foundry revision inspected by Piper 001.
- Report 321 referenced local Course Foundry SHA `9ca412b4e9f75dd46fe183626b52309f3107bfcc`; GitHub cannot resolve that SHA now. It remains evidence about that prior local checkout, not a reproducible remote anchor.
- Historical Prompt 107 merge commit `a49b658f3a230ad74787757cb0ed66ba24d1c7e5` is remotely retrievable and is an ancestor of current Course Foundry `main`.

## Runtime/job-site limitation

The execution shell available to this ChatGPT session could not clone the private repository because outbound GitHub DNS/network access from that shell failed (`Could not resolve host: github.com`). Repository inspection remained possible through the authenticated GitHub connector.

This session has no mounted Brandy/shared Course Foundry checkout, no Savnac runtime, no SWOSU Canvas API/runtime connector, no institutional Zoom meeting-control surface, no institutional Teams meeting-recording control surface, and no physical Stafford 259 device access. Consequently:

- actual Brandy checkout `HEAD`, branch, upstream, and dirty state could not be freshly inspected;
- no unexplained shared checkout dirt was cleaned, reset, stashed, or normalized;
- local validators/builders could not be freshly executed from a pinned checkout;
- no Canvas/Savnac/Zoom/Teams/Classroom mutation was attempted.

This is the single execution-capability blocker for the portions of Job 323 that require institutional or physical job-site access.
