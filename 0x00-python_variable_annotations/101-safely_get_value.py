#!/usr/bin/env python3
"""get a value from dictionary"""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """return value from dic"""
    if key in dct:
        return dct[key]
    else:
        return default
