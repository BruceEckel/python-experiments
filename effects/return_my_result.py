# return_my_result.py
from typing import List, Callable
from my_result import Result, Ok, Err
from my_error import MyError, err

results: List[Result[str, Exception]] = [
    Ok("eeny"),
    Err(TabError("after eeny")),
    Ok("meeny"),
    Err(ValueError("after meeny")),
    Ok("miney"),
    Err(MyError("after miney")),
]


def fallible(n: int) -> Result[str, Exception] | None:
    return results[n] if n < len(results) else None


def test_results(
    results_array: List[Result[str, Exception]],
    fallible_func: Callable[[int], Result[str, Exception] | None],
):
    for n in range(len(results_array) + 1):
        print(f"{n}: ", end="")
        result = fallible_func(n)
        print(result)
        if result is None:
            print("No result")
            continue
        match result:
            case Ok(value):
                print(f"{n}: Success -> {value}")
            case Err(exc):
                match exc:
                    case TabError(args=(msg,)):
                        err("Tab", msg)
                    case ValueError(args=(msg,)):
                        err("Value", msg)
                    case MyError(args=(msg,)):
                        err("My", msg)

        print("-" * 40)


if __name__ == "__main__":
    test_results(results, fallible)
