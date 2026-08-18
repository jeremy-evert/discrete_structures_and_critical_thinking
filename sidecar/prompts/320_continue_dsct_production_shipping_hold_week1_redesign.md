# Prompt 320 — Continue DSCT production shipping while Week 1 redesign is reserved

## Role

You are the DSCT Foreman. Jeremy and Chaz are concurrently reimagining the Week 1 teaching voice and presentation package. That is a separate writer lane.

Your job in this prompt is to keep converting already-authoritative DSCT source into safe, student-visible production Canvas state without turning Jeremy into the orchestration layer and without colliding with the Week 1 redesign.

## Current production truth to verify, not assume

Real SWOSU Canvas target: **course 74035**.

Last known state from Report 319 / the 2026-08-18 launch shift:

- DSCT Week 1 — Reasoning Odyssey: production module exists, published, 8/8 authored items present.
- DSCT Week 2 — Build the Lab, Then Make Results Reproducible: production module exists and is published, but only 7/19 authored items landed.
- The remaining Week 2 page POSTs hit a reproducible content-specific CloudFront/WAF 403 on `swosu.instructure.com`; a trivial probe page could be created/deleted at the same time, so this was not proven to be a blanket rate limit.
- `course_foundry/production_deploy.py` has a production-gated DSCT target for 74035 from Prompt 107.
- Canvas module creation may ignore requested `published=true` until an existing-module metadata pass / explicit verified republish.
- Weeks 4–14 have a resolved semester spine but do **not** yet have finished authored lesson content. Do not fabricate semester content merely to make Canvas look full.

Treat all of that as a starting hypothesis. Begin by independently reading the repo, the owning reports, current Git state, and live production read-back.

## Reserved lane — DO NOT EDIT

Jeremy + Chaz exclusively own the Week 1 narrative/presentation redesign during this shift.

Do not edit, rewrite, regenerate, normalize, or "helpfully improve":

- `planning/week-01-source-map.md`
- anything under `week-01/instructor/`
- anything under `week-01/student/`
- any Week 1 presentation/Beamer source added during this shift
- `semester_kickoff_week` or its presentation sources

You may read those files when necessary to understand production state. If a production defect appears to require changing one of these sources, stop that unit and record the exact seam; do not cross the writer boundary.

## Mission

Ship as much **already-authoritative, student-useful DSCT** as can be safely shipped today.

Good enough and teachable beats polish. A defect blocks promotion only when it prevents a student from finding, accessing, understanding, submitting, or being graded correctly on required work, or creates a meaningful production-safety risk.

Named yellows are acceptable. Silent defects are not.

## Foreman sequence

### 1. Re-orient and verify the live floor

Read at minimum:

- `sidecar/reports/319_week1_production_launch.md`
- `reports/300E_launch_readiness_synthesis.md`
- `reports/303_week2_instructional_package.md`
- `sidecar/reports/306_week2_shared_ai_lab_reuse_map.md`
- `sidecar/reports/307_week3_container_latex_student_path_probe.md`
- `sidecar/reports/316_week3_pinned_container_skill_ladder.md`
- `planning/fall-2026-spine.md`
- `planning/fall-2026-weekly-architecture.md`

Also inspect the current `course_foundry` production deploy path and Prompt 107 report/evidence.

Then perform a read-only live inventory of production course 74035. Confirm exact module publish state, item counts, and what is missing before writing anything.

### 2. Kill the Week 2 WAF blocker without hammering production

Do **not** repeatedly retry the same 12 failing production POSTs.

Dispatch bounded Golem work to identify the smallest reproducible cause of the content-specific WAF failure using source/rendered HTML and local/offline tests wherever possible.

Useful questions include:

- Which exact remaining Week 2 objects fail?
- What rendered HTML differs between a page that succeeds and one that receives CloudFront 403?
- Is there one string, URL form, shell/PowerShell example, loopback/API notation, HTML structure, or encoding pattern common to the failures?
- Can the content be represented equivalently and faithfully without the triggering transport pattern?
- Is the bug better owned by source content, Markdown rendering, Harbor/Imprint request encoding, or Canvas/WAF behavior?

