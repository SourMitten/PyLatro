"""Ante system for managing game progression"""


class Ante:
    """Manages antes and difficulty progression"""

    def __init__(self, starting_ante: int = 1):
        """
        Initialize ante system.
        
        Args:
            starting_ante: Starting ante level
        """
        self.current_ante = starting_ante
        self.max_ante = 8

    def get_current_ante(self) -> int:
        """Get the current ante level"""
        return self.current_ante

    def advance_ante(self) -> bool:
        """
        Advance to the next ante.
        
        Returns:
            True if successfully advanced, False if at max ante
        """
        if self.current_ante < self.max_ante:
            self.current_ante += 1
            return True
        return False

    def get_score_goal(self) -> int:
        """
        Get the score goal for current ante.
        
        Returns:
            The required score to beat the ante
        """
        return 300 * (2 ** (self.current_ante - 1))

    def reset(self):
        """Reset ante to starting level"""
        self.current_ante = 1
