"""Card class representing individual playing cards"""


class Card:
    """Represents a single card in the game"""

    def __init__(self, suit: str, rank: str):
        """
        Initialize a card.
        
        Args:
            suit: The suit of the card (Spades, Hearts, Diamonds, Clubs)
            rank: The rank of the card (2-10, J, Q, K, A)
        """
        self.suit = suit
        self.rank = rank
        self.enhancement = None
        self.seal = None
        self.edition = None

    def __repr__(self) -> str:
        return f"{self.rank} of {self.suit}"
