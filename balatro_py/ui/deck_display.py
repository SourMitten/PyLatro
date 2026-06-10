"""Deck display widget"""


class DeckDisplay:
    """Widget for displaying deck information"""

    def __init__(self):
        """Initialize deck display"""
        self.deck = None

    def render(self):
        """Render the deck display"""
        pass

    def set_deck(self, deck):
        """Set the deck to display"""
        self.deck = deck

    def show_remaining(self):
        """Display remaining cards"""
        pass
