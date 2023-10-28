# convert_exceptions_2.py
from result import Result, Ok, Err
from my_error import MyError, err


results = [
    Ok("eeny"),
    Err(Exception("after eeny")),
    Ok("meeny"),
    Err(TabError("after meeny")),
    Ok("miney"),
    Err(ValueError("after miney")),
    Ok("moe"),
    Err(MyError("after moe")),
]


def fallible2(n: int) -> Result:
    return results[n] if n < len(results) else None


if __name__ == "__main__":
    for n in range(len(results) + 1):
        print(f"{n}: ", end="")
        result = fallible2(n)
        print(result)
        match result:
            case Ok(value=s):
                print(f"{n}: Success -> {s}")
            case None:
                print("No result")
            case Err(value=exc):
                match exc:
                    case TabError(args=(msg,)):
                        err("Tab", msg)
                    case ValueError(args=(msg,)):
                        err("Value", msg)
                    case MyError(args=(msg,)):
                        err("My", msg)
                    case Exception(args=(msg,)):
                        err("Generic", msg)
        print("-" * 40)
