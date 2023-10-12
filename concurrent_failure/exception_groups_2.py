import asyncio
from fallible import fallible
from asyncio import CancelledError
from pprint import pformat


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tasks = [
                tg.create_task(fallible(i))
                for i in range(8)
            ]
    except* ValueError as e:
        print(f"\nValue Error: '{e}'")
    except* TypeError as e:
        print(f"\nType Error: '{e}'")
    except* AttributeError as e:
        print(f"\nAttribute Error: '{e}'")
    except* CancelledError as e:
        print(f"\nCancelled Error: '{e}'")

    for t in tasks:
        try:
            print(
                f"name: {t.get_name()}, result: {t.result()}"
            )  # Or re-raises exception
        # CancelledError is a subclass of BaseException:
        except BaseException as e:
            print(
                f"\n{type(e).__name__}"
                + f"{pformat(e.args, width=47)}"
            )


asyncio.run(main())
