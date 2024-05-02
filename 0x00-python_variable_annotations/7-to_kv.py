#!/usr/bin/env python3
"""convert to KV pair"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """convert to KV pair"""
    return k, v ** 2
