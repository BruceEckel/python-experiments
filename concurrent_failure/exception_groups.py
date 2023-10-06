import asyncio


async def fallible(i: int, print_lock: asyncio.Lock) -> str:
    async with print_lock:
        print(f"fallible({i})")

    match i:
        case 5:
            raise ValueError(f"i = {i}")
        case _ if i % 2 == 0:
            raise TypeError(f"i = {i}")
        case _ if i % 3 == 0:
            raise AttributeError(f"i = {i}")
        case _:
            # Convert number to letter:
            return chr(ord("a") + i)


async def main() -> None:
    print_lock = asyncio.Lock()
    tasks = []
    try:
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(fallible(i, print_lock)) for i in range(10)]
    except ExceptionGroup as e:
        for exc in e.exceptions:
            match exc:
                case ValueError() as e:
                    print(f"Value Error: '{e}'")
                case TypeError() as e:
                    print(f"Type Error: '{e}'")
                case AttributeError() as e:
                    print(f"Attribute Error: '{e}'")

    # Does this produce the same output as above?
    # except* ValueError as e:
    #     print(f"Value Error: '{e}'")
    # except* TypeError as e:
    #     print(f"Type Error: '{e}'")
    # except* AttributeError as e:
    #     print(f"Attribute Error: '{e}'")

    # Don't need this, as Structured concurrency
    # Ensures all the tasks are finished by this point:
    # async with print_lock:
    print("---> Tasks created")
    for t in tasks:
        print(f"{t.get_name()}", end=", ")
        try:
            print(f"result = {t.result()}")
        except Exception as e:
            print(f"{type(e).__name__}[{e}]")


if __name__ == "__main__":
    asyncio.run(main())
