import asyncio


async def fallible(i):
    # print(f"fallible({i})")
    match i:
        case 5:
            raise ValueError(f"i: {i}")
        case _ if i % 2 == 0:
            raise TypeError(f"i: {i}")
        case _ if i % 3 == 0:
            raise AttributeError(f"i: {i}")
        case _:
            # Convert number to letter:
            return chr(ord("a") + i)


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(fallible(i)) for i in range(8)]
    except* ValueError as e:
        print(f"Value Error: '{e}'")
    except* TypeError as e:
        print(f"Type Error: '{e}'")
    except* AttributeError as e:
        print(f"Attribute Error: '{e}'")

    for t in tasks:
        try:
            print(
                f"name: {t.get_name()}, result: {t.result()}"
            )  # Or re-raises exception
        except Exception as e:
            print(f"name: {t.get_name()}, Exception {e}")
        # if t.exception:
        #     print(f"{str(t.exception())}")
        #     # print(f"{dir(t)}")
        # if t.result:
        #     print(f"{str(t.result())}")


asyncio.run(main())
