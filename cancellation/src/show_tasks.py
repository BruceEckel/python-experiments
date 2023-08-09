# show_tasks.py
import asyncio


def show_tasks(msg: str) -> None:
    print(f"{msg}:", end=" ")
    for task in asyncio.all_tasks():
        print(f"{task.get_name()}", end=", ")
    print()
