#  Write a program to create a class with following variables and methods - 1. Private variable named privateVar that contains an integer value 2. Create a private function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the functions.

class myclass:
    __privateVar=12 # thsi is private variable

    def __privateMeth(self): # It is private method 
     print("This is a private method!")
    def hello(self): # fuction to print private variable 
     print("value of private variable is ",self.__privateVar)
     self.__privateMeth() # accessing privateMeth inside a class.
obj=myclass()
obj.hello()
# 0bj.__privateMeth() ...It will raise an attribute error because it is privtre and cannot be called directly.      