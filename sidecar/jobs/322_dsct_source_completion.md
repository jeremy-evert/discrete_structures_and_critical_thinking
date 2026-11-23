# Job 322 — DSCT source completion

## Outcome

Turn the current Fall 2026 DSCT repository from a contracted semester spine into a complete, teachable, student-facing source package that is ready for a fresh live-system preflight.

This job exists because Job 321 correctly proved the current blocker: Weeks 4–15 and Week 17 are not yet complete student-facing weekly packages. Fix that blocker in Git. Do not touch SWOSU production Canvas in this shift.

## Authority

Luna owns this source-completion shift inside `jeremy-evert/discrete_structures_and_critical_thinking`.

Luna may:

- author and revise DSCT student-facing and instructor-facing course source;
- reconcile stale DSCT planning/status documents against the source actually landed;
- create or improve DSCT-local validators, manifests, tests, scripts, and reports;
- dispatch bounded workers for independent week clusters and inspect/reject/repair their receipts;
- make small reversible authoring decisions needed to turn already-frozen contracts into usable lessons, provided they do not change course outcomes, grading weights, checkpoint weeks, official calendar facts, or materially increase required student workload;
- use historical Spring 2026 lessons and accepted Fall 2026 planning/reports as source material and provenance.

Luna may read sibling repositories when they contain an already-adopted shared source or contract, but may not modify another course repository, JTT, Course Foundry, Harbor, or the shared dirty Course Foundry checkout in this job.

## Hard boundaries

- **No SWOSU production Canvas writes.** Production is read-only if inspected at all.
- **No Savnac writes.** This is a source-authoring burn, not a deployment burn.
- Do not reset, clean, stash, normalize, or develop inside the dirty shared Course Foundry checkout.
- Do not take CS1, Computer Architecture, CS2, or JTT work.
- Do not change the settled grading weights in `docs/grading-model.md`.
- Do not move the Reasoning Odyssey checkpoints from Weeks 7, 11, and 14.
- Do not turn Week 16 into a Decision Gate or checkpoint; its Farkle + ML synthesis remains its own 5% category.
- Do not invent a comprehensive programming exam or Reasoning Defense final. Week 17 is the settled 5% individual reflection.
- Do not create a normal Thursday class or graded Thursday artifact for Week 9; Oct 15 is Fall Break.
- Do not create a new formal topic, mandatory assignment, or ordinary class meeting for Week 15. It is the asynchronous Thanksgiving/Mexico travel buffer.
- Do not add a required textbook path. Fall 2026 has no required textbook/external-course spine.

## Authoritative source order

When sources disagree, prefer current accepted Git truth in this order:

1. `docs/grading-model.md`
2. `planning/fall-2026-spine.md`
3. `planning/fall-2026-topic-map.md`
4. `planning/fall-2026-weekly-architecture.md`
5. accepted reports and current student-facing source
6. historical `lessons/*.md` and Spring 2026 archive as provenance/content quarry

Do not let stale historical prompts override newer accepted source.

## First repair: reconcile obvious planning drift

Before mass authoring, inspect the current planning contracts for stale statements. In particular, the weekly-architecture document still contains an old Week 3 sentence that can conflict with the frozen spine's newer rule that Week 3 is a container/LaTeX runway and Weeks 4–14 are the formal topic sequence.

Repair only genuine contradictions. Preserve useful history in reports rather than carrying contradictory instructions forward.

## Week 2 reconciliation

Week 2 has real source and historical production evidence, but the spine status and earlier reports disagree about how complete it is.

Inspect current `week-02/`, its assessment/rubric source, accepted reports, and DSCT-local validators. Resolve source-path/reference defects that are owned by DSCT. If the current Week 2 package is genuinely teachable and internally complete, update its source/status truth accordingly. If a missing shared dependency prevents local validation, name that yellow without blocking Weeks 4–17 authoring.

Do not attack the historical CloudFront/WAF production seam in this source job.

## Formal core: Weeks 4–14

Author the eleven formal topic weeks from the frozen map and historical lesson quarry. Every Fall 2026 formal topic already traces to content Jeremy has taught before; this job is adaptation and packaging, not invention.

Use:

- `planning/fall-2026-topic-map.md` for topic, critical-thinking question, AI failure anatomy, Thursday mode, provenance, and prerequisite chain;
- `planning/fall-2026-weekly-architecture.md` for the Tuesday/Thursday instructional chassis;
- the named `lessons/*.md` historical sources as disciplinary content quarry;
- Week 1's Sources → Rules/Assumptions → Work → Check → One-Sentence Summary method as the reasoning spine;
- existing DSCT assignment/rubric templates and `docs/grading-model.md` rather than creating parallel grading doctrine.

For each formal week, land a coherent student-facing and instructor-facing package. Exact filenames may follow the best current DSCT pattern, but the package must contain enough source for another agent to compile the week without inventing pedagogy.

At minimum, each formal week must make explicit:

- week identity, dates, learning targets, and prerequisite assumptions;
- Tuesday technical lesson/demo source with one inspectable worked example;
- the Tuesday AI-fluency failure mode/check;
- the student's individual reasoning evidence path for that week;
- the correct Thursday mode from the frozen cadence;
- the Thursday artifact/critique/revision expectations when a Thursday meeting exists;
- the correct Decision Gate versus Reasoning Odyssey Checkpoint behavior;
- instructor run-of-show / facilitation notes sufficient to teach the two class meetings;
- source provenance to the historical lesson(s) and current planning contract;
- no unresolved placeholder tokens or fictitious external resources.

### Week-specific invariants

