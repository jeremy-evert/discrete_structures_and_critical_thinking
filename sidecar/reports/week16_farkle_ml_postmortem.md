# Postmortem — DSCT Week 16 Farkle + Machine Learning

**Date:** 2026-08-16  
**Status:** AUTHORED AND WIRED FOR SHARED CONSUMPTION; REAL-CHECKOUT VALIDATION YELLOW

## What we set out to do

DSCT had a contracted Week 16 identity but no authored Week 16 package.

At the same time, Farkle + ML had become the only shared computing-family week without its own canonical computational repository.

Rather than build another course-local copy, this campaign used DSCT as the first clean consumer of the newly consolidated:

`jeremy-evert/Farkle_and_Machine_Learning`

The two goals reinforced each other:

1. make the shared package general enough to serve a genuinely different course;
2. make DSCT Week 16 as complete as the stronger sibling-course weeks without inheriting their pedagogical lens by copy/paste.

---

# Development workflow used

The campaign followed:

> **report -> map -> plan -> implementation/work orders -> raw receipts -> postmortem**

and the operating rule:

> **Ask once: leave breadcrumbs. Ask twice: script it. Ask three times: automate it.**

The third-consumer pattern was applied in the shared repository: validation and consumer synchronization are now centralized scripts rather than another manual sequence.

---

# What DSCT contributed back to the shared machine

The most important DSCT requirement was simple:

> A percentage is not enough evidence if the student cannot inspect the denominator that produced it.

That requirement caused the canonical shared simulation/result surface to retain:

- raw wins A/B;
- ties;
- raw starts A/B;
- raw turns A/B;
- raw Farkles A/B;
- derived rates alongside those counts.

DSCT also caused repeated deterministic seed bundles to become a first-class shared helper so students can inspect multiple samples without each course inventing its own loop.

The helper deliberately stays descriptive. It does not smuggle a new statistics course into Week 16.

---

# How DSCT differs from the sibling courses

## CS1

CS1's Week 16 asks students to understand how precise rules, functions, randomness, and a transparent learner produce program behavior.

DSCT does not ask students to rebuild or deeply read the game code.

## CS2

CS2 asks whether added software complexity/experiment machinery earns its keep while preserving contracts.

DSCT uses the resulting contract/evidence but does not make software architecture the central judgment.

## Computer Architecture

Architecture asks what additional computation/hardware cost buys and whether that cost is worth paying.

DSCT may notice cost as an alternate ordering criterion, but its central problem is what the evidence justifies claiming.

## DSCT

DSCT's central question is:

> **When a Farkle strategy appears better, what are we actually justified in believing?**

Its successful final outputs are not restricted to naming a winner.

Students may:

- defend a limited claim;
- revise an overbroad claim;
- refuse to declare a winner under their predeclared criterion.

That refusal is a feature, not an escape hatch.

---

# Prior DSCT ideas that actually resurfaced

The authored Week 16 uses:

- **logic/claims:** operationally define `better`;
- **algorithm/correctness:** inspect the fairness/rules contract before trusting output;
- **counting/probability:** preserve outcomes/denominators and reason about repeated random samples;
- **expectation/evidence:** compare observed outcomes without treating simulation as proof;
- **relations/order:** alternate metrics can change which strategy is preferred;
- **Boolean/counterexample habit:** search for a case/interpretation that breaks an overclaim;
- **finite-state/model limits:** identify which state the strategy/learner sees and what it omits;
- **AI Fluency:** audit fluent interpretation as a claim, not as evidence.

The Week 16 lab does not force every topic in the semester to make a cameo.

---

# Student package authored

## Planning / overview

- `planning/week-16.md`
- `week-16/README.md`

## Student work

- `week-16/student/farkle-evidence-lab.md`
- `assignments/week-16-farkle-evidence-receipt.md`

## Instructor support

- `week-16/instructor/guide.md`

## Course-facing technical wrapper

