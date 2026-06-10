"""Tarot cards and effects"""

from enum import Enum
from typing import List
from core.card import Card


class TarotType(Enum):
    """Tarot card types"""
    MAGICIAN = "magician"
    HIGH_PRIESTESS = "high_priestess"
    EMPRESS = "empress"
    EMPEROR = "emperor"
    HIEROPHANT = "hierophant"
    LOVERS = "lovers"
    CHARIOT = "chariot"
    STRENGTH = "strength"
    HERMIT = "hermit"
    WHEEL = "wheel"
    JUSTICE = "justice"
    HANGED_MAN = "hanged_man"
    DEATH = "death"
    TEMPERANCE = "temperance"
    DEVIL = "devil"
    TOWER = "tower"
    STAR = "star"
    MOON = "moon"
    SUN = "sun"
    JUDGEMENT = "judgement"
    WORLD = "world"


class Tarot:
    """Base class for tarot cards"""

    def __init__(self, name: str, description: str, tarot_type: TarotType = None):
        """
        Initialize a tarot card.
        
        Args:
            name: Name of the tarot
            description: Description of its effect
            tarot_type: Type of tarot card
        """
        self.name = name
        self.description = description
        self.tarot_type = tarot_type
        self.uses_left = 1

    def use(self, cards: List[Card] = None) -> bool:
        """Use the tarot card"""
        if self.uses_left > 0:
            self.uses_left -= 1
            return True
        return False

    def __repr__(self) -> str:
        return f"Tarot({self.name})"


# Specific Tarot implementations
class MagicianTarot(Tarot):
    """Magician: Upgrade a random card in hand"""
    def __init__(self):
        super().__init__("The Magician", "Upgrades a random card in hand", TarotType.MAGICIAN)


class HighPriestessTarot(Tarot):
    """High Priestess: Creates a Spectral card"""
    def __init__(self):
        super().__init__("The High Priestess", "Creates a Spectral card", TarotType.HIGH_PRIESTESS)


class EmpressTarot(Tarot):
    """Empress: Add a random card to hand"""
    def __init__(self):
        super().__init__("The Empress", "Adds a random card to hand", TarotType.EMPRESS)


class DeathTarot(Tarot):
    """Death: Destroy a random card in hand"""
    def __init__(self):
        super().__init__("Death", "Destroys a random card in hand", TarotType.DEATH)
