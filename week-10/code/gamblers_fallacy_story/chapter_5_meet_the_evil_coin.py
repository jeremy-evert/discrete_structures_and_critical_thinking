import random

CHANCE_OF_HEADS = {
    "fair coin": 0.5,   # heads on one side, tails on the other
    "evil coin": 1.0,   # heads on BOTH sides
}


def flip_coin(coin_name):
    """Flip any coin. The coin's chance of HEADS decides how much of the number line is HEADS."""
    chance_this_coin_lands_heads = CHANCE_OF_HEADS[coin_name]
    if random.random() < chance_this_coin_lands_heads:
        return "HEADS"
    return "TAILS"


for coin_name in CHANCE_OF_HEADS:
    flips = [flip_coin(coin_name) for _ in range(10)]
    print(f"{coin_name}: {flips}")

print("\nThe fair coin and the evil coin are the same code with a different number.")
print("Notice: the fair coin CAN make 5 HEADS in a row too. A streak alone does not prove evil.")
