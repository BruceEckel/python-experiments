# my_result.py
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")  # Any type
E = TypeVar("E", bound=Exception)  # Only Exceptions


@dataclass(frozen=True)
class Result(Generic[T, E]):
    value: T | E


@dataclass(frozen=True)
class Ok(Result[T, E]):
    pass


@dataclass(frozen=True)
class Err(Result[T, E]):
    pass
