from datetime import datetime


class Person:
    def __init__(
        self,
        name: str,
        sname: str,
        birthday: datetime,
        phone_number: str,
    ):
        self.name = name
        self.sname = sname
        self.birthday = birthday
        self.phone_number = phone_number

    def info(self):
        print(
            f"Имя: {self.name}. Фамилия: {self.sname}. Др: {self.birthday}. Телефона: {self.phone_number}"
        )


class Accountant(Person):
    def __init__(
        self,
        name: str,
        sname: str,
        birthday: datetime,
        phone_number: str,
        expirience_age: int,
    ) -> None:
        self.expirience_age = expirience_age
        super().__init__(
            name=name,
            sname=sname,
            birthday=birthday,
            phone_number=phone_number,
        )

    def create_excel_table(self) -> None:
        print("Начинаю создание таблички Excel")


class Programmist(Person):
    def refactor_code(self) -> None:
        print("Программист начал рефакторинг")

    def info(self):
        print("Я программист! Я самый лучший!")


a = Accountant(
    name="aC",
    sname="Ac",
    birthday=datetime(year=2000, month=1, day=1),
    phone_number="87777777777",
    expirience_age=15,
)
p = Programmist(
    name="Pr",
    sname="Pr",
    birthday=datetime(year=2000, month=1, day=1),
    phone_number="87777777777",
)

p.refactor_code()
a.create_excel_table()

p.info()
a.info()

print("Опыт работы бухгалтера:", a.expirience_age, "лет")
