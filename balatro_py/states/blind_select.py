"""Blind selection state"""

from .state_manager import State


class BlindSelect(State):
    """State for selecting blind at start of ante"""

    def __init__(self):
        """Initialize blind select"""
        super().__init__()
        self.available_blinds = []

    def enter(self):
        """Enter blind select"""
        # Generate available blinds
        pass

    def update(self, delta_time: float):
        """Update blind select"""
        pass

    def render(self):
        """Render blind select"""
        pass

    def select_blind(self, blind):
        """Select a blind"""
        pass
