import random

def fair_coin_after_streak(trials=1_000_000, streak=5):
    """After 'streak' heads in a row on a fair coin, how often is the next flip heads?"""
    next_heads = 0
    streaks_seen = 0
    for _ in range(trials):
        flips = [random.random() < 0.5 for _ in range(streak + 1)]
        if all(flips[:streak]):
            streaks_seen += 1
            next_heads += flips[streak]
    print(f"Fair coin: {streaks_seen} streaks of {streak} heads, next was heads {next_heads/streaks_seen:.3f} of the time")

def bag_of_coins_after_streak(trials=1_000_000, streak=5):
    """Pick from 99 fair coins + 1 two-headed coin. After 'streak' heads, how often is the next flip heads?"""
    next_heads = 0
    streaks_seen = 0
    for _ in range(trials):
        is_evil = random.randrange(100) == 0
        heads_chance = 1.0 if is_evil else 0.5
        flips = [random.random() < heads_chance for _ in range(streak + 1)]
        if all(flips[:streak]):
            streaks_seen += 1
            next_heads += flips[streak]
    print(f"Bag of coins: after {streak} heads, next was heads {next_heads/streaks_seen:.3f} of the time")

fair_coin_after_streak()
bag_of_coins_after_streak(streak=5)
bag_of_coins_after_streak(streak=10)