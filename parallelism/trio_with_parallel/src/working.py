import multiprocessing
import trio
import trio_parallel
from scenario_tester import scenario
import math


async def cpu_intensive(n: int) -> float:
    result: float = 0
    for i in range(10_000_000):
        result += math.sqrt(i**3 + i**2 + i * n)
    return result


async def main():
    async with trio.open_nursery() as nursery:
        with scenario() as s:
            for i in range(32):
                nursery.start_soon(cpu_intensive, i)
        print("Tasks initiated")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    trio.run(main)
