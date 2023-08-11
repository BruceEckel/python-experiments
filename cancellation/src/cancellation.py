# cancellation.py
import asyncio
from task import task
from track import track


async def main():
    async with asyncio.TaskGroup() as tg:
        tasks = [
            tg.create_task(
                task(id, n + 1), name=id
            )
            for n, id in enumerate("ABCDEFG")
        ]
        track(stop_task=tasks[0])
        await asyncio.sleep(0.1)
        track(msg="After sleep")
        track(stop_task=tasks[1])
        await asyncio.sleep(0.1)
        track(msg="After sleep")
        track(stop_task=tasks[-1])
        await asyncio.sleep(0.1)
        track(msg="After sleep")
        track(stop_task=tasks[3])


asyncio.run(main())
