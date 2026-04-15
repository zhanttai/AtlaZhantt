from datetime import datetime 

class Product:
    name: stre
    release_date: datetime
    description: str
    __price: float 
    __stock: 0 

def __init__(self, name, release_date, description, price):
    self.name = name
    self.release_date = release_date
    seld.description = description
    if price < 1:
        raise ValueError("Неверное значение")
    self.price = price 

def get_stock(self):
    return self.stock

def set_stock(self, amount):
    if amount < 1 or amount > 100000:
        raise ValueError("Неверное значение")

def sell(self, amount = 1):
    if amount < 1 or amount > 100000:
        raise ValueError("Неверное значение")
    if amount > self.__stock:
        raise ValueError("Не хватает инвентаря") 
    self.__stock -= amount

Iphone_17 = Product(
    name="Iphone 17 Pro Max"
    release_date="2025"
    drscription="Lalalalala"
    price=1500,99
)

Iphone_16 = Product(
    name="Iphone 16 Pro Max"
    release_date="2024"
    drscription="Lalalalala"
    price=1200,99
)

set_stock(self, 10000)
print stock