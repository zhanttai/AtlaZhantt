class BankAccount:
    owner: str
    # Private attribute(приватные аттрибуты) не могут быть вызваны вне контекста класса
    __balance: float = 0.0

    def __init__(self, owner):
        self.owner = owner

    # def __str__(self):
    #     return f"{self.owner} has {self.balance}"

    def __repr__(self):
        return f"{self.owner} has {self.__balance}"

    def add_money(self, amount):
        if amount <= 0:
            raise ValueError("низя")
        with open(f"./ATLA/{self.owner}.txt", "a") as file:
            file.write(f"added {amount}\n")

        self.__balance += amount

    def remove_money(self, amount):
        if amount <= 0:
            raise ValueError("низя")

        if amount > self.__balance:
            raise ValueError(f"ты бедный tebe nuzhno: {amount - self.__balance}")
        
        with open(f"./ATLA/{self.owner}.txt", "a") as file:
            file.write(f"removed {amount}\n")

        self.__balance -= amount
    
    

    def print_transactions(self):
         with open(f"./ATLA/{self.owner}.txt", "r") as file:
            for index, element in enumerate(file, start=1):
                print(index, element, end="")




new_account = BankAccount(owner="Arstan")
new_account.add_money(10.0)
new_account.remove_money(9)
new_account.__balance = 10000000
new_account.print_transactions()