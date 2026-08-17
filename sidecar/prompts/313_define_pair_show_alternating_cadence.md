# Prompt 313 — Define the DSCT Pair Reasoning / Show & Tell alternating cadence

**Status:** FOREMAN-READY DECISION IMPLEMENTATION  
**Source decision:** Jeremy + ChatGPT discussion, 2026-08-17  
**Source quarry:** `sidecar/raw/2026-08-17_dsct_design_decision_pile.md`  
**Scope:** DSCT repository only  
**Required report:** `sidecar/reports/313_pair_show_alternating_cadence.md`

## Decision now settled

DSCT has six recurring event families across the semester:

1. AI Fluency
2. Professional Minds strand 1
3. Professional Minds strand 2
4. Pair Reasoning
5. Show & Tell
6. the weekly Decision / Reasoning Odyssey gate

This does **not** mean all six fire every instructional week.

For the recurring social-reasoning mode, a normal formal-content week uses:

> **Pair Reasoning OR Show & Tell, not both.**

Pair Reasoning and Show & Tell should follow a **predictable alternating cadence** across the formal-content sequence.

The first formal DSCT core week should use **Pair Reasoning**, followed by Show & Tell, then Pair Reasoning, then Show & Tell, continuing in alternation unless an explicit calendar or special-week exception intervenes.

The current Fall 2026 runway is:

- Week 1: compressed Semester Kickoff Week
- Week 2: Building Your AI Lab
- Week 3: Containers + minimum-useful LaTeX
- Weeks 4–14: eleven formal DSCT core weeks
- Week 15: asynchronous travel/Thanksgiving buffer
- Week 16: existing GREEN Farkle + Machine Learning synthesis
- Week 17: final reflection/closeout

Therefore, the **baseline** formal-week social cadence begins at Week 4 with Pair Reasoning.

## Why this decision exists

Pair Reasoning and Show & Tell exercise different reasoning muscles:

- **Pair Reasoning** is the smaller/private challenge mode: another reasoner gets inside the student's reasoning and tests it.
- **Show & Tell** is the public explanation/defense mode: the student makes reasoning inspectable and responds to professional critique.

Both matter, but a Tuesday/Thursday course cannot sustain both as full recurring events every week without creating unnecessary workload and crowding out the mathematics.

The cadence should be learnable and predictable rather than redesigned every week.

## Contract to implement

### 1. One social-reasoning mode per normal formal week

Current operational source should make clear that a normal Week 4–14 formal-content week has exactly one primary recurring social-reasoning mode:

- Pair Reasoning; or
- Show & Tell.

Do not schedule both as separate required recurring graded events in the same normal formal-content week.

This does not prohibit ordinary discussion, peer questions, brief partner checks, or classroom interaction inside other lessons. The rule concerns the named graded recurring event family.

### 2. Predictable alternation

The baseline alternation is:

- first formal core week: **Pair Reasoning**;
- next formal core week: **Show & Tell**;
- then Pair Reasoning;
- then Show & Tell;
- continue the alternating pattern.

Where the final Week 4–14 topic spine is still unresolved, implement the **cadence contract without inventing the final topic mapping**.

### 3. Calendar and special-week exceptions

Calendar reality may interrupt the baseline cadence.

Known examples include institutional breaks, a missing Thursday meeting, runway weeks, Week 15 async travel, Week 16 synthesis, or another explicitly designed special week.

Do not force a social event into a nonexistent class meeting merely to preserve parity.

When an exception exists:

- identify it explicitly;
- preserve the baseline alternation as the default architecture;
- do not silently invent a make-up assignment, extra asynchronous report, or grading penalty;
- do not shift or re-balance later weeks unless current authoritative source already settles that behavior or an explicit course-design decision authorizes it.

If the exact exception treatment is unresolved, report the seam rather than deciding it.

### 4. Relationship to Prompts 311 and 312

Prompt 311 defines the **Pair Reasoning contract**.

Prompt 312 defines the **Show & Tell contract**.

Prompt 313 defines **when those event families fire relative to each other**.

