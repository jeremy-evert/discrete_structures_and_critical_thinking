# Prompt 310 — Inventory stale DSCT source seams and repair dependencies

**Status:** FOREMAN-READY READ-ONLY SOURCE-CONFLICT AUDIT  
**Source quarry:** `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md`  
**Primary write scope:** DSCT report/evidence only  
**Required report:** `sidecar/reports/310_dsct_stale_source_seam_inventory.md`

## Purpose

Prompt 310 produces a dependency-aware map of contradictions between current DSCT source, newer design decisions/directions, historical artifacts, sibling/shared assumptions, and downstream compiler/deployment expectations.

It is an **audit**, not a cleanup pass.

The worker must identify:

- what the conflicting sources actually say;
- which side of the conflict is already decided versus still open;
- what downstream artifacts depend on the stale contract;
- what can later be repaired mechanically;
- what is blocked on Jeremy + ChatGPT design judgment;
- what is historical/provenance only and should not be "fixed";
- what is already GREEN and should not be rebuilt.

## Known seams that must be accounted for

At minimum, Prompt 310 must explicitly inspect and disposition these known seams:

1. stale `Pair Programming` naming versus the decided **Pair Reasoning** name;
2. older Week 2/3 contract versus newer **Week 2 Building Your AI Lab / Week 3 Containers + minimum-useful LaTeX** direction;
3. twelve formal topic bundles in Weeks 3–14 versus eleven formal core slots in Weeks 4–14;
4. grading-model surfaces that may have useful weights but stale naming and unresolved checkpoint/due/revision mechanics;
5. historical ZyBooks/textbook material that should remain provenance rather than become an operational required path;
6. Week 16 Farkle + ML as already validated/GREEN work that should be integrated, not casually rebuilt;
7. historical/incoming Week 2 and assessment branches as archaeology/salvage inputs rather than blind merge targets;
8. Course Foundry/compiler/Savnac assumptions that may encode older Week 2/3, Pair Programming, grading, or course-structure contracts;
9. Reasoning Odyssey / Quest / Gate / World Bible vocabulary seams identified by current DSCT source;
10. shared AI Fluency / Professional Minds / local-AI/container ownership seams where DSCT may currently duplicate or contradict canonical external sources.

Do not assume this list is complete.

## Design-status vocabulary

For every newer direction cited from the quarry or another current design source, classify its authority as:

- **DECIDED** — Jeremy has explicitly settled the decision and later work may reconcile source to it;
- **STRONG DIRECTION** — current preferred design, but a later design pass may still refine it;
- **OPEN QUESTION** — intentionally unresolved;
- **HISTORICAL ONLY** — useful context, not current direction.

Do not promote a `STRONG DIRECTION` or `OPEN QUESTION` into doctrine merely because it appears later in time.

## Seam-status vocabulary

Assign every seam one primary status:

- **READY-MECHANICAL** — resolution is already decided; a later bounded prompt can reconcile it safely;
- **BLOCKED-DESIGN** — requires Jeremy + ChatGPT judgment before source can be changed;
- **EXTERNAL-DEPENDENCY** — local repair depends on another repository/source contract;
- **HISTORICAL-PRESERVE** — apparent inconsistency is historical/provenance evidence and should remain;
- **ALREADY-RESOLVED** — current source already reflects the newer decision;
- **ALREADY-GREEN / DO-NOT-REBUILD** — validated work should be integrated/preserved;
- **AMBIGUOUS** — evidence conflicts or authority is unclear.

Also assign an impact level:

- **HIGH** — could cause wrong student-facing course structure, grading, schedule, or deployment;
- **MEDIUM** — could mislead authors/agents or create duplicate/stale work;
- **LOW** — mostly historical/documentation noise with little operational risk.

Impact is not permission to fix the seam.

## Required work

### 1. Freeze the evidence base

Record:

- DSCT current branch/ref and starting commit SHA;
- relevant historical/incoming DSCT branch names and commit SHAs;
- external repository/ref/commit SHAs for any sibling/shared/compiler source inspected.

