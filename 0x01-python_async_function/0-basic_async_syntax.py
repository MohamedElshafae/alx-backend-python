#!/usr/bin/env python3
"""wait_random function"""
from random import uniform
from asyncio import sleep


async def wait_random(max_delay: int = 10) -> float:
    delay = uniform(0, max_delay)
    await sleep(delay)
    return delay
