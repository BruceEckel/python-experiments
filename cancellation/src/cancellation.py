# cancellation.py
import asyncio
from show_tasks import show_tasks
from obj import Obj
from task import task


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
