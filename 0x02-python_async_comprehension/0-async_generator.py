#!/usr/bin/env python3
"""
0-async_generator module
This module contains the definition of
an async generator.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields random numbers between 0 and 10.

    This generator yields 10 random float values asynchronously. It waits
    for 1 second between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
