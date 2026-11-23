# Postmortem — DSCT Week 16 Farkle + Machine Learning

**Date:** 2026-08-16  
**Status:** GREEN — AUTHORED, SYNCHRONIZED, AND VALIDATED AGAINST CANONICAL SHARED CORE

## What we set out to do

DSCT had a contracted Week 16 identity but no authored Week 16 package. At the same time, Farkle + ML was the common computing-family week without its own canonical computational repository.

Rather than build another course-local fork, this campaign used DSCT as the first clean consumer of:

`jeremy-evert/Farkle_and_Machine_Learning`

The goals reinforced each other:

1. make the shared package general enough to serve a genuinely different course;
2. make DSCT Week 16 as complete as the stronger sibling-course weeks without copying their pedagogical lens.

## Development workflow used

The campaign followed:

> **report -> map -> plan -> implementation/work orders -> raw receipts -> postmortem**

and:

> **Ask once: leave breadcrumbs. Ask twice: script it. Ask three times: automate it.**

Because DSCT became the third serious consumer pattern, shared validation and synchronization were promoted into canonical scripts rather than another manual sequence.

## What DSCT contributed back to the shared machine

The key DSCT requirement was:

> A percentage is not enough evidence if the student cannot inspect the denominator that produced it.

That caused the shared result contract to preserve:

- raw wins A/B;
- ties;
- starts A/B;
- turns A/B;
- Farkles A/B;
- derived rates alongside those counts.

DSCT also caused repeated deterministic seed bundles to become first-class shared evidence, while deliberately stopping short of turning Week 16 into a new statistics course.

## DSCT's course-specific question

> **When a Farkle strategy appears better, what are we actually justified in believing?**

Students may defend a limited claim, revise an overbroad claim, or refuse to declare a winner under their predeclared criterion. A supported refusal is a valid reasoning outcome.

The authored week resurfaces the strongest prior DSCT ideas:

- logic/claims: define `better` operationally;
- algorithms/correctness: inspect fairness and rules before trusting output;
- counting/probability: preserve outcomes and denominators across random samples;
- expectation/evidence: interpret simulation without treating it as proof;
- relations/order: alternate criteria can reverse which strategy is preferred;
- counterexample habits: look for evidence that breaks an overclaim;
- finite-state/model limits: identify state the model sees and omits;
- AI Fluency: treat fluent interpretation as a claim, never as evidence.

## Student/instructor package

- `planning/week-16.md`
- `week-16/README.md`
- `week-16/student/farkle-evidence-lab.md`
- `assignments/week-16-farkle-evidence-receipt.md`
- `week-16/instructor/guide.md`
- `lessons/week-16-farkle-evidence.py`
- `scripts/validate_week16_farkle.py`
- `week-16/fallback/quick_v1_results.csv`

The required student path remains CPU-only and requires no GPU, cloud, NRP, paid AI, or large new programming task.

## Grading alignment

No new grading category was invented.

Week 16 remains inside the existing **Weekly reinforcement / Reasoning Odyssey gate** and uses:

**Sources -> Rules/Assumptions -> Work -> Check Your Answer -> One-Sentence Summary**

The numerical winner is not itself an evidence criterion.

## Canonical consumer mechanism

The course consumes a generated vendor snapshot under:

`lessons/vendor/farkle_ml/`

`_SHARED_PROVENANCE.json` records the shared source repository, source commit, source hashes, and synchronization audit context.

Validated shared source commit:

`d3a1ed379a652731b0b6237c33b4fe42c518ac9e`

The course-local generated snapshot is not independent source truth and should not be hand-edited.

## Real validation evidence

Shared core validation was completed first on a real Windows checkout.

DSCT validation receipt:

`sidecar/runs/week16_farkle_validation_20260816T211906Z.md`

Status: **GREEN**.

It proved:

- shared provenance exists in the consumer;
- the DSCT course-facing runner executes against the synchronized package;
- raw starts/wins/ties/turns/Farkles survive into the evidence surface;
- the repeated `quick_v1` bundle preserved multiple per-seed rows;
- the required path completed without GPU, cloud, or paid-service dependency.

A real observed `quick_v1` result set was retained at:

`week-16/fallback/quick_v1_results.csv`

That fallback is actual validated evidence, not invented sample output. In the three 10-game fallback rows, the learner-vs-threshold A-B win-rate difference moved from -40 to +20 to +60 percentage points, which is particularly useful for the DSCT discussion of sample stability and overclaiming.

Validated consumer commit:

`bab5ef89fa08e73b88bcdabd736600b58c45ec13`

## What real execution taught us

The first synchronization attempt targeted a path where the DSCT repository had not actually been cloned. The original sync tool created a convincing vendor-only directory. That exposed a trust bug in the automation.

The shared synchronization tool was then hardened to require an existing Git worktree before writing. Provenance was also improved so consumers pin to the last commit that actually changed `src/farkle_ml/`, rather than becoming artificially stale after README or housekeeping changes.

That is exactly the desired escalation rule working: repeated work became a script, and the script remembered the failure after the humans stopped thinking about it.

## Remaining work outside DSCT

No DSCT Week 16 release yellow remains.

Do **not** continue reorganizing this course merely because further shared cleanup is imaginable.

CS1 and CS2 legacy/local Farkle ownership can be migrated later using the proven shared sync/check pattern, and Computer Architecture can consume the shared package when its Week 16 build is deliberately executed. Those are separate controlled campaigns.

## Closure

DSCT Week 16 is now a complete, validated reasoning-centered synthesis experience and the first proven clean consumer of the canonical shared Farkle + Machine Learning computational core.

Current classification:

> **GREEN — DEFEND, REVISE, OR REFUSE.**

Then stop.
