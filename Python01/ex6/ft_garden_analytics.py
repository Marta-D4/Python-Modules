#!/usr/bin/env python3

"""
Represents a plant that can grow over time, with the attributes:
    name (str): name of the plant, first letter capitalized.
    height (int): height of the plant in centimeters.
    
def __init__ :
    + Initializes a Plant instance.
def grow:
    + Increases by 1cm a plants height.
def get_info:
    + Returns a plants basic information.
"""
class Plant:
    def __init__(self, name, height):
        self.name = name.capitalize()
        self.height = height

    def grow(self):
        self.height += 1

    def get_info(self):
        return f"- {self.name}: {self.height}cm"


"""
Represents a flowering plant, subclass of Plant, with an additional attribute:
    color (str): color of the flower.
    
def __init__:
    + Initializes a FloweringPlant.
def get_info: 
    + Returns a flowering plants information, with its color.
"""
class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def get_info(self):
        return f"{super().get_info()}, {self.color} flowers (blooming)"


"""
Represents a prize-winning flowering plant, subclass of FloweringPlant, 
with an additional attribute:
    prize_points (int): number of prize points aerned by the flower.
def __init__:
    + Initializes a PrizeFlower.
def get_info: 
    + Returns a prize flower plants information, with its prize points.
"""
class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self):
        return f"{super().get_info()}, Prize points: {self.prize_points}"


"""
Manages multiple gardens, each with its own plants and statistics.
    gardens (dic): dictionary that holds all created gardens.
    total_gardens (int): total number of gardens managed.
    
def __init__:
    + Initializes a GardenManager instance.
def add_plant:
    + Adds a plant to the garden and updates the garden stats.
def grow_all:
    + Helps all plants in the garden grow 1cm.
def report:
    + Prints a report of the gardens plants and stats.
def validate height:
    + Validates the height given.
def create_garden_network:
    + Returns a list of all the names of the gardens managed.
def resume_scores:
    + Prints the total number of gardens and its total points.
"""
class GardenManager:
    gardens = {}
    total_gardens = 0

    """
    Tracks stats for an specific garden, including plant types and growth.
        total_growth (int): total growth in cm of all plants in the garden.
        regular (int): number of regular plants in the garden.
        flowering (int): number of flowering plants in the garden.
        prize (int): number of prize-winnning plants in the garden.
        points (int): total of prize points of a garden.

    def __init__:
        + Initializes the garden statistics.
    def report:
        + Prints a report of the garden stats.
    """
    class GardenStats:
        def __init__(self):
            self.total_growth = 0
            self.regular = 0
            self.flowering = 0
            self.prize = 0
            self.points = 0

        def report(self):
            print(
                f"\nPlants added: {self.regular + self.flowering + self.prize}"
                f", Total growth: {self.total_growth}cm"
            )
            print(
                f"Plant types: {self.regular} regular, {self.flowering} "
                f"flowering, {self.prize} prize flowers"
            )

    def __init__(self, name):
        self.name = name.capitalize()
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.gardens[self.name] = self
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        if isinstance(plant, PrizeFlower):
            self.stats.prize += 1
            self.stats.points += plant.prize_points
        elif isinstance(plant, FloweringPlant):
            self.stats.flowering += 1
        else:
            self.stats.regular += 1
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self):
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.total_growth += 1
            print(f"{plant.name} grew 1cm")

    def report(self):
        print(f"\n=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.get_info())
        self.stats.report()

    @staticmethod
    def validate_height(height):
        if height > 0:
            print("\nHeight validation test: True")
        else:
            print("\nHeight validation test: False")

    @classmethod
    def create_garden_network(cls):
        return list(cls.gardens.keys())

    @classmethod
    def resume_scores(cls):
        print("Garden scores -", end=" ")
        for garden in cls.gardens.values():
            print(f"{garden.name}: {garden.stats.points}", end="  ")
        print(f"\nTotal gardens managed: {cls.total_gardens}")


print("=== Garden Management System Demo ===\n")

# Creating gardens
alice = GardenManager("Alice")
bob = GardenManager("bob")

# Adding plants
alice.add_plant(Plant("Oak Tree", 100))
alice.add_plant(FloweringPlant("Rose", 25, "red"))
alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

# Growing and reporting the stats
alice.grow_all()
alice.report()

# Updating the prize points of the gardens
alice.stats.points += 208
bob.stats.points += 92

# Validating a height value
GardenManager.validate_height(10)

# Displays all gardens scores
GardenManager.resume_scores()

