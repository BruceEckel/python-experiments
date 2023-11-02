# return_result.py
from typing import List
from my_error import MyError
from my_result import Result, Ok, Err


def fallible(n: int) -> Result[str, Exception] | None:
    return results[n] if n in range(len(results)) else None


results: List[Result[str, Exception]] = [
    Ok("eeny"),
    Err(TabError("after eeny")),
    Ok("meeny"),
    Err(ValueError("after meeny")),
    Ok("miney"),
    Err(MyError("after miney")),
]

if __name__ == "__main__":
    for n in range(len(results) + 1):
        result = fallible(n)

        match result:
            case None:
                print(f"{n}: No result")
            case Ok(value):
                print(f"{n}: Success -> {value}")
            case Err(TabError() as e):
                print(f"{n}: Tab Error ->", e)
            case Err(ValueError() as e):
                print(f"{n}: Value Error ->", e)
            case Err(MyError() as e):
                print(f"{n}: My Error ->", e)
            case Err(Exception() as e):
                print(f"{n}: Unknown Error ->", e)

        print(f"{result}\n" + "-" * 25)
