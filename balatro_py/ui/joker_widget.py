"""Joker widget for displaying jokers"""


class JokerWidget:
    """Widget for displaying a joker card"""

    def __init__(self, joker=None):
        """
        Initialize joker widget.
        
        Args:
            joker: The joker to display
        """
        self.joker = joker
        self.x = 0
        self.y = 0
        self.width = 100
        self.height = 100

    def render(self):
        """Render the joker"""
        pass

    def on_click(self):
        """Handle click event"""
        pass
