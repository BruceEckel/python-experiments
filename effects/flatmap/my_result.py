# my_result.py
from dataclasses import dataclass
from typing import Callable, Generic, TypeVar

T = TypeVar("T")  # Holds any type
E = TypeVar("E", bound=Exception)  # Always a type of exception


@dataclass(frozen=True)
class Result(Generic[T, E]):
    value: T | E

    def and_then(
        self, func: Callable[[T], "Result[T, E]"]
    ) -> "Result[T, E]":
        if isinstance(self, Ok):
            return func(self.value)
        return self


@dataclass(frozen=True)
class Ok(Result[T, E]):
    pass


@dataclass(frozen=True)
class Err(Result[T, E]):
    pass
