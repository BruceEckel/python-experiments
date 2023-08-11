# task.py
import asyncio
from obj import Obj


async def task(id: str, delay: int):
    print(f"starting task({id}, {delay})")
    o = Obj(id)
    if id == "G":
        return
    await asyncio.sleep(delay)
    op = Obj(id + "'")
    await asyncio.sleep(1.0)
    # How a task cancels itself:
    if id == "C":
        raise asyncio.CancelledError
    opp = Obj(id + "''")
    print(
        f"~task({id}, {delay})"
        + f" containing {o}, {op} & {opp}"
    )
