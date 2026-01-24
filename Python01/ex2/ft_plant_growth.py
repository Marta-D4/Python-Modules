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
        return f"{self.name}: {self.height}cm, {self.days} days old"


# List of Plant objects
plants = [
    Plant("rose", 25, 30),
    Plant("sunflower", 80, 45),
    Plant("cactus", 15, 120)
]

print("=== Day 1 ===")
for plant in plants:
    print(plant.get_info())

# Stored initial height to calculate the growth
first_height = {plant.name: plant.height for plant in plants}
num_days = 1

# Simulate growth over 7 days
while num_days < 7:
    for plant in plants:
        plant.grow()
        plant.age()
    num_days += 1

# Show the information of each plant
print("\n=== Day 7 ===")
for plant in plants:
    growth = plant.height - first_height[plant.name]
    print(f"{plant.get_info()}\nGrowth this week: +{growth}cm")

