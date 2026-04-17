# Write a program to create a base class that consists of two functions - one to display a value, and another function is an abstract method. Next, create a subclass that consists of a method similar to the abstract method. Finally, showcase how Abstraction is being implemented in this exampl
from abc import ABC, abstractmethod

class AbsClass(ABC):
    def value(self,a):
        print("value ",a)

    @abstractmethod
    def task(self):
        print("This is an absract method!")
class test_class(AbsClass):
    def task(self):
        print("This is test class !")
obj=test_class()
obj.task()
obj.value(200)