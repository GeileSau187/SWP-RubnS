import unittest
import random
from poker import (
    build_deck,
    deal_cards,
    format_hand,
    evaluate_hand,
    SUITS,
    RANKS,
    CARDS_PER_SUIT,
    TOTAL_CARDS,
    CARDS_PER_HAND
)

class TestPokerFunctions(unittest.TestCase):

    def test_build_deck_has_52_unique_cards(self):
        deck = build_deck()
        self.assertEqual(len(deck), TOTAL_CARDS)
        self.assertEqual(len(set(deck)), TOTAL_CARDS)
        for suit, rank in deck:
            self.assertIn(suit, SUITS)
            self.assertIn(rank, RANKS)

    def test_deal_cards_draws_correct_number_without_duplicates(self):
        random.seed(0)
        deck = build_deck()
        hand = deal_cards(deck, CARDS_PER_HAND)
        self.assertEqual(len(hand), CARDS_PER_HAND)
        self.assertEqual(len(set(hand)), CARDS_PER_HAND)

    def test_format_hand_output(self):
        hand = [("♠", "A"), ("♥", "10"), ("♦", "3")]
        formatted = format_hand(hand)
        self.assertEqual(formatted, "A♠, 10♥, 3♦")

    def test_evaluate_hand_categories(self):
        hand_four = [("♠", "A"), ("♥", "A"), ("♦", "A"), ("♣", "A"), ("♠", "K")]
        self.assertEqual(evaluate_hand(hand_four), "Vierling")

        hand_pair = [("♠", "K"), ("♥", "K"), ("♦", "3"), ("♣", "7"), ("♠", "9")]
        self.assertEqual(evaluate_hand(hand_pair), "Zwilling")

        hand_two_pairs = [("♠", "K"), ("♥", "K"), ("♦", "7"), ("♣", "7"), ("♠", "9")]
        self.assertEqual(evaluate_hand(hand_two_pairs), "Zwei Paare")

        hand_flush = [("♠", "2"), ("♠", "5"), ("♠", "9"), ("♠", "J"), ("♠", "K")]
        self.assertEqual(evaluate_hand(hand_flush), "Flush")


if __name__ == "__main__":
    unittest.main()
