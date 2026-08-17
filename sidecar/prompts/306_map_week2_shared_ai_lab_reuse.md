# Prompt 306 — Map reusable Week 2 AI Lab material before DSCT authoring

**Status:** FOREMAN-READY READ-ONLY ARCHAEOLOGY / REUSE MAP  
**Source quarry:** `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md`  
**Primary write scope:** DSCT report/evidence only  
**Required report:** `sidecar/reports/306_week2_shared_ai_lab_reuse_map.md`

## Decision already made

The intended DSCT Week 2 identity is:

> **Building Your AI Lab**

Week 2 should not independently recreate material that already has a canonical owner elsewhere.

The known source areas to inspect are:

- `jeremy-evert/local_ai_lab_setup`
- `jeremy-evert/windows_classroom`
- `jeremy-evert/computer_science_2`
- `jeremy-evert/computer_architecture`
- current and historical Week 2 material inside `jeremy-evert/discrete_structures_and_critical_thinking`

The reusable evidence discipline to investigate is:

> **Check -> Baseline -> bounded AI proposal -> Diff -> Final -> read/reason -> accept or reject from evidence**

The intellectual framing worth tracing from Computer Architecture is the distinction between AI/tool suggestion and independent evidence.

## Decision explicitly NOT made

Prompt 306 does **not** choose:

- the final DSCT bounded exercise;
- whether DSCT reuses `format_student_name` or substitutes a reasoning-flavored exercise;
- final Pair Reasoning prompts;
- final Week 2 reflection language;
- final student-facing Week 2 sequencing beyond identifying reusable source ownership.

Those choices return to Jeremy + ChatGPT.

## Why this is Foreman-ready

The worker is being asked to answer factual questions:

- what material exists now;
- which repository owns it;
- what commit/path contains it;
- what current validation evidence exists;
- which pieces are generic versus course-specific;
- what DSCT would still have to author after reuse.

That is archaeology and provenance mapping, not pedagogy.

## Required work

### 1. Freeze the evidence base

For every repository inspected, record:

- repository name;
- branch/ref inspected;
- exact commit SHA at the start of the investigation;
- relevant paths.

Use current `main` unless a historical branch is being inspected explicitly as archaeology.

Do not use floating descriptions such as "latest CS2 version" without a commit receipt.

### 2. Map ownership before content

Build an ownership table covering at least:

- canonical shared student-facing AI Lab instruction;
- readiness assignment/rubric if present;
- Windows execution/runtime harness;
- `Check` behavior;
- `Baseline` behavior;
- bounded AI/Aider launch path;
- `Diff` behavior;
- independent `Final` verification;
- reset/recovery path if present;
- CS2 course-specific sequencing/wrapper;
- Computer Architecture epistemic framing;
- existing DSCT Week 2 source;
- historical/incoming DSCT Week 2 branches.

For each row, identify the **owning repository** rather than merely the repository where a copy/reference happens to appear.

### 3. Build a reuse-disposition matrix

Classify each candidate artifact or mechanism as exactly one of:

- **POINTER / REUSE CANONICAL** — DSCT should reference the owning source rather than fork it;
- **ADAPT FOR DSCT** — structure/mechanism is reusable but DSCT must author a course-specific wrapper;
- **COURSE-SPECIFIC / DO NOT COPY** — useful evidence but belongs to the sibling course;
- **STALE / SUPERSEDED** — evidence exists but should not drive Fall 2026 authoring;
- **OPEN PEDAGOGICAL CHOICE** — cannot be selected without Jeremy + ChatGPT;
- **MISSING** — a required role in the intended loop has no current owner/source.

Every row must include repository + commit SHA + path and a short reason.

### 4. Prove the evidence loop stage by stage

Create a separate continuity table for:

1. `Check`
2. `Baseline`
3. bounded AI proposal / launch
4. `Diff`
5. `Final`
6. read/reason
7. accept/reject from evidence
8. reset/recovery, if part of the current contract
9. readiness/reflection receipt, if part of the current contract

For each stage, report:

- owning source;
- exact path;
- whether it is instruction, code/harness, assignment/rubric, or course wrapper;
- current verification tier.

Use these verification tiers:

