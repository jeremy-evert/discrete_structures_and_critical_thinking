from colorama import init, Fore
import random

init(autoreset=True)

BACON = {
    'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB',
    'E': 'AABAA', 'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB',
    'I': 'ABAAA', 'J': 'ABAAB', 'K': 'ABABA', 'L': 'ABABB',
    'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA', 'P': 'ABBBB',
    'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
    'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB',
    'Y': 'BBAAA', 'Z': 'BBAAB'
}

REVERSE = {v: k for k, v in BACON.items()}

score = 0

QBS = [
    "MAHOMES",
    "ALLEN",
    "BURROW",
    "HURTS",
    "JACKSON",
    "LOVE",
    "PRESCOTT"
]

TEAMS = [
    "CHIEFS",
    "EAGLES",
    "RAVENS",
    "COWBOYS",
    "VIKINGS",
    "PACKERS",
    "LIONS"
]

FOOTBALL = [
    "TOUCHDOWN",
    "FUMBLE",
    "BLITZ",
    "OFFENSE",
    "DEFENSE",
    "SACK",
    "PLAYOFF",
    "TACKLE"
]


def encode(text):
    return " ".join(BACON[c] for c in text.upper() if c in BACON)


def decode(cipher):
    return "".join(REVERSE.get(x, "?") for x in cipher.split())


def color_cipher(cipher):
    colored = ""

    for char in cipher:
        if char == "A":
            colored += Fore.GREEN + "A"
        elif char == "B":
            colored += Fore.RED + "B"
        else:
            colored += char

    return colored


def rank():
    if score >= 150:
        return "🏆 Hall of Famer"
    elif score >= 100:
        return "⭐ MVP"
    elif score >= 50:
        return "🔥 Pro Bowler"
    elif score >= 20:
        return "🏈 Starter"
    else:
        return "👶 Rookie"


def challenge():
    global score

    category_name, word_list = random.choice([
        ("Quarterbacks", QBS),
        ("NFL Teams", TEAMS),
        ("Football Terms", FOOTBALL)
    ])

    word = random.choice(word_list)

    all_words = QBS + TEAMS + FOOTBALL

    options = [word]

    similar = [
        w for w in all_words
        if w != word and (
            len(w) == len(word) or
            w[0] == word[0]
        )
    ]

    while len(options) < 4 and similar:
        pick = random.choice(similar)

        if pick not in options:
            options.append(pick)

    while len(options) < 4:
        pick = random.choice(all_words)

        if pick not in options:
            options.append(pick)

    random.shuffle(options)

    print("\n🏈 NFL CIPHER CHALLENGE 🏈")
    print("=" * 45)

    print(f"\nCategory: {category_name}")

    cipher = encode(word)

    print("\nDecode this:")
    print(color_cipher(cipher))

    print(f"\nHint #1: {len(word)} letters")
    print(f"Hint #2: Starts with '{word[0]}'")

    print("\nPossible Answers:\n")

    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    answer = input("\nChoose (1-4): ")

    try:
        selected = options[int(answer) - 1]

        if selected == word:
            print(Fore.GREEN + "\n✅ TOUCHDOWN!")
            score += 10
            print(Fore.GREEN + f"You earned 10 points!")
        else:
            print(Fore.RED + "\n❌ INTERCEPTION!")
            print(Fore.YELLOW + f"The answer was {word}")

    except:
        print(Fore.YELLOW + "\nInvalid selection.")


while True:

    print("\n" + "=" * 50)
    print("🏈 NFL BACONIAN CHALLENGE 🏈")
    print("=" * 50)
    print("1. Encode Message")
    print("2. Decode Message")
    print("3. NFL Challenge")
    print("4. View Score & Rank")
    print("5. Exit")

    choice = input("\nChoose: ")

    if choice == "1":

        msg = input("\nEnter Message: ")

        print("\nEncoded:")
        print(color_cipher(encode(msg)))

    elif choice == "2":

        cipher = input("\nEnter Cipher: ")

        print("\nDecoded:")
        print(decode(cipher))

    elif choice == "3":

        challenge()

    elif choice == "4":

        print("\n🏈 PLAYER STATS 🏈")
        print("=" * 25)
        print(f"Score: {score}")
        print(f"Rank: {rank()}")

    elif choice == "5":

        print("\nThanks for playing!")
        print("See you next game day. 🏈")
        break

    else:

        print(Fore.YELLOW + "Invalid Selection.")