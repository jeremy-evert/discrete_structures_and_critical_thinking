# Job 323 — Production Canvas and Week 2 evidence

Verification date: 2026-08-20

## Fresh-production gate

Job 323 requires a fresh read-only identity/inventory of SWOSU production Canvas course `74035`. This session has no SWOSU Canvas runtime/API connector, so that gate could not be freshly executed. No production request, write, delete, unpublish, rename, reorder, reconcile, or prune operation was performed.

The latest durable production evidence remains Report 321. It recorded, read-only:

- course `74035`, Fall 2026 Discrete Structures, section `COMSC-2043-1420`;
- 15 active students and 1 active teacher;
- 7 published modules and 38 items;
- DSCT Week 1 with 8 items;
- DSCT Week 2 with 7 items;
- five other published module surfaces outside the two DSCT week modules;
- 13 published assignments in a kickoff-only grading topology with weighting disabled;
- existing submissions on A01–A05.

Those facts are historical accepted evidence, not a fresh Job 323 readback.

## Safety classification of live-only state

Until a fresh readback and Owner adjudication say otherwise:

- any assignment/object carrying an existing student submission: `PRESERVE` and `OWNER ADJUDICATION REQUIRED`;
- unrelated-looking published kickoff/career/advisor/optional modules and their items: `OWNER ADJUDICATION REQUIRED`;
- any live object not represented in the latest durable inventory: `UNKNOWN`;
- no live-only object is classified as safe-to-delete by this job.

The current source grading model is materially different from the latest live gradebook evidence. No automatic fix or destructive reconcile policy is proposed.

## Week 2 WAF evidence

Report 319 established a content-sensitive CloudFront/WAF condition during the historical Week 2 production push:

- a trivial probe page could be created and removed;
- the next real missing page (`Aider as the Coding Client`) repeatedly received the CloudFront block;
- Week 2 stopped at 7/19 items;
- 12 intended Week 2 objects were not proven live.

Report 321 later still observed Week 2 at 7 items, so no durable evidence shows those 12 items subsequently arrived.

No production probing was performed in Job 323.

## Smallest evidence-backed next action

When the institutional job-site runtime is available:

1. pin exact DSCT, `local_ai_lab_setup`, `windows_classroom`, and repaired Course Foundry SHAs;
2. render the historically first blocked item (`Aider as the Coding Client`) locally and inspect the exact request/body shape without contacting production;
3. reproduce the same desired object on Savnac/non-production after a fresh zero-write dry-run;
4. compare harmless content/request variants there to narrow whether formatting, code literals, loopback/API text, or another payload feature drives the failure;
5. only after that, perform a single bounded production dry-run/read-only comparison. Do not repeatedly submit production probes merely to discover a filter rule.

The WAF seam is therefore an investigation item, not permission to evade institutional controls.

## Production gate

`PRODUCTION: NO WRITE PERFORMED`
