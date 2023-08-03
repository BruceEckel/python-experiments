# sleeper-trio.py
import trio


def tasks():
    ct = trio.lowlevel.current_task()
    return ct.parent_nursery.child_tasks


def show_tasks(msg: str):
    for t in tasks():
        print(
            f"{t.name}[{t.coro.cr_running}]",
            end=" ",
        )
    print(f"\n{msg}\n" + "-" * 25)


async def nap(id: str, secs: int):
    show_tasks(f"{id} napping {secs}s")
    await trio.sleep(secs)
    show_tasks(f"{id} woken after {secs}s")


async def main():
    for task in tasks():
        if task.coro.__name__ == "main":
            task.name = "Main"
    async with trio.open_nursery() as tg:
        tg.start_soon(nap, "A", 5, name="A")
        tg.start_soon(nap, "B", 3, name="B")
        tg.start_soon(nap, "C", 1, name="C")
        show_tasks("tasks created")
    show_tasks("Tasks complete")


if __name__ == "__main__":
    trio.run(main)
