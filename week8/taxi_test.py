from Prac08.taxi import Taxi

newTaxi = Taxi("Prius 1", 100)
newTaxi.drive(40)
print(newTaxi)
print("Your fare: ${:.2f}".format(newTaxi.get_fare()))
newTaxi.start_fare()
newTaxi.drive(100)
print(newTaxi)
print("Your fare: ${:.2f}".format(newTaxi.get_fare()))