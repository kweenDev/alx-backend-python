#!/usr/bin/env python3
"""
This module defines a function `to_kv` that returns a tuple with a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of a number.

    Parameters:
    k (str): A string.
    v (Union[int, float]): An integer or float.

    Returns:
    Tuple[str, float]: A tuple where the first element is the string k, and the second element
    is the square of the number v as a float.
    """
    return (k, float(v ** 2))
