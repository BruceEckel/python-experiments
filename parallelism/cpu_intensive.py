import math


def cpu_intensive(n: int, multiplier: int) -> float:
    result: float = 0
    for i in range(10_000_000 * multiplier):
        result += math.sqrt(i**3 + i**2 + i * n)
    return result
