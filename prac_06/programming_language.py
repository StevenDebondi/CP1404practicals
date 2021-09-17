"""
CP1404 Practical
Programming Language Class
"""


class ProgrammingLanguage:
    """Represent a Programming Language"""

    def __init__(self, name, typing, reflection, year):
        """Make a ProgrammingLanguage from the given variables"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Returns a string of the given ProgrammingLanguage"""
        return "{}, {}, Reflection={}, First appeared in {}".format(self.name,self.typing, self.reflection, self.year )

    def is_dynamic(self):
        """Determine if a given variable is dynamic"""
        return self.typing == "Dynamic"

