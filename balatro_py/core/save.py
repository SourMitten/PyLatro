"""Save system for game state persistence"""

import json
import os
from typing import Dict, Any


class SaveManager:
    """Manages saving and loading game state"""

    def __init__(self, save_dir: str = "saves"):
        """
        Initialize save manager.
        
        Args:
            save_dir: Directory to store save files
        """
        self.save_dir = save_dir
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

    def save_game(self, filename: str, game_state: Dict[str, Any]) -> bool:
        """
        Save game state to file.
        
        Args:
            filename: Name of the save file
            game_state: Dictionary containing game state
            
        Returns:
            True if successful
        """
        try:
            filepath = os.path.join(self.save_dir, f"{filename}.json")
            with open(filepath, "w") as f:
                json.dump(game_state, f, indent=2)
            return True
        except Exception:
            return False

    def load_game(self, filename: str) -> Dict[str, Any]:
        """
        Load game state from file.
        
        Args:
            filename: Name of the save file
            
        Returns:
            Dictionary containing game state
        """
        try:
            filepath = os.path.join(self.save_dir, f"{filename}.json")
            with open(filepath, "r") as f:
                return json.load(f)
        except Exception:
            return {}

    def list_saves(self) -> list:
        """List all available saves"""
        return [f[:-5] for f in os.listdir(self.save_dir) if f.endswith(".json")]
