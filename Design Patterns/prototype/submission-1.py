from abc import ABC, abstractmethod
from typing import Self

class Shape(ABC):
    @abstractmethod
    def clone(self) -> Self:
        pass

class Square(Shape):
    def __init__(self, length: int):
        self.length = length

    def get_length(self) -> int:
        return self.length

    def clone(self) -> Self:
        # Write your code
        return Square(self.length)


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def clone(self) -> Self:
        # Write your code here
        return Rectangle(self.width, self.height)


class Test:
    def clone_shapes(self, shapes: List[Shape]) -> List[Shape]:
        # Write your code here
        return [shape.clone() for shape in shapes]
