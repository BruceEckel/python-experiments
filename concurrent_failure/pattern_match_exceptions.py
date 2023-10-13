import asyncio
from fallible import fallible


async def main():
    tasks = [fallible(i) for i in range(8)]
    results = await asyncio.gather(
        *tasks, return_exceptions=True
    )

    for result in results:
        match result:
            case ValueError():
                print(f"Value Error: {result}")
            case TabError():
                print(f"Tab Error: {result}")
            case AttributeError():
                print(f"Attribute Error: {result}")
            case str(letter):
                print(f"Letter: {letter}")
            case _:
                print(f"Unexpected: {result}")


asyncio.run(main())
