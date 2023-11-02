# return_result.py
from typing import List
from my_error import MyError, err
from my_result import Result, Ok, Err


def fallible(n: int) -> Result[str, Exception] | None:
    return results[n] if n < len(results) else None


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
        print(f"{n}: ", end="")
        result = fallible(n)
        print(result)

        match result:
            case None:
                print("No result")
            case Ok(value):
                print(f"Success -> {value}")
            case Err(TabError() as e):
                err("Tab", e)
            case Err(ValueError() as e):
                err("Value", e)
            case Err(MyError() as e):
                err("My", e)
            case Err(_):
                err("Unknown", "Unknown error type")

        print("-" * 25)
