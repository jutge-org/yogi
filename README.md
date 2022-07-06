![yogi.png](yogi.png)

# `yogi`

The `yogi` package offers a simple typed interface to read input in Python. It is built in order to offer beginners an easy way to read data and to provide static type checking. 


# Installation

- Install with `pip3 install yogi`.
- Upgrade to latest version with `pip3 install --upgrade yogi`.
- Uninstall with `pip3 uninstall yogi`.

Depending on the system you may have to use `pip` rather than `pip3`.

# Usage

## `read`

The `read` function returns the next token in the input. The type of this token must be specified: `int`, `float` or `str`.

For instance, this program reads two integer numbers and writes their sum:

```python
from yogi import read

x = read(int)
y = read(int)

print(x + y)
```

In a similar way, this program reads two real numbers and writes their product:

```python
import yogi

x = yogi.read(float)
y = yogi.read(float)

print(x * y)
```

The `read` function expects that input is available and that its content matches the requested type. Otherwise, it raises an exception.


## `scan`

The `scan` function also returns the next token in the input, but may return `None` when the input ends or when its content does not match the requested type. The type of the token (`int`, `float` or `str`) must be specified.

For instance, this program reads a sequence of integer numbers and writes their sum:

```python
from yogi import scan

s = 0
x = scan(int)
while x is not None:
    s += x
    x = scan(int)
print(s)
```

Consequently, the difference between `read` and `scan` is that the latter returns `None` when input is over or content is not correct, whereas the former fails. In fact, `read` just performs a `scan` and checks it is not `None`.


## `tokens`

The `tokens` function provides a way to iterate over all tokens (with a certain type) in the whole input. The type of the tokens (`int`, `float` or `str`) must be specified. The `tokens` function expects that the content of the read tokens match the requested type. Otherwise, it raises an exception just like `read`.

The usual way to use `tokens` is in a main `for` loop. For instance, this program reads a sequence of integer numbers and writes their sum:

```python
from yogi import tokens

s = 0
for x in tokens(int):
    s += x
print(s)
```

Calling `read` and `scan` within a loop of `tokens` is possible and may be useful. See, for instance, the next code based on [problem P29448 of Jutge.org](https://jutge.org/problems/P29448_en) (without spoilers):

```python
from yogi import tokens

for day in tokens(int):
    month, year = read(int), read(int)
    if correct_date(day, month, year):
        print('Correct Date')
    else:
        print('Incorrect Date')
```

## Tokens

The `read` and `scan` functions return the next token in the input. So does `tokens`, which returns all remaining tokens in the input. The type of the token must be given as a parameter: `scan(int)`, `read(int)`, `read(float)`, `scan(float)`, `scan(str)`, `read(str)`.

Tokens are separated by whitespace, so that `read|scan(str)` returns the next single word. Whitespace characters cannot be obtained.

In the event no more tokens are available, `scan` returns `None`, but `read` raises an exception. 

Also, in the event that the current token does not represent a value of the requested type, `scan` returns `None`, but `read` and `tokens` raise an exception. This could happen, for instace, when `read|scan|tokens(int)` attempt to read a non integer token.

Besides type annotations, the important difference between `read` and `scan` and the `input` built-in function is that `read` and `scan` are able to get their tokens among one or more lines, whereas `input` works on just one single line. On the other hand, it is not possible to obtain whitespaces with `read` and `scan`.


## Typing

`yogi` exposes the types of the functions, so that static type checkers (such as `mypy` or those in IDEs) can be used to reduce bugs. 

The `read` function returns a value of the same type as requested. For instance, `read(int)` returns an `int`.

The `scan` function returns `None` or a value of the same type as requested. For instance, `scan(int)` returns an `Optional[int]`, that is, a `None` or an `int`.

Each element from the `tokens` iterator returns a value of the same type as requested. For instance, `tokens(int)` return a stream of `int` values.

The next table sumarizes this typing:

```python
read(int)        : int
read(float)      : float
read(str)        : str

scan(int)        : Optional[int]
scan(float)      : Optional[float]
scan(str)        : Optional[str]

tokens(int)      : Iterator[int]
tokens(float)    : Iterator[float]
tokens(str)      : Iterator[str]
```


## Exceptions

`read(t)`:

- Raises `EOFError` if trying to read past the end of the input.
- Raises `ValueError` if the read token does not match the type `t`.
- Raises `TypeError` if `t` is not `int`, `float` or `str`.

`scan(t)`:

- Raises `TypeError` if `t` is not `int`, `float` or `str`.

`tokens(t)`:

- Raises `ValueError` if the read token does not match the type `t`.
- Raises `TypeError` if `t` is not `int`, `float` or `str`.


# Extra features

## Recursion limit

When importing the `yogi` package, the maximum depth of the Python interpreter stack is increased (using `sys.setrecursionlimit(1000000)`).  


## Version

The variable `yogi.version` contains the version of the package.


# License

Apache License 2.0


# Credits

- [Jordi Petit](https://github.com/jordi-petit)

© Universitat Politècnica de Catalunya, 2022
