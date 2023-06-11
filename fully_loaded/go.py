from concurrent.futures import ProcessPoolExecutor
import math
import time
import os


def computation(n):  # CPU-intensive
    multiplier = 1  # Increase for longer computations
    result = 0
    for i in range(10**7 * multiplier):
        result += math.sqrt(i**3 + i**2 + i * n)
    return result


if __name__ == "__main__":
    start = time.monotonic()
    logical_processors = os.cpu_count()
    print(f"{logical_processors = }")
    tasks = (logical_processors - 0) * 1  # Try different number of tasks
    print(f"{tasks = }")

    with ProcessPoolExecutor() as executor:
        results = executor.map(computation, range(tasks))

    print(list(results))
    print(f"Elapsed time: {time.monotonic()-start:.2f}s")
