# https://docs.python.org/3/library/asyncio-task.html#asyncio-example-task-cancel
import asyncio


async def suspend(id: str, delay: int):
    print(f"suspend({id}, {delay})")
    try:
        await asyncio.sleep(delay)
    except asyncio.CancelledError:
        print(f"{id} cancelled")
        raise
    finally:
        print(f"{id} finally")
    print(f"{id} completed")


async def f():
    print("starting f()")
    await suspend("A", 3600)  # 1 hour
    print("ending f()")


async def main():
    task = asyncio.create_task(f())
    await asyncio.sleep(3)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): f() cancelled")


asyncio.run(main())
