# Prompt 312 — Define the DSCT Show & Tell contract

**Status:** FOREMAN-READY DECISION IMPLEMENTATION  
**Source decision:** Jeremy + ChatGPT discussion, 2026-08-17  
**Source quarry:** `sidecar/raw/2026-08-17_dsct_design_decision_pile.md`  
**Scope:** DSCT repository only  
**Required report:** `sidecar/reports/312_show_and_tell_contract.md`

## Decision now settled

DSCT **Show & Tell** is one recurring graded event on the weeks where Show & Tell is scheduled.

The semester-level **Show & Tell category remains 5%**.

The inherited separate **Friday feedback report / A7-style grade object is removed as a separate recurring grade category**. Its underlying skill is not removed.

Instead, professional peer critique is a required part of the Show & Tell event and its individual report.

This prompt does **not** reopen the overall grading model. Do not infer any broader category rebalance beyond the explicit removal/folding of the separate Friday-feedback grade object into the Show & Tell contract.

## Why this decision exists

Show & Tell should not be presentation theater.

Its purpose is to make a student's reasoning public enough that other people can inspect, question, challenge, and improve it.

The event must practice two complementary skills:

1. **Defend your own reasoning professionally.**
2. **Critique another person's reasoning professionally.**

Both matter in a Critical Thinking course.

Students should learn to challenge claims, assumptions, evidence, inference, scope, or models without attacking the person, and to receive criticism without treating revision as defeat.

The week's proof, model, simulation, representation, code, derivation, graph, truth table, evidence set, or other technical artifact remains the week's substantive technical work and belongs with the week's normal technical / Reasoning Odyssey evidence.

The **Show & Tell report is not a second copy of that technical submission**.

Its unique evidence is what happened when the student's reasoning became public and when the student professionally challenged another person's reasoning.

## Contract to implement

### 1. Student presents a claim worth defending

The student must make a concrete claim, conclusion, interpretation, model, proof, prediction, or technical judgment visible to the audience.

The exact form varies by week, but the event should make clear:

- what the student is claiming;
- what evidence, proof, model, test, definition, trace, simulation, source, or artifact supports the claim;
- what assumptions or scope boundaries matter;
- what stronger claim the evidence may not justify.

The student should show enough of the technical artifact for the audience to inspect the reasoning. Do not require duplicate submission of the artifact solely for Show & Tell.

### 2. Audience critique is required and professional

Every student participating in Show & Tell must give at least one useful, specific critique/question/challenge to another student's reasoning during the event or in the bounded mechanism defined for that week.

A useful critique targets something inspectable, such as:

- a claim;
- an assumption;
- a definition;
- an inference;
- an omitted case;
- a counterexample;
- an evidence boundary;
- a model choice;
- a representation;
- a proof step;
- a test or simulation design;
- a source or interpretation;
- a stronger claim that exceeds the evidence.

The critique must not reward hostility, performative disagreement, or attacks on the person.

A recurring norm should be expressible approximately as:

> **Critique the claim, assumption, evidence, inference, or model. Do not attack the reasoner.**

Students may agree with a peer and still give useful critique by probing whether the evidence deserves the claimed confidence.

### 3. Receiving criticism is part of the skill

The presenter is expected to treat critique as evidence-bearing input rather than as a contest to win.

A successful outcome may include:

- preserving the original claim because it survives challenge;
- strengthening the justification;
- narrowing the claim;
- correcting an error;
- rejecting an unsupported inference;
- identifying an unresolved uncertainty;
- discovering what evidence would be needed next.

Revision is not failure. Refusing to revise when evidence demands it is not intellectual strength.

### 4. Individual Show & Tell report

Each student submits one individual Show & Tell report for the event.

Keep it compact enough to be sustainable across the semester.

The semantic contract must capture both **defense** and **critique**.

For the student's own presented reasoning, capture:

