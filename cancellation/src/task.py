# task.py
import asyncio
from obj import Obj


async def task(id: str, delay: int):
    print(f"starting task({id}, {delay})")
    o = Obj(id)
    if id == "G":
        print("Early return from G")
        return
    await asyncio.sleep(delay)
    op = Obj(id + "'")
    await asyncio.sleep(1.0)
    if id == "C":
        print("Self-cancelling C")
        raise asyncio.CancelledError
    opp = Obj(id + "''")
    print(
        f"~task({id}, {delay})"
        + f" containing {o}, {op} & {opp}"
    )
