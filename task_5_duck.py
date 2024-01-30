class Duck:
    def __init__(self, name: str) -> None:
        self.name = name

    def quack(self) -> None:
        print("утка крякает")

    def swim(self) -> None:
        print("утра плавает")


class WildDuck(Duck):
    def migrate(self) -> None:
        print("дикая утка мигрировала")


class DomesticDuck(Duck):
    def bring_egg(self) -> None:
        print("домашняя утка принесла яйцо")


class RubberDuck(Duck):
    def jump(self) -> None:
        print("резиновая утка прыгнула")


d1 = Duck("Bob")
d2 = WildDuck("Nick")
d3 = DomesticDuck("Carl")
d4 = RubberDuck("Frank")
d1.quack(), d1.swim()
d2.migrate()
d3.bring_egg()
d4.jump()
