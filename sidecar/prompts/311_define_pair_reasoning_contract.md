# Prompt 311 — Define the DSCT Pair Reasoning contract

**Status:** FOREMAN-READY DECISION IMPLEMENTATION  
**Source decision:** Jeremy + ChatGPT discussion, 2026-08-17  
**Source quarry:** `sidecar/raw/2026-08-17_dsct_design_decision_pile.md`  
**Scope:** DSCT repository only  
**Required report:** `sidecar/reports/311_pair_reasoning_contract.md`

## Decision now settled

The recurring DSCT pair activity is **Pair Reasoning**.

Pair Reasoning is one recurring graded event on the weeks where Pair Reasoning is scheduled. The semester-level **Pair Reasoning report category remains 5%**.

This prompt does **not** reopen the overall grading model. Do not infer that other recurring categories must also change to 5%, and do not rebalance the course percentages here.

The unique purpose of Pair Reasoning is:

> **Expose a student's reasoning to another human reasoner and record what happened under challenge.**

The week's proof, model, code, simulation, checker, graph, truth table, derivation, counterexample, or other technical artifact remains the week's substantive technical work and belongs with the week's normal technical/Reasoning Odyssey evidence.

The **Pair Reasoning report is not a second copy of that technical submission**.

Its unique evidence is the individual student's reasoning before, during, and after another person challenged it.

## Contract to implement

### 1. Before discussion: individual starting position

Each student should briefly establish an independent starting state before substantive pair discussion.

The exact student-facing wording may be polished, but the contract must preserve:

- the claim, approach, prediction, interpretation, or answer the student currently favors;
- why the student currently believes it;
- an assumption, uncertainty, or confidence statement when useful.

This should be compact. Do not create a pre-lab essay.

### 2. During Pair Reasoning: one reasoner sharpens another

The pair should compare reasoning rather than merely divide labor.

The recurring activity should support moves such as:

- compare assumptions or definitions;
- identify where models/approaches differ;
- identify the strongest part of the partner's reasoning;
- challenge an inference, assumption, representation, or evidence boundary;
- seek discriminating evidence through proof, counterexample, trace, test, simulation, source, definition, checker, or another method appropriate to the week;
- distinguish an AI proposal from independently verified evidence when AI materially contributes.

Pair Reasoning does **not** require artificial disagreement.

If both students agree, the task becomes:

> **Test whether the agreement deserves confidence.**

If they disagree, the task is not to win. The task is to identify what evidence, definition, assumption, proof step, observation, or counterexample actually separates the positions.

### 3. After discussion: individual Pair Reasoning report

Each student submits one individual report for the Pair Reasoning event.

Keep the report short enough to be sustainable across the semester, but require evidence of genuine intellectual contact.

The report should capture, in a compact form:

1. **Starting position** — what I thought or proposed before the discussion.
2. **Strongest challenge** — the most important question, objection, counterexample, alternative, or assumption my partner raised.
3. **Evidence that mattered** — what proof/test/definition/trace/source/simulation/etc. actually bore on the disagreement or confidence level.
4. **What changed or survived** — what I revised, narrowed, rejected, strengthened, or preserved after the challenge.
5. **Current position** — what I now believe and why.
6. **What would change my mind next** — the remaining evidence/question that could materially move the conclusion.

These six ideas are the semantic contract. The final student-facing template may compress them into fewer visible prompts if no meaning is lost.

### 4. Programming is optional, reasoning is required

Do not preserve CS2's driver/navigator machinery as a DSCT requirement.

Programming may be the right instrument on some weeks, but Pair Reasoning must also work naturally for:

- proofs;
- counterexamples;
- set/function/relation models;
- counting arguments;
- probability/simulation claims;
- graphs/trees;
- Boolean/SAT reasoning;
- finite-state models;
- source/evidence analysis;
- other formal or computational reasoning tasks.

Do not require every Pair Reasoning event to produce code, commits, or a shared repository.

### 5. Individual accountability

The 5% Pair Reasoning category grades the **individual Pair Reasoning report**, not the quality of a shared pair artifact.

The report must make each student's reasoning visible enough that one student's work cannot simply stand in for the other's.

The technical artifact may be shared or individual depending on the week's technical task, but Pair Reasoning grading should not double-grade the same artifact already assessed in the week's technical/Reasoning Odyssey evidence.

## Source work authorized

Implement this contract coherently in current DSCT source where doing so is unambiguous.

At minimum inspect and reconcile the relevant current surfaces, including:

- `docs/grading-model.md`
- `planning/fall-2026-weekly-architecture.md`
- `planning/fall-2026-topic-map.md`
- the current Pair Reasoning / legacy pair-report assignment template under `assignments/`
- any current rubric or authoring guidance that defines the pair-report semantics

