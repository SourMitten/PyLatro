"""Game over state"""

from .state_manager import State


class GameOver(State):
    """Game over state"""

    def __init__(self):
        """Initialize game over"""
        super().__init__()
        self.final_score = 0
        self.victory = False

    def enter(self):
        """Enter game over"""
        pass

    def update(self, delta_time: float):
        """Update game over"""
        pass

    def render(self):
        """Render game over screen"""
        pass

    def set_result(self, score: int, victory: bool):
        """Set game result"""
        self.final_score = score
        self.victory = victory

    def on_restart(self):
        """Handle restart"""
        pass

    def on_main_menu(self):
        """Return to main menu"""
        pass
