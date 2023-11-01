# test_results.py
from typing import (
    List,
    Callable,
    Protocol,
    TypeVar,
    Any,
    Generic,
)
from my_error import MyError, err

T = TypeVar("T", covariant=True)  # Any type
E = TypeVar("E", bound=Exception, covariant=True)  # Exceptions only


class AnyResult(Protocol, Generic[T, E]):
    value: T | E


def test_results(
    # Any and Exception widen the types:
    results_array: List[AnyResult[Any, Exception]],
    fallible_func: Callable[[int], AnyResult[Any, Exception] | None],
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
            msg = value.args[0] if value.args else "Unknown error"
            match value:
                case TabError():
                    err("Tab", msg)
                case ValueError():
                    err("Value", msg)
                case MyError():
                    err("My", msg)
        else:
            print(f"Success -> {value}")

        print("-" * 40)
