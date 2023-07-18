# Adapted from https://trio.readthedocs.io/en/stable/tutorial.html
# tasks_intro.py
import trio


async def child(id: str):
    print(f"{id}: started! sleeping now...")
    await trio.sleep(4)
    print(f"{id}: exiting!")


def char_range(c1, c2):
    for c in range(ord(c1), ord(c2) + 1):
        yield chr(c)


async def parent():
    print("parent: started!")
    async with trio.open_nursery() as tasks:
        for c in char_range("A", "F"):
            print(f"parent: spawning child({c})")
            tasks.start_soon(child, c)
        print("parent: waiting for children to finish...")
        # Exit the nursery block here
    print("parent: all done!")


trio.run(parent)
