print("⚔️ HERO LEVELING GAME ⚔️")
print("=" * 25)

while True:
    try:
        n = int(input("\nHow many monsters do you want to defeat? "))

        if n < 1:
            print("❌ Enter a number greater than 0.")
            continue

        xp = 0

        print("\n🗡️ Battle Log:")
        for i in range(1, n + 1):
            xp += i
            print(f"Monster {i} defeated! +{i} XP | Total XP: {xp}")

        print(f"\n🏆 Total XP Earned: {xp}")

        if xp < 50:
            print("🥉 Rank: Novice")
        elif xp < 150:
            print("🥈 Rank: Warrior")
        elif xp < 300:
            print("🥇 Rank: Knight")
        else:
            print("👑 Rank: Legendary Hero")

        again = input("\nPlay again? (y/n): ").lower()

        if again != "y":
            print("👋 Thanks for playing!")
            break

    except ValueError:
        print("❌ Please enter a valid integer.")