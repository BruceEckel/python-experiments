import asyncio


class TraceLock(asyncio.Lock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Lock created.")

    async def __aenter__(self):
        print("Lock acquired.")
        await super().__aenter__()

    async def __aexit__(self, exc_type, exc_value, traceback):
        await super().__aexit__(exc_type, exc_value, traceback)
        print("Lock released.")

    def __del__(self):
        print("~Lock")


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
