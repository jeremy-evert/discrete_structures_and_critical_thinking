"""
hot_dog_digits.py
How many hot dogs do we need to get d correct digits of pi with 95% confidence?

Walks through the math one step at a time, then checks it with real simulated throws.

Run:   python hot_dog_digits.py            (pauses between steps)
       python hot_dog_digits.py --no-pause (runs straight through)
"""

import math
import random
import sys
import time

PAUSE = "--no-pause" not in sys.argv
CONFIDENCE_Z = 1.96            # 95% of random results land within 1.96 standard errors
CHANCE_IN_BUCKET = math.pi / 4 # bucket area / box area
DIGIT_TARGETS = [2, 3, 4, 6, 10, 15]


def pause():
    if PAUSE:
        input("\n   ...press Enter to continue...")


def banner(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def wobble_of_one_toss():
    """How much a single toss's contribution to the pi estimate jumps around."""
    p = CHANCE_IN_BUCKET
    return 4 * math.sqrt(p * (1 - p))


def allowed_error(correct_digits):
    """Half of the last digit we want right. 2 digits (3.1) -> 0.05."""
    return 0.5 * 10 ** -(correct_digits - 1)


def hot_dogs_needed(correct_digits):
    root_n = CONFIDENCE_Z * wobble_of_one_toss() / allowed_error(correct_digits)
    return root_n ** 2


def throw_hot_dogs(total_throws, rng):
    in_bucket = 0
    for _ in range(total_throws):
        x = rng.random()
        y = rng.random()
        if x * x + y * y <= 1:
            in_bucket += 1
    return 4 * in_bucket / total_throws


def step_1_one_toss():
    banner("STEP 1: How wobbly is ONE toss?")
    p = CHANCE_IN_BUCKET
    print(f"Chance a hot dog lands in the bucket:  p = pi/4 = {p:.5f}")
    print(f"Chance it misses:                  1 - p = {1 - p:.5f}")
    print("\nEach toss is a yes/no coin flip. A yes/no flip wobbles by sqrt(p(1-p)).")
    print(f"   sqrt({p:.5f} x {1 - p:.5f}) = {math.sqrt(p * (1 - p)):.5f}")
    print("We multiply the fraction by 4 to get pi, so the wobble gets multiplied by 4 too:")
    print(f"   4 x {math.sqrt(p * (1 - p)):.5f} = {wobble_of_one_toss():.5f}")
    print("\nOne toss alone moves our pi estimate by about 1.64. That is terrible.")
    pause()


def step_2_averaging():
    banner("STEP 2: Averaging N tosses shrinks the wobble by sqrt(N)")
    w = wobble_of_one_toss()
    print("standard error = 1.642 / sqrt(N)\n")
    print(f"{'N tosses':>12} {'sqrt(N)':>10} {'standard error':>16}")
    for n in [1, 4, 100, 10_000, 1_000_000]:
        print(f"{n:>12,} {math.sqrt(n):>10,.0f} {w / math.sqrt(n):>16.5f}")
    print("\nNotice: 100x more tosses only buys 10x less wobble.")
    pause()


def step_3_confidence():
    banner("STEP 3: What does 95% confidence mean?")
    print("Random results pile up in a bell curve.")
    print("95% of runs land within 1.96 standard errors of the true answer.")
    print("So we need:   1.96 x 1.642 / sqrt(N)  <  allowed error")
    print("Solve for N:  N  >  (1.96 x 1.642 / allowed error)^2")
    pause()


def step_4_each_row():
    banner("STEP 4: Build the table one row at a time")
    w = wobble_of_one_toss()
    for d in DIGIT_TARGETS:
        target = allowed_error(d)
        root_n = CONFIDENCE_Z * w / target
        n = root_n ** 2
        print(f"\n--- {d} correct digits: {math.pi:.{d - 1}f}")
        print(f"   allowed error   = 0.5 x 10^-{d - 1} = {target:.1e}")
        print(f"   sqrt(N)         = 1.96 x {w:.4f} / {target:.1e} = {root_n:.3e}")
        print(f"   N = sqrt(N)^2   = {n:.3e} hot dogs")
        pause()


def step_5_summary_and_timing():
    banner("STEP 5: The finished table, plus how long YOUR computer would take")
    rng = random.Random()
    sample = 1_000_000
    start = time.perf_counter()
    throw_hot_dogs(sample, rng)
    throws_per_second = sample / (time.perf_counter() - start)
    print(f"Your computer throws about {throws_per_second:,.0f} hot dogs per second.\n")

    print(f"{'digits':>6} {'allowed error':>14} {'hot dogs needed':>17} {'time on this PC':>22}")
    for d in DIGIT_TARGETS:
        n = hot_dogs_needed(d)
        print(f"{d:>6} {allowed_error(d):>14.1e} {n:>17.2e} {describe_time(n / throws_per_second):>22}")
    pause()


def describe_time(seconds):
    for unit, size in [("years", 31_557_600), ("days", 86_400), ("hours", 3_600), ("minutes", 60)]:
        if seconds >= size:
            return f"{seconds / size:,.3g} {unit}"
    return f"{seconds:.2f} seconds"


def step_6_prove_it():
    banner("STEP 6: Don't trust the math. Test it.")
    print("Run many separate experiments at the 'needed' size.")
    print("If the math is right, about 95% should land within the allowed error.\n")
    rng = random.Random()
    for d, experiments in [(2, 200), (3, 20)]:
        n = round(hot_dogs_needed(d))
        target = allowed_error(d)
        hits = 0
        print(f"{d} digits: {experiments} experiments of {n:,} hot dogs each (allowed error {target})")
        for i in range(1, experiments + 1):
            estimate = throw_hot_dogs(n, rng)
            close_enough = abs(estimate - math.pi) < target
            hits += close_enough
            if experiments <= 20 or i <= 5:
                print(f"   experiment {i:>3}: pi ~ {estimate:.5f}   {'OK' if close_enough else 'MISSED'}")
        print(f"   -> {hits}/{experiments} = {100 * hits / experiments:.0f}% landed close enough (math says ~95%)\n")


def main():
    step_1_one_toss()
    step_2_averaging()
    step_3_confidence()
    step_4_each_row()
    step_5_summary_and_timing()
    step_6_prove_it()
    print("Lesson: every extra digit of pi costs 100x more hot dogs.")


if __name__ == "__main__":
    main()