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

    result = results[fallible.index % len(results)]
    fallible.index += 1

    return result


if __name__ == "__main__":
    for n in range(8):

        def show(id: str, msg: str):
            print(f"{n}: {id} Error -> {msg}")

        result = fallible()
        print(result)
        match result:
            case Ok(value=s):
                print(f"{n}: Success -> {s}")
            case Err(value=exc):
                match exc:
                    case TabError(args=(msg,)):
                        show("Tab", msg)
                    case IndentationError(args=(msg,)):
                        show("Indentation", msg)
                    case ValueError(args=(msg,)):
                        show("Value", msg)
                    case Exception(args=(msg,)):
                        show("Generic", msg)
        print("-" * 40)
