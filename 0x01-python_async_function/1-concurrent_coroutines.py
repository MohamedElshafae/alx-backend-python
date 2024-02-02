#!/usr/bin/env python3
"""wait_random function"""
from typing import List
import asyncio
from random import uniform
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """waits for a random delay between 0 and max_delay and returns it"""
    res = []
    for i in range(n):
        delay = await wait_random(max_delay)
        res.append(delay)
    return sorted(res)
