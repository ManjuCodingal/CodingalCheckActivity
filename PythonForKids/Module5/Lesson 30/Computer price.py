# Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.
class Computer:
    def __init__(self):
        self.__maxprice=500
    def sell(self):
        print("Selling price is ",self.__maxprice)
    def setmaxprice(self,price): # This is a setter method to change the price , this will update the private variable __maxprice withi the class.
        self.__maxprice=price
obj=Computer()
obj.sell()
obj.__maxprice=200 # Tried to modify the private variabledirectly outside the class,it will not work.
obj.sell()
obj.setmaxprice(200) # calling the stter method to update the private variable.
obj.sell()