1. **Claim defended** — what I claimed or concluded.
2. **Strongest evidence shown** — the most important evidence/proof/model/test/etc. supporting it.
3. **Strongest audience challenge received** — the question, objection, counterexample, assumption, or boundary that mattered most.
4. **What survived or changed** — what I preserved, revised, narrowed, corrected, rejected, or left unresolved after public challenge.
5. **Evidence boundary** — what my evidence still does **not** justify.

For the critique the student gave another person, capture:

6. **Professional critique given** — what claim/assumption/evidence/inference/model I challenged or questioned.
7. **Why that critique was useful** — what uncertainty, risk, missing evidence, or reasoning boundary the question was intended to expose.

These seven semantic elements may be compressed into fewer student-facing prompts if no meaning is lost. Do not turn them automatically into seven bureaucratic scoring rows.

### 5. Relationship to Pair Reasoning

Keep the distinction legible.

**Pair Reasoning** asks:

> What happened to my reasoning when another reasoner worked closely inside the problem with me?

**Show & Tell** asks:

> What happened when I made my reasoning public, defended it under questions, and professionally challenged someone else's reasoning?

The two activities may share general reasoning habits, but they should expose different social evidence.

### 6. Grade boundary

The semester-level **Show & Tell category remains 5%**.

The separate inherited **Friday feedback / A7-style 5% grade category should be removed from current DSCT grading doctrine** because its unique skill is now explicitly assessed inside Show & Tell.

Do not create a replacement seventh recurring grade category.

Do not double-grade the technical artifact. The technical work remains with the week's normal technical / Reasoning Odyssey evidence.

The Show & Tell grade should measure the student's own public reasoning/response plus their professional critique of a peer.

## Source work authorized

Implement this contract coherently in current DSCT source where doing so is unambiguous.

At minimum inspect and reconcile:

- `docs/grading-model.md`
- `planning/fall-2026-weekly-architecture.md`
- `planning/fall-2026-topic-map.md`
- `assignments/show-and-tell-artifact.md`
- any current Friday-feedback/A7-equivalent assignment or rubric in DSCT
- current authoring/rubric guidance that defines Show & Tell or peer feedback semantics
- Prompt 311 / Pair Reasoning source where cross-reference clarity is useful, without changing Prompt 311's settled contract

Historical CS2 A4/A7 artifacts may be used as provenance, not copied blindly.

## What to author

Create or reconcile one canonical student-facing Show & Tell assignment/report contract in the DSCT source tree.

It should clearly distinguish:

- the week's technical artifact;
- the live public defense;
- the student's individual Show & Tell report;
- the required professional critique the student gives to someone else.

If separate current DSCT Friday-feedback assignment/rubric source exists solely to support the retired separate grade object, reconcile or retire it cleanly while preserving historical/provenance evidence where appropriate.

If no suitable Show & Tell rubric exists, create a **small** rubric/scoring contract. It should reward at least:

- clear, inspectable public reasoning;
- evidence-based response to challenge;
- visible preservation/revision and evidence-boundary awareness;
- specific, professional critique of another person's reasoning;
- individual accountability.

Do not reward polished speaking style for its own sake, disagreement for its own sake, or rhetorical dominance.

## Authority boundary / hard stops

Do **not**:

- change the Show & Tell category above or below 5%;
- reopen Pair Reasoning's 5% decision;
- rebalance unrelated grading categories;
- decide the final overall grading arithmetic beyond the explicit removal/folding of the separate Friday-feedback category;
- decide the final Reasoning Odyssey / Quest / Gate / World Bible ontology;
- freeze the final Week 4–14 topic spine;
- freeze exact Show & Tell weeks if that depends on the unresolved eleven-week spine;
- invent presentation-length rules for the whole semester if current logistics do not support a clear decision;
- invent permanent groups or audience-rotation policy;
- invent attendance penalties, late-work rules, or drop-lowest behavior;
- write to Canvas/Savnac;
- turn Show & Tell into a speech/presentation-performance course.

If one of those decisions becomes necessary, stop at that seam and return it to Jeremy + ChatGPT.

