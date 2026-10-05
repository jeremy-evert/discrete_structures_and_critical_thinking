"""Tests in teaching order. Run: python3 -m pytest -v week-08/teaching"""
import pytest
from recursion_demo import (
    S, S_closed, fact, fib,
    fib_missing_base, fib_wrong_base, bad_no_base, bad_T,
)


# 1. Sum -----------------------------------------------------------------
def test_S_base_case():
    assert S(0) == 0

def test_S_trace_3():
    assert S(3) == 3 + 2 + 1 + 0 == 6

def test_S_matches_closed_form_small_n():
    # evidence, NOT proof: the induction proof is what covers all n
    assert all(S(n) == S_closed(n) for n in range(0, 30))


# 2. Factorial -------------------------------------------------------------
def test_fact_base_and_step():
    assert fact(0) == 1
    assert fact(5) == 5 * fact(4) == 120


# 3. Fibonacci -----------------------------------------------------------
def test_fib_both_base_cases():
    assert (fib(0), fib(1)) == (0, 1)

def test_fib_trace_5():
    # F(5)=F(4)+F(3)=(3)+(2)=5, with F(2)=1,F(3)=2,F(4)=3
    assert [fib(k) for k in range(6)] == [0, 1, 1, 2, 3, 5]

def test_missing_base_case_never_terminates():
    with pytest.raises(RecursionError):
        fib_missing_base(5)

def test_wrong_base_gives_wrong_values():
    assert fib_wrong_base(5) == 0 != fib(5)

def test_fib_less_than_2_pow_n():
    # checks small cases of the claim proved by induction in the handout
    assert all(fib(n) < 2 ** n for n in range(0, 20))

def test_sum_of_fibs_identity():
    # F(1)+...+F(n) = F(n+2) - 1
    assert all(sum(fib(k) for k in range(1, n + 1)) == fib(n + 2) - 1
               for n in range(0, 20))


# 4. Find the bug ----------------------------------------------------------
def test_no_base_case_hits_guard():
    with pytest.raises(RecursionError):
        bad_no_base(3)

def test_bad_T_never_reaches_base_for_positive_input():
    with pytest.raises(RecursionError):
        bad_T(1)    # smallest input that exposes the problem

def test_bad_T_zero_looks_fine():
    assert bad_T(0) == 1    # why "it worked once" is not evidence
