# DSCT Week 16 Farkle + Machine Learning — current-state report

**Date:** 2026-08-16  
**Status:** COURSE CONTRACT EXISTS; WEEK 16 NOT YET AUTHORED; SHARED CORE IMPLEMENTED WITH RUNTIME YELLOW  
**DSCT source inspected at:** `7c4b8cbeaa60803ae4d8ca9d65c7e6f4d1052925`  
**Shared Farkle source currently targeted:** `jeremy-evert/Farkle_and_Machine_Learning` at or after `3be3cc120cebb4d2a43c12dcf7e3b51bca490c99`

## Executive finding

DSCT does not need a translated CS1/CS2 Week 16.

It needs the first **native clean consumer** of the shared Farkle machine.

The authoritative semester spine already reserves Week 16 for **Farkle + Machine Learning synthesis**, and the DSCT course contracts make the disciplinary purpose unusually clear: students should use prior work in claims, algorithms, counting, probability, simulation, decision structures, finite-state models, evidence, and model limits to decide what a computational result actually justifies saying.

The central Week 16 question is therefore:

> **When a Farkle strategy appears better, what are we actually justified in believing?**

The shared repository should provide the computational machine and raw evidence. DSCT should own the argument about what that evidence means.

---

# What DSCT already has

## Authoritative 17-week spine

Current source:

`planning/fall-2026-spine.md`

Week 16 is contracted for Dec. 1 / Dec. 3 as:

**Farkle + Machine Learning synthesis experience**

The spine explicitly says Week 16 depends on prior probability, simulation, state, algorithm, evidence, and model-limit work.

## Course design stance

Current source:

`planning/fall-2026-course-design.md`

DSCT is a reasoning bridge. Students use precise language, definitions, proofs/counterexamples, discrete representations, small programs/simulations, and checks to make defensible claims.

The course is not a textbook march and has no required commercial text for Fall 2026.

## Weekly reasoning method

Current reusable assignment:

`assignments/weekly-problem-solving-writeup.md`

Required reasoning headings:

1. **Sources**
2. **Rules/Assumptions**
3. **Work**
4. **Check Your Answer**
5. **One-Sentence Summary**

Week 1 reinforces the same sequence and the stance:

> **Love AI more. Trust AI less.**

## Grading contract

Current source:

`docs/grading-model.md`

Week 16 Farkle + ML is already part of:

**Weekly reinforcement / Reasoning Odyssey gate — 30% semester category**

It is not a new final-project bucket.

The current grading model explicitly says Week 16 is recurring work inside the weekly gate, not a comprehensive exam or new project category.

Exact due-date/deployment mechanics remain outside this authoring pass.

---

# Prior DSCT ideas Week 16 can legitimately synthesize

The current topic map contracts the following sequence before Week 16.

## Logic, claims, proof

Useful Week 16 transfer:

- define what `better` actually means;
- distinguish a numerical observation from the conclusion someone claims follows;
- name assumptions;
- look for a counterexample to an overclaim.

## Algorithms and correctness

Useful Week 16 transfer:

- the simulator is evidence only if it implements the stated rules;
- edge cases and fairness matter;
- a reproducible wrong program is still wrong.

## Counting and combinatorial reasoning

Useful Week 16 transfer:

- what outcomes/cases are represented;
- whether cases are counted consistently;
- why overlapping/omitted cases matter when describing possibilities.

## Probability, uncertainty, and evidence

This is the strongest direct precursor.

Useful Week 16 transfer:

- sample space;
- conditional reasoning;
- independence assumptions;
- expectation;
- base rates;
- simulation as an estimate rather than proof;
- gambler's-fallacy-style mistakes;
- sampling variability.

## Relations/order criteria

Useful Week 16 transfer:

- `best` depends on an ordering relation/criterion;
- win rate, expected score, simplicity, and cost may produce different orderings;
- one strategy need not dominate another under every criterion.

## Trees / decision structures

Useful Week 16 transfer:

