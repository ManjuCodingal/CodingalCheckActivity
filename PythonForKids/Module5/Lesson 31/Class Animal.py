# Write a program to implement abstraction on animal class (base class). The abstract method will be move will display what subclasses can do. Subclasses can be something like - Human, Dog.
from abc import ABC ,abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can run and walk")
class Dog(Animal):
    def move(self):
        print("I can walk and run and bark!")

obj1=Human()
obj1.move()
obj2=Dog()
obj2.move()