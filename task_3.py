class Employee:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def print_information(self) -> str:
        print("Печатаю информацию...")


class Manager(Employee):
    def manage_employee(self) -> str:
        return "Указываю работникам что делать"


class Developer(Employee):
    def coding(self) -> str:
        return "Создаю код для программы"


m1 = Manager(name="Bob", age=15)
d1 = Developer(name="Clara", age=23)
print(m1.manage_employee())
print(d1.coding())
