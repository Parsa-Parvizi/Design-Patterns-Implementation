"""create an abstract class called spaceship which will simulate a spaceship for a video game.
a) you can assume such simple properties as: i: position, size, displayName, speed.
b) create a number of concrete classes such as:
i: MilleniumFalcon ii: UNSCInfinity iii: USSEnterprise iv: Serenity
c. Using the Simple Factory Method create a factory implementation that will create each of these instances.
"""
from abc import ABC, abstractmethod


class Spaceship(ABC):
    def __init__(self, position, size, display_name, speed):
        self.position = position
        self.size = size
        self.display_name = display_name
        self.speed = speed

    @abstractmethod
    def fly(self):
        pass

    def __str__(self):
        return f"{self.display_name} at {self.position} with size {self.size} and speed {self.speed}"


class MilleniumFalcon(Spaceship):
    def __init__(self, position):
        super().__init__(position, size=34.75, display_name="Millennium Falcon", speed=1050)

    def fly(self):
        print(f"{self.display_name} is flying at speed {self.speed}.")


class UNSCInfinity(Spaceship):
    def __init__(self, position):
        super().__init__(position, size=1.2, display_name="UNSC Infinity", speed=500)

    def fly(self):
        print(f"{self.display_name} is flying at speed {self.speed}.")


class USSEnterprise(Spaceship):
    def __init__(self, position):
        super().__init__(position, size=300, display_name="USS Enterprise", speed=1000)

    def fly(self):
        print(f"{self.display_name} is flying at speed {self.speed}.")


class Serenity(Spaceship):
    def __init__(self, position):
        super().__init__(position, size=25, display_name="Serenity", speed=800)

    def fly(self):
        print(f"{self.display_name} is flying at speed {self.speed}.")


class SpaceshipFactory:
    @staticmethod
    def create_spaceship(spaceship_type, position):
        if spaceship_type == "MillenniumFalcon":
            return MilleniumFalcon(position)
        elif spaceship_type == "UNSCInfinity":
            return UNSCInfinity(position)
        elif spaceship_type == "USSEnterprise":
            return USSEnterprise(position)
        elif spaceship_type == "Serenity":
            return Serenity(position)
        else:
            raise ValueError(f"Unknown spaceship type: {spaceship_type}")


# Example usage
if __name__ == "__main__":
    # Create instances of different spaceships
    falcon = SpaceshipFactory.create_spaceship("MillenniumFalcon", (0, 0))
    infinity = SpaceshipFactory.create_spaceship("UNSCInfinity", (10, 10))
    enterprise = SpaceshipFactory.create_spaceship("USSEnterprise", (20, 20))
    serenity = SpaceshipFactory.create_spaceship("Serenity", (30, 30))

    # Display spaceship information and simulate flying
    for spaceship in [falcon, infinity, enterprise, serenity]:
        print(spaceship)
        spaceship.fly()


# Abstract Class (Spaceship):
# This class defines the basic properties and an abstract method fly() that must be implemented by any concrete spaceship class.

# Concrete Classes:
# Each spaceship class (e.g., MilleniumFalcon, UNSCInfinity, etc.) inherits from Spaceship and implements the fly() method.
# Each class has its own constructor that initializes the spaceship's properties.

# Factory Class (SpaceshipFactory):
# This class contains a static method create_spaceship() that takes a spaceship_type and a position as arguments.
# It returns an instance of the corresponding spaceship class based on the type provided.

# Example Usage:
# The main block demonstrates how to create instances of different spaceships using the factory and how to display their information and simulate their flying behavior.
