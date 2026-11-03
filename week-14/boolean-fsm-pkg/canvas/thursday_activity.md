# Week 14 Thursday: Model Defense, Show & Tell, and Checkpoint 3

**Show & Tell** is a short class presentation: show an example and explain the
checkable **evidence** for it. Evidence means results, such as rows or a trace,
that support or challenge a **claim**, the statement being checked. A
**boundary** is the line between what a model represents and what it leaves
out. A **model limit**
is a relevant fact the model leaves out, so it cannot establish that fact. In
a state machine, an **input** is an event supplied to the machine, such as
`valid`; in `Locked --valid--> Open`, the arrow means “from Locked, on
`valid`, go to Open,” and plain `A -> B` means “A leads to B.” Thursday is a
short public defense. Classmates will see the work, so use a fictional or
otherwise non-sensitive example and critique the claim or model, never the
person.

## Choose one path

- **Boolean/circuit:** show one expression, a proposed equivalent expression
  or circuit, and every row of its truth table. A Boolean expression is a rule
  that produces `True` or `False` from Boolean values.
- **State machine:** show named states, allowed inputs, transitions, a start
  state, two traces, and one model limit. A state machine is a bounded model
  whose transition rules say how an input changes the current state.

Keep the claim small enough that another student can
inspect each row or trace.

## In-class defense

1. State the claim you want the check to support and show its rows or traces.
2. Name the strongest limitation before the audience discovers it.
3. Answer one challenge by testing a row, input, state, or assumption. Revise
   or narrow the claim if the challenge earns that change.
4. Give one specific, professional critique of a peer's evidence or model
   boundary. Critique the evidence, assumption, or inference—not the person.

Keep four notes: your claim and best evidence, the strongest challenge, what
survived or changed, and the critique you gave. A revised claim is a useful
outcome.

## Submission map

Submit the individual [Reasoning Odyssey Checkpoint 3](../../student/odyssey-checkpoint-3.md)
using the published course-site details. That canonical Checkpoint 3 source
replaces the ordinary Week 14 Decision Gate; do not create a second Decision
Gate artifact. The recurring Show & Tell report remains a distinct course-work
object when the course site asks for it, so do not duplicate it inside the
checkpoint.

Use the checkpoint's Sources, Rules / Assumptions, Work, Check Your Answer,
One-Sentence Summary, and Odyssey reflection headings. Finish with a sentence
that says what your evidence establishes and what remains outside the model.
