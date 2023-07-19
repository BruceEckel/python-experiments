import multiprocessing
import trio
import trio_parallel
from scenario_tester import scenario
from cpu_intensive import cpu_intensive


async def main():
    async with trio.open_nursery() as nursery:
        with scenario() as s:
            nursery.start_soon(trio_parallel.run_sync, cpu_intensive, 1, 32)
        print("Tasks initiated")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    trio.run(main)
