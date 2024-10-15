#!/usr/bin/env python3
"""
Module that executes multiple tasks concurrently.
"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times concurrently using asyncio tasks.

    Args:
        n (int): The number of tasks to execute.
        max_delay (int): The maximum delay for each task.

    Returns:
    List[float]: List of the random delays, sorted in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
