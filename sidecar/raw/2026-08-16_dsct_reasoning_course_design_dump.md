# DSCT reasoning-course design dump

**Date:** 2026-08-16  
**Status:** RAW DESIGN QUARRY, NOT YET A COURSE CONTRACT  
**Purpose:** capture the current thinking in one place before slicing it into decisions, prompts, execution tasks, and Foreman work.

This file is intentionally fat. It is not a task list, not a final semester map, not a grading contract, and not a request to bulk-edit the repository. It exists so the next pass can cut clean pieces from one shared body of thought instead of reconstructing the design from chats, sibling repos, historical planning, and memory.

The working method from here is:

1. capture the design here;
2. read it back critically;
3. separate decisions from open questions;
4. turn decisions into a systematic work map;
5. split that map into Jeremy + ChatGPT design work versus bounded Foreman execution;
6. author small DSCT-owned prompts under `sidecar/prompts/`;
7. execute, validate, and reconcile source truth before Savnac deployment.

Do not treat this raw file as permission to silently mutate all existing DSCT planning files. Several current DSCT source files still reflect older decisions and must later be reconciled deliberately.

---

# 1. The center of the course

The strongest current identity for Discrete Structures and Critical Thinking is:

> **Reasoning is the work of the year.**

The course is not merely a list of discrete-mathematics topics. It is also not a conventional discrete-math course with a detached critical-thinking reading strand bolted onto the side.

The math is the vehicle. Critical thinking is the driving process.

A useful sequence-level framing remains:

- CS1 builds vocabulary.
- CS2 builds sentences.
- DSCT builds arguments.

The course should help students learn how a computer scientist knows when an idea deserves to be believed.

The north-star questions are:

> **What would it take to convince a skeptic?**

and

> **How would you reason with them?**

These are not decorative taglines. They should be visible in the structure of assignments, pair work, show-and-tell, source use, proofs, simulations, AI use, reflections, and grading evidence.

A student should finish the course better able to distinguish:

- a claim from evidence;
- evidence from interpretation;
- a valid argument from a true conclusion reached badly;
- a proof from a persuasive-looking explanation;
- a test that supports a claim from a test that overreaches;
- a model from the thing modeled;
- a source from a source-shaped object;
- a counterexample from an anecdote;
- confidence from certainty;
- something tested from something proved;
- a generated answer from a justified answer;
- what the evidence supports from what it does not prove.

---

# 2. Naming decision: Pair Reasoning is the standard

## DECIDED NOW

The standard name for the recurring pair activity in DSCT is:

> **Pair Reasoning**

Drop **Pair Programming** as the conceptual name for this course.

A pair activity may still include programming, a checker, a simulator, a proof assistant, a graph builder, a truth-table evaluator, a recurrence explorer, or another computational artifact. The code is an instrument. The work is reasoning.

The motivation is simple:

> It is no longer sufficient to write a program. We need reasoning. As steel sharpens steel, one reasoner sharpens another.

The pair structure should therefore be designed around intellectual friction, not just cooperative production.

A useful default Pair Reasoning pattern to test later is:

1. each student states an initial claim, approach, prediction, or interpretation;
2. each student explains why they currently believe it;
3. partners compare where their models differ;
4. each partner identifies the strongest part of the other's reasoning;
5. each partner challenges one assumption, inference, representation, or evidence boundary;
6. the pair looks for a counterexample, test, proof step, simulation, source, trace, or other discriminating evidence;
7. the pair records what changed and what did not;
8. each student individually records what they now believe, why, and what would still change their mind.

Pair Reasoning should not require disagreement for theater. If both reasoners agree, the work becomes testing whether the agreement is deserved.

If they disagree, the purpose is not to win. The purpose is to identify what observation, proof, definition, or assumption actually separates the positions.

## CURRENT SOURCE TO RECONCILE LATER

Current DSCT source still says `Pair Programming` in places including:

- `planning/fall-2026-weekly-architecture.md`
- `planning/fall-2026-topic-map.md`
- `docs/grading-model.md`

Do not patch those merely because this raw file exists. A later naming/reasoning-contract prompt should reconcile them coherently across planning, grading, rubrics, assignments, Course Foundry expectations, and Savnac objects.

---

# 3. Naming decision: Reasoning Odyssey is the persistent course spine

## DECIDED DIRECTION

The durable name is:

> **Reasoning Odyssey**

The older idea of a Coding Odyssey made sense when the central persistent work was primarily programming. The wider course sequence has matured. Reasoning is now the work that should persist across code, proofs, models, simulations, visualizations, systems, claims, and technical judgment.

In DSCT, a Reasoning Odyssey should not mean "complete an extra project every week." It should be the place where the student's reasoning becomes longitudinal and visible.

The weekly formal work, the Reasoning Quest/Gate, the World Bible, Pair Reasoning, and Show & Tell should be designed so they feed one coherent learning trail rather than competing as parallel homework systems.

A key future reconciliation question is vocabulary. We currently have historical/current terms such as:

- Reasoning Odyssey;
- Reasoning Quest;
- Reasoning Gate;
- weekly write-up;
- evidence receipt;
- Pair Reasoning reflection;
- Show & Tell reflection;
- World Bible.

We should not create five names for the same work.

The future design pass should define a small ontology, probably something like:

- **Reasoning Odyssey** = the semester-long intellectual journey/context;
- **World Bible** = the student's persistent living record/context within that journey;
- **Reasoning Quest/Gate** = the week's individual reasoning evidence package;
- **Pair Reasoning** = one social challenge mode;
- **Show & Tell** = one public explanation/challenge mode;
- **event reflection** = what changed when reasoning met other people.

