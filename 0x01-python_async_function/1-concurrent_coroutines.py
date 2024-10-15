#!/usr/bin/env python3
"""
Module that contains a coroutine for executing multiple coroutines concurrently.
"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes wait_random n times concurrently.

    Args:
        n (int): The number of times to execute wait_random.
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        List[float]: List of the random delays, sorted in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
