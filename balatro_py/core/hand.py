"""Hand class for managing the player's current hand"""

from typing import List, Tuple, Optional
from .card import Card
from .poker_hands import PokerHandEvaluator, PokerHandType
from .scoring import Scoring


class Hand:
    """Represents the player's current hand of cards"""

    def __init__(self):
        """Initialize an empty hand"""
        self.cards: List[Card] = []
        self.selected_indices: List[int] = []
        self.scoring = Scoring()
        self.last_hand_type: Optional[PokerHandType] = None
        self.last_score = 0

    def add_card(self, card: Card):
        """Add a card to the hand"""
        self.cards.append(card)

    def remove_card(self, card: Card):
        """Remove a card from the hand"""
        if card in self.cards:
            self.cards.remove(card)

    def remove_by_index(self, index: int):
        """Remove a card by index"""
        if 0 <= index < len(self.cards):
            self.cards.pop(index)

    def select_card(self, index: int):
        """Toggle selection of a card"""
        if 0 <= index < len(self.cards):
            if index in self.selected_indices:
                self.selected_indices.remove(index)
            else:
                self.selected_indices.append(index)

    def clear_selection(self):
        """Clear all selected cards"""
        self.selected_indices.clear()

    def get_selected_cards(self) -> List[Card]:
        """Get currently selected cards"""
        return [self.cards[i] for i in self.selected_indices if 0 <= i < len(self.cards)]

    def get_all_cards(self) -> List[Card]:
        """Get all cards in hand"""
        return self.cards.copy()

    def evaluate(self, jokers: list = None) -> Tuple[PokerHandType, List[Card], int, float, int]:
        """
        Evaluate the selected poker hand using Balatro rules from Lua source.
        
        Args:
            jokers: Optional list of active joker cards
            
        Returns:
            Tuple of (hand_type, scoring_cards, base_chips, mult, final_score)
        """
        selected = self.get_selected_cards()
        if not selected:
            return (PokerHandType.HIGH_CARD, [], 0, 0.0, 0)

        # Determine hand type and scoring cards
        hand_type, scoring_cards = PokerHandEvaluator.evaluate_hand(selected)
        
        # Get base chips and mult from hand type (from Lua source)
        base_chips = hand_type.get_base_chips()
        base_mult = hand_type.get_base_mult()
        
        # Calculate score using the Scoring system
        chips, mult, score = self.scoring.calculate_hand_score(
            base_chips, 
            base_mult, 
            scoring_cards,
            jokers
        )
        
        # Store for reference
        self.last_hand_type = hand_type
        self.last_score = score
        
        return (hand_type, scoring_cards, chips, mult, score)

    def get_hand_name(self) -> str:
        """Get the name of the currently held hand type"""
        if self.last_hand_type:
            # Convert enum name to readable format
            name = self.last_hand_type.name.replace("_", " ").title()
            return name
        return "No Hand"

    def clear(self):
        """Clear all cards from the hand"""
        self.cards.clear()
        self.selected_indices.clear()
        self.scoring.reset()
        self.last_hand_type = None
        self.last_score = 0

    def __len__(self) -> int:
        return len(self.cards)

    def __repr__(self) -> str:
        return f"Hand({', '.join(str(card) for card in self.cards)})"
