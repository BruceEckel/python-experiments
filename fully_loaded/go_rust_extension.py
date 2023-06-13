from concurrent.futures import ProcessPoolExecutor
import math
import time
import os
from rust_extension import cpu_intensive


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
