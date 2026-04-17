class BMW:
    def fuel_type(self):
        print("BMW fuel type: Petrol")

    def max_speed(self):
        print("BMW max speed: 250 km/h")


class Ferrari:
    def fuel_type(self):
        print("Ferrari fuel type: Petrol")

    def max_speed(self):
        print("Ferrari max speed: 340 km/h")


cars = [BMW(), Ferrari()]

for car in cars:
    car.fuel_type()
    car.max_speed()
    print()