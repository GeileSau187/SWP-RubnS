import random

#1) Define constants
#2) Create deck
#3) Deal Random Cards
#4) Format the Hand
#5) Search for combinations
#6) Play 100000 times and count the chance to get each combination in %
#7) Compare with Internet

import random

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
CARDS_PER_SUIT = 13
TOTAL_CARDS = 52
CARDS_PER_HAND = 5

def build_deck():
    deck = []
    for i in range(TOTAL_CARDS):
        suit_index = i // CARDS_PER_SUIT
        rank_index = i % CARDS_PER_SUIT

        suit = SUITS[suit_index]
        rank = RANKS[rank_index]

        deck.append((suit, rank))
    return deck

def deal_cards(deck, number_of_cards):
    return random.sample(deck, number_of_cards)

def format_hand(hand):
    return ", ".join(f"{rank}{suit}" for suit, rank in hand)

from collections import Counter

def evaluate_hand(hand):

    suits = [s for s, r in hand]
    ranks = [r for s, r in hand]

    counts = Counter(ranks)
    max_count = max(counts.values())

    flush = len(set(suits)) == 1

    if max_count == 4:
        return "Vierling"
    elif max_count == 3:
        return "Drilling"
    elif list(counts.values()).count(2) == 2:
        return "Zwei Paare"
    elif max_count == 2:
        return "Zwilling"
    elif flush:
        return "Flush"
    else:
        return "Nichts"


def main():
    deck = build_deck()
    hand = deal_cards(deck, CARDS_PER_HAND)
    print("Your poker hand:")
    print(format_hand(hand))
    print("Result:", evaluate_hand(hand))

if __name__ == "__main__":
    main()
