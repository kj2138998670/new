from Prac08.taxi import Taxi
from Prac08.SilverServiceTaxi import SilverServiceTaxi

def main():
    MENU = "q)uit, c)hoose taxi, d)rive"

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    trip_cost = 0
    total_distance = 0
    taxi_choice = ""

    print("Let's drive!")
    print(MENU)
    user_choice = input(">>> ").lower()

    while user_choice != "q":

        if user_choice == "c":
            valid_input = False
            while not valid_input:
                try:
                    print("Taxis available:")
                    get_taxi_menu(taxis)
                    taxi_choice = int(input("Choose taxi: "))
                    if taxi_choice <= len(taxis) - 1:
                        valid_input = True
                    else:
                        print("Not a valid choice")
                except:
                    print("Not a valid number")

            print("{} selected.".format(taxis[taxi_choice]))
            print("Bill to date: ${:.2f}    Distance driven: {}Km".format(trip_cost, total_distance))
            print(MENU)
            user_choice = input(">>> ").lower()

        elif user_choice == "d" and taxi_choice == "":
            print("No taxi selected")
            print(MENU)
            user_choice = input(">>> ").lower()

        elif user_choice == "d" and taxi_choice != "":
            valid_input = False
            while not valid_input:
                try:
                    distance = int(input("Drive how far? "))
                    valid_input = True
                except:
                    print("Not a valid number.")
            taxis[taxi_choice].start_fare()
            km_driven = taxis[taxi_choice].drive(distance)
            total_distance += km_driven
            trip_cost += taxis[taxi_choice].get_fare()
            print("Your {}Km {} trip cost you ${:.2f}".format(km_driven, taxis[taxi_choice],
                                                              taxis[taxi_choice].get_fare()))
            print("Bill to date: ${:.2f}    Distance driven: {}Km".format(trip_cost, total_distance))
            print(MENU)
            user_choice = input(">>> ").lower()

        else:
            print("Not a valid choice")
            print(MENU)
            user_choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f} & distance driven {}Km".format(trip_cost, total_distance))
    print("Taxis are now:")
    get_taxi_menu(taxis)

def get_taxi_menu(taxis_list):
    index = 0
    for taxi in taxis_list:
        print("{} - {}".format(index, taxi))
        index += 1

main()
