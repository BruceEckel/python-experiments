# fallible.py
import asyncio
from asyncio import CancelledError
from pprint import pformat


async def fallible(i: int) -> str:
    await asyncio.sleep(0.1)
    print(f"fallible({i})")
    match i:
        # Commenting all but '_' shows success.
        case 1:
            raise ValueError(f"V[{i}]")
        case 3:
            raise TabError(f"T[{i}]")
        case 5 | 6:
            raise AttributeError(f"A[{i}]")
        case _:
            await asyncio.sleep(3)
            # Convert number to letter:
            return chr(ord("a") + i)


def display(e: Exception, msg: str = ""):
    print(f"{msg}{type(e).__name__}")
    if not isinstance(e, CancelledError):
        print(
            f"  {pformat(e.args, indent= 2, width=47)}"
        )
