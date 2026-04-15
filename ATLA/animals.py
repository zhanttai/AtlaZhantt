class Animals:
    name: str
    age: int

def __init__(self, name: str, age: int):
    self.name=name
    self.age=age

def speak():
    pass
def __str__(name, age):
    animal = Animals("Барсик", 3)
    print(animal)      
    animal.speak()
    return animal

class Dog(Animals):

    def __init__(self, name, age):
        super().__init__()
        self.name=name
        self.age=age

    def __repr__(self):
        return f"{super().__repr__()}"

dog = Dog("Барсик", 3)
print(dog)      # Барсик, 3 лет
dog.speak f("Гав, меня зовут Барсик")    # Гав! Меня зовут Барсиk