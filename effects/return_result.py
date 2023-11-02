# return_result.py
from typing import List
from my_error import MyError, err
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
                err(f"{n}: Tab", e)
            case Err(ValueError() as e):
                err(f"{n}: Value", e)
            case Err(MyError() as e):
                err(f"{n}: My", e)
            case Err(Exception() as e):
                err(f"{n}: Unknown", e)

        print(f"{result}\n" + "-" * 25)
