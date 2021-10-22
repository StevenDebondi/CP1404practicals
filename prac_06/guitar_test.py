"""
CP1404 Practical
Guitar Tests
"""

from prac_06.guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

guitar = Guitar(name, year, cost)
another_guitar = Guitar("Guitar", 2013, 600)

print(f"{guitar.name}, is {guitar.get_age()} years old, expected 99")
print(f"{another_guitar.name} is {another_guitar.get_age()} years old, expected 8")

print(f"{guitar.name} is vintage: {guitar.is_vintage()}, expected True")
print(f"{another_guitar.name} is vintage: {another_guitar.is_vintage()}, expected False")
