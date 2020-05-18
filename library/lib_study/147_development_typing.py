"""
typing --- 类型标注支持
Python运行时不强制执行函数和变量类型注释。它们可以被第三方工具使用，例如类型检查器、ide、索引等等。

紧紧是提示
"""

import typing

print(dir(typing))

Vector = typing.List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


# typechecks; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(new_vector)

# 泛型
from typing import Sequence, TypeVar

T = TypeVar('T')  # Declare type variable


def first(l: Sequence[T]) -> T:  # Generic function
    return l[0]


"""
@typing.overload

@typing.final

@typing.no_type_check

@typing.no_type_check_decorator

@typing.type_check_only

@typing.runtime_checkable
"""
class Base:
    @typing.final
    def done(self) -> None:
        ...
class Sub(Base):
    def done(self) -> None:  # Error reported by type checker
          ...

@typing.final
class Leaf:
    ...
class Other(Leaf):  # Error reported by type checker
    ...

