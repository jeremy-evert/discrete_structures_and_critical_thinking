# Week 3 shared Commons containers lesson — Canvas deployment (DSCT)

**Date:** 2026-09-01
**Target:** production Canvas course 74035 (`COMSC-2043-1420.2026FA`)
**Mission:** `foreman_interface/jobs/tasks/week03_shared_containers_ghcr_and_module.md`
Phase 4 + the 2026-09-01 autonomous Week 3 pass ("PROCEED" item, plus the
mid-turn instruction to surface Anna's landed AI-reasoning LaTeX walkthrough
from the DSCT Week 3 surface).

## Why a native page instead of a link to course 24298

Checked before linking: Computing Commons (course 24298) currently has
**zero student enrollments** and is not public
(`is_public`/`is_public_to_auth_users` both `false`). Linking DSCT students
there would be a dead end. The shared module was instead mirrored as a
**native page in this course**, generated from the single canonical
`computing_commons/curriculum/containers-and-repeatable-environments.md`
source (same content pushed into Architecture's course 75249 too) — one
authored copy, two delivery copies. See the matching Architecture-side
report for the same finding; flagging it here too since it affects DSCT's
reachability of the shared lesson exactly the same way.

## What changed (all additive)

1. Uploaded the Commons deck
   (`week3_containers_commons_deck.pdf`, file id 6579960) and Anna's
   compiled AI-reasoning LaTeX walkthrough report
   (`lectures/ai_reasoning_latex_from_data/final/build/main.pdf`, uploaded
   as `week3_ai_reasoning_latex_walkthrough.pdf`, file id 6579961) to this
   course's Files.
2. Created **"Containers and Repeatable Environments (Shared Lesson)"**
   (`containers-and-repeatable-environments-shared-lesson`), the same
   Commons-sourced content pushed into Architecture, with the deck link
   pointed at this course's own uploaded file.
3. Rewrote the live **"DSCT Week 03 -- Overview"** page from the current
   (post source-update) `week-03/student/container-latex-skill-ladder.md`:
   - removed the stale "the image is not yet published to a shared
     registry" line -- it is now published, public, and pinned
     (`ghcr.io/jeremy-evert/dsct-week3-latex@sha256:e7987919...`);
   - added the "Start here: the shared Commons lesson" section, linking the
     new page and deck, plus the disciplinary question ("What claim can the
     evidence justify?");
   - added the new "Worked example: claim, evidence, assumptions, check,
     confidence" section linking Anna's walkthrough, framed as a real
     evidence-backed instance of this week's reasoning move rather than a
     toy example;
   - the existing validated Run/Inspect/Explain/Perturb-Diagnose-Recover-
     Verify steps and failure-type table are otherwise unchanged.

Week 3 has no graded Canvas object for DSCT (by design, per the page's own
"Status" note) -- there was no grading-semantics surface to hold here.

## Verification

- Confirmed course identity (`74035`, `COMSC-2043-1420.2026FA`) via a fresh
  `GET` immediately before each mutation.
- Confirmed the live page still said "not yet published to a shared
  registry" before the write (proves the read was current), and confirmed
  that phrase is gone after.
- Read back the page after the write: `updated_at` advanced from
  `2026-08-25T21:57:14Z`; the new shared-lesson page link and the
  walkthrough file link are both present in the returned body.
- Module 218918's single item (`DSCT Week 03 -- Overview`) is unchanged in
  count and title.
