"""
CP1404/CP5632 Practical
Silver Service Taxi
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Testing the SilverServiceTaxi Class"""
    my_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    my_taxi.drive(18)
    print(my_taxi, f"for a total of ${my_taxi.get_fare():.2f}")


main()
