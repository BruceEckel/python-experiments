import multiprocessing
import trio
import trio_parallel
import os
import math


def cpu_intensive(n: int, multiplier: int) -> float:
    result: float = 0
    for i in range(10_000_000 * multiplier):
        result += math.sqrt(i**3 + i**2 + i * n)
    return result


async def main():
    async with trio.open_nursery() as nursery:
        for n in range(os.cpu_count()):
            nursery.start_soon(trio_parallel.run_sync, cpu_intensive, n, 2)
        print("Tasks initiated")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    trio.run(main)
