# Prompt 314 — Define the DSCT Decision Gate contract

**Status:** FOREMAN-READY DECISION IMPLEMENTATION  
**Source decision:** Jeremy + ChatGPT discussion, 2026-08-17  
**Evidence consumed:** `sidecar/reports/305_reasoning_vocabulary_inventory.md`  
**Scope:** DSCT repository only  
**Required report:** `sidecar/reports/314_decision_gate_contract.md`

## Decision now settled

The DSCT reasoning ontology should be simplified.

### Student-facing names

- **Reasoning Odyssey** = the semester-long reasoning journey / longitudinal frame.
- **Decision Gate** = the single recurring student-facing weekly individual reasoning submission.

### Names/functions that should not become competing assignment families

- `Reasoning Quest` should not remain a competing student-facing weekly assignment name.
- `Reasoning Gate` should not remain a competing student-facing weekly assignment name where it is merely the old name for the weekly submission.
- `weekly problem-solving write-up` is a reusable reasoning structure/template and historical source, not a second weekly graded object.
- `evidence receipt` / `reasoning receipt` is a reusable evidence format or component that may live inside a Decision Gate or another authorized artifact; it is not automatically its own gradebook object.
- `weekly reinforcement` may remain an internal/gradebook category concept where needed, but students should not be asked to distinguish it from the Decision Gate as another piece of homework.

The anti-bureaucracy rule is:

> **One recurring weekly individual reasoning submission, one student-facing name: Decision Gate.**

## Intended function of a Decision Gate

A Decision Gate asks whether the student has made enough reasoning and evidence visible to justify the conclusion they are carrying forward.

The exact disciplinary work varies by week. A gate may contain a proof, model, computation, simulation, counterexample, graph, truth table, state machine, source analysis, experimental trace, or another form of formal/computational evidence.

The recurring reasoning DNA should preserve the useful existing five-part structure where appropriate:

1. **Sources** — relevant definitions, references, data, examples, or provenance;
2. **Rules / Assumptions** — what is known, assumed, constrained, or uncertain;
3. **Work** — the proof, derivation, model, code, calculation, representation, or analysis;
4. **Check** — how the claim was challenged, tested, cross-checked, or independently verified;
5. **Decision / Summary** — what conclusion is justified now, including an evidence boundary when useful.

Do not force every specialized week into identical prose fields if a more natural artifact preserves the same reasoning semantics. Week 16 is evidence that a specialized receipt can still function as the week's gate without becoming a second assignment family.

## Relationship to other recurring artifacts

### Pair Reasoning

Pair Reasoning remains a separate social-reasoning event/category under Prompt 311. Its unique evidence is what happened when another human reasoner challenged the student's reasoning.

Do not duplicate the technical work inside both artifacts merely to satisfy templates. A Decision Gate may point to or incorporate evidence generated during Pair Reasoning when useful, while the Pair Reasoning report preserves the distinct human-challenge evidence.

### Show & Tell

Show & Tell remains a separate public-defense/critique event/category under Prompt 312. A Decision Gate may use the same underlying proof/model/code/evidence, but the Show & Tell report should preserve the distinct public-defense and professional-critique evidence rather than creating a duplicate technical submission.

### Reasoning Odyssey

The Odyssey is the longitudinal frame that the sequence of Decision Gates, checkpoints, social artifacts, and later reflection make inspectable. Do not turn `Reasoning Odyssey` into the weekly assignment name.

## Source work authorized

Inspect and reconcile current operational DSCT source where the settled naming/function decision can be applied safely.

At minimum inspect:

- `docs/grading-model.md`
- `planning/fall-2026-weekly-architecture.md`
- `planning/fall-2026-topic-map.md`
- `assignments/weekly-problem-solving-writeup.md`
- Week 1 student-facing Reasoning Odyssey language
- Week 2 weekly evidence language
- Week 16 Decision-Gate-equivalent evidence receipt
- any current source that presents `Reasoning Quest`, `Reasoning Gate`, `weekly reinforcement`, `weekly write-up`, or `evidence receipt` as if each were a separate recurring student obligation
- `sidecar/reports/305_reasoning_vocabulary_inventory.md`

Create or reconcile one canonical student-facing Decision Gate assignment/template if current source lacks one.

## Naming discipline

Use this classification for residual terms:

