from cpu_intensive import cpu_intensive
from concurrent.futures import ProcessPoolExecutor
import time
import os


if __name__ == "__main__":
    multiplier = 1  # Increase for longer computations
    logical_processors = os.cpu_count()
    print(f"{logical_processors = }")
    tasks = (logical_processors - 0) * 1  # Try different numbers
    print(f"{tasks = }")
    start = time.monotonic()

    with ProcessPoolExecutor() as executor:
        results = executor.map(cpu_intensive, range(tasks), [multiplier] * tasks)

    print(list(results))
    print(f"Elapsed time: {time.monotonic() - start:.2f}s")
