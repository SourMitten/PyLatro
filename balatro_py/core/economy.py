"""Economy system for managing money and shop"""


class Economy:
    """Handles money and economy mechanics"""

    def __init__(self, starting_money: int = 4):
        """
        Initialize the economy.
        
        Args:
            starting_money: Starting amount of money
        """
        self.money = starting_money
        self.interest_rate = 0.25

    def add_money(self, amount: int):
        """Add money to the player's balance"""
        self.money += amount

    def spend_money(self, amount: int) -> bool:
        """
        Spend money from the player's balance.
        
        Args:
            amount: Amount to spend
            
        Returns:
            True if successful, False if insufficient funds
        """
        if self.money >= amount:
            self.money -= amount
            return True
        return False

    def calculate_interest(self) -> int:
        """
        Calculate interest earned at end of round.
        
        Returns:
            Interest amount
        """
        return int(self.money * self.interest_rate)

    def get_balance(self) -> int:
        """Get current money balance"""
        return self.money
