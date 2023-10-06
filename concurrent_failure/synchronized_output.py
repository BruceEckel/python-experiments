import asyncio


class BaseError(Exception):
    # When pattern matching, bind
    # to the `message` attribute:
    __match_args__ = ("message",)

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class FallibleError(BaseError):
    pass


class PanicError(BaseError):
    pass


async def fallible_task(i: int, print_lock: asyncio.Lock) -> str:
    async with print_lock:
        print(f"fallible({i})")

    if i == 5:
        raise PanicError(f"i:{i} panicked!")
    elif i % 2 == 0:
        raise FallibleError(f"Failed({i})")
    return chr(ord("a") + i)


async def main() -> None:
    print_lock = asyncio.Lock()

    tasks = [fallible_task(i, print_lock) for i in range(10)]

    async with print_lock:
        print("Tasks created")

    results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        match result:
            case str(letter):
                print(f"Letter: {letter}")
            case FallibleError(message):
                print(f"Err: {message}")
            case PanicError(message):
                print(f"Panic: {message}")
            case _:
                print(f"Unexpected: {result}")


if __name__ == "__main__":
    asyncio.run(main())
