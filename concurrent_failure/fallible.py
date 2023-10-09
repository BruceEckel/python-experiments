import asyncio


async def fallible(i: int) -> str:
    await asyncio.sleep(0.1)
    print(f"{i}", end=" ")
    match i:
        # Commenting 1 & 3 shows that 5 cancels everything.
        # Commenting all but '_' shows success.
        case 1:
            raise ValueError(f"V[{i}]")
        case 3:
            raise TypeError(f"T[{i}]")
        case 5:
            raise AttributeError(f"A[{i}]")
        case _:
            await asyncio.sleep(3)
            # Convert number to letter:
            return chr(ord("a") + i)
