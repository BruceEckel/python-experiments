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
            case Err(e):
                if isinstance(e, TabError):
                    err("Tab", e.args[0])
                elif isinstance(e, ValueError):
                    err("Value", e.args[0])
                elif isinstance(e, MyError):
                    err("My", e.args[0])
                else:
                    err("Unknown", "Unknown error type")

        print("-" * 25)
