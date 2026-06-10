"""Mathematical utility functions"""

import math


def clamp(value: float, min_val: float, max_val: float) -> float:
    """
    Clamp a value between min and max.
    
    Args:
        value: Value to clamp
        min_val: Minimum value
        max_val: Maximum value
        
    Returns:
        Clamped value
    """
    return max(min_val, min(max_val, value))


def lerp(start: float, end: float, t: float) -> float:
    """
    Linear interpolation between two values.
    
    Args:
        start: Starting value
        end: Ending value
        t: Interpolation factor (0-1)
        
    Returns:
        Interpolated value
    """
    return start + (end - start) * t


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calculate distance between two points.
    
    Args:
        x1, y1: First point
        x2, y2: Second point
        
    Returns:
        Distance between points
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def normalize_angle(angle: float) -> float:
    """
    Normalize angle to 0-360 range.
    
    Args:
        angle: Angle in degrees
        
    Returns:
        Normalized angle
    """
    return angle % 360
