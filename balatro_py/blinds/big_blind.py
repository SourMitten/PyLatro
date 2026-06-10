"""Big blind implementation"""

from .blind_base import Blind


class BigBlind(Blind):
    """Big blind - medium difficulty"""

    def __init__(self):
        """Initialize big blind"""
        super().__init__("Big Blind", "Harder blind with additional challenge")
        self.score_goal = 600

    def apply_effect(self):
        """Apply big blind effect"""
        # Apply challenging rules
        pass
