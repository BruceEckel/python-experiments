# exceptions.py
import asyncio
from task import task


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            task_args = {id: None for id in "ABCDEFG"}
            task_args["B"] = asyncio.CancelledError
            task_args["D"] = RuntimeError
            task_args["F"] = ZeroDivisionError
            for id in task_args:
                tg.create_task(task(id, task_args[id]), name=id)
    # except* asyncio.CancelledError as e:
    #     print(f"Exceptions: {e.exceptions}")
    except* RuntimeError as e:
        print(f"Exceptions: {e.exceptions}")
    except* ZeroDivisionError as e:
        print(f"Exceptions: {e.exceptions}")


asyncio.run(main())
