from concurrent.futures import ProcessPoolExecutor
import math
import time

MULTIPLIER = 1  # Increase for longer computations


def computation(n):  # CPU-intensive
    result = 0
    for i in range(10**7 * MULTIPLIER):
        result += math.sqrt(i**3 + i**2 + i * n)
    return result


if __name__ == "__main__":
    start = time.monotonic()
    print(f"{MULTIPLIER = }")

    with ProcessPoolExecutor() as executor:
        logical_processors = executor._max_workers
        print(f"{logical_processors = }")
        tasks = (logical_processors - 0) * 1  # Try different numbers of tasks
        print(f"{tasks = }")
        results = executor.map(computation, range(tasks))

    print(list(results))
    print(f"Elapsed time: {time.monotonic()-start:.2f}s")
