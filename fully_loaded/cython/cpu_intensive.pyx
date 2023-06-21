import cython
import math

def cpu_intensive(n: cython.int, multiplier: cython.int) -> cython.double:
    result: cython.double = 0.0
    i: cython.int

    for i in range(int(1e7 * multiplier)):
        result += math.sqrt(i**3 + i**2 + i * n)

    return result
