Counting Cards: Order, Replacement, and Blackjack

*DSCT (Discrete Structures and Critical Thinking) · Week 09 · Conversation artifact · October 13, 2026*

This document records a classroom build session: we started with the four core counting models, turned them into a playable Python card lab, ran it, asked what “replacement” means in blackjack, and then grew it into a standalone interactive website with a pretend bankroll and a Hi-Lo card-counting coach.

1\. The Big Idea: Two Independent Questions

Every counting problem in this lab is answered by asking two separate questions:

1.  Does order matter? (Is AB different from BA?)

2.  Can an item repeat? (Is the chosen item put back before the next draw?)

These are independent decisions. Replacement controls whether an item can repeat. Order controls whether rearranging the selected items makes a different outcome.

The four models (choose r = 2 from cards A, B, C, D)

|                              |                 |                   |           |                                         |
|------------------------------|-----------------|-------------------|-----------|-----------------------------------------|
| **Model**                    | **Order?**      | **Formula**       | **Count** | **Python itertools**                    |
| Permutation                  | Yes, no repeats | n! / (n − r)!     | 12        | permutations(cards, 2)                  |
| Combination                  | No, no repeats  | n! / (r!(n − r)!) | 6         | combinations(cards, 2)                  |
| Ordered with replacement     | Yes, repeats    | n^r               | 16        | product(cards, repeat=2)                |
| Combination with replacement | No, repeats     | C(n + r − 1, r)   | 10        | combinations_with_replacement(cards, 2) |

Key insights we wrote into the lab

- Why r! and not just dividing by r: each unordered hand of r distinct cards has r! ordered versions. For three cards: ABC, ACB, BAC, BCA, CAB, CBA, so we divide by 3! = 6.

