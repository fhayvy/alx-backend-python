#!/usr/bin/env python3
"""Task 2"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Create a measure_time function with integers n
    and max_delay as arguments that measures the total
    execution time for wait_n(n, max_delay),
    and returns total_time / n
    """

    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return (total_time / n)