That is only a candidate structure. The next pass should make it crisp enough that students and agents cannot confuse the objects.

---

# 4. The World Bible should follow the student through CS1, CS2, and DSCT

## STRONG DIRECTION

The World Bible is worth preserving as a recognizable cross-course artifact family.

Its original strength is personalization. Instead of every student experiencing the course as the same sterile sequence of toy problems, the student can maintain a world, system, organization, scenario, domain, or problem space that becomes increasingly theirs.

The World Bible should not mean mandatory fiction.

A "world" can be:

- a frontier settlement;
- a detective bureau;
- a starship;
- a small business;
- a campus system;
- a sports league;
- a scheduling problem;
- a network;
- a game;
- a security scenario;
- a decision process;
- a scientific or social system;
- another bounded context that helps the student care about the reasoning.

## Cross-course progression

### CS1

The World Bible can be primarily about ownership and identity:

- what is my world?
- what exists in it?
- what did I build this week?
- what broke?
- what changed?
- what am I proud of?

### CS2

The World Bible can mature into design and engineering judgment:

- current state;
- design decisions;
- tests/evidence;
- known debt;
- changes and recovery;
- interfaces/contracts;
- what proposal was accepted or rejected and why.

### DSCT

The World Bible can mature again into a reasoning history:

- claims I currently believe;
- definitions I am using;
- assumptions;
- examples/counterexamples;
- sources that informed the claim;
- proof/test/simulation/model evidence;
- uncertainty;
- confidence;
- what changed my mind;
- what survived challenge;
- what stronger claim I am not justified in making;
- what would change my mind next.

This is a beautiful sequence because the same basic habit becomes more intellectually demanding as the student advances.

## Literal carry-forward versus family resemblance

Open design question: should a student literally carry the same World Bible from CS1 into CS2 and DSCT, or should each course create a new course-native World Bible with an optional import/carry-forward path?

Strong recommendation for later discussion:

- preserve the **same recognizable artifact family**;
- allow students to carry a prior world forward when it remains useful;
- do not make prior enrollment a hidden prerequisite;
- transfer/new students must be able to bootstrap an equivalent World Bible in Week 1/2;
- do not force an old world into a DSCT topic when the connection becomes artificial.

The current DSCT planning already contains a healthy version of this idea: a carried world/system can provide context when useful, but a formal topic must stand on its own when the connection would be fake.

## World Bible as evidence of change, not revisionist history

A key lesson from Computer Architecture's Machine Dossier is that we should preserve earlier judgments rather than rewriting history to make the student look smarter later.

The DSCT World Bible could contain selected "claims waiting to be attacked."

For a meaningful claim, students might later mark it as:

- preserved;
- revised;
- corrected;
- narrowed;
- rejected;
- unresolved.

The exact vocabulary is not decided. The important mechanism is longitudinal epistemic honesty.

The student should be able to look back and say:

> I believed this. Here is why. Then this evidence arrived. Here is what changed.

That is a far richer indicator of learning than a clean final answer with the intellectual history scrubbed away.

---

# 5. The recovered DSCT five-move reasoning DNA

A powerful historical sequence should remain central:

1. **Name the Problem**
2. **Consult the Mapmakers**
3. **Find the Fog**
4. **Build the Bridge**
5. **Test the Bridge**

This is better than a generic "show your work" instruction because each move names a different reasoning responsibility.

## Name the Problem

What is actually being claimed or asked?

What kind of question is this?

What terms need definition?

What would count as an answer?

What is in scope and out of scope?

## Consult the Mapmakers

What is already known?

Who has mapped this territory?

What definitions, theorems, examples, specifications, prior work, or reliable sources apply?

Which sources are primary, explanatory, or merely convenient?

## Find the Fog

Where is the uncertainty?

What assumptions are hidden?

What distinctions are being blurred?

Where could a counterexample live?

What does the available evidence fail to establish?

What could a convincing wrong answer look like?

## Build the Bridge

Construct the actual reasoning.

Depending on the week, this may be:

- a proof;
- a counterexample;
- a formal derivation;
- a model;
- an algorithm;
- a checker;
- a simulation;
- a trace;
- a graph;
- a table;
- a visualization;
- a source synthesis;
- a paired argument;
- a bounded experiment.

## Test the Bridge

Attack the answer.

Check edge cases.

Try a counterexample.

Run the model.

Compare with a definition.

Ask another reasoner.

Verify an AI claim independently.

State what the evidence supports and what it does not prove.

Revise if required.

Then answer:

> What would increase my confidence?

and

> What would change my mind?

---

# 6. The best cross-course theft: combine CS2 social reasoning with Architecture experimental reasoning

The sibling-course pass exposed an important design opportunity.

CS2 and Computer Architecture have independently developed complementary parts of the reasoning course we want.

## CS2 contributes the social/judgment machinery

### AI proposal versus evidence loop

CS2 uses a strong recurring pattern:

> **baseline -> bounded proposal -> diff -> independent test -> read/reason -> accept or reject from evidence**

This is especially strong because it separates generation from verification.

A model can produce a proposal. A proposal is not evidence that the proposal is correct.

This should be central in DSCT Week 2 and remain available throughout the course whenever students use AI.

### Pair work as visible judgment

CS2's pair artifact already asks students to explain:

- the problem;
- their approach;
- what changed;
- how it was tested/traced;
- what they personally contributed;
- what they learned or changed after discussion;
- how AI help was verified.

DSCT should adapt this away from programming contribution and toward reasoning contribution.

