#!/usr/bin/env python3
"""return first element of a list"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return none or first element of a list"""
    if lst:
        return lst[0]
    else:
        return None
