# return_result.py
from result import Result, Ok, Err
from my_error import MyError, err


results = [
    Ok("eeny"),
    Err(TabError("after eeny")),
    Ok("meeny"),
    Err(ValueError("after meeny")),
    Ok("miney"),
    Err(MyError("after miney")),
]


def fallible(n: int) -> Result | None:
    return results[n] if n < len(results) else None


if __name__ == "__main__":
    for n in range(len(results) + 1):
        print(f"{n}: ", end="")
        result = fallible(n)
        print(result)
        if result is None:
            print("No result")
            continue
        match result:
            case Ok(value=s):
                print(f"{n}: Success -> {s}")
            case Err(value=exc):
                match exc:
                    case TabError(args=(msg,)):
                        err("Tab", msg)
                    case ValueError(args=(msg,)):
                        err("Value", msg)
                    case MyError(args=(msg,)):
                        err("My", msg)

        print("-" * 40)
