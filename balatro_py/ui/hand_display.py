"""Hand display widget"""


class HandDisplay:
    """Widget for displaying the player's current hand"""

    def __init__(self):
        """Initialize hand display"""
        self.cards = []
        self.x = 0
        self.y = 600

    def render(self):
        """Render the hand"""
        pass

    def update_cards(self, cards):
        """Update the displayed cards"""
        self.cards = cards

    def get_card_at_position(self, x, y):
        """Get card at screen position"""
        pass
