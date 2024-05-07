#!/usr/bin/env python3
""" async """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measure time """
    s_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    e_time = time.time()
    total_time = e_time - s_time
    return total_time / n
