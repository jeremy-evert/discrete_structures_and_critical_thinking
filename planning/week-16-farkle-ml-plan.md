# DSCT Week 16 Farkle + ML implementation plan

**Date:** 2026-08-16  
**Status:** READY FOR AUTHORING  
**Inputs:** `sidecar/reports/week16_farkle_ml_current_state.md`, `planning/week-16-farkle-ml-target-map.md`

## Goal

Build a polished two-meeting Week 16 synthesis experience that consumes the canonical shared Farkle package and uses DSCT's existing Reasoning Odyssey method to decide what computational evidence actually supports.

The shared repository owns the machine.

This course owns the interpretation.

---

# Package shape

Author the following DSCT-owned surface:

```text
planning/week-16.md
week-16/
  README.md
  student/
    farkle-evidence-lab.md
  instructor/
    guide.md
assignments/
  week-16-farkle-evidence-receipt.md
lessons/
  week-16-farkle-evidence.py
sidecar/runs/
sidecar/reports/
```

Generated shared source should eventually land only in the dedicated path:

```text
lessons/vendor/farkle_ml/
```

through the shared repository's synchronization script. Do not hand-maintain that generated directory.

---

# Shared dependency contract

Canonical owner:

`jeremy-evert/Farkle_and_Machine_Learning`

Expected integration mechanism:

```text
python scripts/sync_consumer.py ../discrete_structures_and_critical_thinking/lessons/vendor/farkle_ml --apply
```

from a local clone of the shared repository.

The generated destination must contain:

`_SHARED_PROVENANCE.json`

The DSCT runner should read/report that provenance when practical.

## Runtime yellow

Do not create generated vendor files manually through the connector merely to make the tree look complete.

The synchronization script itself is what must prove the generated-copy workflow on Jeremy's real checkout.

Until then, student/instructor authored assets may land while code execution remains YELLOW.

---

# Student flow

## Tuesday — Make a claim, then try to break it

Target cognitive load:

- understand enough Farkle to interpret the experiment;
- define `better`;
- make a prediction;
- inspect assumptions and raw denominators;
- run/read one initial sample;
- identify one way the result could mislead;
- leave one bounded reasoning trace.

Use the course's five headings:

**Sources -> Rules/Assumptions -> Work -> Check Your Answer -> One-Sentence Summary**

Do not front-load a statistics lecture.

## Thursday — Defend, revise, or refuse

Students inspect/run a named repeated seed bundle.

They:

- preserve per-seed raw evidence;
- compare A-B win-rate difference across samples;
- inspect descriptive spread/range;
- consider one alternate metric or ordering criterion;
- name one model limitation;
- apply a declared decision threshold;
- exchange critique;
- defend, revise, or refuse the conclusion.

The point is a defensible limited claim, not finding the tournament champion.

---

# Course-facing runner

Create:

`lessons/week-16-farkle-evidence.py`

It should be thin.

Responsibilities:

- find/import `lessons/vendor/farkle_ml` through the course checkout;
- fail with a useful message if shared synchronization has not happened;
- run one initial experiment or a named seed bundle;
- save a DSCT-facing CSV/JSON evidence set under a bounded output directory supplied/defaulted by the script;
- print a readable evidence table containing raw counts and percentage-point difference;
- optionally save a simple plot if matplotlib is already available;
- report shared provenance from `_SHARED_PROVENANCE.json`;
- install nothing.

Do not duplicate engine, learner, simulation, or generic validation logic.

Potential modes:

```text
python lessons/week-16-farkle-evidence.py initial
python lessons/week-16-farkle-evidence.py bundle
```

Default matchup may use:

```text
learner:500 vs bank_at_425
```

but the final default should remain instructor-adjustable without code surgery.

---

# Evidence receipt

Create:

`assignments/week-16-farkle-evidence-receipt.md`

It should be short enough to complete during the week.

Required fields:

## Sources

- shared benchmark/package provenance;
- any course source/help used;
- AI source if used.

## Rules / Assumptions

- exact claim;
- definition of `better`;
- sample/bundle;
- decision threshold;
- important comparison/model assumption.

## Work

- prediction;
- compact evidence table or attached generated artifact;
- what changed across samples;
- one alternate metric if used.

