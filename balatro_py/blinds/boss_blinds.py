"""Boss blind implementations"""

from .blind_base import Blind


class BossBlind(Blind):
    """Boss blind - highest difficulty"""

    def __init__(self, name: str = "Boss Blind"):
        """
        Initialize a boss blind.
        
        Args:
            name: Name of the boss blind
        """
        super().__init__(name, "Boss blind with unique effect")
        self.score_goal = 3000

    def apply_effect(self):
        """Apply boss blind effect"""
        # Apply boss-specific rules
        pass
