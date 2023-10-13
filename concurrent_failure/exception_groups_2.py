import asyncio
from fallible import fallible
from asyncio import CancelledError
from pprint import pformat


async def main():
    def display(id: str, e: Exception):
        print(f"\n{repr(e)}")
        print(f"[{id}]: {e.args[0]}")
        for se in e.exceptions:  # e.args[1]
            print(f"\t{repr(se)}")

    try:
        async with asyncio.TaskGroup() as tg:
            tasks = [
                tg.create_task(fallible(i))
                for i in range(8)
            ]
    except* ValueError as e:
        display("Value", e)
    except* TabError as e:
        display("Tab", e)
    except* AttributeError as e:
        display("Attribute", e)
    except* CancelledError as e:  # Never happens
        display("Cancelled", e)

    for t in tasks:
        try:  # Never runs
            print(
                f"{t.get_name()} -> {t.result()}"
            )  # Or re-raises exception
        # CancelledError is a subclass of BaseException:
        except BaseException as e:
            print(
                f"{t.get_name()} "
                + f"{type(e).__name__}{e.args}"
            )


asyncio.run(main())
