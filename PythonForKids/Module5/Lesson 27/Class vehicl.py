#  Write a program to create a class Vehicle and perform the following tasks - 1. Create an __init__ method with arguments - max_speed and mileage 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 3. Print the values of max_speed and mileage by using the object

class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage

VehicleA=Vehicle(120,67)
VehicleB=Vehicle(90,65)

print("Max speed of vehicle A nd B are : ",VehicleA.max_speed,VehicleB.max_speed)
print("Mileage of vehicle a and b are  : ",VehicleA.mileage,VehicleB.mileage)