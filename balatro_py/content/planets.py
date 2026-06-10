"""Planet cards and effects"""

from enum import Enum
from typing import List


class PlanetType(Enum):
    """Planet types"""
    MERCURY = "mercury"
    VENUS = "venus"
    EARTH = "earth"
    MARS = "mars"
    JUPITER = "jupiter"
    SATURN = "saturn"
    URANUS = "uranus"
    NEPTUNE = "neptune"


class Planet:
    """Base class for planet cards"""

    def __init__(self, name: str, description: str, planet_type: PlanetType = None, level_bonus: int = 1):
        """
        Initialize a planet card.
        
        Args:
            name: Name of the planet
            description: Description of its effect
            planet_type: Type of planet
            level_bonus: Level increase for poker hand
        """
        self.name = name
        self.description = description
        self.planet_type = planet_type
        self.level_bonus = level_bonus

    def apply_effect(self, hand_type: str = None) -> tuple:
        """
        Apply the planet's effect to a poker hand.
        
        Returns:
            Tuple of (chip_bonus, mult_bonus)
        """
        return (0, 1.0)

    def __repr__(self) -> str:
        return f"Planet({self.name})"


# Specific Planet implementations
class MercuryPlanet(Planet):
    """Mercury: Upgrades High Card"""
    def __init__(self):
        super().__init__("Mercury", "Levels up High Card", PlanetType.MERCURY, 1)


class VenusPlanet(Planet):
    """Venus: Upgrades Pair"""
    def __init__(self):
        super().__init__("Venus", "Levels up Pair", PlanetType.VENUS, 1)


class MarsIsPlanet(Planet):
    """Mars: Upgrades Five of a Kind"""
    def __init__(self):
        super().__init__("Mars", "Levels up Five of a Kind", PlanetType.MARS, 1)


class JupiterPlanet(Planet):
    """Jupiter: Upgrades Five of a Kind"""
    def __init__(self):
        super().__init__("Jupiter", "Levels up Five of a Kind", PlanetType.JUPITER, 1)
