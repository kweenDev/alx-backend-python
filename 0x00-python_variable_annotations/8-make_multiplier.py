#!/usr/bin/env python3
"""
This module defines a function `make_multiplier` that returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Parameters:
    multiplier (float): The multiplier.

    Returns:
    Callable[[float], float]: A function that multiplies a float by multiplier.
    """
    return lambda x: x * multiplier
