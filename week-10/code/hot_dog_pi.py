"""
hot_dog_pi.py
Estimate pi by throwing simulated hot dogs at a square box with a round bucket inside it.

Box:    square from -1 to 1 on each side   -> area 4
Bucket: circle of radius 1 in the middle    -> area pi
Chance a random hot dog lands in the bucket = pi / 4
So: pi is about 4 * (hot dogs in bucket) / (hot dogs in box)
"""

import math
import random
import sys

import matplotlib.pyplot as plt

EXPERIMENT_SIZES = [10, 25, 50, 100, 250, 500, 1_000, 2_500, 5_000,
                    10_000, 25_000, 50_000, 100_000]
SETTLED_TOLERANCE = 0.01


def throw_hot_dog(rng):
    x = rng.uniform(-1, 1)
    y = rng.uniform(-1, 1)
    return x * x + y * y <= 1


def run_experiment(total_throws, rng):
    """Return the running pi estimate after throw 1, 2, 3, ... total_throws."""
    hot_dogs_in_bucket = 0
    running_estimates = []
    for throw_number in range(1, total_throws + 1):
        if throw_hot_dog(rng):
            hot_dogs_in_bucket += 1
        running_estimates.append(4 * hot_dogs_in_bucket / throw_number)
    return running_estimates


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else None
    rng = random.Random(seed)

    print(f"Seed: {seed if seed is not None else 'random (pass a number to repeat a run)'}")
    print(f"{'hot dogs':>10} {'pi estimate':>12} {'error':>10} {'expected +/-':>13}  settled?")
    print("-" * 60)

    final_estimates = []
    figure, (running_plot, final_plot) = plt.subplots(2, 1, figsize=(11, 9))

    for total_throws in EXPERIMENT_SIZES:
        running_estimates = run_experiment(total_throws, rng)
        final_estimate = running_estimates[-1]
        final_estimates.append(final_estimate)

        error = final_estimate - math.pi
        expected_spread = math.sqrt(math.pi * (4 - math.pi)) / math.sqrt(total_throws)
        settled = "yes" if abs(error) < SETTLED_TOLERANCE else ""
        print(f"{total_throws:>10,} {final_estimate:>12.5f} {error:>+10.5f} {expected_spread:>13.5f}  {settled}")

        throw_numbers = range(1, total_throws + 1)
        running_plot.plot(throw_numbers, running_estimates, linewidth=0.8,
                          label=f"{total_throws:,} hot dogs")

    running_plot.axhline(math.pi, color="black", linestyle="--", label="true pi")
    running_plot.set_xscale("log")
    running_plot.set_ylim(2.0, 4.2)
    running_plot.set_xlabel("hot dogs thrown so far (log scale)")
    running_plot.set_ylabel("pi estimate")
    running_plot.set_title("Each experiment's running estimate of pi")
    running_plot.legend(fontsize=7, ncol=2, loc="lower right")

    spread = [math.sqrt(math.pi * (4 - math.pi)) / math.sqrt(n) for n in EXPERIMENT_SIZES]
    final_plot.fill_between(EXPERIMENT_SIZES,
                            [math.pi - 2 * s for s in spread],
                            [math.pi + 2 * s for s in spread],
                            alpha=0.2, label="expected range (about 95%)")
    final_plot.plot(EXPERIMENT_SIZES, final_estimates, "o-", label="final estimate")
    final_plot.axhline(math.pi, color="black", linestyle="--", label="true pi")
    final_plot.set_xscale("log")
    final_plot.set_xlabel("total hot dogs in the experiment (log scale)")
    final_plot.set_ylabel("final pi estimate")
    final_plot.set_title("Final estimate per experiment: the funnel closes in on pi")
    final_plot.legend()

    figure.tight_layout()
    figure.savefig("hot_dog_pi.png", dpi=150)
    print("\nSaved graph to hot_dog_pi.png")
    plt.show()


if __name__ == "__main__":
    main()