# result.py
from dataclasses import dataclass


@dataclass(frozen=True)
class Result:
    pass


@dataclass(frozen=True)
class Ok(Result):
    string: str

    def __post_init__(self):
        assert isinstance(
            self.string, str
        ), "Expected string in Ok Result."


@dataclass(frozen=True)
class Err(Result):
    err: Exception

    def __post_init__(self):
        assert isinstance(
            self.err, Exception
        ), "Expected exception in Err Result."