- **RENAME TO DECISION GATE** — current student-facing weekly submission labels that are true aliases.
- **PRESERVE FUNCTIONAL TERM** — terms such as evidence receipt when they accurately describe a format/component rather than a competing assignment.
- **PRESERVE HISTORICAL** — archive, reports, raw design quarry, completed prompts, or provenance material.
- **PRESERVE INTERNAL CATEGORY** — gradebook/planning language that has an operational reason to remain but must not create student-facing duplicate homework.
- **AMBIGUOUS / STOP** — any occurrence whose change would require an unresolved grading, World Bible, checkpoint, or semester-spine decision.

Do not perform an indiscriminate global rename.

## Authority boundary / hard stops

Do **not**:

- decide the final World Bible role, schema, carry-forward policy, or submission cadence;
- decide what makes a Reasoning Odyssey checkpoint larger/deeper than a normal Decision Gate;
- select checkpoint weeks or weights;
- change the total grading arithmetic or redistribute weights;
- change Pair Reasoning or Show & Tell contracts beyond direct cross-reference consistency;
- freeze the final Week 4–14 topic spine;
- rewrite Week 2 or Week 3 pedagogy beyond terminology/cross-reference consequences;
- write to Canvas/Savnac;
- create a second weekly reasoning submission under a new label.

If implementation requires one of those choices, preserve the seam and report it to Jeremy + ChatGPT.

## Verification battery

### A. Student-language test

A student should be able to answer in under one minute:

- What is the Reasoning Odyssey?  
  **The semester-long journey of my reasoning.**
- What do I submit each normal week to show my reasoning?  
  **One Decision Gate.**
- Is an evidence receipt another weekly assignment?  
  **No. It is a format/component when useful.**
- Is the weekly problem-solving write-up another required stream?  
  **No. It supplies a reusable reasoning structure.**

If the current source still requires a glossary to distinguish several weekly aliases, the implementation is not done.

### B. Anti-duplication audit

Inspect the current recurring-work surfaces and explicitly answer:

> **How many individual weekly reasoning submissions does the student believe they owe?**

For the recurring Decision Gate function, the correct answer is one.

Pair Reasoning and Show & Tell may create their own distinct event reports on their scheduled weeks, but they must not cause the same technical artifact to be resubmitted as duplicate technical homework.

### C. Specialized-week compatibility

Walk the contract through at least:

1. a proof/counterexample week;
2. a computational/model/simulation week;
3. Week 16 Farkle + ML evidence receipt.

Show that all three can be recognized as Decision Gates without forcing identical bureaucratic prose templates.

### D. Residual vocabulary audit

Run focused searches for:

- `Reasoning Quest`
- `Reasoning Gate`
- `Reasoning Odyssey gate`
- `weekly reinforcement`
- `weekly write-up`
- `weekly problem-solving`
- `evidence receipt`
- `reasoning receipt`
- `Decision Gate`

Classify every meaningful residual occurrence using the naming discipline above. Historical/provenance occurrences are not errors merely because old vocabulary remains visible there.

### E. Diff hygiene

Run and record:

- `git diff --check`
- `git diff --name-status`
- full diff inspection
- focused terminology searches before and after

No opportunistic grading, calendar, World Bible, checkpoint, or topic-spine redesign belongs in this prompt.

## Required report

Create `sidecar/reports/314_decision_gate_contract.md` containing:

1. starting commit SHA;
2. Prompt 305 evidence consumed;
3. files inspected;
4. files changed/created;
5. final student-facing ontology summary;
6. canonical Decision Gate contract/template summary;
7. alias/residual-term classification;
8. anti-duplication result;
9. three specialized-week walkthroughs;
10. validation commands/results;
11. unresolved seams returned to Jeremy + ChatGPT;
12. final commit SHA or working-tree state.

## Definition of done

Prompt 314 is complete when another course author can answer without guessing:

- What does `Reasoning Odyssey` mean?
- What is the one normal weekly individual reasoning submission called?
- What does a Decision Gate have to make visible?
- Are `Reasoning Quest`, `Reasoning Gate`, `weekly write-up`, and `evidence receipt` separate homework streams?
- Can a specialized artifact such as Week 16 still count as a Decision Gate?
- How do Pair Reasoning and Show & Tell remain distinct without duplicating technical work?

If an answer depends on World Bible policy, checkpoint semantics, grading redistribution, or the final topic spine, stop at that boundary and report it rather than inventing doctrine.
