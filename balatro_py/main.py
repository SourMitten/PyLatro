"""Main entry point for PyLatro"""

import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from ui.game_window import GameWindow


def main():
    """Initialize and run the game"""
    try:
        game_window = GameWindow(width=1280, height=800)
        game_window.run()
        game_window.mainloop()
    except Exception as e:
        print(f"Error starting game: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
