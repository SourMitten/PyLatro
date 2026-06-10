"""Shop display widget"""


class ShopDisplay:
    """Widget for displaying the shop"""

    def __init__(self):
        """Initialize shop display"""
        self.items = []
        self.is_open = False

    def render(self):
        """Render the shop"""
        pass

    def open(self):
        """Open the shop"""
        self.is_open = True

    def close(self):
        """Close the shop"""
        self.is_open = False

    def purchase_item(self, item):
        """Purchase an item from the shop"""
        pass
