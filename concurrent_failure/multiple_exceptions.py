import asyncio


async def task_function(i):
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
    tasks = [task_function(i) for i in range(8)]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        match result:
            case ValueError():
                print(f"Value Error: {result}")
            case TypeError():
                print(f"Type Error: {result}")
            case AttributeError():
                print(f"Attribute Error: {result}")
            case str(letter):
                print(f"Letter: {letter}")


asyncio.run(main())
