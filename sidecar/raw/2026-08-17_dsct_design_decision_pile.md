# DSCT design-decision pile

**Date:** 2026-08-17  
**Status:** RAW DESIGN DECISION PILE, NOT YET PROMPT CONTRACTS  
**Purpose:** isolate the course-design questions that remain owned by Jeremy + ChatGPT after the first Foreman-ready mechanical/evidence work was cut into Prompts 304–310.

This file is intentionally a thinking surface, not a task list and not a command queue.

The process for this pile is:

1. gather the consequential design questions here;
2. let Prompts 304–310 return evidence where useful;
3. refine this raw pile into explicit decision contracts;
4. only then cut implementation prompts from decisions that are actually settled.

The piles are allowed to overlap. A decision may depend on evidence gathered by a Foreman prompt, and one decision may unlock several later prompts.

---

# 1. Do not reopen these unless new evidence creates a real contradiction

These directions are already strong enough to treat as current course doctrine while this pile is refined.

## Course identity

> **Reasoning is the work of the year.**

The central questions are:

> **What would it take to convince a skeptic?**

and

> **How would you reason with them?**

Discrete mathematics supplies precise objects worth reasoning about. Critical Thinking supplies the habits used to decide whether a claim deserves confidence.

## Pair activity name

> **Pair Reasoning**

Pair Programming is no longer the conceptual name for the recurring pair activity in DSCT.

Programming may still be used inside Pair Reasoning when code is the right instrument.

## Persistent course direction

> **Reasoning Odyssey**

The old coding-centered framing is no longer broad enough. The Odyssey should be able to carry proofs, models, simulations, arguments, code, evidence, revisions, and changes of mind.

## Week runway

- Week 1: compressed Semester Kickoff Week
- Week 2: **Building Your AI Lab**
- Week 3: **Containers + minimum-useful LaTeX**
- Weeks 4–14: eleven formal DSCT core weeks
- Week 15: asynchronous Thanksgiving/Mexico travel buffer
- Week 16: existing GREEN Farkle + Machine Learning synthesis
- Week 17: individual final reflection/closeout

## Resource philosophy

If a paid book genuinely earns required status, require it.

If no paid book is necessary, do not invent a textbook spine for appearance. Curate the best useful slices of the best available resources and make DSCT provide the connective tissue.

## AI posture

> **Love AI more. Trust AI less.**

AI may propose. Evidence decides.

No paid AI subscription should create a higher attainable grade ceiling.

---

# 2. Dependency map: the order in which the design questions probably need attention

Not every open question is equally upstream.

A useful working order is:

## Tier A — define the student reasoning system

These decisions determine what the recurring course artifacts actually are.

1. Reasoning Odyssey / Reasoning Quest / Gate / World Bible ontology
2. World Bible role in DSCT and cross-course continuity
3. Pair Reasoning contract
4. Show & Tell contract
5. relationship among weekly evidence, social reflection, and persistent record

These should be resolved before grading categories and weekly authoring templates are frozen.

## Tier B — define the semester intellectual spine

6. collapse/reframe twelve current topic bundles into eleven Weeks 4–14 core weeks
7. decide what Week 4's first Show & Tell is actually defending
8. decide checkpoint locations after the final spine exists
9. preserve Week 16 as synthesis rather than accidentally turning it into another core topic

The open-resource harvest from Prompt 308 should inform this tier.

## Tier C — define the runway implementation

10. exact DSCT Week 2 bounded AI-lab reasoning exercise
11. exact Week 2 Pair Reasoning experience
12. supported Week 3 container path
13. supported LaTeX engine/workflow
14. minimum explicit command-line literacy
15. Week 3 reproducibility-focused Pair Reasoning experience

Prompts 306 and 307 should return evidence before these are frozen.

## Tier D — define grading behavior and humane course mechanics

16. what each recurring grade category is actually measuring
17. whether peer feedback remains its own category
18. how Pair Reasoning and Show & Tell reflections differ
19. checkpoint weights/weeks
20. due windows
21. revision/resubmission policy
22. late-work policy
23. drop-lowest behavior
24. attendance/participation evidence expectations

The ontology and semester spine should exist before these are finalized.

## Tier E — authoring and deployment grammar

25. weekly authoring package/template
26. source-card contract
27. validation battery for reasoning quality
28. Course Foundry mapping
29. Savnac fixed-point/read-back expectations

These should become implementation prompts only after the upstream decisions are stable.

---

# 3. Decision cluster A: What exactly is the Reasoning Odyssey system?

## The problem

Current/historical vocabulary includes:

- Reasoning Odyssey
- Reasoning Quest
- Reasoning Gate
- weekly write-up
- evidence receipt
- checkpoint
- World Bible
- Pair Reasoning reflection
- Show & Tell reflection
- peer feedback

