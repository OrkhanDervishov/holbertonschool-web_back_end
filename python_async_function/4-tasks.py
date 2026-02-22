#!/usr/bin/env python3
"""
Doc
"""

import asyncio
from typing import List
from heapq import heappush, heappop

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Doc
    """
    heap = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in tasks:
        delay = await task
        heappush(heap, delay)

    return [heappop(heap) for _ in range(n)]