Do not weaken security controls, evade the WAF, encode content merely to bypass institutional filtering, or invent student-visible wording. We are looking for a legitimate representation/transport defect or a harmless source form that Canvas accepts, not a bypass.

If a narrow source/compiler/rendering repair is supported by evidence, dispatch its implementation to a bounded Golem, test it, independently review it, and promote it through the normal source + production CLI path.

Production remains single-writer Foreman territory. Workers do not receive production credentials or production-write authority.

### 3. Reconcile Week 2 only when the delta is understood

Before any production write, run the vetted production dry-run against exactly course 74035 with `prune_scope=none` unless stronger authority is established.

Require:

- target exactly 74035;
- zero deletes;
- no duplicate module/item creation;
- the proposed creates/updates are explainable from the live inventory;
- no Week 1 redesign files are part of the change;
- assignment/rubric behavior remains source-backed.

Jeremy has authorized continuing the bounded DSCT production deployment of already-authoritative source during this shift. Use the normal reviewed `production_deploy.py ... --confirm-live` path and respect any classifier/human approval gate. Do not route around a safety gate.

After a write, independently read back production before deciding success. Re-assert module publication if Canvas exhibits the known create/publish behavior.

### 4. Do not stop at the WAF if another useful unit is ready

If the Week 2 WAF seam cannot be safely solved in a bounded unit, document it and move to other already-authored source rather than burning the shift on one blocker.

Specifically investigate Week 3. Existing repo evidence includes the pinned container/LaTeX skill ladder and instructor/student artifacts. Determine whether Week 3 is sufficiently authored and accepted to add to `dsct_desired_course.py` without inventing pedagogy.

If YES:

1. author a bounded implementation prompt;
2. dispatch a Golem to extend the desired-course compiler for only the accepted Week 3 source;
3. test locally;
4. independently review against the owning Week 3 reports/contracts;
5. dry-run production;
6. reconcile and read back if clean.

If NO, write the exact missing authoring contract and move on.

For Weeks 4–14, the frozen spine is **not** permission to fabricate lessons. Inventory what real authored material exists and distinguish `SOURCE READY`, `STRUCTURE ONLY`, and `NOT AUTHORED`.

### 5. Preserve ownership and Git hygiene

Use isolated branches/worktrees for Golems. Send raw worker receipts to a scratch/sidecar destination that cannot accidentally contaminate another repo's main branch.

One logical change per commit. Push durable evidence. Do not sweep unrelated dirty state into commits.

Do not edit shared JTT task state until you have verified outcomes worth recording. Project truth belongs first in this repo's Sidecar/reports; JTT receives thin pointers / status afterward.

### 6. Keep Jeremy out of the message bus

Jeremy is teaching and working with Chaz on the Week 1 redesign.

Do not ask him to relay worker messages, watch background jobs, choose implementation trivia, or supervise retries.

Escalate only:

- a true pedagogy/policy decision not already settled by authoritative source;
- a destructive/production boundary beyond the authority above;
- a safety classifier/human approval gate;
- a credential/physical action only Jeremy can perform;
- materially conflicting legitimate source intent.

Otherwise manage the work yourself.

## Success for this shift

Best case:

- Week 1 remains verified GREEN and untouched by this lane;
- Week 2 reaches 19/19 production items and is read back cleanly;
- Week 3 is compiled/deployed if its existing source is sufficient;
- later weeks are advanced only where real authored content exists;
- every remaining blocker has an owning layer, evidence, and next bounded unit.

Acceptable case:

- the WAF remains a named yellow but is precisely isolated;
- another source-backed unit advances;
- no regressions or speculative content are introduced.

The metric is **student-useful accepted work**, not how many objects or tokens we can burn.

Clipboard up. Golems get shovels. Keep shipping. 🍪
