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
        return f"{self.name} ({self.height}cm, {self.days} days)"


plants = [
    Plant("Rose", 25, 30),
    Plant("Oak", 200, 365),
    Plant("Cactus", 5, 90),
    Plant("Sunflower", 80, 45),
    Plant("Fern", 15, 120)
]

print("=== Plant Factory Output ===")

num_plants = 0
for plant in plants:
    print(f"Created: {plant.get_info()}")
    num_plants += 1

print(f"\nTotal plants created: {num_plants}")
