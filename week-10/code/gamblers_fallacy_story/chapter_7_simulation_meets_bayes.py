import random

NUMBER_OF_EXPERIMENTS = 200_000
LONGEST_STREAK_TO_TEST = 10

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


def simulate_the_bag(streak_length):
    """Run many experiments. Return (chance we hold the evil coin, chance next flip is HEADS) after a streak."""
    streaks_seen = 0
    streaks_made_by_evil_coin = 0
    heads_on_the_next_flip = 0
    for _ in range(NUMBER_OF_EXPERIMENTS):
        coin_in_hand = grab_coin_from_bag_without_looking()
        if coin_makes_a_streak(coin_in_hand, streak_length):
            streaks_seen += 1
            if coin_in_hand == "evil coin":
                streaks_made_by_evil_coin += 1
            if flip_coin(coin_in_hand) == "HEADS":
                heads_on_the_next_flip += 1
    return streaks_made_by_evil_coin / streaks_seen, heads_on_the_next_flip / streaks_seen


def bayes_chance_we_hold_the_evil_coin(streak_length):
    """Bayes' rule, written out in words instead of symbols."""
    chance_of_grabbing_evil = BAG_OF_COINS.count("evil coin") / len(BAG_OF_COINS)
    chance_of_grabbing_fair = BAG_OF_COINS.count("fair coin") / len(BAG_OF_COINS)
    chance_evil_coin_makes_streak = 1.0
    chance_fair_coin_makes_streak = 0.5 ** streak_length
    ways_to_get_streak_with_evil_coin = chance_of_grabbing_evil * chance_evil_coin_makes_streak
    ways_to_get_streak_with_fair_coin = chance_of_grabbing_fair * chance_fair_coin_makes_streak
    return ways_to_get_streak_with_evil_coin / (ways_to_get_streak_with_evil_coin + ways_to_get_streak_with_fair_coin)


def bayes_chance_next_flip_is_heads(streak_length):
    """If evil: HEADS for sure. If fair: HEADS half the time. Blend them."""
    chance_evil = bayes_chance_we_hold_the_evil_coin(streak_length)
    chance_fair = 1 - chance_evil
    return chance_evil * 1.0 + chance_fair * 0.5


print("        Holding the evil coin?    Next flip is HEADS?")
print("Streak   simulated    Bayes        simulated    Bayes")
print("------   ---------   ------        ---------   ------")
for streak_length in range(0, LONGEST_STREAK_TO_TEST + 1):
    simulated_evil, simulated_next_heads = simulate_the_bag(streak_length)
    bayes_evil = bayes_chance_we_hold_the_evil_coin(streak_length)
    bayes_next_heads = bayes_chance_next_flip_is_heads(streak_length)
    print(f"{streak_length:6}   {simulated_evil:9.1%}   {bayes_evil:6.1%}"
          f"        {simulated_next_heads:9.1%}   {bayes_next_heads:6.1%}")

print("\nThe longer the streak, the MORE likely HEADS gets. The gambler had it backwards.")
