# Instructor guide — Boolean checks and finite-state-machine limits

This guide is for the Week 14 package's two 75-minute meetings. The package
teaches students to match the scope of a claim to the evidence: every small
Boolean assignment for equivalence, and every declared state/input case for a
finite-state model. Students' artifacts are shared learning resources, so ask
for fictional, non-sensitive examples only.

## Learning target in plain language

Students should be able to:

- fill every row of a small truth table before accepting an equivalence claim;
- distinguish a satisfying witness (one case that works) from a tautology
  (every allowed case works);
- name states, inputs, transitions, a start state, and a trace in a small
  finite-state machine; and
- state a model limit: a relevant fact the model does not represent and
  therefore cannot establish.

The recurring class loop is **predict → run → explain**. A prediction is not
evidence. The visible evidence is a row, counterexample, witness, trace, or
missing transition that another person can inspect.

## Materials and boundaries

Use the student handout, concept map, glossary, prompt page, and the linked
slides. The reference code under `code/` is a committed recovery copy for
instructor use; students do not need a package install or a live service.
There is no Canvas operation in this guide.

For Thursday, use the canonical [Reasoning Odyssey Checkpoint 3
source](../../student/odyssey-checkpoint-3.md) as the source of its submission
headings. The package links to that source; it does not copy or rewrite it.
Checkpoint 3 replaces the ordinary Week 14 Decision Gate. A Show & Tell
report remains a distinct course-work object when the course site requests it;
do not merge the two artifacts or invent a second gate.

## Jargon ledger

Introduce each term in this short form before asking students to use it:

| Term | Say this first |
|---|---|
| Boolean variable | a named place holding `True` or `False` |
| assignment | one choice for every variable |
| expression | a written rule that produces a result |
| gate / circuit | one Boolean operation / connected operations |
| truth table | every allowed assignment and its output |
| equivalence | same output for every allowed assignment |
| counterexample | one allowed case that breaks a universal claim |
| satisfiable | true for at least one allowed assignment |
| witness | the specific case showing satisfiability |
| tautology | true for every allowed assignment |
| state | one named situation in a model |
| input | an event supplied to the model |
| transition | the rule choosing the next state |
| start state | where the trace begins |
| trace | the ordered states and inputs in a run |
| model limit | what the model leaves out and cannot establish |

If a student says “the AI proved it,” ask which row, witness, trace, or
transition is the evidence.

## Tuesday — 75-minute teaching path

| Time | Move | Visible check to protect |
|---|---|---|
| 0:00–0:08 | Display the confident claim `F = (P OR Q) AND (P OR NOT Q)` and the proposed `B = P OR Q`. Use the smoke-alarm analogy: a test button checks whether the alarm can respond; it does not predict a fire. Ask what evidence equivalence requires. | Students predict that every assignment must be checked. |
| 0:08–0:20 | Define variable, assignment, AND, OR, NOT, expression, gate, circuit, equivalence, and truth table. Fill the four rows for `F` and `B`. | The only mismatch is visible at `P=False, Q=True`; one mismatch defeats the universal claim. |
| 0:20–0:38 | Compare the false simplification with `E = (P AND Q) OR (P AND NOT Q)` and `S = P`. Run Prompts 01 and 02, then Prompt 03a. Keep the original and proposed expressions beside the output. | `E` and `S` have no counterexamples; `F` and `B` return exactly `{'P': False, 'Q': True}`. |
| 0:38–0:53 | Define satisfiable, witness, tautology, and counterexample. Run Prompt 03b. Ask whether one successful row can prove “every row.” | `P=True` is a witness, `P=False` is a counterexample to `P` being a tautology; `P OR NOT P` is tautological and `P AND NOT P` is unsatisfiable. |
| 0:53–1:10 | Define state, input, transition, start state, trace, and model limit. Trace the fictional badge model on `valid, timeout, valid`, then show the incomplete transition table and run Prompts 04 and 05. | The trace is `Locked → Open → Locked → Open`; the incomplete table names exactly `("Open", "timeout")`. |
| 1:10–1:25 | Students choose a compact Boolean/circuit or state-machine claim, preview Thursday's challenge, and write the exit sentence. | Each student has a claim, inspectable evidence, and one stated boundary. |

### Prompt recovery cards

- **Prompt 01:** If the assistant starts coding before defining terms, pause and
  ask for the four definitions and one predicted row.
- **Prompt 02:** If it skips a row or silently replaces the expression, put the
  four fixed assignments on the board and compare each output column.
- **Prompt 03a:** Require a returned mapping, not “they differ.” The mapping is
  the counterexample another student can inspect.
- **Prompt 03b:** Separate “at least one” from “every.” Ask for the remaining
  counterexample when a student offers only a witness.
- **Prompt 04:** Keep inputs and states distinct. Read the transition table one
  input at a time and include the start state in the trace.
- **Prompt 05:** Enumerate the state/input pairs. An unstated self-loop is not a
  declared transition and cannot repair a missing rule.

### Common drift and recovery

| Drift | Recovery question |
|---|---|
| “It looks like the familiar simplification.” | Which of the four rows did you check? |
| “`P=True` proves `P`.” | Is that a witness or a check of every assignment? |
| “An omitted input probably leaves the state alone.” | Where is that self-loop declared? |
| “The trace proves a real badge is safe.” | What authorization, reader, or omitted state is outside this model? |

## Thursday — 75-minute model defense

The Thursday activity is a short public defense. Classmates will see the work,
so keep examples fictional or otherwise non-sensitive and critique evidence,
assumptions, or inferences—not people.

| Time | Move | Evidence to protect |
|---|---|---|
| 0:00–0:10 | Rehearse the challenge norm. A useful challenge names a row, input, state, transition, or assumption to test. | The challenge is specific and professional. |
| 0:10–0:20 | Students select one path: Boolean/circuit or state-machine. Confirm that each claim is small enough to inspect. | Boolean path has every row; state path has named states, inputs, transitions, start state, two traces, and a limit. |
| 0:20–0:50 | Run compact Show & Tell defenses. Each student states the claim, shows the supporting row(s) or trace(s), names the strongest limit first, answers one challenge, and gives one peer critique. | The audience can reproduce the evidence and see what survived the challenge. |
| 0:50–1:05 | Quiet revision. Students test the challenge and narrow or defend the claim based on the result. | The revision is tied to an actual check, not confidence or presentation polish. |
| 1:05–1:13 | Students organize the four notes requested by the activity: claim/evidence, strongest challenge, what survived or changed, and peer critique. | The notes preserve the evidence boundary and revision. |
| 1:13–1:15 | Exit sentence: “My evidence establishes ___ under ___; it does not establish ___ because that boundary is outside the model.” | A limited conclusion is stated plainly. |

Do not require programming, a particular diagram tool, an AI account, or a
polished presentation. Paper or a local editable file is enough.

## Time-tight cut

If Tuesday loses time, preserve the false simplification, all four rows,
Prompt 03b's witness/tautology distinction, and the complete/incomplete state
model contrast. Move Prompt 01's prose definitions and the optional circuit
drawing to the handout. On Thursday, protect one complete defense per path
before expanding the number of presenters.

## Instructor self-check

- [ ] I asked for a prediction before each check.
- [ ] I kept the exact false row visible.
- [ ] I separated a witness from a universal claim.
- [ ] I treated missing transitions as missing, not as self-loops.
- [ ] I required a model limit before accepting a state trace.
- [ ] I protected peer visibility and fictional examples.
- [ ] I kept Checkpoint 3 linked and distinct from any Show & Tell report.
