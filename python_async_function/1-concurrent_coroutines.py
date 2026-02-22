#!/usr/bin/env python3
"""
Doc
"""

import asyncio
from typing import List
from heapq import heappush, heappop

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Doc
    """
    heap = []
    tasks = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    for task in tasks:
        delay = await task
        heappush(heap, delay)

    delays = [heappop(heap) for _ in range(n)]
    return delays
