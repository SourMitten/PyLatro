"""Voucher cards and effects"""

from enum import Enum


class VoucherType(Enum):
    """Voucher types"""
    TAROT_GRABBER = "tarot_grabber"
    PLANET_GRABBER = "planet_grabber"
    TELESCOPE = "telescope"
    CRYSTAL_BALL = "crystal_ball"
    MONEY_CLIP = "money_clip"
    MASTERCARD = "mastercard"
    DIRECTORATE = "directorate"
    MAGIC_TRICK = "magic_trick"
    ILLUSION = "illusion"


class Voucher:
    """Base class for voucher cards"""

    def __init__(self, name: str, description: str, voucher_type: VoucherType = None, cost: int = 10):
        """
        Initialize a voucher.
        
        Args:
            name: Name of the voucher
            description: Description of its effect
            voucher_type: Type of voucher
            cost: Cost to purchase
        """
        self.name = name
        self.description = description
        self.voucher_type = voucher_type
        self.cost = cost
        self.is_active = False
        self.uses_left = 1

    def activate(self):
        """Activate the voucher"""
        self.is_active = True

    def use(self) -> bool:
        """Use the voucher"""
        if self.uses_left > 0:
            self.uses_left -= 1
            return True
        return False

    def __repr__(self) -> str:
        return f"Voucher({self.name})"


# Specific Voucher implementations
class TarotGrabber(Voucher):
    """Tarot Grabber: Adds a Tarot card in each shop"""
    def __init__(self):
        super().__init__("Tarot Grabber", "Grants a Tarot card in each shop", VoucherType.TAROT_GRABBER, 10)


class PlanetGrabber(Voucher):
    """Planet Grabber: Adds a Planet card in each shop"""
    def __init__(self):
        super().__init__("Planet Grabber", "Grants a Planet card in each shop", VoucherType.PLANET_GRABBER, 10)


class Telescope(Voucher):
    """Telescope: Identifies a random Planet for you"""
    def __init__(self):
        super().__init__("Telescope", "Identifies a random Planet", VoucherType.TELESCOPE, 15)
