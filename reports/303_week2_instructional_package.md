# Prompt 303 — DSCT Week 2 instructional package

**Run date:** 2026-08-16
**Meetings:** Tuesday 2026-08-25 and Thursday 2026-08-27
**Branch:** `golem/dsct-303-week2`

## What was authored

- `week-02/README.md`
- `week-02/instructor/tuesday-run-of-show.md`
- `week-02/instructor/thursday-run-of-show.md`
- `week-02/student/tuesday-activity.md`
- `week-02/student/thursday-activity.md`
- `week-02/student/week-02-evidence-assignment.md`
- `week-02/student/week-02-evidence-rubric.md`

The package is source-only. No Canvas/Savnac write, Week 1 edit, Week 3–14
authoring, `course_metadata.yaml` edit, ZyBooks edit, `runs/` edit, or shared
upstream edit was made.

## Chassis mapping

Tuesday follows the frozen 75-minute contract: Professional Minds AI Fluency
about 8 minutes; Wednesday-strand content about 12 minutes; technical
lecture/demo about 47 minutes; and reasoning check/exit about 8 minutes. The
run-of-show labels the Professional Minds source slots as current/pending and
does not fabricate missing source.

Thursday follows the frozen 75-minute contract: Friday-strand content for
about 10–12 minutes; pair investigation/show-and-tell for about 50–55 minutes;
and critique, revision, evidence receipt, and exit for about 8–10 minutes.
The six Container Connections sections are sequenced across the pair-work
segment, with a bounded Bill/Brandy analysis and cleanup evidence at close.

## Grading application

The graded item is one **40-point Week 2 Evidence Portfolio**: 20 points for
the shared local-AI readiness artifact and 20 points for the Container
Connections receipts/reflection. The Tuesday 20-point allocation is the
shared rubric's 5/4/4/4/3 structure; Thursday uses five evidence-first
criteria worth 4 points each, shown in the authored rubric. These are
assignment points, not percentage weights or a new grading category.

Under answered Question 004, the portfolio belongs entirely in the **50%
recurring weekly course-work** bucket because it is a lab/evidence activity.
It is not one of the 45% weekly Reasoning Odyssey write-ups and does not use
the 5% final reflection. Optional World Bible notes do not receive a separate
grade. An infrastructure-caused `NOT READY` or instructor-directed stop is
handled by preserving accurate evidence and an approved substitute, consistent
with the shared source rubric.

## Reused versus newly written

Reused by pointer: the local-AI shared Week 2 instructional pages, readiness
assignment and 20-point rubric; the DSCT string-normalization extension; the
Windows classroom execution guide named by the CS2 precedent; and all four
Container Connections source files (instructor brief, architecture, evidence
manifest, and reflection/evaluation guide). No source prose or commands were
copied into DSCT.

Newly written: the DSCT Week 2 overview, two date-specific run-of-show pages,
two short evidence organizers, the portfolio wrapper, and the DSCT rubric
crosswalk. The Thursday rubric translates the shared evaluation guide into
gradable criteria without changing its evidence or claim boundaries.

## Limitations and validation

The Container Connections sources state `DRY-RUN-REQUIRED` and are pending an
instructor dry run; this package preserves that limitation and does not claim
classroom hardening. Professional Minds per-week source anchors remain
pending in the frozen architecture, so the run-of-show pages use source-slot
labels rather than invented content.

No Python test suite applies to this content repository. `git diff --check`
completed with no output. The requested make checks could not run because the
environment has no `make` executable: `make task-check` returned
`/bin/bash: line 1: make: command not found` (exit 127), and `make check`
returned the same error (exit 127). The final commit, push status, and final
worktree status are recorded in the handoff below.

## Handoff

- AGENTS.md: no repo-local file exists; the shared `../AGENTS.md` was followed.
- Commit: the final local `HEAD` on `golem/dsct-303-week2` (exact hash is
  reported by the final `git rev-parse HEAD` validation below and in the handoff
  message; amending this report necessarily changes the hash).
- Push: blocked. The configured SSH push failed with
  `cannot run ssh: No such file or directory`; a direct HTTPS attempt failed
  with `could not read Username for 'https://github.com': No such device or
  address`. No remote was changed.
- Final `git status --short`: clean after the local commit/amend; the branch is
  one local commit ahead until an authenticated push is available.

## Next recommended prompt

Instructor dry-run and classroom hardening of the shared Container Connections
package, followed by a separate readiness/deployment decision. Do not treat
this source-only authoring pass as that operational validation.