### Own-work reflection separate from peer feedback

CS2 wisely distinguishes:

- reflection on my own demonstration;
- feedback I gave someone else.

That is a valuable distinction for DSCT.

A Show & Tell reflection can ask what happened to my reasoning when I had to defend it.

A peer-feedback artifact can ask whether I could inspect another person's argument generously but critically.

If grading bandwidth permits both, they serve different learning goals.

## Computer Architecture contributes the experimental/epistemic machinery

### Sensory experiment grammar

Architecture's reusable grammar is:

> **Predict -> Perturb -> Run -> Measure -> Visualize -> Explain -> Revise**

For DSCT, "Perturb" can be generalized beyond hardware:

- change an assumption;
- alter an input;
- vary a parameter;
- search for a counterexample;
- change one graph edge;
- alter a sample-space condition;
- change a recurrence base case;
- vary a simulation rule;
- test another representation;
- attack a proof step;
- introduce an adversarial case.

Not every DSCT claim should be tested empirically. Some require proof. Some require definition analysis. Some require source criticism. Some require social challenge.

The value of this grammar is not that every week becomes a lab. The value is that when a claim can be challenged computationally or experimentally, students have a disciplined method.

### Evidence-boundary discipline

Architecture repeatedly asks students not only what evidence supports, but what it does not establish.

This should be a first-class DSCT expectation:

> **What does your evidence justify, and what stronger claim would exceed it?**

This is one of the cleanest bridges between discrete mathematics and Critical Thinking.

Examples:

- a million successful simulations do not prove a universal theorem;
- one counterexample can disprove a universal statement;
- a proof under assumptions does not establish the conclusion when the assumptions fail;
- a visualization can reveal a pattern without explaining its cause;
- a passing test supports tested behavior, not every possible behavior;
- a model can be internally correct while representing reality badly;
- a source can accurately report an observation without justifying the interpretation attached to it.

### Explain / Defend receipt

Architecture's compact receipt is highly reusable:

1. bounded claim/answer;
2. evidence that matters;
3. mechanism or reasoning connecting evidence to the claim;
4. limitation, including what the evidence does not prove;
5. revision after evidence;
6. AI/tool contribution plus independent verification when relevant.

This may fit naturally inside the DSCT Reasoning Quest rather than becoming a separate assignment.

### Prior belief and pre-test prediction

Architecture requires a prior belief and prediction before evidence arrives.

That matters because hindsight is cheap.

DSCT should consider making students state, when appropriate:

- what do I currently think?
- why?
- how confident am I?
- what would I expect to observe if I am right?
- what result would force me to revise?

Then the student confronts evidence and updates.

This turns "reflection" into calibration rather than memoir.

---

# 7. A candidate unified DSCT reasoning grammar

This is not yet a final rubric. It is a synthesis worth testing.

## Before evidence

1. **Name the Problem**
2. **Consult the Mapmakers**
3. **Find the Fog**
4. record a prior belief/prediction where meaningful;
5. state assumptions and initial confidence.

## Challenge the claim

6. **Build the Bridge** with the method appropriate to the question;
7. if empirical/computational testing fits, use **Predict -> Perturb -> Run -> Measure -> Visualize**;
8. if proof fits, identify assumptions, logical steps, and possible counterexamples;
9. if source analysis fits, compare source quality, scope, and disagreement;
10. if social challenge fits, expose the reasoning through Pair Reasoning or Show & Tell;
11. if AI contributes, preserve the proposal/evidence distinction.

## After evidence

12. **Test the Bridge**;
13. state what the evidence supports;
14. state what the evidence does not prove;
15. identify the strongest remaining counterargument, uncertainty, or model limitation;
16. revise/correct/narrow/preserve the claim;
17. update confidence;
18. answer what would change my mind next;
19. answer what it would take to convince a skeptic.

This grammar should be compact enough that it becomes habitual rather than exhausting.

The future rubric-design pass should resist turning every bullet into a separate scored criterion. The goal is cognitive structure, not a 19-row bureaucratic monster.

---

# 8. Week 2 is Building Your AI Lab

## DECIDED NOW

The current intended DSCT Week 2 identity is:

> **Building Your AI Lab**

Week 2 should not independently reinvent content that already exists in CS2 and shared repositories.

The first sources to bounce against are:

- `jeremy-evert/local_ai_lab_setup`
- `jeremy-evert/windows_classroom`
- `jeremy-evert/computer_science_2` Week 2 integration material
- Computer Architecture Week 2's epistemic framing

## What CS2 already has that DSCT can reuse

CS2 already has a mature ownership contract:

- `local_ai_lab_setup` owns canonical shared instructional content and readiness material;
- `windows_classroom` owns the tested Windows execution harness;
- the course repo owns sequencing, purpose, and course-specific extension.

CS2's proven student loop is approximately:

1. understand the system model;
2. `Check` readiness;
3. observe a known failing `Baseline`;
4. make one bounded Aider-assisted proposal;
5. inspect the `Diff`;
6. run an independent `Final` test;
7. read/reason;
8. accept or reject from evidence;
9. preserve a readiness/reflection receipt.

The exact CS2 `format_student_name` exercise is not automatically DSCT doctrine.

What should be stolen first is the **structure** and the **evidence discipline**.

## What Architecture adds to Week 2

Architecture frames its AI Lab around the question:

> How can AI help me investigate a machine without becoming my source of truth?

The reusable intellectual structure is:

- question/hypothesis;
- context;
- AI/tool used;
- observation;
- evidence artifact;
- conclusion;
- revision after verification.

That is extremely compatible with DSCT.

