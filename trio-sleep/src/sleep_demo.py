import trio


async def sleeper(id: str) -> None:
    print(f"{id} started and going to sleep")
    await trio.sleep(1)
    print(f"{id} awoken, exiting")


async def main():
    async with trio.open_nursery() as tasks:
        print("main starting a")
        tasks.start_soon(sleeper, "a")

        print("main starting b")
        tasks.start_soon(sleeper, "b")

        print("main: waiting for children to finish...")

    print("main exiting")


if __name__ == "__main__":
    trio.run(main)
