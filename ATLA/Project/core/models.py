import random
import uuid
from uuid import UUID


class Account:
    owner_name: str
    __balance: float = 0.00
    account_number: UUID

    def __init__(
        self, owner_name: str, balance: float, account_number: UUID = uuid.uuid4()
    ):
        self.owner_name = owner_name
        self.__balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Некорректная сумма")

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Некорректная сумма")
        if amount > self.__balance:
            raise ValueError("Некорректная сумма")
        self.__balance -= amount

    def save_accounts(self, accounts_list):
        with open("./Project/core/Account_List.txt", "a") as file:
            for acc in accounts_list:
                file.write(
                    f"{acc.owner_name}|{acc.account_number}|{acc.show_balance()}\n"
                )

    def show_balance(self):
        return self.__balance

    def __str__(self):  # Магический метод __str__
        return f"Account({self.owner_name}, balance={self.__balance}, id={self.account_number})"


class CreditPlans:
    min_term: int
    max_term: int
    min_percent: float
    max_percent: float

    def __init__(self, min_term=6, max_term=36, min_percent=10, max_percent=25):
        self.min_term = min_term
        self.max_term = max_term
        self.min_percent = min_percent
        self.max_percent = max_percent

    def generate_plan(self, amount):
        term = random.randint(self.min_term, self.max_term)
        percent = random.uniform(self.min_percent, self.max_percent)

        total = amount + (amount * percent / 100)
        monthly_payment = total / term

        return {
            "amount": amount,
            "term": term,
            "percent": round(percent, 2),
            "monthly_payment": round(monthly_payment, 2),
            "total": round(total, 2),
        }


class PremiumAccount(Account):
    bonus: float

    def __init__(
        self,
        owner_name: str,
        balance: float = 0.0,
        bonus_rate: float = 0.05,
    ):
        super().__init__(owner_name, balance)
        self.bonus = bonus_rate

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Некорректное значние")

        bonus = amount * self.bonus
        total = amount + bonus

        super().deposit(total)

        return bonus

    def __str__(self):
        return f"PremiumAccount({self.owner_name}, bonus={self.bonus * 100}%)"
