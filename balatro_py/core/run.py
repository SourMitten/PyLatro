"""Game run/session management"""

from typing import List
from .ante import Ante
from .round import Round
from .economy import Economy


class Run:
    """Manages an entire game run/session"""

    def __init__(self):
        """Initialize a new run"""
        self.ante = Ante()
        self.rounds: List[Round] = []
        self.economy = Economy()
        self.is_active = True

    def start_new_ante(self):
        """Start a new ante"""
        self.rounds.append(Round())

    def complete_current_ante(self) -> bool:
        """
        Complete the current ante.
        
        Returns:
            True if successful
        """
        return self.ante.advance_ante()

    def end_run(self):
        """End the current run"""
        self.is_active = False

    def get_current_round(self) -> Round:
        """Get the current round"""
        return self.rounds[-1] if self.rounds else None

    def get_run_score(self) -> int:
        """Get total score for the run"""
        return sum(round.score for round in self.rounds)
