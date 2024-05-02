#!/usr/bin/env python3
"""sum list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum a list of floats"""
    if input_list is None:
        return 0
    else:
        return sum(input_list)
