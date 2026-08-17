# Prompt 318 — Define the one-drop regular Decision Gate policy

## Purpose

Implement one narrow grading-policy decision for Fall 2026 DSCT:

> Within the regular **Decision Gate** category, the single lowest retained Decision Gate score is omitted from the category calculation.

This is a resilience policy, not a substitute for the course's continuous late-work and revision/resubmission policy.

## Settled surrounding doctrine

Treat the following as already decided and do not reopen them:

1. **Reasoning Odyssey** is the semester-long reasoning journey.
2. **Decision Gate** is the single student-facing recurring weekly individual reasoning submission.
3. Regular Decision Gates collectively remain the **30%** recurring weekly reasoning category.
4. Odyssey Checkpoints are separate special milestones in Weeks 7, 11, and 14 and collectively remain **15%**.
5. Week 16 Farkle + Machine Learning is a separate **5%** synthesis category, not a Decision Gate and not a checkpoint.
6. Pair Reasoning and Show & Tell are separate social-reasoning categories/events and are not part of the Decision Gate drop rule.
7. Revisions/resubmissions remain open while the course submission system is open.
8. Each submitted attempt receives a fresh academic-quality judgment.
9. The canonical continuous late-work policy applies after academic-quality grading, at roughly 1% per 24 hours late with continuous/hour-level arithmetic rather than whole-day cliffs.
10. For each assignment, the gradebook retains the **highest recorded score earned across attempts**. A later weaker attempt must never lower the student's retained score.

Relevant prompt contracts include:

- `sidecar/prompts/314_define_decision_gate_contract.md`
- `sidecar/prompts/315_define_odyssey_checkpoints_and_farkle_synthesis.md`
- `sidecar/prompts/317_define_revision_resubmission_highest_score_policy.md`

The continuous late-work implementation/provenance lives upstream in the shared curriculum / Course Foundry grading path. Do not copy or fork that arithmetic into DSCT.

## Required policy semantics

Reconcile current DSCT source documents so they state unambiguously:

> **Drop one regular Decision Gate:** after each Decision Gate has resolved to its retained highest recorded score across attempts, omit the single lowest regular Decision Gate score from the 30% Decision Gate category calculation.

The order matters:

1. Grade each attempt for academic quality.
2. Apply the canonical late-work adjustment to that attempt where applicable.
3. For each regular Decision Gate, retain the student's highest recorded attempt score.
4. Across the student's regular Decision Gates, omit the single lowest retained Decision Gate score from the category calculation.

This means a student can keep revising a weak gate. If its retained score rises above another gate, the identity of the dropped gate can change automatically.

## What is eligible for the drop

Eligible:

- regular Decision Gates in the recurring 30% Decision Gate category.

Not eligible:

- Odyssey Checkpoints,
- Week 16 Farkle + Machine Learning synthesis,
- Pair Reasoning reports,
- Show & Tell reports,
- AI Fluency / Professional Minds work,
- career evidence,
- final reflection,
- attendance/participation,
- any other non-Decision-Gate category.

Do not broaden the policy beyond regular Decision Gates without a new explicit Jeremy + ChatGPT decision.

## Missing and zero-score behavior

A never-submitted regular Decision Gate may be represented as a zero/missing score by the deployment system and is eligible to be the single dropped regular Decision Gate.

Do **not** convert that rule into a reason to stop accepting the work. The assignment remains available for late submission/revision under Prompt 317 and the canonical late-work policy while the course submission system is open. If the student later submits and raises that gate's retained score, the category should simply re-evaluate which regular gate is lowest.

## Rationale to preserve in source doctrine

The one-drop rule solves a different problem from continuous late work:

- continuous late work says: **getting behind should not eliminate the reason to finish**;
- revision/highest-score says: **better reasoning later can still improve the record**;
- one dropped Decision Gate says: **one bad week should not define the semester**.

The policy should preserve deadlines as pacing signals without creating a `too late, do not bother` incentive.

## Files to inspect before editing

At minimum inspect:

- `docs/grading-model.md`
- `planning/fall-2026-weekly-architecture.md`
- `planning/fall-2026-topic-map.md`
- current Decision Gate / weekly reasoning assignment templates
- current grading/late/revision language elsewhere in current DSCT source
- Prompts 314, 315, and 317
- Prompt 305 vocabulary report where useful for terminology consistency

Also search current source for stale language such as:

- `drop lowest`
- `drop-lowest`
- `weekly gate`
- `Reasoning Odyssey gate`
- `Reasoning Quest`
- `Decision Gate`
- `late work`
- `resubmit`
- `revision`
- `highest score`

Use historical files only as provenance. Do not rewrite archives merely to make searches quiet.

## Required verification scenarios

The report must reason through at least these examples using symbolic or simple sample scores. Do not invent external-system behavior beyond the settled policy.

### Scenario A — ordinary lowest score drops

A student has retained regular-gate scores such as:

`92, 88, 95, 74, 91`

Verify that `74` is omitted from the Decision Gate category calculation.

### Scenario B — revision changes which gate is dropped

A gate initially retains `60` and is the dropped gate. A later resubmission raises that gate's retained score to `89`; another gate remains at `72`.

Verify that `72`, not the improved gate, becomes the omitted score.

### Scenario C — later weaker resubmission cannot hurt

A gate retains `90`. A later attempt, after quality and late adjustment, records `81`.

Verify that the gate still retains `90` before the category drop logic is applied.

### Scenario D — one missing gate

A student has exactly one never-submitted regular Decision Gate plus otherwise completed gates.

Verify that the missing/zero gate may consume the single drop, while the assignment itself remains open for later submission under the late-work policy.

### Scenario E — special objects are protected

Verify that a low Week 7/11/14 checkpoint, low Week 16 Farkle + ML score, low Pair Reasoning score, or low Show & Tell score cannot be selected by this rule.

## Report

Write:

`sidecar/reports/318_drop_lowest_decision_gate_policy.md`

The report must include:

1. files inspected,
2. current-state conflicts found,
3. files changed,
4. exact final policy wording,
5. the required verification scenarios,
6. any deployment seam where DSCT source doctrine is clear but an external gradebook/compiler needs later implementation,
7. explicit confirmation that no Canvas/Savnac write occurred.

## Hard stops

Do **not**:

- change the 30% Decision Gate weight,
- change the 15% checkpoint weight,
- change the 5% Farkle + ML weight,
- create additional drops,
- drop a checkpoint or special category,
- alter the canonical late-work arithmetic,
- close revisions/resubmissions at checkpoints,
- create a final-submission cutoff beyond an already-existing authoritative institutional/course-close boundary,
- redistribute any other grading category,
- redesign the Week 4–14 topic spine,
- settle the World Bible contract,
- touch Canvas or Savnac,
- modify Jeremy Task Tracking,
- perform opportunistic cleanup.

If implementing this source policy would require changing an external grading engine, compiler, or Canvas setting, document that seam precisely and stop at the DSCT repository boundary unless a later prompt explicitly authorizes cross-repository implementation.

## Git discipline

- Inspect before editing.
- Keep changes bounded to this policy.
- One logical change per commit.
- Use a clear commit message.
- Run relevant text/consistency checks and `git diff --check` where available.
- Preserve concurrent/untracked work that is not part of this prompt.
