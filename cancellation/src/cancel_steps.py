import asyncio
from obj import Obj


async def suspend(id: str, delay: int):
    print(f"suspend({id}, {delay})")
    o = Obj(id)
    try:
        await asyncio.sleep(delay)
    except asyncio.CancelledError as e:
        print(f"CancelledError: {e}")
        print(f"{id} cancelled")
        raise  # Don't swallow it
    finally:
        print(f"{id} finally")
    print(f"{id} completed with {o}")


async def f():
    print("starting f()")
    await suspend("A", 8)
    print("ending f()")


async def main():
    task = asyncio.create_task(f())
    await asyncio.sleep(2)
    task.cancel("from main()")
    try:
        await task
    except asyncio.CancelledError:
        print("main(): f() cancelled")


asyncio.run(main())
