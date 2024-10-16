#!/usr/bin/env python3
"""
2-measure_runtime module
This module contains a coroutine that measures the
total runtime for executing four instances of
async_comprehension in parallel.
"""

import asyncio
import time
from importlib import import_module as using

async_comprehension = using("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime for running four instances of
    async_comprehension in parallel.

    Returns:
        float: The total runtime for executing async_comprehension
        four times.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    return time.time() - start_time
