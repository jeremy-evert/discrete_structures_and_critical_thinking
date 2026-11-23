# Prompt 304 — Reconcile Pair Reasoning as the DSCT pair-activity name

**Status:** FOREMAN-READY MECHANICAL  
**Source quarry:** `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md`  
**Scope:** `jeremy-evert/discrete_structures_and_critical_thinking` only  
**Required report:** `sidecar/reports/304_pair_reasoning_name_reconciliation.md`

## Decision already made

The recurring DSCT pair activity is named:

> **Pair Reasoning**

`Pair Programming` is no longer the conceptual/student-facing name for that recurring course activity.

This prompt does **not** decide what Pair Reasoning means pedagogically. That decision is already outside this work order. Programming may still be one tool used during Pair Reasoning, and ordinary technical references to programming remain valid when they actually mean programming.

The source quarry records the reason for the change:

> It is no longer sufficient to write a program. We need reasoning. As steel sharpens steel, one reasoner sharpens another.

Known current-source seams include at least:

- `planning/fall-2026-weekly-architecture.md`
- `planning/fall-2026-topic-map.md`
- `docs/grading-model.md`

Do not assume that list is complete.

## Why this is Foreman-ready

The only authorized judgment is textual/source reconciliation against an already-settled name. The worker may locate stale uses, classify them by role, and update unambiguous current-course terminology. The worker may not redesign the activity, its grading semantics, or the semester cadence.

## Required work

### 1. Establish the before-state

Search the entire DSCT repository for terminology that may denote the old recurring activity, including at minimum:

- `Pair Programming`
- `pair programming`
- `Pair Programming report`
- `paired-programming`
- `paired programming`
- A3-equivalent labels where context clearly identifies the DSCT recurring pair activity

Record the exact search commands and every relevant hit in the report before editing.

### 2. Classify every relevant hit

Assign each relevant hit exactly one disposition:

- **RENAME** — current DSCT doctrine, planning, assignment, rubric, or student-facing language that denotes the recurring activity;
- **PRESERVE-TECHNICAL** — the text genuinely refers to programming as a tool/task rather than the course activity name;
- **PRESERVE-HISTORICAL** — historical/provenance/raw evidence that should not be rewritten;
- **AMBIGUOUS-STOP** — changing it would require a pedagogical, grading, scheduling, or ontology decision.

The report must include path, line/context, disposition, and reason for every relevant hit.

### 3. Reconcile only unambiguous current terminology

For **RENAME** hits:

- change the recurring activity name to **Pair Reasoning**;
- adjust nearby grammar where needed so the text reads naturally;
- update cross-references or labels only when required to keep the same object coherent;
- preserve any real programming-specific meaning inside the activity description.

Do not perform unrelated cleanup while touching these files.

### 4. Preserve evidence and history

Do not rewrite the raw design quarry, historical reports, archived evidence, or provenance solely to make search results prettier.

If a historical artifact is actively masquerading as current doctrine, report that seam rather than silently converting historical evidence into current source.

### 5. Produce the required report

Create `sidecar/reports/304_pair_reasoning_name_reconciliation.md` containing:

1. starting commit SHA;
2. exact search commands used;
3. before-state hit inventory;
4. disposition table for every relevant hit;
5. files changed;
6. files deliberately preserved;
7. ambiguous seams returned to Jeremy + ChatGPT;
8. validation commands and results;
9. final commit SHA or working-tree state, depending on the execution environment.

## Authority boundary / hard stops

Do **not**:

- redesign Pair Reasoning;
- invent or revise Pair Reasoning reflection questions;
- change grading weights, points, assignment-group structure, or due rules;
- decide whether peer feedback is separate or embedded;
- change the Week 4–14 Pair Reasoning / Show & Tell cadence;
- decide Week 4's first Show & Tell content;
- rename or redefine Reasoning Odyssey, Reasoning Quest/Gate, World Bible, evidence receipt, or Show & Tell;
- change Week 2/3 content allocation;
- touch production Savnac or Canvas;
- perform broad wording cleanup unrelated to this naming migration.

If a proposed rename would force any of those decisions, classify it **AMBIGUOUS-STOP**, leave the source unchanged, and report it.

## Verification battery

Run and record all applicable checks.

### A. Diff hygiene

- `git diff --check`
- `git diff --name-only`
- inspect the full diff and confirm every content change is required by this naming reconciliation or its direct grammatical/cross-reference consequence.

### B. Residual terminology search

Repeat the old-name searches after editing.

A nonzero residual count is allowed. **Every residual relevant hit must be present in the report and justified as `PRESERVE-TECHNICAL`, `PRESERVE-HISTORICAL`, or `AMBIGUOUS-STOP`.**

There must be no unexplained old-name hit in current operational DSCT doctrine/student-facing source.

### C. New-name presence

Search for `Pair Reasoning` and confirm the known current planning/grading surfaces now use the new name where they refer to the recurring pair activity.

At minimum, explicitly inspect:

- `planning/fall-2026-weekly-architecture.md`
- `planning/fall-2026-topic-map.md`
- `docs/grading-model.md`

### D. Semantic spot-check

For every changed file, read the paragraph/table row around the edit and verify that:

- `Pair Reasoning` names the recurring activity;
- references to actual programming have not been incorrectly erased;
- no grading, cadence, or assignment semantics changed accidentally.

## Definition of done

Prompt 304 is complete only when all of the following are true:

1. every relevant old-name hit has an explicit disposition;
2. every unambiguous current/student-facing recurring-activity label uses **Pair Reasoning**;
3. historical and genuine programming references are preserved where appropriate;
4. no pedagogical/grading/cadence decision was made by implication;
5. the residual-search audit has no unexplained hit;
6. `git diff --check` passes;
7. the required report contains enough evidence for another person to reproduce the audit without trusting the worker's summary.

If any item cannot be satisfied without a new course-design decision, stop at that seam and return it explicitly rather than guessing.