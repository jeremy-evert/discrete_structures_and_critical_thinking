# Prompt 315 — Define Odyssey checkpoints and split out the Farkle + ML synthesis

**Status:** FOREMAN-READY DECISION IMPLEMENTATION  
**Source decision:** Jeremy + ChatGPT discussion, 2026-08-17  
**Scope:** DSCT repository only  
**Required report:** `sidecar/reports/315_odyssey_checkpoints_and_farkle_synthesis.md`

## Decisions now settled

This prompt resolves the special-evidence tier inside the Fall 2026 Reasoning Odyssey.

The course now distinguishes three levels of Odyssey evidence:

1. **Decision Gates — 30% semester category**  
   The normal recurring weekly reasoning evidence. A Decision Gate asks whether the student has made the week's reasoning inspectable enough to justify the conclusion being carried forward.

2. **Reasoning Odyssey Checkpoints — 15% semester category**  
   Three special synthesis milestones, each representing one-third of the 15% checkpoint category. They occur in **Weeks 7, 11, and 14**.

3. **Farkle + Machine Learning Synthesis — 5% semester category**  
   Week 16 is now a special synthesis event in its own 5% category. It is no longer an ordinary Decision Gate and it is not one of the three Odyssey checkpoints.

These distinctions are deliberate. Do not collapse them back into one weekly-work family.

## Why Weeks 7, 11, and 14

The placements are based on the current Fall 2026 technical sequence and calendar.

### Week 7 — Checkpoint 1

Week 7 closes the first major formal-reasoning arc in the current map:

- logic, claims, and proof;
- sets/functions/sequences as representations;
- algorithms, correctness, and growth;
- integer properties / modular reasoning;
- induction, recursion, and recurrences.

Checkpoint 1 should ask students to look across their existing evidence and identify how their reasoning about definitions, proof, correctness, assumptions, and checking has developed.

It is not a new technical project layered on top of Week 7.

### Week 11 — Checkpoint 2

Week 11 is the next natural synthesis point after the course has added:

- counting and combinatorial reasoning;
- probability, uncertainty, simulation, and evidence;
- relations / equivalence / partial orders / representations;
- graphs and network reasoning.

Week 11 also avoids using Week 9, whose Thursday meeting is lost to Fall Break.

Checkpoint 2 should make students inspect how their reasoning changes when they move from proof/correctness questions into uncertainty, modeling, representation, and network structure.

It is not a new technical project layered on top of Week 11.

### Week 14 — Checkpoint 3

Week 14 is the end-of-formal-spine checkpoint and the existing mini-capstone/model-limits location.

The current map reaches finite-state machines, invariants, model limits, and synthesis here. Checkpoint 3 should therefore ask students to synthesize the formal core of the semester and examine what their evidence can and cannot establish.

This is the final Odyssey checkpoint before the Week 16 special synthesis.

## Checkpoints are more special than normal Decision Gates

A checkpoint must expose evidence that an ordinary Decision Gate does not.

A normal Decision Gate asks, approximately:

> **What conclusion does this week's evidence justify?**

A checkpoint asks, approximately:

> **What does a collection of my completed reasoning reveal about how I reason, how that reasoning has changed, and what I still need to test?**

The exact student-facing template may be polished, but every checkpoint must require the student to use **existing Decision Gate / course evidence across multiple weeks** and make a defensible synthesis about their own reasoning.

Useful checkpoint evidence includes:

- a claim the student changed, narrowed, rejected, or strengthened;
- a recurring reasoning weakness, blind spot, or failure mode the student can now see;
- a piece of evidence, proof, model, counterexample, test, or explanation the student now regards as especially strong;
- a comparison showing something the student can now reason about more effectively than before;
- a case where confidence increased for a justified reason;
- a case where confidence appropriately decreased;
- an unresolved question, uncertainty, model limit, or piece of evidence that could still change the student's mind;
- explicit references/links/pointers to the prior work supporting those claims.

The checkpoint is therefore **synthesis of real prior evidence**, not retrospective vibes and not a second midterm exam.

## No double-submission on checkpoint weeks

On Weeks **7, 11, and 14**, the checkpoint is the **main Odyssey evidence object for that week**.

