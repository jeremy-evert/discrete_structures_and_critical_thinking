# Discrete Structures and Critical Thinking — Fall 2026 Course Design

**Status:** historical design blueprint; no Canvas/Savnac configuration has
been changed. RECONCILED 2026-08-15: DSCT has no required textbook or external
course for Fall 2026. Its ZyBooks references and section decisions are
historical planning provenance, not an operational adoption or course spine.

## Design stance

COMSC-2043 is the reasoning bridge after CS1/CS2 and MATH-1513: students use
precise language, definitions, proof, discrete representations, small programs,
and simulations to make and test claims. It is not a compressed tour of every
available textbook topic. The former ZyBooks path and accompanying
[section decisions](zybooks-section-decisions.csv) are retained as historical
planning provenance only; no path from them is required.

### Intended outcomes

Students will be able to:

1. translate a claim into precise logical, set, function, relational, or graph
   language and state assumptions;
2. construct, critique, and revise a proof or counterexample;
3. select and justify a discrete model for an algorithm, counting,
   probability, cryptography, or state problem;
4. implement or simulate a small model, inspect its output, and explain the
   limits of its conclusion; and
5. communicate reproducible reasoning using sources, work, checking, and a
   concise conclusion.

### Rhythm, assessment, and AI expectations

The existing weekly problem-solving write-up remains the main evidence format:
Sources, Rules/Assumptions, Work, Check, and One-Sentence Summary.  Pair work,
show-and-tell, and a small synthesis project make reasoning public without
turning every week into a high-stakes test.  Short concept checks are used to
surface misconceptions.  Career evidence remains a light recurring strand,
not a competing second course.

AI may be used to generate examples, alternate explanations, test cases, or
questions, but students must label that use, verify claims against definitions,
and submit their own trace, proof, code/output, or explanation.  An unverified
AI answer is not evidence.  AI may not replace the individual reflection or
the student’s account of assumptions and checking.

## Semester spine and module blueprint

The dated operational spine and weekly architecture were reconciled by
Prompt 302. The table below is retained as pedagogical design intent and
reading rationale, not as the dated week allocation. The authoritative
calendar is [`fall-2026-spine.md`](fall-2026-spine.md), and the authoritative
topic/source mapping is [`fall-2026-topic-map.md`](fall-2026-topic-map.md).
Week 1 is the landed kickoff; Week 2 is Building Your AI Lab / Containers and
Repeatability; formal DSCT topics begin in Week 3 and end in Week 14; Week 15
is an asynchronous Thanksgiving/Mexico buffer; Week 16 is Farkle + ML; Week
17 is Final Reflection. No points, grading weights, or due dates are implied.

`KEEP` and `OPTIONAL` identifiers below are historical section references
only; titles, classifications, and prerequisites are in the CSV. They do not
describe required readings. Each module must include a Week at a Glance
overview, accessible instructor slides/material, locally selected learning
materials, an activity/assignment, and a visible evidence or rubric. Due dates
remain unset unless a later source-backed calendar supplies them.

