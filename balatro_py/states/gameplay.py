"""Gameplay state"""

import tkinter as tk
from tkinter import ttk
from .state_manager import State
from core.run import Run
from core.round import Round
from core.deck import Deck
from content.jokers import (
    BuffetJoker, CarpenterJoker, CheekyJoker, GreedyJoker,
    InsaneJoker, SmileyJoker, BlueprintJoker
)


class Gameplay(State):
    """Main gameplay state"""

    def __init__(self, game_window):
        """Initialize gameplay"""
        super().__init__()
        self.game_window = game_window
        self.game_run = None
        self.current_round = None
        self.jokers = []
        self.frame = None
        self.selected_card_indices = set()

    def enter(self):
        """Enter gameplay"""
        # Clear previous content
        for widget in self.game_window.main_frame.winfo_children():
            widget.destroy()

        # Initialize new run
        self.game_run = Run()
        self.start_new_round()
        
        # Add some starter jokers for testing
        self.add_starter_jokers()
        
        # Create main gameplay frame
        self.frame = ttk.Frame(self.game_window.main_frame)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.render_gameplay()

    def start_new_round(self):
        """Start a new round"""
        score_goal = 300 * (2 ** (self.game_run.ante.current_ante - 1))
        self.current_round = Round(target_score=score_goal)
        self.current_round.draw_cards(5)

    def add_starter_jokers(self):
        """Add starter jokers for testing"""
        self.jokers = [
            CarpenterJoker(),
            BuffetJoker(),
        ]

    def render_gameplay(self):
        """Render the gameplay interface"""
        # Clear frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Top bar - Score and status
        top_frame = ttk.Frame(self.frame)
        top_frame.pack(fill=tk.X, padx=10, pady=10)

        status_label = ttk.Label(
            top_frame,
            text=f"Ante {self.game_run.ante.current_ante} | {self.current_round.get_status()}",
            font=("Arial", 12)
        )
        status_label.pack(side=tk.LEFT)

        money_label = ttk.Label(
            top_frame,
            text=f"Money: ${self.game_run.economy.get_balance()}",
            font=("Arial", 12)
        )
        money_label.pack(side=tk.RIGHT)

        # Middle section - Main game area
        main_area = ttk.Frame(self.frame)
        main_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left side - Jokers
        joker_frame = ttk.LabelFrame(main_area, text="Jokers", padding=10)
        joker_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=5)

        for joker in self.jokers:
            joker_label = ttk.Label(
                joker_frame,
                text=f"• {joker.name}\n  {joker.description[:40]}...",
                relief=tk.SUNKEN,
                padding=5
            )
            joker_label.pack(fill=tk.X, pady=5)

        # Center - Game display and cards
        game_display = ttk.Frame(main_area)
        game_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        # Current hand display
        cards_frame = ttk.LabelFrame(game_display, text="Your Hand", padding=10)
        cards_frame.pack(fill=tk.BOTH, expand=True)

        self.render_cards(cards_frame)

        # Bottom bar - Action buttons
        button_frame = ttk.Frame(self.frame)
        button_frame.pack(fill=tk.X, padx=10, pady=10)

        play_btn = ttk.Button(
            button_frame,
            text="Play Hand",
            command=self.on_play_hand,
            width=20
        )
        play_btn.pack(side=tk.LEFT, padx=5)

        discard_btn = ttk.Button(
            button_frame,
            text="Discard",
            command=self.on_discard,
            width=20
        )
        discard_btn.pack(side=tk.LEFT, padx=5)

        stand_btn = ttk.Button(
            button_frame,
            text="Stand",
            command=self.on_stand,
            width=20
        )
        stand_btn.pack(side=tk.LEFT, padx=5)

        score_label = ttk.Label(
            button_frame,
            text=f"Round Score: {self.current_round.round_score}",
            font=("Arial", 12, "bold")
        )
        score_label.pack(side=tk.RIGHT, padx=5)

    def render_cards(self, parent):
        """Render cards in hand"""
        for i, card in enumerate(self.current_round.hand.cards):
            is_selected = i in self.selected_card_indices
            bg_color = "#4a90e2" if is_selected else "#2a5cdb"
            
            card_btn = tk.Button(
                parent,
                text=f"{card.rank}\n{card.suit[0]}",
                bg=bg_color,
                fg="white",
                font=("Arial", 14, "bold"),
                width=8,
                height=3,
                command=lambda idx=i: self.on_card_click(idx)
            )
            card_btn.pack(side=tk.LEFT, padx=5)

    def on_card_click(self, index: int):
        """Handle card click"""
        if index in self.selected_card_indices:
            self.selected_card_indices.remove(index)
        else:
            self.selected_card_indices.add(index)
        self.render_gameplay()

    def on_play_hand(self):
        """Handle play hand action"""
        if not self.selected_card_indices:
            return

        # Select cards in hand
        for idx in self.selected_card_indices:
            if 0 <= idx < len(self.current_round.hand.cards):
                self.current_round.hand.select_card(idx)

        # Play the hand
        score = self.current_round.play_hand(self.jokers)
        self.selected_card_indices.clear()

        # Draw replacement cards
        num_played = len(self.current_round.hand.get_selected_cards())
        self.current_round.draw_cards(5 - len(self.current_round.hand.cards))

        # Check if round is complete
        if self.current_round.check_round_complete():
            if self.current_round.round_won:
                self.on_ante_won()
            else:
                self.on_ante_lost()
        else:
            self.render_gameplay()

    def on_discard(self):
        """Handle discard action"""
        if not self.selected_card_indices:
            return

        # Select cards for discard
        for idx in self.selected_card_indices:
            if 0 <= idx < len(self.current_round.hand.cards):
                self.current_round.hand.select_card(idx)

        # Perform discard
        if self.current_round.discard():
            self.selected_card_indices.clear()
            self.render_gameplay()

    def on_stand(self):
        """Handle stand action - end blind without playing more hands"""
        if self.current_round.round_score >= self.current_round.target_score:
            self.on_ante_won()
        else:
            self.on_ante_lost()

    def on_ante_won(self):
        """Handle ante won"""
        # Advance to next ante
        if self.game_run.ante.advance_ante():
            self.start_new_round()
            self.render_gameplay()
        else:
            # Game won!
            self.game_window.change_state("main_menu")

    def on_ante_lost(self):
        """Handle ante lost - game over"""
        self.game_window.change_state("main_menu")

    def update(self, delta_time: float):
        """Update gameplay"""
        pass

    def render(self):
        """Render gameplay"""
        pass