## Candidate DSCT-specific Week 2 purpose

A possible DSCT Week 2 question is:

> **How can AI help me reason without becoming my source of truth?**

Students should leave Week 2 with a working local lab and a first experience of using AI as a proposal engine whose claims are independently checked.

The lab is not the intellectual endpoint. The endpoint is a habit:

> fluent output is not evidence.

## Candidate Tuesday / Thursday shape

Not yet a contract, but a promising direction:

### Tuesday

- AI Fluency/shared strands;
- understand local system roles: PowerShell, Python, Git, Ollama, Aider, localhost/API/client-server;
- run readiness checks;
- perform one bounded AI-assisted change;
- inspect the diff;
- independently test;
- introduce evidence boundaries.

### Thursday

- Professional Minds/shared strand;
- **Pair Reasoning**, not Pair Programming;
- partners inspect each other's evidence chain or reason through a bounded lab failure/claim;
- individual receipt records what changed after another reasoner challenged the explanation;
- Week 2 Reasoning Quest is a confidence beacon that the lab works and the student can defend what they know about it, not a giant setup report.

---

# 9. Week 3 is Containers + LaTeX

## DECIDED DIRECTION

The current intended Week 3 runway is:

> **Containers + minimum-useful LaTeX**

Formal DSCT core should begin after this runway, in Week 4.

## Why LaTeX belongs here

Discrete mathematics is one of the most natural homes in the curriculum for LaTeX because students need to communicate:

- equations;
- logic notation;
- sets;
- relations;
- proofs;
- recurrences;
- tables;
- graphs/figures;
- citations;
- structured technical reasoning.

The goal is not to create a TeX wizardry side course.

LaTeX should be an instrument for clear mathematical and technical communication.

A minimum useful vertical slice might be:

1. open a provided `.tex` source;
2. edit title/text/sections;
3. write a small amount of mathematical notation;
4. include a table or figure when appropriate;
5. compile reproducibly;
6. obtain a readable PDF;
7. use that format later for selected Reasoning Odyssey artifacts.

Architecture's Machine Dossier work reinforces a useful principle:

> LaTeX and Python are instruments. The evidence and explanation earn the grade.

The same should hold here.

## Why containers belong here

Containers are valuable not because students need Docker trivia, but because DSCT benefits from reproducible computational reasoning.

A container can give the class a shared environment for:

- Python;
- LaTeX/Tectonic/latexmk;
- graph tools;
- small simulations;
- checkers;
- course-owned scripts;
- reproducible examples;
- later Farkle/ML work where useful.

Container Foundations already has patterns/templates worth reusing rather than reinventing.

## OPEN QUESTION: how much Linux command line is actually necessary?

Do students need to "know Linux" to use containers successfully?

Probably not in the sense of taking a Linux command-line mini-course.

They may, however, need enough shell literacy to understand what is happening when the happy path breaks.

Possible approaches to evaluate later:

### Option A: wrappers hide almost everything

Provide PowerShell/Make/task wrappers such as:

- `./classroom check`
- `./classroom build`
- `./classroom run`
- `./classroom reset`

or equivalent Windows-friendly commands.

Students learn the conceptual container model, not command trivia.

### Option B: teach a tiny survival vocabulary

Only the handful of commands genuinely needed to navigate/recover:

- where am I?
- what files are here?
- change directory;
- inspect a file;
- run a supplied command;
- read an error;
- rerun/reset.

This is command-line literacy, not a Linux unit.

### Option C: local AI helps translate/recover

Students can ask their local model to explain commands and errors.

This is attractive, but the course should not make AI the only recovery path. If the model confidently suggests destructive or irrelevant commands, students need enough context to recognize that the suggestion still requires verification.

### Design principle

Do not decide this from intuition alone.

Before final Week 3 authoring, test the actual container + LaTeX path with student-like users and observe what shell knowledge is genuinely required.

The question is not:

> Should students learn Linux because Linux is good?

The question is:

> What is the smallest command-line understanding required to run, inspect, recover, and trust the reproducible environment we actually ask them to use?

Keep this open until the environment is tested.

## Candidate Week 3 Pair Reasoning experience

A powerful possibility is to make reproducibility social.

One student produces a small containerized LaTeX artifact or supplied exercise.

The partner attempts to reproduce it using the documented path.

The pair reasons about:

- what assumptions the instructions made;
- what failed;
- whether the failure is environment, command, source, or reasoning;
- what evidence demonstrates reproducibility;
- what the successful compile does and does not prove.

This would make containers serve the Critical Thinking mission rather than becoming infrastructure trivia.

---

# 10. Current semester shape and a major reconciliation problem

## LATEST INTENDED SHAPE

- Week 1: compressed Semester Kickoff Week
- Week 2: Building Your AI Lab
- Week 3: Containers + minimum-useful LaTeX
- Weeks 4-14: legitimate DSCT technical core
- Week 15: asynchronous Thanksgiving/Mexico travel buffer
- Week 16: existing GREEN Farkle + Machine Learning synthesis
- Week 17: individual final reflection/closeout

## CURRENT SOURCE CONFLICT

Current DSCT main still reflects an older contract in which:

- Week 2 combines Building Your AI Lab with Containers and Repeatability;
- Week 3 begins formal DSCT with Logic, Claims & Proof;
- Weeks 3-14 contain twelve formal DSCT topic weeks;
- `Pair Programming` is the pair-activity name.

The latest design gives Weeks 4-14 only **eleven** formal DSCT weeks.

The current topic map contains **twelve** formal topics:

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

Something must therefore be combined, reframed, moved, or narrowed.