We do not want students maintaining five differently named artifacts that all ask them to explain the same work again.

## Strong current direction

A promising ontology is:

- **Reasoning Odyssey** = semester-long journey / persistent intellectual frame
- **World Bible** = living record/context inside the Odyssey
- **Reasoning Quest or Gate** = week's individual evidence package
- **Pair Reasoning** = social challenge mode
- **Show & Tell** = public explanation/defense mode
- **event reflection** = individual record of what changed when reasoning met another human

This is not yet frozen.

## Questions to decide

1. Is `Reasoning Quest` or `Reasoning Gate` the student-facing weekly name, or do both serve distinct purposes?
2. Is the weekly evidence package a separate file/object, or can it be assembled from the week's actual proof/model/code + a compact reasoning receipt?
3. What is a checkpoint beyond a normal weekly gate?
4. Does the World Bible live inside the Odyssey, or is the World Bible the persistent implementation of the Odyssey?
5. Which artifact does the student open first when asked, "Show me how your thinking changed this semester"?
6. Can the system be explained to a student in under one minute without a glossary?

## Anti-bureaucracy test

For every proposed artifact, ask:

> **What unique evidence does this object expose that another object does not?**

If the answer is weak, merge or remove the object.

## Evidence expected from Foreman work

Prompt 305 should return the actual current vocabulary/function map before this is frozen.

---

# 4. Decision cluster B: What does the World Bible become in DSCT?

## Why it matters

The World Bible is one of the strongest continuity mechanisms across CS1, CS2, and DSCT because it lets students personalize their learning and preserve history rather than treating each week as disposable.

## Proposed maturation

### CS1

Ownership and identity.

### CS2

Design and engineering judgment.

### DSCT

Reasoning history.

Possible DSCT content includes:

- claims currently believed
- definitions
- assumptions
- examples and counterexamples
- sources
- proof/test/simulation/model evidence
- uncertainty
- confidence
- what changed the student's mind
- what survived challenge
- what stronger claim is not justified
- what would change the student's mind next

## Questions to decide

1. Literal carry-forward from CS1/CS2, or a new DSCT-native World Bible with optional import?
2. Should the student-facing name remain exactly `World Bible`?
3. Does a student choose one world/system/domain for the semester, or can the context evolve?
4. How does a transfer/new student bootstrap cleanly?
5. What constitutes a meaningful update?
6. How often can there be **no change** without penalty?
7. Which claims are worth tracking longitudinally?
8. Should the student preserve earlier wrong beliefs rather than overwriting them?
9. Is there a compact status vocabulary such as preserve / revise / narrow / reject / unresolved, or is that too much machinery?

## Strong constraint

The World Bible must not become compulsory fiction or ceremonial weekly journaling.

A topic must stand on its own when forcing the carried world would be artificial.

## Evidence expected from Foreman work

Prompt 309 should recover what the World Bible actually does in CS1/CS2/DSCT before this contract is frozen.

---

# 5. Decision cluster C: What is Pair Reasoning as an experience?

## Name is decided

> **Pair Reasoning**

## Purpose direction

One reasoner sharpens another.

The point is not merely to split labor. The point is to expose reasoning to another mind.

## Candidate anatomy

1. state an initial claim / approach / prediction
2. explain why you currently believe it
3. compare models/assumptions
4. identify the strongest part of the partner's reasoning
5. challenge one assumption/inference/evidence boundary
6. seek discriminating evidence
7. record what changed and what survived
8. individually state what you now believe and what would change your mind

## Questions to decide

1. Must each person state a position before discussion?
2. What happens when both partners already agree?
3. Does every Pair Reasoning event require a computational artifact?
4. How much individual accountability is needed?
5. What is the shortest reflection that still captures a genuine change/challenge?
6. Should partners stay together for multiple weeks or rotate?
7. How do we protect against one student doing all reasoning while the other signs the receipt?
8. How do we distinguish useful disagreement from debate theater?
9. What exactly earns the Pair Reasoning grade?

## Strong direction

Agreement is not failure. If both reasoners agree, they should test whether the agreement is deserved.

Winning is not the goal. Identifying what evidence, definition, assumption, proof step, or counterexample separates the positions is the goal.

---

# 6. Decision cluster D: What is Show & Tell as an experience?

## Purpose direction

Show & Tell should be public explanation and defense, not presentation theater.

The student makes reasoning visible enough that other people can interrogate it.

## Candidate questions

- What am I claiming?
- What is my strongest evidence?
- What assumption should the audience challenge?
- What is my most likely overclaim?
- What audience question exposed something I had not considered?
- What did I revise afterward?

