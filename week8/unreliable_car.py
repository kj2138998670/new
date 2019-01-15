from Prac08.car import Car
import random

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        randomChance = random.randint(0, 100)
        print(randomChance)
        if randomChance < self.reliability:
            return super().drive(distance)
        else: return 0
