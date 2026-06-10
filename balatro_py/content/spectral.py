"""Spectral cards and effects"""


class Spectral:
    """Base class for spectral cards"""

    def __init__(self, name: str, description: str):
        """
        Initialize a spectral card.
        
        Args:
            name: Name of the spectral
            description: Description of its effect
        """
        self.name = name
        self.description = description

    def cast(self):
        """Cast the spectral card"""
        pass

    def __repr__(self) -> str:
        return f"Spectral({self.name})"
