# The Gambler's Fallacy, Told With Coins

*Week 10 · Discrete Structures and Critical Thinking · SWOSU*

> **The one-sentence version:** a random thing never *owes* you a correction. A fair coin has no memory, and when the past *does* tell you something, it tells you the streak is more likely to keep going, not to reverse.

---

## How to use this folder

All the code lives next to this file:

```text
week-10/code/gamblers_fallacy_story/
├── README.md                              <- you are here
├── chapter_1_one_coin_flip.py
├── chapter_2_many_flips.py
├── chapter_3_how_rare_is_a_streak.py
├── chapter_4_the_gamblers_question.py
├── chapter_5_meet_the_evil_coin.py
├── chapter_6_the_bag_of_coins.py
└── chapter_7_simulation_meets_bayes.py
```

Run the chapters **in order**, from the `week-10\code` folder:

```powershell
python .\gamblers_fallacy_story\chapter_1_one_coin_flip.py
```

Each chapter runs by itself and adds **one** new idea. Every chapter takes a few seconds. Your numbers will be a little different from the sample runs below, because the flips are random. That's the point.

---

## Part 1: The idea, in four acts

### Act 1: A fair coin has no memory

You flip a fair coin and get **H H H H H**. What's the chance the next flip is heads?

$$P(\text{H on flip 6} \mid \text{5 heads so far}) = \frac{1}{2}$$

The confusion comes from mixing up two different questions:

| Question | Answer |
|---|---|
| *Before* you start, what's the chance of 6 heads in a row? | $(1/2)^6 = 1/64$ |
| *Given* 5 heads already happened, what's the chance the 6th is heads? | $1/2$ |

**HHHHHH** and **HHHHHT** each have probability 1/64. Once the first five flips are done, both endings are equally likely.

### Act 2: The die isn't "due" a 6

Ten rolls without a 6? The next roll is still $1/6$.

*"But the law of large numbers says it evens out!"* It does, but by **dilution**, not **correction**. Say you're 10 heads ahead after 20 flips (15 H, 5 T). After 1,000 more fair flips you'd expect about 515 H and 505 T. You're **still** 10 ahead, but the share of heads went from 75% to about 50.5%. The early streak never gets paid back. It gets buried.

### Act 3: One evil coin

The **Evil Coin** has heads on **both** sides, so it lands heads every time. After **H H H H H**, betting on tails is wrong twice over. The coin still has no memory, and heads streaks are exactly what this coin does.

### Act 4: A bag of 100 coins, and one of them is evil

The bag holds **99 fair coins** and **1 evil coin** with heads on both sides. You grab one without looking and keep getting heads.

Now the past *does* matter. It can't change the coin, but it changes **what you believe about which coin you're holding**. That's Bayes' rule:

$$P(\text{evil} \mid k \text{ heads}) = \frac{\frac{1}{100}\cdot 1}{\frac{1}{100}\cdot 1 + \frac{99}{100}\cdot\left(\frac{1}{2}\right)^k} = \frac{1}{1 + \frac{99}{2^k}}$$

$$P(\text{next H}) = P(\text{evil})\cdot 1 + P(\text{fair})\cdot\tfrac{1}{2}$$

| Heads in a row ($k$) | Chance it's the evil coin | Chance next flip is heads |
|---|---|---|
| 0 | 1.0% | 50.5% |
| 1 | 2.0% | 51.0% |
| 3 | 7.5% | 53.7% |
| 5 | 24.4% | 62.2% |
| 7 | 56.4% | 78.2% |
| 10 | 91.2% | 95.6% |

**The longer the streak, the *more* likely heads gets.** The gambler's fallacy points the wrong way.

### The big lesson

| Situation | What a streak of heads tells you about the next flip |
|---|---|
| Fair coin or fair die | Nothing. Still 1/2 (or 1/6). |
| Known evil coin | Nothing new. Still its usual chance. |
| Unknown coin from a bag | **More** likely heads, because you learned about the coin. |

In none of these cases does tails become "due."

