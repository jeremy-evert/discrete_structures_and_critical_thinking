import random

STREAK_LENGTH = 5
NUMBER_OF_EXPERIMENTS = 1_000_000


def flip_fair_coin():
    """Flip a fair coin once."""
    if random.random() < 0.5:
        return "HEADS"
    return "TAILS"


def flip_fair_coin_several_times(number_of_flips):
    """Flip the coin several times and return the list of results."""
    return [flip_fair_coin() for _ in range(number_of_flips)]


def every_flip_was_heads(flips):
    """True only when every single flip in the list is HEADS."""
    return all(flip == "HEADS" for flip in flips)


print("The gambler says: 'After 5 HEADS in a row, TAILS is due!'")
print("Let's test that. Whenever we see a streak, we flip ONE more time and write it down.\n")

experiments_that_made_a_streak = 0
heads_after_the_streak = 0
tails_after_the_streak = 0

for _ in range(NUMBER_OF_EXPERIMENTS):
    flips = flip_fair_coin_several_times(STREAK_LENGTH)
    if every_flip_was_heads(flips):
        experiments_that_made_a_streak += 1
        the_very_next_flip = flip_fair_coin()
        if the_very_next_flip == "HEADS":
            heads_after_the_streak += 1
        else:
            tails_after_the_streak += 1

print(f"Streaks of {STREAK_LENGTH} HEADS found: {experiments_that_made_a_streak:,}")
print(f"  Next flip was HEADS: {heads_after_the_streak:,}")
print(f"  Next flip was TAILS: {tails_after_the_streak:,}")
print(f"\nChance of HEADS after the streak: {heads_after_the_streak / experiments_that_made_a_streak:.3f}")
print("The coin has no memory. TAILS was never 'due'.")
