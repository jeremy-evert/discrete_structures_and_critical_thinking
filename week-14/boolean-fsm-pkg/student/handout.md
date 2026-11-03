# Handout — Boolean checks and state traces

## The habit: predict, run, explain

Before trusting a **claim** (a statement someone wants the check to support),
write your prediction. Then run a check that could show a difference.
**Evidence** is the checkable result, such as table rows or a trace, that
supports or challenges the claim. Finally, explain what the result covers and
what it leaves unanswered.
Use fictional, non-sensitive examples. Class artifacts are shared learning
resources: classmates will see your work, so protect real people's information.

## 1. Check a Boolean claim with every row

A **Boolean value** is either `True` or `False`. A **Boolean variable** is a
named place that holds one Boolean value. An **assignment** chooses a value for
each variable; an **allowed assignment** is any combination of `True` and
`False` for those variables. A **Boolean expression** is a rule that produces `True` or
`False` from those values.

The operations are small rules: in Boolean expressions, an **input** is a
value supplied to an operation, so `P` and `Q` are the inputs in `P AND Q`.
`P AND Q` is true only when both inputs are true; `P OR Q` is true when at
least one input is true; `NOT P` reverses the value. A **truth table** lists every assignment and the resulting output. A
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
Checking every allowed assignment is a **proof** of whether these two
expressions are equivalent: it covers every case in this finite table. A
**simplification** is a shorter or simpler expression intended to keep the
same meaning; it still needs this check.

## 2. A witness does not cover every case

An expression is **satisfiable** when at least one allowed assignment makes it true.
It is **unsatisfiable** when no allowed assignment makes it true.
That particular successful assignment is a **satisfying witness** (or just a
**witness**). A **tautology** is an expression that is true for every allowed
assignment. These are different
questions:

- `P` is satisfiable; `P=True` means the variable `P` has value `True`, and
  this assignment is a witness.
- `P` is not a tautology; `P=False` is a counterexample.
- `P OR NOT P` is a tautology.
- `P AND NOT P` is not satisfiable: no assignment makes it true.

The check for “at least one” must not be reported as a check for “every.”

## 3. Trace a small state model

A **finite-state machine** is a small model with named situations and rules
that say how machine events change them. A **state** is one named situation.
An **input** to this machine is an **event** supplied to it, such as `valid`
or `timeout`; this differs from a Boolean input value such as `P`. A
**transition** is a rule saying which next state follows from one state and
one input. The **start state** is where a run begins. A **trace** is the
ordered record of states and inputs during a run.

In arrow notation, `A --event--> B` means “from state A, on this event, go to
state B”; a plain `A -> B` means “A leads to B.” For a fictional access badge,
use these explicit rules:

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
establish it. Its **boundary** is the line between what the model represents
and what it leaves out. This two-state model can show the stated state changes; it cannot
establish whether a real person was authorized, whether a physical reader
worked, or what should happen for an input that has no listed rule.

## Three AI traps to catch

An **AI assistant** is a tool that generates text or code. It can sound certain
while skipping a check. For each trap, demand the named evidence:

1. **Familiar-looking simplification:** require all allowed assignments and the exact
   counterexample row. The false `B` claim fails at `P=False, Q=True`.
2. **One witness treated as universal proof:** ask whether the claim is
   satisfiable or a tautology, then require either one witness or every row as
   appropriate. `P=True` alone does not prove that `P` is always true.
3. **A missing rule silently treated as a same-state move:** a **self-loop** is
   a transition that leaves the machine in the same state. A **missing
   transition** is a state/input pair for which the model has no stated next
   state. List every state/input pair that the model promises to handle. In
   the rules above, `Open --timeout--> Locked` is present; if it were omitted,
   that would be the missing rule, and we must not silently assume `Open`
   stays `Open`.

## Self-check

I can complete every row before accepting equivalence; distinguish a witness
from a tautology; write a trace from a start state; and name one model limit.
