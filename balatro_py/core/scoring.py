"""Scoring system for hands and multipliers - Following Balatro (Lua source) logic"""

from typing import List, Dict, Tuple
from .card import Card


class Scoring:
    """Handles all scoring calculations following exact Balatro rules"""

    # Rank chip values from Lua source
    RANK_CHIPS = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
        "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11
    }

    def __init__(self):
        """Initialize scoring system"""
        self.base_chips = 0
        self.chip_mult = 1.0
        self.hand_mult = 1.0
        self.scored_cards: List[Card] = []

    def calculate_hand_score(
        self,
        hand_type_chips: int,
        hand_type_mult: int,
        scored_cards: List[Card],
        jokers: list = None,
    ) -> Tuple[int, float, int]:
        """
        Calculate the score for a given hand using Balatro rules.
        
        Following Lua source: base_chips * hand_mult * total_mult = final_score
        
        Args:
            hand_type_chips: Base chips from hand type (from PokerHandType)
            hand_type_mult: Base multiplier from hand type
            scored_cards: Cards that scored
            jokers: Active joker cards with effects
            
        Returns:
            Tuple of (total_chips, total_mult, final_score)
        """
        total_chips = hand_type_chips
        total_mult = float(hand_type_mult)

        # Step 1: Add chips from card ranks
        # In Balatro, each card in the hand adds its rank value in chips
        for card in scored_cards:
            rank_chips = self.RANK_CHIPS.get(card.rank, 0)
            total_chips += rank_chips

        # Step 2: Apply card enhancements (multiplicative cards, glass, steel, etc)
        # Enhancements can add mult or modify chips
        for card in scored_cards:
            if card.enhancement:
                enhancement_mult = self._get_enhancement_mult(card.enhancement)
                if enhancement_mult > 0:
                    total_mult *= enhancement_mult
                else:
                    total_chips = self._apply_enhancement_chips(card.enhancement, total_chips)

        # Step 3: Apply seals (Gold seal, Red seal, etc)
        # Seals modify chips or mult
        for card in scored_cards:
            if card.seal:
                total_chips, mult_mod = self._apply_seal_effect(card.seal, total_chips)
                total_mult *= mult_mod

        # Step 4: Apply edition effects (Foil, Holographic, Polychrome)
        for card in scored_cards:
            if card.edition:
                chip_mult, mult_mult = self._apply_edition_effect(card.edition)
                total_chips = int(total_chips * chip_mult)
                total_mult *= mult_mult

        # Step 5: Apply joker effects (this is where most complexity happens)
        if jokers:
            for joker in jokers:
                if joker.active:
                    joker_chips, joker_mult = joker.calculate_effect(scored_cards)
                    total_chips += joker_chips
                    total_mult *= joker_mult
                    joker.on_play(scored_cards)

        # Step 6: Calculate final score
        final_score = int(total_chips * total_mult)

        # Store for later reference
        self.base_chips = total_chips
        self.chip_mult = total_mult
        self.scored_cards = scored_cards

        return (total_chips, total_mult, final_score)

    @staticmethod
    def _get_enhancement_mult(enhancement: str) -> float:
        """
        Get multiplier for a card enhancement.
        Returns mult modifier (>1 means multiply, =0 means handle separately)
        """
        enhancement_mults = {
            "bonus": 0.0,   # Bonus card: +30 chips (handled separately)
            "mult": 2.0,    # Mult card: x2 multiplier
            "glass": 2.0,   # Glass card: x2 mult (but can break)
            "steel": 1.5,   # Steel card: x1.5 chips multiplier
            "stone": 0.0,   # Stone card: +50 chips
            "gold": 0.0,    # Gold card: +$3
            "lucky": 0.0,   # Lucky card: random
        }
        return enhancement_mults.get(enhancement, 0.0)

    @staticmethod
    def _apply_enhancement_chips(enhancement: str, chips: int) -> int:
        """Apply chip bonuses from enhancements"""
        enhancement_chips = {
            "bonus": 30,    # Bonus card: +30 chips
            "stone": 50,    # Stone card: +50 chips
            "steel": 0,     # Handled with mult
            "glass": 0,     # Handled with mult
            "gold": 0,      # Money, not chips
            "lucky": 0,     # Random
        }
        return chips + enhancement_chips.get(enhancement, 0)

    @staticmethod
    def _apply_seal_effect(seal: str, chips: int) -> Tuple[int, float]:
        """
        Apply seal effect to chips and mult.
        Returns (modified_chips, mult_modifier)
        """
        seal_effects = {
            "gold": (chips + 10, 1.0),      # Gold seal: +10 chips
            "red": (chips * 2, 1.0),        # Red seal: x2 chips
            "blue": (chips, 1.0),           # Blue seal: create card (handled elsewhere)
            "purple": (chips, 1.0),         # Purple seal: return to hand (handled elsewhere)
        }
        if seal in seal_effects:
            return seal_effects[seal]
        return (chips, 1.0)

    @staticmethod
    def _apply_edition_effect(edition: str) -> Tuple[float, float]:
        """
        Apply edition effect to chips and mult multipliers.
        Returns (chip_mult, mult_mult)
        """
        edition_effects = {
            "base": (1.0, 1.0),              # Base: no effect
            "foil": (1.5, 1.0),              # Foil: x1.5 chips
            "holographic": (1.0, 2.0),       # Holographic: x2 mult
            "polychrome": (1.5, 1.5),        # Polychrome: x1.5 chips AND x1.5 mult
            "negative": (1.0, 1.0),          # Negative: +1 joker slot (handled elsewhere)
        }
        return edition_effects.get(edition, (1.0, 1.0))

    def reset(self):
        """Reset scoring values"""
        self.base_chips = 0
        self.chip_mult = 1.0
        self.hand_mult = 1.0
        self.scored_cards.clear()

    def get_total_score(self) -> int:
        """Get total score from current scoring"""
        return int(self.base_chips * self.chip_mult * self.hand_mult)
