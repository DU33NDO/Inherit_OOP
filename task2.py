from datetime import datetime


class Vehicle:
    def __init__(
        self,
        speed: int,
        color: str,
        capacity: float,
        year_of_release: datetime,
    ) -> None:
        self.speed = speed
        self.color = color
        self.capacity = capacity
        self.year_of_release = year_of_release

    def __repr__(self) -> str:
        return f"speed = {self.speed}, color = {self.color}, capacity = {self.capacity} metr square, year of release: {self.year_of_release}"


class Car(Vehicle):
    def __init__(
        self,
        speed: int,
        color: str,
        capacity: float,
        year_of_release: datetime,
        has_spoiler: bool,
    ) -> None:
        self.has_spoiler = has_spoiler
        super().__init__(
            speed=speed, color=color, capacity=capacity, year_of_release=year_of_release
        )

    def __repr__(self) -> str:
        return f"{super().__repr__()}, has spoiler = {self.has_spoiler}"


class Bus(Vehicle):
    def __init__(
        self,
        speed: int,
        color: str,
        capacity: float,
        year_of_release: datetime,
        has_conductor: bool,
    ) -> None:
        self.has_conductor = has_conductor
        super().__init__(
            speed=speed, color=color, capacity=capacity, year_of_release=year_of_release
        )

    def __repr__(self) -> str:
        return f"{super().__repr__()}, has conductor = {self.has_conductor}"


a1 = Car(
    speed=12,
    color="red",
    capacity=2.0,
    year_of_release=datetime(year=2021, month=3, day=11),
    spoiler=True,
)
a2 = Bus(
    speed=12,
    color="blue",
    capacity=4.0,
    year_of_release=datetime(year=2011, month=3, day=11),
    conductor=False,
)

print(a1)
print(a2)
