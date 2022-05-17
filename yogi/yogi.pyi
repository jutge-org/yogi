from typing import Optional, TypeVar, Type


version: str


T = TypeVar('T', int, float, str)


def read(t: Type[T]) -> T:
    ...


def scan(t: Type[T]) -> Optional[T]:
    ...
