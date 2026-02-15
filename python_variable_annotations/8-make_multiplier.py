#!/usr/bin/env python3
"""
doc
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    doc
    """
    def multiplier_function(n: float) -> float:
        return n * multiplier

    return multiplier_function
