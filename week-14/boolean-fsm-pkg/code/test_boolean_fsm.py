"""Executable checks for the Week 14 reference implementation."""

import pytest

from boolean_fsm import (
    FiniteStateMachine,
    all_assignments,
    conjunction,
    disjunction,
    equivalence_counterexamples,
    equivalent,
    evaluate,
    is_tautology,
    negate,
    satisfying_assignment,
    tautology_counterexample,
    variable,
)
from examples import (
    FALSE_EXPRESSION,
    FALSE_SIMPLIFICATION,
    SOURCE_EXPRESSION,
    SOURCE_SIMPLIFICATION,
    complete_badge_model,
    incomplete_badge_model,
)


def test_all_assignments_use_fixed_false_before_true_order():
    assert all_assignments(("P", "Q")) == [
        {"P": False, "Q": False},
        {"P": False, "Q": True},
        {"P": True, "Q": False},
        {"P": True, "Q": True},
    ]


def test_false_simplification_differs_on_exactly_one_row():
    assert equivalence_counterexamples(
        FALSE_EXPRESSION, FALSE_SIMPLIFICATION, ("P", "Q")
    ) == [{"P": False, "Q": True}]


def test_source_activity_simplification_is_equivalent_on_all_rows():
    assert equivalent(SOURCE_EXPRESSION, SOURCE_SIMPLIFICATION, ("P", "Q"))


def test_missing_variable_is_rejected_instead_of_invented():
    with pytest.raises(KeyError, match="missing variable"):
        evaluate(variable("P"), {})


def test_witness_for_p_does_not_make_p_a_tautology():
    expression = variable("P")
    assert satisfying_assignment(expression) == {"P": True}
    assert not is_tautology(expression)
    assert tautology_counterexample(expression) == {"P": False}


def test_tautology_and_unsatisfiable_expression_are_separate_checks():
    p_or_not_p = disjunction(variable("P"), negate(variable("P")))
    p_and_not_p = conjunction(variable("P"), negate(variable("P")))
    assert is_tautology(p_or_not_p)
    assert satisfying_assignment(p_and_not_p) is None


def test_complete_badge_trace_is_explicit():
    machine = complete_badge_model()
    assert machine.validate_total() == []
    assert machine.run_trace(("valid", "timeout", "valid")) == [
        "Locked",
        "Open",
        "Locked",
        "Open",
    ]


def test_incomplete_badge_model_names_exact_missing_transition():
    assert incomplete_badge_model().validate_total() == [("Open", "timeout")]


def test_unknown_input_fails_visibly():
    with pytest.raises(ValueError, match="unknown input"):
        complete_badge_model().run_trace(("expired",))


def test_missing_transition_fails_visibly():
    machine = incomplete_badge_model()
    with pytest.raises(ValueError, match="missing transition"):
        machine.run_trace(("valid", "timeout"))


def test_no_implicit_self_loop_is_added():
    machine = FiniteStateMachine(
        states=("Locked", "Open"),
        input_alphabet=("valid", "timeout"),
        start_state="Locked",
        transitions={("Locked", "valid"): "Open"},
    )
    assert machine.validate_total() == [
        ("Locked", "timeout"),
        ("Open", "valid"),
        ("Open", "timeout"),
    ]

