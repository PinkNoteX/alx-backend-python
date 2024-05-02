#!/usr/bin/env python3
"""return ls of tuples with length of elements"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """return ls of tuples with length of elements"""
    return [(i, len(i)) for i in lst]
