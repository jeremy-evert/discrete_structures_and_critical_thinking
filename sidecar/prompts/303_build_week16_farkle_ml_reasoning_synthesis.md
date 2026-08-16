# Sidecar Prompt 303 - Build DSCT Week 16 Farkle + ML reasoning synthesis

**Status:** READY TO EXECUTE IN COORDINATION WITH `Farkle_and_Machine_Learning` PROMPTS 001/002  
**Repository:** `jeremy-evert/discrete_structures_and_critical_thinking`  
**Owner:** Foreman / DSCT worker  
**Mode:** inspect course contract -> inspect canonical shared Farkle package -> report -> map -> plan -> build DSCT-native Week 16 -> validate -> receipts -> postmortem

## Mission

Author the missing **DSCT Week 16 Farkle + Machine Learning synthesis experience** as a real, polished course week built against the canonical shared package in:

`jeremy-evert/Farkle_and_Machine_Learning`

DSCT is the first clean consumer of the shared repository. Do not copy the shared Farkle engine/learner/simulation machinery into this course unless a temporary provenance-pinned fallback is explicitly required by the shared-repo migration plan.

The DSCT Week 16 question is:

> **When a Farkle strategy appears better, what are we actually justified in believing?**

The desired student feeling is:

> I can use probability, simulation, algorithms, state models, and critical-thinking habits to decide what the evidence supports, what it does not support, and what decision I would defend anyway.

This is synthesis, not a new formal topic and not a second final project.

---

# Follow the development workflow

Use the course-development workflow deliberately:

1. **Look at what we have and make a report.**
2. **Look at what we want and make a map.**
3. **Create a plan document that builds on the report and map.**
4. **Break implementation into explicit work/acceptance checks if needed.**
5. **Implement while leaving raw receipts.**
6. **Write a postmortem.**

Apply:

> **Ask once: leave breadcrumbs. Ask twice: script it. Ask three times: automate it.**

If DSCT needs a repeated validation/synchronization action already used by other courses, consume or improve the shared script instead of writing another manual sequence.

---

# Read first: DSCT course truth

Read current:

- `README.md`
- `planning/fall-2026-course-design.md`
- `planning/fall-2026-spine.md`
- `planning/fall-2026-topic-map.md`
- `planning/fall-2026-weekly-architecture.md`
- current Week 1/Reasoning Odyssey evidence method
- current grading-model / Question 004-derived source truth
- relevant Week 9 Probability, Uncertainty & Evidence source if authored by execution time
- relevant Week 14 Finite-State Machines, Invariants & Model Limits source if authored by execution time
- any existing Week 16 files created after this prompt was authored

Record the exact DSCT commit inspected.

The authoritative spine currently contracts:

- Week 9: Probability, Uncertainty & Evidence;
- Week 14: Finite-State Machines, Invariants & Model Limits;
- Week 15: async buffer;
- Week 16: Farkle + Machine Learning synthesis;
- Week 17: Final Reflection.

Do not move those identities.

---

# Read the canonical shared package

Inspect current:

`jeremy-evert/Farkle_and_Machine_Learning`

including:

- Prompt 001 consolidation report/map/plan/results;
- Prompt 002 DSCT-first-clean-consumer report;
- canonical rules/engine;
- strategy contract;
- baseline human strategies;
- transparent learner;
- simulation/comparison semantics;
- experiment/result schema;
- seed-bundle/repeated-run support;
- raw result counts;
- plotting/evidence helpers;
- tests;
- validation command;
- technical instructor notes.

If shared Prompt 001/002 has not yet produced a usable canonical package, author the DSCT report/map/plan but do not invent a private DSCT fork to hide the dependency. Name the shared-package yellow and stop implementation at the correct boundary.

---

# Phase A - Current-state report

Write:

`sidecar/reports/303_week16_farkle_ml_current_state.md`

Document:

- DSCT Week 16 current authored state;
- authoritative Week 16 course contract;
- relevant prior-week concepts students should actually have by then;
- shared Farkle package status and commit;
- student/instructor artifacts that do not yet exist;
- grading/evidence constraints;
- dependencies and yellows.

Do not pretend source-pending Weeks 9/14 lessons are already taught if they are still not authored. Distinguish contracted curriculum from landed curriculum.

---

# Phase B - Target map

Write:

`planning/week-16-farkle-ml-target-map.md`

Map the synthesis back to the semester.

A strong mapping should include:

