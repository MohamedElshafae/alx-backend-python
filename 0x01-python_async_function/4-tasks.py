#!/usr/bin/env python3
"""wait_random function"""
import asyncio
from typing import List
import asyncio
task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """waits for a random delay between 0 and max_delay"""
    return sorted(await asyncio
                  .gather(*(task_wait_random(max_delay) for _ in range(n))))
