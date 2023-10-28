# string_convert_exceptions.py
from string_result import StringResult, Ok, Err


def fallible() -> StringResult:
    # Holds its value between function calls:
    if not hasattr(fallible, "index"):
        fallible.index = 0

    results = [
        Ok("eeny"),
        Err(err=Exception("after eeny")),
        Ok("meeny"),
        Err(err=Exception("after meeny")),
        Ok("miney"),
        Err(err=Exception("after miney")),
        Ok("moe"),
        Err(err=Exception("after moe")),
    ]

    result = results[fallible.index % len(results)]
    fallible.index += 1

    return result


if __name__ == "__main__":
    for n in range(11):
        result = fallible()
        match result:
            case StringResult(string=str(s)):
                print(f"{n}: String -> {s}")
            case StringResult(err=exc) if isinstance(exc, Exception):
                print(f"{n}: Error -> {exc}")
