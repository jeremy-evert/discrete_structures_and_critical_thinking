# Prompt 304 — Reconcile Pair Reasoning as the DSCT pair-activity name

**Status:** FOREMAN-READY MECHANICAL CUT FROM THE DESIGN QUARRY  
**Source quarry:** `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md`  
**Scope:** DSCT repository only

## Why this is Foreman-ready

The pedagogical naming decision is already made. This prompt does **not** ask the worker to decide what pair work means.

The standard name for the recurring pair activity in DSCT is:

> **Pair Reasoning**

Drop **Pair Programming** as the conceptual name for this course.

A pair activity may still include programming, a checker, a simulator, a proof assistant, a graph builder, a truth-table evaluator, a recurrence explorer, or another computational artifact. The code is an instrument. The work is reasoning.

The motivation is already settled:

> It is no longer sufficient to write a program. We need reasoning. As steel sharpens steel, one reasoner sharpens another.

Current DSCT source still says `Pair Programming` in places including:

- `planning/fall-2026-weekly-architecture.md`
- `planning/fall-2026-topic-map.md`
- `docs/grading-model.md`

The raw design dump explicitly says this naming should later be reconciled coherently across planning, grading, rubrics, assignments, Course Foundry expectations, and Savnac objects.

Because the name is decided, locating and reconciling stale naming is mechanical source maintenance.

## Work

1. Search the DSCT repository for current/student-facing uses of:
   - `Pair Programming`
   - `Pair Programming report`
   - `paired-programming`
   - obvious A3-equivalent labels that refer to the DSCT pair activity.
2. Classify each hit as:
   - current doctrine/student-facing and should become **Pair Reasoning**;
   - historical/provenance and should remain unchanged;
   - ambiguous and should be reported rather than silently edited.
3. Reconcile only the unambiguous current-doctrine/student-facing names.
4. Preserve technical references to programming when programming is actually the activity/tool. Do not rewrite sentences merely because the word `programming` appears.
5. Update cross-references only where necessary to keep paths/labels coherent.
6. Produce a sidecar report listing:
   - files changed;
   - historical/provenance hits deliberately preserved;
   - ambiguous hits returned for review;
   - exact search terms used;
   - validation performed.

## Hard stops

Do **not**:

- redesign the Pair Reasoning activity;
- invent its final reflection questions;
- change grading weights or point values;
- decide whether peer feedback is separate or embedded;
- change the Week 4–14 Pair/Show cadence;
- rename Reasoning Odyssey, World Bible, or Show & Tell;
- change Savnac/Canvas live systems.

If a naming change would force one of those decisions, stop at that seam and report it.

## Acceptance

This prompt is complete when current DSCT doctrine consistently uses **Pair Reasoning** for the recurring pair activity, historical evidence is preserved, and every unresolved semantic seam is explicitly reported instead of guessed.