Do **not** require students to submit both:

- a full ordinary Decision Gate, and
- a separate checkpoint package

for the same week's Odyssey work.

The week's actual technical work still happens and should provide evidence inside the checkpoint where appropriate. The active Pair Reasoning or Show & Tell event may also feed evidence into the checkpoint while retaining its own already-settled social-reasoning report/category semantics.

This rule prevents the checkpoint from becoming homework duplication.

## Farkle + Machine Learning is now special

Week 16 Farkle + Machine Learning remains the already-accepted synthesis centered on the question:

> **When a Farkle strategy appears better, what are we actually justified in believing?**

Preserve the existing GREEN Farkle + ML work unless a direct reconciliation is necessary for this grading/category decision.

Week 16 now has its own semester-level **5% Farkle + Machine Learning Synthesis** category.

It is:

- not an ordinary Decision Gate;
- not Checkpoint 3 or Checkpoint 4;
- not a comprehensive exam;
- not a programming-performance contest;
- not graded on which strategy wins.

Its special role is to make students combine probability/simulation, algorithms, models, evidence boundaries, repeated measurement, AI skepticism, and justified claims in a rich end-of-semester problem.

The existing evidence-receipt mechanics may remain the student-facing implementation where they still fit. `Evidence receipt` is a format, not permission to create another category.

## Grading arithmetic decision

The old separate **Friday feedback report / A7-equivalent 5% category** is being retired by the settled Show & Tell decision in Prompt 312. Professional peer critique remains assessed inside Show & Tell; only the separate grade bucket disappears.

The freed 5 percentage points are now assigned to:

- **Farkle + Machine Learning Synthesis — 5%**

This resolves the grading-arithmetic seam explicitly.

Do not take these 5 points from Decision Gates, checkpoints, Show & Tell, Pair Reasoning, or another category.

Subject to already-settled prompt changes, the relevant intended semester weights are therefore:

- Decision Gates — **30%**
- Reasoning Odyssey Checkpoints — **15% total**
  - Checkpoint 1, Week 7 — equal one-third of checkpoint category
  - Checkpoint 2, Week 11 — equal one-third of checkpoint category
  - Checkpoint 3, Week 14 — equal one-third of checkpoint category
- Farkle + Machine Learning Synthesis — **5%**
- Pair Reasoning — **5%**
- Show & Tell — **5%** with professional peer critique inside the event/report contract rather than a separate feedback category

Do not use this prompt to rebalance unrelated course categories.

## Relationship to Prompt 314

Prompt 314 defines `Decision Gate` as the single student-facing name for recurring weekly Odyssey evidence and `Reasoning Odyssey` as the semester journey.

If Prompt 314 has completed, consume its report and terminology as current doctrine.

If Prompt 314 has not completed, avoid simultaneous conflicting edits. Implement the checkpoint/Farkle decisions only where safe and clearly report the remaining dependency.

Do not resurrect `Reasoning Gate`, `Reasoning Quest`, `weekly write-up`, or `evidence receipt` as competing gradebook objects while implementing this prompt.

## Current source surfaces to inspect

At minimum inspect and reconcile where unambiguous:

- `docs/grading-model.md`
- `planning/fall-2026-topic-map.md`
- `planning/fall-2026-weekly-architecture.md`
- `planning/week-16.md`
- `week-16/`
- `assignments/week-16-farkle-evidence-receipt.md`
- current Decision Gate / Odyssey assignment or rubric surfaces after Prompt 314
- Prompt 312 report/source if available, to confirm retirement of the separate feedback grade bucket

Consume rather than overwrite accepted Week 16 evidence.

## Source work authorized

This prompt authorizes the bounded source changes needed to make current DSCT doctrine say coherently that:

- normal Decision Gates occupy the 30% recurring category;
- checkpoint weeks are 7, 11, and 14;
- checkpoint weeks use the checkpoint as the week's main Odyssey evidence object rather than stacking a duplicate ordinary gate;
- checkpoints synthesize prior evidence and reasoning development rather than introduce separate technical projects;
- Week 16 Farkle + ML has its own 5% special synthesis category;
- Week 16 is removed from the ordinary Decision Gate category;
- the retired separate feedback/A7 5% is the source of the Farkle + ML 5%;
- the direct semester arithmetic remains 100% after already-settled Prompt 312 changes.

