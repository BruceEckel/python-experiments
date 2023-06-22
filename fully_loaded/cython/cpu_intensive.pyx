import cython
import math

def cpu_intensive(n: cython.int, multiplier: cython.int) -> cython.double:
    result: cython.double = 0.0
    i: cython.ulong

    for i in range(10_000_000 * multiplier):
        result += math.sqrt(i**3 + i**2 + i * n)

    return result
