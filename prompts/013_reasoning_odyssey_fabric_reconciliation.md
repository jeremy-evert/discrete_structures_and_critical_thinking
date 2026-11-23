# Prompt 013 — Reasoning Odyssey fabric reconciliation (DSCT slice of Prompt 126)

## Status

READY. Dispatched by Foreman. Supersedes Prompt 011 (superseded 2026-08-15,
stood down against a moving target — its Week-2 assumption and
"no existing infrastructure" premise are both stale now that the real spine
landed). This prompt targets the current spine, not Prompt 011's stale one.

`jeremy_task_tracking/prompts/126_cross_course_reasoning_odyssey_fabric.md`
is the cross-course doctrine. `jeremy_task_tracking/questions/
answered_questions/004_dsct_grading_and_final_format.md` is DSCT's own
resolved grading/final-format decision and is binding — this prompt
reconciles source into that decision, it does not reopen it.

## Read first

- `jeremy_task_tracking/prompts/126_cross_course_reasoning_odyssey_fabric.md`
  (full doctrine)
- `jeremy_task_tracking/questions/answered_questions/
  004_dsct_grading_and_final_format.md` (binding grading/final decision)
- `planning/fall-2026-spine.md` (current 17-week dated spine — authoritative)
- `planning/fall-2026-weekly-architecture.md` (Weeks 3-14 Tuesday/Thursday
  chassis contract — currently has zero Reasoning Odyssey / World Bible
  reference)
- `planning/fall-2026-topic-map.md` (Weeks 3-14 detailed source map — has
  exactly one Odyssey mention, a Week 14 mini-capstone)
- `planning/fall-2026-course-design.md` (older design doc — stale relative
  to the current spine: still uses a different week numbering, still lists
  "current grading weights and final format" as an open Jeremy decision
  that Question 004 already resolved)
- `week-01/` and `reports/301_week1_launch_package.md` (the one already-landed
  week, for the concrete Odyssey/World-Bible pattern actually in use)

## Why this exists

Question 004 resolved DSCT's grading structure: 45% weekly Reasoning
Odyssey write-ups, 50% recurring weekly course work, 5% final reflection —
explicitly **not** a second gradebook. The weekly write-ups and the
recurring concept-checks/labs/show-and-tell work are the *same* work,
reframed through the Odyssey's World-Bible continuity, not a parallel track.

That decision is not yet reflected in the two documents that actually
govern how future weeks 2-17 get authored:

- `fall-2026-weekly-architecture.md`'s Tuesday/Thursday chassis slots
  (Reasoning challenge/check/exit, Pair Programming/Show & Tell, Critique/
  revision/evidence receipt) have no language connecting them to a
  persistent World Bible or to Question 004's grading categories.
- `fall-2026-course-design.md` still frames grading weights and final
  format as unresolved and uses stale week numbers from before the real
  spine landed.

Weeks 2 and 3-17 are `CONTRACTED_NOT_AUTHORED` — there is no actual lesson
content yet to retrofit. The correct target for this reconciliation is the
**planning/source layer**, so that whoever authors each week's real content
later inherits Odyssey continuity and the correct grading-category mapping
by default, per Prompt 126's own instruction: "reconcile the doctrine into
authoritative planning/source, then integrate ... into the real weekly
disciplinary work."

## Task

1. In `fall-2026-weekly-architecture.md`, add a concise section (do not
   rewrite the existing chassis tables) that:
   - states the World Bible/persistent-context pattern in DSCT terms: a
     chosen world, system, organization, scenario, or problem space a
     student can bring claims, structures, data, or decisions from into
     logic/proof/modeling work "where pedagogically appropriate" (Prompt
     126's own DSCT example) — not mandatory fiction, not forced every
     week;
   - maps which existing chassis slots are the natural home for Odyssey
     continuity (most plausibly the Tuesday reasoning-challenge/exit-check
     and the Thursday Pair Programming/Show & Tell artifact) without
     inventing new slots or new time allocations;
   - states which existing chassis output maps to which Question-004 grading
     category (weekly write-up vs. recurring concept-check/lab/activity) so
     a future author doesn't have to re-derive the mapping;
   - explicitly does not author any Week 2-17 lesson content — this is a
     planning-contract edit, not content authoring.
2. In `fall-2026-topic-map.md`, check whether the single existing Week-14
   Odyssey mention should be joined by light touch-points at other weeks
   (a short phrase in the existing "failure anatomy" or activity columns,
   not new columns or new rows) where a world-continuity connection is
   genuinely natural given that week's topic — e.g. Week 10's
   relations/equivalence work, Week 11's graphs, Week 16's synthesis. Do not
   force every week; leave a week's existing cell alone if forcing a
   connection would read as decorative.
3. In `fall-2026-course-design.md`, reconcile the stale grading/final-format
   language: either replace the "still needed" framing with a pointer to
   the now-resolved Question 004 (preferred, smallest edit), or if this
   document is fully superseded by `fall-2026-spine.md` +
   `fall-2026-weekly-architecture.md` + `fall-2026-topic-map.md`, say so
   explicitly at the top of the file rather than leaving contradictory
   claims live. Do not silently delete it — DSCT's own prior reconciliation
   pattern (Prompt 012) keeps superseded material with an explicit
   superseded header, not deletion.
4. Do not touch `week-01/`, `course_metadata.yaml`'s textbook block (Prompt
   012 already handled that), or any grading-weight number — Question 004's
   45/50/5 split is final unless Jeremy revisits it.
5. Do not touch `computer_architecture` or any other repo.

## Do not

- Do not author Week 2-17 lesson content. That is separate, later work.
- Do not invent a second Odyssey assignment or grade category — Question
  004 is explicit that this is the same weekly work, not a parallel track.
- Do not change the 45/50/5 grading split.
- Do not force an Odyssey touch-point onto every topic-map week regardless
  of fit.
- Do not conflict with or revert Jeremy's concurrent live spine-authoring
  work — re-read `fall-2026-spine.md` immediately before editing in case it
  moved again.

## Required report

Write `reports/013_reasoning_odyssey_fabric_reconciliation.md` covering:

- exact edits made to each of the three planning files;
- which chassis slots were mapped to which Question-004 grading category,
  and why;
- which topic-map weeks got a light Odyssey touch-point and which were
  deliberately left alone, and why;
- how `fall-2026-course-design.md`'s stale grading language was resolved;
- confirmation no Week 2-17 content was authored and no grading weight
  changed;
- confirmation the current live spine was re-read before editing and this
  work did not conflict with it.

## Done when

A future author of any DSCT Week 2-17 lesson can read
`fall-2026-weekly-architecture.md` and `fall-2026-topic-map.md` and know,
without re-deriving it, how that week's real disciplinary work connects to
a student's World Bible where appropriate and which Question-004 grading
category it feeds — without a second Odyssey assignment ever having been
invented.
