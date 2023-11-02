# type_union.py
from typing import List
from my_error import MyError, err


def fallible(n: int) -> str | TabError | ValueError | MyError | None:
    return results[n] if 0 <= n < len(results) else None


results: List[str | TabError | ValueError | MyError] = [
    "eeny",
    TabError("after eeny"),
    "meeny",
    ValueError("after meeny"),
    "miney",
    MyError("after miney"),
]


if __name__ == "__main__":
    for n in range(len(results) + 1):
        match fallible(n):
            case str(s):
                print(f"{n}: Success -> {s}")
            case TabError() as e:
                err(f"{n}: Tab", e)
            case ValueError() as e:
                err(f"{n}: Value", e)
            case MyError() as e:
                err(f"{n}: My", e)
            case None:
                print(f"{n}: No result")
