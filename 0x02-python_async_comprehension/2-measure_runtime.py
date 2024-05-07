#!/usr/bin/env python3
""" measure runtime """
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measue runtime """
    start: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end: float = time.perf_counter()
    return (end - start)
