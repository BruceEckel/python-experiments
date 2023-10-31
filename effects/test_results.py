# test_results.py
from typing import List, Callable, Protocol, TypeVar, Optional
from my_error import MyError, err

T = TypeVar("T")  # Any type
E = TypeVar("E", bound=Exception)  # Only an Exception


class AnyResult(Protocol):
    value: T | E


def test_results(
    results_array: List[AnyResult],
    fallible_func: Callable[[int], Optional[AnyResult]],
):
    for n in range(len(results_array) + 1):
        print(f"{n}: ", end="")
        result = fallible_func(n)
        print(result)
        if result is None:
            print("No result")
            continue

        value = result.value  # Use duck typing to access .value
        if isinstance(value, Exception):
            match value:
                case TabError(args=(msg,)):
                    err("Tab", msg)
                case ValueError(args=(msg,)):
                    err("Value", msg)
                case MyError(args=(msg,)):
                    err("My", msg)
        else:
            print(f"Success -> {value}")

        print("-" * 40)
