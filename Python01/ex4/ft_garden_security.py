#!/usr/bin/env python3

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

plant.set_height(25)
plant.set_age(30)

plant.set_height(-5)

print(f"\n{plant.get_info()}")
