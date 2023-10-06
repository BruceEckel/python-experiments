import asyncio


async def fallible(i: int, print_lock: asyncio.Lock) -> str:
    async with print_lock:
        print(f"fallible({i})")

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


async def main() -> None:
    print_lock = asyncio.Lock()

    tasks = [fallible(i, print_lock) for i in range(10)]

    async with print_lock:
        print("Tasks created")

    results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        match result:
            case str(letter):
                print(f"Letter: {letter}")
            case ValueError():
                print(f"Value Error: {result.args[0]}")
            case TypeError():
                print(f"Type Error: {result.args[0]}")
            case AttributeError():
                print(f"Attribute Error: {result.args[0]}")
            case _:
                print(f"Unexpected: {result}")


if __name__ == "__main__":
    asyncio.run(main())
