"""Synthetic examples used by the Week 14 Boolean/FSM checks."""

from boolean_fsm import FiniteStateMachine, conjunction, disjunction, negate, variable


P = variable("P")
Q = variable("Q")

# The source activity's correct simplification: E is equivalent to S.
SOURCE_EXPRESSION = disjunction(conjunction(P, Q), conjunction(P, negate(Q)))
SOURCE_SIMPLIFICATION = P

# The deliberately false AI simplification used in the deck.
FALSE_EXPRESSION = conjunction(disjunction(P, Q), disjunction(P, negate(Q)))
FALSE_SIMPLIFICATION = disjunction(P, Q)


BADGE_STATES = ("Locked", "Open")
BADGE_INPUTS = ("valid", "timeout")
BADGE_MODEL_LIMIT = (
    "This synthetic model tracks only two named states and two declared inputs; "
    "it does not establish authorization, a physical reader condition, or a "
    "missing Denied or Expired state."
)


def complete_badge_model() -> FiniteStateMachine:
    """Return the complete two-state classroom model with explicit self-loops."""
    return FiniteStateMachine(
        states=BADGE_STATES,
        input_alphabet=BADGE_INPUTS,
        start_state="Locked",
        transitions={
            ("Locked", "valid"): "Open",
            ("Locked", "timeout"): "Locked",
            ("Open", "valid"): "Open",
            ("Open", "timeout"): "Locked",
        },
    )


def incomplete_badge_model() -> FiniteStateMachine:
    """Return a model missing exactly the transition needed after ``Open``."""
    return FiniteStateMachine(
        states=BADGE_STATES,
        input_alphabet=BADGE_INPUTS,
        start_state="Locked",
        transitions={
            ("Locked", "valid"): "Open",
            ("Locked", "timeout"): "Locked",
            ("Open", "valid"): "Open",
        },
    )

