import asyncio
from fallible import fallible
from asyncio import CancelledError
from pprint import pformat


async def main():
    def display(id: str, e: Exception):
        print(f"\ntype(e): {type(e).__name__}")
        print(f"{id}: '{e}'\n\t'{e.exceptions}'")

    try:
        async with asyncio.TaskGroup() as tg:
            tasks = [
                tg.create_task(fallible(i))
                for i in range(8)
            ]
    except* ValueError as e:
        display("Value", e)
    except* TypeError as e:
        display("Type", e)
    except* AttributeError as e:
        display("Attribute", e)
    except* CancelledError as e:
        display("Cancelled", e)

    for t in tasks:
        try:
            print(
                f"name: {t.get_name()}, result: {t.result()}"
            )  # Or re-raises exception
        # CancelledError is a subclass of BaseException:
        except BaseException as e:
            print(
                f"{t.get_name()} "
                + f"{type(e).__name__}"
                + f"{pformat(e.args, width=47)}"
            )


asyncio.run(main())
