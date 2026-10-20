import random


def flip_fair_coin():
    """Flip a fair coin once. Half of the number line is HEADS, half is TAILS."""
    if random.random() < 0.5:
        return "HEADS"
    return "TAILS"


def fraction_of_flips_that_are_heads(number_of_flips):
    """Flip the coin many times and report what fraction came up HEADS."""
    heads_count = 0
    for _ in range(number_of_flips):
        if flip_fair_coin() == "HEADS":
            heads_count += 1
    return heads_count / number_of_flips


print("How often does a fair coin land HEADS?\n")
for number_of_flips in [1, 2, 4, 6, 8, 10, 100, 1_000, 10_000, 100_000, 1_000_000]:
    fraction = fraction_of_flips_that_are_heads(number_of_flips)
    print(f"{number_of_flips:>9,} flips: HEADS {fraction:.3f} of the time")

print("\nFew flips: the answer wobbles. Many flips: it settles near 0.500.")
