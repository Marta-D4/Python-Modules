#!/usr/bin/env python3

class Plant():
    def __init__(self, name, height, days):
        self.name = name.capitalize()
        self.height = height
        self.days = days

    def base_info(self, plant_type):
        return f"{self.name} ({plant_type}): {self.height}cm, {self.days} days"


class Flower(Plant):
    def __init__(self, name, height, days, color):
        super().__init__(name, height, days)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        return f"\n{self.base_info('Flower')}, {self.color} color"


class Tree(Plant):
    def __init__(self, name, height, days, trunk_diameter):
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = self.trunk_diameter * 2
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self):
        return f"\n{self.base_info('Tree')}, {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    def __init__(self, name, height, days, harvest_season, nutritional_value):
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        return (
            f"\n{self.base_info('Vegetable')}, {self.harvest_season} harvest"
        )


flowers = [
    Flower("rose", 25, 30, "red"),
    Flower("tulip", 15, 22, "purple")
]

trees = [
    Tree("oak", 500, 1825, 50),
    Tree("birch", 300, 1506, 25)
]

vegetables = [
    Vegetable("tomato", 80, 90, "summer", "vitamin C"),
    Vegetable("carrot", 20, 40, "spring", "vitamin E")
]

print("=== Garden Plant Types ===")

for flower in flowers:
    print(f"{flower.get_info()}")
    flower.bloom()

for tree in trees:
    print(f"{tree.get_info()}")
    tree.produce_shade()

for vegetable in vegetables:
    print(f"{vegetable.get_info()}")
    print(f"{vegetable.name} is rich in {vegetable.nutritional_value}")
