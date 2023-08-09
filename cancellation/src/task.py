# task.py
import asyncio
from obj import Obj


async def task(id: str, delay: int):
    print(f"starting task({id}, {delay})")
    o = Obj(id)
    await asyncio.sleep(delay)
    op = Obj(id + "'")
    await asyncio.sleep(1.0)
    opp = Obj(id + "''")
    print(
        f"~task({id}, {delay})"
        + f" containing {o}, {op} & {opp}"
    )
