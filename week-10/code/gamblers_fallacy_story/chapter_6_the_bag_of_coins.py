import random

STREAK_LENGTH = 5
NUMBER_OF_EXPERIMENTS = 1_000_000

CHANCE_OF_HEADS = {
    "fair coin": 0.5,
    "evil coin": 1.0,
}

BAG_OF_COINS = ["fair coin"] * 99 + ["evil coin"] * 1


def flip_coin(coin_name):
    """Flip any coin. The coin's chance of HEADS decides how much of the number line is HEADS."""
    chance_this_coin_lands_heads = CHANCE_OF_HEADS[coin_name]
    if random.random() < chance_this_coin_lands_heads:
        return "HEADS"
    return "TAILS"


def grab_coin_from_bag_without_looking():
    """Reach into the bag and pull out one coin at random."""
    return random.choice(BAG_OF_COINS)


def coin_makes_a_streak(coin_name, streak_length):
    """Flip until we get the streak, or stop early the moment TAILS shows up."""
    for _ in range(streak_length):
        if flip_coin(coin_name) == "TAILS":
            return False
    return True


print(f"The bag has {BAG_OF_COINS.count('fair coin')} fair coins and {BAG_OF_COINS.count('evil coin')} evil coin.")
print(f"Grab a coin without looking. Flip it {STREAK_LENGTH} times.")
print("Question: if it made a streak, how likely is it that we are holding the evil coin?\n")

grabbed_evil_coin_overall = 0
experiments_that_made_a_streak = 0
streaks_made_by_evil_coin = 0

for _ in range(NUMBER_OF_EXPERIMENTS):
    coin_in_hand = grab_coin_from_bag_without_looking()
    if coin_in_hand == "evil coin":
        grabbed_evil_coin_overall += 1
    if coin_makes_a_streak(coin_in_hand, STREAK_LENGTH):
        experiments_that_made_a_streak += 1
        if coin_in_hand == "evil coin":
            streaks_made_by_evil_coin += 1

print(f"BEFORE flipping: we held the evil coin {grabbed_evil_coin_overall / NUMBER_OF_EXPERIMENTS:.1%} of the time.")
print(f"AFTER seeing {STREAK_LENGTH} HEADS: we held the evil coin {streaks_made_by_evil_coin / experiments_that_made_a_streak:.1%} of the time.")
print("\nThe flips did not change the coin. They changed what we KNOW about the coin.")
