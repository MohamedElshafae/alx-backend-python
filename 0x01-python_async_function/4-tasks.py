#!/usr/bin/env python3
"""wait_random function"""
from asyncio.tasks import create_task
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """waits for a random delay between 0 and max_delay and returns it"""

    return await asyncio.gather(*(task_wait_random(max_delay) for _ in range(n)))