## Verification battery

### A. Contract consistency

Verify that current operational source consistently expresses all of the following:

- Show & Tell is public explanation and defense under questions, not presentation theater;
- the student presents a claim with inspectable evidence;
- audience critique is required and professional;
- receiving criticism and revising when warranted are part of the skill;
- the individual report records both defense and critique;
- the technical artifact is not duplicated as the Show & Tell report;
- the semester Show & Tell category remains 5%;
- the separate inherited Friday-feedback grade object no longer survives as a current independent 5% category;
- no replacement recurring category was invented.

### B. Anti-duplication test

Explicitly answer in the report:

> **What evidence would disappear if the Show & Tell report were removed?**

A correct answer should include evidence of public defense, response to audience challenge, evidence-boundary awareness, and professional critique given to another student.

If the answer is merely the week's technical artifact, the implementation has failed.

### C. Professional-critique scenarios

Walk the student-facing contract through at least these cases:

1. **Presenter is wrong or overclaims:** a peer challenge exposes a real flaw and the presenter revises.
2. **Presenter survives challenge:** audience questions are serious, but the claim remains justified.
3. **Peer agrees:** the student still produces useful critique by probing assumptions, scope, missing cases, or confidence.
4. **Non-programming week:** the event centers on proof, counterexample, counting argument, relation/model, or another formal artifact rather than code.

For each case, show that the contract rewards critical professionalism rather than combat or empty praise.

### D. Pair Reasoning distinction

Confirm that a student or later author can explain the difference between Pair Reasoning and Show & Tell without relying on the calendar rotation alone.

The distinction should be semantic:

- Pair Reasoning = close collaborative challenge inside the reasoning process;
- Show & Tell = public defense plus professional critique of peers.

### E. Grade-boundary audit

Inspect `docs/grading-model.md` and related source and verify:

- Show & Tell remains exactly 5%;
- the separate Friday-feedback/A7-style category is removed/folded rather than left as another 5%;
- no unrelated category weight is changed by this prompt;
- no technical artifact is accidentally graded twice because of this prompt;
- no new recurring grade category is invented.

If removing the separate 5% feedback bucket makes the total grading arithmetic temporarily unresolved, **do not invent a destination for those percentage points**. Report the arithmetic seam explicitly for the later grading-model decision. This prompt settles the semantic category structure, not the final reallocation of every course percentage.

### F. Diff hygiene

Run and record:

- `git diff --check`
- `git diff --name-only`
- relevant Show & Tell / Friday feedback / A7 terminology searches
- full diff inspection

Confirm that every source change belongs to the Show & Tell contract, the explicit folding/removal of separate feedback grading, or a direct cross-reference consequence.

## Required report

Create `sidecar/reports/312_show_and_tell_contract.md` containing:

1. starting commit SHA;
2. files inspected;
3. historical A4/A7 evidence consulted, if any;
4. files changed/created/retired;
5. final canonical Show & Tell contract summary;
6. how public defense and professional critique coexist in one event;
7. how the technical artifact and Show & Tell report remain distinct;
8. scenario walkthrough results;
9. Pair Reasoning distinction check;
10. grade-boundary audit, including any unresolved total-percentage seam;
11. validation commands/results;
12. unresolved seams returned to Jeremy + ChatGPT;
13. final commit SHA or working-tree state.

## Definition of done

Prompt 312 is complete only when another course author can answer, without guessing:

- What is Show & Tell?
- What must the presenter make public?
- What must the student do when receiving criticism?
- What professional critique must the student give someone else?
- What gets submitted?
- What unique evidence earns the Show & Tell grade?
- Why is the technical artifact not graded twice?
- How is Show & Tell different from Pair Reasoning?
- Is Show & Tell still exactly 5%?
- Is the separate Friday-feedback grade object gone while the feedback skill remains assessed?

If any answer depends on an unresolved broader course-design decision, preserve that boundary and report it rather than inventing doctrine.
