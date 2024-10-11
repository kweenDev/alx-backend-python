#!/usr/bin/env python3
"""
This module defines a function `safely_get_value` that
safely gets a value from a dictionary.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: typing.Mapping, key: typing.Any, default:
                     typing.Union[T, None] = None) -> \
        typing.Union[typing.Any, T]:
    """
    Safely gets a value from a dictionary by key, or returns a default value if
    the key does not exist.

    Parameters:
    dct (Mapping[Any, Any]): A dictionary.
    key (Any): A key to search for.
    default (Union[T, None]): The default value if the key is not found.

    Returns:
    Union[Any, T]: The value associated with the key, or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
