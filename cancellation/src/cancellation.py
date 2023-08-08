import asyncio


def show_tasks(msg: str):
    print(f"{msg}:")
    for task in asyncio.all_tasks():
        if task.get_coro().__name__ == "main":
            task.set_name("Main")
        running = task.get_coro().cr_running
        print(
            f"{task.get_name()}[{running}]",
            end=" ",
        )
    print("\n" + "-" * 25)


class Obj:
    def __init__(self, id: str) -> None:
        self.id = id
        print(f"Created {self}")

    def __repr__(self):
        return f"[{self.id}]"

    def __del__(self):
        print(f"~{self}")


async def task(id: str, delay: int):
    print(f"starting task({id}, {delay})")
    obj = Obj(id)
    await asyncio.sleep(delay)
    objp = Obj(id + "'")
    await asyncio.sleep(1.0)
    print(
        f"ending task({id}, {delay})"
        + f" containing {obj} & {objp}"
    )


async def main():
    def stop(taskref):
        print(
            f"!!! cancel {taskref.get_name()}"
        )
        taskref.cancel()

    async with asyncio.TaskGroup() as tg:
        tasks = [
            tg.create_task(
                task(id, n + 1), name=id
            )
            for n, id in enumerate("ABCDEF")
        ]
        show_tasks("Post-creation")
        stop(tasks[0])
        show_tasks("After stop(tasks[0])")
        await asyncio.sleep(0.5)
        stop(tasks[1])
        show_tasks("After stop(tasks[1])")
        stop(tasks[-2])
        show_tasks("After stop(tasks[-2])")


asyncio.run(main())
