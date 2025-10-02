import asyncio
from functools import wraps
from typing import Callable


def synchronous(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        return asyncio.run(func(*args, **kwargs))

    return wrapper
