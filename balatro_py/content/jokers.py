"""Joker cards and effects"""

from typing import List, Tuple
from enum import Enum


class JokerRarity(Enum):
    """Joker rarity levels"""
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    LEGENDARY = "legendary"


class Joker:
    """Base class for joker cards"""

    def __init__(self, name: str, description: str, cost: int = 5, rarity: JokerRarity = JokerRarity.COMMON):
        """
        Initialize a joker.
        
        Args:
            name: Name of the joker
            description: Description of its effect
            cost: Cost in shop
            rarity: Rarity level
        """
        self.name = name
        self.description = description
        self.cost = cost
        self.rarity = rarity
        self.active = True
        self.activation_count = 0
        self.chip_bonus = 0
        self.mult_bonus = 0

    def calculate_effect(self, scored_cards: List) -> Tuple[int, float]:
        """
        Calculate the chip and mult bonus from this joker.
        
        Args:
            scored_cards: Cards that were scored in this hand
            
        Returns:
            Tuple of (chip_bonus, mult_bonus)
        """
        return (self.chip_bonus, 1.0 + self.mult_bonus)

    def on_play(self, scored_cards: List):
        """Called when hand is played"""
        self.activation_count += 1

    def on_discard(self):
        """Called when cards are discarded"""
        pass

    def on_round_start(self):
        """Called at start of round"""
        pass

    def on_round_end(self):
        """Called at end of round"""
        pass

    def deactivate(self):
        """Deactivate the joker"""
        self.active = False

    def __repr__(self) -> str:
        return f"Joker({self.name})"


# Specific Joker implementations
class BlueprintJoker(Joker):
    """Blueprint: Copies the effect of the rightmost joker"""
    def __init__(self):
        super().__init__(
            "Blueprint",
            "Copies the effect of the rightmost Joker",
            cost=8,
            rarity=JokerRarity.UNCOMMON
        )


class BuffetJoker(Joker):
    """Buffet: Every poker hand is worth x1.5 more"""
    def __init__(self):
        super().__init__(
            "Buffet",
            "Every poker hand is worth x1.5 more",
            cost=8,
            rarity=JokerRarity.UNCOMMON
        )
        self.mult_bonus = 0.5

    def calculate_effect(self, scored_cards: List) -> Tuple[int, float]:
        return (0, 1.5)


class CarpenterJoker(Joker):
    """Carpenter: Every poker hand is worth +15 chips"""
    def __init__(self):
        super().__init__(
            "Carpenter",
            "Every poker hand is worth +15 chips",
            cost=5,
            rarity=JokerRarity.COMMON
        )

    def calculate_effect(self, scored_cards: List) -> Tuple[int, float]:
        return (15, 1.0)


class CheekyJoker(Joker):
    """Cheeky: Every poker hand is worth +3 chips for every card in hand"""
    def __init__(self):
        super().__init__(
            "Cheeky",
            "Every poker hand is worth +3 chips for every card in hand",
            cost=6,
            rarity=JokerRarity.COMMON
        )

    def calculate_effect(self, scored_cards: List) -> Tuple[int, float]:
        hand_size = 5  # Default hand size, should be passed in
        return (3 * hand_size, 1.0)


class GreedyJoker(Joker):
    """Greedy: Earn $4 every time a card with a Gold seal is scored"""
    def __init__(self):
        super().__init__(
            "Greedy",
            "Earn $4 every time a card with a Gold seal is scored",
            cost=6,
            rarity=JokerRarity.UNCOMMON
        )

    def calculate_effect(self, scored_cards: List) -> Tuple[int, float]:
        gold_seal_count = sum(1 for card in scored_cards if hasattr(card, 'seal') and card.seal == "gold")
        return (0, 1.0)  # Money gain handled elsewhere


class InsaneJoker(Joker):
    """Insane: Every poker hand is worth x3, but each joker is worth -1x mult"""
    def __init__(self):
        super().__init__(
            "Insane",
            "Every poker hand is worth x3, but each joker is worth -1x mult",
            cost=10,
            rarity=JokerRarity.RARE
        )

    def calculate_effect(self, scored_cards: List) -> Tuple[int, float]:
        return (0, 3.0)


class SmileyJoker(Joker):
    """Smiley: Every poker hand is worth x1.05 for every Happy card in hand"""
    def __init__(self):
        super().__init__(
            "Smiley",
            "Every poker hand is worth x1.05 for every Happy card in hand",
            cost=5,
            rarity=JokerRarity.COMMON
        )

    def calculate_effect(self, scored_cards: List) -> Tuple[int, float]:
        happy_count = 0  # Would need to track happy cards
        return (0, 1.0 + (0.05 * happy_count))
