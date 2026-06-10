"""Shop state"""

from .state_manager import State


class Shop(State):
    """Shop state for purchasing items"""

    def __init__(self):
        """Initialize shop"""
        super().__init__()
        self.available_items = []

    def enter(self):
        """Enter shop"""
        # Generate available items
        pass

    def update(self, delta_time: float):
        """Update shop"""
        pass

    def render(self):
        """Render shop"""
        pass

    def purchase_item(self, item):
        """Purchase an item"""
        pass

    def refresh_shop(self):
        """Refresh available items"""
        pass