**The one honest exception: drawing without replacement.** A deck of cards *does* have memory. If lots of low cards have been dealt, the cards left really are richer in high cards. That's why card counting works in Blackjack and "coin counting" doesn't.

---

## Part 2: Expected value of a fair die

There's no single most likely roll. All six faces tie at $1/6$. The **expected value** is the long-run average:

$$E[X] = \frac{1+2+3+4+5+6}{6} = \frac{21}{6} = 3.5$$

**Balance-point intuition:** $1+6 = 2+5 = 3+4 = 7$. Every pair averages to 3.5, so the faces balance between 3 and 4.

**The catch:** you can never roll a 3.5. Expected value describes the average over many rolls, not any single roll. If your first 10 rolls average 2.0, the die doesn't owe you high numbers. The average drifts back toward 3.5 by dilution, just like the coins.

---

## Part 3: Why Bayes matters, and why it's strange we know about him

### Why it matters

Most probability runs **forward**: *if this is the coin, what flips will I see?* Bayes runs it **backward**: *I saw these flips, so which coin do I probably have?*

$$P(\text{cause} \mid \text{evidence}) = \frac{P(\text{evidence} \mid \text{cause})\cdot P(\text{cause})}{P(\text{evidence})}$$

The same reasoning powers rare-disease screening (most positive tests for a rare disease are false positives), Bayesian spam filters (Rosen, *Discrete Mathematics and Its Applications*, Section 7.3), code-breaking at Bletchley Park, searches for a lost H-bomb and Soviet submarines, and the study that settled who wrote the disputed *Federalist Papers*.

### A short history

| When | What happened |
|---|---|
| c. 1701 | Thomas Bayes is born, son of a Presbyterian minister |
| 1719 | Studies logic and theology at the University of Edinburgh |
| 1731 | Publishes a book of **theology** |
| 1736 | **Anonymously** defends Newton's calculus against Bishop Berkeley |
| 1742 | Elected to the Royal Society, probably on the strength of that anonymous book |
| 1761 | Dies. His probability essay is still unpublished. |
| 1763 | His friend **Richard Price** finds and edits it. It's read to the Royal Society on December 23. |
| Later | **Laplace** independently develops the idea and gives it the modern form |
| 20th century | Leading statisticians attack it while codebreakers quietly use it |
| 21st century | It becomes mainstream |

### Why it's strange we know any of this

1. **He never published his most famous idea.** Price found it in his papers after he died.
2. **His math reputation rested on an anonymous book.**
3. **His family's religious group kept a low profile.** They were Nonconformists, outside the Church of England, and few records of his life survive.
4. **Even his birth records are missing.** One historian notes that an old parish register turned up in a hay loft, and another was cut up by a tailor for a measuring tape.
5. **We don't know what he looked like.** The one portrait everyone uses is doubtful.
6. **The textbook formula isn't in his essay in that form.** Laplace gave it the form we use.
7. **He seems to have set the work aside** and never returned to it.

**Classroom punchline:** Bayes's actual question was the **mystery coin** problem. A coin has some unknown chance of heads, and you've counted its successes and failures. What can you say about that chance? That's our bag of coins, about 260 years earlier.

---

## Part 4: Random isn't one thing (Python's random libraries)