Do not solve that accidentally while doing Week 2/3 work.

It needs a deliberate intellectual-spine pass after the source harvest.

Possible combination questions to investigate later, without deciding now:

- Can sets/functions and relations be arranged as one broader representation week without becoming overloaded?
- Can trees live naturally inside the graph week, freeing a week while preserving catalog coverage?
- Can algorithms/correctness become a recurring reasoning lens rather than a standalone week?
- Should logic/proof occupy more than one week because it is foundational to the skeptic question?
- Can Boolean/SAT and finite-state systems be connected without shortchanging either?

The source harvest and catalog requirements should constrain this decision.

---

# 11. Tuesday / Thursday course rhythm

The T/Th chassis remains a strong direction, but it needs naming and runway updates.

## Tuesday: Learn + Build

Candidate stable functions:

1. AI Fluency touchpoint
2. Professional Minds Wednesday strand
3. real DSCT technical lecture
4. guided example/demo/application
5. short reasoning trace, prediction, or exit

Tuesday must remain a real technical class.

The course should not become a playlist of external links plus Thursday activities.

## Thursday: Think + Defend

Candidate stable functions:

1. Professional Minds Friday strand
2. Pair Reasoning **or** Show & Tell
3. applied/social reasoning work
4. individual critique/revision/evidence receipt

## Runway exception

Weeks 2 and 3 should probably use **Pair Reasoning on both Thursdays** because the class is still learning the lab/reproducibility/reasoning machinery.

## Formal-core cadence

The latest recovered direction for Weeks 4-14 is:

- odd weeks: Pair Reasoning
- even weeks: Show & Tell

That creates an immediate question for Week 4, the first core week and an even week:

> What exactly does the first Show & Tell synthesize now that Week 3 is Containers + LaTeX rather than a formal DSCT topic?

Do not hand-wave this. Week 4 Show & Tell must have something worth publicly defending.

Possible answers can be generated later, but the final decision should be deliberate.

---

# 12. Pair Reasoning and Show & Tell should challenge different dimensions

If both remain in the course, they should not be two names for "talk to someone about your homework."

## Pair Reasoning candidate purpose

Pair Reasoning is intimate adversarial collaboration.

The student puts reasoning beside another reasoner's reasoning and tests the seams.

Questions might include:

- Where do our assumptions differ?
- Which definition are we using?
- What is the strongest counterexample?
- Which step is doing the real work?
- What evidence would discriminate between our claims?
- Did one of us change our mind?
- If neither changed, did we earn the agreement?

## Show & Tell candidate purpose

Show & Tell is public explanation and defense.

The student must make a claim/model/proof/simulation understandable enough that other people can interrogate it.

Questions might include:

- What am I claiming?
- What is my strongest evidence?
- What assumption should the audience challenge?
- What is the most likely overclaim?
- What question from the audience exposed something I had not considered?
- What did I revise afterward?

## Peer feedback candidate purpose

If a separate peer-feedback artifact survives the grading design, it should assess the reasoner's ability to examine someone else's reasoning.

A compact DSCT feedback pattern could be:

1. strongest supported part;
2. weakest inference or least-supported assumption;
3. one counterexample/question;
4. one additional test/source/proof move that could raise confidence.

This should be generous and specific, not debate-club point scoring.

---

# 13. Critical Thinking should be visible in actions, not only readings

Professional Minds and critical-thinking readings can provide language, examples, cognitive-bias awareness, argument structures, and reflection prompts.

But the Critical Thinking part of DSCT is successful only if students repeatedly **do** things such as:

- define terms;
- separate claims from evidence;
- state assumptions;
- test edge cases;
- find counterexamples;
- distinguish validity from truth;
- inspect denominators/base rates;
- challenge independence assumptions;
- compare representations;
- check whether a model omitted important structure;
- reason about uncertainty;
- identify evidence boundaries;
- calibrate confidence;
- change their mind when evidence earns the change;
- defend a claim to another human;
- explain what would change their mind next.

A future week-map pass should pair every discrete-structures topic with a characteristic Critical Thinking move.

Examples already visible in current planning include:

- logic -> validity/soundness and unjustified steps;
- sets/functions -> representation and hidden domain changes;
- algorithms -> tests versus correctness proof;
- crypto -> attacker assumptions and security overclaim;
- induction -> missing base cases and circular reasoning;
- counting -> double counting and non-exhaustive partitions;
- probability -> base rates, independence, simulation overclaim;
- relations -> claiming equivalence/order when properties fail;
- graphs -> solving the graph correctly while modeling reality incorrectly;
- trees -> hierarchy erasing relevant relations;
- Boolean/SAT -> equivalence versus satisfiable versus universally true;
- finite-state systems -> omitted states/transitions and model limits.

This woven pattern is worth preserving even if the exact week allocation changes.

---

# 14. Resource philosophy: buy a book only when a book earns its place

## DECIDED PHILOSOPHY

If students genuinely need to buy a book, they buy one.

If they do not need to buy a book, do not replace one commercial textbook with one arbitrary free textbook just to preserve the appearance of a textbook-driven course.

Instead, curate a catalog of the best parts of the best resources available and expose students to the most useful pieces, tied together by coherent course-owned instruction.

The external resources are ingredients.

The course is the sauce that makes the ingredients belong together.

## Architecture's resource labels are worth stealing

Candidate labels for the DSCT source harvest:

