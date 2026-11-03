# Handout — Boolean checks and state traces

## The habit: predict, run, explain

Before trusting a claim, write your prediction. Then run a check that could
show a difference. Finally, explain what the result does and does not prove.
Use fictional, non-sensitive examples. Class artifacts are shared learning
resources: classmates will see your work, so protect real people's information.

## 1. Check a Boolean claim with every row

A **Boolean value** is either `True` or `False`. A **Boolean variable** is a
named place that holds one Boolean value. An **assignment** chooses a value for
each variable. A **Boolean expression** is a rule that produces `True` or
`False` from those values.

The operations are small rules: `P AND Q` is true only when both inputs are
true; `P OR Q` is true when at least one input is true; `NOT P` reverses the
value. A **truth table** lists every assignment and the resulting output. A
gate is a picture of one operation; a **circuit** connects gates to represent
an expression.

Test this claim, not just its familiar shape:

```text
F = (P OR Q) AND (P OR NOT Q)
claimed shorter form: B = P OR Q
```

| `P` | `Q` | `F` | `B` | same? |
|---|---|---|---|---|
| False | False | False | False | yes |
| False | True | False | True | **no** |
| True | False | True | True | yes |
| True | True | True | True | yes |

Two expressions are **equivalent** when they produce the same output for every
allowed assignment. One allowed assignment where they differ is a
**counterexample** to a claim that they are equivalent. Here the second row is
the counterexample, so the claimed shorter form is not equivalent to `F`.

## 2. A witness is not a proof for every case

An expression is **satisfiable** when at least one assignment makes it true.
That particular successful assignment is a **witness**. A **tautology** is an
expression that is true for every allowed assignment. These are different
questions:

- `P` is satisfiable; `P=True` is a witness.
- `P` is not a tautology; `P=False` is a counterexample.
- `P OR NOT P` is a tautology.
- `P AND NOT P` is not satisfiable: no assignment makes it true.

The check for “at least one” must not be reported as a check for “every.”

## 3. Trace a small state model

A **finite-state machine** is a small model with named situations and rules
for how inputs change them. A **state** is one named situation. An **input** is
an event given to the machine. A **transition** is a rule saying which next
state follows from one state and one input. The **start state** is where a run
begins. A **trace** is the ordered record of states and inputs during a run.

For a fictional access badge, use these explicit rules:

```text
states: Locked, Open
start state: Locked
Locked --valid--> Open
Open   --timeout--> Locked
```

The trace for `valid, timeout, valid` is:

```text
Locked --valid--> Open --timeout--> Locked --valid--> Open
```

A **model limit** is a relevant fact the model leaves out, so the model cannot
establish it. This two-state model can show the stated state changes; it cannot
establish whether a real person was authorized, whether a physical reader
worked, or what should happen for an input that has no listed rule.

## Three AI traps to catch

An **AI assistant** is a tool that generates text or code. It can sound certain
while skipping a check. For each trap, demand the named evidence:

1. **Familiar-looking simplification:** require all assignments and the exact
   counterexample row. The false `B` claim fails at `P=False, Q=True`.
2. **One witness treated as universal proof:** ask whether the claim is
   satisfiable or a tautology, then require either one witness or every row as
   appropriate. `P=True` alone does not prove that `P` is always true.
3. **Missing transition hidden as a self-loop:** a self-loop is a transition
   that leaves the machine in the same state. List every state/input pair that
   the model promises to handle. The check should name the missing `Open
   --timeout--> Locked` rule instead of silently assuming that `Open` stays
   `Open`.

## Self-check

I can complete every row before accepting equivalence; distinguish a witness
from a tautology; write a trace from a start state; and name one model limit.
