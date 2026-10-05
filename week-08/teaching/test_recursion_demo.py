"""Tests in teaching order. Run: python3 -m pytest -v week-08/teaching"""
import pytest
from recursion_demo import (
    S, S_closed, fact, fib,
    fib_missing_base, fib_wrong_base, bad_no_base, bad_T,
    first_n_where_factorial_wins, horner, direct_eval, op_counts,
    odd_sum, L_picture, odd_sum_bogus_step,
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


# 4a. Growth: factorial vs 2^n vs n^k --------------------------------------
def test_52_factorial_dwarfs_2_pow_52_and_n_pow_10():
    assert fact(52) == 80658175170943878571660636856403766975289505440883277824000000000000
    assert fact(52) > 2 ** 52 * 10 ** 40
    assert fact(52) > 52 ** 10 * 10 ** 40

def test_factorial_gt_2_pow_n_false_before_4_true_from_4():
    # why the honest base case is n = 4, not 0
    assert [n for n in range(0, 12) if fact(n) > 2 ** n] == list(range(4, 12))
    assert not fact(0) > 2 ** 0          # 1 > 1 is false
    assert fact(4) == 24 > 16 == 2 ** 4  # the base case

def test_factorial_step_inequality():
    # inductive step: (k+1)! = (k+1) k! > (k+1) 2^k >= 2 * 2^k  when k+1 >= 2
    assert all(fact(k + 1) == (k + 1) * fact(k) for k in range(0, 30))
    assert all(fact(k) > 2 ** k and (k + 1) * 2 ** k > 2 ** (k + 1)
               for k in range(4, 30))

def test_factorial_overtakes_n_pow_10_at_n_15():
    assert first_n_where_factorial_wins(lambda n: n ** 10) == 15

# 4b. Polynomials as recurrences (Horner) ----------------------------------
def test_factorial_reduction_trace_5():
    # f(5)=5*f(4)=5*4*f(3)=...=5*4*3*2*1*f(0); f(0)=1
    assert [fact(k) for k in range(6)] == [1, 1, 2, 6, 24, 120]

def test_horner_small_cubic_trace():
    # p(x) = 2x^3 - 6x^2 + 2x - 1 at x = 3
    value, steps = horner([2, -6, 2, -1], 3)
    assert steps == [2, 0, 2, 5]          # p_0..p_3
    assert value == 5

def test_horner_matches_direct_evaluation():
    coeffs = [2, -6, 2, -1]
    assert direct_eval(coeffs, 3) == 2 * 27 - 6 * 9 + 2 * 3 - 1 == 5
    assert all(horner(coeffs, x)[0] == direct_eval(coeffs, x)
               for x in range(-5, 6))

def test_horner_operation_count_payoff():
    # degree 3: direct 9 mults, Horner 3. degree 10: 65 vs 10.
    assert op_counts(3)["direct"][0] == 9 and op_counts(3)["horner"][0] == 3
    assert op_counts(10)["direct"][0] == 65 and op_counts(10)["horner"][0] == 10

# 4c. Sum of the first n odd numbers = n^2 ---------------------------------
def test_odd_sum_is_n_squared():
    assert [odd_sum(n) for n in range(6)] == [0, 1, 4, 9, 16, 25]
    assert all(odd_sum(n) == n * n for n in range(0, 50))   # evidence; proof is by induction

def test_L_picture_shape():
    assert L_picture(3).splitlines() == ["1 2 3", "2 2 3", "3 3 3"]


# 4. Find the bug ----------------------------------------------------------
def test_no_base_case_hits_guard():
    with pytest.raises(RecursionError):
        bad_no_base(3)

def test_bad_T_never_reaches_base_for_positive_input():
    with pytest.raises(RecursionError):
        bad_T(1)    # smallest input that exposes the problem

def test_bad_T_zero_looks_fine():
    assert bad_T(0) == 1    # why "it worked once" is not evidence

def test_bogus_step_points_backward():
    # P(k+1) => P(k): "proves" the true claim by an invalid direction, and
    # would equally "prove" a false one. Only P(k) => P(k+1) is a bridge.
    assert odd_sum_bogus_step(4, 25) == 16
    assert odd_sum_bogus_step(4, 26) == 17    # false claim, same "proof"
