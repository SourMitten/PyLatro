"""Main menu state"""

import tkinter as tk
from tkinter import ttk
from .state_manager import State


class MainMenu(State):
    """Main menu state"""

    def __init__(self, game_window):
        """Initialize main menu"""
        super().__init__()
        self.game_window = game_window
        self.buttons = []
        self.frame = None

    def enter(self):
        """Enter main menu"""
        # Clear previous content
        for widget in self.game_window.main_frame.winfo_children():
            widget.destroy()

        # Create menu frame
        self.frame = ttk.Frame(self.game_window.main_frame)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title = ttk.Label(
            self.frame,
            text="PyLatro",
            font=("Arial", 48, "bold")
        )
        title.pack(pady=50)

        # Subtitle
        subtitle = ttk.Label(
            self.frame,
            text="A Python Implementation of Balatro",
            font=("Arial", 14)
        )
        subtitle.pack(pady=10)

        # Buttons
        button_frame = ttk.Frame(self.frame)
        button_frame.pack(pady=50)

        new_game_btn = ttk.Button(
            button_frame,
            text="New Game",
            command=self.on_new_game,
            width=20
        )
        new_game_btn.pack(pady=10)
        self.buttons.append(new_game_btn)

        continue_btn = ttk.Button(
            button_frame,
            text="Continue Game",
            command=self.on_continue,
            width=20
        )
        continue_btn.pack(pady=10)
        self.buttons.append(continue_btn)

        collection_btn = ttk.Button(
            button_frame,
            text="Collection",
            command=self.on_collection,
            width=20
        )
        collection_btn.pack(pady=10)
        self.buttons.append(collection_btn)

        quit_btn = ttk.Button(
            button_frame,
            text="Quit",
            command=self.on_quit,
            width=20
        )
        quit_btn.pack(pady=10)
        self.buttons.append(quit_btn)

    def update(self, delta_time: float):
        """Update main menu"""
        pass

    def render(self):
        """Render main menu"""
        pass

    def on_new_game(self):
        """Handle new game button"""
        self.game_window.change_state("gameplay")

    def on_continue(self):
        """Handle continue game button"""
        # TODO: Load save file
        self.game_window.change_state("gameplay")

    def on_collection(self):
        """Handle collection button"""
        # TODO: Go to collection state
        pass

    def on_quit(self):
        """Handle quit button"""
        self.game_window.close()
