# exception_groups_2.py
import asyncio
from fallible import fallible, display
from asyncio import CancelledError


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tasks = [
                tg.create_task(fallible(i))
                for i in range(8)
            ]
    except* ValueError as e:
        display(e)
    except* TabError as e:
        display(e)
    except* AttributeError as e:
        display(e)
    except* CancelledError as e:  # Never happens
        display(e)
    finally:
        print("- Tasks Complete -")

    for t in tasks:
        # There's no t.result(); raises exception:
        try:
            print(f"{t.get_name()} -> {t.result()}")
        except Exception as e:
            display(e, "Exception: ")
        # CancelledError is a subclass of BaseException:
        except BaseException as e:
            display(e, "BaseException: ")


asyncio.run(main())
