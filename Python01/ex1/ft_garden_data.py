#!/usr/bin/env python3

"""
Represents a plant with the attributes:
    name (str): name of the plant, the first letter capitalized. 
    height (int): height of the plant in centimeters.
    age (int): age of the plant in days.
The function inside initializes a new Plant instance.
"""
class Plant():
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = height
        self.age = age


# List of Plant objects
plants = [
    Plant("rose", 25, 30),
    Plant("sunflower", 80, 45),
    Plant("cactus", 15, 120)
]

# Displays information of each plant registered
print("=== Garden Plant Registry ===")
for plant in plants:
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")

