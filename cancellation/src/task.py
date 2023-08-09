import asyncio
from obj import Obj


async def task(id: str, delay: int):
    print(f"starting task({id}, {delay})")
    obj = Obj(id)
    await asyncio.sleep(delay)
    objp = Obj(id + "'")
    await asyncio.sleep(1.0)
    print(
        f"ending task({id}, {delay})"
        + f" containing {obj} & {objp}"
    )
