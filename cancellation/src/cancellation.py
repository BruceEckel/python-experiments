# cancellation.py
import asyncio
from task import task
from track import track


async def main():
    async with asyncio.TaskGroup() as tg:
        tasks = {
            id: tg.create_task(
                task(id, n + 1), name=id
            )
            for n, id in enumerate("ABCDEFG")
        }
        track(stop_task=tasks["A"])
        await asyncio.sleep(0.1)
        track(msg="After sleep")
        track(stop_task=tasks["B"])
        await asyncio.sleep(0.1)
        track(msg="After sleep")
        track(stop_task=tasks["F"])
        await asyncio.sleep(0.1)
        track(msg="After sleep")
        track(stop_task=tasks["D"])


asyncio.run(main())
