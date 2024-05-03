#!/usr/bin/env python3
"""return a list muliplied"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """return a list muliplied"""
    zoomed: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
