#!/usr/bin/env python3

"""
Represents a plant with secure attributes for height and age, 
prevents invalid changes through setter methods.
Atributes:
    name (str): name of the plant, first letter capitalized.
    __height (int): height of the plant in centimeters (private attribute).
    __days (int): age of the plant in days (private attribute).

def __init__:
    + Initializes a SecurePlant with given name, height and age.
def get_height:
    + Retrieves the current height of the plant.
def get_age:
    + Retrieves the current age of the plant.
def get_info:
    + Returns the current information of the plant.
def set_height:
    + Updates the plants height if the value is non-negative.
    + If the height is negative an error message is displayed.
def set_age:
    + Updates the plants age if the value is non-negative.
    + If the age is negative an error message is displayed.
"""
class SecurePlant:
    def __init__(self, name, height, days):
        self.name = name.capitalize()
        self.__height = height
        self.__days = days
        print(f"Plant created : {self.name}")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__days

    def get_info(self):
        return (
            f"Current plant: {self.name} "
            f"({self.get_height()}cm, {self.get_age()} days)"
        )

    def set_height(self, height):
        if height < 0:
            print(
                "\nInvalid operation attempted: "
                f"height {height}cm [REJECTED]"
            )
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, days):
        if days < 0:
            print(f"\nInvalid operation attempted: age {days} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__days = days
            print(f"Age updated: {self.__days} days [OK]")


print("=== Garden Security System ===")

plant = SecurePlant("Rose", 20, 30)

# Updating valid attributes
plant.set_height(25)
plant.set_age(30)

# Testing invalid values
plant.set_height(-5)

# Shows the plants final information
print(f"\n{plant.get_info()}")

