# task.py
import asyncio
from obj import Obj


async def task(id: str, delay: int):
    o = Obj(id)
    print(f"starting task({id}, {delay})")
    await asyncio.sleep(delay)
    op = Obj(id + "'")
    await asyncio.sleep(1.0)
    opp = Obj(id + "''")
    print(
        f"ending task({id}, {delay})"
        + f" containing {o}, {op} & {opp}"
    )
