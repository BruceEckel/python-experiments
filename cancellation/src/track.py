# track.py
import asyncio


def track(
    stop_task: asyncio.Task | None = None,
    msg: str = "",
) -> None:
    def display(s: str):
        print(s, end=": ")

    if msg:
        display("(" + msg + ")")
    if stop_task:
        name = stop_task.get_name()
        display(f"! {name}.cancel()")
        stop_task.cancel()
    for t in asyncio.all_tasks():
        print(f"{t.get_name()}", end=", ")
    print()
