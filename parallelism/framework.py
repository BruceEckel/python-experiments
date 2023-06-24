from concurrent.futures import ProcessPoolExecutor
import time
import os
from rust_extension import cpu_intensive


class RunCPUIntensive:
    def __enter__(self):
        self.multiplier = 1  # Increase for longer computations
        logical_processors = os.cpu_count()
        print(f"{logical_processors = }")
        self.tasks = (logical_processors - 0) * 1  # Try different numbers
        print(f"{self.tasks = }")
        self.start = time.monotonic()
        self.results = []

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.monotonic() - self.start
        print(f"{list(self.results)}\nElapsed time: {elapsed_time:.2f}s")


if __name__ == "__main__":
    with RunCPUIntensive() as test:
        with ProcessPoolExecutor() as executor:
            test.results = executor.map(
                cpu_intensive, range(test.tasks), [test.multiplier] * test.tasks
            )

    # multiplier = 1  # Increase for longer computations
    # logical_processors = os.cpu_count()
    # print(f"{logical_processors = }")
    # tasks = (logical_processors - 0) * 1  # Try different numbers
    # print(f"{tasks = }")
    # start = time.monotonic()

    # with ProcessPoolExecutor() as executor:
    #     results = executor.map(cpu_intensive, range(tasks), [multiplier] * tasks)

    # print(f"{list(results)}\nElapsed time: {time.monotonic() - start:.2f}s")