## Check Your Answer

- one way the evidence could mislead;
- one counterargument/critique;
- one model limitation;
- how the student checked or revised the claim.

## One-Sentence Summary

The final limited conclusion.

Allow `I refuse to declare a winner under my stated rule` as a valid evidence-backed conclusion.

---

# Instructor guide

Create:

`week-16/instructor/guide.md`

Include:

- prerequisite shared validation/sync check;
- 75-minute Tuesday run-of-show;
- 75-minute Thursday run-of-show;
- discussion traps;
- useful wrong claims;
- AI-audit options;
- how to handle a live execution failure using validated fallback evidence;
- what is and is not being assessed;
- reminder not to reward the strategy that happens to win as the learning outcome.

## Useful wrong claims

Seed discussion with claims such as:

- `A won this run, therefore A is better.`
- `10,000 simulations prove A is optimal.`
- `The same seed reproduced, therefore the conclusion is reliable.`
- `A is 0.4 percentage points ahead, so the difference matters.`
- `The learner used machine learning, so it should beat a simple rule.`
- `The largest number is the best decision.`

Students should attack the reasoning, not merely label the statement false.

---

# Week-at-a-Glance

Create:

`week-16/README.md`

It should state:

- dates Dec. 1/3;
- synthesis identity;
- central question;
- Tuesday/Thursday path;
- required student artifacts;
- zero-cost/CPU-only path;
- no new formal DSCT topic;
- no new final project.

`planning/week-16.md` should be the compact operational planning source that points at these artifacts.

---

# Evidence criteria

Per Prompt 315 (2026-08-17, Jeremy+ChatGPT), Week 16 now has its own
**Farkle + Machine Learning Synthesis** category (5%), funded by the Prompt
312 retirement of the separate Friday-feedback/A7 5% category rather than by
inventing new points or taking weight from another category. Week 16 is no
longer inside the weekly Decision Gate (Reasoning Odyssey gate) category and
is not one of the three Reasoning Odyssey Checkpoints. See
`docs/grading-model.md` for the full arithmetic.

The evidence criteria should reward whether the student:

1. states a precise limited claim/criterion;
2. exposes assumptions and raw evidence;
3. checks stability/alternative interpretation;
4. identifies a model limitation;
5. revises/defends/refuses the conclusion based on evidence;
6. leaves a reproducible reasoning trail.

Do not grade which strategy won.

A small criteria section may live inside the receipt rather than creating a second independent rubric file unless the course's current Canvas/Savnac authoring requires one later.

---

# Fallback evidence

After the shared package validator runs successfully on a real checkout:

- retain its canonical seed-bundle CSV/JSON;
- copy or reference a **validated** DSCT classroom fixture generated from that exact shared commit;
- record provenance;
- use it if classroom live execution fails.

Do not fabricate fallback win-rate values during connector-only authoring.

---

# DSCT validation

Create a small course-specific validator only for course seams if needed, e.g.:

`scripts/validate_week16_farkle.py`

It must **not** reimplement the shared tests.

It should check:

- vendor provenance file exists;
- expected shared import succeeds;
- initial/bundle runner produces DSCT evidence artifacts;
- raw columns survive;
- student/instructor links exist;
- receipt headings match course reasoning method;
- no required paid/GPU/cloud dependency.

If this validation sequence repeats elsewhere, it belongs back in shared automation.

---

# Raw receipts and postmortem

During build write:

`sidecar/runs/week16_farkle_ml_connector_receipt.md`

After real execution write timestamped runtime receipts.

Final postmortem:

`sidecar/reports/week16_farkle_ml_postmortem.md`

It should state:

- shared commit consumed;
- DSCT artifacts authored;
- prior concepts that actually resurfaced;
- student burden;
- runtime evidence;
- whether DSCT forced shared-schema changes;
- named yellows;
- final commit(s).

---

# Immediate authoring order

Proceed now with authored course content that does not require fabricated runtime results:

1. `planning/week-16.md`;
2. `week-16/README.md`;
3. student lab;
4. evidence receipt;
5. instructor guide;
6. thin evidence runner;
7. DSCT seam validator;
8. connector receipt/postmortem status.

Leave generated vendor source and validated fallback numbers for the real-checkout sync/validation step.
