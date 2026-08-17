# Prompt 305 — Inventory DSCT Reasoning Odyssey / World Bible / Quest vocabulary

**Status:** FOREMAN-READY READ-ONLY ARCHAEOLOGY  
**Source quarry:** `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md`  
**Primary scope:** `jeremy-evert/discrete_structures_and_critical_thinking`  
**Required report:** `sidecar/reports/305_reasoning_vocabulary_inventory.md`

## Decision context already known

The durable course direction is:

> **Reasoning Odyssey**

The design quarry also says the weekly formal work, Reasoning Quest/Gate, World Bible, Pair Reasoning, Show & Tell, and event reflections should feed one coherent learning trail rather than becoming parallel homework systems.

What is **not** decided yet is the final student-facing ontology among terms such as:

- Reasoning Odyssey;
- Reasoning Quest;
- Reasoning Gate;
- weekly write-up;
- weekly reinforcement;
- checkpoint;
- evidence receipt;
- event reflection;
- Pair Reasoning reflection/report;
- Show & Tell reflection;
- peer-feedback report;
- World Bible;
- legacy Coding Odyssey / coding-odyssey variants.

Prompt 305 gathers the evidence needed for Jeremy + ChatGPT to make that ontology decision later. It does not make the decision.

## Why this is Foreman-ready

Repository archaeology is mechanical if the worker is forbidden from normalizing vocabulary. The useful output is a trustworthy map of what names currently exist, what objects they appear to denote, where they came from, and where the same work may have multiple labels.

## Scope boundary relative to Prompt 309

Prompt 305 is **DSCT vocabulary archaeology**.

Prompt 309 is the deeper **cross-course World Bible provenance** job.

For Prompt 305, inspect CS1/CS2 only when a DSCT source explicitly points to a sibling A-number, object, or naming source and that limited lookup is needed to explain the DSCT term. Do not duplicate Prompt 309's broad cross-course World Bible archaeology.

## Required work

### 1. Establish a vocabulary search set

Search DSCT for the terms above plus obvious capitalization, spacing, hyphenation, singular/plural, and legacy variants.

At minimum include searches for:

- `Reasoning Odyssey`
- `Coding Odyssey`
- `Reasoning Quest`
- `Reasoning Gate`
- `World Bible`
- `weekly reinforcement`
- `weekly write-up`
- `checkpoint`
- `evidence receipt`
- `reflection`
- `Pair Reasoning`
- `Pair Programming`
- `Show & Tell`
- `A3`, `A4`, `A7` where those labels appear to be semantic inheritance rather than arbitrary identifiers

Record exact search commands in the report.

### 2. Build an object-level inventory

Do not make one row per raw text hit. Consolidate hits that clearly describe the same object in the same source family.

For each distinct current or historically relevant object/term, record:

- term/label;
- representative path(s);
- current, historical/provenance, or ambiguous status;
- apparent student action;
- apparent artifact produced;
- whether it appears to create a gradebook object;
- whether it is persistent across weeks or event-specific;
- whether it is individual, pair, peer-feedback, or public-defense work;
- whether another term appears to describe substantially the same work;
- source/provenance note;
- confidence in the interpretation: **HIGH / MEDIUM / LOW**.

### 3. Separate names from functions

Create a second compact matrix with two columns that matter for later design:

- **name currently used**;
- **function the source appears to require**.

This is important because two names may describe one function, or one name may be used for two different functions.

### 4. Identify collision classes

Explicitly flag:

- **ALIAS** — multiple labels appear to denote the same work;
- **OVERLOAD** — one label appears to denote different work in different places;
- **DUPLICATE-HOMEWORK RISK** — two artifacts appear to ask students to report the same reasoning twice;
- **STALE-LEGACY** — an older label remains but appears superseded;
- **GRADEBOOK-SEAM** — naming cannot be changed safely without a grading/category decision;
- **UNRESOLVED** — source evidence is insufficient to classify confidently.

Do not resolve those classes. Report them.

### 5. Produce the required report

Create `sidecar/reports/305_reasoning_vocabulary_inventory.md` containing:

1. starting commit SHA;
2. exact search terms/commands;
3. DSCT object-level vocabulary matrix;
4. name-versus-function matrix;
5. collision-class findings;
6. limited sibling lookups used, each with repository + commit/ref + path;
7. unanswered questions that require Jeremy + ChatGPT;
8. coverage/verification results.

## Write authority

This is a read-only archaeology prompt.

Allowed repository writes are limited to:

- `sidecar/reports/305_reasoning_vocabulary_inventory.md`;
- optional run evidence under a clearly named `sidecar/runs/305_*` path if the local Foreman convention requires it.

Do **not** edit planning, assignments, rubrics, grading, source lessons, the raw quarry, or sibling repositories.

## Hard stops

Do **not**:

- choose the final ontology;
- rename any current course object;
- decide whether Reasoning Quest and Reasoning Gate are the same thing;
- decide whether World Bible literally carries across courses;
- decide World Bible update cadence;
- merge or split grading categories;
- decide whether peer feedback is separately graded;
- invent assignments or reflection questions;
- alter Canvas/Savnac;
- turn a low-confidence inference into course doctrine.

## Verification battery

### A. Search coverage

Repeat the vocabulary searches after the report is drafted and verify that every meaningful current/historical term discovered is represented in the object-level inventory or explicitly marked irrelevant with a reason.

### B. Surface coverage

Explicitly state whether each of these source families was inspected and what was found:

- `planning/`
- `docs/`
- `assignments/`
- `rubrics/` if present
- student-facing course content directories if present
- `sidecar/reports/` and `sidecar/raw/` for historical/provenance context

If a directory does not exist, say so rather than silently skipping it.

### C. Write-scope audit

Run:

- `git diff --check`
- `git diff --name-only`

The changed-file list must contain only the required report and optional Prompt-305 run evidence. Any course-source modification is a failure of scope.

### D. Evidence quality audit

For every **MEDIUM** or **LOW** confidence interpretation, provide at least one representative source path and explain the ambiguity. Do not hide uncertainty in prose.

## Definition of done

Prompt 305 is complete only when:

1. the search set and inspected source families are documented;
2. every meaningful DSCT vocabulary/object family discovered has a disposition in the inventory;
3. names are separated from their apparent functions;
4. aliases, overloads, duplicate-homework risks, stale legacy, and grading seams are explicitly surfaced;
5. no final ontology decision has been made;
6. no course source was modified;
7. another reader can use the report to make the ontology decision without repeating basic DSCT repository archaeology.

If the evidence is genuinely insufficient, return **UNRESOLVED** with source citations/paths rather than guessing.