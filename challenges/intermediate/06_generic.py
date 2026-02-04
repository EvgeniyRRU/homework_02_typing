"""
TODO:

The function `add` accepts two arguments and returns a value, they all have the same type.
"""
from typing import assert_type, TypeVar

T = TypeVar("T")

def add(a: T, b: T) -> T:
    return a

assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)
assert_type(add(["1"], ["2"]), list[str])
# assert_type(add(1, "2"), int)
