#!/usr/bin/env python3
"""
This module defines a function `sum_mixed_list` that
sums a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list containing integers and floats.

    Returns:
    float: The sum of all integers and floats in the list.
    """
    return float(sum(mxd_lst))
