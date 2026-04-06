# Create a class named Dog
class Dog:
    
    # Class variable (shared by all objects)
    animal = "Dog"
    
    # Constructor to initialize breed and colour
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

    # Method to display details
    def display_details(self):
        print("Animal:", Dog.animal)
        print("Breed:", self.breed)
        print("Colour:", self.colour)
        print("----------------------")


# Create two different objects
dog1 = Dog("Labrador", "Golden")
dog2 = Dog("German Shepherd", "Black and Brown")

# Display details of both dogs
dog1.display_details()
dog2.display_details()