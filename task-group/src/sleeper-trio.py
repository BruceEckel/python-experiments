# sleeper-trio.py
import trio


async def sleeper(id: str, secs: int):
    print(f"{id} sleeping {secs}s")
    await trio.sleep(secs)
    print(f"{id} waking {secs}s")


async def main():
    async with trio.open_nursery() as nursery:
        nursery.start_soon(sleeper, "a", 5)
        nursery.start_soon(sleeper, "b", 3)
        nursery.start_soon(sleeper, "c", 1)
        for task in nursery.child_tasks:
            coro = task.coro
            print(
                f"{task.name}: "
                + f"{coro.__name__}, "
                + f"{coro.cr_running}"
            )

    print("Tasks complete")


if __name__ == "__main__":
    trio.run(main)
