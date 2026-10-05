"""Week 8 Tuesday live-coding examples, in teaching order.

1. S(n)   -- sum 1..n, the gentle first example
2. fact(n)
3. fib(n) -- correctness: BOTH base cases (speed was Week 6)
4. the bug demo -- definitions that fail, guarded so they cannot hang a laptop
"""
from functools import lru_cache


# ---- 1. Sum: S(0) = 0, S(n) = n + S(n-1) ---------------------------------
def S(n):
    if n == 0:                    # base case
        return 0
    return n + S(n - 1)           # reduction: n -> n-1 moves toward 0


def S_closed(n):
    return n * (n + 1) // 2       # the claim we prove by induction


# ---- 2. Factorial: 0! = 1, n! = n * (n-1)! -------------------------------
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


# ---- 3. Fibonacci: F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) -------------
def fib(n):
    if n == 0:                    # base case 1
        return 0
    if n == 1:                    # base case 2 (needed: step reaches back TWO)
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_missing_base(n):
    """BROKEN on purpose: only F(0) is a base case. Guarded by a depth limit."""
    def go(k, depth):
        if depth > 50:
            raise RecursionError("no base case reached")
        if k == 0:
            return 0
        return go(k - 1, depth + 1) + go(k - 2, depth + 1)
    return go(n, 0)


def fib_wrong_base(n):
    """BROKEN on purpose: F(1) wrongly set to 0, so every value is 0."""
    if n < 2:
        return 0
    return fib_wrong_base(n - 1) + fib_wrong_base(n - 2)


# ---- 4. Find the bug ------------------------------------------------------
def bad_no_base(n, depth=0):
    """S with the base case deleted: never terminates (guard stops it at 100)."""
    if depth > 100:
        raise RecursionError("depth guard hit: no base case")
    return n + bad_no_base(n - 1, depth + 1)


def bad_T(n, depth=0):
    """The activity's T: T(0)=1, T(n)=T(n+1). The 'reduction' goes UP."""
    if depth > 100:
        raise RecursionError("depth guard hit: input never reaches base case")
    if n == 0:
        return 1
    return bad_T(n + 1, depth + 1)