- Week 4: Logic, Claims & Proof; Show & Tell; ordinary Decision Gate.
- Week 5: Sets, Functions & Sequences; Pair Reasoning; ordinary Decision Gate.
- Week 6: Algorithms, Correctness & Growth; Show & Tell; ordinary Decision Gate.
- Week 7: Integer Properties & Cryptography; Pair Reasoning; **Odyssey Checkpoint 1 replaces the ordinary Decision Gate**.
- Week 8: Induction, Recursion & Recurrences; Show & Tell; ordinary Decision Gate.
- Week 9: Counting & Combinatorial Reasoning; Tuesday-only Fall Break week; pair-style work folds into Tuesday; ordinary Decision Gate unless current accepted grading source says otherwise.
- Week 10: Probability, Uncertainty & Evidence; Show & Tell; ordinary Decision Gate.
- Week 11: Relations/Orders/Matrices/Digraphs; Pair Reasoning; **Odyssey Checkpoint 2 replaces the ordinary Decision Gate**.
- Week 12: Graphs & Network Reasoning; Show & Tell; ordinary Decision Gate.
- Week 13: Trees, Search & Decision Structures; Pair Reasoning; ordinary Decision Gate.
- Week 14: Boolean Algebra/Circuits/SAT + Finite-State Machines/Model Limits; Show & Tell mini-capstone; **Odyssey Checkpoint 3 replaces the ordinary Decision Gate**.

## Week 15

Author an explicit student-facing asynchronous buffer/wind-down package and instructor note so the week is not an empty hole in the course.

It may:

- orient students to Thanksgiving/travel expectations;
- point them toward already-open revision/resubmission opportunities;
- summarize what remains before Week 16;
- provide optional review or catch-up guidance.

It may **not** invent a new formal topic, new normal class meeting, new required assignment, or new due date.

## Week 17

Author the final individual reflection package using the already-settled 5% category in `docs/grading-model.md`.

The final should be low-stress and evidence-bearing, asking students to reflect on how their reasoning changed, what evidence changed their mind, where AI helped or misled, what methods transferred, and what remains uncertain. Reuse existing reflection/rubric source where available before writing new material.

Do not add a comprehensive exam.

## Remaining recurring categories

Inventory the source required by the existing grading model, including course evaluation, career artifact sequence, Tuesday technical evidence, attendance/participation, AI Fluency, Professional Minds, Pair Reasoning, Show & Tell, Decision Gates, checkpoints, Week 16, and Week 17.

If a recurring category is already represented by a reusable template/shared source, reference/reuse it instead of cloning it into every week.

If an exact per-week schedule is absent but can be resolved by the frozen weekly chassis without changing semester weight or workload, Luna may choose a simple consistent schedule and record the decision. Escalate only decisions that materially alter student obligations or settled grading policy.

## Validation

Create or improve DSCT-local validation so the repository can falsify the claim that source completion is done.

At minimum prove:

- Weeks 1–17 have an intentional student-facing source state;
- Weeks 4–14 each satisfy the formal-week package contract above;
- Week 9 has no Thursday class requirement;
- Week 15 contains no new formal topic/required graded assignment/due date;
- Week 16 remains the validated Farkle + ML package and is not duplicated into another category;
- Week 17 has the final 5% reflection package;
- checkpoint weeks are exactly 7, 11, 14 and do not also create ordinary Decision Gates;
- grading weights still total 100%;
- no unresolved placeholder/source tokens remain in the newly authored package;
- referenced DSCT-local files exist;
- `git diff --check` passes.

Run any existing relevant DSCT validators as well. Do not make missing external deployment dependencies look like source failures; name those separately.

## Worker strategy

This is large enough to parallelize, but not to surrender integration.

Prefer bounded week clusters such as:

- worker A: Weeks 4–6;
- worker B: Weeks 7–9;
- worker C: Weeks 10–12;
- worker D: Weeks 13–14;
- worker E: Weeks 15 and 17 plus recurring-source audit.

Each worker gets exact authority, forbidden paths, acceptance tests, and evidence destination. Luna independently inspects receipts and resulting source, repairs inconsistencies, and integrates accepted work. Do not ask Jeremy to relay worker output.

If a worker repeatedly fails to produce artifacts, do not burn the shift retrying the same broad prompt. Narrow the unit or complete a tiny integration task directly under the Foreman tiny-work exception.

## Git discipline

- Start from current canonical DSCT `main` and fetch before promotion.
- Use isolated worker branches/worktrees.
- One logical change per commit where practical.
- Do not force-push.
- Do not overwrite unexpected remote drift; stop or rebase/repair deliberately according to the Foreman contract.
- Promote accepted DSCT work to canonical `main` during this shift when safe.

## Evidence

Write:

`sidecar/reports/322_luna_dsct_source_completion.md`

Include:

- starting and ending DSCT SHAs;
- week-by-week final source classification;
- worker branches/receipts and acceptance decisions;
- files/packages authored;
- planning contradictions repaired;
- validation commands/results;
- named external/deployment yellows deliberately deferred;
- exact next action.

End with exactly one verdict:

`**Verdict:** `SOURCE READY FOR PREFLIGHT``

or

`**Verdict:** `SOURCE BLOCKED``

For `SOURCE BLOCKED`, state the single material source/pedagogy decision that prevents a complete teachable package.

## Done

This job is done when current canonical DSCT `main` contains a complete teachable Fall 2026 source package and durable validation proving the Job 321 source blocker has been removed, or one genuine source/pedagogy blocker has been isolated precisely enough that another agent does not need to rediscover it.

Do not perform Savnac or SWOSU production writes in this shift.