| Library | What it's good at | Don't use it for |
|---|---|---|
| `random` | Games, simulations, classroom demos, **repeatable** results with `random.seed()` | Passwords or tokens |
| `secrets` | Passwords, login tokens, reset links | Repeatable experiments (you can't seed it) |
| `random.SystemRandom` | Secure randomness with the familiar `random` methods | Repeatable experiments |
| `numpy.random` | Millions of values at once, fast simulations | Security |
| `scipy.stats` | Specialized distributions | Simple dice games |
| `torch` / `jax` | Machine learning, randomness on the GPU | Security |

**Why so many?** "Random" can mean **repeatable**, **unguessable**, or **fast at scale**, and no single generator is best at all three. Python's `random` is *pseudo*-random: a formula. With the same seed you get the same sequence, which is great for science and terrible for passwords. Python's documentation warns not to use it for security.

**The thought to leave students with:** even the computer's "fair die" has no memory of past rolls. Yet the whole sequence was decided the moment you chose the seed.

---

## Part 5: The code story, one chapter at a time

The original version packed everything into two dense functions. This version starts slower, adds one idea per chapter, and uses names that read like English.

### Chapter 1: What *is* a coin flip to a computer?

**File:** `chapter_1_one_coin_flip.py`

```python
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
```

**Sample run:**

```text
We will flip a fair coin 10 times.
Each flip, the computer picks a random number between 0 and 1.
Below 0.5 means HEADS. 0.5 or above means TAILS.

Flip  1: random number 0.196  ->  HEADS
Flip  2: random number 0.604  ->  TAILS
Flip  3: random number 0.778  ->  TAILS
Flip  4: random number 0.639  ->  TAILS
Flip  5: random number 0.000  ->  HEADS
Flip  6: random number 0.087  ->  HEADS
Flip  7: random number 0.584  ->  TAILS
Flip  8: random number 0.872  ->  TAILS
Flip  9: random number 0.035  ->  HEADS
Flip 10: random number 0.380  ->  HEADS
```

**The intuition:** Picture a ruler from 0 to 1. The left half is painted HEADS and the right half TAILS. Each flip throws a dart at the ruler. This chapter shows every dart, so `random.random() < 0.5` stops being mysterious.

**Ask the class:** Is 0.5 itself heads or tails? (Tails: `<` means strictly less than.)

### Chapter 2: Does it really come out to half?

**File:** `chapter_2_many_flips.py`

```python
import random


def flip_fair_coin():
    """Flip a fair coin once. Half of the number line is HEADS, half is TAILS."""
    if random.random() < 0.5:
        return "HEADS"
    return "TAILS"


def fraction_of_flips_that_are_heads(number_of_flips):
    """Flip the coin many times and report what fraction came up HEADS."""
    heads_count = 0
    for _ in range(number_of_flips):
        if flip_fair_coin() == "HEADS":
            heads_count += 1
    return heads_count / number_of_flips


print("How often does a fair coin land HEADS?\n")
for number_of_flips in [10, 100, 1_000, 10_000, 100_000, 1_000_000]:
    fraction = fraction_of_flips_that_are_heads(number_of_flips)
    print(f"{number_of_flips:>9,} flips: HEADS {fraction:.3f} of the time")

print("\nFew flips: the answer wobbles. Many flips: it settles near 0.500.")
```

**Sample run:**

```text
How often does a fair coin land HEADS?

       10 flips: HEADS 0.600 of the time
      100 flips: HEADS 0.490 of the time
    1,000 flips: HEADS 0.502 of the time
   10,000 flips: HEADS 0.503 of the time
  100,000 flips: HEADS 0.501 of the time
1,000,000 flips: HEADS 0.500 of the time

Few flips: the answer wobbles. Many flips: it settles near 0.500.
```

**The intuition:** With 10 or 100 flips the fraction bounces around. By a million flips it settles near 0.500. That's dilution: the coin never corrects itself, but the wobble gets buried.

**Ask the class:** Why is the 100-flip row sometimes way off while the million-flip row almost never is?

### Chapter 3: How rare is a streak?

**File:** `chapter_3_how_rare_is_a_streak.py`

```python
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
```

**Sample run:**

```text
One experiment = flip a fair coin 5 times.
Here are 5 sample experiments so you can see what one looks like:

Experiment 1: ['TAILS', 'TAILS', 'TAILS', 'TAILS', 'HEADS']  streak? False
Experiment 2: ['TAILS', 'HEADS', 'HEADS', 'HEADS', 'TAILS']  streak? False
Experiment 3: ['TAILS', 'TAILS', 'HEADS', 'HEADS', 'TAILS']  streak? False
Experiment 4: ['TAILS', 'HEADS', 'HEADS', 'HEADS', 'TAILS']  streak? False
Experiment 5: ['TAILS', 'TAILS', 'TAILS', 'HEADS', 'HEADS']  streak? False

Ran 100,000 experiments.
3,089 of them were 5 HEADS in a row.
Measured chance of a streak : 0.0309
Predicted chance (1/2)^5   : 0.0312  (that is 1 in 32)
```

**The intuition:** Before any flips, five heads in a row is rare: about 1 in 32. Students see five sample experiments first, so "experiment" means something concrete before the big count.

**Ask the class:** If a streak is so rare, doesn't that mean tails is coming? (Hold that thought for Chapter 4.)

### Chapter 4: The gambler's question

**File:** `chapter_4_the_gamblers_question.py`

```python
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
```

**Sample run:**

```text
The gambler says: 'After 5 HEADS in a row, TAILS is due!'
Let's test that. Whenever we see a streak, we flip ONE more time and write it down.

Streaks of 5 HEADS found: 31,293
  Next flip was HEADS: 15,703
  Next flip was TAILS: 15,590

Chance of HEADS after the streak: 0.502
The coin has no memory. TAILS was never 'due'.
```

**The intuition:** This is the original `fair_coin_after_streak`, rewritten in words. The flip after the streak gets its own variable, `the_very_next_flip`, so you can watch it happen. Out of tens of thousands of streaks, the next flip splits almost exactly 50/50.

**Key line:** "rare *before* it happens" and "likely *after* it happens" are different questions.

### Chapter 5: Meet the evil coin

**File:** `chapter_5_meet_the_evil_coin.py`

```python
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
```

**Sample run:**

```text
fair coin: ['TAILS', 'TAILS', 'HEADS', 'TAILS', 'TAILS', 'HEADS', 'TAILS', 'TAILS', 'TAILS', 'TAILS']
evil coin: ['HEADS', 'HEADS', 'HEADS', 'HEADS', 'HEADS', 'HEADS', 'HEADS', 'HEADS', 'HEADS', 'HEADS']

The fair coin and the evil coin are the same code with a different number.
Notice: the fair coin CAN make 5 HEADS in a row too. A streak alone does not prove evil.
```

**The intuition:** A small refactor: `flip_fair_coin()` becomes `flip_coin(coin_name)`. The only difference between the coins is how much of the ruler is painted HEADS. For the evil coin, that's all of it.

**Ask the class:** The fair coin can also make 5 heads in a row. So how could you ever tell which coin you're holding?

### Chapter 6: The bag, and the twist

**File:** `chapter_6_the_bag_of_coins.py`

```python
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
```

**Sample run:**

```text
The bag has 99 fair coins and 1 evil coin.
Grab a coin without looking. Flip it 5 times.
Question: if it made a streak, how likely is it that we are holding the evil coin?

BEFORE flipping: we held the evil coin 1.0% of the time.
AFTER seeing 5 HEADS: we held the evil coin 24.8% of the time.

The flips did not change the coin. They changed what we KNOW about the coin.
```

**The intuition:** This is the "aha" chapter. Before flipping, you hold the evil coin about **1%** of the time. Among experiments that made a streak, it's about **25%**. `coin_makes_a_streak` stops at the first tails, just like you would at a real table.

**Key line:** the flips didn't change the coin. They changed what we *know* about the coin.

### Chapter 7: Simulation meets Bayes

**File:** `chapter_7_simulation_meets_bayes.py`

```python
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
```

**Sample run:**

```text
        Holding the evil coin?    Next flip is HEADS?
Streak   simulated    Bayes        simulated    Bayes
------   ---------   ------        ---------   ------
     0        1.0%     1.0%            50.6%    50.5%
     1        2.0%     2.0%            51.0%    51.0%
     2        3.8%     3.9%            51.7%    51.9%
     3        7.6%     7.5%            53.5%    53.7%
     4       13.4%    13.9%            56.7%    57.0%
     5       24.1%    24.4%            61.6%    62.2%
     6       39.3%    39.3%            69.9%    69.6%
     7       56.7%    56.4%            78.9%    78.2%
     8       71.9%    72.1%            85.2%    86.1%
     9       83.8%    83.8%            91.8%    91.9%
    10       90.2%    91.2%            96.1%    95.6%

The longer the streak, the MORE likely HEADS gets. The gambler had it backwards.
```

**The intuition:** The Bayes function reads like a sentence: out of all the ways a streak can happen, what share came from the evil coin? The simulated column and the Bayes column agree within about a percent on every row.

**Key line:** the longer the streak, the *more* likely heads gets. The gambler had it backwards.

---

## Part 6: Debugging notes (real mistakes, kept as lessons)

The first time these chapters were pasted into PowerShell, two things went wrong. Both are worth showing students.

### Bug 1: the line that got eaten

Chapters 5, 6, and 7 crashed with:

```text
    if random.random() < CHANCE_OF_HEADSreturn "HEADS"
                                               ^^^^^^^
SyntaxError: invalid syntax
```

The code had been tested and worked, but when it was displayed in chat, part of one line disappeared: the dictionary lookup, the colon, and the line break. Copy/paste carried the damage straight into the file.

**The fix** was to split that one crowded line into two simple steps with a descriptive name, so a missing piece is easy to spot:

```python
chance_this_coin_lands_heads = CHANCE_OF_HEADS[coin_name]
if random.random() < chance_this_coin_lands_heads:
    return "HEADS"
```

**Lesson:** "it worked on my machine" doesn't mean it survived the trip. Run the code after every copy, and keep the real file in Git, not in a chat window.

### Bug 2: the folder inside the folder

The paste commands start with:

```powershell
New-Item -ItemType Directory -Force -Path .\gamblers_fallacy_story | Out-Null
```

The `.\` means "starting from **where I am now**." They were run from *inside* `gamblers_fallacy_story`, so PowerShell created another one inside it:

```text
code\gamblers_fallacy_story\gamblers_fallacy_story\chapter_5_meet_the_evil_coin.py
```

**Lesson:** a relative path depends on where you're standing. Run `pwd` before you paste a command that creates folders.

---

## Ideas for next time

- **Refactor lesson:** every chapter copies its helper functions so it can run alone. Move `flip_coin`, `grab_coin_from_bag_without_looking`, and `coin_makes_a_streak` into a shared `coins.py`, then `import` them.
- **Change one number:** make the bag 90 fair and 10 evil, or make the evil coin 90% heads instead of 100%. Predict the Chapter 7 table *before* you run it.
- **Seed it:** add `random.seed(42)` to the top of a chapter so the whole class gets identical output.
- **Bridge to Blackjack:** draw cards *without* replacement and show that the deck, unlike the coin, *does* have memory.

---

## Sources

- Thomas Bayes biography: <https://en.wikipedia.org/wiki/Thomas_Bayes>
- Bayes's 1763 essay, as communicated by Richard Price: <https://bayes.wustl.edu/Manual/an.essay.pdf>
- About the essay and what it actually contains: <https://en.wikipedia.org/wiki/An_Essay_towards_solving_a_Problem_in_the_Doctrine_of_Chances>
- Bayes' theorem and its history: <https://en.wikipedia.org/wiki/Bayes%27_theorem>
- J. D. Holland, "The Reverend Thomas Bayes, F.R.S. (1702–61)": <https://www.jstor.org/stable/pdf/2982413.pdf>
- A. I. Dale, "Bayes or Laplace?": <https://www.jstor.org/stable/pdf/41133662.pdf>
- Edward Simpson, "Bayes at Bletchley Park": <https://math.oxford.emory.edu/site/math117/bayesTheorem/enigma_and_bayes_theorem.pdf>
- Summary of Sharon McGrayne, *The Theory That Would Not Die*: <https://www.lesswrong.com/posts/RTt59BtFLqQbsSiqd/a-history-of-bayes-theorem>
- Kenneth Rosen, *Discrete Mathematics and Its Applications* (7th ed.), Section 7.3, "Bayes' Theorem"
