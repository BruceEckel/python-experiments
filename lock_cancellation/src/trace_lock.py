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
