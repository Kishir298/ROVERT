"""
ROVERT Helper Functions
=======================
Small reusable functions used across the project.
"""


import time


def current_time_ms():
    """
    Returns current time in milliseconds.
    Useful for timing loops and communication delays.
    """
    return int(time.time() * 1000)



def clamp(value, minimum, maximum):
    """
    Keeps a value between a minimum and maximum.

    Example:
    clamp(300, 0, 255) -> 255
    """
    return max(minimum, min(value, maximum))



def timestamp():
    """
    Returns a readable timestamp.
    """
    return time.strftime("%Y-%m-%d %H:%M:%S")