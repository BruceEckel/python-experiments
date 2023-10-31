# return_my_result.py
from typing import List
from my_result import Result, Ok, Err
from my_error import MyError
from test_results import test_results

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


if __name__ == "__main__":
    test_results(results, fallible)
