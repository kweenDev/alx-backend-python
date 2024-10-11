#!/usr/bin/env python3
"""
This module defines a function `zoom_array` that zooms in a tuple.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zooms in a tuple by repeating each item in the tuple a specified number of times.

    Parameters:
    lst (Tuple[int, ...]): A tuple of integers.
    factor (int): The factor by which to zoom in.

    Returns:
    List[int]: A list containing the zoomed in values.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
