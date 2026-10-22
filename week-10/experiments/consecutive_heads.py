#!/usr/bin/env python3
"""Exact math and small simulations for waiting on consecutive fair-coin heads.

Run: python3 week-10/experiments/consecutive_heads.py
Optional: python3 week-10/experiments/consecutive_heads.py --trials 3000 --max-sim-target 12 --seed 2043
"""

import argparse
import random
from fractions import Fraction


def expected_wait_flips(n):
    """Compute the exact expectation by recurrence for a fair coin.

    Let E[k] be the expected additional tosses with k consecutive heads
    already in hand. A tail resets to state 0, so E[k] = 1 + (E[k+1] + E[0])/2.
    Solving backward from E[n] = 0 gives E[0] = 2**(n+1) - 2.
    The recurrence keeps the computation linear even when n is enormous.
    """
    if n < 1:
        raise ValueError("run length must be positive")
    expectation_at_zero = 0
    for _ in range(n):
        expectation_at_zero = 2 * (expectation_at_zero + 1)
    return expectation_at_zero


def batch_expected_flips(n):
    """Expected flips for independent, non-overlapping batches of n all-heads."""
    return n * 2**n


def format_big(n):
    return f"{n:,}"


def human_time(flips):
    """Wall time at one flip per second, for intuition about scale."""
    if flips < 3600:
        return f"{flips / 60:,.1f} minutes"
    if flips < 86400:
        return f"{flips / 3600:,.1f} hours"
    if flips < 365.25 * 86400:
        return f"{flips / 86400:,.1f} days"
    return f"{flips / (365.25 * 86400):,.2g} years"


def simulate_continuous(n, trials, rng):
    """Return stopping times (toss counts) for independent continuous runs."""
    waits = []
    for _ in range(trials):
        run = tosses = 0
        while run < n:
            tosses += 1
            run = run + 1 if rng.getrandbits(1) else 0
        waits.append(tosses)
    return waits


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trials", type=int, default=3000,
                        help="independent continuous-run simulations per target (default: 3000)")
    parser.add_argument("--max-sim-target", type=int, default=12,
                        help="largest n to simulate; choose a modest value (default: 12)")
    parser.add_argument("--seed", type=int, default=2043,
                        help="random seed for reproducible simulation (default: 2043)")
    args = parser.parse_args()
    if args.trials < 1 or args.max_sim_target < 1:
        parser.error("--trials and --max-sim-target must be positive")

    print("CONSECUTIVE HEADS: exact expectations, then small experiments")
    print("Fair independent tosses; one toss per second only for scale comparisons.\n")
    print("Specified sequence means H repeated n times: probability = (1/2)^n.")
    print("Continuous waiting allows overlapping candidate runs; its expectation is 2^(n+1)-2.")
    print("Independent n-toss batches discard partial runs; expectation is n*2^n flips.\n")
    print(f"{'n':>3}  {'P(H^n) exact':>16}  {'continuous E flips':>22}  {'batch E flips':>18}  {'continuous @1 toss/s':>20}")
    for n in range(2, 101):
        probability = Fraction(1, 2**n)
        continuous = expected_wait_flips(n)
        print(f"{n:>3}  {str(probability):>16}  {format_big(continuous):>22}  {format_big(batch_expected_flips(n)):>18}  {human_time(continuous):>20}")

    print("\nSMALL-TARGET SIMULATION (continuous sequence; independent trials)")
    print(f"Seed={args.seed}; trials per target={args.trials}; simulation cap n={args.max_sim_target}.")
    rng = random.Random(args.seed)
    print(f"{'n':>3}  {'exact E':>12}  {'simulated mean':>16}  {'median':>10}  {'max observed':>13}")
    for n in range(2, min(args.max_sim_target, 100) + 1):
        waits = simulate_continuous(n, args.trials, rng)
        mean = sum(waits) / len(waits)
        ordered = sorted(waits)
        median = ordered[len(ordered) // 2]
        print(f"{n:>3}  {expected_wait_flips(n):>12,}  {mean:>16,.2f}  {ordered[len(ordered) // 2]:>10,}  {max(waits):>13,}")

    print("\nWHY STOP SIMULATING? For n=100:")
    exact = expected_wait_flips(100)
    print(f"  Exact continuous expectation: {exact:,} tosses ({human_time(exact)} at 1 toss/s).")
    print("  A specified 100-flip block is all heads with probability 1/2^100.")
    print("  A finite simulation can show small-n behavior and check code; it cannot practically")
    print("  wait for the n=100 event. Exact mathematics answers that question directly.\n")

    print("THE 101ST FLIP")
    print("  Conditional on having just seen 100 heads, the next independent fair toss is still")
    print("  heads with probability 1/2 (and tails with probability 1/2). The prefix changes no odds.")
    print("  A simulation may start at that already-qualified state and sample the next toss: this")
    print("  tests the conditional model, but does not observe the astronomically rare 100-head prefix.")
    print("  Conditioning mathematically is valid; claiming the run was observed by simulation is not.")


if __name__ == "__main__":
    main()
