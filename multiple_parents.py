class BaseOne:
    def sing(self):
        print("Я пою")


class BaseTwo:
    def ride(self):
        print("Я еду")


class Child(BaseOne, BaseTwo):
    pass


c = Child()
c.ride()
b = c.sing()
print()
