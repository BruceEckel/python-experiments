# operations.py
from result import Result, Ok, Err


def get_number(s: str) -> Result[int, Exception]:
    try:
        return Ok(int(s))
    except ValueError:
        return Err(ValueError(f"Couldn't convert {s} to a number."))


def double(n: int) -> Result[int, Exception]:
    return Ok(n * 2)


def to_string(n: int) -> Result[str, Exception]:
    try:
        return Ok(str(n))
    except Exception as e:
        return Err(e)
