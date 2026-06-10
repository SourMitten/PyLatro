"""Small blind implementation"""

from .blind_base import Blind


class SmallBlind(Blind):
    """Small blind - easier difficulty"""

    def __init__(self):
        """Initialize small blind"""
        super().__init__("Small Blind", "Standard blind with normal rules")
        self.score_goal = 300

    def apply_effect(self):
        """Apply small blind effect"""
        # Apply standard rules
        pass
