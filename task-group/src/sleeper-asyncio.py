# sleeper-asyncio.py
import asyncio


def show_tasks(msg: str):
    for task in asyncio.all_tasks():
        running = task.get_coro().cr_running
        print(
            f"{task.get_name()}[{running}]",
            end=" ",
        )
    print(f"\n{msg}\n" + "-" * 25)


async def nap(id: str, secs: int):
    show_tasks(f"{id} napping {secs}s")
    await asyncio.sleep(secs)
    show_tasks(f"{id} woken after {secs}s")


async def main():
    for task in asyncio.all_tasks():
        if task.get_coro().__name__ == "main":
            task.set_name("Main")
    async with asyncio.TaskGroup() as tg:
        tg.create_task(nap("A", 5), name="A")
        tg.create_task(nap("B", 3), name="B")
        tg.create_task(nap("C", 1), name="C")
        show_tasks("tasks created")
    show_tasks("Tasks complete")


asyncio.run(main())
