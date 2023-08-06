import asyncio


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
    print(f"ending task({id}, {delay}) containing {obj} & {objp}")


async def main():
    def stop(taskref):
        print(f"!!! cancelling {taskref.get_name()}")
        taskref.cancel()

    async with asyncio.TaskGroup() as tg:
        tasks = [
            tg.create_task(task(id, n + 1), name=id) for n, id in enumerate("ABCDEF")
        ]
        stop(tasks[0])
        await asyncio.sleep(0.5)
        stop(tasks[1])
        stop(tasks[-2])


asyncio.run(main())
