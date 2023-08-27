# lock_cancellation.py
import asyncio
from trace_lock import TraceLock


async def task_with_lock(lock: TraceLock):
    async with lock:
        await asyncio.sleep(5)
        print("Sleep complete.")


async def main():
    lock = TraceLock()
    task = asyncio.create_task(task_with_lock(lock))
    await asyncio.sleep(2)
    print("cancelling task")
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Task cancelled.")


asyncio.run(main())
