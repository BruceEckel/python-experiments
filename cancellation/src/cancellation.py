# cancellation.py
import asyncio
from obj import Obj
from task import task


def track(
    stop_task: asyncio.Task | None = None,
    msg: str = "",
) -> None:
    def display(s: str):
        print(s, end=": ")

    if msg:
        display("(" + msg + ")")
    if stop_task:
        name = stop_task.get_name()
        display(f"! {name}.cancel()")
        stop_task.cancel()
    for t in asyncio.all_tasks():
        print(f"{t.get_name()}", end=", ")
    print()


async def main():
    async with asyncio.TaskGroup() as tg:
        tasks = [
            tg.create_task(
                task(id, n + 1), name=id
            )
            for n, id in enumerate("ABCDEF")
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
