# LUNA-DSCT-01 — Worksite boundary and branch archaeology

**Date:** 2026-08-16
**Repository:** `discrete_structures_and_critical_thinking`
**Checked commit:** `b4ec183` (`main`, `origin/main`)
**Scope:** read-only inventory; no branch checkout, merge, deletion, or live
Canvas/Savnac action.

## Sitrep

- The checkout is on `main`, aligned with `origin/main`, and has one
  pre-existing untracked file:
  `prompts/305_week2_assessment_contract_reconciliation.md`. It was preserved
  unchanged.
- No root `AGENTS.md` exists. No `sidecar/` directory exists. The repository's
  local operating guidance is therefore `README.md`, `prompts/README.md`, the
  current source files, and the reports/runs evidence already committed.
- `README.md` is a historical placeholder (“under construction”, pivoted on
  2026-07-14), not a current operational course map.
- `prompts/`, `reports/`, `raw/`, and `runs/` are legacy/root coordination and
  evidence surfaces. They contain useful provenance, but they are not by
  themselves authoritative over current course files.
- Current course truth is the committed `main` package: `course_metadata.yaml`,
  `planning/`, `week-01/`, `week-02/`, `assignments/`, `lessons/`, and
  `docs/grading-model.md`, interpreted with the accepted reports 300E, 301,
  302, 303, and 304.

## Incoming branch matrix

Both incoming branches fork at `f2e7977` (`Contract DSCT Fall 2026 semester
spine and weekly architecture`) and are not descendants of current `main`.

| Surface | `origin/agent/prompt303-dsct-week2` | `origin/agent/prompt305-dsct-assessment` | Decision against current `main` |
|---|---|---|---|
| Week 2 instructional files | Rewrites `week-02/README.md`, instructor run-of-shows, and student paths; adds nested Tuesday/Thursday guides and container examples; deletes the prior flat activity/assignment/rubric paths. | Carries the same competing Week 2 rewrite. | **Superseded as a package.** Do not merge either branch wholesale. The merged `main` Week 2 package is current truth. |
| `docs/grading-model.md` | Deletes the grading model. | Deletes the grading model. | **Forbidden to resurrect/delete.** `main`'s accepted named-category model is authoritative. |
| Assessment contract | Not present as a dedicated additive contract. | Adds `assessment/week-02-readiness-assessment-contract.yaml` and approved-materials manifest. | **Salvage candidate.** Port only after repointing stale paths to current `main` and validating every reference. |
| Assessment fixtures | Not present as the complete contract battery. | Adds eight Week 2 fixtures plus manifest under `assessment/fixtures/week-02/`. | **Salvage candidate.** Additive port only; do not import the branch's competing Week 2 tree. |
| Historical prompts/reports/raw/runs | Deletes several root artifacts while adding its own run evidence. | Same broad deletion set plus assessment evidence. | **Preserve provenance.** No bulk cleanup in this inventory unit. |
| `.gitignore` | Deletes the tracked file. | Deletes the tracked file. | **Reject.** Current `main` protection remains. |

## Keep / reimplement / superseded / conflict matrix

| Artifact or boundary | Classification | Evidence / next handling |
|---|---|---|
| `main` Week 2 package (`week-02/`, reports 303/304) | Keep / authoritative | Merged by `b4ec183`; Prompt 305 itself says the package is already merged and live. |
| `docs/grading-model.md` | Keep / authoritative | Present on `main`; both incoming branches delete it. |
| `course_metadata.yaml`, `planning/`, Week 1, assignments, lessons | Keep | Current course source; no reason found to replace them during archaeology. |
| `origin/agent/prompt303-dsct-week2` | Superseded whole-package branch; salvage selectively | Its instructional prose and evidence may explain provenance, but its paths/layout conflict with `main`. Leave branch untouched. |
| `origin/agent/prompt305-dsct-assessment` | Conflict as a whole; additive salvage source | Its assessment contract/fixtures are explicitly identified by untracked Prompt 305 as worth porting. Use `git show` path reads, not checkout/merge. |
| `prompts/305_week2_assessment_contract_reconciliation.md` | Active local work request; preserve | Pre-existing untracked file. It defines the additive-only port, forbidden paths, acceptance check, and report destination. Do not stage it in this inventory commit. |
| Root `prompts/`, `reports/`, `raw/`, `runs/` | Historical evidence / legacy coordination | Preserve until a separately authorized layout-reconciliation unit classifies and moves artifacts. |
| Missing `AGENTS.md` and `sidecar/` | Worksite boundary gap | Do not invent a sidecar migration here. Future work should use the repository's existing reports/runs convention unless a separate boundary decision creates sidecar structure. |
| Root `README.md` and `prompts/README.md` | Stale operational guidance | Candidate for LUNA-DSCT-02, not modified here. |
| `assignments/programming-exam.md` | Open source artifact, not classified by this read-only pass | JTT separately calls for its audit; defer to that bounded item. |

## Branch safety verdict

The two `agent/*` branches are reconciliation inputs, not merge candidates.
Their common base predates the merged Week 2 work, and both contain broad
deletions/replacements that would regress current truth (especially the
grading model and the flat Week 2 package). The safe next implementation unit
is the already-authored Prompt 305 additive assessment-contract port:

1. read current `main` Week 2 paths as authority;
2. read only the assessment contract, approved-materials manifest, and fixture
   files from `origin/agent/prompt305-dsct-assessment`;
3. repoint any stale paths;
4. add the contract/fixtures without modifying `week-02/`, grading, metadata,
   or Week 1; and
5. run the prompt's explicit YAML path-existence acceptance check.

No branch was checked out, merged, pushed, pruned, or otherwise mutated by
this inventory.
