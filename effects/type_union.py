# type_union.py
from my_error import MyError, err

results = [
    "eeny",
    Exception("after eeny"),
    "meeny",
    TabError("after meeny"),
    "miney",
    ValueError("after miney"),
    "moe",
    MyError("after moe"),
]


def fallible1(
    n: int,
) -> str | Exception | TabError | ValueError | MyError | None:
    return results[n] if n < len(results) else None


if __name__ == "__main__":
    for n in range(len(results) + 1):
        print(f"{n}: ", end="")
        match fallible1(n):
            case str(s):
                print(f"Success -> {s}")
            case TabError(args=(msg,)):
                err("Tab", msg)
            case ValueError(args=(msg,)):
                err("Value", msg)
            case MyError(args=(msg,)):
                err("My", msg)
            case Exception(args=(msg,)):
                err("Generic", msg)
            case None:
                print("No result")
