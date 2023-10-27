# type_union.py
from dataclasses import dataclass


@dataclass
class Result:
    string: str | None = None
    err: Exception | None = None


def fallible() -> Result:
    results = [
        Result("eeny"),
        Result(err=Exception("after eeny")),
        Result("meeny"),
        Result(err=Exception("after meeny")),
        Result("miney"),
        Result(err=Exception("after miney")),
        Result("moe"),
        Result(err=Exception("after moe")),
    ]

    # Create a 'static' variable for this function:
    if not hasattr(fallible, "index"):
        fallible.index = 0

    result = results[
        fallible.index % len(results)
    ]
    fallible.index += 1

    return result


if __name__ == "__main__":
    for n in range(11):
        result = fallible()
        match result:
            case Result(string=str(s)):
                print(f"{n}: String -> {s}")
            case Result(err=exc) if isinstance(
                exc, Exception
            ):
                print(f"{n}: Error -> {exc}")
