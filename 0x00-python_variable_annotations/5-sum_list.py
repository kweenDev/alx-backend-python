#!/usr/bin/env python3
"""
This module defines a function `sum_list` that sums a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats.

    Parameters:
    input_list (List[float]): A list of float numbers.

    Returns:
    float: The sum of all floats in the list.
    """
    return sum(input_list)