- **EXISTS** — artifact/path exists;
- **SOURCE-COHERENT** — source and surrounding contract agree on what it does;
- **VALIDATED-BY-RECEIPT** — a prior report/run proves execution, with exact receipt path + commit;
- **EXECUTED-NOW** — worker safely executed a non-destructive validation during Prompt 306 and recorded command/output;
- **UNVERIFIED** — existence is known but behavior has not been demonstrated.

Do **not** promote `EXISTS` to `VALIDATED` just because prose says a harness works.

### 5. Inspect DSCT historical Week 2 work without merging

Locate known incoming/historical Week 2 branches or artifacts.

For each:

- record branch/ref and commit;
- compare conceptually against current `main` and current intended Week 2 identity;
- identify salvageable material;
- identify stale assumptions;
- identify conflicts requiring design choice.

Do not merge, cherry-pick, or rewrite history.

### 6. Identify the DSCT delta

End the report with a compact **DSCT STILL OWNS** section.

It must separate:

- course-specific framing that clearly needs authoring later;
- pedagogical choices that Jeremy + ChatGPT must make;
- actual missing infrastructure, if any;
- content that should remain a pointer to another canonical owner.

Do not fill those gaps in this prompt.

## Required report

Create `sidecar/reports/306_week2_shared_ai_lab_reuse_map.md` containing:

1. starting DSCT commit SHA;
2. repository/ref/commit inventory for every external source inspected;
3. ownership table;
4. reuse-disposition matrix;
5. stage-by-stage evidence-loop continuity table;
6. validation-tier evidence and receipt paths;
7. DSCT historical-branch archaeology;
8. `DSCT STILL OWNS` section;
9. unresolved Jeremy + ChatGPT decisions;
10. verification commands/results.

## Write authority

Allowed writes are limited to:

- `sidecar/reports/306_week2_shared_ai_lab_reuse_map.md`;
- optional clearly named Prompt-306 evidence under `sidecar/runs/306_*`.

Do not modify source in DSCT or any sibling/shared repository.

## Hard stops

Do **not**:

- choose or author the final DSCT Week 2 bounded exercise;
- blindly import CS2's `format_student_name` exercise;
- write final Week 2 student lessons;
- decide final Pair Reasoning/reflection prompts;
- change Week 2 grading weights or category semantics;
- decide Week 3 container/LaTeX design;
- mutate shared/sibling repositories;
- merge/cherry-pick historical DSCT branches;
- install or reconfigure system software merely to raise a validation tier;
- perform destructive/reset actions on a live student or production environment;
- write to Savnac/Canvas.

If a fact cannot be established safely, mark it **UNVERIFIED** rather than expanding scope.

## Verification battery

### A. Provenance audit

Every candidate in the reuse matrix must have:

- repository;
- exact commit SHA/ref;
- path;
- disposition;
- reason.

No provenance-free recommendation passes.

### B. Evidence-loop completeness

All required stages of the `Check -> Baseline -> bounded proposal -> Diff -> Final -> read/reason -> accept/reject` loop must appear in the continuity table as either mapped or explicitly **MISSING/UNVERIFIED**.

Silently omitting a stage is failure.

### C. Validation-claim audit

Every claim that a path is "tested," "working," "validated," or equivalent must be backed by either:

- an exact prior receipt/report/run path and commit; or
- an `EXECUTED-NOW` command/output receipt.

Otherwise downgrade the claim to `EXISTS`, `SOURCE-COHERENT`, or `UNVERIFIED`.

### D. Duplication audit

Explicitly identify any place DSCT currently duplicates content with a canonical shared owner. Do not fix it here. Report whether later authoring should point, adapt, or retire the duplicate.

### E. Write-scope audit

Run:

- `git diff --check`
- `git diff --name-only`

Only the required report and optional Prompt-306 run evidence may change.

Where local sibling checkouts are used, verify they remain unmodified.

## Definition of done

Prompt 306 is complete only when:

1. canonical ownership is explicit for every reusable Week 2 role found;
2. every reuse recommendation has repo + commit + path provenance;
3. the evidence loop is mapped stage by stage with honest validation tiers;
4. historical DSCT Week 2 work has been inventoried without merging it;
5. duplication and stale/superseded material are visible;
6. the exact DSCT delta is explicit;
7. pedagogical choices remain unresolved and clearly returned to Jeremy + ChatGPT;
8. no source repository was mutated;
9. another author can begin DSCT Week 2 design without repeating this archaeology or accidentally forking canonical shared content.