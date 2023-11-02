# type_union.py
from typing import List
from my_error import MyError


def fallible(n: int) -> str | TabError | ValueError | MyError | None:
    return results[n] if n in range(len(results)) else None


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
                print(f"{n}: Tab Error ->", e)
            case ValueError() as e:
                print(f"{n}: Value Error ->", e)
            case MyError() as e:
                print(f"{n}: My Error ->", e)
            case None:
                print(f"{n}: No result")
