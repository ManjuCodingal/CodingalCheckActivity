#  Write a Python program to implement Inheritance by creating a Parent Class Vehicle with a constructor that has details like name, maximum speed, and mileage. Then, create a Child Class Bus that inherits Class Vehicle. Finally, showcase Inheritance to display the details of the Vehicle Bus named - School Volvo.

class vehicle:

    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class Bus(vehicle):
    pass
school_bus=Bus("school volvo",140,34)

print("Vehicle name is ",school_bus.name)
print("Max speed ",school_bus.max_speed)
print("Mileage : ",school_bus.mileage)