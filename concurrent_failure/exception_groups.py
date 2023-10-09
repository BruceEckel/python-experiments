import asyncio
from fallible import fallible


async def main() -> None:
    try:
        async with asyncio.TaskGroup() as tg:
            # Test a non-ExceptionGroup:
            # tasks = []
            # raise RuntimeError("Nothing works!")
            tasks = [
                tg.create_task(
                    fallible(i),
                    name=f"Task {i}",
                )
                for i in range(8)
            ]
        # Any exceptions --> can't get here:
        print("Tasks Complete, no exceptions")
    except Exception as e:
        print(f"\n->\n{e = }\n{e.args = }")
        if isinstance(e, ExceptionGroup):
            for exc in e.exceptions:
                print(
                    f"\t{type(exc).__name__}{exc.args}"
                )

    for t in tasks:
        cancelled = t.cancelled()
        c = "Not " if not cancelled else ""
        e = "\n" if cancelled else ": "
        print(f"{t.get_name()}: {c}Cancelled", end=e)
        if not cancelled:
            try:
                # If it failed, result() rethrows
                print(f"{t.result() = }")
            except Exception as e:
                print(f"{type(e).__name__}({e})")


if __name__ == "__main__":
    asyncio.run(main())