## Authority boundary / hard stops

Do **not**:

- change the total Decision Gate category away from 30%;
- change the total checkpoint category away from 15%;
- change the Farkle + ML synthesis category away from 5%;
- move checkpoint weeks away from 7, 11, and 14;
- invent a fourth checkpoint;
- create a separate ordinary Decision Gate submission on checkpoint weeks;
- redesign the accepted Week 16 Farkle + ML intellectual question;
- reopen the Pair Reasoning contract;
- reopen the Show & Tell contract;
- restore a separate peer-feedback category;
- decide the unresolved World Bible contract;
- freeze or redesign the final eleven-topic Week 4–14 spine beyond the checkpoint placements decided here;
- change late-work, attendance, drop-lowest, or resubmission policy;
- write to Canvas or Savnac.

If final topic-spine reconciliation changes the exact topic labels surrounding Weeks 7 or 11, preserve the **checkpoint week placements** unless Jeremy + ChatGPT explicitly revise them. Report any semantic seam rather than silently moving a checkpoint.

## Verification battery

### A. Weight audit

Verify the current intended source model has:

- Decision Gates: 30%
- Odyssey Checkpoints: 15%
- Farkle + ML synthesis: 5%
- no separate Friday feedback/A7-equivalent grade category after Prompt 312 reconciliation
- total course weight: exactly 100%

Show the arithmetic in the report.

### B. Checkpoint-week audit

Verify Weeks 7, 11, and 14 are the only three checkpoint weeks and that no ordinary Decision Gate is separately required in those weeks.

### C. Distinct-evidence audit

Explicitly answer:

> **What evidence would disappear if the checkpoint category were removed?**

A correct answer must involve longitudinal synthesis of the student's own prior reasoning evidence. If the answer is only "the Week 7/11/14 technical assignment," the implementation has failed.

Also answer:

> **What evidence would disappear if the Farkle + ML category were removed?**

The answer should identify the special cross-topic endgame synthesis and evidence-boundary reasoning, not merely "another Decision Gate."

### D. Anti-bureaucracy walkthrough

Walk through one checkpoint week and demonstrate that a student is not being asked to submit a full ordinary Decision Gate plus a second checkpoint covering the same work.

### E. Week 16 preservation

Verify the accepted Week 16 central question and evidence discipline remain intact and that the category move does not accidentally make strategy outcome, coding polish, or compute resources determine the grade.

### F. Diff hygiene

Run and record:

- `git diff --check`
- `git diff --name-only`
- focused searches for checkpoint week labels, Decision Gate labels, Week 16 grading placement, and stale A7/Friday-feedback category language
- full diff inspection

Confirm every source edit is a direct consequence of this decision or an unavoidable cross-reference repair.

## Required report

Create `sidecar/reports/315_odyssey_checkpoints_and_farkle_synthesis.md` containing:

1. starting commit SHA;
2. Prompt 312 and Prompt 314 dependency status;
3. files inspected;
4. files changed/created;
5. final checkpoint semantics;
6. rationale/source evidence for Weeks 7, 11, and 14;
7. proof that checkpoint weeks do not double-submit an ordinary gate;
8. final Week 16 Farkle + ML category placement;
9. before/after grading arithmetic and explicit 100% check;
10. distinct-evidence audit answers;
11. validation commands/results;
12. unresolved seams returned to Jeremy + ChatGPT;
13. final commit SHA or working-tree state.

## Definition of done

Prompt 315 is complete only when another course author can answer, without guessing:

- How are normal Decision Gates different from checkpoints?
- Why are checkpoints special?
- How many checkpoints exist?
- Which weeks contain them?
- Does a checkpoint week also require a separate full Decision Gate?
- What percentage do the checkpoints occupy?
- Is Farkle + ML a Decision Gate, checkpoint, or separate synthesis?
- What percentage is Farkle + ML?
- Where did that 5% come from?
- Does the course still total exactly 100%?

If any answer requires an unresolved World Bible or final topic-spine decision, preserve that boundary rather than inventing doctrine.