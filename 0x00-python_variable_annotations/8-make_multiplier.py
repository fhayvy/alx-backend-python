#!/usr/bin/env python3
"""Task 8"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float multiplier as argument
    and returns a function that multiplies
    a float by multiplier"""

    def multiplier_function(n: float) -> float:
        """The multiplier function"""

        return n * multiplier
    return multiplier_function
