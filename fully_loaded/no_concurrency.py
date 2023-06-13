from concurrent.futures import ProcessPoolExecutor
import math
import time
import os


def cpu_intensive(n, multiplier):
    result = 0
    for i in range(10**7 * multiplier):
        result += math.sqrt(i**3 + i**2 + i * n)
    return result


if __name__ == "__main__":
    multiplier = 1  # Increase for longer computations
    logical_processors = os.cpu_count()
    print(f"{logical_processors = }")
    tasks = (logical_processors - 0) * 1  # Try different numbers
    print(f"{tasks = }")
    start = time.monotonic()

    results = [cpu_intensive(n, multiplier) for n in range(tasks)]

    print(results)
    print(f"Elapsed time: {time.monotonic() - start:.2f}s")