| Week | Central question and student objectives | Historical reference menu (not required) | Activity, milestone, and evidence | Student-facing Canvas/Savnac module shape / readiness |
|---|---|---|---|---|
| 1 | How will we learn and show reasoning here? Locate course tools; set a study practice; distinguish help from evidence. | No textbook reading; orientation lesson and career evidence pack. | Learning-practice plan; low-stakes 3-2-1 check. | Overview, Course Information, learning-practice material, study check, accessibility/help links. Must publish the kickoff path. |
| 2 | How do claims, definitions, proof, sequences, and sets work together? Translate claims; identify counterexamples; write a checked proof. | KEEP 1.1–1.4, 1.6–1.7, 1.11; 2.1–2.7; 3.1, 3.3–3.4, 3.6–3.7. OPTIONAL 1.5, 1.8–1.10, 1.12–1.13, 3.2, 3.5, 15.2. | Guided claim clinic and proof peer review; Write-up 1. | Overview, proof slides, selected links, write-up/rubric, concept check. Need an instructor-created proof-feedback exemplar. |
| 3 | How can a function or matrix represent a discrete system? Identify mapping properties; use a matrix only when it clarifies. | KEEP 4.1, 4.3, 4.5. OPTIONAL 4.2, 4.4. | Representation comparison and small code/table trace; Write-up 2. | Overview, representation examples, links, problem write-up, rubric. Matrix scope needs a prepared instructor example. |
| 4 | What makes a procedure reliable and efficient? State inputs/outputs; trace edge cases; compare growth informally. | KEEP 7.1–7.3. OPTIONAL 7.5–7.6. | Pair algorithm trace and complexity explanation; concept check. | Overview, trace worksheet, links, pair report, check. Relies on COMSC-1053 programming fluency. |
| 5 | How do integer properties support reversible encoding? Perform modular calculations; test encode/decode claims; name limits. | KEEP 9.1–9.3, 9.5, 9.9–9.10. OPTIONAL 9.4, 9.6–9.8, 9.11. | Cryptography pair exercise with test cases; Write-up 3. | Overview, instructor cryptography scenario, links, pair artifact/rubric. Keep security claims modest and evidence-based. |
| 6 | When does a recursive claim or program stop and why is it correct? Trace recurrence; apply induction; compare recursion and iteration. | KEEP 8.1–8.5, 8.8, 8.10–8.11. OPTIONAL 8.6–8.7, 8.9, 8.12–8.17. | Recursion trace plus proof or invariant explanation; short programming exam or equivalent focused artifact. | Overview, trace/proof materials, links, assessment and rubric. Requires a supported coding environment. |
| 7 | Which counting model matches the constraints? Choose product, permutation, subset, complement, or inclusion-exclusion reasoning and defend it. | KEEP 10.1, 10.4–10.5, 10.7–10.8, 10.11; 11.2–11.3. OPTIONAL 10.2–10.3, 10.6, 10.9–10.10, 10.12, 11.1. | Counting-model sort and Write-up 4. | Overview, worked decision tree, links, write-up/rubric, check. Avoid assigning every counting variant. |
| 8 | How can a probability model be checked rather than merely calculated? Define events; interpret conditional probability and expectation; compare simulation. | KEEP 12.1–12.3, 12.5–12.6. OPTIONAL 12.4, 12.7–12.8. | Simulation lab and result interpretation; show-and-tell artifact. | Overview, simulation starter, links, demo submission, rubric. Requires a lightweight language/tool choice. |
| 9 | What does a relation assert, and which properties does it have? Represent and classify relations; connect digraphs and orders. | KEEP 6.1–6.3, 6.7, 6.9. OPTIONAL 6.4–6.6, 6.8, 6.10. | Relation classification clinic; Write-up 5. | Overview, relation/digraph materials, links, problem write-up, rubric. Preserve time for explanation rather than matrix-power detail. |
| 10 | What can a graph model reveal about a system? Build a graph; distinguish paths/cycles; explain connectivity or optimization question. | KEEP 13.1–13.2, 13.4–13.7, 13.9. OPTIONAL 13.3, 13.8. | Model a local/system problem; graph show-and-tell. | Overview, graph-model prompt, links, artifact and peer questions. Instructor supplies context-rich modeling cases. |
| 11 | How do trees organize search and hierarchy? Identify tree structure; trace a traversal; relate a tree to a graph. | KEEP 14.1–14.5. OPTIONAL 14.6. | Traversal/code-or-diagram activity; Write-up 6. | Overview, tree examples, links, write-up/rubric, concept check. Scope minimum-spanning-tree optimization as enrichment. |
| 12 | How does Boolean reasoning connect claims, satisfiability, and machine behavior? Simplify and verify expressions; explain a gate/circuit model. | KEEP 5.1–5.3, 5.5–5.6. OPTIONAL 5.4. | Truth-table/simplification lab; focused evidence artifact. | Overview, Boolean examples, links, lab submission/rubric. Needs an instructor-created bridge from logic to circuits. |
| 13 | How can a finite-state model make behavior inspectable? Design states/transitions; trace inputs; test a small machine. | KEEP 7.4 (revisited). OPTIONAL 7.5–7.6 as context. | State-machine pair build and individual validation reflection. | Overview, state-machine builder/material, link, pair report, individual reflection. Intentional reinforcement of Week 4 computation. |
| 14 | How can discrete tools support an authentic claim or application? Scope a problem; choose a model; communicate limitations and evidence. | Revisit only the KEEP sections needed by each project; no new textbook march. | Synthesis project proposal/demo and career-evidence update. | Overview, project guide, selectable reference links, milestone/rubric. Needs current project choice and success criteria. |
| 15 | What do we know, what remains uncertain, and how do we defend a conclusion? Integrate models; revise from feedback; reflect accurately. | Targeted OPTIONAL review only. | Project/final reflection and cumulative concept check. | Overview, review map, optional links, project/reflection, rubric. Use Question 004 for the resolved final-format and grading structure; leave operational details to later source-backed authoring. |
| 16 | Finals week: demonstrate selected outcomes without adding new content. | No new reading. | Final only if the later approved assessment plan requires it. | Final instructions and accommodations information must be visible only after format/date are source-backed. |

## Limitations of the historical ZyBooks proposal

- Feedback-rich proof critique, including how to repair an unclear argument.
- Contextual modeling problems that make critical-thinking choices visible.
- Small programming/simulation environments, test-data design, and code review.
- The paired collaboration, show-and-tell, and individual accountability trail.
- Career evidence, metacognition, accessibility/help orientation, and final reflection.
- Instructor examples that connect Boolean logic to circuits and state models to
  practical processes without overstating the model.

## Lean configuration and open decisions

The historical manifest has 126 sections: 75 KEEP (59.5%), 46 OPTIONAL
(36.5%), and 5 UNUSED (4.0%). Its proposed required/optional configuration and
vendor-price question are superseded for DSCT by the 2026-08-15 decision: no
required textbook or external course for Fall 2026. The counts and section
classification are retained as planning provenance only.

Question 004, `jeremy_task_tracking/questions/answered_questions/004_dsct_grading_and_final_format.md`,
resolved the grading structure and final-format decision. The current source
of truth is that decision: weekly Decision Gates and recurring
weekly course work are the same integrated weekly work, not a second
gradebook or parallel assignment. Future authors should use the current spine,
weekly architecture, and topic map for the dated operational contract. Other
design choices—career-strand treatment, project choices and tooling, and the
exact student-facing due-date cadence—remain to be specified by later
source-backed authoring.
