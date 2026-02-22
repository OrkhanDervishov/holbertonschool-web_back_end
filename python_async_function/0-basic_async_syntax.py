#!/usr/bin/env python3
"""
Doc
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Doc
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
