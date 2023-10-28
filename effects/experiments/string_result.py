# string_result.py
from dataclasses import dataclass


@dataclass(frozen=True)
class StringResult:
    pass


@dataclass(frozen=True)
class Ok(StringResult):
    string: str

    def __post_init__(self):
        assert isinstance(
            self.string, str
        ), "Expected string in Ok StringResult."


@dataclass(frozen=True)
class Err(StringResult):
    err: Exception

    def __post_init__(self):
        assert isinstance(
            self.err, Exception
        ), "Expected exception in Err StringResult."