- **PRIMARY** - official/specification/normative truth layer where applicable;
- **ADAPT** - reusable/adaptable material with a compatible license and attribution requirements;
- **LINK** - valuable public material that should be linked rather than copied/adapted;
- **TOOL** - official documentation/software/tooling;
- **CURRENT EVIDENCE** - time-sensitive observations/data that must be date-stamped rather than frozen into doctrine.

For DSCT, another useful label might be:

- **EXPLANATION** - excellent pedagogical explanation that is not itself the primary truth source.

The exact taxonomy can wait for the source-harvest prompt.

## Candidate source-card fields

Each Week 4-14 source card could contain:

- technical concept;
- Critical Thinking move;
- best open reading;
- primary/authoritative truth source where applicable;
- alternate explanation;
- short video/demo;
- hands-on/computational activity;
- coding/simulation bridge;
- proof/counterexample bridge;
- AI-verification angle;
- licensing/reuse posture;
- accessibility considerations;
- why this source earned a place;
- what part of the source we specifically want students to use;
- what we intentionally do **not** ask students to consume;
- course-owned connective tissue needed.

This avoids "read Chapter 7" as the default instructional primitive.

## Known source families worth harvesting later

Without treating this raw list as final verification:

- MIT OpenCourseWare Mathematics for Computer Science;
- Oscar Levin, *Discrete Mathematics: An Open Introduction*;
- Matthew Van Cleave, *Introduction to Logic and Critical Thinking*;
- Open Logic Project;
- SWOSU-owned materials;
- strong public university course notes;
- official tool/documentation sources;
- a small number of excellent public talks/videos/demos;
- possibly one strategically chosen TED talk;
- possibly one LinkedIn Learning item when it genuinely adds value and student access is appropriate.

The later source-harvest job should verify availability, licensing, quality, accessibility, and current URLs before authoring.

---

# 15. LaTeX, containers, and the course toolchain should serve reasoning

The course should resist tooling becoming identity.

Students are not in DSCT to become:

- Docker specialists;
- Linux shell specialists;
- TeX package specialists;
- matplotlib syntax specialists;
- AI prompt technicians.

Those can all be useful instruments.

The learning target is reasoning.

A useful toolchain principle is:

> Provide enough scaffolding that students spend their cognitive budget on the claim, model, proof, evidence, and explanation rather than environment archaeology.

At the same time, scaffolding should not make the environment a magic box that students cannot inspect or recover.

That tension should be tested, not philosophized away.

## Candidate reproducible DSCT workbench

A future implementation might evaluate a course-owned container with:

- Python;
- selected math/graph libraries;
- a lightweight LaTeX path such as Tectonic or latexmk;
- course templates;
- plotting helpers;
- small verification scripts;
- stable input/output directories;
- simple Windows-friendly wrappers.

This is not a decision to build that exact stack. It is a direction to test.

The success criterion is not "container starts."

The success criterion is:

> A normal student can create, inspect, rerun, share, and recover a small reasoning artifact without the toolchain becoming the assignment.

---

# 16. AI posture across the course

The course should be aggressively AI-literate without confusing AI output with truth.

Useful recurring doctrine:

> **Love AI more. Trust AI less.**

AI can help students:

- generate examples;
- generate counterexamples to test;
- propose proof approaches;
- explain a definition another way;
- build small checkers;
- generate test cases;
- suggest model structures;
- find questions to ask;
- critique prose;
- explore source vocabulary;
- debug tooling;
- compare interpretations.

AI cannot be treated as evidence merely because it is fluent.

When AI materially contributes, the student should be able to distinguish:

1. what the AI proposed;
2. what changed because of the proposal;
3. what independent evidence was used;
4. what the student personally concluded;
5. why the proposal was accepted, revised, or rejected.

No required paid AI subscription should create a higher attainable grade ceiling.

The local Week 2 lab is valuable precisely because it gives every student a concrete AI system they can interrogate without making a commercial provider the curriculum.

---

# 17. Reasoning Odyssey and the weekly Quest should not become duplicate homework

This is a major design constraint.

The weekly Reasoning Quest/Gate should be the evidence package for the week's real intellectual work, not an essay appended after the work.

A good gate may include:

- the actual proof/model/code/simulation/table/graph;
- the relevant evidence;
- a compact explanation;
- a World Bible update where useful;
- a Pair Reasoning or Show & Tell insight where applicable.

The persistent Odyssey should provide continuity, not another gradebook.

The World Bible should preserve useful context, not require a ceremonial entry every week when nothing meaningful changed.

Pair Reasoning and Show & Tell reflections should capture the social change in reasoning, not restate the Quest.

The guiding anti-bureaucracy question should be:

> Is this object exposing a different dimension of reasoning, or are we asking the student to tell us the same thing again?

---

# 18. Candidate Reasoning Quest evidence fields

This list is deliberately larger than a future student template should be.

Possible fields to test:

- bounded question/claim;
- definitions;
- sources/mapmakers;
- assumptions;
- starting prediction;
- starting confidence;
- strongest alternative/counterexample;
- proof/model/computation/simulation/trace;
- test/check;
- result;
- warrant: why this evidence bears on the claim;
- what the evidence supports;
- what it does not prove;
- revision after evidence;
- final confidence;
- unresolved uncertainty;
- what would change my mind;
- AI/tool contribution and independent verification;
- one-sentence conclusion.

The future design pass should compress these into a student-friendly structure tied to the five-move DNA.

One possible destination is that the five moves remain the visible headings, while the richer evidence-boundary/confidence questions live inside them.

---

# 19. Grading implications to revisit later

Current DSCT main has a 100% grading model with named categories inherited from CS1/CS2, including:

