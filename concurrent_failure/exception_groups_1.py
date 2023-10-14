# exception_groups_1.py
import asyncio
from fallible import fallible, display


async def main() -> None:
    tasks = []
    try:
        # raise RuntimeError("Outside TaskGroup")
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
    except Exception as e:
        display(e)
    finally:
        print("- Tasks Complete -")

    for t in tasks:
        print(
            f"{t.get_name()}: "
            + f"cancelled[{t.cancelled()}]"
        )
        if not t.cancelled():
            try:
                # If it failed, t.result() raises
                print(f"\t{t.result()}")
            except Exception as e:
                display(e)


if __name__ == "__main__":
    asyncio.run(main())
