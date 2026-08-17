# Prompt 317 — Define DSCT revision, resubmission, and highest-score policy

## Purpose

Implement the settled DSCT grading-policy decision that students should remain motivated to keep trying after a missed due date or a weak first attempt.

This prompt is a bounded policy-reconciliation task. It should make the current DSCT source model reflect the settled revision/resubmission doctrine without redesigning unrelated grading categories, Canvas/Savnac deployment, or Marker/Course Foundry internals.

## Settled doctrine

The course should explicitly support continued effort:

> **Too late, sucker is not the policy. Better reasoning later is still better reasoning.**

For eligible DSCT work, especially Decision Gates and other evidence-bearing reasoning submissions:

1. **Revisions and resubmissions remain open while the course is open and the submission system can still accept the work.**
2. Each attempt is evaluated fresh for academic quality.
3. The existing continuous late-work policy applies to the timestamp of that attempt.
4. The late-work policy is **1% per 24 hours late, calculated continuously to the second/hour rather than rounded up by day**, with excused-late time handled by the existing trusted policy layer.
5. Lateness must remain separate from academic-quality judgment. Marker should continue to grade the work itself without due/submission timestamps contaminating the reasoning score; the deterministic late-work adapter applies afterward.
6. **The student keeps the highest recorded score earned across attempts. A later attempt must never lower an already-earned grade.**
7. A later attempt may therefore improve the academic-quality score enough to overcome some or all of the additional late penalty. That is desirable: students should have a real incentive to improve weak reasoning.
8. Revision means substantive improvement to the evidence or reasoning, not merely cosmetic changes. Examples include:
   - correcting an invalid inference;
   - narrowing or changing a claim;
   - adding stronger evidence;
   - repairing a proof/test/model;
   - responding to criticism or counterevidence;
   - improving the evidence boundary or uncertainty statement;
   - adding a discriminating test/counterexample.

## Existing implementation evidence to respect

The existing cross-course grading pipeline already contains a deterministic continuous late-work adapter in `course_foundry`, established by the accepted Marker-sidecar late-work integration work. The known acceptance behavior includes:

- 1 hour late = exactly 1/24 of 1% reduction;
- 12 hours late = 0.5% reduction;
- 24 hours late = 1% reduction;
- 21 days late = 21% reduction;
- excused-late seconds reduce effective lateness;
- Marker/Coach receive unpenalized academic work and the late-policy calculation happens afterward.

Do not reimplement or fork that arithmetic in DSCT. Reuse/reference the canonical shared policy where appropriate.

## Required work

Inspect the current DSCT grading and assignment-policy surfaces before editing, including at minimum:

- `docs/grading-model.md`
- current planning/weekly architecture surfaces that mention due dates, revision, resubmission, or Decision Gates
- `sidecar/prompts/314_define_decision_gate_contract.md`
- `sidecar/prompts/315_define_odyssey_checkpoints_and_farkle_synthesis.md`
- the current raw decision pile only as provenance, not authority

Then reconcile the smallest set of current authoritative DSCT source files necessary to make the policy unambiguous.

## Required semantic result

A reasonable student-facing statement should communicate all of the following without implementation jargon:

- due dates matter and help students keep pace;
- missing a due date does not make an assignment worthless;
- late work remains worth doing;
- revisions/resubmissions remain welcome;
- each new attempt may improve the grade;
- the highest recorded score remains;
- later submissions are still subject to the continuous late-work adjustment;
- substantive revision is encouraged because the course values changed reasoning in response to evidence.

Do not tell students that a checkpoint permanently closes earlier Decision Gates. A checkpoint may mark an intellectual milestone, but it must not become a gradebook guillotine that removes the incentive to finish or improve earlier work.

## Acceptance scenarios

Verify the policy language and model against at least these scenarios:

### A. Strong late first submission
A student submits high-quality work several days late. The work is graded for quality, then the continuous late adjustment applies. The attempt still earns meaningful credit.

### B. Weak on-time first attempt, stronger late revision
A student earns a weak academic score on time, learns from feedback, resubmits stronger work later, and the later quality score after its late adjustment exceeds the first recorded score. The later higher recorded score becomes the grade.

### C. Strong first attempt, worse later attempt
A student resubmits but the new attempt would produce a lower recorded score. The earlier higher score remains. A revision can never punish the student merely for trying again.

### D. Criticism-driven revision
A Pair Reasoning or Show & Tell challenge exposes a flaw. The student substantively revises the corresponding evidence-bearing work and may improve the recorded score under the same late-policy arithmetic.

### E. Checkpoint boundary
A student revises an earlier Decision Gate after a checkpoint has occurred. Unless another explicitly authoritative course or system boundary prevents submission, the checkpoint itself must not be cited as the reason the work is closed.

## Hard stops

Do **not** independently decide or change:

- the overall DSCT percentage allocation beyond already-settled prompts;
- Decision Gate / checkpoint / Farkle category weights;
- exact Canvas/Savnac availability/until dates;
- the final end-of-course hard close imposed by institutional grade deadlines;
- drop-lowest policy;
- attendance policy;
- World Bible ontology;
- the final Week 4–14 technical spine;
- Marker or Course Foundry code.

If an implementation or institutional hard-close date must eventually be chosen, report that as a deployment seam rather than inventing it.

## Report

Write:

`sidecar/reports/317_revision_resubmission_highest_score_policy.md`

The report should identify:

- files changed;
- exact policy wording established;
- any stale/contradictory policy language found;
- whether any deployment seam remains;
- acceptance-scenario results;
- any decision that still genuinely requires Jeremy + ChatGPT.

## Git discipline

One logical change, one clear commit. Do not perform opportunistic cleanup. Preserve concurrent/untracked work. If `main` advances before execution, reconcile before editing.
