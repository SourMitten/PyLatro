"""Main game window using tkinter"""

import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from states.state_manager import StateManager
from states.main_menu import MainMenu
from states.gameplay import Gameplay


class GameWindow:
    """Main game window and display"""

    def __init__(self, width: int = 1024, height: int = 768):
        """
        Initialize the game window.
        
        Args:
            width: Window width in pixels
            height: Window height in pixels
        """
        self.width = width
        self.height = height
        self.is_running = False
        
        # Initialize tkinter
        self.root = tk.Tk()
        self.root.title("PyLatro")
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)
        
        # Configure style
        self.root.configure(bg="#1a1a2e")
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create state manager
        self.state_manager = StateManager()
        self.setup_states()
        
        # Bind window close
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
        # Frame timing
        self.frame_time = 16  # ~60 FPS
        self.is_running = False

    def setup_states(self):
        """Setup game states"""
        main_menu = MainMenu(self)
        gameplay = Gameplay(self)
        
        self.state_manager.register_state("main_menu", main_menu)
        self.state_manager.register_state("gameplay", gameplay)
        
        # Start at main menu
        self.state_manager.change_state("main_menu")

    def run(self):
        """Start the game loop"""
        self.is_running = True
        self.game_loop()

    def game_loop(self):
        """Main game loop"""
        if self.is_running:
            # Update current state
            self.state_manager.update(self.frame_time / 1000.0)
            
            # Render current state
            self.state_manager.render()
            
            # Schedule next frame
            self.root.after(self.frame_time, self.game_loop)
        else:
            self.root.quit()

    def change_state(self, state_name: str):
        """Change to a different state"""
        self.state_manager.change_state(state_name)

    def close(self):
        """Close the game window"""
        self.is_running = False
        self.root.destroy()

    def get_canvas(self) -> tk.Canvas:
        """Get the main canvas for drawing"""
        if not hasattr(self, 'canvas'):
            self.canvas = tk.Canvas(
                self.main_frame,
                width=self.width,
                height=self.height,
                bg="#1a1a2e",
                highlightthickness=0
            )
            self.canvas.pack()
        return self.canvas

    def mainloop(self):
        """Start the tkinter mainloop"""
        self.root.mainloop()
