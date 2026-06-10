"""Animation system for UI effects"""


class Animation:
    """Base class for animations"""

    def __init__(self, duration: float):
        """
        Initialize animation.
        
        Args:
            duration: Duration of animation in seconds
        """
        self.duration = duration
        self.elapsed = 0
        self.is_playing = False

    def start(self):
        """Start the animation"""
        self.is_playing = True
        self.elapsed = 0

    def update(self, delta_time: float):
        """
        Update animation progress.
        
        Args:
            delta_time: Time elapsed since last frame
        """
        if self.is_playing:
            self.elapsed += delta_time
            if self.elapsed >= self.duration:
                self.is_playing = False

    def is_finished(self) -> bool:
        """Check if animation is finished"""
        return not self.is_playing