Prompt 304 owns the broad terminology migration from Pair Programming to Pair Reasoning. Do not duplicate archaeology already completed by Prompt 304 if its report is available. Consume that report and build on it.

If Prompt 304 has not yet completed, implement only what can be done safely without creating conflicting simultaneous edits, and report the dependency.

## What to author

Create or reconcile one canonical student-facing Pair Reasoning assignment/report contract in the DSCT source tree.

It should be concise enough for repeated use and should clearly distinguish:

- the week's technical work;
- the live Pair Reasoning activity;
- the student's individual Pair Reasoning report.

If a rubric already exists, reconcile it. If no usable rubric exists, create a **small** rubric or scoring contract that measures the unique Pair Reasoning evidence without turning the six semantic fields above into six bureaucratic scoring rows by default.

A good compact rubric should reward at least:

- authentic engagement with another reasoner's challenge;
- evidence-based response rather than assertion;
- visible revision/preservation of the student's own reasoning;
- individual accountability.

Do not reward disagreement for its own sake.

## Authority boundary / hard stops

Do **not**:

- change the Pair Reasoning category above or below 5%;
- rebalance other grading categories;
- decide the final overall grading arithmetic;
- decide the final Reasoning Odyssey / Quest / Gate / World Bible ontology;
- decide the final Show & Tell contract;
- decide whether Show & Tell peer feedback remains a separate grade category;
- freeze the final Week 4–14 topic spine;
- freeze exact Pair Reasoning weeks if that depends on the unresolved eleven-week spine;
- require stable semester-long partners or a partner-rotation policy;
- invent attendance penalties or late-work rules;
- write to Canvas/Savnac;
- turn Pair Reasoning into a programming-only activity.

If one of those decisions becomes necessary, stop at that seam and return it to Jeremy + ChatGPT.

## Verification battery

### A. Contract consistency

Verify that current source consistently expresses all of the following:

- Pair Reasoning is the recurring pair activity;
- its unique purpose is reasoning under human challenge;
- it can use code but does not require code;
- the technical artifact is not duplicated as the Pair Reasoning report;
- the Pair Reasoning report is individual;
- the semester category remains 5%;
- agreement is allowed but must still be tested;
- the activity does not inherit required driver/navigator roles from CS2.

### B. Anti-duplication test

For the canonical assignment/report, explicitly answer in the report:

> **What evidence would disappear if the Pair Reasoning report were removed?**

A correct answer should describe evidence of the student's reasoning changing, narrowing, strengthening, or surviving another human's challenge.

If the answer is merely “the technical work,” the implementation has failed because it duplicates the weekly technical evidence.

### C. Three scenario walkthroughs

Walk the student-facing contract through at least these three hypothetical cases:

1. **Disagreement:** partners begin with materially different claims or approaches.
2. **Agreement:** partners begin with the same answer/approach and must test whether agreement deserves confidence.
3. **Non-programming week:** the task is primarily proof/counterexample/formal reasoning rather than code.

For each case, show that the same Pair Reasoning contract produces meaningful individual evidence without forcing fake disagreement or programming artifacts.

### D. Grade-boundary audit

Inspect `docs/grading-model.md` and any related assignment language and verify:

- Pair Reasoning remains 5% at the semester-category level;
- no other category weight changed;
- no shared artifact is accidentally counted twice because of this prompt;
- no new grade category was invented.

### E. Diff hygiene

Run and record:

- `git diff --check`
- `git diff --name-only`
- relevant terminology searches
- full diff inspection

Confirm that every source change belongs to the Pair Reasoning contract or a direct cross-reference consequence.

## Required report

Create `sidecar/reports/311_pair_reasoning_contract.md` containing:

1. starting commit SHA;
2. Prompt 304 dependency status and any evidence consumed from it;
3. files inspected;
4. files changed/created;
5. final canonical Pair Reasoning contract summary;
6. how the technical artifact and individual report are kept distinct;
7. three scenario walkthrough results;
8. grade-boundary audit;
9. validation commands/results;
10. unresolved seams returned to Jeremy + ChatGPT;
11. final commit SHA or working-tree state.

## Definition of done

Prompt 311 is complete only when another course author can answer, without guessing:

- What is Pair Reasoning?
- What does a student do before, during, and after it?
- What gets submitted?
- What unique evidence earns the Pair Reasoning grade?
- Why is the report not duplicate homework?
- What happens if partners already agree?
- Can the activity work without programming?
- Is the semester Pair Reasoning category still exactly 5%?

If any answer depends on an unresolved broader course-design decision, preserve that boundary and report it rather than inventing doctrine.