| Prior DSCT idea | Week 16 Farkle question |
|---|---|
| Logic / claims | What exactly is the claim: "A is better than B" in what sense? |
| Algorithms / correctness | Is the simulator implementing the claimed rules and comparison fairly? |
| Counting | What is the relevant sample space / how are cases represented? |
| Probability | What outcomes are random, conditional, independent, or not? |
| Expectation | What does expected score/value say that win rate does not? |
| Simulation | What can repeated simulated games estimate, and what can they not prove? |
| Relations/order | What ordering criterion makes one strategy "better"? Does another criterion reverse it? |
| Trees/decision structures | How can a decision policy represent future choices or tradeoffs? |
| Boolean/SAT checking habit | What counterexample or edge case would falsify the claim? |
| Finite-state models | What state does the strategy/model see? What state is omitted? |
| Model limits | What conclusion remains outside the model no matter how many games we simulate? |

Do not force every row into the student assignment. The map is an authoring tool for selecting the strongest synthesis threads.

---

# Central intellectual design

The Week 16 lab should make students distinguish at least four different questions that people casually collapse into "which strategy is best?"

## 1. Is the comparison fair?

Students inspect:

- same game rules;
- same target score;
- balanced starting positions;
- fixed strategy definitions;
- sufficient raw counts;
- seed/trial identity;
- no hidden change to the workload.

## 2. Is the observed difference stable?

Students compare repeated deterministic seed bundles and ask:

- Did A beat B once, or repeatedly?
- How much did the measured win rate move across bundles?
- Does the sign/order of the difference stay the same?
- Does increasing the number of games make the story more stable?

Do not teach "more trials automatically prove truth." Teach that more evidence can reduce sampling noise while assumptions/model limitations remain.

## 3. Is the difference meaningful?

A difference like 25.0% versus 25.3% may be real in one experimental sense and still be unimportant for a decision.

Ask students to state a **decision threshold before or alongside the evidence**, for example:

- choose the simpler strategy unless another improves win rate by at least X percentage points;
- choose the strategy that meets a target floor with the least training effort;
- choose the strategy whose advantage persists across all tested bundles;
- refuse to declare a winner when evidence is too unstable for the stated decision rule.

The point is not to prescribe one threshold. The point is to expose that "better" depends on a criterion.

## 4. What does the model not establish?

Students must identify at least one limitation such as:

- classroom Farkle variant differs from another house rule;
- strategy cannot observe a relevant feature;
- learner state omits total/opponent score;
- training on solo turns differs from learning full-game strategy;
- simulation covers a finite sample of random trajectories;
- chosen opponent/baseline changes what "good" means;
- target score is fixed at the classroom value;
- an observed win rate is not a proof of universal optimality.

---

# Student experience

Keep the required work humane and playful.

A good two-meeting Week 16 shape is:

## Tuesday - Make a claim, then try to break it

Use the recurring DSCT reasoning method:

**Sources -> Rules/Assumptions -> Work -> Check -> One-Sentence Summary**

Students:

1. play or inspect enough Farkle to understand the decision;
2. choose or receive two fixed shared-package strategies;
3. write a prediction/claim about which is better and define "better";
4. inspect the comparison contract and assumptions;
5. run an initial bounded experiment;
6. identify one plausible way the first result could mislead them;
7. leave a short Tuesday reasoning trace.

A useful Tuesday AI lens is:

> **What would a convincing but wrong claim about these results look like?**

Examples include gambler's-fallacy reasoning, treating one seed as proof, false independence, denominator blindness, or confusing a tiny numerical difference with a meaningful decision advantage.

## Thursday - Defend, revise, or refuse the conclusion

Students:

1. run/inspect several deterministic seed bundles or sample sizes;
2. preserve the raw evidence table;
3. compare stability/spread and at least one alternate metric if available;
4. identify one model limitation;
5. make a final decision under a declared criterion;
6. receive critique from a peer/pair;
7. revise the claim if necessary;
8. submit the individual evidence receipt.

The Thursday artifact can be a compact evidence table + graph/plot + defended conclusion rather than a conventional programming assignment.

---

# Evidence table / visualization

Use shared machine-readable receipts to produce a small DSCT-facing evidence table.

Minimum useful columns may include:

- seed bundle;
- games;
- wins A / wins B / ties;
- win rate A / B;
- percentage-point difference;
- starts A / B;
- relevant expected-score/value metric if shared package supports it;
- one stability/spread summary across bundles.

Provide one readable plot if it helps, such as:

