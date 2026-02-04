"""
TODO:

The function `add` accepts two arguments and returns a value, they all have the same type.
The type can only be str or int.
"""
from typing import assert_type, TypeVar

TStrInt = TypeVar("TStrInt", str, int)

def add(a: TStrInt, b: TStrInt) -> TStrInt:
    return a

assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)

# add(["1"], ["2"])
# add("1", 2)
