"""
CP1404 Practical
Taxi Test
"""
from taxi import Taxi


def main():
    """Testing the Taxi Class"""
    my_taxi = Taxi("Prius 1", 100, 1.23)
    my_taxi.drive(40)
    print(my_taxi, my_taxi.get_fare())
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi, my_taxi.get_fare())


main()
