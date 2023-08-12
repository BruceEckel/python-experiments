# task.py
import asyncio
from obj import Obj


async def task(id: str, exception_type=None):
    print(f"starting task({id}, {exception_type})")
    o = Obj(id)
    await asyncio.sleep(0.1)
    op = Obj(id + "'")
    if exception_type:
        print(f"{id} Raising Exception {exception_type}")
        raise exception_type(id)
    await asyncio.sleep(0.1)
    opp = Obj(id + "''")
    print(f"~task({id}, {exception_type})" + f" containing {o}, {op} & {opp}")
    return id
