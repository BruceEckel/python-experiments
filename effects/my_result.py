# result.py
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")  # Holds any type
E = TypeVar("E", bound=Exception)  # Always a type of exception


@dataclass(frozen=True)
class Result(Generic[T, E]):
    value: T | E


@dataclass(frozen=True)
class Ok(Result[T, E]):
    def __post_init__(self):
        if isinstance(self.value, Exception):
            raise TypeError("Not expecting Exception")


@dataclass(frozen=True)
class Err(Result[T, E]):
    def __post_init__(self):
        if not isinstance(self.value, Exception):
            raise TypeError("Expecting Exception")
