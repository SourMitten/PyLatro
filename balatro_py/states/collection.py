"""Collection state for viewing unlocked items"""

from .state_manager import State


class Collection(State):
    """Collection state for viewing discovered items"""

    def __init__(self):
        """Initialize collection"""
        super().__init__()
        self.items = []

    def enter(self):
        """Enter collection"""
        pass

    def update(self, delta_time: float):
        """Update collection"""
        pass

    def render(self):
        """Render collection"""
        pass

    def filter_by_type(self, item_type: str):
        """Filter collection by item type"""
        pass
