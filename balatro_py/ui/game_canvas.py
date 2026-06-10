"""Game canvas for rendering"""


class GameCanvas:
    """Canvas for rendering game elements"""

    def __init__(self, width: int, height: int):
        """
        Initialize the canvas.
        
        Args:
            width: Canvas width
            height: Canvas height
        """
        self.width = width
        self.height = height

    def draw(self):
        """Draw all game elements"""
        pass

    def update(self):
        """Update canvas state"""
        pass
