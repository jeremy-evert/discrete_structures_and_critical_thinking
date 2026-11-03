# Red tests for the Week 14 checks

The examples below are instructional red tests. They are **not collected by
pytest**: they are fenced code in this document, not Python files. They show
the wrong implementations that the committed reference suite must reject.

## Red test: false simplification must expose exactly one row

```python
# Non-collection example: this intentionally fails for the wrong claim.
def test_wrong_simplification_is_not_accepted():
    assert equivalent(FALSE_EXPRESSION, FALSE_SIMPLIFICATION, ("P", "Q"))
```

The correct checker rejects that claim and returns exactly
`{"P": False, "Q": True}` as its counterexample.

## Red test: an omitted transition must not become an implicit self-loop

```python
# Non-collection example: this intentionally fails if a missing transition
# is silently treated as staying in the same state.
def test_omitted_transition_is_not_a_self_loop():
    machine = incomplete_badge_model()
    assert machine.run_trace(("valid", "timeout")) == ["Locked", "Open", "Open"]
```

The reference implementation reports the missing `("Open", "timeout")`
transition and raises a visible error when the trace reaches it.