- strategies encode decisions from state;
- more possible future branches can make a decision method more expensive without making it universally better.

## Boolean checking habit

Useful Week 16 transfer:

- find the assignment/edge case that breaks an overbroad claim;
- distinguish `worked for these trials` from `true under every possible case`.

## Finite-state models and model limits

This is the second strongest direct precursor.

Useful Week 16 transfer:

- which state variables are visible to a strategy/learner;
- which potentially relevant state is omitted;
- what the model cannot establish even after many simulated games.

---

# Shared Farkle package status

The new canonical shared repository now contains connector-authored:

- classroom rules/engine;
- strategy contract;
- human threshold/state-aware strategies;
- transparent experience-table learner;
- bounded one-step rollout strategy;
- fair repeated-game simulator;
- raw + derived evidence receipts;
- named deterministic seed bundles;
- shared tests;
- one-command validator;
- provenance-pinned consumer synchronization script.

Important DSCT-driven improvement already landed in shared source:

**raw wins/ties/Farkles/turns/starts are retained alongside rates.**

That means DSCT can inspect denominators and construct evidence tables without scraping terminal prose.

## Shared runtime yellow

The shared package was authored through the connected GitHub interface. It has not yet been executed from Jeremy's real private checkout.

Required shared validation command:

```text
python scripts/validate.py
```

Required consumer synchronization pattern:

```text
python scripts/sync_consumer.py <course-destination> --apply
python scripts/sync_consumer.py <course-destination> --check
```

Until those run successfully, DSCT implementation may be authored against the shared contract but cannot be classified fully GREEN.

---

# What DSCT Week 16 is missing today

No polished Week 16 course package currently exists.

Missing student/instructor surface includes:

- Week 16 planning page;
- Week-at-a-Glance / student lesson;
- instructor guide;
- DSCT evidence/Reasoning Odyssey receipt;
- evidence criteria/rubric guidance;
- course-facing shared-package runner/wrapper;
- fallback evidence generated from validated shared fixtures;
- raw validation receipt;
- postmortem.

There is no existing DSCT Farkle engine to preserve or migrate.

That is an advantage.

---

# Recommended student burden

Week 16 should remain synthesis and application, not a new technical unit.

Students should **not** be required to:

- implement Farkle;
- write a new ML algorithm;
- learn formal hypothesis testing;
- build a dashboard;
- configure GPU/cloud/NRP;
- create tournament infrastructure;
- write a large new program.

A humane Week 16 asks students to:

1. understand the shared comparison enough to audit it;
2. define a claim and decision criterion;
3. make a prediction;
4. inspect one initial result;
5. identify how it might mislead;
6. inspect several deterministic samples;
7. compare stability and one alternate metric;
8. name a model limitation;
9. defend, revise, or refuse the conclusion.

---

# Current yellows

## YELLOW A — shared package runtime

Shared tests/validator not yet executed on real checkout.

## YELLOW B — shared -> DSCT synchronization

The synchronization script exists but has not yet performed its first real apply/check cycle.

## YELLOW C — deterministic fallback evidence

Do not fabricate sample win-rate numbers. Generate fallback evidence from the validated shared package after the first real run.

## YELLOW D — Weeks 9/14 may still be contracted rather than authored

Week 16 may synthesize their contracted concepts because the semester spine says it should, but student-facing cross-references must not point to nonexistent lessons. Resolve links against whatever has actually landed by deployment time.

---

# Recommendation

Proceed with DSCT authoring now.

The course contract and shared computational contract are clear enough to create:

1. Week 16 target map;
2. Week 16 implementation plan;
3. student lesson;
4. instructor guide;
5. evidence receipt/rubric criteria;
6. thin DSCT evidence runner that consumes the generated shared vendor package;
7. validation wrapper that checks the DSCT-specific evidence shape without duplicating the shared validator.

Do not call the week fully GREEN until the shared package and DSCT consumer have both been executed on a real checkout.
