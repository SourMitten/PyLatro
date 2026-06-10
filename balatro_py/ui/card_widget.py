"""Card widget for displaying cards"""


class CardWidget:
    """Widget for displaying a single card"""

    def __init__(self, card=None):
        """
        Initialize card widget.
        
        Args:
            card: The card to display
        """
        self.card = card
        self.x = 0
        self.y = 0
        self.width = 100
        self.height = 150

    def render(self):
        """Render the card"""
        pass

    def on_click(self):
        """Handle click event"""
        pass
