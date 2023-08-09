# show_tasks.py
import asyncio
import typing


@typing.no_type_check  # Mypy gets confused
def show_tasks(msg: str) -> None:
    print(f"{msg}:")
    for task in asyncio.all_tasks():
        if task.get_coro().__name__ == "main":
            task.set_name("Main")
        running = task.get_coro().cr_running
        print(
            f"{task.get_name()}[{running}]",
            end=" ",
        )
    print("\n" + "-" * 25)
