import asyncio
from fallible import fallible
from pprint import pformat


async def main() -> None:
    tasks = []
    try:
        # raise RuntimeError("Not in TaskGroup")
        async with asyncio.TaskGroup() as tg:
            # raise RuntimeError("In TaskGroup")
            tasks = [
                tg.create_task(
                    fallible(i),
                    name=f"Task {i}",
                )
                for i in range(8)
            ]
        print("No exceptions")
    except ExceptionGroup as e:
        print(
            f"\n{type(e).__name__}"
            + f"{pformat(e.args, width=47)}"
        )
    except Exception as e:
        print(f"Not an ExceptionGroup: {e}")
    finally:
        print("- Tasks Complete -")

    for t in tasks:
        cancelled = t.cancelled()
        c = "Not " if not cancelled else ""
        e = "\n" if cancelled else ": "
        print(f"{t.get_name()}: {c}Cancelled", end=e)
        if not cancelled:
            try:
                # If it failed, t.result() rethrows
                print(f"{t.result()}")
            except Exception as e:
                print(f"{type(e).__name__}({e})")


if __name__ == "__main__":
    asyncio.run(main())
