"""
TODO:

foo only accepts literal 'left' and 'right' as its argument.
"""
from typing import Literal

type TDirection = Literal["left", "right"]

def foo(direction: TDirection):
    ...

foo("left")
foo("right")

a = "".join(["l", "e", "f", "t"])
# foo(a)
