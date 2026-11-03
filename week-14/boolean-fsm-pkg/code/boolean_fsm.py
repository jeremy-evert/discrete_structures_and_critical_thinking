"""Small, explicit Boolean and finite-state-machine checkers for Week 14.

The Boolean expressions in this module are tuple trees.  A variable is
``("var", "P")``; the other supported nodes are ``("not", child)``,
``("and", left, right)``, and ``("or", left, right)``.  The representation is
deliberately small so that each operation can be inspected in a truth table.

The state-machine implementation also keeps its declarations explicit.  A
missing transition is an error; it is never silently treated as a self-loop.
"""

from __future__ import annotations

from itertools import product
from typing import Mapping, Iterable


Expression = tuple
Assignment = dict[str, bool]


def variable(name: str) -> Expression:
    """Return a Boolean variable node."""
    _check_name(name)
    return ("var", name)


def negate(expression: Expression) -> Expression:
    """Return a NOT node."""
    return ("not", expression)


def conjunction(left: Expression, right: Expression) -> Expression:
    """Return an AND node."""
    return ("and", left, right)


def disjunction(left: Expression, right: Expression) -> Expression:
    """Return an OR node."""
    return ("or", left, right)


def _check_name(name: str) -> None:
    if not isinstance(name, str) or not name:
        raise ValueError("variable names must be non-empty strings")


def _check_expression(expression: Expression) -> None:
    if isinstance(expression, str):
        _check_name(expression)
        return
    if not isinstance(expression, tuple) or not expression:
        raise ValueError(f"invalid Boolean expression: {expression!r}")

    operator = expression[0]
    if operator == "var" and len(expression) == 2:
        _check_name(expression[1])
    elif operator == "not" and len(expression) == 2:
        _check_expression(expression[1])
    elif operator in {"and", "or"} and len(expression) == 3:
        _check_expression(expression[1])
        _check_expression(expression[2])
    else:
        raise ValueError(f"invalid Boolean expression: {expression!r}")


def expression_variables(expression: Expression) -> tuple[str, ...]:
    """Return the expression's variable names in deterministic order."""
    _check_expression(expression)
    names: set[str] = set()

    def collect(node: Expression) -> None:
        if isinstance(node, str):
            names.add(node)
        elif node[0] == "var":
            names.add(node[1])
        elif node[0] == "not":
            collect(node[1])
        else:
            collect(node[1])
            collect(node[2])

    collect(expression)
    return tuple(sorted(names))


def evaluate(expression: Expression, assignment: Mapping[str, bool]) -> bool:
    """Evaluate an expression, rejecting a missing variable value."""
    _check_expression(expression)

    def visit(node: Expression) -> bool:
        if isinstance(node, str):
            name = node
            if name not in assignment:
                raise KeyError(f"assignment is missing variable {name!r}")
            value = assignment[name]
            if type(value) is not bool:
                raise TypeError(f"assignment value for {name!r} must be bool")
            return value

        operator = node[0]
        if operator == "var":
            return visit(node[1])
        if operator == "not":
            return not visit(node[1])
        if operator == "and":
            return visit(node[1]) and visit(node[2])
        return visit(node[1]) or visit(node[2])

    return visit(expression)


def all_assignments(variables: Iterable[str]) -> list[Assignment]:
    """Return all Boolean assignments in False-before-True order."""
    names = tuple(variables)
    for name in names:
        _check_name(name)
    if len(set(names)) != len(names):
        raise ValueError("variables must not contain duplicates")
    return [dict(zip(names, values)) for values in product((False, True), repeat=len(names))]


def _scope(expression: Expression, variables: Iterable[str] | None) -> tuple[str, ...]:
    if variables is None:
        return expression_variables(expression)
    names = tuple(variables)
    for name in names:
        _check_name(name)
    if len(set(names)) != len(names):
        raise ValueError("variables must not contain duplicates")
    missing = set(expression_variables(expression)) - set(names)
    if missing:
        raise ValueError(f"scope is missing expression variables: {sorted(missing)!r}")
    return names


def truth_table(
    expression: Expression, variables: Iterable[str] | None = None
) -> list[dict[str, object]]:
    """Return rows containing an ``assignment`` and its Boolean ``value``."""
    names = _scope(expression, variables)
    return [
        {"assignment": assignment, "value": evaluate(expression, assignment)}
        for assignment in all_assignments(names)
    ]


