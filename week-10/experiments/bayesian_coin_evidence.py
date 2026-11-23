#!/usr/bin/env python3
"""Bayesian evidence for a fair coin versus a 90%-heads coin.

Run: python3 week-10/experiments/bayesian_coin_evidence.py
Optional: --trials 100000 --seed 2043

Model: exactly one coin type is selected once, then tosses are independent:
F has P(H)=1/2; W has P(H)=9/10. Evidence is n consecutive heads.
"""

import argparse
import random
from fractions import Fraction

PRIORS = (Fraction(1, 1000), Fraction(1, 10), Fraction(1, 2))
THRESHOLDS = (Fraction(1, 2), Fraction(9, 10), Fraction(99, 100))


def posterior(prior, heads):
    """Bayes theorem using exact rational arithmetic."""
    likelihood_weighted = Fraction(9, 10) ** heads
    likelihood_fair = Fraction(1, 2) ** heads
    return (likelihood_weighted * prior) / (
        likelihood_weighted * prior + likelihood_fair * (1 - prior)
    )


def posterior_odds(prior, heads):
    """Independent log-odds calculation: prior odds x likelihood ratio."""
    if prior == 0:
        return 0.0
    if prior == 1:
        return 1.0
    prior_odds = float(prior / (1 - prior))
    odds = prior_odds * (1.8 ** heads)
    return odds / (1 + odds)


def first_over(prior, threshold, maximum=1000):
    for n in range(1, maximum + 1):
        if posterior(prior, n) > threshold:
            return n
    return None


def simulate_fixed_dataset(prior, heads, trials, rng):
    """Simulate repeated datasets conditional on observing all heads.

    Each replicate first samples a coin type from the prior, then samples heads.
    The returned proportion is W among replicates whose evidence was all heads.
    """
    weighted_and_evidence = evidence = 0
    for _ in range(trials):
        weighted = rng.random() < float(prior)
        p_heads = 0.9 if weighted else 0.5
        observed = all(rng.random() < p_heads for _ in range(heads))
        if observed:
            evidence += 1
            weighted_and_evidence += int(weighted)
    return weighted_and_evidence, evidence


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trials", type=int, default=1_000_000,
                        help="Monte Carlo candidate datasets (default: 1,000,000)")
    parser.add_argument("--seed", type=int, default=2043)
    args = parser.parse_args()
    if args.trials < 1:
        parser.error("--trials must be positive")

    print("MODEL: one coin type is selected once; tosses are independent given its type.")
    print("Fair: P(H)=0.50; weighted: P(H)=0.90; evidence: n consecutive heads.\n")
    print("POSTERIOR PROBABILITY THE COIN IS WEIGHTED")
    print(f"{'n':>2}  " + "  ".join(f"prior {float(p)*100:>5.1f}%" for p in PRIORS))
    for n in range(1, 26):
        values = "  ".join(f"{float(posterior(prior, n))*100:>8.3f}%" for prior in PRIORS)
        print(f"{n:>2}  {values}")

    print("\nFIRST n WHERE POSTERIOR EXCEEDS THRESHOLD (strictly greater)")
    print(f"{'prior':>8}  " + "  ".join(f">{float(t)*100:.0f}%" for t in THRESHOLDS))
    for prior in PRIORS:
        values = "  ".join(str(first_over(prior, t)) for t in THRESHOLDS)
        print(f"{float(prior)*100:>7.1f}%  {values}")

    n = 15
    p = posterior(PRIORS[0], n)
    print("\nNELL'S 15-HEAD CLAIM (prior weighted = 0.1%)")
    print(f"Exact posterior: {p} = {float(p)*100:.6f}% (about {float(p)*100:.1f}%).")
    print("So the stated approximately 87% prediction is supported under this model.")

    print("\n$100 BET: expected value depends on the contract and payout.")
    print("Assume a $100 stake buys a bet that pays the listed net profit if W, and loses $100 if F.")
    print("With posterior p, EV = p * net profit - (1-p) * $100.")
    print(f"At n=15 and prior 0.1%, p={float(p):.6f}; break-even net profit is ${(1-float(p))/float(p)*100:,.2f}.")
    print(f"{'net profit if W':>20}  {'EV per $100 stake':>20}")
    for profit in (100, 500, 700, 750, 1000):
        ev = float(p) * profit - (1 - float(p)) * 100
        print(f"${profit:>19,.0f}  ${ev:>19,.2f}")
    print("A stated $100 bet alone omits the payoff and decision context; probability by itself cannot settle value.")

    print("\nINDEPENDENT MATHEMATICAL CHECK: PRIOR ODDS x LIKELIHOOD RATIO")
    for prior in PRIORS:
        maximum_difference = max(abs(float(posterior(prior, n)) - posterior_odds(prior, n))
                                 for n in range(1, 26))
        print(f"prior {float(prior)*100:>4.1f}%: max absolute difference through n=25 = {maximum_difference:.3g}")

    print("\nMONTE CARLO CHECK (simulation evidence, not exact answer)")
    rng = random.Random(args.seed)
    print(f"Seed={args.seed}; candidate datasets per prior={args.trials:,}; target n=5.")
    print(f"{'prior':>8}  {'qualifying datasets':>21}  {'sim posterior':>15}  {'exact posterior':>16}")
    for prior in PRIORS:
        weighted_and_evidence, evidence = simulate_fixed_dataset(prior, 5, args.trials, rng)
        simulated = weighted_and_evidence / evidence if evidence else float('nan')
        print(f"{float(prior)*100:>7.1f}%  {evidence:>21,}  {simulated*100:>14.3f}%  {float(posterior(prior, 5))*100:>15.3f}%")
    print("The Monte Carlo estimates fluctuate, especially when qualifying evidence is sparse; exact Bayes is the benchmark.")


if __name__ == "__main__":
    main()