Do not use floating descriptions such as "the current Course Foundry" without a commit receipt.

### 2. Inspect known DSCT source surfaces

At minimum inspect:

- `planning/fall-2026-spine.md`
- `planning/fall-2026-weekly-architecture.md`
- `planning/fall-2026-topic-map.md`
- `planning/fall-2026-course-design.md`
- `docs/grading-model.md`
- assignments and rubrics relevant to pair/show/Odyssey/grading semantics;
- current Reasoning Odyssey / World Bible surfaces;
- Week 2 source/history;
- Week 16 validated package/report;
- historical ZyBooks/source-decision material;
- `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md` as design evidence, not automatic doctrine.

If a named path no longer exists, record `NOT PRESENT` rather than silently substituting something else.

### 3. Inspect downstream/external assumptions

Read-only inspect, where accessible and relevant:

- Course Foundry DSCT desired-course/compiler/push source;
- shared AI Fluency sources;
- Professional Minds sources;
- `local_ai_lab_setup`;
- `windows_classroom`;
- container curriculum/foundations;
- sibling CS2/Computer Architecture source only where it owns a contract DSCT references.

For every external finding, record repository + exact commit/ref + path.

Do not turn this into a broad sibling-course review. Follow only dependencies that touch a DSCT seam.

### 4. Build the seam matrix

Each seam row must contain:

- seam ID;
- short name;
- impact level;
- current source path(s);
- exact current statement/contract summarized faithfully;
- newer conflicting decision/direction source;
- design-status classification: `DECIDED / STRONG DIRECTION / OPEN QUESTION / HISTORICAL ONLY`;
- seam status;
- student-facing risk, if any;
- authoring/agent risk, if any;
- downstream files/repositories/systems affected;
- relevant sibling/shared owner, if any;
- safe mechanical repair that would become possible after decisions are frozen, if known;
- blocking Jeremy + ChatGPT decision, if any;
- related Prompt 304–309 evidence job, if applicable;
- evidence/provenance paths.

Do not put a proposed pedagogical answer in the `safe mechanical repair` field.

### 5. Build a dependency graph/table

Create a second table showing which seams depend on which evidence/decisions before repair.

At minimum account for relationships such as:

- Pair Reasoning naming -> Prompt 304;
- DSCT vocabulary/ontology -> Prompt 305;
- Week 2 shared ownership/reuse -> Prompt 306;
- Week 3 toolchain evidence -> Prompt 307;
- Week 4–14 resource evidence -> Prompt 308;
- World Bible lineage -> Prompt 309;
- eleven-week core-spine choice -> Jeremy + ChatGPT design decision after relevant evidence;
- Course Foundry/Savnac reconciliation -> only after source contracts are frozen.

This is a dependency map, not permission to schedule or execute all repairs.

### 6. Audit operational textbook/ZyBooks leakage

Search current operational source for:

- required textbook language;
- ZyBooks assignment/readings as current requirements;
- old chapter/section assumptions that a student would still be expected to follow.

Classify each hit as:

- current operational requirement;
- historical/provenance;
- source-mapping reference only;
- ambiguous.

Do not delete historical evidence.

### 7. Audit Week 16 preservation boundary

Locate exact evidence that Week 16 Farkle + ML is validated/GREEN.

Record:

- DSCT commit/ref;
- report/path;
- key artifact paths;
- any Course Foundry/deployment dependency;
- which later seams may legitimately integrate it without rebuilding it.

Mark any proposed work that would unnecessarily re-author validated Week 16 as a `DO-NOT-REBUILD` risk.

### 8. Audit incoming/historical branches without merging

For each relevant incoming/historical DSCT branch:

- record branch and commit SHA;
- compare against current `main` enough to identify unique files/content relevant to current seams;
- classify unique material as potentially salvageable, stale, superseded, or decision-dependent;
- record merge/cherry-pick risk.

Do not merge, rebase, cherry-pick, or delete branches.

### 9. Audit Course Foundry/compiler assumptions

Identify exact DSCT compiler/desired-course/push code or configuration that assumes:

