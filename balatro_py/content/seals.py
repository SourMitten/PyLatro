"""Card seals"""

from enum import Enum


class SealType(Enum):
    """Seal types"""
    GOLD = "gold"
    RED = "red"
    BLUE = "blue"
    PURPLE = "purple"


class Seal:
    """Base class for card seals"""

    def __init__(self, name: str, seal_type: SealType = None, color: str = ""):
        """
        Initialize a seal.
        
        Args:
            name: Name of the seal
            seal_type: Type of seal
            color: Color of the seal
        """
        self.name = name
        self.seal_type = seal_type
        self.color = color

    def apply(self, card):
        """Apply the seal to a card"""
        card.seal = self

    def __repr__(self) -> str:
        return f"Seal({self.name})"


# Specific Seal implementations
class GoldSeal(Seal):
    """Gold Seal: +10 chips per scoring"""
    def __init__(self):
        super().__init__("Gold Seal", SealType.GOLD, "gold")


class RedSeal(Seal):
    """Red Seal: Earn $2 when scored"""
    def __init__(self):
        super().__init__("Red Seal", SealType.RED, "red")


class BlueSeal(Seal):
    """Blue Seal: Create a free card when scored"""
    def __init__(self):
        super().__init__("Blue Seal", SealType.BLUE, "blue")


class PurpleSeal(Seal):
    """Purple Seal: Return to hand when scored"""
    def __init__(self):
        super().__init__("Purple Seal", SealType.PURPLE, "purple")
