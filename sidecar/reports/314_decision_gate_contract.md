# Prompt 314 — Decision Gate contract report

## 1. Starting commit SHA

`2ec8ea82b822a96d6bec987bb0306e51ce51376c` (origin/main at job start; also the
local `worker/prompt309-world-bible` HEAD, which matched origin/main exactly).
Work was done on a fresh worktree branched from `origin/main` at this SHA:
`worker/prompt314-decision-gate`.

## 2. Prompt 305 evidence consumed

`sidecar/reports/305_reasoning_vocabulary_inventory.md` (full inventory read).
Key evidence used:

- The object-level inventory rows for `Reasoning Odyssey`, `Reasoning Quest`,
  `Reasoning Gate`, `Weekly reinforcement`, `Weekly problem-solving write-up`,
  and `Evidence receipt / reasoning receipt`, all flagged ALIAS/OVERLOAD/
  DUPLICATE-HOMEWORK-RISK candidates.
- The "Questions for Jeremy + ChatGPT" section, especially Q1–Q2 (is
  `Reasoning Odyssey` also the weekly package name; should students see
  `Reasoning Quest`, `Reasoning Gate`, or neither), which this prompt's
  settled decision directly answers.
- The finding that `Reasoning Quest` has zero current operational hits
  (proposal/raw-quarry only) and that `Reasoning Gate` as a standalone
  assignment name also has zero current operational hits — only the
  `Weekly reinforcement / Reasoning Odyssey gate` gradebook category exists.

## 3. Files inspected

All files named in the prompt's "Source work authorized" list, plus files
discovered via the term searches below:

- `docs/grading-model.md`
- `planning/fall-2026-weekly-architecture.md`
- `planning/fall-2026-topic-map.md`
- `planning/fall-2026-course-design.md`
- `assignments/weekly-problem-solving-writeup.md`
- `assignments/week-16-farkle-evidence-receipt.md`
- `assignments/pair-reasoning-report.md`
- `assignments/show-and-tell-artifact.md`
- `week-01/README.md`
- `week-01/student/reasoning-method.md`
- `week-01/instructor/tuesday-run-of-show.md`
- `week-01/instructor/thursday-run-of-show.md`
- `week-02/student/week-02-evidence-assignment.md`
- `week-02/instructor/thursday-run-of-show.md`
- `week-16/README.md`
- `planning/week-16.md`
- `planning/week-16-farkle-ml-plan.md`
- `planning/week-16-farkle-ml-target-map.md`
- `docs/career-connection.md`
- `planning/week-01-source-map.md`
- `templates/weekly-rubric.md`
- `sidecar/reports/305_reasoning_vocabulary_inventory.md`

## 4. Files changed/created

Changed (12 files, no files created — no canonical Decision Gate file was
missing; the existing reusable template plus a new section in Week 1's
README supplied the canonical language):

- `docs/grading-model.md`
- `docs/career-connection.md`
- `planning/fall-2026-course-design.md`
- `planning/fall-2026-weekly-architecture.md`
- `planning/week-16.md`
- `planning/week-16-farkle-ml-plan.md`
- `planning/week-16-farkle-ml-target-map.md`
- `week-01/README.md`
- `week-02/student/week-02-evidence-assignment.md`
- `week-16/README.md`
- `assignments/week-16-farkle-evidence-receipt.md`
- `assignments/weekly-problem-solving-writeup.md`

No planning, grading arithmetic, checkpoint, World Bible, Pair Reasoning
contract, Show & Tell contract, or topic-spine file was restructured — only
the student-facing/cross-reference naming for the one recurring weekly
individual reasoning submission was reconciled.

## 5. Final student-facing ontology summary

- **Reasoning Odyssey** = the semester-long journey of the student's
  reasoning (longitudinal frame only). Never the weekly assignment name.
