#!/usr/bin/env python3
"""Task 1"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times.
    """
    delays: List[float] = []
    tasks: List[asyncio.Task] = []

    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for future in asyncio.as_completed(tasks):
        delay = await future
        delays.append(delay)

    return delays
