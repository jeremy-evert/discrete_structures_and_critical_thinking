# Glossary — Boolean expressions and state models

Terms are in the order used to build a check from simple values to a state
trace.

- **Boolean value:** one of two values, `True` or `False`.
- **Boolean variable:** a named place that holds one Boolean value, such as
  `P`.
- **Assignment:** a choice of a Boolean value for every variable, such as
  `P=False, Q=True`. An **allowed assignment** is any combination of `True` or
  `False` for the variables.
- **Proof:** a check that covers every case. For a finite truth table, that
  means checking every row.
- **Claim:** a statement someone wants a check to support.
- **Evidence:** a checkable result, such as table rows or a trace, that
  supports or challenges a claim.
- **AND:** an operation that is true only when both values are `True`.
- **OR:** an operation that is true when at least one value is `True`.
- **NOT:** an operation that reverses a Boolean value.
- **Expression:** a written rule that uses values and operations to produce an
  output. `P OR Q` is an expression.
- **Gate:** a picture of one Boolean operation, such as an AND gate.
- **Circuit:** connected gates used to represent an expression.
- **Truth table:** a table with one row for each assignment and the output for
  that row.
- **Equivalence:** a relationship in which two expressions have the same output
  for every allowed assignment.
- **Universal claim:** a statement that says something is true for every
  allowed case.
- **Counterexample:** one allowed case that shows a universal claim is false.
- **Satisfiable:** true for at least one allowed assignment.
- **Witness:** the specific assignment that shows an expression is satisfiable.
- **Tautology:** an expression that is true for every allowed assignment.
- **Unsatisfiable:** an expression for which no allowed assignment produces
  `True`.
- **Finite-state machine:** a bounded model made from named states, allowed
  events, and transition rules.
- **State:** one named situation in a finite-state machine, such as `Locked`.
- **Input:** in a Boolean expression, a value supplied to an operation; in a
  state machine, an event supplied to the machine, such as `valid` or
  `timeout`.
- **Event:** something supplied to a state machine, such as `valid` or
  `timeout`.
- **Transition:** a rule that maps a current state and an input to the next
  state, such as `Locked --valid--> Open`.
- **Arrow notation:** `A --event--> B` means “from A, on this event, go to B”;
  plain `A -> B` means “A leads to B.”
- **Start state:** the state where a trace begins.
- **Trace:** the ordered record of states and inputs as a machine runs.
- **Model:** a deliberately limited description of a situation, not the whole
  real world.
- **Model limit:** a relevant fact that a model does not represent and
  therefore cannot establish.
- **Boundary:** the line between what a model represents and what it leaves
  out.
- **Self-loop:** a transition that leaves the machine in the same state. It
  must be stated; it is not a safe guess for a missing rule.
- **Missing transition:** a state/event pair for which the model gives no
  next state.
- **Simplification:** a shorter or simpler expression meant to keep the same
  meaning; it must still be checked.
- **Show & Tell:** a short class presentation in which you show an example
  and explain the checkable evidence for it.
- **AI assistant:** a tool that generates text or code. Its output is a claim
  to check, not evidence by itself.
