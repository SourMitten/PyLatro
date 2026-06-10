"""Card editions"""

from enum import Enum


class EditionType(Enum):
    """Edition types"""
    FOIL = "foil"
    HOLOGRAPHIC = "holographic"
    POLYCHROME = "polychrome"
    NEGATIVE = "negative"


class Edition:
    """Base class for card editions"""

    def __init__(self, name: str, edition_type: EditionType = None):
        """
        Initialize an edition.
        
        Args:
            name: Name of the edition
            edition_type: Type of edition
        """
        self.name = name
        self.edition_type = edition_type

    def get_chip_mult(self) -> float:
        """Get chip multiplier from edition"""
        return 1.0

    def get_mult_mult(self) -> float:
        """Get mult multiplier from edition"""
        return 1.0

    def apply(self, card):
        """Apply the edition to a card"""
        card.edition = self

    def __repr__(self) -> str:
        return f"Edition({self.name})"


# Specific Edition implementations
class FoilEdition(Edition):
    """Foil: x1.5 Chips"""
    def __init__(self):
        super().__init__("Foil", EditionType.FOIL)

    def get_chip_mult(self) -> float:
        return 1.5


class HolographicEdition(Edition):
    """Holographic: x2 Mult"""
    def __init__(self):
        super().__init__("Holographic", EditionType.HOLOGRAPHIC)

    def get_mult_mult(self) -> float:
        return 2.0


class PolychromeEdition(Edition):
    """Polychrome: x1.5 Chips AND x1.5 Mult"""
    def __init__(self):
        super().__init__("Polychrome", EditionType.POLYCHROME)

    def get_chip_mult(self) -> float:
        return 1.5

    def get_mult_mult(self) -> float:
        return 1.5


class NegativeEdition(Edition):
    """Negative: +1 Joker Slot"""
    def __init__(self):
        super().__init__("Negative", EditionType.NEGATIVE)
