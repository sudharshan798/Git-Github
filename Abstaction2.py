from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        None
class tiger(Animal):
    def eat(self):
        print("The tiger eat Non Veg")
class cow(Animal):
    def eat(self):
        print("The cow eat Veg")
obj = cow()
obj.eat()
obj2= tiger()
obj2.eat()