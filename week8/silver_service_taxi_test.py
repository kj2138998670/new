from Prac08.SilverServiceTaxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Hummer", 200, 2)
taxi.drive(18)
print(taxi)
print("Your fare: ${:.2f}".format(taxi.get_fare()))