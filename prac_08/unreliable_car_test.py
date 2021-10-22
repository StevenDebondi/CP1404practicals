"""
CP1404 Practical
Unreliable Car Test
"""
from unreliable_car import UnreliableCar


def main():
    """Testing the UnreliableCar Class"""
    my_unreliable_car = UnreliableCar("FIAT", 100, 40)
    my_reliable_car = UnreliableCar("Ferrari", 100, 95)
    for i in range(1, 10):
        print(f"Driving {i}")
        print(f"{my_unreliable_car.name} drove {my_unreliable_car.drive(i)}")
        print(f"{my_reliable_car.name} drove {my_reliable_car.drive(i)}")
    print(my_reliable_car)
    print(my_unreliable_car)


main()
