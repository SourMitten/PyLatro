"""Logger for game events"""

import logging
from datetime import datetime


class GameLogger:
    """Logger for game events and debugging"""

    def __init__(self, log_file: str = "game.log"):
        """
        Initialize logger.
        
        Args:
            log_file: Path to log file
        """
        self.logger = logging.getLogger("PyLatro")
        self.logger.setLevel(logging.DEBUG)
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def debug(self, message: str):
        """Log debug message"""
        self.logger.debug(message)

    def info(self, message: str):
        """Log info message"""
        self.logger.info(message)

    def warning(self, message: str):
        """Log warning message"""
        self.logger.warning(message)

    def error(self, message: str):
        """Log error message"""
        self.logger.error(message)

    def critical(self, message: str):
        """Log critical message"""
        self.logger.critical(message)


# Create global logger instance
logger = GameLogger()
