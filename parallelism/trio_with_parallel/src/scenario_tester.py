from contextlib import contextmanager
from dataclasses import dataclass, field
import trio
import os
from pprint import pformat


@dataclass
class Scenario:
    multiplier: int
    tasks: int
    args1: range = field(init=False)
    args2: list[int] = field(init=False)
    results: list[float] = field(default_factory=list)

    def __post_init__(self):
        self.args1 = range(self.tasks)
        self.args2 = [self.multiplier] * self.tasks


@contextmanager
def scenario():
    multiplier = 1  # Increase for longer computations
    logical_processors = os.cpu_count()
    print(f"{logical_processors = }")
    tasks = (logical_processors - 0) * 1  # Try different numbers
    print(f"{tasks = }")
    start = trio.current_time()
    scenario = Scenario(multiplier, tasks)
    try:
        yield scenario
    finally:
        elapsed = trio.current_time() - start
        # print(
        #     f"""{pformat(list(scenario.results))}
        #       Elapsed time: {elapsed:.2f}s"""
        # )
