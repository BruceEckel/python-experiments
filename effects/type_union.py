# type_union.py
from typing import List
from my_error import MyError, err

results: List[str | TabError | ValueError | MyError] = [
    "eeny",
    TabError("after eeny"),
    "meeny",
    ValueError("after meeny"),
    "miney",
    MyError("after miney"),
]


def fallible1(
    n: int,
) -> str | TabError | ValueError | MyError | None:
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
            case None:
                print("No result")
