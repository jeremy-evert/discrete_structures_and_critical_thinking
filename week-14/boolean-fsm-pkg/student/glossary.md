# Glossary — Boolean expressions and state models

Terms are in the order used to build a check from simple values to a state
trace.

- **Boolean value:** one of two values, `True` or `False`.
- **Boolean variable:** a named place that holds one Boolean value, such as
  `P`.
- **Assignment:** a choice of a Boolean value for every variable, such as
  `P=False, Q=True`.
- **AND:** an operation that is true only when both inputs are true.
- **OR:** an operation that is true when at least one input is true.
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
  inputs, and transition rules.
- **State:** one named situation in a finite-state machine, such as `Locked`.
- **Input:** an event supplied to the machine, such as `valid` or `timeout`.
- **Transition:** a rule that maps a current state and an input to the next
  state, such as `Locked --valid--> Open`.
- **Start state:** the state where a trace begins.
- **Trace:** the ordered record of states and inputs as a machine runs.
- **Model:** a deliberately limited description of a situation, not the whole
  real world.
- **Model limit:** a relevant fact that a model does not represent and
  therefore cannot establish.
- **Self-loop:** a transition that leaves the machine in the same state. It
  must be stated; it is not a safe guess for a missing rule.
- **AI assistant:** a tool that generates text or code. Its output is a claim
  to check, not evidence by itself.
