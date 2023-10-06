import asyncio
from typing import List, Any


class BaseError(Exception):
    message: str

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)

    # When pattern matching, bind
    # to the `message` attribute:
    __match_args__ = ("message",)


class FallibleError(BaseError):
    pass


class PanicError(BaseError):
    pass


async def fallible(
    i: int, print_lock: asyncio.Lock
) -> str | None:  # It can return str or raise an error
    async with print_lock:
        print(f"fallible({i})")

    if i == 5:
        raise PanicError(f"i:{i} panicked!")
    elif i % 2 == 0:
        raise FallibleError(f"Failed({i})")
    else:
        # Convert number to char:
        return chr(ord("a") + i)


async def main() -> None:
    print_lock = asyncio.Lock()

    tasks: List[asyncio.Task[str | None]] = [
        asyncio.create_task(fallible(i, print_lock)) for i in range(10)
    ]

    async with print_lock:
        print("Tasks created")

    results: List[str | BaseError | Any] = await asyncio.gather(
        *tasks, return_exceptions=True
    )  # Can be string, one of the exceptions, or any other unexpected result

    for result in results:
        match result:
            case str(letter):
                print(f"Letter: {letter}")
            case FallibleError(error_msg):
                print(f"Err: {error_msg}")
            case PanicError(panic_msg):
                print(f"Panic: {panic_msg}")
            case _:
                print(f"Unexpected: {result}")


if __name__ == "__main__":
    asyncio.run(main())
