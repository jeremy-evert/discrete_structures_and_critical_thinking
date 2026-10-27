import pytest

from playlist.depends import CycleError, leaves_first


def test_two_functions_that_need_each_other_are_reported():
    with pytest.raises(CycleError):
        leaves_first({"a": {"b"}, "b": {"a"}})


def test_the_error_names_the_loop():
    with pytest.raises(CycleError) as problem:
        leaves_first({"a": {"b"}, "b": {"c"}, "c": {"a"}, "d": set()})
    assert "a -> b -> c -> a" in str(problem.value)
