"""Deck class for managing card collections"""

from typing import List
from .card import Card


class Deck:
    """Represents a deck of cards"""

    def __init__(self):
        """Initialize the deck with standard playing cards"""
        self.cards: List[Card] = []
        self._initialize_standard_deck()

    def _initialize_standard_deck(self):
        """Create a standard 52-card deck"""
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def draw(self, num_cards: int = 1) -> List[Card]:
        """
        Draw cards from the deck.
        
        Args:
            num_cards: Number of cards to draw
            
        Returns:
            List of drawn cards
        """
        drawn = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return drawn

    def shuffle(self):
        """Shuffle the deck"""
        import random
        random.shuffle(self.cards)

    def __len__(self) -> int:
        return len(self.cards)
