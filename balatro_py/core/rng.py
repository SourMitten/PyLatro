"""Random number generation system"""

import random
from typing import List, TypeVar, Any

T = TypeVar("T")


class RNG:
    """Handles all randomization for the game"""

    def __init__(self, seed: int = None):
        """
        Initialize RNG.
        
        Args:
            seed: Random seed for reproducibility
        """
        if seed is not None:
            random.seed(seed)
        self.seed = seed

    def random_int(self, min_val: int, max_val: int) -> int:
        """
        Generate random integer in range.
        
        Args:
            min_val: Minimum value (inclusive)
            max_val: Maximum value (inclusive)
            
        Returns:
            Random integer
        """
        return random.randint(min_val, max_val)

    def random_choice(self, items: List[T]) -> T:
        """
        Choose random item from list.
        
        Args:
            items: List to choose from
            
        Returns:
            Random item from list
        """
        return random.choice(items)

    def random_shuffle(self, items: List[T]) -> List[T]:
        """
        Shuffle a list.
        
        Args:
            items: List to shuffle
            
        Returns:
            Shuffled list
        """
        shuffled = items.copy()
        random.shuffle(shuffled)
        return shuffled
