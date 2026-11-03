# Week 14 Tuesday: Boolean Algebra, Circuits, SAT, and State Models

An **assignment** gives every variable a value; an **allowed assignment** is
any combination of `True` or `False` for those variables. **Equivalent** means
two expressions give the same result for every allowed assignment. A **state
model** is a simplified description of a system using named conditions and
rules for how events change them. In Boolean expressions, an **input** is a
value supplied to an operation, such as `P` and `Q` in `P AND Q`; in a state
model, an input is an event supplied to the machine.

**Big question:** Is this transformation equivalent under every assignment,
and what can this state model not establish?

Here, **SAT** is short for satisfiability: whether at least one allowed
assignment makes an expression true. **Unsatisfiable** means no allowed
assignment makes it true. A **proof** here is a check that covers every case.
A **counterexample** is an allowed assignment that shows a claim is false. A
**satisfying witness** is an assignment that makes an expression true. A
**tautology** is an expression that is true for every allowed assignment.
A **transition** is a rule saying which next state follows from one state and
one input. A **trace** is the ordered record of states and inputs during a run.
An **arrow** such as `Locked --valid--> Open` means “from Locked, on the
`valid` event, go to Open”; a plain `A -> B` means “A leads to B.”

## Start here

1. Open the [Boolean and finite-state-machine slides]({{FILE_URL:boolean_fsm_slides.pdf}})
   (`{{FILE:boolean_fsm_slides.pdf}}`).
2. Read the handout, concept map, and glossary pages in this module.
3. Work through the five Claude prompt files on the prompts page. Predict
   first, run the check, and explain what the **evidence**—the checkable rows
   or trace—does and does not show.

## What you will check

- all four assignments for a two-variable Boolean expression and its proposed
  simplification (a shorter or simpler form meant to keep the same meaning);
- the difference between a counterexample, a satisfying witness, and a
  tautology;
- a fictional two-state badge trace with explicit transitions; and
- a **missing transition**: a state/event pair with no rule saying what happens
  next. A **self-loop** is a transition that returns to the same state; do not
  assume one when a rule is missing.

Use only fictional, non-sensitive examples. Class artifacts are shared
learning resources: classmates will see your work.

## Before Thursday

Bring one compact Boolean/circuit or state-machine **claim** (a statement you
want the check to support) that a peer can inspect. **Evidence** is the
checkable rows or trace that supports or challenges the claim. On Thursday,
**Show & Tell** means briefly showing your example and explaining your check
to classmates. You will defend the evidence, accept a challenge, and state the
model's **boundary**: what it leaves out and therefore cannot establish.
