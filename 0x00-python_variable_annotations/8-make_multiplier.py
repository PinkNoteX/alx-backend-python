#!/usr/bin/env python3
"""Contains a function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ multiply a num by muliplier """

    def multi_func(num: float) -> float:
        """ function to return """
        return multiplier * num

    return multi_func