- old Week 2/3 structure;
- old Pair Programming name;
- old topic-week allocation;
- old grading/object names;
- other stale source contracts.

Report the dependency. Do not edit compiler/deployment code here.

## Required report

Create `sidecar/reports/310_dsct_stale_source_seam_inventory.md` containing:

1. starting DSCT commit SHA;
2. branch/ref/commit inventory;
3. inspected source-surface checklist;
4. known-seam checklist with explicit disposition for all ten required seams;
5. full seam matrix;
6. dependency graph/table;
7. textbook/ZyBooks leakage audit;
8. Week 16 GREEN preservation evidence;
9. historical/incoming branch audit;
10. Course Foundry/downstream assumption audit;
11. high-impact unresolved seams;
12. ready-mechanical seams;
13. explicit Jeremy + ChatGPT decisions still blocking repair;
14. verification commands/results.

## Write authority

Allowed writes are limited to:

- `sidecar/reports/310_dsct_stale_source_seam_inventory.md`;
- optional Prompt-310 audit evidence under `sidecar/runs/310_*`.

This prompt must not repair course source.

## Hard stops

Do **not**:

- solve the eleven-week intellectual spine;
- decide how twelve current topic bundles collapse into eleven slots;
- decide the final Reasoning Odyssey / Quest / Gate / World Bible ontology;
- decide grading weights, due policy, revision policy, drop rules, or checkpoint weeks;
- duplicate Prompt 304's Pair Reasoning repair if it has not yet run;
- perform Prompt 305–309's design/evidence jobs wholesale instead of merely recording dependencies;
- merge/cherry-pick incoming branches;
- reintroduce ZyBooks/textbook requirements;
- rebuild Week 16;
- edit Course Foundry/compiler code;
- bulk-edit stale files;
- write Savnac/Canvas.

If an obvious repair depends on an unresolved decision, mark it `BLOCKED-DESIGN` rather than fixing it.

## Verification battery

### A. Required-seam coverage

All ten known seams listed at the top of this prompt must appear in the report with one of:

- evidence-backed seam row;
- `ALREADY-RESOLVED` with proof;
- `NOT PRESENT` with inspected paths/search evidence.

No known seam may disappear silently.

### B. Source/provenance audit

Every seam must cite:

- current source path/ref;
- conflicting/newer direction source;
- external repo + commit + path where an external dependency is involved.

No memory-only seam passes.

### C. Authority audit

Every newer direction must be labeled `DECIDED`, `STRONG DIRECTION`, `OPEN QUESTION`, or `HISTORICAL ONLY`.

The report fails if raw-quarry ideas are silently treated as settled doctrine.

### D. Dependency audit

Every `BLOCKED-DESIGN` seam must name the specific decision blocking it.

Every `READY-MECHANICAL` seam must explain why the required policy/meaning is already settled.

### E. Historical preservation audit

Historical/provenance material, including ZyBooks decisions and incoming branches, must remain intact. The report must distinguish historical evidence from operational source rather than optimizing for zero search hits.

### F. Week 16 preservation audit

The report must include exact GREEN/validated Week 16 evidence and explicitly identify it as a preservation boundary.

### G. Write-scope audit

Run:

- `git diff --check`
- `git diff --name-only`

Only the required report and optional Prompt-310 audit evidence may change in DSCT. External repositories must remain unmodified.

## Definition of done

Prompt 310 is complete only when:

1. every known seam has an explicit evidence-backed disposition;
2. additional discovered seams are added rather than ignored;
3. settled decisions are distinguished from strong directions and open questions;
4. downstream compiler/shared/deployment dependencies are traceable by exact repo/ref/path;
5. all `BLOCKED-DESIGN` seams name their blocking decision;
6. all `READY-MECHANICAL` seams have a clear reason they are safe to repair later;
7. historical evidence is preserved;
8. Week 16's GREEN boundary is proven and protected;
9. incoming branches are inventoried without merging;
10. no course source or external repository was modified;
11. Jeremy + ChatGPT can use the report to author later repair prompts in dependency order without repeating the conflict archaeology.