def equivalence_counterexamples(
    left: Expression,
    right: Expression,
    variables: Iterable[str] | None = None,
) -> list[Assignment]:
    """Return every assignment on which two expressions differ."""
    if variables is None:
        names = tuple(sorted(set(expression_variables(left)) | set(expression_variables(right))))
    else:
        names = tuple(variables)
        for name in names:
            _check_name(name)
        if len(set(names)) != len(names):
            raise ValueError("variables must not contain duplicates")
        expression_names = set(expression_variables(left)) | set(expression_variables(right))
        if not expression_names.issubset(names):
            raise ValueError("scope is missing an expression variable")
    return [
        assignment
        for assignment in all_assignments(names)
        if evaluate(left, assignment) != evaluate(right, assignment)
    ]


def equivalent(
    left: Expression,
    right: Expression,
    variables: Iterable[str] | None = None,
) -> bool:
    """Return whether two expressions agree on every assignment in scope."""
    return not equivalence_counterexamples(left, right, variables)


def satisfying_assignment(
    expression: Expression, variables: Iterable[str] | None = None
) -> Assignment | None:
    """Return the first witness making an expression true, if one exists."""
    for assignment in all_assignments(_scope(expression, variables)):
        if evaluate(expression, assignment):
            return assignment
    return None


def is_tautology(expression: Expression, variables: Iterable[str] | None = None) -> bool:
    """Return whether an expression is true for every assignment in scope."""
    return tautology_counterexample(expression, variables) is None


def tautology_counterexample(
    expression: Expression, variables: Iterable[str] | None = None
) -> Assignment | None:
    """Return the first assignment making an expression false, if one exists."""
    for assignment in all_assignments(_scope(expression, variables)):
        if not evaluate(expression, assignment):
            return assignment
    return None


class FiniteStateMachine:
    """A finite state machine with explicit states and transitions."""

    def __init__(
        self,
        states: Iterable[str],
        input_alphabet: Iterable[str] | None = None,
        start_state: str | None = None,
        transitions: Mapping[tuple[str, str], str] | None = None,
        *,
        inputs: Iterable[str] | None = None,
    ) -> None:
        if input_alphabet is None:
            input_alphabet = inputs
        elif inputs is not None:
            raise TypeError("provide input_alphabet or inputs, not both")
        if input_alphabet is None or start_state is None or transitions is None:
            raise TypeError("states, input_alphabet, start_state, and transitions are required")

        self.states = tuple(dict.fromkeys(states))
        self.input_alphabet = tuple(dict.fromkeys(input_alphabet))
        if not self.states or not self.input_alphabet:
            raise ValueError("states and input alphabet must not be empty")
        if start_state not in self.states:
            raise ValueError(f"unknown start state: {start_state!r}")
        self.start_state = start_state
        self.transitions = dict(transitions)

        for (state, input_symbol), next_state in self.transitions.items():
            if state not in self.states:
                raise ValueError(f"transition has unknown state: {state!r}")
            if input_symbol not in self.input_alphabet:
                raise ValueError(f"transition has unknown input: {input_symbol!r}")
            if next_state not in self.states:
                raise ValueError(f"transition has unknown destination: {next_state!r}")

    def validate_total(self) -> list[tuple[str, str]]:
        """Return every missing explicit state/input transition."""
        return [
            (state, input_symbol)
            for state in self.states
            for input_symbol in self.input_alphabet
            if (state, input_symbol) not in self.transitions
        ]

    def step(self, state: str, input_symbol: str) -> str:
        """Apply one declared transition, rejecting unknown or missing input."""
        if state not in self.states:
            raise ValueError(f"unknown state: {state!r}")
        if input_symbol not in self.input_alphabet:
            raise ValueError(f"unknown input: {input_symbol!r}")
        try:
            return self.transitions[(state, input_symbol)]
        except KeyError as error:
            raise ValueError(
                f"missing transition for ({state!r}, {input_symbol!r})"
            ) from error

    def run_trace(self, inputs: Iterable[str]) -> list[str]:
        """Return the start state followed by each state after one input."""
        state = self.start_state
        trace = [state]
        for input_symbol in inputs:
            state = self.step(state, input_symbol)
            trace.append(state)
        return trace

