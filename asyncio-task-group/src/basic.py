# basic.py
import asyncio


async def sleeper(id: str, secs: int):
    print(f"{id} sleeping {secs}s")
    await asyncio.sleep(secs)
    print(f"{id} waking {secs}s")


async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(sleeper("a", 5))
        tg.create_task(sleeper("b", 3))
        tg.create_task(sleeper("c", 1))
        for task in asyncio.all_tasks():
            coro = task.get_coro()
            print(
                f"{task.get_name()}: "
                + f"{coro.__name__}, "
                + f"{coro.cr_running}"
            )
    print("Tasks complete")


asyncio.run(main())
