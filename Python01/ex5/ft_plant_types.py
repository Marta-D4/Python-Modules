#!/usr/bin/env python3

"""
Represents a plant with the attributes:
    name (str): name of the plant, the first letter capitalized. 
    height (int): height of the plant in centimeters.
    age (int): age of the plant in days.
    
def __init__:
    + Initializes a Plant instance.
def base_info:
    + Returns a basic formatted string with the plants general info.
"""
class Plant():
    def __init__(self, name, height, days):
        self.name = name.capitalize()
        self.height = height
        self.days = days

    def base_info(self, plant_type):
        return f"{self.name} ({plant_type}): {self.height}cm, {self.days} days"


"""
Represents a flower, subclass of Plant, with an additional attribute:
    color (str): color of the flower.

def __init__:
    + Initializes a Flower instance.
def bloom:
    + Simulates the flower blooming printing a message.
def get_info:
    + Returns the flowers information.
"""
class Flower(Plant):
    def __init__(self, name, height, days, color):
        super().__init__(name, height, days)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        return f"\n{self.base_info('Flower')}, {self.color} color"


"""
Represents a tree, subclass of Plant, with an additional attribute:
    trunk_diameter (int): diameter of the trees trunk in centimeters.

def __init__:
    + Initializes a Tree instance.
def produce_shade:
    + Simulates the tree providing shade calculating and printing the shade area.
def get_info:
    + Returns the trees information.
"""
class Tree(Plant):
    def __init__(self, name, height, days, trunk_diameter):
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = self.trunk_diameter * 2
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self):
        return f"\n{self.base_info('Tree')}, {self.trunk_diameter}cm diameter"


"""
Represents a vegetable, subclass of Plant, with an additional attribute:
    harvest_season (str): season in which the vegetable is harvested.
    nutritional_value (str): nutritional benefit of the vegetable.

def __init__:
    + Initializes a Vegetable instance.
def get_info:
    + Returns the vegetables information.
"""
class Vegetable(Plant):
    def __init__(self, name, height, days, harvest_season, nutritional_value):
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        return (
            f"\n{self.base_info('Vegetable')}, {self.harvest_season} harvest"
        )


# Lists of different plant types (flowers, trees, vegetables)
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

# Displays flowers info and triggers bloom()
for flower in flowers:
    print(f"{flower.get_info()}")
    flower.bloom()

# Displays trees info and triggers produce_shade()
for tree in trees:
    print(f"{tree.get_info()}")
    tree.produce_shade()

# Displays vegetables info and nutritional value
for vegetable in vegetables:
    print(f"{vegetable.get_info()}")
    print(f"{vegetable.name} is rich in {vegetable.nutritional_value}")

