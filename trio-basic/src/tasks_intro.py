# Adapted from https://trio.readthedocs.io/en/stable/tutorial.html
# tasks_intro.py
import trio


async def child(id: str):
    print(f"{id}: started! sleeping now...")
    await trio.sleep(4)
    print(f"{id}: exiting!")


async def parent():
    print("parent: started!")
    async with trio.open_nursery() as tasks:
        for c in "ABCDEF":
            print(f"parent: spawning child({c})")
            tasks.start_soon(child, c)
        print("parent: waiting for children to finish...")
        # Exit the nursery block here
    print("parent: all done!")


trio.run(parent)
