#!/usr/bin/env python3
""" async """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ more than one async"""
    dela: List[float] = []
    all_del: List[float] = []
    for i in range(n):
        dela.append(wait_random(max_delay))
    for delay in asyncio.as_completed(dela):
        earliest_result = await delay
        all_del.append(earliest_result)
    return all_del