- `lessons/week-16-farkle-evidence.py`

## DSCT seam validation

- `scripts/validate_week16_farkle.py`

## Build trail

- `sidecar/reports/week16_farkle_ml_current_state.md`
- `planning/week-16-farkle-ml-target-map.md`
- `planning/week-16-farkle-ml-plan.md`
- `sidecar/runs/week16_farkle_ml_connector_receipt.md`

---

# Student burden

The required path is intentionally small.

Students do not write a new game or ML system.

They:

1. define a claim and criterion;
2. predict;
3. inspect/run one initial sample;
4. identify how it could mislead;
5. inspect a repeated seed bundle;
6. compare descriptive stability/spread;
7. inspect one alternate metric;
8. name one model limitation;
9. critique one confident interpretation;
10. defend, revise, or refuse the claim.

The required computational path is CPU-only and has no paid AI, GPU, cloud, or NRP dependency.

---

# Grading alignment

No new grading category was invented.

Week 16 remains part of the existing:

**Weekly reinforcement / Reasoning Odyssey gate**

The receipt uses the course's established:

**Sources -> Rules/Assumptions -> Work -> Check Your Answer -> One-Sentence Summary**

The numerical winner is not an evidence criterion.

---

# Integration mechanism

The intended Fall 2026 consumer path is a generated vendor snapshot synchronized from the canonical shared repository.

Canonical shared script:

```text
python scripts/sync_consumer.py ../discrete_structures_and_critical_thinking/lessons/vendor/farkle_ml --apply
```

The generated package records:

`_SHARED_PROVENANCE.json`

This preserves a self-contained course checkout without pretending DSCT owns an independent Farkle fork.

No generated vendor files were manually created during connector authoring.

---

# What we cannot truthfully claim yet

This environment can write the private GitHub repositories through the connector but cannot execute their current private checkouts.

Therefore this postmortem does **not** claim:

- shared unit-test pass count;
- observed shared validation runtime;
- actual strategy win rates;
- successful shared -> DSCT synchronization;
- DSCT seam-validator pass count;
- generated fallback evidence.

No plausible-looking sample evidence was fabricated.

---

# Named yellows

## YELLOW 1 — shared validator

Run from `Farkle_and_Machine_Learning`:

```text
python scripts/validate.py
```

## YELLOW 2 — first real consumer synchronization

From the shared checkout:

```text
python scripts/sync_consumer.py ../discrete_structures_and_critical_thinking/lessons/vendor/farkle_ml --apply
python scripts/sync_consumer.py ../discrete_structures_and_critical_thinking/lessons/vendor/farkle_ml --check
```

## YELLOW 3 — DSCT seam validation

From DSCT:

```text
python scripts/validate_week16_farkle.py
```

## YELLOW 4 — fallback fixture

After the above succeeds, preserve one validated `classroom_v1` evidence bundle for classroom fallback use and record the synchronized shared commit.

---

# What should happen after the yellows are green

Do **not** immediately continue reorganizing repositories for aesthetic reasons.

Once shared + DSCT are validated:

1. record the runtime receipts;
2. repair any defects found by real execution;
3. freeze the shared contract for the first Fall 2026 consumer;
4. then plan/migrate CS1 and CS2 away from accidental shared-code forks using the same sync/check mechanism;
5. let Computer Architecture consume the stable package when its Prompt 005 is deliberately executed.

The migration of existing working courses is a separate controlled step.

---

# Closure

DSCT Week 16 is no longer `CONTRACTED_NOT_AUTHORED` in substance.

It now has a complete reasoning-centered student/instructor surface and is wired to consume the canonical shared machine through a scripted, provenance-pinned mechanism.

Current classification:

> **AUTHORED AND WIRED; REAL-CHECKOUT VALIDATION YELLOW**

Promote to GREEN only after the shared validator, sync apply/check, and DSCT seam validator have produced real receipts.