- Numbering outcomes (#1, \#2, \#3…) is just labeling. It does not make order matter inside a hand.

- Probability trap: with replacement, unordered hands are NOT equally likely. AB can arrive as AB or BA; AA arrives only one way. Counting unique hands is not the same as counting equally likely outcomes.

- Combinations with replacement connect back to stars and bars from the Chapter 6 material.

2\. Version 1: counting_card_lab.py

A dependency-free Python program with a menu: \[1\] Counting lab, \[2\] Blackjack, \[q\] Quit. It runs self-tests at startup (deck size, ace handling, busts, all four counting modes).

Run it

cd C:\Users\<you>\git\discrete_structures_and_critical_thinking\week-09

python .\counting_card_lab.py

Counting lab: predict, then reveal

Students predict the number of outcomes for each model, then the program enumerates every outcome with numbers and asserts the count matches the formula.

from itertools import permutations

cards = \["A", "B", "C", "D"\]

for number, draw in enumerate(permutations(cards, 2), start=1):

print(number, draw)

\# AB and BA are different. No repeated card.

Ace handling: the hand total function

def hand_total(hand):

total = sum(11 if rank == "A" else 10 if rank in ("J", "Q", "K") else int(rank)

for rank, suit in hand)

aces = sum(rank == "A" for rank, suit in hand)

while total \> 21 and aces:

total -= 10

aces -= 1

return total

Aces start at 11 and drop to 1 one at a time only when the hand would bust. Test: A + A + 9 = 21.

Exact next-draw bust chance

bust_cards = sum(hand_total(player + \[card\]) \> 21 for card in deck)

print(f"Next-draw bust chance: {bust_cards}/{len(deck)}")

The program tries every remaining card, appends it to the hand, and counts how many cause a bust. This is a bust chance, not a chance of winning the round.

3\. What “Experimental replacement mode? \[y/N\]” Means

The prompt asks: after drawing a card, should that same card be available to draw again? The capital N means pressing Enter selects No.

|                        |                                    |                                                         |
|------------------------|------------------------------------|---------------------------------------------------------|
|                        | **Without replacement (Enter)**    | **With replacement (y)**                                |
| What happens           | The drawn card leaves the deck     | The card stays available, as if put back and reshuffled |
| Same exact card again? | No (other sevens can still appear) | Yes, the same 7♥ can repeat                             |
| Pool size              | Shrinks with every draw            | Stays at 52                                             |
| Code                   | deck.pop()                         | random.choice(deck)                                     |

Which is traditional?

Without replacement is the traditional blackjack model. Dealt cards stay out of the available deck until they are collected and eventually reshuffled. Casinos may use a multi-deck shoe, so another 7♥ can appear from a different deck, but that is not replacement of the card already dealt. Our y option is a math experiment.

4\. Our Test Run (Evidence)

|           |            |                  |                       |                          |
|-----------|------------|------------------|-----------------------|--------------------------|
| **Round** | **Dealer** | **Player start** | **Bust chance shown** | **Result after hitting** |
| 1         | 8♣ J♥ = 18 | 7♣ Q♣ = 17       | 32/48 = 66.7%         | 6♦ → 23, bust            |
| 2         | 2♦ K♦ = 12 | 8♣ 6♠ = 14       | 22/48 = 45.8%         | 10♠ → 24, bust           |
| 3         | A♥ 7♠ = 18 | 5♣ 10♥ = 15      | 26/48 = 54.2%         | K♣ → 25, bust            |

Discussion prompt: in round 1, two-thirds of the deck busts a 17. In round 2 the dealer showed only 12. What would standing have required the dealer to do?

What the class noticed was missing

- No bank account: nothing at stake, so no sense of consequences across rounds.

- No card counting: each round used a fresh deck, so history was erased and counting was meaningless.

- Terminal only: wanted a more fun, interactive website.

5\. Version 2: blackjack_counting_lab.html

A single standalone HTML file (no installs, no network) that opens in any browser.

Start-Process .\blackjack_counting_lab.html

Features

- \$500 pretend bankroll with available balance, stake in play, session net, and rounds settled.

- Persistent shoe of 1, 2, or 6 decks so cards stay removed between rounds and history matters.

- Hi-Lo counting coach with running count, true count, and a hide-answers practice mode with a count checker.

- Card receipt: every exposed card with its tag and the running count.

- Bankroll ledger for the whole session and a JSON export for classroom evidence.

- Exact next-draw bust lab and percentage of tens, faces, and aces remaining.

- Counting playground with generated outcome lists and matching Python code.

Table rules (classroom variant)

All cards face up. Dealer stands on all 17s. Blackjack profit 3:2, ordinary win 1:1, push returns stake. No splits, doubles, insurance, or surrender. Classroom reshuffle when 25% or 24 cards remain, whichever is larger (our design choice). Pretend money only; reloading resets the session.

Hi-Lo card values

|                |         |              |
|----------------|---------|--------------|
| **Cards**      | **Tag** | **Action**   |
| 2, 3, 4, 5, 6  | +1      | Add one      |
| 7, 8, 9        | 0       | No change    |
| 10, J, Q, K, A | −1      | Subtract one |

The tags sum to zero over a full deck (balanced). True count = running count ÷ decks remaining. A positive count means more low cards than high cards have left the shoe. It summarizes composition; it does not predict the next card or guarantee a win. With replacement, true count is disabled because seen cards never leave the pool.

Bankroll accounting as code

balance -= stake \# reserve once at deal

\# Settlement returns: loss 0; push stake; win 2\*stake

\# Two-card blackjack returns 2.5\*stake (includes original stake)

balance += returned_amount

running_count += hi_lo(card)

true_count = running_count / (len(shoe) / 52)

6\. Verification Performed

- Python self-tests passed: deck, aces, busts, and all four counting modes.

- All 48 interactive counting configurations (n = 3–6, r = 1–3, both switches) matched their formulas.

- Bankroll engine tests passed: win, loss, push, and blackjack accounting; balanced Hi-Lo; textbook count example.

- Website script: 900 simulated rounds across 1/2/6 decks and both replacement modes checked accounting, count, card conservation, and all 8 playground modes.

- Limit: the website logic was tested with a mocked page; no visual browser test was performed.

7\. Student Activities

1.  Predict all four counts for r = 2, then for r = 3, before revealing.

2.  Explain in one sentence why combinations divide by r! instead of r.

3.  Play five rounds with a persistent shoe and a fixed \$10 stake. Check your running count after every hand.

4.  Turn on replacement. Explain why the running sum no longer describes the cards remaining.

5.  Add a Python test: hand_total of A, A, 9 must equal 21.

6.  Export your JSON receipt and commit it to your repository as evidence.

8\. Files and Sources

- counting_card_lab.py: terminal version (Week 09 folder).

- blackjack_counting_lab.html: interactive website version.

- Chapter6.pptx (Section 6.3 and 6.5): permutations, combinations, and combinations with repetition.

- Python itertools documentation: docs.python.org/3/library/itertools.html

- Hi-Lo reference: countingedge.com/card-counting/hi-lo/

- Shuffling and shoe procedures: ivycasino.com blog; vegas-aces.com dealer guide.

*Safety note: this lab uses pretend money only and is a teaching tool for counting, state, and probability, not a gambling strategy trainer.*
