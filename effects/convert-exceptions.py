# convert-exceptions.py
from typing import Iterator
from dataclasses import dataclass


@dataclass  # Or enum? which is really an 'OR'
class Result:
    string: str | None = None
    err: Exception | None = None


def fallible() -> Iterator[Result]:
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
    while True:
        for result in results:
            yield result


if __name__ == "__main__":
    for n, result in zip(
        range(11), fallible()
    ):
        match result:
            case Result(string=str(s)):
                print(f"{n}: String -> {s}")
            case Result(err=exc) if isinstance(
                exc, Exception
            ):
                print(f"{n}: Error -> {exc}")
