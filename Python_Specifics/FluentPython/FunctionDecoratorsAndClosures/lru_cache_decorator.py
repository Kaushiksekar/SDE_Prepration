import functools
from simple_decorator import clock

@functools.lru_cache() # optimizes with memoization by removing from cache by using LRU technique
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == "__main__":
    print(fibonacci(6))
