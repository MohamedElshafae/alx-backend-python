#!/usr/bin/env python3
"""function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function make_multiplier"""
    def f(n: float) -> float:
        """function make_multiplier"""
        return n * multiplier
    return f
