#!/usr/bin/env python3
"""
1-async_comprehension module
This module contains the definition of an async comprehension function.
"""

import asyncio
from typing import List
from importlib import import_module as using

async_generator = using("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehensions over
    async_generator.

    Returns:
        List[float]: A list containing 10 random float numbers.
    """
    return [num async for num in async_generator()]