- win-rate difference by seed bundle;
- measured win rate versus number of games;
- strategy comparison across several bundles.

Axes and denominators must be honest.

No dashboard is required.

---

# Probability and uncertainty scope

This is synthesis, not a new statistics unit.

Students may use descriptive ideas already available from prior weeks:

- frequency / proportion;
- expectation;
- conditional reasoning;
- independence assumptions;
- repeated simulation;
- range/spread/stability;
- base rates;
- sample-space reasoning.

Optional instructor enrichment may introduce a transparent bootstrap or confidence interval if the shared package and prior instruction make it genuinely useful.

Do not require formal hypothesis tests, p-values, normal approximations, calculus, or a statistics library.

---

# AI / critical-thinking connection

Week 16 should explicitly reinforce:

> **Love AI more. Trust AI less.**

A useful bounded activity is to give AI the raw experiment receipt and ask it for a conclusion, then have students audit the response for:

- unsupported causal language;
- hidden assumptions;
- denominator mistakes;
- overclaiming from one run;
- failure to mention model limits;
- treating the largest number as automatically "best";
- confident prose unsupported by the evidence.

AI use is optional on the zero-cost path if required access cannot be guaranteed. A pre-generated instructor example can provide the same critique task.

AI output is never the evidence.

---

# Required DSCT artifacts

Author a complete Week 16 package comparable in polish to the stronger sibling-course weeks, including at minimum:

- `planning/week-16.md` or the course-consistent Week 16 planning source;
- student Week-at-a-Glance / lesson;
- instructor guide;
- Reasoning Odyssey / evidence receipt;
- rubric or evidence criteria consistent with the existing grading model;
- shared-package invocation instructions;
- sample/fallback evidence table from deterministic shared fixtures;
- one plotting/view path if it materially helps the reasoning;
- DSCT validation script or, preferably, consumption of the shared validator plus a tiny DSCT wrapper if repetition requires it;
- raw validation receipt;
- postmortem.

Do not duplicate the shared engine, learner, simulator, or general experiment framework.

---

# Grading guardrails

Week 16 is a synthesis experience, not an invented fourth technical checkpoint or separate final.

Use the existing DSCT grading/evidence structure.

The individual reasoning receipt should make accountability visible even when evidence is gathered in pairs.

Do not invent a new grading percentage or due-date policy.

---

# Validation requirements

Before marking DSCT Week 16 GREEN, prove:

1. the shared package installs/runs or is otherwise consumable through the chosen Fall 2026 mechanism;
2. deterministic seed bundles reproduce the same raw counts;
3. different seed bundles can produce meaningfully different samples, demonstrating why one run is not the whole story;
4. fair-comparison starter balancing is visible;
5. raw denominators/counts survive into the DSCT evidence table;
6. at least one pair of strategies can be compared in bounded CPU time;
7. the student required path needs no GPU, paid AI, cloud account, or premium dependency;
8. fallback/sample evidence supports class discussion if live execution fails;
9. all student-facing paths resolve;
10. the lesson asks students to name a limitation and revise/defend a conclusion rather than merely report a winner.

Do not require one predetermined strategy to win.

---

# Raw receipts

Write validation/build receipts under:

`sidecar/runs/`

Record:

- DSCT commit;
- shared Farkle package commit;
- commands run;
- raw test/experiment outputs or artifact paths;
- runtime;
- pass/fail;
- named yellows;
- files changed;
- rollback notes.

---

# Postmortem

Write:

`sidecar/reports/303_week16_farkle_ml_postmortem.md`

Include:

- what was authored;
- how DSCT differs from CS1/CS2/Architecture;
- exact shared package consumed;
- which DSCT prior topics actually resurfaced;
- student burden/runtime;
- validation evidence;
- whether DSCT forced any useful change to the shared schema;
- named yellows;
- final commit SHA(s).

---

# Explicit non-goals

Do not:

- fork the shared Farkle implementation;
- teach formal reinforcement learning;
- teach a new statistics course in Week 16;
- build tournament infrastructure;
- require GPU/cloud/NRP;
- require paid AI;
- add a second final project;
- create a leaderboard as the learning objective;
- claim simulation proves universal optimality;
- make students write a large new program.

---

# Done when

DSCT Week 16 is a tested, joyful synthesis experience where Farkle provides the uncertainty and ML provides the tempting claim, but **reasoning decides what the evidence actually earns us the right to say**.

The shared repository owns the computational machine. DSCT owns the argument about what that machine's evidence means.

Then stop.
