"""Card enhancements"""

from enum import Enum


class EnhancementType(Enum):
    """Enhancement types"""
    BONUS = "bonus"
    MULT = "mult"
    GLASS = "glass"
    STEEL = "steel"
    STONE = "stone"
    GOLD = "gold"
    LUCKY = "lucky"


class Enhancement:
    """Base class for card enhancements"""

    def __init__(self, name: str, enhancement_type: EnhancementType = None):
        """
        Initialize an enhancement.
        
        Args:
            name: Name of the enhancement
            enhancement_type: Type of enhancement
        """
        self.name = name
        self.enhancement_type = enhancement_type

    def get_chip_bonus(self) -> int:
        """Get chip bonus from enhancement"""
        return 0

    def get_mult_bonus(self) -> float:
        """Get multiplier bonus from enhancement"""
        return 0.0

    def apply(self, card):
        """Apply the enhancement to a card"""
        card.enhancement = self

    def __repr__(self) -> str:
        return f"Enhancement({self.name})"


# Specific Enhancement implementations
class BonusCard(Enhancement):
    """Bonus Card: +30 chips"""
    def __init__(self):
        super().__init__("Bonus Card", EnhancementType.BONUS)

    def get_chip_bonus(self) -> int:
        return 30


class MultCard(Enhancement):
    """Mult Card: x2 multiplier"""
    def __init__(self):
        super().__init__("Mult Card", EnhancementType.MULT)

    def get_mult_bonus(self) -> float:
        return 2.0


class GlassCard(Enhancement):
    """Glass Card: +20 chips, can break"""
    def __init__(self):
        super().__init__("Glass Card", EnhancementType.GLASS)

    def get_chip_bonus(self) -> int:
        return 20


class SteelCard(Enhancement):
    """Steel Card: x1.5 chips"""
    def __init__(self):
        super().__init__("Steel Card", EnhancementType.STEEL)

    def get_chip_bonus(self) -> int:
        return 15


class GoldCard(Enhancement):
    """Gold Card: Gain $3"""
    def __init__(self):
        super().__init__("Gold Card", EnhancementType.GOLD)

    def get_chip_bonus(self) -> int:
        return 0  # Money gain handled elsewhere
