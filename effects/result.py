# result.py
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")  # Holds any type
E = TypeVar("E", bound=Exception)  # Always a type of exception


@dataclass(frozen=True)
class Result(Generic[T]):
    value: T


@dataclass(frozen=True)
class Ok(Result[T]):
    pass


@dataclass(frozen=True)
class Err(Result[E]):
    pass
