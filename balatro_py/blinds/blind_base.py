"""Base blind class"""


class Blind:
    """Base class for all blinds"""

    def __init__(self, name: str, description: str):
        """
        Initialize a blind.
        
        Args:
            name: Name of the blind
            description: Description of its effect
        """
        self.name = name
        self.description = description
        self.score_goal = 1000
        self.active = False

    def activate(self):
        """Activate the blind"""
        self.active = True

    def deactivate(self):
        """Deactivate the blind"""
        self.active = False

    def apply_effect(self):
        """Apply the blind's effect"""
        pass

    def __repr__(self) -> str:
        return f"Blind({self.name})"
