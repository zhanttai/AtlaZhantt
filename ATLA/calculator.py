from ast import Raise
from binascii import Error
def add (a, b):
    return a + b 
def subtract (a, b):
    return a - b 
def multiply (a, b):
    return a * b
def divide (a, b):
    try:
        return a / b 
    except ZeroDivisionError:
        return ValueError

def calculate():
    a = input("Введите первое число: ")
    b = input("Введите второе число: ") 
    