class BankAccount:
    def __init__(self, balance: float) -> None:
        self.balance = balance

    def replenishment(self, cash_add) -> str:
        self.balance += cash_add
        return f"было добавлено {cash_add} тг"

    def withdrawal(self, cash_sub) -> str:
        self.balance -= cash_sub
        return f"было снято {cash_sub} тг"


class CurrentAccount(BankAccount):
    def show_account(self) -> str:
        return f"Ваш текущий счет составляет {self.balance} тг"


class SavingsAccount(BankAccount):
    def add_money(self, money1) -> str:
        self.balance += money1
        return f"было переведено на сберегательный счет - {money1}, сберегательный счет равен - {self.balance}"


m = BankAccount(10000.0)
m1 = CurrentAccount(7000.0)
m2 = SavingsAccount(3000.0)
print(m.replenishment(1000))
print(m.balance)
print(m1.show_account())
print(m2.add_money(1200))
