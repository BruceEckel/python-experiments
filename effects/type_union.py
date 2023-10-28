# type_union.py


class MyError(Exception):
    pass


def fallible(
    i: int,
) -> str | TabError | ValueError | MyError | Exception | None:
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

    return results[i] if len(results) > i else None


if __name__ == "__main__":

    def err(type: str, msg: str):
        print(f"{type} Error -> {msg}")

    for n in range(9):
        print(f"{n}: ", end="")
        match fallible(n):
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
