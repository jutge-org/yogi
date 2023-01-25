# Copyright 2022, Universitat Politècnica de Catalunya
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
Simple typed interface to read input in Python
"""


from typing import Optional, TypeVar, Type, Iterator
import sys


version = '1.3.2'
"""package version"""


# hack to get more stack size
sys.setrecursionlimit(1000000)


# type variable that can represent int, float or str
T = TypeVar('T', int, float, str)


def read(t: Type[T]) -> T:
    """
    Returns the next token of the input interpreted as having type t.

    Raises EOFError if trying to read past the end of the input.
    Raises ValueError if the read token does not match the type t.
    Raises TypeError if t is not int, float or str.
    """

    _check(t)
    token = _get()
    if token is None:
        raise EOFError
    else:
        return t(token)  # might rise ValueError


def scan(t: Type[T]) -> Optional[T]:
    """
    Returns the next token of the input interpreted as having type t.
    Returns None when trying to read past the end of the input
    or if the read token does not match the type t.

    Raises TypeError if t is not int, float or str.
    """

    _check(t)
    token = _get()
    if token is None:
        return None
    else:
        try:
            return t(token)
        except ValueError:
            return None


def tokens(t: Type[T]) -> Iterator[T]:
    _check(t)
    while True:
        try:
            token = next(_generator)
        except StopIteration:
            break
        yield t(token)  # might rise ValueError


def _check(t: Type[T]) -> Optional[str]:
    """Check that the type t is valid."""
    if t not in [int, float, str]:
        raise TypeError


def _get() -> Optional[str]:
    """Returns the next token in the input or None if eof."""

    try:
        token = next(_generator)
    except StopIteration:
        return None
    return token


def _token_generator() -> Iterator[str]:
    """Generates the tokens in all the lines of input."""
    for line in sys.stdin:
        for token in iter(line.split()):
            yield token


_generator = _token_generator()
"""Generator instance."""
