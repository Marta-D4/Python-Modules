#!/usr/bin/env python3

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


plants = [
    Plant("rose", 25, 30),
    Plant("sunflower", 80, 45),
    Plant("cactus", 15, 120)
]

print("=== Day 1 ===")
for plant in plants:
    print(plant.get_info())

first_height = {plant.name: plant.height for plant in plants}
num_days = 1

while num_days < 7:
    for plant in plants:
        plant.grow()
        plant.age()
    num_days += 1

print("\n=== Day 7 ===")
for plant in plants:
    growth = plant.height - first_height[plant.name]
    print(f"{plant.get_info()}\nGrowth this week: +{growth}cm")
