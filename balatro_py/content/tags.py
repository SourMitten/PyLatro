"""Game tags and modifiers"""


class Tag:
    """Base class for game tags"""

    def __init__(self, name: str, description: str):
        """
        Initialize a tag.
        
        Args:
            name: Name of the tag
            description: Description of what it does
        """
        self.name = name
        self.description = description

    def __repr__(self) -> str:
        return f"Tag({self.name})"
