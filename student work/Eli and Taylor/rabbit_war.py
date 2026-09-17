import random

months = int(input("Months of rabbit warfare: "))

a = 1
b = 1

print("\n=== OFFICIAL BUNNY WAR REPORT ===\n")

for month in range(1, months + 1):

    if month == 1:
        rabbits = a
    elif month == 2:
        rabbits = b
    else:
        rabbits = a + b
        a = b
        b = rabbits

    events = [
        "captured a carrot fortress",
        "invaded the Celery Republic",
        "launched tactical lettuce strikes",
        "declared war on gravity",
        "built a moon burrow",
        "elected a turnip as emperor",
        "accidentally conquered Nebraska",
        "weaponized fluffiness"
    ]

    print(f"Month {month}: {rabbits} rabbits {random.choice(events)}.")

print("\nThe war ended when everyone forgot why it started.")
