import random

STREAK_LENGTH = 5
NUMBER_OF_EXPERIMENTS = 100_000


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


print(f"One experiment = flip a fair coin {STREAK_LENGTH} times.")
print("Here are 5 sample experiments so you can see what one looks like:\n")
for experiment_number in range(1, 6):
    flips = flip_fair_coin_several_times(STREAK_LENGTH)
    print(f"Experiment {experiment_number}: {flips}  streak? {every_flip_was_heads(flips)}")

experiments_that_made_a_streak = 0
for _ in range(NUMBER_OF_EXPERIMENTS):
    flips = flip_fair_coin_several_times(STREAK_LENGTH)
    if every_flip_was_heads(flips):
        experiments_that_made_a_streak += 1

measured_chance = experiments_that_made_a_streak / NUMBER_OF_EXPERIMENTS
predicted_chance = 0.5 ** STREAK_LENGTH

print(f"\nRan {NUMBER_OF_EXPERIMENTS:,} experiments.")
print(f"{experiments_that_made_a_streak:,} of them were {STREAK_LENGTH} HEADS in a row.")
print(f"Measured chance of a streak : {measured_chance:.4f}")
print(f"Predicted chance (1/2)^{STREAK_LENGTH}   : {predicted_chance:.4f}  (that is 1 in {2 ** STREAK_LENGTH})")
