#!/usr/bin/env python3
"""
Module that creates an asyncio task from a coroutine.
"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
   Creates an asyncio task from the wait_random coroutine.

   Args:
       max_delay (int): The maximum delay in seconds for the task.

   Returns:
       asyncio.Task: The asyncio Task that wraps the coroutine.
   """
    return asyncio.create_task(wait_random(max_delay))
