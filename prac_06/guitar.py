"""
CP1404 Practical
Guitar Class
"""
CURRENT_YEAR = 2021
VINTAGE = 50


class Guitar:
    """Represents a Guitar Object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string of a Guitar"""
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Gets how old a Guitar is"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Gets if the Guitar is vintage or not"""
        return self.get_age() >= VINTAGE
