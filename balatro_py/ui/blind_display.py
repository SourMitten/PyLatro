"""Blind display widget"""


class BlindDisplay:
    """Widget for displaying blind information"""

    def __init__(self):
        """Initialize blind display"""
        self.blind = None
        self.x = 400
        self.y = 200

    def render(self):
        """Render the blind display"""
        pass

    def set_blind(self, blind):
        """Set the blind to display"""
        self.blind = blind

    def show_score_goal(self):
        """Display the score goal"""
        pass
