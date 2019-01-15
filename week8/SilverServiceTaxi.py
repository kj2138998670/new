from Prac08.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        return super().get_fare() * self.fanciness + SilverServiceTaxi.flagfall

    def __str__(self):
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(super(Taxi, self).__str__(),
                                                      Taxi.current_fare_distance, self.price_per_km, SilverServiceTaxi.flagfall)