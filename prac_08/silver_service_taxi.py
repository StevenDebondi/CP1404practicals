"""
CP1404/CP5632 Practical
Silver Service Taxi
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A variation of the Taxi Class"""

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness = 0.0):
        """Initialize a Silver Service Taxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string for the fare with added flagfall"""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Get the current fare + flagfall"""
        return self.flagfall + super().get_fare()
