import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from concurrent.futures import ProcessPoolExecutor
import math
import time
import os


def cpu_intensive(n: int, multiplier: int) -> float:
    result: float = 0
    for i in range(1_000_000 * multiplier):
        result += math.sqrt(i**3 + i**2 + i * n)
    return result


def use_all_cores():
    multiplier = 1  # Increase for longer computations
    logical_processors = os.cpu_count()
    print(f"{logical_processors = }")
    tasks = (logical_processors - 0) * 1  # Try different numbers
    print(f"{tasks = }")
    start = time.monotonic()

    with ProcessPoolExecutor() as executor:
        results = executor.map(cpu_intensive, range(tasks), [multiplier] * tasks)

    return f"{list(results)}\nElapsed time: {time.monotonic() - start:.2f}s"


def greeting(name):
    if name:
        return f"Hello, {name}"
    else:
        return "Hello, stranger"


class HelloWorld(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label("Your name: ", style=Pack(padding=(0, 5)))
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            "Say Hello!", on_press=self.say_hello, style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        self.main_window.info_dialog(
            # greeting(self.name_input.value),
            # "Hi there!",
            "Output",
            use_all_cores(),
        )


def main():
    return HelloWorld()
