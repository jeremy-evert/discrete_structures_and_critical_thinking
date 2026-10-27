import pytest

from merger.deps import CycleError, leaves_first
from relations import antisymmetric_failure
from test_dependencies import closure

LOOP = {"parse": {"validate"}, "validate": {"parse"}, "report": {"validate"}}


def test_a_cycle_is_reported_not_silently_ordered():
    with pytest.raises(CycleError) as problem:
        leaves_first(LOOP)
    assert "parse" in str(problem.value) and "validate" in str(problem.value)


def test_a_cycle_breaks_antisymmetry_with_a_concrete_pair():
    depends = closure(LOOP)
    witness = antisymmetric_failure(lambda a, b: (a, b) in depends, sorted(LOOP))
    assert witness == ("parse", "validate")
