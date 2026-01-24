#!/usr/bin/env python3

"""
Represents a plant that can grow over time, with the attributes:
    name (str): name of the plant, first letter capitalized.
    height (int): height of the plant in centimeters.
    days (int): age of the plant in days.
def __init__ :
    + Initializes a Plant instance.
def grow:
    + Increases by 1cm a plants height.
def age:
    + Increases by 1 day a plants age.
def get_info:
    + Returns a plants current information.
"""
class Plant():
    def __init__(self, name, height, days):
        self.name = name.capitalize()
        self.height = height
        self.days = days

    def grow(self):
        self.height += 1

    def age(self):
        self.days += 1

    def get_info(self):
        return f"{self.name} ({self.height}cm, {self.days} days)"

# List of Plant objects
plants = [
    Plant("Rose", 25, 30),
    Plant("Oak", 200, 365),
    Plant("Cactus", 5, 90),
    Plant("Sunflower", 80, 45),
    Plant("Fern", 15, 120)
]

print("=== Plant Factory Output ===")

# Counts and show all created plants
num_plants = 0
for plant in plants:
    print(f"Created: {plant.get_info()}")
    num_plants += 1

# Shows total number of plants created
print(f"\nTotal plants created: {num_plants}")

