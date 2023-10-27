# convert_exceptions_2.py
from result import Result, Ok, Err


def fallible() -> Result:
    # Holds its value between function calls:
    if not hasattr(fallible, "index"):
        fallible.index = 0

    results = [
        Ok("eeny"),
        Err(Exception("after eeny")),
        Ok("meeny"),
        Err(IndentationError("after meeny")),
        Ok("miney"),
        Err(TabError("after miney")),
        Ok("moe"),
        Err(ValueError("after moe")),
    ]

    result = results[
        fallible.index % len(results)
    ]
    fallible.index += 1

    return result


if __name__ == "__main__":
    for n in range(11):
        result = fallible()
        print(result)
        match result:
            case Ok(value=s):
                print(f"{n}: Success -> {s}")
            case Err(value=exc):
                print(f"{n}: Error -> {exc}")
