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
    print("Tasks complete")


asyncio.run(main())
