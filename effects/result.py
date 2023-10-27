# result.py
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")  # Holds any type
E = TypeVar(  # Always some type of exception
    "E", bound=Exception
)


@dataclass(frozen=True)
class Result(Generic[T]):
    value: T


@dataclass(frozen=True)
class Ok(Result[T]):
    pass


@dataclass(frozen=True)
class Err(Result[E]):
    pass
