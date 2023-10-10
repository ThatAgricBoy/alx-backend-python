import asyncio
import random

async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (float): The maximum delay in seconds (default is 10).

    Returns:
        float: The random delay that was waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

