# DSCT assignment-create deployment — executed

Follow-up to `dsct_pure_course_recovery.md` / `dsct_pure_course_deployment_manifest.md`. That pass built 13 unpublished module stubs and left the 13 graded objects themselves undeployed, blocked on `create_assignment` in that session. This pass re-tested `create_assignment` against course 74035 with the credential in `~/.config/canvas/canvas.env` — it worked cleanly (verified live with a scratch assignment, created and deleted before this deployment began). The earlier blocker did not reproduce. All 13 graded objects below are now live, published, on the course.

Course: `74035` (Fall 2026 Discrete Structures). `apply_assignment_group_weights` confirmed still `false` before and after this pass — the 70%-vs-100% weight-migration question from `docs/grading-model.md` remains open and untouched, per that doc's own instruction that weight migration is a separate, later, gated step.

## Assignment groups created

All four were missing; all four created at the target weights recorded in `docs/grading-model.md` (weights are inert right now since group-weighting isn't applied live):

| Group | ID | Weight |
|---|---|---|
| Decision Gate | 157225 | 30% |
| Reasoning Odyssey Checkpoints | 157226 | 15% |
| Farkle + ML Synthesis | 157227 | 5% |
| Final Individual Reflection | 157228 | 5% |

Pre-existing groups `Assignments` (151259, 0%) and `Semester kickoff week` (156892, 5%) were left untouched.

## 13 graded objects deployed

Each assignment: 100 points, `online_text_entry` + `online_upload` submission types, published, built from the exact source file(s) in the manifest with a short "argue against yourself" framing block prepended (adversarial-but-collegial framing, at the owner's request — encourages students to find and test objections to their own answer rather than treating the assignment as a one-shot conclusion). Each was added as a published module item to its corresponding module, and each of those 13 modules (previously unpublished stubs) was published.

| Week | Assignment | Canvas ID | Group | Module |
|---|---|---|---|---|
| 4 | Decision Gate — Week 4: Logic, Claims & Proof | 914336 | Decision Gate | 218903 |
| 5 | Decision Gate — Week 5: Sets, Functions & Sequences | 914337 | Decision Gate | 218904 |
| 6 | Decision Gate — Week 6: Algorithms, Correctness & Growth | 914338 | Decision Gate | 218905 |
| 7 | Reasoning Odyssey Checkpoint 1 — Weeks 4–7 | 914339 | Reasoning Odyssey Checkpoints | 218906 |
| 8 | Decision Gate — Week 8: Induction, Recursion & Recurrences | 914340 | Decision Gate | 218907 |
| 9 | Decision Gate — Week 9: Counting & Combinatorial Reasoning | 914341 | Decision Gate | 218908 |
| 10 | Decision Gate — Week 10: Probability, Uncertainty & Evidence | 914342 | Decision Gate | 218909 |
| 11 | Reasoning Odyssey Checkpoint 2 — Weeks 8–11 | 914343 | Reasoning Odyssey Checkpoints | 218910 |
| 12 | Decision Gate — Week 12: Graphs & Network Reasoning | 914344 | Decision Gate | 218911 |
| 13 | Decision Gate — Week 13: Trees, Search & Decision Structures | 914345 | Decision Gate | 218912 |
| 14 | Reasoning Odyssey Checkpoint 3 — Weeks 11–14 | 914346 | Reasoning Odyssey Checkpoints | 218913 |
| 16 | Farkle + Machine Learning Synthesis | 914347 | Farkle + ML Synthesis | 218914 |
| 17 | Final Individual Reflection | 914348 | Final Individual Reflection | 218915 |

All 13 rows deployed cleanly — no failures, no skipped rows.

## Framing blocks used (verbatim, four variants)

- 8 Decision Gates: "find the strongest disagreement" — go looking for the best argument against your own answer before submitting.
- 3 checkpoints: "attack your own weakest link" — pick the weakest link in your chain of reasoning and attack it.
- Week 16 (Farkle): "make your assistant disagree with you" — have the AI genuinely argue the other side, not as a formality.
- Week 17 (final reflection): "argue with your past self" — name something you believed this semester you'd now push back on.

Full text lives in the assignment descriptions on Canvas (not duplicated as separate files in this repo — the descriptions were assembled at deploy time from the manifest source files plus these framing blocks, then posted directly).

## Not touched (guardrails held)

- Weeks 1–3 (already live) — not re-verified, not modified.
- The six retired categories (Monday Moment quiz, Wacky Wednesday, Fun Friday, Pair Reasoning report, Show & Tell report, career artifact sequence) — nothing created for them.
- `apply_assignment_group_weights` — left `false`.
- No other course touched.

## Verification performed

- Full module list re-read after all mutations: all 20 modules `published: true` (was 7/20 before this pass, all 13 formerly-stub weeks now published).
- Full assignment-group list re-read: 6 groups total, weights as specified.
- `apply_assignment_group_weights` re-read after deployment: still `false`.

## Recommended next action

The weight-migration question in `docs/grading-model.md` (surviving categories sum to 70%, two precedent-backed redistribution options recorded, neither chosen) is now the only remaining open item blocking a fully resolved grading model. That is an owner decision, not a deployment mechanics problem — this pass deliberately did not touch it.
