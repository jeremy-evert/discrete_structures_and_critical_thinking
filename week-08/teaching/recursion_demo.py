"""Week 8 Tuesday live-coding examples, in teaching order.

0. pattern is not proof: regions of a circle (2^(n-1) fails at n=6)
0b. one problem, five strategies; when recursion is the natural fit

1. S(n)   -- sum 1..n, the gentle first example
2. fact(n)
3. fib(n) -- correctness: BOTH base cases (speed was Week 6)
4. growth: n! vs 2^n vs n^k, Horner as a recurrence, odd numbers = n^2
5. the bug demo -- definitions that fail, guarded so they cannot hang a laptop
"""
from functools import lru_cache


# ---- 0. Pattern is not proof: regions cut by chords of a circle ----------
from math import comb, sqrt


def regions(n):
    """Max regions when n points on a circle are joined by all chords."""
    return comb(n, 4) + comb(n, 2) + 1


def regions_recursive(n):
    if n == 1:                      # base case
        return 1
    return regions_recursive(n - 1) + (n - 1) + comb(n - 1, 3)   # recursive step


def regions_closed(n):
    return comb(n, 4) + comb(n, 2) + 1


def guess_pow2(n):
    """The tempting pattern 1, 2, 4, 8, 16, ... (evidence, not a warrant)."""
    return 2 ** (n - 1)


# ---- 0b. One problem, five strategies: S(n) = 1 + 2 + ... + n ------------
def sum_recursive(n):
    return 0 if n == 0 else n + sum_recursive(n - 1)


def sum_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def sum_closed(n):
    return n * (n + 1) // 2              # Gauss: pair 1 with n, 2 with n-1, ...


def sum_memo(n, _table={0: 0}):
    """Dynamic programming: fill a table bottom-up, reuse earlier entries."""
    for i in range(len(_table), n + 1):
        _table[i] = _table[i - 1] + i
    return _table[n]


def sum_brute(n):
    """Brute-force enumeration: build every term, then add them all."""
    return sum(list(range(1, n + 1)))


# ... and Fibonacci, same idea (speed race = Week 6; here: which are *right*)
def fib_loop(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_memo(n, _cache={0: 0, 1: 1}):
    if n not in _cache:
        _cache[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return _cache[n]


def fib_closed(n):
    """Binet's formula in floating point: elegant, and WRONG for large n."""
    phi = (1 + sqrt(5)) / 2
    return round(phi ** n / sqrt(5))


def first_fib_closed_failure(limit=200):
    for n in range(limit):
        if fib_closed(n) != fib_loop(n):
            return n


# ---- When recursion is the natural fit: the DATA is recursive ------------
def nested_sum(x):
    """Add every number in a list that may contain lists, to any depth."""
    if isinstance(x, int):
        return x
    return sum(nested_sum(item) for item in x)


def merge_sort(xs):
    if len(xs) <= 1:                      # base case
        return xs
    mid = len(xs) // 2
    left, right = merge_sort(xs[:mid]), merge_sort(xs[mid:])   # halves
    out = []
    while left and right:
        out.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    return out + left + right


def ai_sum(n):
    """A plausible AI answer. Right for n = 1..4, wrong at the smallest input."""
    return n + ai_sum(n - 1) if n > 1 else 1


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


# ---- 4a. Growth: factorial vs exponential vs polynomial ------------------
def first_n_where_factorial_wins(base_fn, start=1, limit=200):
    """Smallest n >= start with n! > base_fn(n) that stays true through limit."""
    for n in range(start, limit):
        if all(fact(m) > base_fn(m) for m in range(n, limit)):
            return n
    return None


# ---- 4b. Polynomials as recurrences (Horner) -----------------------------
# p_0(x) = a_n ;  p_k(x) = x * p_{k-1}(x) + a_{n-k}   (coefficients high -> low)
def horner(coeffs, x):
    """coeffs = [a_n, ..., a_0]. Returns (value, list of p_k(x) steps)."""
    p = coeffs[0]
    steps = [p]
    for a in coeffs[1:]:
        p = x * p + a
        steps.append(p)
    return p, steps


def direct_eval(coeffs, x):
    """Term-by-term, each power built from scratch by repeated multiplication."""
    n = len(coeffs) - 1
    total = 0
    for i, a in enumerate(coeffs):
        power = 1
        for _ in range(n - i):
            power *= x
        total += a * power
    return total


def op_counts(n):
    """(mults, adds) for degree n: direct (naive powers) vs Horner."""
    direct_mults = sum(range(n + 1)) + n      # powers: n(n+1)/2, times a_i: n
    return {"direct": (direct_mults, n), "horner": (n, n)}


# ---- 4c. Sum of the first n odd numbers = n^2 ----------------------------
def odd_sum(n):
    if n == 0:
        return 0
    return odd_sum(n - 1) + (2 * n - 1)       # add the n-th L-shape


def L_picture(n):
    """ASCII square: the k-th L-shape is drawn with the digit k (mod 10)."""
    return "\n".join(
        " ".join(str(max(r, c) % 10 + 0) for c in range(1, n + 1))
        for r in range(1, n + 1)
    )


def odd_sum_bogus_step(k, claim_for_k_plus_1):
    """BROKEN on purpose: 'proves' P(k) from P(k+1) -- the arrow points backward."""
    return claim_for_k_plus_1 - (2 * k + 1)


# ---- 5. Find the bug ------------------------------------------------------
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