- a `Paired-programming report` category;
- Show & Tell reflection;
- Friday feedback report;
- weekly Reasoning Odyssey gate;
- Reasoning Odyssey checkpoints;
- final reflection;
- shared strands and other recurring categories.

This file does **not** change those weights.

Future reconciliation needs to ask:

1. rename Pair Programming to Pair Reasoning everywhere;
2. determine whether pair reflection and Show & Tell reflection remain distinct 5% groups or should be shaped differently;
3. determine whether peer feedback remains a separate graded category;
4. ensure the weekly Quest/Gate is not duplicate work;
5. decide checkpoint weeks after the Week 4-14 spine is frozen;
6. decide due windows, revision, late work, and drop-lowest behavior;
7. keep Week 17 low-stress and reflective;
8. keep the course free of a comprehensive programming exam;
9. ensure Week 16 Farkle remains the already-validated synthesis experience rather than being casually redefined as another checkpoint;
10. ensure every grading object measures reasoning that actually belongs in the course.

No grading decision should be made merely because a sibling course uses that percentage.

---

# 20. Architecture's authoring workbench is worth adapting

Computer Architecture learned that a technical week works better when the entire week's argument stays coherent.

Its pattern is roughly:

- week overview/question;
- teaching/model;
- experiment/investigation;
- Explain/Defend receipt;
- references;
- instructor notes;
- validation.

DSCT should consider an analogous weekly authoring package.

The exact repository layout need not match Architecture, but each week should be traceable as one argument:

> **technical question -> formal ideas -> worked example -> test/challenge -> social reasoning -> evidence -> explanation/defense -> Reasoning Odyssey update**

A future DSCT weekly template might include:

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

This is only a candidate.

The deeper lesson to steal is that later week authors should not have to re-decide basic course grammar every time.

Freeze a small authoring grammar, pilot one week, validate it, then scale.

---

# 21. Validation should include actual student-like reasoning, not only file checks

A week is not ready because Markdown exists.

Future DSCT validation should test at least four layers:

## Source coherence

- central question is consistent;
- technical lecture matches the activity;
- activity matches the Quest/rubric;
- shared strands are correctly sourced;
- no stale ZyBooks requirements leak through;
- no old Pair Programming name remains after migration;
- dates/calendar exceptions are correct.

## Tool execution

- commands run on the actual intended environment;
- container path works;
- LaTeX compiles;
- supplied scripts run;
- fallbacks work;
- errors are recoverable;
- no hidden admin/premium dependency exists.

## Student reasoning

Use synthetic/bounded student personas to submit examples such as:

- assertion with no evidence;
- plausible but wrong reasoning;
- invalid counterexample;
- successful test that overclaims universality;
- strong evidence with too-high confidence;
- correct answer with invalid reasoning;
- incomplete but intellectually honest submission;
- strong submission that states evidence boundaries.

Then prove the rubric/Marker/Coach behavior distinguishes them appropriately.

## Social activity

For Pair Reasoning and Show & Tell, validate that the reflection prompts actually capture a change or challenge in reasoning rather than produce generic "I learned a lot" prose.

---

# 22. Week 15, Week 16, and Week 17 boundaries

## Week 15

Asynchronous travel/Thanksgiving buffer.

Do not invent a fake formal DSCT topic just because there is a module slot.

The work should be purposeful, lightweight, and navigable without live instructor presence.

Possible roles to decide later:

- catch-up;
- curation of the World Bible/Reasoning Odyssey;
- source/evidence cleanup;
- preparation for Week 16;
- professional artifact;
- no new high-stakes reasoning demand.

## Week 16

Farkle + Machine Learning is already GREEN and should not be casually rewritten.

Its central epistemic question is already excellent for DSCT:

> When a Farkle strategy appears better, what are we actually justified in believing?

It naturally exercises:

- probability;
- simulation;
- uncertainty;
- repeated trials;
- model limits;
- deterministic seeds;
- comparison;
- overclaim avoidance;
- evidence boundaries.

Integrate it into the semester grammar without rebuilding it.

## Week 17

Final individual reflection/closeout.

The student should use prior evidence, including the World Bible/Reasoning Odyssey, rather than complete a new feature sprint or technical final.

Strong reflection prompts from sibling courses suggest questions such as:

- What can you reason about now that you could not before?
- Which belief, model, proof habit, or assumption changed most?
- Which mistake taught you the most?
- When did evidence force you to reject a persuasive story?
- Which claim survived repeated attack?
- How did another reasoner sharpen your thinking?
- How did AI help, and when did you have to reject it?
- What does "convince a skeptic" mean to you now?
- What would you preserve or redesign in your own reasoning process?

---

# 23. Equity and access doctrine

The required course path should not reward students for owning better tools.

A student on the required free/accessible path should be able to earn the same grade ceiling as a student with:

- paid ChatGPT/Claude/Codex/Copilot/etc.;
- a personal GPU;
- a powerful home workstation;
- premium SaaS;
- private infrastructure;
- advanced Linux experience.

Premium tools may improve convenience or provide optional enrichment.

They should not create additional attainable points.

For computational experiments, if a student's machine cannot support a measurement or tool reliably, provide course-owned fallback data/trace/environment that preserves the reasoning objective.

The grading target is the reasoning, not the machine.

---

# 24. Things we should explicitly avoid

Do not let DSCT become:

