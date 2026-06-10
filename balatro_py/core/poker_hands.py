"""Poker hand classification and evaluation"""

from enum import Enum
from typing import List, Tuple, Dict
from collections import Counter
from .card import Card


class PokerHandType(Enum):
    """Enumeration of poker hand types following exact Balatro stats from Lua source"""
    # (order, base_chips, base_mult) - from game.lua hands table
    FLUSH_FIVE = (1, 160, 16)           # Flush Five (invisible hand)
    FLUSH_HOUSE = (2, 140, 14)          # Flush House (invisible hand)
    FIVE_OF_A_KIND = (3, 120, 12)       # Five of a Kind (invisible hand)
    STRAIGHT_FLUSH = (4, 100, 8)        # Straight Flush
    FOUR_OF_A_KIND = (5, 60, 7)         # Four of a Kind
    FULL_HOUSE = (6, 40, 4)             # Full House
    FLUSH = (7, 35, 4)                  # Flush
    STRAIGHT = (8, 30, 4)               # Straight
    THREE_OF_A_KIND = (9, 30, 3)        # Three of a Kind
    TWO_PAIR = (10, 20, 2)              # Two Pair
    PAIR = (11, 10, 2)                  # Pair
    HIGH_CARD = (12, 5, 1)              # High Card

    def get_base_chips(self) -> int:
        return self.value[1]

    def get_base_mult(self) -> int:
        return self.value[2]


class PokerHandEvaluator:
    """Evaluate and classify poker hands according to Balatro rules (Lua source)"""

    RANK_ORDER = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    SUIT_ORDER = {"Spades": 0, "Hearts": 1, "Diamonds": 2, "Clubs": 3}

    @staticmethod
    def evaluate_hand(cards: List[Card]) -> Tuple[PokerHandType, List[Card]]:
        """
        Evaluate a poker hand and determine its type.
        Follows Balatro's evaluation order from Lua source.
        
        Args:
            cards: List of cards to evaluate
            
        Returns:
            Tuple of (hand type, scoring cards)
        """
        if not cards:
            return (PokerHandType.HIGH_CARD, cards)

        ranks = [card.rank for card in cards]
        suits = [card.suit for card in cards]
        rank_values = [PokerHandEvaluator.RANK_ORDER[r] for r in ranks]
        
        rank_counts = Counter(ranks)
        suit_counts = Counter(suits)
        
        is_flush = len(suit_counts) == 1
        straight_info = PokerHandEvaluator._check_straight(rank_values)
        is_straight = straight_info[0]
        
        # Check for hand types in Balatro priority order
        
        # Straight Flush
        if is_flush and is_straight:
            return (PokerHandType.STRAIGHT_FLUSH, cards)
        
        # Four of a Kind
        for rank, count in rank_counts.items():
            if count >= 4:
                scoring_cards = [c for c in cards if c.rank == rank]
                kicker = [c for c in cards if c.rank != rank]
                return (PokerHandType.FOUR_OF_A_KIND, scoring_cards + kicker)
        
        # Full House: Three of a kind + pair
        three_kind = [rank for rank, count in rank_counts.items() if count >= 3]
        pair = [rank for rank, count in rank_counts.items() if count >= 2 and rank != (three_kind[0] if three_kind else None)]
        if three_kind and pair:
            three_rank = three_kind[0]
            pair_rank = pair[0]
            scoring_cards = [c for c in cards if c.rank in [three_rank, pair_rank]]
            return (PokerHandType.FULL_HOUSE, scoring_cards)
        
        # Flush
        if is_flush:
            return (PokerHandType.FLUSH, cards)
        
        # Straight
        if is_straight:
            return (PokerHandType.STRAIGHT, cards)
        
        # Three of a Kind
        if three_kind:
            three_rank = three_kind[0]
            scoring_cards = [c for c in cards if c.rank == three_rank]
            kickers = [c for c in cards if c.rank != three_rank]
            return (PokerHandType.THREE_OF_A_KIND, scoring_cards + kickers)
        
        # Two Pair
        pairs = [rank for rank, count in rank_counts.items() if count >= 2]
        if len(pairs) >= 2:
            pair_cards = [c for c in cards if c.rank in pairs[:2]]
            kicker = [c for c in cards if c.rank not in pairs[:2]]
            return (PokerHandType.TWO_PAIR, pair_cards + kicker)
        
        # Pair
        if pairs:
            pair_cards = [c for c in cards if c.rank == pairs[0]]
            kickers = [c for c in cards if c.rank != pairs[0]]
            return (PokerHandType.PAIR, pair_cards + kickers)
        
        # High Card (sort by rank value descending)
        sorted_cards = sorted(cards, key=lambda c: PokerHandEvaluator.RANK_ORDER[c.rank], reverse=True)
        return (PokerHandType.HIGH_CARD, sorted_cards)

    @staticmethod
    def _check_straight(rank_values: List[int]) -> Tuple[bool, List[int]]:
        """Check if cards form a straight"""
        sorted_ranks = sorted(set(rank_values))
        
        # Check for regular straight (5 cards)
        if len(sorted_ranks) == 5:
            if sorted_ranks[-1] - sorted_ranks[0] == 4:
                return (True, sorted_ranks)
        
        # Check for A-2-3-4-5 (wheel) straight with low ace
        if set(sorted_ranks) == {2, 3, 4, 5, 14}:
            return (True, [2, 3, 4, 5, 1])  # Ace is low (1) in this case
        
        return (False, [])
