#!/usr/bin/env python3
"""
This module defines a function `element_length` that returns a list of tuples
with elements and their lengths.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with each element and its length.

    Parameters:
    lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a sequence
    and its length.
    """
    return [(i, len(i)) for i in lst]
