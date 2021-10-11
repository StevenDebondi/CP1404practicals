"""
CP1404 Practical
Unreliable Car Class
"""

from random import randint
from car import Car


class UnreliableCar(Car):
    """Specialized version a Car that is unreliable"""

    def __init__(self, name, fuel, reliability):
        """Initialize an Unreliable Car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car dependant on reliability"""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0

        distance_driven = super().drive(distance)
        return distance_driven
