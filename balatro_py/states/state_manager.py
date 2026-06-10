"""State manager for handling game states"""

from typing import Dict, Type


class State:
    """Base class for game states"""

    def __init__(self):
        """Initialize state"""
        pass

    def enter(self):
        """Called when entering this state"""
        pass

    def exit(self):
        """Called when exiting this state"""
        pass

    def update(self, delta_time: float):
        """
        Update state.
        
        Args:
            delta_time: Time elapsed since last update
        """
        pass

    def render(self):
        """Render the state"""
        pass


class StateManager:
    """Manages game state transitions"""

    def __init__(self):
        """Initialize state manager"""
        self.states: Dict[str, State] = {}
        self.current_state: State = None

    def register_state(self, name: str, state: State):
        """
        Register a state.
        
        Args:
            name: Name of the state
            state: State instance
        """
        self.states[name] = state

    def change_state(self, name: str):
        """
        Change to a different state.
        
        Args:
            name: Name of the state to change to
        """
        if self.current_state:
            self.current_state.exit()
        
        if name in self.states:
            self.current_state = self.states[name]
            self.current_state.enter()

    def update(self, delta_time: float):
        """Update current state"""
        if self.current_state:
            self.current_state.update(delta_time)

    def render(self):
        """Render current state"""
        if self.current_state:
            self.current_state.render()
