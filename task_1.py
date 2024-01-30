class Figure:
    def area(self):
        raise NotImplementedError

    def perimetr(self):
        raise NotImplementedError


class Rectangle(Figure):
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

    def area(self) -> int:
        return self.length * self.width

    def perimetr(self) -> int:
        return (self.length + self.width) * 2


class Circle(Figure):
    def __init__(self, radius: int) -> None:
        self.radius = radius
        self.pi = 3.14

    def area(self) -> float:
        return self.pi * (self.radius**2)

    def perimetr(self) -> float:
        return 2 * self.pi * self.radius


fig1 = Rectangle(
    length=12,
    width=2,
)
fig2 = Circle(
    radius=4,
)
print(fig1.area())
print(fig1.perimetr())
print(fig2.area())
print(fig2.perimetr())
