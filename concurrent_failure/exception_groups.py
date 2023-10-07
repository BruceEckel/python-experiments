import asyncio


async def fallible(i: int) -> str:
    print(f"{i}", end=" ")
    match i:
        case 2:
            raise ValueError(f"VE[{i}]")
        case 5:
            raise TypeError(f"TE[{i}]")
        case 7:
            raise AttributeError(f"AE[{i}]")
        case _:
            await asyncio.sleep(1)
            # Convert number to letter:
            return chr(ord("a") + i)


async def main() -> None:
    try:
        async with asyncio.TaskGroup() as tg:
            # tasks = []
            # raise RuntimeError("Nothing works!")
            tasks = [
                tg.create_task(
                    fallible(i),
                    name=f"Task {i}",
                )
                for i in range(10)
            ]
        print("Tasks Complete, no exceptions")
    except Exception as e:
        print(f"\n->\n{e = }\n{e.args = }")
        if isinstance(e, ExceptionGroup):
            for exc in e.exceptions:
                print(
                    f"\t{type(exc).__name__}{exc.args}"
                )

    for t in tasks:
        print(f"{t.get_name()}: {t.cancelled() = }")
        if not t.cancelled():
            try:
                print(f"{t.result() = }")
            except Exception as e:
                print(f"{type(e).__name__}({e})")


if __name__ == "__main__":
    asyncio.run(main())