- a Rosen/ZyBooks chapter march with Critical Thinking commentary;
- a collection of unrelated OER links;
- a programming course with math vocabulary;
- a proof course that never lets students test claims computationally;
- a simulation course that mistakes repeated trials for proof;
- a debate course where rhetorical confidence beats evidence;
- an AI prompting course;
- a Linux course;
- a Docker course;
- a LaTeX course;
- a weekly worksheet factory;
- a giant semester project that hides weak weekly reasoning;
- a rubric bureaucracy in which students answer nineteen reflection questions every week;
- a course where Pair Reasoning means two people silently typing beside one another;
- a course where Show & Tell is presentation theater;
- a course where the World Bible becomes compulsory fiction;
- a course where old source history silently overrides current intent.

---

# 25. Current repository seams to remember for the slicing pass

The next systematic pass should inspect and reconcile at least:

- `planning/fall-2026-spine.md`
- `planning/fall-2026-weekly-architecture.md`
- `planning/fall-2026-topic-map.md`
- `planning/fall-2026-course-design.md`
- `docs/grading-model.md`
- existing assignments/rubrics using Pair Programming / A3-equivalent naming
- existing Reasoning Odyssey / World Bible surfaces
- Week 2 work on historical incoming branches
- Week 16 validated package
- Course Foundry DSCT compiler expectations
- shared AI Fluency sources
- shared Professional Minds sources
- `local_ai_lab_setup`
- `windows_classroom`
- Container Foundations / container curriculum
- sibling CS2 reasoning artifacts
- sibling Computer Architecture authoring/evidence patterns

Important known seams:

1. Pair Programming naming is stale against the new Pair Reasoning decision.
2. Current Week 2/3 calendar contract is stale against the new Week 2 AI Lab / Week 3 Containers + LaTeX runway.
3. Current Weeks 3-14 map has twelve formal topics, but new Weeks 4-14 core has eleven slots.
4. Current grading model may contain good weights but stale naming and unresolved due/revision/checkpoint mechanics.
5. Historical ZyBooks source files remain provenance only and should not become operational requirements again.
6. Week 16 is already validated and should be integrated rather than rebuilt.
7. The two old incoming Week 2/assessment branches are archaeological inputs, not blind merge targets.

---

# 26. Questions intentionally left open

These are questions, not failures.

## Course grammar

- What exact relationship should exist among Reasoning Odyssey, Reasoning Quest/Gate, World Bible, event reflections, and checkpoints?
- What does Week 4's first Show & Tell synthesize?
- Which of the current twelve formal topics should combine or move so Weeks 4-14 contain eleven legitimate core weeks?
- Which checkpoint weeks best fit the final spine?

## World Bible

- Literal cross-course carry-forward or optional import into a fresh course-native Bible?
- Should the DSCT World Bible keep the same student-facing name, or does it need a subtitle such as "World Bible: Reasoning Record"?
- How often must it be updated before it becomes bureaucracy?
- Which kinds of claims deserve longitudinal tracking?

## Pair Reasoning

- Exact individual reflection shape?
- Should partners independently state initial positions before talking?
- How should the course handle pairs that already agree?
- How often should a pair artifact include computation/code versus pure formal reasoning?
- Is peer feedback on Show & Tell a separate graded object or embedded in another category?

## LaTeX / containers

- What minimum command-line literacy is truly required?
- Can wrappers and templates make Linux knowledge mostly unnecessary?
- Which container runtime is the supported classroom path?
- Should the required LaTeX engine be Tectonic, latexmk/TeX Live, or another tested path?
- What should a student do when the container or compile fails?
- Can the local LLM be a recovery assistant without becoming the only recovery strategy?

## Sources

- Exact Week 4-14 source cards after live verification?
- Which materials are ADAPT vs LINK vs PRIMARY?
- Which external videos are genuinely better than course-owned explanation?
- Where does one paid-access item, if any, earn its place?

## Grading

- Exact recurring point values?
- due windows?
- late policy?
- revision/resubmission?
- drop-lowest behavior?
- checkpoint weights/points?
- how to preserve humane flexibility without making the evidence trail meaningless?

---

# 27. A possible design thesis to test

One promising way to describe the entire course is:

> **DSCT is a laboratory for justified belief in computer science.**

Discrete structures give students objects precise enough to reason about:

- propositions;
- sets;
- functions;
- relations;
- algorithms;
- recurrences;
- counts;
- probabilities;
- graphs;
- trees;
- Boolean systems;
- state machines.

Critical Thinking gives students the habits required to ask whether their reasoning deserves confidence.

AI gives them an extraordinarily fluent source of candidate explanations, examples, errors, and challenges.

Pair Reasoning gives them another human mind against which to test their own.

Show & Tell makes reasoning public enough to defend.

The World Bible makes intellectual change visible across time.

LaTeX makes formal reasoning communicable.

Containers make computational evidence reproducible.

The Reasoning Odyssey ties the journey together.

And the skeptic question keeps the whole machine pointed in one direction:

> **What would it take to convince a skeptic?**

If a student can answer that question more precisely, more humbly, and with better evidence in December than in August, the course has done something important.

---

# 28. Next use of this file

Do not immediately turn this entire document into one monster prompt.

The next pass should slice it into a systematic design/work map.

A likely sequence is:

1. identify every **DECIDED** statement that needs source reconciliation;
2. identify every **OPEN QUESTION** requiring Jeremy + ChatGPT thought;
3. identify every **EVIDENCE GATHERING** job that a Foreman can run without making pedagogy;
4. identify every **IMPLEMENTATION** job that becomes bounded once a decision exists;
5. order dependencies;
6. create small DSCT-owned prompts under `sidecar/prompts/`;
7. keep JTT out of the loop until the DSCT worksite itself has a coherent campaign worth proposing upstream.

The immediate value of this dump is that we can now reason from a common artifact rather than from scattered chat archaeology.
