"""Classroom counting lab and face-up blackjack. No money or dependencies."""
from itertools import combinations, permutations, product, combinations_with_replacement
from math import comb, perm
import random


def hand_total(hand):
    total = sum(11 if rank == 'A' else 10 if rank in ('J', 'Q', 'K') else int(rank)
                for rank, suit in hand)
    aces = sum(rank == 'A' for rank, suit in hand)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total


def make_deck():
    return [(rank, suit) for suit in ('H', 'D', 'C', 'S')
            for rank in ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')]


def show(hand):
    return ' '.join(rank + suit for rank, suit in hand)


def counting_lab():
    cards = ['A', 'B', 'C', 'D']
    print('\nFour distinct cards: A, B, C, D. Choose two.')
    cases = [
        ('Order matters, no replacement', permutations(cards, 2), perm(4, 2)),
        ('Order ignored, no replacement', combinations(cards, 2), comb(4, 2)),
        ('Order matters, with replacement', product(cards, repeat=2), 4 ** 2),
        ('Order ignored, with replacement', combinations_with_replacement(cards, 2), comb(5, 2)),
    ]
    for title, outcomes, expected in cases:
        print('\n' + title)
        guess = input('Predict the number of outcomes (Enter to skip): ').strip()
        outcomes = list(outcomes)
        if guess:
            print('Correct!' if guess == str(expected) else f'Not yet: the answer is {expected}.')
        for number, outcome in enumerate(outcomes, start=1):
            print(f'{number:2}: {" ".join(outcome)}')
        assert len(outcomes) == expected
    print('\nAB and BA are different ordered draws, but the same unordered hand.')
    print('Numbering outcomes is just labeling them; it does not change the count.')
    print('With replacement, unordered hands are NOT equally likely: AB has two draw orders; AA has one.')
    print('Try changing the card list and selection size as your next coding exercise.')


def blackjack():
    replacement = input('Experimental replacement mode? [y/N]: ').strip().lower() == 'y'
    deck = make_deck()
    random.shuffle(deck)

    def draw():
        if replacement:
            return random.choice(deck)
        if not deck:
            raise RuntimeError('Deck exhausted. Start a new round.')
        return deck.pop()

    player, dealer = [], []
    for _ in range(2):
        player.append(draw())
        dealer.append(draw())
    print('\nClassroom rules: all cards visible; dealer stands on every 17.')
    print('No betting, splits, doubles, insurance, or payouts. Fresh deck each round.')
    print('Replacement mode is an experiment, not standard blackjack.')
    print('Dealer:', show(dealer), 'Total:', hand_total(dealer))
    player_natural = hand_total(player) == 21
    dealer_natural = hand_total(dealer) == 21
    if player_natural or dealer_natural:
        print('You:', show(player), 'Total:', hand_total(player))
        print('Tie: both have blackjack.' if player_natural and dealer_natural else
              'You win with blackjack!' if player_natural else 'Dealer wins with blackjack.')
        return
    while hand_total(player) < 21:
        print('\nYou:', show(player), 'Total:', hand_total(player))
        bust_cards = sum(hand_total(player + [card]) > 21 for card in deck)
        print(f'Next-draw bust chance: {bust_cards}/{len(deck)} = {bust_cards / len(deck):.1%}')
        print('This is a bust chance, not a chance of winning the round.')
        action = input('[h]it or [s]tand: ').strip().lower()
        if action == 's':
            break
        if action != 'h':
            print('Please enter h or s.')
            continue
        player.append(draw())
    if hand_total(player) > 21:
        print('You:', show(player), 'Total:', hand_total(player), 'You bust. Dealer wins.')
        return
    while hand_total(dealer) < 17:
        dealer.append(draw())
    p, d = hand_total(player), hand_total(dealer)
    print('You:', show(player), 'Total:', p)
    print('Dealer:', show(dealer), 'Total:', d)
    print('You win!' if d > 21 or p > d else 'Tie!' if p == d else 'Dealer wins.')


def self_test():
    assert len(make_deck()) == len(set(make_deck())) == 52
    assert hand_total([('A', 'H'), ('K', 'S')]) == 21
    assert hand_total([('A', 'H'), ('A', 'S'), ('9', 'D')]) == 21
    assert hand_total([('A', 'H'), ('6', 'S'), ('10', 'D')]) == 17
    assert hand_total([('K', 'H'), ('Q', 'S'), ('2', 'D')]) == 22
    assert [len(list(f('ABCD', 2))) for f in (permutations, combinations, combinations_with_replacement)] == [12, 6, 10]
    assert len(list(product('ABCD', repeat=2))) == 16
    print('Self-tests passed: deck, aces, busts, and all four counting modes.')


def main():
    self_test()
    while True:
        choice = input('\n[1] Counting lab  [2] Blackjack  [q] Quit: ').strip().lower()
        if choice == 'q':
            return
        if choice == '1':
            counting_lab()
        elif choice == '2':
            blackjack()
        else:
            print('Choose 1, 2, or q.')


if __name__ == '__main__':
    main()