## Questions to decide

1. What must a student physically show or demonstrate?
2. Individual or small-group presentation?
3. How much time per student/group?
4. Is audience feedback graded separately or folded into participation/reasoning evidence?
5. What is the individual post-event reflection?
6. How different must Show & Tell be from Pair Reasoning to justify separate categories?
7. What does Week 4's first Show & Tell synthesize when Week 3 is tools runway rather than formal discrete math?

## Strong constraint

Show & Tell must force explanation, challenge, and revision. If it can be completed as a polished monologue with no intellectual risk, it is too weak.

---

# 7. Decision cluster E: What are the eleven formal Week 4–14 core weeks?

## Current problem

The current map has twelve bundles:

1. Logic, Claims & Proof
2. Sets, Functions & Sequences
3. Algorithms, Correctness & Growth
4. Integer Properties & Cryptography
5. Induction, Recursion & Recurrences
6. Counting & Combinatorial Reasoning
7. Probability, Uncertainty & Evidence
8. Relations, Equivalence, Partial Orders, Matrices & Digraphs
9. Graphs & Network Reasoning
10. Trees, Search & Decision Structures
11. Boolean Algebra, Circuits & SAT
12. Finite-State Machines, Invariants & Model Limits

The new runway leaves eleven Week 4–14 slots.

## Questions to investigate before deciding

- Can trees live naturally inside graph/network reasoning?
- Can algorithms/correctness become a recurring reasoning lens rather than its own week?
- Can sets/functions/relations be reorganized around representation without overload?
- Should logic/proof get more protected space because it anchors the skeptic question?
- Can Boolean/SAT and finite-state systems share a coherent systems-modeling week?
- Does cryptography earn a full week or work better as a motivating application of integer/modular reasoning?
- Which concept most naturally feeds Week 16 Farkle + ML without duplicating it?

## Decision criteria

The final spine should optimize for:

1. catalog coverage
2. coherent prerequisite flow
3. reasoning depth rather than chapter coverage
4. a characteristic Critical Thinking move every week
5. a meaningful Pair Reasoning or Show & Tell artifact
6. enough time to actually teach the mathematics
7. compatibility with the skeptic north star
8. natural bridges to AI verification and computational checking where appropriate
9. Week 16 synthesis value
10. student workload realism

## Evidence expected from Foreman work

Prompt 308 should return the source/resource harvest before this decision is frozen.

Prompt 310 should return stale-source/dependency seams after the earlier evidence work completes.

---

# 8. Decision cluster F: What exactly happens in Week 2?

## Identity is decided

> **Building Your AI Lab**

## Strong instructional purpose

A student should leave Week 2 with a working local AI environment and the beginning of a durable epistemic habit:

> **AI proposes. Evidence decides.**

## Shared structure worth preserving

`Check -> Baseline -> bounded proposal -> Diff -> independent Final test -> read/reason -> accept or reject from evidence`

## Questions to decide

1. Reuse CS2's bounded exercise or create a DSCT-flavored one?
2. If DSCT-specific, what claim/evidence task is simple enough for Week 2 but genuinely about reasoning?
3. What exactly gets submitted?
4. How much of the shared readiness artifact is reused directly?
5. What is the Thursday Pair Reasoning experience?
6. What does the Week 2 Reasoning Quest/Gate look like before formal discrete topics begin?
7. How do we make the setup evidence useful without producing a giant configuration report?

## Evidence expected from Foreman work

Prompt 306 should return the reuse/ownership/evidence map before final Week 2 authoring.

---

# 9. Decision cluster G: What exactly happens in Week 3?

## Identity is decided

> **Containers + minimum-useful LaTeX**

## Why

LaTeX gives students a professional way to communicate formal reasoning.

Containers give computational reasoning a reproducible environment.

Neither tool is the intellectual center of the class.

## Questions to decide

1. Which container runtime is the required supported path?
2. Which LaTeX engine/workflow is the required path?
3. What is the smallest explicit shell vocabulary students need?
4. What can wrappers safely hide?
5. What recovery path exists when wrappers fail?
6. What must students understand conceptually about containers?
7. What minimum LaTeX features belong in the required vertical slice?
8. What artifact demonstrates reproducibility?
9. What is the Thursday Pair Reasoning experience?
10. Can a partner reproduce another student's artifact from documented instructions?

## Strong rule

Do not answer the Linux question ideologically.

Answer:

> **What is the smallest command-line understanding required to run, inspect, recover, and trust the environment we actually ask students to use?**

## Evidence expected from Foreman work

Prompt 307 should return an empirical student-path probe before this toolchain is frozen.

---

# 10. Decision cluster H: What should the grading model actually measure?

