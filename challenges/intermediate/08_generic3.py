"""
TODO:

The function `add` accepts one argument and returns a value, they all have the same type.
The type can only be int or subclasses of int.
"""
from typing import assert_type

def add[T: int](a: T) -> T:
    return a

class MyInt(int):
    pass

assert_type(add(1), int)
assert_type(add(MyInt(1)), MyInt)
# assert_type(add("1"), str)

# add(["1"], ["2"])
# add("1", 2)
