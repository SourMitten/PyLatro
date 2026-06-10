"""Tooltip system for UI hints"""


class Tooltip:
    """Tooltip widget for displaying information"""

    def __init__(self, text: str):
        """
        Initialize tooltip.
        
        Args:
            text: Text to display in tooltip
        """
        self.text = text
        self.x = 0
        self.y = 0
        self.visible = False

    def show(self, x: int, y: int):
        """
        Show tooltip at position.
        
        Args:
            x: X position
            y: Y position
        """
        self.x = x
        self.y = y
        self.visible = True

    def hide(self):
        """Hide the tooltip"""
        self.visible = False

    def render(self):
        """Render the tooltip"""
        pass