Do not change percentages yet merely because current source has percentages.

First decide the evidence model.

## Questions to decide

1. What unique dimension does Pair Reasoning assess?
2. What unique dimension does Show & Tell assess?
3. Is peer feedback a separate skill worth a separate grade object?
4. What does the weekly Reasoning Quest/Gate assess that other artifacts do not?
5. What makes a checkpoint larger/deeper than a weekly gate?
6. How does the World Bible contribute without becoming another grade stream?
7. What belongs in attendance/participation versus evidence-bearing work?
8. How much revision should be allowed/encouraged?
9. What late policy preserves learning without making deadlines meaningless?
10. What can safely be dropped/forgiven without breaking the reasoning trail?

## Anti-duplication rule

For every grade object, ask:

> **What evidence would disappear if this object were removed?**

If the answer is "none," the object probably does not deserve its own category.

---

# 11. Decision cluster I: What is the weekly authoring grammar?

Once the upstream decisions are made, later authors need a stable chassis so they do not redesign the course every week.

## Candidate weekly argument

> technical question -> formal ideas -> worked example -> challenge/test -> social reasoning -> evidence -> explanation/defense -> Odyssey update

## Candidate package

```text
week-NN/
  README.md
  tuesday.md
  thursday.md
  references.md
  reasoning-quest.md
  _instructor.md
  _validation.md
```

This is not yet doctrine.

## Questions to decide

1. What files are actually necessary?
2. Where do AI Fluency and Professional Minds bind in?
3. Where does the World Bible update live when relevant?
4. How is Pair Reasoning represented versus Show & Tell?
5. What validation receipt proves the week is coherent?
6. What student-like failure cases should be tested before release?

---

# 12. Decision cluster J: What does "done" mean for a DSCT week?

A week is not ready because Markdown exists.

## Candidate readiness dimensions

### Source coherence

- central question matches technical content
- activity matches reasoning target
- assignment/rubric matches actual work
- shared content provenance is correct

### Tool execution

- commands run
- container/LaTeX path works where relevant
- fallback path works
- no hidden paid/admin dependency

### Student reasoning

Rubric/Marker should distinguish examples such as:

- assertion with no evidence
- correct answer with invalid reasoning
- plausible but wrong reasoning
- test result that overclaims proof
- strong evidence with unjustified certainty
- honest uncertainty with good evidence boundaries
- strong reasoning that changes after counterevidence

### Social reasoning

Pair/Show prompts should produce evidence of challenge/revision rather than generic reflection prose.

## Question to decide

What is the smallest acceptance battery that reliably catches a weak week before it reaches students?

---

# 13. Questions that should probably wait for evidence already in flight

Do not spend expensive design time answering these before the relevant reports come back unless a decision becomes urgent.

## Wait for Prompt 305

- final artifact ontology
- Quest vs Gate naming/function
- duplicate homework risks

## Wait for Prompt 306

- final Week 2 bounded exercise
- what can be reused verbatim/pointer-based
- what is genuinely DSCT-specific

## Wait for Prompt 307

- Linux/shell requirement
- container runtime support posture
- LaTeX implementation choice
- wrapper/recovery balance

## Wait for Prompt 308

- final eleven-week intellectual spine
- exact reading/source slices

## Wait for Prompt 309

- World Bible carry-forward contract
- DSCT bootstrap path
- what continuity is already real versus aspirational

## Wait for Prompt 310

- exact reconciliation order across source files
- downstream Course Foundry/Savnac repair dependencies

---

# 14. Candidate refinement format for the next pass

When we refine this raw pile, each decision should become a compact decision card with:

```text
Decision ID:
Question:
Why it matters:
Already settled constraints:
Evidence available:
Evidence still pending:
Options:
Tradeoffs:
Jeremy + ChatGPT decision:
Consequences:
Files/prompts unlocked:
Verification that the decision was implemented correctly:
```

A decision should not become an implementation prompt until the `Jeremy + ChatGPT decision` field is explicit enough that the worker does not need to infer pedagogy.

---

# 15. Working priority when Jeremy + ChatGPT return to this pile

If no new evidence has arrived yet, the best discussion order is probably:

1. **Reasoning Odyssey / World Bible / weekly evidence ontology**
2. **Pair Reasoning versus Show & Tell contracts**
3. **eleven-week core-spine criteria and candidate compressions**
4. **Week 4 first Show & Tell problem**
5. **grading evidence model**
6. **weekly authoring grammar**

If Foreman reports arrive first, consume the relevant evidence before making the corresponding decision.

The goal is not to clear every question quickly.

The goal is to make each consequential decision once, make it legible, and then let implementation proceed without rediscovering the course philosophy.