Do not reopen or redesign the semantic contracts from 311/312 here. Consume them if completed; otherwise preserve compatibility and limit this prompt to cadence.

### 5. Grading boundary

This cadence decision does not change the semester category weights.

Preserve:

- Pair Reasoning as its settled 5% semester category;
- Show & Tell as its settled 5% semester category.

Do not redistribute grading weight, repair the broader grading arithmetic, or infer that each category must have the same number of weekly objects.

A semester category can contain only the events scheduled for that event family.

## Source work authorized

Inspect and reconcile current DSCT surfaces that define the weekly social mode or rotation, including at minimum:

- `planning/fall-2026-weekly-architecture.md`
- `planning/fall-2026-topic-map.md`
- `docs/grading-model.md`
- relevant course-design/schedule source that explicitly names Pair Reasoning / Show & Tell cadence
- completed Prompt 311 / 312 reports if available

Update only what is necessary to make the cadence contract coherent.

Do not freeze unresolved Week 4–14 technical topics merely to assign social modes.

## Hard stops

Do **not**:

- make Pair Reasoning and Show & Tell both required recurring events in a normal formal week;
- change either category's 5% weight;
- repair the overall grading-model arithmetic;
- choose the final eleven Week 4–14 technical topics;
- invent the exact treatment of a calendar exception when current doctrine does not settle it;
- change Week 16's GREEN synthesis contract;
- write to Canvas or Savnac;
- redesign AI Fluency or Professional Minds;
- redesign the Pair Reasoning or Show & Tell semantic contracts owned by Prompts 311 and 312.

## Verification battery

### A. One-mode-per-week audit

For every currently operational formal Week 4–14 row/surface that names a recurring social mode, verify that the source promises at most one named recurring mode for that normal week:

- Pair Reasoning; or
- Show & Tell.

No normal week may require both.

### B. Alternation audit

Verify that the baseline formal-core cadence starts with Pair Reasoning and alternates predictably thereafter, subject only to explicit exception markers.

Where the current topic map is stale against the new Week 4–14 eleven-week spine, distinguish:

- cadence truth that can be repaired now;
- unresolved topic placement that must remain open.

### C. Exception audit

Identify every Fall 2026 week in the current source where calendar/special-week structure prevents ordinary cadence.

For each, record whether the treatment is:

- already decided;
- safe mechanical reconciliation;
- or blocked by a design decision.

Do not invent missing policy.

### D. Category-boundary audit

Verify:

- Pair Reasoning remains 5%;
- Show & Tell remains 5%;
- no new grade category is created;
- no ordinary formal week accidentally creates both graded social-event objects;
- the number of events in the two categories is allowed to differ because of the odd eleven-week core and calendar exceptions.

### E. Diff hygiene

Run and record:

- `git diff --check`
- `git diff --name-only`
- searches for `Pair Reasoning`, `Show & Tell`, and stale rotation language
- full diff inspection

Confirm every change is a direct cadence consequence.

## Required report

Create `sidecar/reports/313_pair_show_alternating_cadence.md` containing:

1. starting commit SHA;
2. Prompt 311/312 dependency status;
3. files inspected;
4. files changed;
5. baseline cadence now expressed by current source;
6. one-mode-per-week audit result;
7. calendar/special-week exception table;
8. grading-boundary audit;
9. validation commands/results;
10. unresolved seams returned to Jeremy + ChatGPT;
11. final commit SHA or working-tree state.

## Definition of done

Prompt 313 is complete only when another course author can answer, without guessing:

- Do Pair Reasoning and Show & Tell both happen as required recurring events in the same normal week? **No.**
- Which one starts the formal-content sequence? **Pair Reasoning.**
- What happens next? **Predictable alternation.**
- Can calendar/special weeks interrupt the pattern? **Yes, explicitly.**
- Does an interruption authorize invented make-up work or grading changes? **No.**
- Are Pair Reasoning and Show & Tell still separate 5% semester categories? **Yes.**

If implementing the cadence would require choosing unresolved technical topics or inventing an exception policy, stop at that seam and report it rather than manufacturing doctrine.