#!/usr/bin/env python3
"""wait_random function"""
from random import uniform


async def wait_random(max_delay=10):
    return uniform(0, max_delay)
