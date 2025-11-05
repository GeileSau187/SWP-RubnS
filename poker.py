import random

#1) Define constants
#2) Create deck
#3) Deal Random Cards
#4) Format the Hand
#5) Search for combinations
#6) Play 100000 times and count the chance to get each combination in %
#7) Compare with Internet

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

CARDS_PER_HAND = 5

def build_deck():
    deck = [(suit, rank) for suit in SUITS for rank in RANKS]
    return deck

def deal_cards(deck, number_of_cards):
    return random.sample(deck, number_of_cards)

def format_hand(hand):
    return ", ".join(f"{rank}{suit}" for suit, rank in hand)

def main():
    deck = build_deck()

    hand = deal_cards(deck, CARDS_PER_HAND)

    print("Your poker hand:")
    print(format_hand(hand))

# Run the program
if __name__ == "__main__":
    main()
