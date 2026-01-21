#!/usr/bin/env python3

class Plant():
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = height
        self.age = age


plants = [
    Plant("rose", 25, 30),
    Plant("sunflower", 80, 45),
    Plant("cactus", 15, 120)
]

print("=== Garden Plant Registry ===")
for plant in plants:
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
