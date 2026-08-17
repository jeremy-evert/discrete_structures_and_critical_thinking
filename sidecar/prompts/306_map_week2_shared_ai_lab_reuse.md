# Prompt 306 — Map reusable Week 2 AI Lab material before DSCT authoring

**Status:** FOREMAN-READY ARCHAEOLOGY / REUSE MAP  
**Source quarry:** `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md`  
**Scope:** evidence gathering and ownership mapping; do not author final DSCT Week 2

## Why this is Foreman-ready

The Week 2 identity is already decided:

> **Building Your AI Lab**

The design quarry explicitly says Week 2 should not independently reinvent content that already exists in sibling/shared repositories.

First sources to bounce against:

- `jeremy-evert/local_ai_lab_setup`
- `jeremy-evert/windows_classroom`
- `jeremy-evert/computer_science_2` Week 2 integration material
- Computer Architecture Week 2 epistemic framing

CS2 already has a mature ownership contract in which shared repos own canonical instructional/runtime material and the course repo owns sequencing, purpose, and course-specific extension.

The reusable student evidence loop is approximately:

1. understand the system model;
2. `Check` readiness;
3. observe a known failing `Baseline`;
4. make one bounded Aider-assisted proposal;
5. inspect the `Diff`;
6. run an independent `Final` test;
7. read/reason;
8. accept or reject from evidence;
9. preserve a readiness/reflection receipt.

Architecture contributes the epistemic frame:

> How can AI help me investigate a machine without becoming my source of truth?

with a reusable structure of question/hypothesis, context, AI/tool used, observation, evidence artifact, conclusion, and revision after verification.

The mechanical job is to identify what already exists and what DSCT would actually need to add. The pedagogical choice of the final DSCT exercise remains with Jeremy + ChatGPT.

## Work

1. Inspect current `main` in the four source areas above.
2. Record exact repository, commit/ref, and path for reusable Week 2 material.
3. Build a comparison table with at least:
   - shared/canonical content;
   - Windows/runtime harness;
   - CS2 sequencing/course wrapper;
   - Architecture epistemic framing;
   - current DSCT Week 2 source/branches.
4. Classify candidate material as:
   - **REUSE DIRECTLY / POINTER**;
   - **ADAPT FOR DSCT**;
   - **COURSE-SPECIFIC, DO NOT COPY**;
   - **STALE / SUPERSEDED**;
   - **OPEN PEDAGOGICAL CHOICE**.
5. Explicitly inspect the known `Check -> Baseline -> bounded proposal -> Diff -> Final -> read/reason -> accept/reject` path and report whether current source still supports it.
6. Inspect any DSCT incoming Week 2 branch as archaeology only; do not blind-merge it.
7. Produce a DSCT sidecar report that tells a later author exactly what can be reused and what still needs Jeremy + ChatGPT design.

## Hard stops

Do **not**:

- choose the final DSCT bounded exercise;
- blindly copy CS2's `format_student_name` exercise;
- decide final Pair Reasoning prompts;
- write final student-facing Week 2 lessons;
- change grading weights;
- mutate shared repositories;
- write to Savnac/Canvas.

## Acceptance

Complete when a later DSCT Week 2 author can avoid duplication and knows the canonical ownership/provenance of every reusable piece, while all genuine pedagogy remains explicitly unresolved.