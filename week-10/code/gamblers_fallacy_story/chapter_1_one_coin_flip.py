import random

print("We will flip a fair coin 10 times.")
print("Each flip, the computer picks a random number between 0 and 1.")
print("Below 0.5 means HEADS. 0.5 or above means TAILS.\n")

for flip_number in range(1, 11):
    random_number = random.random()
    if random_number < 0.5:
        coin_landed_on = "HEADS"
    else:
        coin_landed_on = "TAILS"
    print(f"Flip {flip_number:2}: random number {random_number:.3f}  ->  {coin_landed_on}")
