#!/usr/bin/env python3
""" async """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Tasks """
    dela: List[float] = []
    all_del: List[float] = []
    for i in range(n):
        dela.append(task_wait_random(max_delay))
    for delay in asyncio.as_completed(dela):
        earliest_result = await delay
        all_del.append(earliest_result)
    return all_del
