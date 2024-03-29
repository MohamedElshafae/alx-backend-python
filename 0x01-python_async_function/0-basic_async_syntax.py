#!/usr/bin/env python3
"""wait_random function"""
from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay and returns it"""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
