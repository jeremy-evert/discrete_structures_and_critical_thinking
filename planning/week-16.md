# Week 16 — Farkle + Machine Learning reasoning synthesis

**Tuesday, December 1 and Thursday, December 3, 2026**  
COMSC-2043-1420 · 12:30–1:45 PM · Gen. Thomas P. Stafford Center, Room 259

## Status

**GREEN — student/instructor package authored and validated against the canonical shared Farkle + ML core on a real Windows checkout.**

## Central question

> **When a Farkle strategy appears better, what are we actually justified in believing?**

Week 16 is a synthesis experience, not a new formal DSCT topic and not a second final project.

The computational machine comes from:

`jeremy-evert/Farkle_and_Machine_Learning`

DSCT owns the interpretation of its evidence.

## Semester payoff

This week deliberately brings back the strongest prior reasoning habits:

- define the claim before arguing about it;
- expose rules and assumptions;
- check the algorithm/experiment before trusting its output;
- reason about random samples and expectation;
- inspect denominators rather than only percentages;
- notice that different ordering criteria can produce different `best` strategies;
- name what the model/state leaves out;
- challenge a polished AI/human interpretation with evidence.

## Tuesday — Make a claim, then try to break it

Students:

1. inspect the fixed classroom Farkle rules and shared comparison contract;
2. define what `better` means for one strategy comparison;
3. declare a decision criterion/threshold;
4. predict the result;
5. run or inspect one bounded sample;
6. preserve raw counts/denominators;
7. identify one way the first result could mislead;
8. leave a short Reasoning Odyssey trace.

## Thursday — Defend, revise, or refuse

Students:

1. run or inspect a named repeated deterministic seed bundle;
2. compare results across samples;
3. inspect descriptive stability/spread;
4. consider one alternate metric or ordering criterion;
5. identify one model limitation;
6. critique one confident interpretation from a peer, instructor, or AI;
7. apply the declared decision rule;
8. defend, revise, or refuse the original conclusion.

A supported refusal to declare a winner is a valid reasoning outcome.

## Student path

Week-at-a-Glance:

- `week-16/README.md`

Lab:

- `week-16/student/farkle-evidence-lab.md`

Evidence receipt:

- `assignments/week-16-farkle-evidence-receipt.md`

Course-facing evidence runner:

- `lessons/week-16-farkle-evidence.py`

Instructor guide:

- `week-16/instructor/guide.md`

Validated classroom fallback:

- `week-16/fallback/quick_v1_results.csv`

## Grading placement

This work belongs to the existing **Weekly reinforcement / Reasoning Odyssey gate** category.

No new grading percentage, checkpoint, final project, or comprehensive exam is created here.

The evidence receipt uses the existing course method:

**Sources -> Rules/Assumptions -> Work -> Check Your Answer -> One-Sentence Summary**

## Required path

- ordinary CPU;
- free/open local Python path;
- no paid AI/API;
- no GPU/cloud/NRP requirement;
- no new ML algorithm implementation;
- no formal hypothesis-test requirement;
- no large new programming task.

AI critique may use a live zero-cost tool when available or an instructor-provided example when it is not.

## Validation evidence

The canonical shared core was validated on Windows and retained its real receipt in the shared repository.

DSCT then consumed the generated, provenance-pinned package in:

`lessons/vendor/farkle_ml/`

The DSCT seam validator completed **GREEN** and retained:

`sidecar/runs/week16_farkle_validation_20260816T211906Z.md`

The validated consumer proved that:

- shared provenance is present;
- the course-facing runner executes against the generated shared package;
- raw starts/wins/ties/turns/Farkles survive into the evidence surface;
- repeated seed rows survive into the evidence table;
- the required path needs no GPU, cloud, or paid service.

The curated fallback CSV is real observed evidence from that validated run, not fabricated sample output.

Do not hand-edit generated shared source in the DSCT repository. Refresh it only through the canonical synchronization script and validate again after a shared-source change.
