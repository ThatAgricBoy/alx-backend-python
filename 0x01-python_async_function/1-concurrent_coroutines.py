# Import wait_random from random_delay.py
from . import wait_random

import asyncio


async def wait_n(n, max_delay=10):
    """
    Asynchronous routine that spawns wait_random n times with the
    specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (float): The maximum delay in seconds (default is 10).

    Returns:
        list of float: List of delays in ascending order.
    """
    # Create a list to store the delays
    delays = []

    # Create a list of tasks for wait_random
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Use asyncio.gather to execute tasks concurrently
    results = await asyncio.gather(*tasks)

    # Add the results to the delays list
    delays.extend(results)

    # Sort the delays in ascending order
    delays.sort()

    return delays
