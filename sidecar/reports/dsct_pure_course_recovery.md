# DSCT pure-course recovery — report

Campaign: Olivia's owner mission `foreman_interface/jobs/tasks/owner_20260825_cs2_dsct_pure_course_recovery_map_april.md` (commit `3bb54121c3822fca4416f8a3777602912bc3d29c`). Track B (DSCT), executed after CS2 per the mission's ordering.

## Weeks 4–14 actual source status discovered (corrects this session's earlier wrong assumption)

An earlier pass in this session claimed DSCT Weeks 4–14 had "nothing authored yet." That was wrong — it came from checking only `lessons/`, `assignments/`, and `planning/`, and missing the actual per-week content, which lives in top-level `week-NN/` directories. `planning/fall-2026-spine.md` marks all eleven formal weeks (4–14) `AUTHORED`; a full file inventory confirms this is accurate:

| Week | Files found | Shape |
|---|---|---|
| 4 | README, instructor run-of-show (Tue+Thu), student decision-gate, thursday-show-and-tell, tuesday-activity | regular gate, Show & Tell week |
| 5 | same shape | regular gate, Pair Reasoning week |
| 6 | same shape | regular gate, Show & Tell week |
| 7 | README, instructor run-of-show, student odyssey-checkpoint-1, tuesday-activity | checkpoint (no decision-gate — checkpoint replaces it) |
| 8 | README, instructor run-of-show, student decision-gate, tuesday-activity | regular gate, no separate Thursday artifact file |
| 9 | README, instructor Tuesday-only run-of-show, student decision-gate, tuesday-activity | regular gate, Tuesday-only (Fall Break Thursday) |
| 10 | same shape as 8 | regular gate |
| 11 | same shape as 7 | checkpoint |
| 12 | same shape as 8 | regular gate |
| 13 | README, instructor run-of-show, student decision-gate, thursday-pair-reasoning, tuesday-activity | regular gate, Pair Reasoning week |
| 14 | README, instructor guide, student odyssey-checkpoint-3, thursday-show-and-tell, tuesday-activity | checkpoint + Show & Tell mini-capstone |

Every week's content is real, distinct, disciplinary, and matches `fall-2026-topic-map.md`'s frozen sequence exactly — this was fully authored technical curriculum, not a placeholder, and the recovery mission's correction was accurate: nothing here needed to be written from scratch.

**Also discovered:** no `week-NN/` directory contains a separate Monday Moment/Wacky Wednesday/Fun Friday/career-artifact file for any week — those categories in the old `docs/grading-model.md` were never backed by real per-week content, only by generic reusable templates in `assignments/`. This made the Decision-029 reconciliation simpler than expected: retiring those categories drops zero authored student-facing content, only category placeholders that were never filled in.

## Source reconciliations made under Decision 029

1. **`docs/grading-model.md`** — the six retired categories (Monday Moment quiz, Wacky Wednesday, Fun Friday, Pair Reasoning report, Show & Tell report, Career artifact sequence — 30% total) are struck through and marked `RETIRED (Decision 029)` in the weights table, with the historical Prompt 312/315 notes preserved as provenance rather than deleted. The "Chassis and rotation boundaries" section's Pair-Reasoning/Show-and-Tell framing was rewritten to describe them as real, still-scheduled, ungraded in-class activities whose evidence may still appear *inside* that week's Decision Gate submission — not deleted from the course experience, just no longer separately graded. All settled humane policies (continuous late-work, highest-recorded-score, revision/resubmission while the course is open, drop-one-regular-Decision-Gate) were preserved completely unchanged — none of them depend on the retired categories.
2. **`planning/fall-2026-weekly-architecture.md`** — added a status note: the Tuesday/Thursday chassis table's `SOURCE_PENDING` Professional Minds AI Fluency/Wednesday/Friday segments were never built (confirmed by the week-NN inventory above going straight from orientation to technical content) and should not be source-filled going forward — Decision 029 makes their absence correct, not an authoring gap.
3. **Three reusable assignment templates marked retired in place** (not deleted, matching the CS1/CS2 precedent): `assignments/career-artifact-sequence.md`, `assignments/show-and-tell-artifact.md`, `assignments/pair-reasoning-report.md`.

