"""
CP1404 Practical
Playing The Guitars (not really :) )
"""
from prac_06.guitar import Guitar

guitars = []

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print(f"{new_guitar} added.")
    name = input("Name: ")

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage = ""
    if guitar.is_vintage():
        vintage = "(vintage)"
    print(f"Guitar {i} = {guitar.name} ({guitar.year}), worth $ {guitar.cost} {vintage}")
