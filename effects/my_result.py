from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")  # Any type
E = TypeVar("E", bound=Exception)  # Only Exceptions


@dataclass(frozen=True)
class Result(Generic[T, E]):
    value: T | E


@dataclass(frozen=True)
class Ok(Result[T, E]):
    def __post_init__(self):
        assert not isinstance(self.value, Exception)

    def __repr__(self) -> str:
        return f"Ok({self.value!r})"


@dataclass(frozen=True)
class Err(Result[T, E]):
    def __post_init__(self):
        assert isinstance(self.value, Exception)

    def __repr__(self) -> str:
        return f"Err({self.value!r})"
