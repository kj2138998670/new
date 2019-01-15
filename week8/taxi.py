"""
CP1404/CP5632 Practical
Car class
"""
from Prac08.car import Car

class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.20 # 1.23
    current_fare_distance = 0
    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(),
                                                             Taxi.current_fare_distance,
                                                             Taxi.price_per_km)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return Taxi.price_per_km * Taxi.current_fare_distance

    def start_fare(self):
        """Begin a new fare."""
        Taxi.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        Taxi.current_fare_distance += distance_driven
        return distance_driven