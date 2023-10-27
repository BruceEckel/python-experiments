# result.py
from dataclasses import dataclass


class Result:
    pass


@dataclass(frozen=True)
class Ok(Result):
    string: str

    def __post_init__(self):
        assert isinstance(
            self.string, str
        ), "Expected a string in Ok result."


@dataclass(frozen=True)
class Err(Result):
    err: Exception

    def __post_init__(self):
        assert isinstance(
            self.err, Exception
        ), "Expected an exception in Err result."


# Example Usage
result1 = Ok("eeny")
result2 = Err(Exception("after eeny"))
