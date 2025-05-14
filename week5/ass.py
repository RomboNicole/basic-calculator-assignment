# Assignment 1: My Own Class - Hero

# Main hero class
class Hero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def display_info(self):
        print(f"{self.name} protects {self.city} with {self.power}.")

# A special hero who can fly
class FlyingHero(Hero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def display_info(self):
        print(f"{self.name} flies at {self.flight_speed} km/h to save {self.city} using {self.power}.")

# Create some hero objects
print("Assignment 1 Output:")
hero1 = Hero("Captain Python", "Super Coding", "Code City")
hero2 = FlyingHero("Wind Rider", "Air Control", "Sky Town", 450)

hero1.display_info()
hero2.display_info()

print("\n")  # Spacer

# Activity 2: Polymorphism with Vehicles

# Main vehicle class
class Vehicle:
    def move(self):
        print("Vehicle is moving...")

# Specific vehicle types
class Car(Vehicle):
    def move(self):
        print("Car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("Boat is sailing on the water.")

# List of vehicles
print("Activity 2 Output:")
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()

    