## Open owner question (recorded, not guessed)

Removing the six retired categories leaves the surviving DSCT disciplinary categories at **70%, not 100%** (5 kickoff + 5 attendance + 3 tech-presentation + 2 course-eval + 30 Decision Gate + 15 checkpoints + 5 Farkle + 5 final reflection). Two precedent-backed resolution options recorded in `docs/grading-model.md`, neither chosen: (1) proportional redistribution of all 8 surviving categories to 100% (Architecture/CS2 precedent), or (2) a flat top-up of the freed 30 points onto Decision Gate + Checkpoints only (matching Architecture's own heavier disciplinary-weight shift). This does not block manifest preparation or Canvas structure — only the eventual live weight-migration step, which is separately gated behind a grade-impact preview regardless.

## Current pure-DSCT weekly student path

A normal formal week (4–14, excluding checkpoint weeks) now has exactly one graded object — the Decision Gate — plus real in-class Tuesday/Thursday activity that is not separately submitted. Checkpoint weeks (7, 11, 14) submit the checkpoint instead, never both. Week 16 is the Farkle + ML Synthesis (already source-ready, correctly outside the Decision Gate/checkpoint families). Week 17 is the final individual reflection.

## Graded-object deployment manifest

Full deterministic manifest: `sidecar/reports/dsct_pure_course_deployment_manifest.md`. 13 objects total: 8 Decision Gates (weeks 4,5,6,8,9,10,12,13), 3 checkpoints (7,11,14), Farkle synthesis (16), final reflection (17).

## Safe live Pages/Modules/navigation prepared

Course allowlist restricted to `{74035, 24298}` for every live call. 13 new Canvas Modules created (weeks 4,5,6,7,8,9,10,11,12,13,14,16,17), **all unpublished** — invisible to enrolled students. Each holds one unpublished "DSCT Week NN — Overview" Page previewing the week's real source content and explicitly stating the graded object is not yet deployed. Weeks 1–2 (already live and published) were independently re-verified unchanged before and after this pass (8 and 7 items respectively, both times). Week 3 and Week 15 intentionally received no new module — Week 3 is a non-formal-topic runway week with its own already-authored toolchain, not part of this manifest; Week 15 has no formal topic or assignment by design (async Thanksgiving buffer).

## Exact assignment-create deployment queue still blocked

13 rows — see `sidecar/reports/dsct_pure_course_deployment_manifest.md`. `create_assignment` was confirmed blocked in this session (Track A) and was not retried in Track B, per the mission's explicit doctrine.

## Tests / readback performed

- `read_canvas_config().allowed_course_ids` verified `{74035, 24298}` before every call.
- Live module list re-read after all mutations: 20 total modules; Weeks 1–2 unchanged (8/7 items, published); 13 new modules all `published: false` with exactly 1 item each.
- One created page's body independently re-read and confirmed content-correct (avoided the earlier CS2 session's backtick shell-escaping bug this time by not using backticks in the f-string source).

## Confirmation

No earned student work, live grade weights, or existing published content in Weeks 1–2 or the Success Foundations modules were disturbed.

## Verdict

`DSCT TRACK COMPLETE — WEEKS 4-14 CONFIRMED FULLY AUTHORED (NOT REBUILT), SOURCE RECONCILED UNDER DECISION 029, ONE OPEN OWNER ARITHMETIC QUESTION RECORDED, MANIFEST READY, SAFE UNPUBLISHED STRUCTURE PREPARED, 13 ASSIGNMENT-CREATE ROWS QUEUED FOR THE BLOCKED-CAPABILITY DEPLOYMENT PASS`