- **Decision Gate** = the one recurring student-facing weekly individual
  reasoning submission. New Week 1 language (`week-01/README.md`, "What you
  submit each week") states this explicitly and is the canonical
  introduction of the term to students.
- Internal-only: the gradebook/category label `weekly reinforcement /
  Reasoning Odyssey gate` (30% of the grade, `docs/grading-model.md`) is the
  category a Decision Gate is graded under. Students are not asked to
  distinguish "weekly reinforcement" from "Decision Gate" as separate
  homework — the report language now says the category *is* the Decision
  Gate, not a second thing next to it.
- `Reasoning Odyssey checkpoints` (15%) remains a distinct, larger,
  occasional-week Odyssey object. This prompt does not touch checkpoint
  semantics, weeks, or weights — that is explicitly out of authority
  (Prompt 315's territory) and is called out as a preserved seam below.

## 6. Canonical Decision Gate contract/template summary

No new grading category, file family, or rubric was invented. The canonical
student-facing definition now lives in `week-01/README.md` under "What you
submit each week": a Decision Gate makes visible whether the student has
enough reasoning and evidence to justify the conclusion carried forward, and
its disciplinary form varies by week while the Sources/Rules-Assumptions/
Work/Check/Decision-Summary shape recurs.

The existing reusable five-part template,
`assignments/weekly-problem-solving-writeup.md`, is now explicitly
cross-referenced as the base shape a Decision Gate may use directly or adapt
into a specialized artifact, with Week 16's evidence receipt cited as the
worked example of a specialized Decision Gate.

## 7. Alias/residual-term classification

| Term | Classification | Notes |
|---|---|---|
| `Reasoning Odyssey` (semester frame) | current doctrine, unchanged | Longitudinal frame only; never renamed to a weekly-submission label. |
| `Reasoning Odyssey gate` / `Weekly reinforcement` (gradebook category, `docs/grading-model.md`) | PRESERVE INTERNAL CATEGORY | Retained as the Canvas/Savnac-facing category name; reworded so it reads as "this category is the Decision Gate," not a second parallel object. |
| `Reasoning Odyssey checkpoints` | PRESERVE INTERNAL CATEGORY / AMBIGUOUS-STOP (checkpoint semantics) | Left untouched; checkpoint week-selection and depth criteria are out of this prompt's authority (see Section 11). |
| `Reasoning Quest` | RENAME TO DECISION GATE (no live occurrences to rename) | Zero current-source hits; only appears in `sidecar/raw/`, `sidecar/reports/`, and `sidecar/prompts/` provenance/prompt files, which are PRESERVE HISTORICAL. |
| `Reasoning Gate` (as a would-be second weekly assignment name) | RENAME TO DECISION GATE (no live occurrences to rename) | Same as above — only ever existed as a raw-quarry proposal and inside the `Reasoning Odyssey gate` category label, which is preserved as an internal category, not renamed away. |
| `weekly problem-solving write-up` / `assignments/weekly-problem-solving-writeup.md` | PRESERVE FUNCTIONAL TERM | Kept as the reusable Sources/Rules/Work/Check/Summary template; new cross-reference line ties it explicitly to "supplies the shape for a Decision Gate," not a second object. |
| `evidence receipt` / `reasoning receipt` | PRESERVE FUNCTIONAL TERM | Kept everywhere it names a format/component (Week 2 six searchable files, Week 16's receipt, the Tuesday presentation-receipt group, Thursday critique/revision receipt). Week 16's file was retitled to lead with "Decision Gate" while keeping "Evidence Receipt" as its format descriptor. |
| `weekly reinforcement` | PRESERVE INTERNAL CATEGORY | Explicitly may remain a gradebook/planning label; source now says students see one name, Decision Gate, for the submission itself. |
| `A3` / `A4` / `A7` (Pair Reasoning / Show & Tell / Friday feedback categories) | PRESERVE INTERNAL CATEGORY | Untouched — distinct category family, not a Decision Gate alias; out of scope per the authority boundary (do not change Pair Reasoning/Show & Tell contracts beyond direct cross-reference consistency). |
| `Coding Odyssey`, `Pair Programming` (stale legacy) | PRESERVE HISTORICAL | Not touched; unaffected by this prompt and outside its scope. |
| Occurrences inside `sidecar/raw/`, `sidecar/reports/`, `sidecar/prompts/`, `reports/`, `runs/`, `archive/`, `raw/` | PRESERVE HISTORICAL | Left as-is; these are provenance/prompt/report material, not current operational source, and old vocabulary appearing there is not an error under the naming discipline. |

## 8. Anti-duplication result

**How many individual weekly reasoning submissions does the student believe
they owe? One — the Decision Gate.**

Verified by re-reading every current operational surface after edits:
`docs/grading-model.md`, `planning/fall-2026-weekly-architecture.md`,
`planning/fall-2026-course-design.md`, `week-01/README.md`,
`week-02/student/week-02-evidence-assignment.md`, `week-16/README.md`,
`planning/week-16.md`, `planning/week-16-farkle-ml-plan.md`,
`planning/week-16-farkle-ml-target-map.md`, and
`assignments/week-16-farkle-evidence-receipt.md`. Each now states the
Decision Gate is the one weekly individual reasoning object; "weekly
reinforcement" is presented only as the gradebook category name, not a
second student-visible obligation. Pair Reasoning (5%, A3-equivalent) and
Show & Tell (5% + 5%, A4/A7-equivalent) remain distinct, separately
scheduled, separately graded categories — `docs/grading-model.md` and
`planning/fall-2026-weekly-architecture.md` already kept their technical
artifacts from duplicating the Decision Gate's technical work (Pair
Reasoning's report is the human-challenge record; Show & Tell's reflection
is the public-defense record), and no change in this prompt widened or
narrowed that boundary.

## 9. Three specialized-week walkthroughs

1. **Proof/counterexample week (e.g., Week 3, Logic/Claims/Proof).** The
   Tuesday reasoning challenge/exit and Thursday Pair Reasoning artifact (a
   checker, counterexample generator, or proof verifier per
   `planning/fall-2026-topic-map.md`) feed the individual Decision Gate via
   the Sources/Rules/Work/Check/Summary shape from
   `assignments/weekly-problem-solving-writeup.md` — a formal proof or
   counterexample stands in for "Work," and the Check step is the student's
   own challenge/test of the proof. No separate "Reasoning Quest" or second
   write-up is required.
2. **Computational/model/simulation week (e.g., Week 9, Probability;
   or Week 8, Counting).** The Decision Gate's "Work" section is a
   simulation, expectation calculation, or enumerator instead of prose
   derivation; "Check" is a cross-check against an alternate metric, sample,
   or independence assumption. The artifact can be code/output plus a short
   interpretation rather than a five-heading essay, consistent with "Do not
   force every specialized week into identical prose fields."
3. **Week 16 Farkle + ML evidence receipt.** `assignments/week-16-farkle-evidence-receipt.md`
   is now titled "Week 16 Decision Gate — Farkle + Machine Learning Evidence
   Receipt" and its Purpose section states it is Week 16's Decision Gate
   using a receipt format, still organized under Sources / Rules-Assumptions
   / Work / Check / One-Sentence Summary headings, and still graded inside
   the same 30% Decision Gate category — no new grading percentage, project
   bucket, or comprehensive exam was introduced. This is the clearest
   existing proof that a specialized receipt functions as a Decision Gate
   without becoming a second assignment family.

## 10. Validation commands/results

```sh
git diff --check
# (no output — no whitespace/conflict-marker errors)

git diff --name-status
# M  assignments/week-16-farkle-evidence-receipt.md
# M  assignments/weekly-problem-solving-writeup.md
# M  docs/career-connection.md
# M  docs/grading-model.md
# M  planning/fall-2026-course-design.md
# M  planning/fall-2026-weekly-architecture.md
# M  planning/week-16-farkle-ml-plan.md
# M  planning/week-16-farkle-ml-target-map.md
# M  planning/week-16.md
# M  week-01/README.md
# M  week-02/student/week-02-evidence-assignment.md
# M  week-16/README.md
```

Focused term searches, run before and after edits (`rg -il --fixed-strings
"<term>" .`), for: `Reasoning Quest`, `Reasoning Gate`, `Reasoning Odyssey
gate`, `weekly reinforcement`, `weekly write-up`, `weekly problem-solving`,
`evidence receipt`, `reasoning receipt`, `Decision Gate`.

- **Before:** `Decision Gate` had zero occurrences anywhere in current or
  historical source (only this prompt file itself and sibling
  prompts/reports referenced it). `Reasoning Quest` and `Reasoning Gate` (as
  a standalone weekly-submission name) had zero occurrences outside
  `sidecar/raw/`, `sidecar/reports/`, and `sidecar/prompts/`.
- **After:** `Decision Gate` now appears consistently across the 12 changed
  operational files (grading model, weekly architecture, course design,
  Week 1/2/16 student-facing pages, career connection, and the two Week 16
  Farkle+ML planning files), always naming the same one weekly individual
  submission. `Reasoning Quest` and `Reasoning Gate` remain absent from
  current operational source and unchanged in `sidecar/` provenance
  (PRESERVE HISTORICAL — not an error).

Full diff was inspected manually (`git diff`, reproduced during this job);
every hunk stays within terminology/cross-reference wording — no grading
arithmetic, week numbering, checkpoint policy, or rubric criteria changed.

## 11. Unresolved seams returned to Jeremy + ChatGPT

These were touched only enough to keep cross-references consistent and are
explicitly not decided here, per the authority boundary:

1. **Checkpoint semantics.** What makes a `Reasoning Odyssey checkpoint`
   larger/deeper than an ordinary Decision Gate, and which weeks are
   checkpoint weeks, remains open (`docs/grading-model.md` still says "with
   the specific weeks published in the course schedule"). This is Prompt
   315's territory; only the Decision Gate side of the boundary was
   clarified here.
2. **World Bible carry-forward.** `planning/fall-2026-weekly-architecture.md`
   and `week-02/student/week-02-evidence-assignment.md` still treat World
   Bible context as optional/not graded. This prompt did not touch or decide
   World Bible schema, cadence, or carry-forward policy (Prompt 309's
   territory).
3. **Internal category label wording.** `docs/grading-model.md` still uses
   the compound `Weekly reinforcement / Reasoning Odyssey gate` internally
   in a few spots (e.g., inside the checkpoint-family aggregate-check
   sentence and in `planning/week-16.md` and the two Week-16-Farkle-ML
   planning files) rather than being fully collapsed to `Decision Gate`
   everywhere. This was a deliberate choice to preserve the internal
   category name (per the naming discipline's PRESERVE INTERNAL CATEGORY
   rule) rather than perform an indiscriminate global rename of the
   gradebook label itself — flagging it in case Jeremy + ChatGPT want the
   internal category label itself renamed in a later, explicitly authorized
   pass.
4. **`planning/fall-2026-course-design.md`'s Week 1–16 pedagogical-intent
   table** (lines ~65–82) still uses old per-week "Write-up N" labels inside
   a table the document itself says is superseded by the spine/weekly
   architecture/topic map and "not... the dated week allocation." Left
   untouched as PRESERVE HISTORICAL/pedagogical-intent material rather than
   current operational contract; flagged here in case that table should
   later be retired or relabeled.

## 12. Final commit SHA / working-tree state

Branch: `worker/prompt314-decision-gate`
Committed and pushed to `origin/worker/prompt314-decision-gate`.
Final commit SHA: see companion message (recorded after commit/push below).
