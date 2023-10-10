# From ChatGPT; doesn't really show collisions
import asyncio


async def print_task(name, delay):
    await asyncio.sleep(delay)
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} completed")


async def main():
    tasks = [
        print_task(f"T{i}", i * 0.1)
        for i in range(5)
    ]
    await asyncio.gather(*tasks)


asyncio.run(main())
